import folium
import pandas
import firebase_admin
from firebase_admin import credentials

firebase_admin.initialize_app()

data = pandas.read_csv("ConsumosMensuales.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
cons_mensual = list(data["CONSUMO_MENSUAL"])

def obtener_color_consumo(cons_mensual):
	if cons_mensual <100:
		return 'green'
	elif 100 <= cons_mensual < 200:
		return 'orange'
	else:
		return 'red'
	
		

map = folium.Map(location=[41.68,2.8], zoom_start = 15)

fgv = folium.FeatureGroup(name="Consumos")

for lt, ln, nm, cons_m in zip(lat, lon, name, cons_mensual):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(nm) + "= " + str(cons_m) + " kW", icon=folium.Icon(color = obtener_color_consumo(cons_m))))


map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("index.html")
