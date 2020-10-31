import folium
import geojson
from folium.plugins import MarkerCluster

def calculations(**kwargs):
    """Что-то будем вычислять """
    pass

map = folium.Map(location=[43.164242, 131.905624], zoom_start = 12)
marker_cluster = MarkerCluster().add_to(map)
with open("POI.geojson", encoding='UTF-8') as read_file:
    data = geojson.load(read_file)
    for i in range(2251):
        pos = data[i].get('geometry').get('coordinates')
        name = data[i].get('properties').get('name')
        pos[0], pos[1] = pos[1], pos[0]
        print(i)
        folium.CircleMarker(location=pos, popup=name, radius = 9, color="red").add_to(marker_cluster)

marker_cluster_adm = MarkerCluster().add_to(map)
with open("Vladivostok_adm.geojson", encoding='UTF-8') as read_file:
    data = geojson.load(read_file)
    for num, pos in enumerate(data.get('features')[0].get('geometry').get('coordinates')[0]):
        pos[0], pos[1] = pos[1], pos[0]
        print(num)
        folium.CircleMarker(location=pos, popup='i', radius=9, color="blue").add_to(marker_cluster_adm)
num = 0
marker_cluster_buildings = MarkerCluster().add_to(map)
with open("buildings.geojson", encoding='UTF-8') as read_file:
    data = geojson.load(read_file)
    for i in range(60902):
        for pos in data[i].get('geometry').get('coordinates')[0][0]:
            pos[0], pos[1] = pos[1], pos[0]
            num += 1
            print(num)
            folium.CircleMarker(location=pos, popup=i, radius=1, color="green").add_to(marker_cluster_buildings)
print('save map')
map.save("map1.html")