import os
import requests
from collections import defaultdict
from datetime import datetime
import hashlib
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
USERNAME = os.getenv("LASTFMUSERNAME")
SESSION_KEY = os.getenv("SESSION_KEY")
LIMIT = 200  # <- Adjust this limit as needed
LOG_FILE = 'album_log.txt'
album_cache = set()
google_docs_text = ""

class Album:
    def __init__(self, name, artist, date):
        self.name = name.strip().lower()
        self.artist = artist.strip().lower()
        self.date = date

    def __eq__(self, other):
        return (self.name, self.artist) == (other.name, other.artist)

    def __hash__(self):
        return hash((self.name, self.artist))

    def __str__(self):
        return f"{self.date} | {self.artist} - {self.name}"

    def __repr__(self):
        return self.__str__()

def generate_api_sig(params):
    raw = ''.join(f"{k}{v}" for k, v in sorted(params.items()))
    raw += API_SECRET
    return hashlib.md5(raw.encode('utf-8')).hexdigest()

def get_recent_tracks():
    load_dotenv(override=True)
    
    url = 'https://ws.audioscrobbler.com/2.0/'
    
    sig_params = {
        'method': 'user.getRecentTracks',
        'user': os.getenv("LASTFMUSERNAME"),
        'api_key': os.getenv("API_KEY"),
        'limit': str(LIMIT),
        'extended': '1',
        'sk': os.getenv("SESSION_KEY")
    }

    api_sig = generate_api_sig(sig_params)
    sig_params['format'] = 'json'
    sig_params['api_sig'] = api_sig

    response = requests.get(url, params=sig_params)

    return response.json()

def timestamp_to_date(ts):
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d')

def group_tracks_by_day_and_album(tracks):
    day_album_map = defaultdict(lambda: defaultdict(set))
    for track in tracks:
        if 'date' not in track:
            continue
        date = timestamp_to_date(track['date']['uts'])
        album = track['album']['#text']
        artist = track['artist']['name']
        name = track['name']
        if album:
            key = f"{album}///{artist}"
            day_album_map[date][key].add(name)
    return day_album_map

def log_albums(day_album_map):
    
    global google_docs_text
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        for date in sorted(day_album_map.keys()):  # Oldest first
            albums = day_album_map[date]
            for full_album_key, tracks in albums.items():
                album, artist = full_album_key.split("///")
                track_count = len(tracks)

                if track_count >= 5:
                    album_key = (album.strip().lower(), artist.strip().lower())

                    if album_key not in album_cache:
                        album_cache.add(album_key)
                        album_obj = Album(album, artist, date)
                        f.write(str(album_obj) + '\n')
                        google_docs_text += str(album_obj) + '\n'
                    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        for date in sorted(day_album_map.keys(), reverse=True):  # <-- sort by date descending
            albums = day_album_map[date]
            for full_album_key, tracks in albums.items():
                album, artist = full_album_key.split("///")
                track_count = len(tracks)

                if track_count >= 5:  # Placeholder logic
                    album_key = (album.strip().lower(), artist.strip().lower())

                    if album_key not in album_cache:
                        album_cache.add(album_key)
                        album_obj = Album(album, artist, date)
                        f.write(str(album_obj) + '\n')
                

def get_album_log_text():
    return google_docs_text
        
def load_existing_albums(file_path):
    cache = set()
    if not os.path.exists(file_path):
        return cache
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if "|" in line:
                date_part, album_part = line.strip().split(" | ", 1)
                if " - " in album_part:
                    artist, name = album_part.split(" - ", 1)
                    cache.add((name.strip().lower(), artist.strip().lower()))
    return cache




def start():
    load_dotenv(override=True)
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    USERNAME = os.getenv("LASTFMUSERNAME")
    SESSION_KEY = os.getenv("SESSION_KEY")
    global album_cache  # Tell Python to use the global variable, not create a local one
    print("Fetching recent tracks...")
    album_cache = load_existing_albums(LOG_FILE)
    data = get_recent_tracks()
    tracks = data.get('recenttracks', {}).get('track', [])
    grouped = group_tracks_by_day_and_album(tracks)
    log_albums(grouped)
    print("Done.")
    print(f"Writing to: {LOG_FILE}")
