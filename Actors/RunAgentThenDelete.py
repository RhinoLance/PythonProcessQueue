__author__ = 'Lance'

import os
import time

class RunAgentThenDelete:

	def __init__(self, config, fProgress):
		self.config = config
		self.fProgress = fProgress

		#get the agent
		mod = __import__('{0}.{1}'.format('Agents', config['agent']['name']), fromlist=[config['agent']['name']])
		klass = getattr(mod, config['agent']['name'])

		self.agent = klass()
		self.target = config['target']

	def perform(self, srcPath):

		destPath = os.path.join(self.target, os.path.basename(srcPath))

		self.log( "Processing " + os.path.basename(srcPath) )

		try:
			#execute the agent against the file
			self.agent.process( srcPath, destPath, {})
			os.remove(srcPath)

		except:
			self.log('error')
			return False

		return True

	def log(self, data):
		if self.fProgress != None:
			self.fProgress(data)