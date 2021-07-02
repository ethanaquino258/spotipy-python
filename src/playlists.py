from authentication import authCode
import spotipy
import csv

def userPlaylists():
    client = authCode("playlist-read-private")

    results = client.current_user_playlists()

    while results['next']:
        results = client.next(results)
        playlists = results['items']
        for idx, item in enumerate(playlists):
            playlistObject = results['items'][idx]

            id = playlistObject['id']
            collaborative = playlistObject['collaborative']
            playlistName = playlistObject['name']
            creator = playlistObject['owner']['id']

            print(f'ID: {id}\nName: {playlistName}\nCreator: {creator}\nCollaborative: {collaborative}\n')
            print(f'Total Playlists: {idx}')
    exit()

# for some reason the current user playlist functionality is not getting every playlist I have, most noticeably 'top songs' and 'great songs'.
# could be the pagination, could be the spotify api itself, could be me
# clean this up another time
def writeToCSV():
    client = authCode("playlist-read-private")

    results = client.current_user_playlists()

    playlistDict = []

    while results['next']:
        results = client.next(results)
        playlists = results['items']
        for idx, item in enumerate(playlists):
            playlistObject = results['items'][idx]

            id = playlistObject['id']
            collaborative = playlistObject['collaborative']
            playlistName = playlistObject['name']
            creator = playlistObject['owner']['id']
            
            playlistItem = {'id': id, 'playlist name': playlistName, 'creator': creator, 'collaborative': collaborative}
            playlistDict.append(playlistItem)

    with open('playlists.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'playlist name', 'creator', 'collaborative']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for thing in playlistDict:
            writer.writerow({'id': thing['id'], 'playlist name': thing['playlist name'], 'creator': thing['creator'], 'collaborative': thing['collaborative']})

def playlistDataCollector():
    client = authCode("playlist-read-private")

    items = []

    results = client.playlist_tracks(playlist_id='6MXsOjipLt0yEC2OFMSj6N')

    for item in results['items']:
        items.append(item)

    while results['next']:
        results = client.next(results)
        for item in results['items']:
            items.append(item)

    dictObj = []

    overallGenres = set()

    for item in items:
        artistList = []
        genreList = []
        for artist in item['track']['artists']:
            artistList.append(artist['name'])

            artistResult = client.artist(artist['id'])
            genreList.append(artistResult['genres'])
            
            for genre in artistResult['genres']:
                overallGenres.add(genre)
        
        trackItem = {'uri': item['track']['uri'], 'name': item['track']['name'], 'artists': artistList, 'genres': genreList}
        dictObj.append(trackItem)

    with open('genreSorter.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'artists', 'genres', 'uri']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in dictObj:
            writer.writerow({'name': entry['name'], 'artists': entry['artists'], 'genres': entry['genres'], 'uri': entry['uri']})

    print(overallGenres)