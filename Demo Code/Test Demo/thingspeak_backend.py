import http.client
import urllib.parse
import requests
import json

def getData(api_key,channel_id):
#Pulls data from an entire Thingspeak channel.
	
	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/feeds.json?api_key='+key+'&results=8000'
	
	pull_data=requests.get(url).json()
	
	return pull_data
	
def getField(tdata):
#Prints the field values in a feed

	pull_data=tdata
	feed='feeds'
	field='field1'
	
	for i in pull_data[feed]:
		temp=i[field]
		print(temp)
		
def getLast(api_key,channel_id):
#returns the latest entry in the thingspeak channel
	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/fields/field1/last.json?key='+key+'&results=8000'
	
	pull_data=requests.get(url).json()
	
	'https://api.thingspeak.com/channels/CHANNEL_ID/feeds/last?api_key'+key+'&results=1'

	return pull_data

def newSetting(api_key,channel_id,setting):
#writes a new car setting to the config thingspeak
	return 0
	i
def getAddress(lt,ln): 
#returns the street address of a set of coordinates
	latitude=lt
	longitude=ln
	
	URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
	api_key = 'QIb2IpsnEhXcnrbXrkTmErXA3PwNMTzUkX0HKdnuc4A'
	PARAMS = {
				'at': '{},{}'.format(latitude,longitude),
				'apikey': api_key
             }

	r = requests.get(url = URL, params = PARAMS)
	data = r.json() 

	for i in data['items']:
		temp=i['address']['label']
		return temp

def main():
	lat='45.3694076'
	lng='-75.7030896'
	x=getAddress(lat,lng)
	print(x)
if __name__ == "__main__":
	main()
