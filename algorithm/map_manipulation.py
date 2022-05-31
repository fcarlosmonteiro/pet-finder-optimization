# import the library
import folium
import pandas as pd

# Make an empty map
center=[-25.753834153585533, -53.05983441738876]
m = folium.Map(location=center, tiles="OpenStreetMap", zoom_start=16)

# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[-53.063426526198306,-53.05160334995361],
   'lat':[-25.752299003614507,-25.762638238002804],
   'name':['Bob', 'Tobi'],
   'value':[10, 12]
}, dtype=str)

# add marker one by one on the map
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(m)

# Show the map
m.save('index.html')