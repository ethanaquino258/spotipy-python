from authentication import authCode
import spotipy

def userPlaylists():
    client = authCode("playlist-read-private")

    results = client.current_user_playlists()

    for idx, item in enumerate(results['items']):
        playlistObject = results['items'][idx]

        collaborative = playlistObject['collaborative']
        playlistName = playlistObject['name']
        creator = playlistObject['owner']['id']

        print(f'Name: {playlistName}\nCreator: {creator}\nCollaborative: {collaborative}\n')
    exit()