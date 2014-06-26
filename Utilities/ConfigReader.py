__author__ = 'Lance'

import xml.etree.cElementTree as et

class ConfigReader:
	def readFile(self, filePath):

		fo = open("foo.txt", "r+")
		str = fo.read()

		tree=et.fromstring(str)

		config = {
			'server': tree.find('server'),
		    'processList': []
		}

		for element in tree.findall('process'):
		    process = {
			    'commsPort': element.find('commsPort'),
		        'trigger': element.find('trigger').text
		    }

			if process['trigger'] == 'interval':



		print "\nan alternate way:"
		el=tree.find('file[2]/Name')  # xpath
		print '{:>15}: {:<30}'.format(el.tag, el.text)

		fo.close()