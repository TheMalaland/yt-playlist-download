import yt_dlp
import os
import time
import random
from concurrent.futures import ThreadPoolExecutor
from yt_dlp.utils import DownloadError

def download_video_and_audio(option, playlist_url, base_folder):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio combined
        'outtmpl': os.path.join(base_folder, '%(playlist)s/%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    if option == "audio_only":
        ydl_opts.update({
            'format': 'bestaudio/best',  # Download only the best audio
            'outtmpl': os.path.join(base_folder, '%(playlist)s/audio/%(title)s.%(ext)s')
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except DownloadError as e:
        print(f"Error downloading video: {e}")

def progress_hook(d):
    print(f"Downloading: {d['filename']} | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")

def download_videos_concurrently(option, playlist_urls, base_folder):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in playlist_urls:
            futures.append(executor.submit(download_video_and_audio, option, url, base_folder))
            time.sleep(random.uniform(1, 3))  # Random delay between downloads to avoid detection

        for future in futures:
            future.result()

def main():
    # URLs de las playlists y carpeta base
    playlist_urls = input("Enter the playlist URLs (comma separated): ").split(',')
    base_folder = "C:\\Users\\rodri\\Music"
    
    # Opción del usuario
    print("Choose an option:")
    print("1. Video & Audio")
    print("2. Audio Only")
    
    option = input("Enter the number for your option (1/2): ")
    option = "audio_only" if option == "2" else "video_audio"

    download_videos_concurrently(option, playlist_urls, base_folder)

if __name__ == "__main__":
    main()