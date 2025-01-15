import yt_dlp
import os
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor
from yt_dlp.utils import DownloadError

def download_video_and_audio(option, playlist_url, base_folder):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Download best video and audio in MP4 format
        'outtmpl': os.path.join(base_folder, '%(playlist)s/%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    if option == "audio_only":
        ydl_opts.update({
            'format': 'bestaudio/best',  # Download only the best audio
            'outtmpl': os.path.join(base_folder, '%(playlist)s/audio/%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except DownloadError as e:
        print(f"Error downloading video: {e}")

def progress_hook(d):
    try:
        print(f"Downloading: {d['filename']} | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")
    except UnicodeEncodeError:
        print("Downloading: [filename with special characters] | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")

def download_videos_concurrently(option, playlist_urls, base_folder):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in playlist_urls:
            futures.append(executor.submit(download_video_and_audio, option, url, base_folder))
            time.sleep(random.uniform(1, 3))  # Random delay between downloads to avoid detection

        for future in futures:
            future.result()

def main():
    if len(sys.argv) != 3:
        print("Usage: python video_and_audio.py <playlist_urls> <option>")
        sys.exit(1)

    playlist_urls = sys.argv[1].split(',')
    option = sys.argv[2]
    base_folder = "C:\\Users\\rodri\\Music"

    start_time = time.time()  # Record the start time
    download_videos_concurrently(option, playlist_urls, base_folder)
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time
    print(f"All downloads are complete. Files are saved in: {base_folder}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()