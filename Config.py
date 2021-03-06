class Config:

	config = {
		'server': '127.0.0.1',
	    'processList':[
		    {
			    'id': 'captureImage',
			    'commsPort':18881,
		        'trigger': {
			        'name': 'Interval',
		            'rate': 0.5
		        },
		        'actor': {
			        'name': 'CopyLatest',
		            'source': 'c:\\users\\lance\\temp\\s1',
		            'target': 'c:\\users\\lance\\temp\\t1'
		        }
		    },
	        {
			    'id': 'processImage',
			    'commsPort':18882,
		        'trigger': {
			        'name': 'AllImagesInDirectory',
		            'source': 'c:\\users\\lance\\temp\\t1'
		        },
		        'actor': {
			        'name': 'RunAgentThenDelete',
		            'target': 'c:\\users\\lance\\temp\\t2',
		            'agent': {
			            'name': 'Sobel'
		            }
		        }
		    }
	    ]
	}

	def getProcess(self, id):

		for process in self.config['processList']:
			if process['id'] == id:
				return process


		return None