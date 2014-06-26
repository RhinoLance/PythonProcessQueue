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
#commClient = Communicator.RsClient()
#commClient.start(Config.Config.config['server'], config['commsPort'])
#commClient.send('{0} process started'.format(id))

def getClass( module, config):

	print(config)
	#dynamically get the class reference.
	exec('from {0} import {1}'.format(module, config['name']))
	klass = __import__('{0}.{1}'.format( module, config['name']))
	return klass(config)

#because we have called the trigger name the same as the class name in the config, we can dynamically create the trigger.
trigger = getClass('Triggers', config['trigger'])

#because we have called the actor name the same as the class name in teh config, we can dynamically create the actor.
actor = getClass(Actors, config['actor'])

#now we hook them together, expecting that every trigger will have a start function, and every actor a perform function
trigger.start(actor.perform)

