import json
import pandas as pd
import collections
import lyricsgenius
import streamlit as st

client_access_token = "HpIYpWE8urYEimLXmjRsNBXLUERWVVS85HHCQEWrSKBedFN0b7OxCweWpLbk7CT-"
LyricsGenius = lyricsgenius.Genius(client_access_token)
LyricsGenius.excluded_terms = ["Live", "(Live)", "MTV Unplugged", "Demo"]

def getSongs(artist, album_name=None, max_songs=None):
    clean_name = artist.replace(' ', '')
    lyrics_dict = collections.defaultdict(str)
    if album_name is None:
        artist_obj = LyricsGenius.search_artist(artist, max_songs=max_songs)
        artist_obj.save_lyrics(filename=f'Lyrics_{clean_name}', overwrite=True)
        print('Data saved')
        with open(f'Lyrics_{clean_name}.json') as f:
            data = json.load(f)
        print('Data loaded')
        for song in data['songs']:
            lyrics_dict[song['title']] += song['lyrics']
    else:
        clean_album = album_name.replace(' ', '')
        album_obj = LyricsGenius.search_album(album_name, artist)
        album_obj.save_lyrics(filename=f'Lyrics_{clean_album}', overwrite=True)
        print('Data saved')
        with open(f'Lyrics_{clean_album}.json') as f:
            data = json.load(f)
        print('Data loaded')
        for song in data['tracks']:
            lyrics_dict[song['song']['full_title'].split('by')[0].strip()] += song['song']['lyrics']
 
    lyrics_df = pd.DataFrame.from_dict(dict(lyrics_dict), orient='index').reset_index().rename(columns={'index':'song_title',0:'lyrics'})
    return lyrics_df

artist_name = st.text_input('Artist name')
album_name  = st.text_input('Album name')

lyrics_df = getSongs(artist_name, album_name)
artist_clean = artist_name.replace(' ','')
album_clean  = album_name.replace(' ','')
    
@st.cache
def convert_df(df):
    return df.to_csv()

csv = convert_df(lyrics_df)

if album_name == '':
  st.download_button(
      label="Download data as CSV",
      data=csv,
      file_name=f'lyrics_{artist_clean}.csv',
      mime='text/csv',
  )
else:
  st.download_button(
      label="Download data as CSV",
      data=csv,
      file_name=f'lyrics_{artist_clean}-{album_clean}.csv',
      mime='text/csv',
  )