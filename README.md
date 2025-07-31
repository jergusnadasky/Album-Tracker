# Album-Tracker

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
   SESSION_KEY=
   TOKEN=YOUR_SESSION_TOKEN
   ```
   For now you can fill out USERNAME

  ***Don’t share this file! It contains your private API keys and phone number.***

  4. Go to https://www.last.fm/api/account/create and create an API Account. For Callback URL put http://localhost:8080

  5. Paste API key and API secret into .env file

  6. access this page with a web browser https://www.last.fm/api/auth/?api_key=API_KEY_HERE

  7. click allow access

  8. after the redirect, take note of the 'token=' field in the URL and paste it into .env

  9. Run session_key_extractor.py

  10. take note of the 'key=' ouput in the console and paste it into .env for SESSION_KEY

  11. Run log_albums.py and profit

