# import the library
import folium
import pandas as pd

class Create_Maps:
   def __init__(self):
      center=[-25.753834153585533, -53.05983441738876]
      self.m = folium.Map(location=center, tiles="OpenStreetMap", zoom_start=16)

   def mark_points(self,lat,long):

      data = pd.DataFrame({
         'lon':long,
         'lat':lat,
         'name':['Bob, Cachorro', 'Tobi','Pipoca','Reginaldo','Totó','Tom','Devil','Jorginho','Gil','Magrelo']
      }, dtype=str)

      # add marker one by one on the map
      for i in range(0,len(data)):
         folium.Marker(
            location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
            popup=data.iloc[i]['name']
         ).add_to(self.m)

      # Show the map
      self.m.save('index.html')

   def plot_route(self,lat,long):

      loc = list(zip(lat,long))
      print(loc)
      folium.PolyLine(loc,
                     color='red',
                     weight=10,
                     opacity=0.5).add_to(self.m)

      # Show the map
      self.m.save('route.html')