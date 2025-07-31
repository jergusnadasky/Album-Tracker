# Album-Tracker

---

This python script uses the Last.fm API to gather and dump the albums you have listened to recently. Many people in the world discover new music and expand their taste by listening to new albums everyday and I wanted to create a tool that will extract that information and save it automatically . I personally want to keep a record of when I listened to an album and what the album was, and this is a digital way of doing it.

Previously, I logged albums manually in a notes app on my phone, but I wanted a more seamless and automated solution — something that could run in the background and maintain a dated history of what I listened to. This script captures that information and writes it to a text file, and in the future, I plan to sync it with Google Docs for better accessibility and backup.

Ultimately, it solves the small but meaningful problem of keeping a personal music diary without the effort of manual entry.

---

## Requirements

- Python 3.7+
- [Last.fm Account](https://www.last.fm/)

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/jergusnadasky/Album-Tracker.git
   
2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   
3. **Create a `.env` file**
   In the project root, create a file named `.env` and paste the following:

   ```env
   # Initial detail
   LASTFMUSERNAME=YOUR_LAST.FM_USERNAME

   # Received upon API registration
   API_KEY=YOUR_LAST.FM_API_KEY
   API_SECRET=YOUR_LAST.FM_API_SECRET

   # Received upon auth
   # Keep SESSION_KEY empty
   SESSION_KEY=
   ```
   For now you can fill out USERNAME

  ***Don’t share this file! It contains your private API keys!***

  4. Go to https://www.last.fm/api/account/create and create an API Account. Only input a name.

  5. Paste API key and API secret into .env file inside of the quotes

  6. run auth_setup.py and click allow access.

  7. after the redirect, copy the url and paste it into the console.

  8. Run log_albums.py and profit

