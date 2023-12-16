document.addEventListener('DOMContentLoaded', function() {
    var badgeContainer = document.getElementById('tryhackme-badge');
    if (badgeContainer) {
        var script = document.createElement('script');
        script.src = 'https://tryhackme.com/badge/270763';
        script.onload = function() {
            // Handle successful loading
        };
        script.onerror = function() {
            // Handle errors (e.g., content blocked by CSP)
            console.error('TryHackMe badge script could not be loaded.');
        };
        badgeContainer.appendChild(script);
    }
});

