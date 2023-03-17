const btn_loc = document.getElementById("get_gps");
const txtloc = document.getElementById("location")

btn_loc.addEventListener("click", showPosition);

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else {
        txtloc.value = "Geolocation is not supported my browser!"
    }
}

function showPosition(position) {
    txtloc.value = position.coords.latitude +","+ position.coords.longitude;
}
