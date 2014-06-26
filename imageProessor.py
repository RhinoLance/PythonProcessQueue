__author__ = 'lance@rinosw.com'

import sys
import os
import re
import time
import logging

class imageProcesor:

	def __init__(self, defaultOutput='', actor=None):
		self.actor = actor

	def process(self, source, destination=None, config=None):

		if destination is None: destination = self.defaultOutput

		return self.actor.process( source, destination, config)


import scipy.misc
from skimage.io import imread
from skimage import filter
from threading import Timer


##############################################################################
### Start processing
##############################################################################

if len(sys.argv) != 3:
	print( "Usage processQueue <source> <target>" )
	print(len(sys.argv))
	exit()

src = sys.argv[1];
target = sys.argv[2];
img_re = re.compile(r'.+\.(jpg|png|jpeg|tif|tiff|bmp)$', re.IGNORECASE)
queueCount = 0;

initialize_logger('')
Timer(1, log).start()

while True:
	#fileList = os.listdir( src )
	fileList = []

	for fileName in os.listdir( src ):
		if img_re.match(fileName):
			fileList.append(os.path.join(src, fileName))

	queueCount = len(fileList)

	print(queueCount)

	if( len(fileList) > 0 ):

		file = fileList[0]

		try:
			srcPath = os.path.join(src, os.path.basename(file))
			destPath = os.path.join(target, os.path.basename(file))
			processFile(srcPath, destPath)
			os.remove(srcPath)

		except:
			print( "Error deleting")

	else:
		time.sleep(0.1)





