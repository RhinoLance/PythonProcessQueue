__author__ = 'Lance'

import time
import sys
import Config
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

while True:
	commClient.send({'id':id, 'data': 'abc' })
	time.sleep(1)