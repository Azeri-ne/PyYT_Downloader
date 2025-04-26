from pytubefix import YouTube
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

def main() -> None:
    download_single_audio('https://www.youtube.com/watch?v=GRxofEmo3HA')


def check_for_valid_resolution(resolution:int) -> bool:
    valid_resolutions = [144, 240, 360, 480, 720, 1080]

    if resolution in valid_resolutions:
        return True

    return False


def check_for_valid_url(url:str) -> bool:
    if url.startswith('https://www.youtube.com'):
        return True

    return False


def download_stream(stream:str) -> None:
    try:
        stream.download(output_path=DOWNLOAD_PATH)

    except Exception as error:
        print(f"Error: {error}")
    print("+--------------------+")


def get_audio_stream(url:str) -> str:
    if not check_for_valid_url(url):
        print("Error: Invalid URL")
        return None

    yt = YouTube(url, use_po_token=True)

    print(yt.title)
    audio_stream = yt.streams.get_audio_only()

    return audio_stream


def get_video_stream(url:str, resolution:int) -> str:
    if not check_for_valid_url(url):
        print("Error: Invalid URL")
        return None

    if not check_for_valid_resolution(resolution):
        print("Error: Invalid resolution")
        return None

    yt = YouTube(url, use_po_token=True)

    print(f'Downloading: {yt.title}')
    video_stream = yt.streams.get_by_resolution(resolution)

    return video_stream


def download_single_audio(url:str) -> None:
    audio_stream = get_audio_stream(url)

    try:
        if audio_stream == None:
            raise ValueError("Stream is None")
        download_stream(audio_stream)

    except Exception as error:
        print(f"Error: {error}")


def download_single_video(url:str, resolution:int) -> None:
    video_stream = get_video_stream(url, resolution)

    try:
        if video_stream == None:
            raise ValueError("Stream is None")
        download_stream(video_stream)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == '__main__':
    main()