document.addEventListener('DOMContentLoaded', function() {
    const text = 'RUMAIS - A Cybersecurity Odyssey';
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            document.getElementById('typing-effect').innerHTML += text.charAt(index);
            index++;
            setTimeout(typeEffect, 100); // Adjust speed here
        }
    }

    typeEffect();
});

