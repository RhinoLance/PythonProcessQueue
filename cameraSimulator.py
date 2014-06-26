import sys
import os
import re
import time
import logging
import shutil
import glob

import scipy.misc
from skimage.io import imread
from skimage import filter
from threading import Timer

def process():

	Timer(sampleRate/1000, process).start()

	newFile = os.path.join( os.path.dirname(target), '{0}.jpeg'.format(time.time()))

	try:
		shutil.copyfile(src, newFile)
		print( 'added {0}'.format(os.path.basename(newFile)))
	except:
		print("Error copying")


##############################################################################
### Start processing
##############################################################################

if len(sys.argv) != 4:
	print( "Usage cameraSimulator <source> <target> <sample rate (milliseconds)>" )
	print(len(sys.argv))
	exit()

src = sys.argv[1]
target = sys.argv[2]
sampleRate = int(sys.argv[3])

Timer(1, process).start()

while True:
	#never exit
	time.sleep(1)


