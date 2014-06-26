__author__ = 'Lance@rhinosw.com'

from threading import Timer

class Interval:

	def __init__(self, config):
		self.running = False
		self.config = config

		self.rate = config['rate']

	def start(self, callback):
		self.callback = callback
		self.running = True
		self.run()

	def stop(self):
		self.countdown.cancel()
		self.running = False

	def run(self):
		Timer(self.config.rate, self.run).start()
		self.callback()