## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Script: Create-UpdateViewDefinitionHostedFeatureLayer.py
## Goal: To create a view and update view definition query of a hosted feature layer
## Author: Imtiaz Syed - PG&E
## Date: June 13, 2019
## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
from arcgis import GIS
from arcgis.features import FeatureLayerCollection

def search_layer(conn,layer_name):
    search_results = conn.content.search(layer_name, item_type="Feature Layer")
    proper_index = [i for i, s in enumerate(search_results) 
                    if '"' + layer_name + '"' in str(s)]
    found_item = search_results[proper_index[0]]
    flc = FeatureLayerCollection.fromitem(found_item)
    return flc

def create_view(conn, source_flc, view_name, layer_index, view_def):
    new_view = source_flc.manager.create_view(name=view_name)
    # Search for newly created View
    view_flc = search_layer(conn, view_name)
    # The viewDefinitionQuery property appears under layers
    view_layer = view_flc.layers[layer_index]
    # Update the definition to include the view definition query
    view_layer.manager.update_definition(view_def)
    print("View created")

def main():
    conn = GIS('https://geomartawrrqa.maps.arcgis.com', 'admin_evmqa', 'adminqa2019%')
    # Index of the Layer to be filtered
    layer_index = 0
    # Define a SQL query filter
	view_def = {"viewDefinitionQuery" : "PARCEL_NAME = '954566179'"}
    # Search for target Hosted Feature Layer
    source_flc = search_layer(conn, "PSPS Testing V1")
    # Create View from Hosted Feature Layer
    create_view(conn, source_flc, "viewLayer", layer_index, view_def)

if __name__ == '__main__':
    sys.exit(main())




