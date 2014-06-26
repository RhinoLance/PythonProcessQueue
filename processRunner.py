__author__ = 'Lance'

import time
import sys
import Config
import Triggers
import Actors
from Utilities import Communicator


id = sys.argv[1]

#load the config
config = Config.Config().getProcess(id)
if config == None:
	exit

#set up the communicator that will be used to pass messages back to the controller process.
commClient = Communicator.RsClient()
commClient.start(Config.Config.config['server'], config['commsPort'])
commClient.send('{0} process started'.format(id))

def getClass( module, config, callback):

	#dynamically get the class reference.
	#exec('from {0} import {1}'.format(module, config['name']))
	#klass = __import__('{0}.{1}'.format( module, config['name']))

	mod = __import__('{0}.{1}'.format(module, config['name']), fromlist=[config['name']])
	klass = getattr(mod, config['name'])

	return klass(config, callback)

#define the function to run when the trigger reports progress
triggerCount = 0
def triggerCallback(data):
	global triggerCount, commClient
	triggerCount += 1
	commClient.send({'id': config['trigger']['name'], 'data': data})

#because we have called the trigger name the same as the class name in the config, we can dynamically create the trigger.
trigger = getClass('Triggers', config['trigger'], triggerCallback)

#define the function to run when the actor reports progress
actorCount = 0
def actorCallback(data):
	global actorCount, commClient
	actorCount += 1
	commClient.send({'id': config['actor']['name'], 'data': data})

#because we have called the actor name the same as the class name in teh config, we can dynamically create the actor.
actor = getClass('Actors', config['actor'], actorCallback)

#now we hook them together, expecting that every trigger will have a start function, and every actor a perform function
trigger.start(actor.perform)

