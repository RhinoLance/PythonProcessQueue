__author__ = 'Lance@rhinosw.com'

from threading import Timer

class Interval:

	def __init__(self, processor, config):
		self.running = False
		self.processor = processor
		self.config = config

	def start(self):
		self.running = True
		self.run()

	def stop(self):
		self.countdown.cancel()
		self.running = False

	def run(self):
		Timer(self.config.rate, self.run).start()
		self.processor.process()