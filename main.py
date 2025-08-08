import google_docs_auth_setup
import last_fm_auth_setup
import write_albums

i = 0
use_google_docs = False

input("Welcome to the Last.fm Album Logger! Press Enter to continue...")
last_fm_auth_setup.start()
print("Last.fm authentication complete.")




while i != 1:
    userChoice = input("Type 'y' to use Google Docs API integration: [y/n] ").strip().lower()

    if userChoice == 'y':
        i = 1
        service = google_docs_auth_setup.get_google_docs_service()


        if(service):
            write_albums.start()
            document_id = google_docs_auth_setup.get_document_id_from_user()
            text_to_append = write_albums.get_album_log_text() 
            google_docs_auth_setup.append_to_doc(service, document_id, text_to_append)
            
        elif userChoice == 'n':
            break
        else:       
            print("Invalid input, please try again.")
        
