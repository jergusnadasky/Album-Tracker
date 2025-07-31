﻿# Album-Tracker

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
   TOKEN=YOUR_SESSION_TOKEN
   ```
   For now you can fill out USERNAME

  ***Don’t share this file! It contains your private API keys and phone number.***

  4. Go to https://www.last.fm/api/account/create and create an API Account. Only input a name.

  5. Paste API key and API secret into .env file inside of the quotes

  6. run auth_setup.py and click allow access.

  7. after the redirect, copy the url and paste it into the console.

  8. Run log_albums.py and profit

