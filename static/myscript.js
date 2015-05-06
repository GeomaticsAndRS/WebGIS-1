var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.MapQuest({layer: 'sat'})
          })
        ],
        view: new ol.View({
          center: ol.proj.transform([37.41, 8.82], 'EPSG:4326', 'EPSG:3857'),
          zoom: 4
        })
      });

var vector = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        url: '/map/static_geojson',
        projection: 'EPSG:3857'
    })
});

map.addLayer(vector);