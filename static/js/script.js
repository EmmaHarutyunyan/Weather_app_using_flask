function openMoonPhase() {
    document.getElementById('moon-modal').style.display = 'flex';
}

function closeMoonPhase() {
    document.getElementById('moon-modal').style.display = 'none';
}


window.onload = function() {
    document.getElementById('temperature').style.display = 'block';
    document.getElementById('temperature-hours').style.display = 'block';
    document.getElementById('map-container').style.display = 'block';
    document.getElementById('city-image').style.display = 'block';

    document.getElementById('temperature').style.opacity = 1;
    document.getElementById('temperature-hours').style.opacity = 1;
    document.getElementById('map-container').style.opacity = 1;
    document.getElementById('city-image').style.opacity = 1;
};