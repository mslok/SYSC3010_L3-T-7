import http.client
import urllib.parse
import time
import requests
import json 
import random 

#https://api.thingspeak.com/channels/1160858/feeds.json?api_key=9SO0XFLPB59ODN5L&results=2

def read_channel_feed():
#Read data from all fields in a channel with HTTP GET
    read_key='9SO0XFLPB59ODN5L'
    url='https://api.thingspeak.com/channels/1160858/feeds.json?api_key='
    header='&results=2'
    url_ac=url+read_key+header
    print(url_ac)

    pull_data=requests.get(url_ac).json()
    print(json.dumps(pull_data, indent = 4))

def write_channel_feed():
    update='&field1={}&field2={}&field3={}'.format(7.0,8.0,9.0)
#Update channel data with HTTP GET or POST
    write_key='UU2HQ2WXR5L56DDK'
    url='https://api.thingspeak.com/update?api_key='
#write custom header parse later 
    header=update
    url_ac=url + write_key + header
    print(url_ac)

    data=urllib.request.urlopen(url_ac)
    print(data)

#need to add try and catch logic for read and write error response (200)
def read_channel_field():
    read_key='9SO0XFLPB59ODN5L'
    url='https://api.thingspeak.com/channels/1160858/fields/3.json?api_key='
    header='&results=2'
    url_ac=url+read_key+header
    print(url_ac)

    pull_data=requests.get(url_ac).json()
    channel_id=pull_data['channel']['id']
    print(channel_id)
    
    field_1=pull_data['feeds']
    print(json.dumps(field_1, indent=4))

    
def read_channel_status():
	return 0

def main():
    write_channel_feed()
    read_channel_feed()
    read_channel_field()


if __name__ == "__main__":
    main()



