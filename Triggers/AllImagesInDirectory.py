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
		#We only want to deal with image files, so create an 'image' regular expression
		img_re = re.compile(r'.+\.(jpg|png|jpeg|tif|tiff|bmp)$', re.IGNORECASE)

		while self.running:
			fileList = []

			#Get a list of files in the source directory
			for fileName in os.listdir( self.config['source'] ):
				#We only want to do something with the file if it matches the image reg exp.
				if img_re.match(fileName):
					#add the image file to the fileList array for later use.
					fileList.append(os.path.join(self.config['source'], fileName))

			#Now we go through all our image files
			while( len(fileList) > 0 ):
				#Get the first file, and remove from the list.
				file = fileList.pop(0)

				#Call the callback.  If it fails, make the process sleep for one second, otherwise
				#there is the potential to go into a tight loop, with little time for file locks to resolve themselves.
				if( not self.fCallback(file)):
					time.sleep(1)

				#If a progress listener has been registered, call the listener function with the
				#number of files that still need to be processed.
				if self.fProgress != None:
					self.fProgress(len(fileList))

		#sleep here, we don't want to go into a tight loop if there aren't any images to process
		time.sleep(0.2)