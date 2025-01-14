const sidePane = document.getElementById('sidePane');

    // Show the pane when the mouse is on the left edge
    document.addEventListener('mousemove', (event) => {
        if (event.clientX < 50) { // Mouse near the left edge
            sidePane.style.left = '0';
        } else if (event.clientX > 300) { // Mouse away from the pane
            sidePane.style.left = '-300px';
        }
    });