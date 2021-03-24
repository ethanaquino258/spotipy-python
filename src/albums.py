from authentication import authCode
import spotipy

def savedAlbums():
    client = authCode("user-library-read")

    results = client.current_user_saved_albums()

    for item in results['items']:
        albumObject = item['album']

        artist = albumObject['artists'][0]['name']
        albumName = albumObject['name']

        print(f'{artist} - {albumName}')

    exit()