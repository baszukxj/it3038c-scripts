# Project 3 - Python Flask App with Lyric Genius Plugin

Author - Xavier Baszuk

# Description

For this project, I added to my project 2 and created a flask app which will use a python module to lookup lyrics for a song by artist. 
All you need to do is run the main flask app 'main.py' and fill in the corresponding fields with a artist name, song name, and genuis bearer token.

# Dependencies

This project relies on lyricsgenius and flask modules to search the genuis API and host the web app. See below to install:
```
pip install lyricsgenius
pip install Flask
```

This project also relies on you passing in a bearer token when filling out the input fields.
The program will throw an error without a valid access token. You can generate a valid bearer token here: https://docs.genius.com/#/getting-started-h1