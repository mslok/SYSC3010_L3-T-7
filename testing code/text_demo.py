import http.client
import urllib.parse
import requests
import json

#my read api key 9SO0XFLPB59ODN5L
#my write key UU2HQ2WXR5L56DDK
#my channel id 1160858

#mikes read api key WQUCC93KDMBOY6V5
#mikes write api key OBGBKNICJSMTDX1G
#mikes channel id 1223588

#ambars read api key B4B863GDK58LVJGP
#amabrs channel id 1226682

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
	field=pull_data
	#print(field_1)
	
	total=0
	n=0
	
	print("Accelerometer readings:")
	
	for i in field['feeds']:
		temp=i['field1']
		print(temp)
		total=total+float(temp)
		n=n+1
	
	if n !=0:
		avg=total/n
		print("The average value is: " + str(avg))
	else: 
		print("No data to be anazlyzed, channel empty.")

def main():
	ret_json=read_channel('B4B863GDK58LVJGP','1226682')
	disp_text=json.dumps(ret_json, indent=4)
	print(disp_text)
	analyze_field('B4B863GDK58LVJGP','1226682','1')
	
	
if __name__ == "__main__":
    main()
