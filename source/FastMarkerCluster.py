import folium
import json
from folium.plugins import FastMarkerCluster

# Declaring the location of the Map
sg_map = folium.Map(center=[1.3649170000000002, 103.82287200000002], zoom_start=12, min_zoom=12, max_zoom=16)

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
        north_east_data = json.load(ne)

    # Obtaining the list from Key:Value | "Features":[]
    north_east_list = north_east_data['features']
    north_east_coordinates = []
    for x in range(len(north_east_list)):
        data_set = north_east_list[x]
        for i in range(len(data_set['geometry']['coordinates'][0])):
            thisTuple = (data_set['geometry']['coordinates'][0][i][1], data_set['geometry']['coordinates'][0][i][0])
            north_east_coordinates.append(thisTuple)
    return north_east_coordinates


################################################### START OF NORTH EAST #########################################################
# Setting the NORTH EAST Fast Marker Cluster
north_east = FastMarkerCluster(data=json_filter('aedes-mosquito-breeding-habitats-south-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)
# Adding the Cluster to the Map
sg_map.add_child(north_east)
################################################### END OF NORTH EAST #########################################################

################################################### START OF NORTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
north_west = FastMarkerCluster(data=json_filter('aedes-mosquito-breeding-habitats-north-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
sg_map.add_child(north_west)
################################################### END OF NORTH WEST #########################################################

################################################### START OF SOUTH EAST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_east = FastMarkerCluster(data=json_filter('aedes-mosquito-breeding-habitats-south-east-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
sg_map.add_child(south_east)
################################################### END OF SOUTH EAST #########################################################

################################################### START OF SOUTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_west = FastMarkerCluster(data=json_filter('aedes-mosquito-breeding-habitats-south-west-geojson.geojson'), name='Cluster Icons',
                               icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
sg_map.add_child(south_west)
################################################### END OF SOUTH WEST #########################################################

################################################### START OF CENTRAL #########################################################
# THIS LINE CREATES THE CENTRAL CLUSTER
central = FastMarkerCluster(data=json_filter('aedes-mosquito-breeding-habitats-central-geojson.geojson'), name='Cluster Icons',
                            icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
sg_map.add_child(central)
################################################### END OF CENTRAL #########################################################

sg_map.save("pls_work.html")
