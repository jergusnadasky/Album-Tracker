# google_docs_auth_setup.py


#https://console.cloud.google.com/apis/library/docs.googleapis.com?inv=1&invt=Ab4rLg&project=ddos-300917

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
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('docs', 'v1', credentials=creds)

def append_to_doc(service, document_id, text):
    requests = [
        {
            'insertText': {
                'endOfSegmentLocation': {},
                'text': text + '\n'  # Append text with a newline
            }
        }
    ]
    service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()
