import folium
import json
from folium.plugins import FastMarkerCluster
from folium.plugins import FeatureGroupSubGroup

# Declaring the location of the Map
def make_folium_map():
    sg_map = folium.Map(center=[1.3649170000000002, 103.82287200000002], min_zoom=12, zoom_start=12, max_zoom=18,
                        width='85%',
                        height='85%')
    # sg_map.add_child(south_east)
    # sg_map.add_child(north_east)
    # sg_map.add_child(south_west)
    # sg_map.add_child(north_west)
    # sg_map.add_child(central)

    # Dengue Markers on the Map

    # dengue_markers.add_child(south_east)

    # dengue_markers.add_child(south_west)
    # dengue_markers.add_child(north_west)
    # dengue_markers.add_child(central)

    dengue_cluster = folium.FeatureGroup(name="Dengue Cluster")
    sg_map.add_child(dengue_cluster)

    south_east_grp = FeatureGroupSubGroup(dengue_cluster, 'South East')
    south_east_grp.add_child(south_east)
    sg_map.add_child(south_east_grp)

    South_west_marker = FeatureGroupSubGroup(dengue_cluster, 'South West')
    South_west_marker.add_child(south_west)
    sg_map.add_child(South_west_marker)

    north_east_marker = FeatureGroupSubGroup(dengue_cluster, 'North East')
    north_east_marker.add_child(north_east)
    sg_map.add_child(north_east_marker)

    north_west_marker = FeatureGroupSubGroup(dengue_cluster, 'North West')
    north_west_marker.add_child(north_west)
    sg_map.add_child(north_west_marker)

    central_marker_grp = FeatureGroupSubGroup(dengue_cluster, 'Central')
    central_marker_grp.add_child(central)
    sg_map.add_child(central_marker_grp)


    sg_map.add_child(folium.LayerControl())
    # sg_map.save('templates/map.html')

    return sg_map

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
north_east = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-east-geojson.geojson'),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)
# Adding the Cluster to the Map
# sg_map.add_child(north_east)
################################################### END OF NORTH EAST #########################################################

################################################### START OF NORTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
north_west = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-west-geojson.geojson'),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(north_west)
################################################### END OF NORTH WEST #########################################################

################################################### START OF SOUTH EAST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_east = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-east-geojson.geojson'),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(south_east)
################################################### END OF SOUTH EAST #########################################################

################################################### START OF SOUTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_west = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-west-geojson.geojson'),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(south_west)
################################################### END OF SOUTH WEST #########################################################

################################################### START OF CENTRAL #########################################################
# THIS LINE CREATES THE CENTRAL CLUSTER
central = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-central-geojson.geojson'),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

# Adding the Cluster to the Map
# sg_map.add_child(central)
################################################### END OF CENTRAL #########################################################


## Function to read file 
## -- Dirty fix to return number of items in each json file -- 
def json_fileread(filename):
    with open(filename) as ne: 
        json_data = json.load(ne)
    json_list = json_data['features']
    json_data_coordinates = []
    for x in range(len(json_list)):
        data_set = json_list[x]
        for i in range(len(data_set['geometry']['coordinates'][0])):
            thisTuple = (data_set['geometry']['coordinates'][0][i][1], data_set['geometry']['coordinates'][0][i][0])
            json_data_coordinates.append(thisTuple)
    return len(json_data_coordinates)

## Compare function to store each count into a dict, with corresponding area 
def list_compare():
    dictc = {'North-east':[], 
    'North-west':[], 'South-east':[], 'South-west':[], 'Central':[]}

    north_east = json_fileread('source/dengue_data/aedes-mosquito-breeding-habitats-north-east-geojson.geojson')
    north_west = json_fileread('source/dengue_data/aedes-mosquito-breeding-habitats-north-west-geojson.geojson')
    south_east = json_fileread('source/dengue_data/aedes-mosquito-breeding-habitats-south-east-geojson.geojson')
    south_west = json_fileread('source/dengue_data/aedes-mosquito-breeding-habitats-south-west-geojson.geojson')
    central = json_fileread('source/dengue_data/aedes-mosquito-breeding-habitats-central-geojson.geojson')

    dictc['North-east'].append(north_east)
    dictc['North-west'].append(north_west)
    dictc['South-west'].append(south_west)
    dictc['South-east'].append(south_east)
    dictc['Central'].append(central)
    return max(dictc, key=dictc.get)