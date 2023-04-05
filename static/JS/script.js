let btn_loc = document.querySelector("#get_gps");
const txtloc = document.querySelector("#rlocation")

if (btn_loc){
    btn_loc.addEventListener('click', getLocation);
}


function getLocation() {
    /* get user location */
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        txtloc.value = "Geolocation is not supported my browser!"
    }
}

function showPosition(position) {
    /* get longtude and latitude */
    txtloc.value = position.coords.latitude +","+ position.coords.longitude;
}
