from authentication import authCode
import spotipy

def savedAlbums():
    client = authCode("user-library-read")

    results = client.current_user_saved_albums()

    for idx, item in enumerate(results['items']):
        track = item['album']
        print(idx, track['artists'][0]['name'], " – ", item['album']['name'])
    
    exit()