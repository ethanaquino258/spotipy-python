# About

This program gathers and processes user information from Spotify. The UI and functionality is contained in the terminal. 

# What you'll need
1. A Spotify account
2. python 3 or later (earlier versions of python may work as well but I haven't looked into it)
3. pipenv (you can get pipenv if you have python by running `pip install pipenv`)

# Getting Started

1. Go to the [Spotify developer portal](https://developer.spotify.com/dashboard/login) and login with your account. Accept the following terms of service
2. Click the **Create an app** button and fill out the following fields
3. Take note of **Client ID**, **Client Secret**, and set a **Redirect URI** (`http://localhost:8080/callback/` should do)
4. Create a `.env` file in the following format:
```
SPOTIFY_CLIENT_ID="client ID from step 3"
SPOTIFY_CLIENT_SECRET="client Secret from step 3"
SPOTIFY_USERNAME="your username"
REDIRECT_URI="http://localhost:8080/callback/"
```
5. Run `pipenv install` to download all dependencies
6. Run `pipenv run python src/main.py`

