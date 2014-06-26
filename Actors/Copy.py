__author__ = 'Lance'

import shutil

class Copy:

	def __init__(self, config):
		self.config = config

	def process(self, source):
		shutil.copy(source, self.config.dest)
