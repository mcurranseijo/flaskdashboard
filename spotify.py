import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth


class Spotify(object):
    def __init__(self):
        scope = "user-library-read user-read-currently-playing user-read-playback-state"
        self.song_data = {
            'artist': "n/a",
            'albumcover': "n/a",
            'track': "n/a",
            'album': "n/a"
        }
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def tracks(self):
        recent = self.sp.current_user_playing_track()
        print(recent)
        if recent == None:
            print("using old data")
            with open('nowPlaying.json') as f:
                self.song_data = json.load(f)
            return self.song_data
        else:
            self.song_data['artist'] = recent['item']['album']['artists'][0]['name']
            self.song_data['albumcover'] = recent['item']['album']['images'][0]['url']
            self.song_data['track'] = recent['item']['name']
            self.song_data['album'] = recent['item']['album']['name']
            print("using new data")
            with open('nowPlaying.json', 'w') as json_file:
                json.dump(self.song_data, json_file)
            return self.song_data

