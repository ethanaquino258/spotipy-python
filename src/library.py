from authentication import authCode
from datetime import datetime
import csv
import pandas as pd
import numpy

def libraryRead():
    client = authCode("user-library-read")
    results = client.current_user_saved_tracks()

    tracks = results['items']

    while results['next']:
        results = client.next(results)
        tracks.extend(results['items'])
    
    songsDict = []
    overallGenres = set()

    for item in tracks:
        artistList = []
        genreList = []

        timeAdded = item['added_at'][:-1]

        itemTime = datetime.strptime(timeAdded, "%Y-%m-%dT%H:%M:%S")

        trackObj = item['track']
        for artist in trackObj['artists']:
            artistList.append(artist['name'])

            artistResult = client.artist(artist['id'])
            genreList.append(artistResult['genres'])

            for genre in artistResult['genres']:
                overallGenres.add(genre)
        
        trackItem = {'uri': trackObj['uri'], 'name': trackObj['name'], 'artists': artistList, 'genres': genreList, 'time added': itemTime}
        songsDict.append(trackItem)

    with open('user-library.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'artists', 'genres', 'uri', 'time added']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in songsDict:
            writer.writerow({'name': entry['name'], 'artists': entry['artists'], 'genres': entry['genres'], 'uri': entry['uri'], 'time added': entry['time added']})

    songs = pd.read_csv('user-library.csv')
    df = pd.DataFrame(data=songs)

    genreDict = []

    for genre in overallGenres:
        rslt_df = df.loc[df['genres'].str.contains(genre)]

        genreObj = {'genre': genre, 'occurences': len(rslt_df)}
        genreDict.append(genreObj)

    with open('user-library-genre-details.csv', 'w', newline='') as csvfile:
        fieldnames = ['genre', 'number of occurences']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in genreDict:
            writer.writerow({'genre': entry['genre'], 'number of occurences': entry['occurences']})

def playlistByGenre():
    client = authCode("playlist-modify-public")

    songs = pd.read_csv("user-library.csv")
    df = pd.DataFrame(data=songs)

    desiredGenre = input("""
    Please enter the name of the genre you'd like to make a playlist for:
    (see user-library-genre-details.csv for list of genres in your library)
    """)

    rslt_df = df.loc[df['genres'].str.contains(desiredGenre)]

    if len(rslt_df) < 1:
        print("\ngenre not found!\n")
        exit

    uriList = []

    for index, row in rslt_df.iterrows():
        uriList.append(row['uri'])

    user = client.me()
    createResults = client.user_playlist_create(user['id'], desiredGenre)
    newPlaylistID = createResults['id']

    # spotify limits amount of tracks you can add per request to 100 max; this is a 'paginator' of sorts
    if len(uriList) > 100:
        sections = len(uriList)//100
        
        splitList = numpy.array_split(uriList, sections + 1)

        for arry in splitList:
            smallerList = []
            for item in arry:
                smallerList.append(item)

            client.user_playlist_add_tracks(user['id'], newPlaylistID, smallerList)