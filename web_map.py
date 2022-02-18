"""Create a web application"""
import json
from geopy.geocoders import Nominatim, ArcGIS
import folium
import twitter_data


def read_data(path: str):
    """
    Read json file.
    """
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def get_coordinates(place: str) -> tuple:
    """
    Get tuple of latitude and longitude of the place.
    """
    geolocator_1 = Nominatim(user_agent='http')
    geolocator_2 = ArcGIS()
    location = geolocator_1.geocode(place)
    if location is None:
        location = geolocator_2.geocode(place)
    if location is not None:
        return location.latitude, location.longitude
    return


def get_friends_info(data: dict) -> tuple:
    """
    Get friends's names, locations and coordinates.
    """
    friends_info = []
    for friend in data['users']:
        name = friend['screen_name']
        location = friend['location']
        coordinates = get_coordinates(location)
        friends_info.append((name, location, coordinates))
    return friends_info


def create_map(friends_info):
    """
    Create a web map with info about friends.
    """
    text = """<i>Name</i>: {}<br>
            <i>Location</i>: {}"""
    web_map = folium.Map(location=(0, 0), zoom_start=2)
    fg_friends = folium.FeatureGroup(name='Friends')
    for friend in friends_info:
        if friend[2]:
            iframe = folium.IFrame(html=text.format(
                friend[0], friend[1]), width=300, height=70)
            fg_friends.add_child(folium.Marker(location=friend[2],
                                               popup=folium.Popup(iframe),
                                               icon=folium.Icon(icon='user', color='lightred')))
    web_map.add_child(fg_friends)
    web_map.add_child(folium.LayerControl())
    web_map.save('friends_map.html')


def main(nickname):
    """
    Main function.
    """
    data = twitter_data.get_data(nickname)
    friends = get_friends_info(data)
    create_map(friends)
