function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            document.getElementById("id_latitude").value = position.coords.latitude;
            document.getElementById("id_longitude").value = position.coords.longitude;
        }, function(error) {
            alert("Error getting location: " + error.message);
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
