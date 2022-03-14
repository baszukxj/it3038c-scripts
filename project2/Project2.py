# The goal of this script is to output lyrics of a song quickly in a console setting. It will do this by scraping
# genius.com for lyrics of a song and output them to a console.

# Import Genius Lyric module, which allows us to connect to the Genius API to search for lyrics for songs
import lyricsgenius, sys

# Configure Auth Bearer Token (bearer token should be passed in as an argument when running the script)
token = sys.argv[1]

# Configure genius client
genius = lyricsgenius.Genius(token)

# Receive input from user
artistInput = input("Who is the artist of the song?: ")

# Search for artist
artist = genius.search_artist(artistInput, max_songs=2, sort="title", include_features=True)

# Receive input from user
songInput = input("What is the name of the song?: ")

# Search GeniusAPI for song
song = artist.song(songInput)

# Print output
print("-----Lyrics--------")
print(song.lyrics)







