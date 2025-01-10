import yt_dlp
import os

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
    
    # Descargar la playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} | {d['percent']}% | {d['speed']} | ETA: {d['eta']}s")
    elif d['status'] == 'finished':
        print(f"Download finished: {d['filename']}")

def main():
    # URL de la playlist y carpeta base
    playlist_url = input("Enter the playlist URL: ")
    base_folder = input("Enter the base folder path: ")
    
    # Opción del usuario
    print("Choose an option:")
    print("1. Video & Audio")
    print("2. Audio Only")
    
    option = input("Enter the number for your option (1/2): ")
    option = "audio_only" if option == "2" else "video_audio"

    download_video_and_audio(option, playlist_url, base_folder)

if __name__ == "__main__":
    main()
