import http.client
import urllib.parse
import requests
import json
from pprint import pprint

#my read api key 9SO0XFLPB59ODN5L
#my write key UU2HQ2WXR5L56DDK
#my channel id 1160858

#mikes read api key WQUCC93KDMBOY6V5
#mikes write api key OBGBKNICJSMTDX1G
#mikes channel id 1223588

#simply prints channel data and feeds 
def read_channel(api_key,channel_id):
	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/feeds.json?api_key='+key+'&results=8000'
	
	pull_data=requests.get(url).json()
	
	return pull_data

def analyze_field(api_key,channel_id,field_id):
	key=api_key
	channel=channel_id
	num=field_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/field/'+num+ '.json?api_key='+key+'&results=8000'
	
	pull_data=requests.get(url).json()
	field_1=pull_data
	#print(field_1)
	
	total=0
	n=0
	
	print("Accelerometer readings:")
	
	for i in field_1['feeds']:
		temp=i['field1']
		print(temp)
		total=total+float(temp)
		n=n+1
	
	avg=total/n
	print("The average value is: " + str(avg))
	

def main():
	ret_json=read_channel('WQUCC93KDMBOY6V5','1223588')
	disp_text=json.dumps(ret_json, indent=4)
	print(disp_text)
	analyze_field('WQUCC93KDMBOY6V5','1223588','1')
	
	
if __name__ == "__main__":
    main()
