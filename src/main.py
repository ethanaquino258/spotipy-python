import spotipy
import authentication
from albums import savedAlbums
from artists import topArtists, followedArtists
from tracks import savedTracks, topTracks, currentTrack, recentlyPlayedTracks
from playlists import findInPlaylists, userPlaylists
from shows import savedShows
from library import libraryRead, playlistByGenre

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
            10. write library to CSV
            11. generate playlist for specific genre
            12. filter playlists by song
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
            "10": libraryRead,
            "11": playlistByGenre,
            "12": findInPlaylists
        }

        actions[actionItem]()
        
    except spotipy.client.SpotifyException as e:
        print("======ERROR======")
        print(e)
        exit()


if __name__ == "__main__":
    main()
