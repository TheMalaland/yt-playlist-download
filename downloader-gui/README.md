# Downloader GUI

This project is a user-friendly GUI for downloading videos and audio from playlists. It is built using Node.js and provides a simple interface for users to input playlist URLs and select download options.

## Project Structure

```
downloader-gui
├── public
│   ├── index.html        # Main HTML document for the user interface
│   ├── styles.css       # Styles for the UI
│   └── scripts
│       └── main.js      # JavaScript for handling user interactions
├── src
│   ├── app.js           # Entry point of the Node.js application
│   ├── downloader.js     # Logic for downloading videos and audio
│   └── routes
│       └── index.js     # Defines routes for the application
├── package.json         # Configuration file for npm
├── .gitignore           # Specifies files to be ignored by Git
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd downloader-gui
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   ```
   npm start
   ```

4. **Open your browser** and navigate to `http://localhost:3000` to access the downloader GUI.

## Usage Guidelines

- Enter the playlist URLs in the input field, separated by commas.
- Choose the download option (Video & Audio or Audio Only).
- Click the download button to start the downloading process.

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.