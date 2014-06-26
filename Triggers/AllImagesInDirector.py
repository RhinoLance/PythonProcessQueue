__author__ = 'Lance@conryclan.com'

import os
import re
import time

class AllImagesInDirectory:

	def ___init___(self, processor, config):
		self.running = False
		self.processor = processor
		self.config = config

	def start(self):
		self.running = True
		run()

	def stop(self):
		self.running = False

	def run(self):
		img_re = re.compile(r'.+\.(jpg|png|jpeg|tif|tiff|bmp)$', re.IGNORECASE)

		while self.running:
			fileList = []

			for fileName in os.listdir( self.config.src ):
				if img_re.match(fileName):
					fileList.append(os.path.join(self.config.src, fileName))

			while( len(fileList) > 0 ):

				file = fileList[0]

				self.processor.process(fileList[0])


		#sleep here, we don't want to go into a tight loop if there aren't any images to process
		time.sleep(0.1)