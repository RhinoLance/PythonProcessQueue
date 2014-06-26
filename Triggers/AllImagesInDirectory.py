__author__ = 'Lance@conryclan.com'

import os
import re
import time

class AllImagesInDirectory:

	def __init__(self, config, fProgress):
		self.running = False
		self.config = config
		self.fProgress = fProgress

	def start(self, fCallback):
		self.running = True
		self.fCallback = fCallback
		self.run()

	def stop(self):
		self.running = False

	def run(self):
		img_re = re.compile(r'.+\.(jpg|png|jpeg|tif|tiff|bmp)$', re.IGNORECASE)

		while self.running:
			fileList = []

			for fileName in os.listdir( self.config['source'] ):
				if img_re.match(fileName):
					fileList.append(os.path.join(self.config['source'], fileName))

			while( len(fileList) > 0 ):
				file = fileList.pop(0)

				if( not self.fCallback(file)):
					time.sleep(1)

				if self.fProgress != None:
					self.fProgress(len(fileList))

		#sleep here, we don't want to go into a tight loop if there aren't any images to process
		time.sleep(0.2)