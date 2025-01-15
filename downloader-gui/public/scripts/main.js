document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('download-form');
    const playlistInput = document.getElementById('playlist-urls');
    const optionInput = document.getElementById('download-option');
    const statusMessage = document.getElementById('status-message');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const playlistUrls = playlistInput.value.split(',').map(url => url.trim());
        const option = optionInput.value;

        if (playlistUrls.length === 0 || !option) {
            statusMessage.textContent = 'Please enter valid playlist URLs and select an option.';
            return;
        }

        statusMessage.textContent = 'Downloading...';

        try {
            const response = await fetch('/download', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ playlistUrls, option }),
            });

            if (response.ok) {
                statusMessage.textContent = 'Download started successfully!';
            } else {
                statusMessage.textContent = 'Error starting download. Please try again.';
            }
        } catch (error) {
            statusMessage.textContent = 'An error occurred: ' + error.message;
        }
    });
});