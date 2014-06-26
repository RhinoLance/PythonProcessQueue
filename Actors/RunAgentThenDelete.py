__author__ = 'Lance'

import os

class RunAgentThenDelete:

	def __init__(self, agent, config):
		self.config = config
		self.agent = agent

	def process(self, src):
		self.agent.process(src, self.config.dest, None)
		os.remote(src)