# import the library
import folium
import pandas as pd

class Create_Maps:

   def __init__(self):
      center=[-25.753834153585533, -53.05983441738876]
      self.m = folium.Map(location=center, tiles="OpenStreetMap", zoom_start=16)


   def plot_route(self,lat,long):
      self.data = pd.DataFrame({
         'lon':long,
         'lat':lat,
         'name':['Bob, Cachorro', 'Tobi','Pipoca','Reginaldo','Totó','Tom','Devil','Jorginho','Gil','Magrelo']
      }, dtype=str)

      loc = list(zip(lat,long))
      for i,pet in enumerate(loc):
         folium.Marker(
            location=pet,
            icon=folium.DivIcon(html=f"""<div style="font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size:20px; color: blue">{ i+1 }</div>"""),
            popup=self.data.iloc[i]['name']
         ).add_to(self.m)
         
      folium.PolyLine(loc,
                     color='red',
                     weight=10,
                     opacity=0.5).add_to(self.m)

      # Show the map
      self.m.save('route.html')