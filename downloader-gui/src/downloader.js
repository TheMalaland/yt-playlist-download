const fs = require('fs');
const { exec } = require('child_process');

function downloadVideoAndAudio(option, url, baseFolder) {
    // Logic to download video and audio
    const command = option === 'audio_only' 
        ? `youtube-dl -x --audio-format mp3 -o "${baseFolder}/%(title)s.%(ext)s" ${url}` 
        : `youtube-dl -f bestvideo+bestaudio --merge-output-format mp4 -o "${baseFolder}/%(title)s.%(ext)s" ${url}`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error downloading ${url}: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        console.log(`Downloaded: ${url}`);
    });
}

function downloadVideosConcurrently(option, playlistUrls, baseFolder) {
    const promises = playlistUrls.map(url => {
        return new Promise((resolve) => {
            setTimeout(() => {
                downloadVideoAndAudio(option, url.trim(), baseFolder);
                resolve();
            }, Math.random() * (3000 - 1000) + 1000); // Random delay between 1 to 3 seconds
        });
    });

    return Promise.all(promises);
}

module.exports = {
    downloadVideoAndAudio,
    downloadVideosConcurrently
};