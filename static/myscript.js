var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.MapQuest({layer: 'sat'})
          })
        ],
        view: new ol.View({
          center: ol.proj.transform([0, 0], 'EPSG:4326', 'EPSG:3857'),
          zoom: 0
        })
      });

var vector = new ol.layer.Vector({
    source: new ol.source.GeoJSON({
        url: '/map/static_geojson',
        projection: 'EPSG:3857'
    })
});

// Source retrieving data in GeoJSON format using AJAX
var vectorSource = new ol.source.ServerVector({
    format: new ol.format.GeoJSON(),
    loader: function(extent, resolution, projection) {
        var url = '/map/dynamic_geojson?'+
            'bbox=' + extent.join(',');

        $.ajax({
            url: url
        })
        .done(function(response) {
            //var features = vectorSource.getFeatures();
            //for(var i=0; i< features.length && i<10; i++) {
            //        vectorSource.removeFeature(features[i]);
            //    }
            vectorSource.addFeatures(vectorSource.readFeatures(response));
        });
    },
    projection: 'EPSG:3857'
});

// Vector layer
var vectorLayer = new ol.layer.Vector({
    source: vectorSource
});

map.addLayer(vectorLayer);