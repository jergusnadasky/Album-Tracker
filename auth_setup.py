import os
import hashlib
from urllib.parse import parse_qs, urlparse
import requests
import webbrowser
from dotenv import load_dotenv, set_key, find_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SESSION_KEY = os.getenv("SESSION_KEY")

def generate_api_sig(params, secret):
    raw = ''.join(f"{k}{v}" for k, v in sorted(params.items()))
    raw += secret
    return hashlib.md5(raw.encode('utf-8')).hexdigest()

def save_to_env(key, value):
    dotenv_path = find_dotenv()
    if not dotenv_path:
        # Create .env if not exists
        with open('.env', 'w') as f:
            f.write('')
        dotenv_path = '.env'
    set_key(dotenv_path, key, value)

def get_session_key(url):

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    token = query_params.get('token', [None])[0]

    params = {
        'method': 'auth.getSession',
        'api_key': API_KEY,
        'token': token,
    }
    params['api_sig'] = generate_api_sig(params, API_SECRET)
    params['format'] = 'json'

    resp = requests.get("https://ws.audioscrobbler.com/2.0/", params=params)
    data = resp.json()

    if 'session' in data:
        return data['session']['key']
    else:
        print("Failed to get session key:", data)
        return None

def main():
    global API_KEY, API_SECRET, SESSION_KEY

    if not API_KEY or not API_SECRET:
        print("ERROR: Please add API_KEY and API_SECRET to your .env file before running this script.")
        print("You can get these by creating an app here: https://www.last.fm/api/account/create")
        return

    if SESSION_KEY:
        print("Session key already found in .env. No need to authenticate again.")
        print(f"SESSION_KEY={SESSION_KEY}")
        return

    auth_url = f"http://www.last.fm/api/auth/?api_key={API_KEY}"
    print(f"Opening browser for authorization:\n{auth_url}\n")
    webbrowser.open(auth_url)

    token = input("After authorizing the app, please paste the URL here: ").strip()

    session_key = get_session_key(token)
    if session_key:
        print(f"Success! Your session key is:\n{session_key}")
        save_to_env("SESSION_KEY", session_key)
        print("Saved SESSION_KEY to .env for future use.")
    else:
        print("Could not obtain session key. Please try again.")

if __name__ == "__main__":
    main()
