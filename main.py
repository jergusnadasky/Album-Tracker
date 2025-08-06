import google_docs_auth_setup
import last_fm_auth_setup
import write_albums

i = 0
use_google_docs = False

input("Welcome to the Last.fm Album Logger! Press Enter to continue...")
last_fm_auth_setup.start()


while i != 1:
    userChoice = input("Type 'y' to use Google Docs API integration: [y/n] ").strip().lower()

    if userChoice == 'y':
        i = 1
        use_google_docs = True
        service = google_docs_auth_setup.get_google_docs_service()
        document_id = google_docs_auth_setup.get_document_id_from_user()
        
    elif userChoice == 'n':
        i = 1
        use_google_docs = False
    else:
        print("Invalid input, please try again.")
        
write_albums.start()
    

if use_google_docs:
    text_to_append = write_albums.get_album_log_text() 
    google_docs_auth_setup.append_to_doc(service, document_id, text_to_append)

