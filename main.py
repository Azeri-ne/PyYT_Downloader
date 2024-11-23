from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

def main() -> None:
    download_playlist_audio(r'https://www.youtube.com/playlist?list=PLVjuPmviYbgMHKGawtNzdVCOTprSqKSyJ')


def download_single_video(url:str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yt_stream = yt.streams.get_by_resolution(720)
    try:
        yt_stream.download(output_path=DOWNLOAD_PATH)

    except Exception as error:
        print(f"Error! Can't find video. ({error})")


def download_single_audio(url:str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yt_stream = yt.streams.get_audio_only()
    try:
        yt_stream.download(output_path=DOWNLOAD_PATH)

    except Exception as error:
        print(f"Error! Can't find video. ({error})")


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


def download_playlist_audio(url:str) -> None:
    playlist = Playlist(url)
    playlist_title = playlist.title

    playlist_folder = DOWNLOAD_PATH / playlist_title
    playlist_folder.mkdir(parents=True, exist_ok=True)
    downloaded_videos = 0

    for video in playlist.videos:
        try:
            print(video.title)
            yt_stream = video.streams.get_audio_only()
            yt_stream.download(output_path=playlist_folder,
                               filename_prefix=f"{downloaded_videos + 1} - ",
                               max_retries=3)
            downloaded_videos += 1

        except Exception as error:
            print(f"Error! Can't find video. ({error})")
            continue

    print(f"Process complete: {downloaded_videos} audio downloaded.")


def get_titles_in_playlist(url:str) -> None:
    playlist = Playlist(url)

    for video in playlist.videos:
        try:
            print(video.title)

        except Exception as e:
            print(f"Error! Can't find video. ({e})")
            continue


if __name__ == '__main__':
    main()