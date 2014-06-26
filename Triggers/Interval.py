__author__ = 'Lance@rhinosw.com'

from threading import Timer

class Interval:

	def __init__(self, config, fProgress):
		self.running = False
		self.config = config
		self.rate = config['rate']
		self.triggerCount = 0
		self.fProgress = fProgress

	def start(self, callback):
		self.callback = callback
		self.running = True
		self.run()

	def stop(self):
		self.countdown.cancel()
		self.running = False

	def run(self):
		Timer(int(self.config['rate']), self.run).start()
		self.triggerCount +=1

		if self.callback != None:
			self.callback()

		if self.fProgress != None:
			self.fProgress(self.triggerCount)