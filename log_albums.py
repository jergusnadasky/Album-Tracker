import os
import requests
from collections import defaultdict
from datetime import datetime
import hashlib
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
USERNAME = os.getenv("LASTFMUSERNAME")
SESSION_KEY = os.getenv("SESSION_KEY")
LIMIT = 200
LOG_FILE = 'album_log.txt'

def generate_api_sig(params):
    raw = ''.join(f"{k}{v}" for k, v in sorted(params.items()))
    raw += API_SECRET
    return hashlib.md5(raw.encode('utf-8')).hexdigest()

def get_recent_tracks():
    url = 'https://ws.audioscrobbler.com/2.0/'
    
    # Parameters used for signature
    sig_params = {
        'method': 'user.getRecentTracks',
        'user': USERNAME,
        'api_key': API_KEY,
        'limit': str(LIMIT),
        'extended': '1',
        'sk': SESSION_KEY
    }
    
    # Generate signature
    api_sig = generate_api_sig(sig_params)
    
    # Add format after signature
    sig_params['format'] = 'json'
    sig_params['api_sig'] = api_sig

    response = requests.get(url, params=sig_params)
    
    print(response.status_code)
    print(response.text)
    
    print(f"✅ Fetched {len(response.json().get('recenttracks', {}).get('track', []))} tracks")
    return response.json()




def timestamp_to_date(ts):
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d')

def group_tracks_by_day_and_album(tracks):
    day_album_map = defaultdict(lambda: defaultdict(set))
    print("📅 Grouping tracks...")
    for track in tracks:
        if 'date' not in track:
            continue
        date = timestamp_to_date(track['date']['uts'])
        album = track['album']['#text']
        artist = track['artist']['name']
        name = track['name']
        print(f"Track: {name} | Artist: {artist} | Album: {album} | Date: {date}")
        if album:
            key = f"{album}///{artist}"
            day_album_map[date][key].add(name)


    print("📅 Grouping tracks...")
    print(f"Track: {name} | Artist: {artist} | Album: {album} | Date: {date}")

    return day_album_map

def log_albums(day_album_map):
    with open(LOG_FILE, 'a') as f:
        for date, albums in day_album_map.items():
            for full_album_key, tracks in albums.items():
                album, artist = full_album_key.split("///")
                track_count = len(tracks)
                print(f"🧪 Album: {album} by {artist} — {track_count} unique tracks on {date}")

                if track_count >= 5: #TODO add check for half of album length
                    entry = f"{date} | {artist} - {album}"
                    f.write(entry + '\n') #TODO fix duplicate entries
                    print("🎧", entry)
                print(f"✅ Logging: {artist} - {album} on {date}")


if __name__ == "__main__":
    print("📡 Fetching recent tracks...")
    data = get_recent_tracks()
    tracks = data.get('recenttracks', {}).get('track', [])
    grouped = group_tracks_by_day_and_album(tracks)
    log_albums(grouped)
    print("✅ Done.")
    print(f"📂 Writing to: {LOG_FILE}")

