import os
import folium
from folium.plugins import MarkerCluster
from GPS_Extraction import process_images
import numpy as np

# script_dir = os.path.dirname(os.path.realpath(__file__))
# print(script_dir)

def open_webview():
    # this is the path to the predicted images
    folder_path = os.path.join('runs', 'detect', 'predict')
    print(folder_path)

    output_list = process_images(folder_path)

    coordinates_list = []

    for coord in output_list:
        x, y, image_path = coord
        coordinates_list.append([x, y, image_path])

    x_values = [coord[0] for coord in coordinates_list]
    y_values = [coord[1] for coord in coordinates_list]

    mean_latitude = np.mean(x_values)
    mean_longitude = np.mean(y_values)

    map = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=15)

    marker_cluster = MarkerCluster().add_to(map)

    for x, y, z in coordinates_list:
        street_view_link = f'http://maps.google.com/maps?q=&layer=c&cbll={x},{y}&cbp=11,0,0,0,0'
        popup_html = f'<a href="{street_view_link}" target="_blank">View in Google Street View</a><br><img src="{z}" style="width:250px; height:250px;">'
        folium.Marker(
            location=[x, y],
            popup=folium.Popup(popup_html, max_width=300),
        ).add_to(marker_cluster)

    categories = ['Detected']
    layer_control = folium.LayerControl(position='topleft', collapsed=False)

    marker_cluster.layer_name = 'Detected'
    map.add_child(marker_cluster)

    map.add_child(layer_control)

    map.save('detected.html')


open_webview()
