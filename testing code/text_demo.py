import http.client
import urllib.parse
import requests
import json

def read_channel(api_key,channel_id):
	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'feeds.json?api_key='+key
	print(url)


def main():
	return 0

if __name__ == "__main__":
    main()
