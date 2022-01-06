from authentication import authCode
from datetime import datetime
import csv
import pandas as pd
import numpy


def multiples(count):
    multipleList = []
    intendedRange = count//100
    for i in range(intendedRange):
        multipleList.append(i*100)
    return multipleList


def libraryRead():
    try:
        with open('user-library.csv', newline='') as readfile:
            fileReader = csv.reader(readfile)

            header = next(fileReader)
            firstLine = next(fileReader)

            mostRecent = datetime.strptime(firstLine[-1], "%Y-%m-%dT%H:%M:%S")
    except FileNotFoundError:
        pass

    client = authCode("user-library-read")
    results = client.current_user_saved_tracks()

    tracks = results['items']

    while results['next']:
        results = client.next(results)
        tracks.extend(results['items'])

    trackTotal = len(tracks)
    print(f'**{trackTotal} tracks compiled. Analyzing (this could take a while)...**')

    songsDict = []
    overallGenres = set()

    trackCounter = 0
    progressMarkers = multiples(trackTotal)

    for item in tracks:
        if trackCounter in progressMarkers:
            print(f'{trackCounter}/{trackTotal} analyzed...')
        artistList = []
        genreList = []

        timeAdded = item['added_at'][:-1]

        # itemTime = datetime.strptime(timeAdded, "%Y-%m-%dT%H:%M:%S")

        # print(itemTime < mostRecent)
        # if itemTime < mostRecent:
        #     break

        trackObj = item['track']
        for artist in trackObj['artists']:
            artistList.append(artist['name'])

            artistResult = client.artist(artist['id'])

            # if artist['name'] == 'Iwalani Kahalewai':
            #     print(artistResult['genres'])
            if artistResult['genres'] == []:
                genreResult = 'no genre'
            else:
                genreResult = artistResult['genres']

            genreList.append(genreResult)

        for genreArray in genreList:
            for genre in genreArray:
                overallGenres.add(genre)

        trackItem = {'uri': trackObj['uri'], 'name': trackObj['name'],
                     'artists': artistList, 'genres': genreList, 'time added': timeAdded}
        songsDict.append(trackItem)
        trackCounter += 1

    print('**Done! Writing to file now**')

    with open('user-library.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'artists', 'genres', 'uri', 'time added']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in songsDict:
            writer.writerow({'name': entry['name'], 'artists': entry['artists'],
                            'genres': entry['genres'], 'uri': entry['uri'], 'time added': entry['time added']})

    print('**Track file written. Writing genres to file now')

    songs = pd.read_csv('user-library.csv')
    df = pd.DataFrame(data=songs)

    genreDict = []

    for genre in overallGenres:
        rslt_df = df.loc[df['genres'].str.contains(genre)]

        genreObj = {'genre': genre, 'occurences': len(rslt_df)}
        genreDict.append(genreObj)

    with open('user-genres.csv', 'w', newline='') as csvfile:
        fieldnames = ['genre', 'number of occurences']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in genreDict:
            writer.writerow(
                {'genre': entry['genre'], 'number of occurences': entry['occurences']})

    print('Done!')


def playlistByGenre():
    client = authCode("playlist-modify-public")

    try:
        songs = pd.read_csv("user-library.csv")
        df = pd.DataFrame(data=songs)
    except:
        print("Library file not found. Creating now...")
        libraryRead()
        playlistByGenre()

    desiredGenre = input("""
    Please enter the name of the genre you'd like to make a playlist for:
    (see user-genres.csv for list of genres in your library)

    For multiple genres in different playlists, separate using *
    Do not add a space after the asterisk
    """)

    genres = desiredGenre.split('*')

    for genre in genres:
        rslt_df = df.loc[df['genres'].str.contains(genre)]

        if len(rslt_df) < 1:
            print("\ngenre not found!\n")
            exit

        uriList = []

        for index, row in rslt_df.iterrows():
            uriList.append(row['uri'])

        user = client.me()
        createResults = client.user_playlist_create(user['id'], genre)
        newPlaylistID = createResults['id']

        # spotify limits amount of tracks you can add per request to 100 max; this is a 'paginator' of sorts
        if len(uriList) > 100:
            sections = len(uriList)//100

            splitList = numpy.array_split(uriList, sections + 1)

            for arry in splitList:
                smallerList = []
                for item in arry:
                    smallerList.append(item)

                client.user_playlist_add_tracks(
                    user['id'], newPlaylistID, smallerList)
        else:
            client.user_playlist_add_tracks(user['id'], newPlaylistID, uriList)
