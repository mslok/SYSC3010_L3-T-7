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
def getAddress(): 
	return 0

def readFile():
	return 0

def main():
	x=getSetting('WQUCC93KDMBOY6V5','1223588')
	print(x)
if __name__ == "__main__":
	main()
