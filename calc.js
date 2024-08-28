
window.onload = function() {
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    // Set the fill color to blue
    ctx.fillStyle = '#0000FF';

    // Draw a rectangle at coordinates (50, 50) with width 200 and height 100
    ctx.fillRect(50, 50, 200, 100);
};
