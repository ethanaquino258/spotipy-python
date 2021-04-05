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

    results = client.current_user_top_artists(limit=50, time_range=timeRange[timePicker])
    
    artists = results['items']
    results = client.next(results)
    artists.extend(artists)

    print("the popularity metric ranges from 0-100, w/ 100 as the highest level of popularity attainable")
    
    for idx, item in enumerate(artists):
        artistObject = artists[idx]

        artist = artistObject['name']
        genres = artistObject['genres']
        followers = artistObject['followers']['total']
        popularity = artistObject['popularity']


        print(f'{idx + 1}. {artist}\nGenres: {genres}\nFollowers: {followers}\nPopularity: {popularity}\n')
    exit()

def followedArtists():
    client = authCode("user-follow-read")

    results = client.current_user_followed_artists()
    
    print("the popularity metric ranges from 0-100, w/ 100 as the highest level of popularity attainable")

    for idx, item in enumerate(results['artists']['items']):
        artistObject = results['artists']['items'][idx]

        artist = artistObject['name']
        genres = artistObject['genres']
        followers = artistObject['followers']['total']
        popularity = artistObject['popularity']

        print(f'{artist}\nGenres: {genres}\nFollowers: {followers}\nPopularity: {popularity}\n')

    # TODO figure out why leaving ['items'] out of enumerate causes idx to only reach 5 instead of 20, something to do  with enumerate()
    # for idx, item in enumerate(results['artists']):
    #     artist = results['artists']['items'][idx]['name']
    #     print(f'{idx}. {artist}')
    exit()