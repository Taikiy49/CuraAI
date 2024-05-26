import folium

def plot_locations(locations):
    my_map = folium.Map(location=[0, 0], zoom_start=2)

    for location in locations:
        latitude, longitude = location
        folium.Marker(location=[latitude, longitude], popup="Location").add_to(my_map)

    return my_map


def create_map(locations):
    my_map = plot_locations(locations)
    my_map.save("templates/multiple_locations_map.html")
    my_map
