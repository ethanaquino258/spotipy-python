from authentication import authCode
import spotipy

def userPlaylists():
    client = authCode("playlist-read-private")

    results = client.current_user_playlists()

    for idx, item in enumerate(results['items']):
        collaborative = results['items'][idx]['collaborative']
        playlistName = results['items'][idx]['name']
        creator = results['items'][idx]['owner']['id']

        print(f'{idx}. Name: {playlistName} \nCreator: {creator} \nCollaborative: {collaborative}')
    exit()