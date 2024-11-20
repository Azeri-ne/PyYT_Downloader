from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'


def main() -> None:
    download_single_audio(r'https://www.youtube.com/watch?v=uAXEFoUqvig&pp=ygUuYmVjb21pbmcgaW5zYW5lIGluZmVjdGVkIG11c2hyb29tIGFuZCB3YXJyaW9ycw%3D%3D')


def download_single_video(url) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yt_stream = yt.streams.get_by_resolution('720p')
    yt_stream.download(output_path=DOWNLOAD_PATH)


def download_single_audio(url) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yt_stream = yt.streams.get_audio_only()
    yt_stream.download(output_path=DOWNLOAD_PATH)


if __name__ == '__main__':
    main()