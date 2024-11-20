from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

URL = r'https://www.youtube.com/watch?v=BwGpXK3W6tE'
CURRENT_DIRECTORY = Path(__file__).parent
DOWNLOAD_PATH = CURRENT_DIRECTORY / 'Downloads'

yt = YouTube(URL, on_progress_callback=on_progress)
print(yt.title)

yt_stream = yt.streams.get_audio_only()
yt_stream.download(output_path=DOWNLOAD_PATH)