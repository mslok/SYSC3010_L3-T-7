import http.client
import urllib.parse
import time
import requests
import json 
import random 


#write_key = 'UU2HQ2WXR5L56DDK'
#https://api.thingspeak.com/channels/1160858/feeds.json?api_key=9SO0XFLPB59ODN5L&results=2

def read_channel_feed():
#Read data from all fields in a channel with HTTP GET
    read_key='9SO0XFLPB59ODN5L'
    url='https://api.thingspeak.com/channels/1160858/feeds.json?api_key='
    header='&results=2'

    url_ac=url + read_key + header

    print(url_ac)

def write_channel_feed():
	return 0

def read_channel_field():
	return 0

def read_channel_status():
	return 0

def main():
    read_channel_feed()
    

if __name__ == "__main__":

    main()



