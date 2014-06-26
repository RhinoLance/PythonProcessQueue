__author__ = 'Lance'

class AgentRunner:

	def __init__(self, config):
		self.config = config

	def process(self, source):
		shutil.copy(source, self.config.dest)
