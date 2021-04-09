from authentication import authCode
import spotipy
import random

def topArtists():
    client = authCode("user-top-read playlist-modify-public")

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

    print("the popularity metric ranges from 0-100, w/ 100 as the highest level of popularity attainable")
    
    idList =[]

    for idx, item in enumerate(artists):
        artistObject = artists[idx]
        
        artist = artistObject['name']
        genres = artistObject['genres']
        followers = artistObject['followers']['total']
        popularity = artistObject['popularity']
    
        print(f'{idx + 1}. {artist}\nGenres: {genres}\nFollowers: {followers}\nPopularity: {popularity}\n')
        
        idObject = {}
        idObject['artist'] = artist
        idObject['id'] = item['id']
        idList.append(idObject)
    
    createOption = input("Would you like to make a playlist? y/n\nNOTE: one random track from a random album in an artist's discography will be added per artist\n")

    if createOption == "y":
        playlistName = input("please enter a name for the playlist:\n")

        user = client.me()
        createResults = client.user_playlist_create(user['id'], playlistName)

        newPlaylistID = createResults['id']

        addTracks = []
        for artist in idList:
            artistName = artist['artist']

            albumResults = client.artist_albums(artist['id'],album_type='album',country=['US'],limit=50)

            if len(albumResults['items']) > 50:
                while albumResults['next']:
                    paginatedResults = client.next(results)
                    albumResults.append(paginatedResults)

            albumList = albumResults['items']
            if albumList == []:
                print(f'\nUnable to get data for artist {artistName}\n')
                searchResult = client.search(artistName,type='artist')
                print(searchResult)
                continue
            index = random.randint(0, (len(albumList)-1))
            chosenAlbum = albumList[index]['id']

            print(albumList[index]['available_markets'])

            albumTracks = client.album_tracks(chosenAlbum, limit=50)
            trackList = albumTracks['items']
            
            print("\n======track logic=====\n")
            print(artistName)
            print("# of albums")
            print(len(albumList))
            print(albumList[index]['total_tracks'])

            if albumList[index]['total_tracks'] > 50:
                paginatedTracks = client.next(albumTracks)
                trackList.extend(paginatedTracks['items'])

            index2 = random.randint(0, (len(trackList)-1))
            print()
            print(index2)
            chosenTrack = trackList[index2]['id']
            print(chosenTrack)
            client.user_playlist_add_tracks(user['id'], newPlaylistID, [chosenTrack])

            addTracks.append(chosenTrack)
            print("\n========DONE=========\n")

            # to stop random tracks from being added: add checks at the track level, if they fail break and retry (inefficient but works)
        print(addTracks)
        print(len(addTracks))
        # client.user_playlist_add_tracks(user['id'], newPlaylistID, addTracks)
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