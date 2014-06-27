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
		#use the timer object to initiate a countdown, at which time the trigger is called.
		#The trigger also self resets each time as python doesn't appear to offer a repeating timer.
		Timer(int(self.config['rate']), self.run).start()
		self.triggerCount +=1

		if self.callback != None:
			#If a function was passed to the start method, call the function at the trigger.
			self.callback()

		if self.fProgress != None:
			#If a progress listener has been registered, call the listener function with the
			#number of times the trigger has been executed.
			self.fProgress(self.triggerCount)