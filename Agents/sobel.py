__author__ = 'Lance@rhinosw.com'

import scipy.misc
from skimage.io import imread
from skimage import filter

class Sobel:

	def process(self, src, dest, config):

		try:
			srcImg = imread(src, flatten=True)

			destImg = filter.sobel(srcImg)
			scipy.misc.imsave(dest, destImg)

			return True
		except:
			return False
