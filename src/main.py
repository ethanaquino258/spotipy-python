import spotipy
import authentication
from albums import savedAlbums
from artists import topArtists, followedArtists
from tracks import savedTracks, topTracks, currentTrack, recentlyPlayedTracks
from playlists import userPlaylists
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
            "9": savedShows
        }

        actions[actionItem]()

        # right now the app seems to loop on itself as spotipy automatically assigns 127.0.0.1 as a local server, and i keep getting errors that the address is already in use
        # ignore first part, address in use definitely occurs though
        # somehow is solved by restarting computer and clearing safari cache. the former resets running processes and the latter allows you to hit the correct page
        # address in use likely caused by vscode trying to add helpers (if u cancel this error will occur)

        # next step is pagination
        
    except spotipy.client.SpotifyException as e:
        print("======ERROR======")
        print(e)
        exit()


if __name__ == "__main__":
    main()
