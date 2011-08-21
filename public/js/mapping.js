$(document).ready(function () {
  vectors = null;
  var map, highlightCtrl, layer, popup, lonlat;

  OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {

    defaultHandlerOptions: {
      'single': true,
      'double': false,
      'pixelTolerance': 0,
      'stopSingle': false,
      'stopDouble': false
    },

    initialize: function (options) {
      this.handlerOptions = OpenLayers.Util.extend({}, this.defaultHandlerOptions);
      OpenLayers.Control.prototype.initialize.apply(
      this, arguments);
      this.handler = new OpenLayers.Handler.Click(
      this, {
        'click': this.trigger
      }, this.handlerOptions);
    },


    trigger: function (e) {
      lonlat = map.getLonLatFromViewPortPx(e.xy);

      var popupHTML = "<div style='font-size:.8em'>w00t!<br>" + "<img src='http://news.nationalgeographic.com/news/images/thumbs/070316-gorilla-lice_170.jpg'><br>" + "I cAn haZ teH treez at " + lonlat + "?</div>" + "<button type='button' OnClick='drawTreeDot();'>YES</button>" + "<button type='button' OnClick='popupDestroy();'>NO</button>";


      popup = new OpenLayers.Popup.FramedCloud("chicken", lonlat, null, popupHTML, null, true, null);
      popup.autoSize = true;
      map.addPopup(popup);

      // popups will disapear when map is clicked in another location
      // also, the OnClick / close box functionality of the popup and 
      // its yes/no boxes will draw a tree (if yes) and close the popup
      map.events.register("click", map, popupDestroy);
      vectors.events.register("click", highlightCtrl, popupDestroy);
    }

  });


  map = new OpenLayers.Map('map');

  layer = new OpenLayers.Layer.OSM.Mapnik("OpenStreetMap (Mapnik)", {
    isBaseLayer: true
  });

  var defStyle = {
    fillColor: "green",
    fillOpacity: "0.0"
  };
  var sty = OpenLayers.Util.applyDefaults(defStyle, OpenLayers.Feature.Vector.style["default"]);
  var sm = new OpenLayers.StyleMap({
    'default': sty,
    'select': {
      strokeColor: "red",
      fillColor: "red"
    }
  });
  sm.styles['default'].addRules([
  new OpenLayers.Rule({
    filter: new OpenLayers.Filter.Comparison({
      type: OpenLayers.Filter.Comparison.EQUAL_TO,
      property: "type",
      value: "tree"
    }),
    symbolizer: {
      fillColor: "38FF60",
      fillOpacity: "1.0"
    }
  }), new OpenLayers.Rule({
    elseFilter: true
  })]);

  vectors = new OpenLayers.Layer.Vector("vector", {
    styleMap: sm
  });

  vectors.addFeatures(neighborhoodFeatures);

  var report = function (e) {
      OpenLayers.Console.log(e.type, e.feature.id);
    };

  highlightCtrl = new OpenLayers.Control.SelectFeature(vectors, {
    hover: true,
    highlightOnly: true,
    renderIntent: "temporary",
    eventListeners: {
      beforefeaturehighlighted: report,
      featurehighlighted: report,
      featureunhighlighted: report,
    },
  });
  var selectCtrl = new OpenLayers.Control.SelectFeature(vectors, {
    clickout: true
  });
  map.addControl(highlightCtrl);
  map.addControl(selectCtrl);
  highlightCtrl.activate();
  selectCtrl.activate();

  //map.addControl(new OpenLayers.Control.EditingToolbar(vectors));
  //map.addControl(new OpenLayers.Control.LayerSwitcher());
  map.addControl(new OpenLayers.Control.MousePosition());

  var sf = new OpenLayers.Control.SelectFeature(vectors);
  map.addControl(sf);
  sf.activate();

  map.addLayers([layer, vectors]);


  var click = new OpenLayers.Control.Click();
  map.addControl(click);
  click.activate();

  map.setCenter(
  new OpenLayers.LonLat(-122.45, 37.77).transform(
  new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject()), 13);

});


  /*
   * Destroy popup and stop event
   */

  function popupDestroy(e) {
    popup.destroy();
    popup = null;
    OpenLayers.Util.safeStopPropagation(e);
  }

  function drawTreeDot() {
    var origin_xy = new OpenLayers.Geometry.Point(lonlat.lon, lonlat.lat);
    var circle = OpenLayers.Geometry.Polygon.createRegularPolygon(origin_xy, 35, 20, 0);
    vectors.addFeatures([new OpenLayers.Feature.Vector(circle, {
      type: "tree"
    })]);
    popupDestroy();
  }
