from pytubefix import YouTube, Playlist
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

def main() -> None:
    pass


def get_audio_stream(url:str) -> str:
    yt = YouTube(url, 
                 use_po_token=True)
    print(yt.title)

    audio_stream = yt.streams.get_audio_only()

    return audio_stream


def download_single_audio(url:str) -> None:
    audio_stream = get_audio_stream(url)
    try:
        audio_stream.download(output_path=DOWNLOAD_PATH)

    except Exception as error:
        print(f"Error! Download failed: ({error})")
    print("+--------------------+")


def download_playlist_audio(url:str) -> None:
    playlist = Playlist(url, use_po_token=True)
    playlist_title = playlist.title

    playlist_folder = DOWNLOAD_PATH / playlist_title
    playlist_folder.mkdir(parents=True, exist_ok=True)
    downloaded_videos = 0

    failed_downloads = []

    for video in playlist.videos:
        try:
            audio_stream = get_audio_stream(url)
            audio_stream.download(output_path=playlist_folder,
                               filename_prefix=f"{downloaded_videos + 1} - ",
                               max_retries=3)
            downloaded_videos += 1

        except Exception as error:
            print(f"Error! Can't find video. ({error})")
            failed_downloads.append(video.title)
            downloaded_videos += 1

            continue

    print(f"Process complete: {downloaded_videos} audio downloaded.")
    if failed_downloads:
        print("These audio failed to download:")
        for failed_download in failed_downloads:
            print(failed_download)
    print("+--------------------+")


def download_single_video(url:str) -> None:
    yt = YouTube(url,
                 use_po_token=True)
    print(yt.title)

    yt_stream = yt.streams.get_by_resolution(1440)
    try:
        yt_stream.download(output_path=DOWNLOAD_PATH)

    except Exception as error:
        print(f"Error! Can't find video. ({error})")
    print("+--------------------+")


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


def get_titles_in_playlist(url:str) -> None:
    playlist = Playlist(url)

    for video in playlist.videos:
        try:
            print(video.title)

        except Exception as e:
            print(f"Error! Can't find video. ({e})")
            continue
    print("+--------------------+")


if __name__ == '__main__':
    main()