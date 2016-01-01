# ENtrack
The Echonest Track Fetcher

This code interfaces with The Echo Nest to retrieve track information about a given track.

An instance of the TrackFetcher class requires an API key to be entered (obtained from The Echo Nest developer website), and once the instance has been created, one can call the getInfo method, with a string ID as a parameter, to return a dictionary containing the track information. Currently, the audio_summary is returned, rather than simply the track information.

Usage:

In order to get the information about a specific track (perhaps a track from Spotify), you need to create an instance of the TrackFetcher Class:

t = TrackFetcher('API KEY')

Now that the object has been created, we can use it to get a dictionary containing the informationa about a track:

info = t.getInfo('spotify:track:3zBhJBEbDD4a4SO1EaEiBP')

Here, info is a dictionary. We can select particular keys in the dictionary to obtain specific information:

print(info.get('danceability'))

This code prints the danceability of the song in question. This particular attribute is returned as a float, but other attributes will have different types, depending on the attribute queried.
