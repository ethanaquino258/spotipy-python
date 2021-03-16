def topTracks(client):
    print("====TOP====")
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

    print(timeRange)
    print(timeRange[timePicker])

    results = client.current_user_top_tracks(time_range=timeRange[timePicker])

    for idx, item in enumerate(results['items']):
        track = item['album']
        print(idx, track['artists'][0]['name'], " – ", item['name'])
    
    return

def savedTracks(client):
    print("====SAVED====")
    results = client.current_user_saved_tracks()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    
    return

def currentTrack(client):
    print("current track")


def recentlyPlayedTracks(client):
    results = client.current_user_recently_played()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

