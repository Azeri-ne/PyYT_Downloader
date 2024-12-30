from pytubefix import YouTube, Playlist
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

def main() -> None:
    download_single_video(r'https://www.youtube.com/watch?v=GkFqe3tZVpg&pp=ygURaG90IHBvdCBjb21tYW5kZXI%3D', [720, 1080])

def handle_playlist_error(error, failed_downloads, 
                          downloaded_videos, video) -> None:
            print(f"Error! Can't find video. ({error})")
            failed_downloads.append(video.title)
            downloaded_videos += 1


def list_failed_videos(failed_downloads) -> None:
        print("These audio failed to download:")
        for failed_download in failed_downloads:
            print(failed_download)


def print_border() -> None:
    print("+--------------------+")


def get_audio_stream(url:str) -> str:
    yt = YouTube(url, use_po_token=True)
    print(yt.title)

    audio_stream = yt.streams.get_audio_only()

    return audio_stream

def check_for_valid_resolution(resolution:int) -> bool:
    print(resolution)
    valid_resolutions = [144, 240, 360, 480, 720, 1080]

    if resolution in valid_resolutions:
        print("True")
        return True

    print("False")
    return False

# New get_stream function WIP
def get_stream(url:str, stream_type:str, *resolution:int) -> str:
    if not url.startswith('https://www.youtube.com'):
        print("Error: Invalid URL")
        # Log this
        return None

    if len(resolution) > 1:
        print("Warning: Only one resolution is allowed")

    yt = YouTube(url, use_po_token=True)
    print(yt.title)

    if stream_type == 'audio':
        audio_stream = yt.streams.get_audio_only()

        return audio_stream

    if stream_type == 'video':
        video_resolution = resolution[0]
        if check_for_valid_resolution(video_resolution):
            video_stream = yt.streams.get_by_resolution(video_resolution)
            
            return video_stream

        print("Error: Invalid resolution")
        return None

    print("Error: Stream type is invalid")
    return None


def new_download_stream(url:str, stream_type:str, *resolution:int) -> None:
    if stream_type == 'audio':
        stream = get_stream(url, 'audio')

    if stream_type == 'video':
        # Check for valid resolution here?
        stream = get_stream(url, 'video', resolution)

    try:
        if stream == None:
            raise Exception
        
        stream.download(output_path=DOWNLOAD_PATH)

    except Exception:
        print(f"Error: Download failed")
    print("+--------------------+")

def download_stream(stream:str) -> None:
    try:
        if stream == None:
            raise Exception
        
        stream.download(output_path=DOWNLOAD_PATH)

    except Exception:
        print(f"Error: Download failed")

    print("+--------------------+")

def download_single_audio(url:str) -> None:
    audio_stream = get_stream(url, 'audio')
    download_stream(audio_stream)


def download_single_video(url:str, resolution:int) -> None:
    video_stream = get_stream(url, 'video', resolution)
    download_stream(video_stream)


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
    print_border()


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