import random
import time
from Utilities import Communicator

from threading import Timer

#with Communicator.RsClient() as commClient:

commClient = Communicator.RsClient()

def log():
	commClient.send('abc')
	Timer(1, log).start()

commClient.start('localhost',8000)
#log()

while True:
	commClient.send("abc")
	time.sleep(random.randint(1,10)/100)
