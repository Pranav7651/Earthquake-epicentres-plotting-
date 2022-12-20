import pandas as pd
import folium

data=pd.read_csv("./Earthquake_data_csv/database.csv")

lat=list(data["Latitude"])
lon=list(data["Longitude"])
mag=list(data["Magnitude"])

def circle_color(m):
    if(m>=6 and m<7):
        return "orange"
    else :
        return "red"

map=folium.Map(location=[23.500932, 79.038836],zoom_start=4.5,tiles="CartoDB Positron")

fgc=folium.FeatureGroup(name="coordinates",fill=True)

for lt,ln,m in zip(lat,lon,mag):
    if(m>=6):
        fgc.add_child(folium.CircleMarker(location=[lt,ln],radius=6,fill=True,tooltip="click for more information",popup="<strong>Magnitude: "+str(m),fill_color=circle_color(m),color="grey",fill_opacity=0.7))

fgp=folium.FeatureGroup(name="boundary")
fgp.add_child (folium.GeoJson(data=open("./Boundaries_json/world.json",'r',encoding='utf-8-sig').read(),style_function=lambda x:{
    'fillColor':'white'}))

map.add_child(fgc)

map.add_child(fgp)
map.add_child(folium.LayerControl())

map.add_child(fgc)
map.save("Map1.html")