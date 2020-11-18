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
	
def getField(tdata,fnum):
#Prints the field values in a feed
	txt=fnum
	pull_data=tdata
	feed='feeds'
	field='field'+'{}'.format(txt)
	
	for i in pull_data[feed]:
		temp=i[field]
		print(temp)
		
def getLast(api_key,channel_id):
#returns the latest entry in the thingspeak channel
	
	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/fields/field1/last.json?				   key='+key+'&results=8000'
	
	pull_data=requests.get(url).json()
	
	'https://api.thingspeak.com/channels/CHANNEL_ID/feeds/last?api_key'+key+'&results=1'

	return pull_data

def newSetting(api_key,channel_id,param):
#writes a new car setting to the config thingspeak
	
	setting=param
	key=api_key
	channel=channel_id
	
	update='&field4={}'.format(setting)
	url='https://api.thingspeak.com/update?api_key='+key+update
	
	data=urllib.request.urlopen(url)
	return data
	
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

def combine(api_key,channel_id):
	return(0)

def main():
	x=getData('9SO0XFLPB59ODN5L','1160858')
	y=getField(x,'4')
	print(y)
if __name__ == "__main__":
	main()
