# Project 2 - Python Plugin

Author - Xavier Baszuk

# Description

For this project, I created a python script which will use a python module to lookup lyrics for a song by artist. All you need to do is run the script with a genuis bearer token as an arguement and then fill out the input fields as they pop up.

# Dependencies

This project relies on lyricsgenius module to search the genuis API. See below to install:
```
pip install lyricsgenius
```

This project also relies on you passing in a bearer token as an arguement when running the script. The program will throw an error without a valid access token. You can generate a valid bearer token here: https://docs.genius.com/#/getting-started-h1