# google_docs_auth_setup.py


#https://console.cloud.google.com/welcome?inv=1&invt=Ab48Fw&project=ddos-300917

from tkinter import Tk, filedialog
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv, set_key, find_dotenv

from last_fm_auth_setup import save_to_env

load_dotenv()

GOOGLE_DOCS_URL = os.getenv("GOOGLE_DOCS_URL")

SCOPES = ['https://www.googleapis.com/auth/documents']

def get_document_id_from_user():
    if GOOGLE_DOCS_URL:
        # If GOOGLE_DOCS_URL is set, use it to extract the document ID
        return GOOGLE_DOCS_URL.split("/d/")[1].split("/")[0]
    
    url = input("Enter your Google Docs document URL or ID: ").strip()
    save_to_env("GOOGLE_DOCS_URL", url)
    # Support full URL or just ID
    if "/d/" in url:
        return url.split("/d/")[1].split("/")[0]
    return url  # assume it's just the ID

def get_google_docs_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        try:
            print("Token not found or invalid. Please select your client_secret.json file.")

            # Use tkinter file dialog to select credentials file
            root = Tk()
            root.withdraw()  # Hide the main window
            cred_file = filedialog.askopenfilename(
                title="Select your Google API client_secret.json",
                filetypes=[("JSON files", "*.json")]
            )
            root.destroy()

            if not cred_file:
                raise Exception("No client_secret file selected.")

            flow = InstalledAppFlow.from_client_secrets_file(cred_file, SCOPES)
            creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        except Exception as e:
            print("\n❌ ERROR: Could not complete Google Docs authentication.")
            print("👉 Visit https://console.cloud.google.com/ to enable the Google Docs API and download your client_secret.json file.")
            print(f"📄 Error Details: {e}")
            return None

    try:
        service = build('docs', 'v1', credentials=creds)
        print("✅ Google Docs service ready.")
        return service
    except Exception as e:
        print(f"❌ Failed to build Google Docs service: {e}")
        return None

def append_to_doc(service, document_id, text):
    requests = [
        {
            'insertText': {
                'endOfSegmentLocation': {},
                'text': text + '\n' # Append text with a newline
            }
        }
    ]
    service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()
