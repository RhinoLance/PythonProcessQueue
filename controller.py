import atexit
import time
import Config
import subprocess
import threading
from Triggers import Interval
from Utilities import Communicator
from os.path import abspath, dirname, join

import ast
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading
from threading import Timer

currentValues = {'Interval':0, 'AllImagesInDirectory':0}
timeSeries = []
totalAr = []
queueAr = []
timeSeriesCount = 0

def initChart():

	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	ax2 = fig.add_subplot(1,1,1)

	def animate(i):
		ax1.clear()
		ax2.clear()
		ax1.plot(timeSeries,totalAr)
		ax2.plot(timeSeries,queueAr)

	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

#create a timed plotting action
def plot():
	global timeSeriesCount

	Timer(1, plot).start()
	#take the current values and add to the plot array.  We need to do it this way, as the data may come in at different rates.
	totalAr.append(currentValues['Interval'])
	queueAr.append(currentValues['AllImagesInDirectory'])
	timeSeries.append(timeSeriesCount)
	timeSeriesCount += 1

	#remove the old data, as we only want to watch the last 100 readings.
	while len(timeSeries) > 100:
		totalAr.pop(0)
		queueAr.pop(0)
		timeSeries.pop(0)

#Create a new thread for the chart, otherwise it blocks the rest of the process.
chartThread = threading.Thread(target=initChart, args = ())
chartThread.daemon = True
chartThread.start()
plot()

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

#define what to do when messages are received
def callback(data):
	print("{0}".format(data))

	if isinstance(data, dict):
		if data['id'] == 'Interval' or data['id'] == 'AllImagesInDirectory':
			try:
				currentValues[data['id']] = int(data['data'])
			except:
				None



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
