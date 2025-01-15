import yt_dlp
import os
import time
import random
import logging
from concurrent.futures import ThreadPoolExecutor
from yt_dlp.utils import DownloadError

# Configuración del registro de actividad
logging.basicConfig(filename='download.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_video_and_audio(option, playlist_url, base_folder, retries=3):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio combined
        'outtmpl': os.path.join(base_folder, '%(playlist)s/%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'external_downloader': 'aria2c',  # Use aria2c as external downloader
        'external_downloader_args': ['-x', '16', '-k', '1M'],  # Configure aria2c
        'ratelimit': '500K',  # Set rate limit to avoid throttling
    }

    if option == "audio_only":
        ydl_opts.update({
            'format': 'bestaudio/best',  # Download only the best audio
            'outtmpl': os.path.join(base_folder, '%(playlist)s/audio/%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    for attempt in range(retries):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([playlist_url])
            logging.info(f"Successfully downloaded: {playlist_url}")
            break  # Break if download is successful
        except DownloadError as e:
            logging.error(f"Error downloading video (attempt {attempt + 1}): {e}")
            if attempt + 1 == retries:
                logging.error(f"Failed to download video after {retries} attempts: {playlist_url}")
        except Exception as e:
            logging.error(f"Unexpected error (attempt {attempt + 1}): {e}")
            if attempt + 1 == retries:
                logging.error(f"Failed to download video after {retries} attempts: {playlist_url}")

def progress_hook(d):
    logging.info(f"Downloading: {d['filename']} | {d.get('percent', 'N/A')}% | {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")

def download_videos_concurrently(option, playlist_urls, base_folder, max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for url in playlist_urls:
            futures.append(executor.submit(download_video_and_audio, option, url, base_folder))
            time.sleep(random.uniform(1, 3))  # Random delay between downloads to avoid detection

        for future in futures:
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error processing future: {e}")

def main():
    try:
        # URLs de las playlists y carpeta base
        playlist_urls = input("Enter the playlist URLs (comma separated): ").split(',')
        base_folder = "C:\\Users\\rodri\\Music"
        
        # Opción del usuario
        print("Choose an option:")
        print("1. Video & Audio")
        print("2. Audio Only")
        
        option = input("Enter the number for your option (1/2): ")
        option = "audio_only" if option == "2" else "video_audio"

        # Configuración de descargas simultáneas
        max_workers = int(input("Enter the number of simultaneous downloads: "))

        download_videos_concurrently(option, playlist_urls, base_folder, max_workers)
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()