import google_docs_auth_setup
import last_fm_auth_setup
import write_albums
from colorama import init, Fore, Style
from pyfiglet import figlet_format

init(autoreset=True)

def show_banner():
    banner = figlet_format("ALBUM LOGGER", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + Style.BRIGHT + "Track your recent albums with Last.fm + Google Docs!\n")

def main():
    i = 0
    use_google_docs = False

    show_banner()
    input(Fore.LIGHTWHITE_EX + "🎧 Press Enter to begin setup...")

    last_fm_auth_setup.start()
    print(Fore.GREEN + "✅ Last.fm authentication complete.\n")

    while i != 1:
        userChoice = input(Fore.CYAN + "📝 Use Google Docs integration? [y/n]: ").strip().lower()

        if userChoice == 'y':
            i = 1
            service = google_docs_auth_setup.get_google_docs_service()

            if service:
                print(Fore.GREEN + "✅ Google Docs ready.\n")
                write_albums.start()
                document_id = google_docs_auth_setup.get_document_id_from_user()
                text_to_append = write_albums.get_album_log_text()
                google_docs_auth_setup.append_to_doc(service, document_id, text_to_append)
                print(Fore.GREEN + "📄 Albums written to Google Docs.")
            else:
                print(Fore.RED + "❌ Google Docs setup failed.")

        elif userChoice == 'n':
            write_albums.start()
            i = 1
        else:
            print(Fore.RED + "❌ Invalid input. Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()
