import folium
import json
from folium.plugins import FastMarkerCluster
from folium.plugins import FeatureGroupSubGroup

"""
    Function Name: make_folium_map()
    Variable: NILL
    Description: The function generates and returns folium map object. 
    The folium object contains 
        - FastMarkerCluster groups
        - Feature Groups 
    Output: Folium Map Object   
"""


# Declaring the location of the Map
def make_folium_map():
    sg_map = folium.Map(location=[1.3649170000000002, 103.82287200000002], min_zoom=12, zoom_start=12, max_zoom=18,
                        width='85%',
                        height='85%')

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

    return sg_map


# STRING IS USED TO SET CLUSTER SIZE + COLOR
icon_create_function = """
    function(cluster) {
    var childCount = cluster.getChildCount();
    var c = ' marker-cluster-large';

    return new L.DivIcon({ html: '<div><span>' + childCount + '</span></div>', className: 'marker-cluster' + c, iconSize: new L.Point(40, 40)  });
    }
    """
# ----------------------------------------------------------------------------------------------------------------------------
"""
    Function Name: json_filter(filename)
    
    Variable: 
        - filename: Dengue Data json file
    
    Description: The function takes in json data and returns a list of tuples with the tuple containing latitude & Longitude 
    of dengue clusters
    
    The list output example:
     [ (latitude,longitude) ] 
    
    Output: List of tuples containing coordinates. 
"""


# Function takes in a list, returns after sorting.
def json_filter(filename, condition):
    # RETRIEVING DATA FROM NORTH EAST DATA FILE
    with open(filename) as ne:
        json_data = json.load(ne)

    # Obtaining the list from Key:Value | "Features":[]
    json_list = json_data['features']
    json_data_coordinates = []
    for x in range(len(json_list)):
        data_set = json_list[x]
        for i in range(len(data_set['geometry']['coordinates'][0])):
            coordinateTuple = (
            data_set['geometry']['coordinates'][0][i][1], data_set['geometry']['coordinates'][0][i][0])
            json_data_coordinates.append(coordinateTuple)
    if condition == 1:
        return json_data_coordinates
    elif condition == 2:
        return len(json_data_coordinates)

   


################################################### START OF NORTH EAST #########################################################
# Setting the NORTH EAST Fast Marker Cluster
north_east = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-east-geojson.geojson',1),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

################################################### END OF NORTH EAST #########################################################

################################################### START OF NORTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
north_west = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-west-geojson.geojson',1),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

################################################### END OF NORTH WEST #########################################################

################################################### START OF SOUTH EAST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_east = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-east-geojson.geojson',1),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

################################################### END OF SOUTH EAST #########################################################

################################################### START OF SOUTH WEST #########################################################
# THIS LINE CREATES THE NORTH WEST CLUSTER
south_west = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-west-geojson.geojson',1),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)

################################################### END OF SOUTH WEST #########################################################

################################################### START OF CENTRAL #########################################################
# THIS LINE CREATES THE CENTRAL CLUSTER
central = FastMarkerCluster(
    data=json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-central-geojson.geojson',1),
    name='Cluster Icons',
    icon_create_function=icon_create_function, control=False)


################################################### END OF CENTRAL #########################################################

"""
    Function Name: list_compare()
    Variable: NILL
    Description: Function to compare number of cases per region. 
    Output: Return region with highest number of cases. 
"""

## Compare function to store each count into a dict, with corresponding area
def list_compare():
    # Create a dict to store all location and hold count of case per region.
    dictc = {'North-east': [],
             'North-west': [], 'South-east': [], 'South-west': [], 'Central': []}

    north_east = json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-east-geojson.geojson',2)
    north_west = json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-north-west-geojson.geojson',2)
    south_east = json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-east-geojson.geojson',2)
    south_west = json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-south-west-geojson.geojson',2)
    central = json_filter('source/dengue_data/aedes-mosquito-breeding-habitats-central-geojson.geojson',2)

    # Store data into dict location. 
    dictc['North-east'].append(north_east)
    dictc['North-west'].append(north_west)
    dictc['South-west'].append(south_west)
    dictc['South-east'].append(south_east)
    dictc['Central'].append(central)
    # Return max dict value. 
    return max(dictc, key=dictc.get)
