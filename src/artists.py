from authentication import authCode
import spotipy

def topArtists():
    client = authCode("user-top-read")

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

    results = client.current_user_top_artists(time_range=timeRange[timePicker])

    for idx, item in enumerate(results['items']):
        artist = results['items'][idx]['name']
        print(f'{idx}. {artist}')
    exit()

def followedArtists():
    client = authCode("user-follow-read")

    results = client.current_user_followed_artists()

    for idx, item in enumerate(results['artists']['items']):
        artist = results['artists']['items'][idx]['name']
        print(f'{idx}. {artist}')

    # TODO figure out why leaving ['items'] out of enumerate causes idx to only reach 5 instead of 20, something to do  with enumerate()
    # for idx, item in enumerate(results['artists']):
    #     artist = results['artists']['items'][idx]['name']
    #     print(f'{idx}. {artist}')
    exit()