# Album-Tracker

---

This python script uses the Last.fm API to gather and dump the albums you have listened to recently. Many people in the world discover new music and expand their taste by listening to new albums everyday and I wanted to create a tool that will extract that information and save it automatically. I personally want to keep a record of when I listened to an album and what the album was, and this is a digital way of doing it.

Previously, I logged albums manually in a notes app on my phone, but I wanted a more seamless and automated solution — something that could run in the background and maintain a dated history of what I listened to. This script captures that information and writes it to a text file and a google doc using Google Docs API services.

Ultimately, it solves the small but meaningful problem of keeping a personal music diary without the effort of manual entry.

---

## Requirements

- Python 3.7+
- [Last.fm Account](https://www.last.fm/)
- Google Account

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
   LASTFMUSERNAME=''

   # Received upon API registration
   API_KEY=''
   API_SECRET=''

   # Received upon auth
   # Keep SESSION_KEY empty
   SESSION_KEY=''

   #Google Docs API credentials
   # Keep GOOGLE_DOCS_URL empty
   GOOGLE_DOCS_URL=''

   ```
  ***Don’t share this file! It contains your private API keys!***

## Google Docs API Set-up

If you plan on using the Google Docs API integration, follow these steps. 

1. visit https://console.cloud.google.com/projectcreate?

2. Type 'Last.fm Album Tracker' into project name

3. Create it

4. after redirect, click navigation menu and go to 'APIs & Services'

5. press 'Enable APIs & Services'

6. Search for 'Google Docs API' and enable it

7. After redirect, press 'Create credentials'

8. Check 'User data' and fill in required fields

9. skip scopes page

10. For OAuth Client ID set application type to 'Desktop App'

11. On the 'Your Credentials' step, click Download and save that file in the root of this repo.

12. Click Navigation Menu and hover over 'APIs & Services' and click 'OAuth Consent Screen'

13. on the left tab click Audience and under Test Users, add yourself with your email.

## Initial Run

1. Run Main.py and follow directions in console

2. Input Last.fm username, Last.fm application API key and API secret. Visit https://www.last.fm/api/account/create to get this

3. After redirect, click 'Yes, Allow Access' and after redirect, copy and paste the url into the terminal. This has your token.

4. Last.fm auth complete

5. If you did the Google Docs API setup, type 'y'. If not type 'n'.

6. When asked for file, select the client_secret.json file that you downloaded earlier

7. After redirect sign in and authenticate and click continue

8. Create a new google doc and paste the URL into the console.
