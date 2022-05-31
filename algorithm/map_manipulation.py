# import the library
import folium
import pandas as pd

# Make an empty map
center=[-25.753834153585533, -53.05983441738876]
m = folium.Map(location=center, tiles="OpenStreetMap", zoom_start=16)

# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[-53.06342,-53.05160,-53.05668, -53.06003,-53.06226,-53.05777,-53.06638,-53.08245,-53.06719,-53.06851,-53.06596,-53.06457,-53.06204],
   'lat':[-25.75229,-25.76263,-25.74263,-25.75328,-25.75332,-25.75316,-25.74445,-25.74773,-25.75695,-25.75669,-25.75468,-25.75704,-25.75422],
   'name':['Bob', 'Tobi','Pipoca','Reginaldo','Totó','Tom','Devil','Jorginho','Paçoca','Gil','Magrelo','Princesa','Mimosa'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43, 21, 11, 15, 26, 66]
}, dtype=str)

# add marker one by one on the map
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(m)

# Show the map
m.save('index.html')