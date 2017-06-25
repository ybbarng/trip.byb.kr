$(function() {
  var defaultLatLng = [37.475533, 126.964645];
  var defaultScale = 10;
  var latLng = defaultLatLng;
  var scale = defaultScale;
  L.mapbox.accessToken = 'pk.eyJ1IjoieWJiYXJuZyIsImEiOiJjaXl1NTdiZmIwMDE5MzNsZjFjdzU4Z3Z2In0.9KVCtlQf3dDv4_F2ol0ksw';
  var map = new L.mapbox.Map('map', 'mapbox.streets')
    .setView(latLng, scale);

  var PictureMarker = L.Icon.extend({
    options: {
      iconSize: [100, 56.25],
      iconAnchor: [50, 28.125]
    }
  });

  var PictureMarkerTemplates = {
  };

  var pictureMarkers = new Map();
  $.get('/pictures/', function(pictures) {
    console.log(pictures);
    for (var i = 0; i < pictures.length; i++) {
      var picture = pictures[i];
      var picture_path = picture[0];
      var pictureMarker = PictureMarkerTemplates[picture_path];
      if (pictureMarker === undefined) {
        pictureMarker = new PictureMarker({
          iconUrl: picture_path
        });
        PictureMarkerTemplates[picture_path] = pictureMarker;
      }
      var marker = new L.marker(
        [picture[1], picture[2]],
        {icon: pictureMarker});
      if (!pictureMarkers.has(picture_path)) {
        map.addLayer(marker);
        pictureMarkers.set(picture_path, marker);
      }
    }
  });
});
