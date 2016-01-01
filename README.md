# ENtrack
The Echonest Track Fetcher

This code interfaces with The Echo Nest to retrieve track information about a given track.

An instance of the TrackFetcher class requires an API key to be entered (obtained from The Echo Nest developer website), and once the instance has been created, one can call the getInfo method, with a string ID as a parameter, to return a dictionary containing the track information. Currently, the audio_summary is returned, rather than simply the track information.
