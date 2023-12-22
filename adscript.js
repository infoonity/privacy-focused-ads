// adscript.js

document.addEventListener('DOMContentLoaded', function() {
    const content = document.body.innerText; // Get all text from the body

    fetch('http://127.0.0.1:5000/analyze', { // Update to match your Flask server URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: content })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        displayAd(data.keyword); // Display the ad based on the keyword
    })
    .catch(error => {
        console.error('Error:', error);
        displayAd('default'); // Display a default image in case of an error
    });
});

function displayAd(keyword) {
    const adElement = document.getElementById('ad');
    const imageUrl = getAdImageUrl(keyword);
    adElement.innerHTML = `<img src="${imageUrl}" alt="Ad for ${keyword}">`;
}

function getAdImageUrl(keyword) {
    const adImages = {
//You can change the image URLs here to match where your ad images will be stored. Please have a default image.
        'car': 'http://127.0.0.1:5000/static/images/car.png',
        'carrot': 'http://127.0.0.1:5000/static/images/carrot.png',
        'parrot': 'http://127.0.0.1:5000/static/images/parrot.png',
        'default': 'http://127.0.0.1:5000/static/images/pizza.png' // Default image path
    };
    return adImages[keyword] || adImages['default'];
}
