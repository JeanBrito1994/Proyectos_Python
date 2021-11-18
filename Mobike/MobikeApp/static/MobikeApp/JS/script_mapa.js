function iniciarMap(){
    var coord = {lat: -33.4403883,lng:-70.6465029};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    })
    var marker = new google.maps.marker({
        position: coord,
        map: map
    })
}