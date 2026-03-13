document.addEventListener('DOMContentLoaded', function () {
    const target = document.getElementById('typing-effect');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (!target) {
        return;
    }

    if (reducedMotion.matches) {
        target.textContent = 'Cyber Threat Detection Engineer';
        return;
    }

    const phrases = [
        'Cyber Threat Detection Engineer',
        'Detection Engineering | Purple Team Ops',
        'SOC Monitoring | SIEM | ATT&CK Mapping'
    ];

    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function tick() {
        const current = phrases[phraseIndex];

        if (isDeleting) {
            charIndex -= 1;
        } else {
            charIndex += 1;
        }

        target.textContent = current.slice(0, charIndex);

        let delay = isDeleting ? 35 : 70;

        if (!isDeleting && charIndex === current.length) {
            delay = 1600;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            delay = 220;
        }

        window.setTimeout(tick, delay);
    }

    tick();
});
