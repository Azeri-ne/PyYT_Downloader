from pytubefix import YouTube, Playlist
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

def main() -> None:
        pass


def handle_playlist_error(error, failed_downloads, 
                          downloaded_videos, video) -> None:
            print(f"Error! Can't find video. ({error})")
            failed_downloads.append(video.title)
            downloaded_videos += 1


def list_failed_videos(failed_downloads) -> None:
        print("These audio failed to download:")
        for failed_download in failed_downloads:
            print(failed_download)


def make_playlist_directory(playlist:Playlist) -> None:
    playlist_title = playlist.title
    playlist_folder = DOWNLOAD_PATH / playlist_title

    playlist_folder.mkdir(parents=True, exist_ok=True)


def download_playlist_audio(url:str) -> None:
    playlist = Playlist(url, use_po_token=True)
    playlist_title = playlist.title

    playlist_folder = DOWNLOAD_PATH / playlist_title
    playlist_folder.mkdir(parents=True, exist_ok=True)

    downloaded_videos = 0
    failed_downloads = []

    for video in playlist.videos:
        try:
            print(video.title)
            audio_stream = video.streams.get_audio_only()
            audio_stream.download(output_path=playlist_folder,
                filename_prefix=f"{downloaded_videos + 1} - ",
                max_retries=3)
            downloaded_videos += 1

        except Exception as error:
            handle_playlist_error(error, failed_downloads,
                                  downloaded_videos, video)

            continue

    print(f"Process complete: {downloaded_videos} audio downloaded.")
    if failed_downloads:
        list_failed_videos(failed_downloads)
    print("+--------------------+")


def new_download_playlist_audio(url:str) -> None:
    playlist = Playlist(url, use_po_token=True)
    make_playlist_directory(playlist)
    # Return the path variable I guess?

    downloaded_videos = 0
    failed_videos = []

    for video in playlist.videos:
        try:
            print("Lol")

        except Exception as error:
            print("Womp womp")
            continue


def download_playlist_video(url:str) -> None:
    playlist = Playlist(url)
    playlist_title = playlist.title

    playlist_folder = DOWNLOAD_PATH / playlist_title
    playlist_folder.mkdir(parents=True, exist_ok=True)
    downloaded_videos = 0

    for video in playlist.videos:
        try:
            print(video.title)
            yt_stream = video.streams.get_by_resolution(720)
            yt_stream.download(output_path=playlist_folder,
                               filename_prefix=f"{downloaded_videos + 1} - ",
                               max_retries=3)
            downloaded_videos += 1

        except Exception as error:
            print(f"Error! Can't find video. ({error})")
            continue

    print(f"Process complete: {downloaded_videos} videos downloaded.")
    print("+--------------------+")


if __name__ == '__main__':
    main()