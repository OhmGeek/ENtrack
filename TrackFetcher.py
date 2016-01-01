import requests
import json

class TrackFetcher(object):
	
	def __init__(self, api_key):
		self.api_key = api_key

	def getInfo(self,ID):
		rawurl = "http://developer.echonest.com/api/v4/track/profile"

		#initialise parameters
		par = {}
		par["api_key"] = self.api_key
		par["id"] = ID
		par["format"] = "json"
		par["bucket"] = "audio_summary"

		#send get request and get JSON. Process this.
		r = requests.get(rawurl, params = par)
		trackInfo = r.json().get('response')
		if(trackInfo is not None):
			trackInfo = trackInfo.get('track')
			if(trackInfo is not None):
				trackInfo = trackInfo.get('audio_summary')
				if(trackInfo is not None):
					return trackInfo
		return None
