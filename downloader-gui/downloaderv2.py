import yt_dlp
import os
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor
from yt_dlp.utils import DownloadError

def progress_hook(d):
    try:
        print(f"Downloading: {d['filename']} | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")
    except UnicodeEncodeError:
        print("Downloading: [filename with special characters] | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")

def download_video_and_audio(option, playlist_url, base_folder):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio combined
        'outtmpl': os.path.join(base_folder, '%(playlist)s/%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    if option == "audio_only":
        ydl_opts.update({
            'format': 'bestaudio/best',  # Download only the best audio
            'outtmpl': os.path.join(base_folder, '%(playlist)s/audio/%(title)s.%(ext)s'),
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except DownloadError as e:
            print(f"Error downloading {playlist_url}: {e}")

def download_videos_concurrently(option, playlist_urls, base_folder):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download_video_and_audio, option, url, base_folder) for url in playlist_urls]
        for future in futures:
            future.result()

def main():
    if len(sys.argv) < 3:
        print("Usage: python downloaderv2.py <urls> <option>")
        sys.exit(1)

    playlist_urls = sys.argv[1].split(',')
    option = sys.argv[2]
    base_folder = "C:\\Users\\rodri\\Music"

    download_videos_concurrently(option, playlist_urls, base_folder)

if __name__ == "__main__":
    main()