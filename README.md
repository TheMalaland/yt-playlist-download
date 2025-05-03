# YouTube Playlist Downloader

This project is a Python-based tool that allows you to download videos and/or audio from YouTube playlists concurrently using the `yt-dlp` library. It supports downloading the best available video and audio quality or extracting audio-only files in MP3 format.

## Features

- **Concurrent Downloads**: Downloads multiple videos or audio files simultaneously to save time.
- **Audio-Only Option**: Converts audio to MP3 format with high quality (320 kbps).
- **Customizable Output**: Files are saved in a structured folder format based on the playlist and file type.
- **Error Handling**: Skips problematic videos and continues downloading the rest of the playlist.

## Requirements

- **Python**: Version 3.7 or higher.
- **pip**: Python's package manager.
- **ffmpeg**: Required for audio extraction and conversion to MP3.

## Installation

1. Clone this repository or download the project files.
2. Ensure you have Python and `pip` installed on your system.
3. Install the required dependencies by running the `setup_program.bat` file:

    ```bash
    [setup_program.bat](http://_vscodecontentref_/2)
    ```