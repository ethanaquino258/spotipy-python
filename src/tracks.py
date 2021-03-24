from authentication import authCode
import spotipy

def topTracks():
    timePicker = input("""Please choose a time range 
        1. short-term
        2. medium-term
        3. long-term
    """)

    timeRange = {
        "1": "short_term",
        "2": "medium_term",
        "3": "long_term"
    }

    client = authCode("user-top-read")

    results = client.current_user_top_tracks(time_range=timeRange[timePicker])

    for idx, item in enumerate(results['items']):
        trackObject = item['album']

        artist = trackObject['artists'][0]['name']
        songName = item['name']

        print(f'{idx + 1}. {artist} - {songName}')
    
    exit()

def savedTracks():
    client = authCode("user-library-read")
    results = client.current_user_saved_tracks()

    for item in results['items']:
        trackObject = item['track']

        songName = trackObject['name']
        artist = trackObject['artists'][0]['name']

        print(f'{artist} - {songName}')
    
    exit()

def currentTrack():
    client = authCode("user-read-playback-state")
    results = client.current_user_playing_track()

    trackObject = results['item']

    artist = trackObject['artists'][0]['name']
    songName = trackObject['name']

    print(f'{artist} - {songName}')

    exit()


def recentlyPlayedTracks():
    client = authCode("user-read-recently-played")
    results = client.current_user_recently_played()

    for item in results['items']:
        trackObject = item['track']

        artist = trackObject['artists'][0]['name']
        songName = trackObject['name']

        print(f'{artist} - {songName}')

    exit()

