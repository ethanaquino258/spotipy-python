import spotipy
import authentication
from albums import savedAlbums
from artists import topArtists, followedArtists
from tracks import savedTracks, topTracks, currentTrack, recentlyPlayedTracks, genreSorting
from playlists import playlistDataCollector, userPlaylists, writeToCSV
from shows import savedShows

def main():
    print("Hello!\nWelcome to my spotipy project")

    try:
        actionItem = input("""
        Enter the # of the action you wish to take

            1. top tracks
            2. saved tracks
            3. current track
            4. recently played tracks
            5. top artists
            6. followed artists
            7. saved albums
            8. playlists
            9. saved shows
            10. genreSorting
            11. writeToCSV
            12.playListDataCollector
        """)

        actions = {
            "1": topTracks,
            "2": savedTracks,
            "3": currentTrack,
            "4": recentlyPlayedTracks,
            "5": topArtists,
            "6": followedArtists,
            "7": savedAlbums,
            "8": userPlaylists,
            "9": savedShows,
            "10": genreSorting,
            "11": writeToCSV,
            "12": playlistDataCollector
        }

        actions[actionItem]()
        
    except spotipy.client.SpotifyException as e:
        print("======ERROR======")
        print(e)
        exit()


if __name__ == "__main__":
    main()
