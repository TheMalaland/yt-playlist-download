import os
from tqdm import tqdm
import yt_dlp
import re

def sanitize_filename(name):
    return re.sub(r'[\/:*?"<>|]', '', name)

def progress_hook(progress, progress_bar):
    if progress['status'] == 'downloading':
        total = progress.get('total_bytes', 1)
        downloaded = progress.get('downloaded_bytes', 0)
        progress_bar.n = downloaded
        progress_bar.total = total
        progress_bar.refresh()
    elif progress['status'] == 'finished':
        print("\nDownload complete!")


def download_playlist(option, playlist_url, base_folder):

     # Extraer metadatos de la playlist
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        playlist_title = playlist_info.get('title', 'Playlist')
    
    
    playlist_folder = os.path.join(base_folder, sanitize_filename(playlist_title))

 

    output_folder = f"{playlist_folder}"
    video_folder = f"{output_folder}/videos"
    audio_folder = f"{output_folder}/audio"

    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(audio_folder, exist_ok=True)


    if option == "video":
        # Configuración para videos en máxima calidad
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{video_folder}/%(title)s.%(ext)s',
            'progress_hooks': [lambda p: progress_hook(p, progress_bar)],
        }
    elif option == "audio":
        # Configuración para solo audio en máxima calidad
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{audio_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'progress_hooks': [lambda p: progress_hook(p, progress_bar)],
        }
    else:
        print("Invalid option. Use 'video' or 'audio'.")
        return

    progress_bar = tqdm(desc="Downloading Playlist", unit="bytes", unit_scale=True)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    progress_bar.close()
    print(f"Playlist downloaded to: {output_folder}")


# Ejemplo de uso
if __name__ == "__main__":
    print("Select an option:")
    print("1. Download Videos")
    print("2. Download Audios")
    choice = input("Enter your choice (1/2): ")

    playlist_url = input("Enter the playlist URL: ")

    base_folder = "C:\\Users\\rodri\\Music"

    if choice == "1":
        download_playlist("video", playlist_url, base_folder)
    elif choice == "2":
        download_playlist("audio", playlist_url, base_folder)
    else:
        print("Invalid choice.")
