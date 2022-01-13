from spotipy.client import Spotify
from authentication import authCode
import csv
import string

def paginate():
    paginator = input('next? y/n')
    if paginator == 'y':
        return True
    else:
        return False

def compare(s1, s2):
    translator = str.maketrans('','', string.punctuation)

    # haven't tried to see if this works and wondering if its worth doing
    # theres remastered, mono, single, single edit, radio edit, album version, etc etc. Just a pain and while I'm assuming it's consistent I'm not sure
    
    # if 'Remastered' in s1:
    #     print(s1)
    #     remasteredIndex = s1.index('Remastered')
    #     s1 = s1[:remasteredIndex+(len('Remastered'))]
    #     print(s1)

    return s2.translate(translator).lower() in s1.translate(translator).lower()

def multiples(count):
    multipleList = []
    intendedRange = count//100
    for i in range(intendedRange):
        multipleList.append(i*100)
    return multipleList

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

def findInPlaylists():
    song = input('Please enter the name of the song you\'re looking for:\n')

    client = authCode('playlist-read-private')

    results = client.current_user_playlists(limit=50)

    # print(results['items'])
    print('gathering playlist data...')

    playlists = results['items']

    while results['next']:
        results = client.next(results)
        playlists.extend(results['items'])
    
    playlistTotal = len(playlists)

    print(f'{playlistTotal} gathered. Analyzing...')
    try:
        progressMarkers = multiples(playlistTotal)

        total = 0
        for playlist in playlists:

            if playlist['owner']['display_name'] == 'Spotify':
                continue

            total +=1
            if total in progressMarkers:
                print(f'{total}/{playlistTotal}')

            id = playlist['id']
            playlistName = playlist['name']

            playlistRaw = client.playlist_items(playlist_id=id)
            playlistItems = playlistRaw['items']

            while playlistRaw['next']:
                playlistRaw = client.next(playlistRaw)
                playlistItems.extend(playlistRaw['items'])

            itemTotal = 0
            for item in playlistItems:
                itemTotal +=1
                if item['track']['episode']:
                    pass
                else:
                    trackName = item['track']['name']
                    if compare(trackName, song) is True:
                        print('\n================')
                        print(f'found {trackName} in {playlistName}')
                        print('================\n')
    except Exception as e:
        # issue with audio bites from spotify. Can ignore in an except statement centered on playlistItems for loop or try to address
        # compare function not working with case sensitivity
        print(f'ERROR: {e}\n')
        print(total)
        print(playlistName)
        print(playlist)
        print(itemTotal)
        print(item)
        print(playlistItems)
        pass
