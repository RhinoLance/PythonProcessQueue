import atexit
import time
import Config
import subprocess
import threading
from Triggers import Interval
from Utilities import Communicator
from os.path import abspath, dirname, join

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

xar = [3,4,5,6,7,8,9]
yar = [8,7,2,4,3,6,7]

def initChart():

	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)

	def animate(i):
		ax1.clear()
		ax1.plot(xar,yar)

	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

#Create a new thread for the chart, otherwise it blocks the rest of the process.
chartThread = threading.Thread(target=initChart, args = ())
chartThread.daemon = True
chartThread.start()

#load the config
config = Config.Config.config
print(config)

listenerDict = {}  #collection of comms listeners
processDict = {}  #collection of processes, so that we can stop them later.

#create a cleanup function for any processes and threads
def cleanup():
	for listener in listenerDict:
		#stop the listener
		listener.stop()

	for process in processDict:
		#terminate the process
		subprocess.Popen.terminate(process)


atexit.register(cleanup)
count = 1

#define what to do when messages are received
def callback(data):
	global count
	print("{0}".format(data))
	xar.append(5+ count)
	yar.append(5+ count)
	count +=1

#let's set up each process from the config
for process in config['processList']:
	id = process['id']

	#set up the communicator that will be used to pass messages back to the controller process.
	listenerDict[id] = Communicator.RsListener()
	listenerDict[id].start(callback, config['server'], process['commsPort'])
	print('{}: listening'.format(id))

	#run the process
	path = abspath(join(dirname(__file__), 'processRunner.py'))
	processDict[id] = subprocess.Popen( ['python', path, id] )
	print( '{0} state: {1}'.format( id, processDict[id]))

while True:
	time.sleep(1)
