import json
import pyen
class SongInfo:
    
    def __init__(self, apikey):
        self.en = pyen.Pyen(apikey)
    #returns True if load successful, false if load problematic.
    def loadInfo(self,ID):
        response = self.en.get('track/profile',id=ID,bucket='audio_summary')
        return response['track']['audio_summary']

