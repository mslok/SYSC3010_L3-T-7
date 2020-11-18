import requests
import json
#45.3694076', 'field3': '-75.7030896
# api-endpoint
URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"

#API key
api_key = 'QIb2IpsnEhXcnrbXrkTmErXA3PwNMTzUkX0HKdnuc4A'

latitude='45.3694076'
longitude='-75.7030896'

# Defining a params dictionary for the parameters to be sent to the API 
PARAMS = {
			'at': '{},{}'.format(latitude,longitude),
			'apikey': api_key
         }

# Sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# Extracting data in json format 
data = r.json() 

#Taking out title from JSON

y=json.dumps(data, indent=4)

print(y)
