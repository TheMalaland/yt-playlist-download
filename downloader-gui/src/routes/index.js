const express = require('express');
const router = express.Router();
const { downloadVideos } = require('../downloader');

// Route to handle downloading videos
router.post('/download', async (req, res) => {
    const { playlistUrls, option } = req.body;

    try {
        await downloadVideos(option, playlistUrls);
        res.status(200).json({ message: 'Download started successfully.' });
    } catch (error) {
        res.status(500).json({ message: 'Error starting download.', error: error.message });
    }
});

module.exports = router;