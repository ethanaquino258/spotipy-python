from authentication import authCode
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
