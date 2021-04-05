from authentication import authCode
import spotipy

def savedAlbums():
    client = authCode("user-library-read")

    results = client.current_user_saved_albums()

    while results['next']:
        results = client.next(results)
        albums = results['items']
        for item in albums:
            albumObject = item['album']

            artist = albumObject['artists'][0]['name']
            albumName = albumObject['name']

            print(f'{artist} - {albumName}')
        
        albums.extend(results['items'])

    exit()