import threading

from multiprocessing.connection import Listener
from multiprocessing.connection import Client
from array import array

class RsClient:

	def __enter__(self):
		"""no init"""

	def __exit__(self, type=None, value=None, tb=None):

		#self.conn may not exist so expect that it may fail.
		try:
			self.conn.close()
		except:
			pass

	def start(self, host='localhost', port=8000, key='8457#$%^&3648'):

		address = (host, port)
		self.conn = Client(address)

	def send(self, data):
		try:
			self.conn.send(data)
		except:
			self.stop()

	def stop(self):
		self.conn.close()


class RsListener:
	def __enter__(self):
		return self

	def __exit__(self, type=None, value=None, tb=None):

		#self.listener may not exist so expect that it may fail.
		try:
			self.listener.close()
			self.conn.close()
		except:
			pass

	def start(self, callback, host='localhost', port=8000):

		self.callback = callback

		#Create a new thread for each listener, otherwise only one can run at a time.
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.listen, args = (host, port, self.stopEvent))
		self.thread.daemon = True
		self.thread.start()


	def listen(self, host, port, stopEvent):
		address = (host, port)
		self.listener = Listener(address, 'AF_INET' )
		self.conn = self.listener.accept()

		while( not stopEvent.is_set()):
			try:
				self.callback(self.conn.recv())
			except:
				self.stop()

	def stop(self):
		self.stopEvent.set()
		self.conn.close()
