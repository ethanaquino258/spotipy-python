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
    try:
        results = client.current_user_top_tracks(time_range=timeRange[timePicker])
    except spotipy.client.SpotifyException as e:
        print("===CLIENT ERROR===")
        print(e)

    for idx, item in enumerate(results['items']):
        track = item['album']
        print(idx, track['artists'][0]['name'], " – ", item['name'])
    
    exit()

def savedTracks():
    client = authCode("user-library-read")
    results = client.current_user_saved_tracks()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    
    exit()

def currentTrack():
    client = authCode("user-read-playback-state")
    results = client.current_user_playing_track()

    print(results['item']['artists'][0]['name'], " - ", results['item']['name'])

    exit()


def recentlyPlayedTracks():
    client = authCode("user-read-recently-played")
    results = client.current_user_recently_played()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

    exit()

