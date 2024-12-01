import downloader as dl

def main() -> None:
    while True:
        show_menu()

        choice = get_choice()
        if choice == '0':
            break
        handle_choice(choice)

    print("Shutting down.")


def show_menu() -> None:
    print('''
    ***~ PyYT Downloader ~***
          
    [0] Exit
    [1] Download one video
    [2] Download one video, audio only
    [3] Download a playlist
    [4] Download a playlist, audio only
    [5] List all songs in a playlist
          ''')


def get_choice() -> str:
    choice = input("What are we stealing today? ")

    return choice


def handle_choice(choice) -> None:
    if choice == '1':
        url = input("Enter video url: ")
        dl.download_single_video(url)

    elif choice == '2':
        url = input("Enter video url: ")
        dl.download_single_audio(url)

    elif choice == '3':
        url = input("Enter playlist url: ")
        dl.download_playlist_video(url)

    elif choice == '4':
        url = input("Enter playlist url: ")
        dl.download_playlist_audio(url)

    elif choice == '5':
        url = input("Enter playlist url: ")
        dl.get_titles_in_playlist(url)

    else:
        print("Invalid choice! Try again.")


if __name__ == '__main__':
    main()