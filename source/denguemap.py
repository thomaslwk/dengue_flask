# import folium 
# import json
# import folium.plugins import FastMarkerCluster

# def make_folium_map():
#     folium_map = folium.Map(location=[1.3521, 103.8198], 
#                              zoom_start=13)
#     # img = folium.raster_layers.ImageOverlay(map_overlay,
#     #                                         bounds=[(max_lat - delta_lat, min_lon), (max_lat, max_lon)],
#     #                                          opacity=1,
#     #                                          name="Paths")

#     # img.add_to(folium_map)
#     # folium.LayerControl().add_to(folium_map)
#     return folium_map._repr_html_()

import folium
import json
from folium.plugins import FastMarkerCluster

# Declaring the location of the Map
def make_folium_map(): 
    sg_map = folium.Map(center=[1.3649170000000002, 103.82287200000002], zoom_start=12, min_zoom=12, max_zoom=16)
    sg_map.add_child(south_east)
    sg_map.add_child(north_east)
    sg_map.add_child(south_west)
    sg_map.add_child(north_west)
    sg_map.add_child(central)
    return sg_map._repr_html_()

# sg_map = folium.Map(center=[1.3649170000000002, 103.82287200000002], zoom_start=12, min_zoom=12, max_zoom=16)
# FUNCTION USED TO SET CLUSTER COUNT + COLOR
icon_create_function = """
    function(cluster) {
    var childCount = cluster.getChildCount();
    var c = ' marker-cluster-large';

    return new L.DivIcon({ html: '<div><span>' + childCount + '</span></div>', className: 'marker-cluster' + c, iconSize: new L.Point(40, 40)  });
    }
    """

callback_string = """ 
    function (row) {
                    var icon = L.AwesomeMarkers.icon({
                        icon: 'exclamation-sign',
                        markerColor: 'red'
                    });
                    var marker = L.marker(new L.LatLng(row[0], row[1]));
                    marker.setIcon(icon);
                    return marker;
"""

# Function takes in a list, returns after sorting.
def json_filter(filename):
    # RETRIEVING DATA FROM NORTH EAST DATA FILE
    with open(filename) as ne:
        json_data = json.load(ne)

    # Obtaining the list from Key:Value | "Features":[]
    json_list = json_data['features']
    json_data_coordinates = []
    for x in range(len(json_list)):
        data_set = json_list[x]
        for i in range(len(data_set['geometry']['coordinates'][0])):
            thisTuple = (data_set['geometry']['coordinates'][0][i][1], data_set['geometry']['coordinates'][0][i][0])
            json_data_coordinates.append(thisTuple)
    return json_data_coordinates

################################################### START OF NORTH EAST #########################################################
# Setting the NORTH EAST Fast Marker Cluster
north_east = FastMarkerCluster(data=json_filter('source/aedes-mosquito-breeding-habitats-south-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)
# Adding the Cluster to the Map
# sg_map.add_child(north_east)
################################################### END OF NORTH EAST #########################################################

################################################### START OF NORTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
north_west = FastMarkerCluster(data=json_filter('source/aedes-mosquito-breeding-habitats-north-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(north_west)
################################################### END OF NORTH WEST #########################################################

################################################### START OF SOUTH EAST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_east = FastMarkerCluster(data=json_filter('source/aedes-mosquito-breeding-habitats-south-east-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(south_east)
################################################### END OF SOUTH EAST #########################################################

################################################### START OF SOUTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_west = FastMarkerCluster(data=json_filter('source/aedes-mosquito-breeding-habitats-south-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(south_west)
################################################### END OF SOUTH WEST #########################################################

################################################### START OF CENTRAL #########################################################
# THIS LINE CREATES THE CENTRAL CLUSTER
central = FastMarkerCluster(data=json_filter('source/aedes-mosquito-breeding-habitats-central-geojson.geojson'), name='Cluster Icons',
                            icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(central)
################################################### END OF CENTRAL #########################################################

