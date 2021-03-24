from authentication import authCode
import spotipy

def savedShows():
    client = authCode("user-library-read")

    results = client.current_user_saved_shows()

    for idx, result in enumerate(results['items']):
        showObject = results['items'][idx]['show']

        showName = showObject['name']
        showDesc = showObject['description']
        showPublisher = showObject['publisher']
        
        print(f'Name: {showName}\nPublisher: {showPublisher}\n{showDesc}\n')

    exit()