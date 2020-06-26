# MapUsiingFoulimLibByPython
folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via folium.
folium makes it easy to visualize data that’s been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map.

The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. folium supports both Image, Video, GeoJSON and TopoJSON overlays.
the parameters are used :
Parameters
location (tuple or list, default None) – Latitude and Longitude of Map (Northing, Easting).

width (pixel int or percentage string (default: '100%')) – Width of the map.

height (pixel int or percentage string (default: '100%')) – Height of the map.

tiles (str, default 'OpenStreetMap') – Map tileset to use. Can choose from a list of built-in tiles, pass a custom URL or pass None to create a map without tiles. For more advanced tile layer options, use the TileLayer class.

min_zoom (int, default 0) – Minimum allowed zoom level for the tile layer that is created.

max_zoom (int, default 18) – Maximum allowed zoom level for the tile layer that is created.

zoom_start (int, default 10) – Initial zoom level for the map.

attr (string, default None) – Map tile attribution; only required if passing custom tile URL.

crs (str, default 'EPSG3857') – Defines coordinate reference systems for projecting geographical points into pixel (screen) coordinates and back. You can use Leaflet’s values : * EPSG3857 : The most common CRS for online maps, used by almost all free and commercial tile providers. Uses Spherical Mercator projection. Set in by default in Map’s crs option. * EPSG4326 : A common CRS among GIS enthusiasts. Uses simple Equirectangular projection. * EPSG3395 : Rarely used by some commercial tile providers. Uses Elliptical Mercator projection. * Simple : A simple CRS that maps longitude and latitude into x and y directly. May be used for maps of flat surfaces (e.g. game maps). Note that the y axis should still be inverted (going from bottom to top).

control_scale (bool, default False) – Whether to add a control scale on the map.

prefer_canvas (bool, default False) – Forces Leaflet to use the Canvas back-end (if available) for vector layers instead of SVG. This can increase performance considerably in some cases (e.g. many thousands of circle markers on the map).

no_touch (bool, default False) – Forces Leaflet to not use touch events even if it detects them.

disable_3d (bool, default False) – Forces Leaflet to not use hardware-accelerated CSS 3D transforms for positioning (which may cause glitches in some rare environments) even if they’re supported.

zoom_control (bool, default True) – Display zoom controls on the map.

**kwargs – Additional keyword arguments are passed to Leaflets Map class: https://leafletjs.com/reference-1.6.0.html#map

to use this lib you need to install it 
first open cmd then type $ pip install folium
or $ conda install -c conda-forge folium
to learn more open this website https://pypi.org/project/folium/
then install it from your environment like i use PyCharm so all what you need to do to press right click at the red lamp and install it there. :D 
i Wish that explanation is useful best luck and best wishes. 
enjoy with your first map...........
Abdullah :) 
