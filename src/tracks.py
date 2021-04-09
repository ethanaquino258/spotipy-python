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

    client = authCode("user-top-read playlist-modify-public")

    results = client.current_user_top_tracks(limit=50,time_range=timeRange[timePicker])

    tracks = results['items']

    uriList = []

    for idx, item in enumerate(tracks):
        uriList.append(item['uri'])
        trackObject = item['album']

        artist = trackObject['artists'][0]['name']
        songName = item['name']

        print(f'{idx + 1}. {artist} - {songName}')
    
    createOption = input("would you like to make this a playlist? y/n\n")

    if createOption == "y":
        playlistName = input("please enter a name for the playlist:\n")

        user = client.me()
        createResults = client.user_playlist_create(user['id'], playlistName)

        newPlaylistID = createResults['id']

        client.user_playlist_add_tracks(user['id'], newPlaylistID, uriList)

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

