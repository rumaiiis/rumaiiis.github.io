document.addEventListener("DOMContentLoaded", function() {
    function createMatrixEffect(containerId) {
        var canvas = document.createElement('canvas'),
            ctx = canvas.getContext('2d');

        document.getElementById(containerId).appendChild(canvas);

        canvas.width = window.innerWidth * 0.15; // Adjust width to 15% of window
        canvas.height = window.innerHeight;

        var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%'.split('');
        var fontSize = 10, columns = canvas.width / fontSize;
        var drops = Array.from({ length: columns }).fill(1);

        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#0F0'; // Green text
            ctx.font = fontSize + 'px arial';

            for (let i = 0; i < drops.length; i++) {
                var text = characters[Math.floor(Math.random() * characters.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.95) drops[i] = 0;
                drops[i]++;
            }
        }

        setInterval(draw, 33);
    }

    createMatrixEffect("matrix-panel-left");
    createMatrixEffect("matrix-panel-right");
});

