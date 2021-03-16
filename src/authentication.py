import spotipy
import spotipy.util as util
import sys
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def authCode():
    load_dotenv()

    clientID = os.getenv('SPOTIFY_CLIENT_ID')
    clientSecret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_URI = os.getenv('REDIRECT_URI')

    # scope = "user-library-read user-read-recently-played user-top-read"
    scope = "user-library-read user-top-read"
        
    # if len(sys.argv) > 1:
    #     username = sys.argv[1]
    # else:
    #     print("Usage: %s username" % (sys.argv[0],))
    #     sys.exit()

    username = input("Enter username:")

    token = util.prompt_for_user_token(
        username, scope, clientID, clientSecret, redirect_URI
    )

    sp = spotipy.Spotify(auth=token)
    
    return sp
