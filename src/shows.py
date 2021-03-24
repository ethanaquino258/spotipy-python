from authentication import authCode
import spotipy

def savedShows():
    client = authCode("user-library-read")

    results = client.current_user_saved_shows()

    for idx, result in enumerate(results['items']):
        showName = results['items'][idx]['show']['name']
        showDesc = results['items'][idx]['show']['description']
        showPublisher = results['items'][idx]['show']['publisher']
        print(f'{idx}. Name: {showName}\nPublisher: {showPublisher}\n{showDesc}\n')

    exit()