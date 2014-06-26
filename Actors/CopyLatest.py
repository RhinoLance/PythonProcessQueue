__author__ = 'Lance'

import glob
import os
import shutil

class CopyLatest:

	def __init__(self, config, callback):
		self.config = config
		self.source = config['source']
		self.target = config['target']
		self.callback = callback

	def perform(self):
		try:
			srcPath = max(glob.iglob(os.path.join(self.source, '*')), key=os.path.getctime)
		except:
			return

		destPath = os.path.join(self.target, os.path.basename(srcPath))

		self.log( "Processing " + os.path.basename(srcPath) )

		try:
			shutil.copyfile(srcPath, destPath)
		except:
			self.log( "error" )

	def log(self, data):
		if self.callback != None:
			self.callback(data)
