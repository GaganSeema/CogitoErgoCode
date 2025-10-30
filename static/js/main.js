document.getElementById('generate-btn').addEventListener('click', () => {
    const prompt = document.getElementById('prompt-input').value;
    const generateBtn = document.getElementById('generate-btn');
    const generatedImage = document.getElementById('generated-image');

    generateBtn.disabled = true;
    generateBtn.textContent = 'Generating...';
    generatedImage.src = '';

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    })
    .then(response => response.json())
    .then(data => {
        generatedImage.src = data.image_url;
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Image';
    })
    .catch(error => {
        console.error('Error:', error);
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Image';
    });
});
