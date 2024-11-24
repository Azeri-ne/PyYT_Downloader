import downloader as dl

def main() -> None:
    while True:
        show_menu()

        choice = get_choice()
        if choice == '0':
            break

    print("Shutting down.")


def show_menu() -> None:
    print('''
    ***~ PyYT Downloader ~***
          
    [0] Exit
    [1] Download one video
    [2] Download one video, audio only
    [3] Download a playlist
    [4] Download a playlist, audio only 
          ''')


def get_choice() -> str:
    choice = input("What are we stealing today? ")

    return choice


if __name__ == '__main__':
    main()