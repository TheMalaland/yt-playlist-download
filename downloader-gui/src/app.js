const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

// Cambia la ruta para apuntar a la carpeta 'public' fuera de 'src'
app.use(express.static(path.join(__dirname, '..', 'public')));
app.use(express.json());

app.post('/download', (req, res) => {
    const { urls, option } = req.body;
    console.log(`Received download request: URLs=${urls}, Option=${option}`);
    const command = `python ../video_and_audiov2.py "${urls.join(',')}" "${option}"`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send('Error executing download script');
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
        res.send('Download started');
    });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});