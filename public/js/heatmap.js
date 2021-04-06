var myMap = L.map("map", {
  center: [41.2119, -99.1842],
  zoom: 5
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 17,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);


d3.csv("Resources/Original Data/bfro_reports_geocoded.csv", function(data) {

  var heatArray = [];

  for (var i = 0; i < data.length; i++) {

    var geohash = data[i].geohash;

    if (geohash) {
      console.log(data[i].longitude);
      console.log(data[i].latitude);
      
      heatArray.push([data[i].latitude, data[i].longitude]);
    }
  }

  var heat = L.heatLayer(heatArray, {
    max: .028,
    radius: 50,
    blur: 35
  }).addTo(myMap);

});

