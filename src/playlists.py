from authentication import authCode
import spotipy

def userPlaylists():
    client = authCode("playlist-read-private")

    results = client.current_user_playlists()

    while results['next']:
        results = client.next(results)
        playlists = results['items']
        for idx, item in enumerate(playlists):
            playlistObject = results['items'][idx]

            collaborative = playlistObject['collaborative']
            playlistName = playlistObject['name']
            creator = playlistObject['owner']['id']

            print(f'Name: {playlistName}\nCreator: {creator}\nCollaborative: {collaborative}\n')
            print(f'Total Playlists: {idx}')
    exit()