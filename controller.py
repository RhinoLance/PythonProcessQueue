import atexit
import time
import Config
import subprocess
import threading
from Triggers import Interval
from Utilities import Communicator
from os.path import abspath, dirname, join

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
