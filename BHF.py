#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


# In[22]:


#BHF = pd.read_csv("BHF_str.csv")
# Data Source: https://data.stadt-zuerich.ch/dataset/hystreet_fussgaengerfrequenzen
# Feiertage Schweiz
# Demonstrationen
# Density
# Pedestrian Dynamics?: https://github.com/PedestrianDynamics/PedPy/blob/main/notebooks/user_guide.ipynb


# In[39]:


url_cs = "https://data.stadt-zuerich.ch/dataset/hystreet_fussgaengerfrequenzen/download/hystreet_fussgaengerfrequenzen_seit2021.csv"

BHF = pd.read_csv(
    url_cs,
    sep=',',
    encoding='utf-8',
)
BHF.head(2)


# In[40]:


from urllib.request import urlopen 
import json 
url_js = "https://data.stadt-zuerich.ch/dataset/hystreet_fussgaengerfrequenzen/download/hystreet_locations.json"


# In[41]:


response = urlopen(url_js) 
data_json = json.loads(response.read()) 
json_df = pd.json_normalize(data_json["features"])
json_df


# In[42]:


import geopandas as gpd

geojson_gdf = gpd.GeoDataFrame.from_features(data_json["features"])
merged_data = pd.merge(BHF, geojson_gdf, how = "inner", left_on = "location_id", right_on = "hystreet_location_id")
merged_data.head(2)


# In[43]:


merged_data.head(2)


# In[44]:


gdf = gpd.GeoDataFrame(merged_data, geometry = gpd.GeoSeries(merged_data["geometry"]))


# In[46]:


import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Documentation: https://dlab.berkeley.edu/news/adding-basemaps-python-contextily
# 'EPSG:4326' is WGS84, the default CRS for GPS coordinates----------------------

gdf = gdf.set_crs("EPSG:4326") 

# Transform to Web Mercator (EPSG:3857)----------------------

gdf_3857 = gdf.to_crs("EPSG:3857")

# Create the plot----------------------

fig, ax = plt.subplots(figsize = (18, 9)) #--- faster ---
#fig, ax = plt.subplots(figsize = (30, 15)) --- for better rendering quality ---

gdf_3857.plot(ax=ax, column = "pedestrians_count", 
              cmap = "YlOrRd", 
              legend=True, 
              legend_kwds={'label': "pedestrians count"})
plt.title("Passantenfrequenzen an der Bahnhofstrasse - Stundenwerte")

# Padding for left and right sides----------------------

extra_space_lr = 1000 

# Padding for top and bottom----------------------

extra_space_tb = 200  

total_bounds = gdf_3857.total_bounds
x_min, y_min, x_max, y_max = total_bounds

# Adjust the limits to include more area around both GeoDataFrame and basemap----------------------

ax.set_xlim(x_min - extra_space_lr, x_max + extra_space_lr)
ax.set_ylim(y_min - extra_space_tb, y_max + extra_space_tb)

ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery)  

plt.grid(visible=True)
plt.show()


# In[48]:


# Consistency Analysis----------------------

# Count columns and rows----------------------

print(f"Count rows: {len(BHF)}")
print(f"Count columns: {len(BHF.columns)}")
print()

# BHF info----------------------

print(BHF.info())
print()

# Entries after 03.03.2022 are consistent (Dataset Description)----------------------

BHF["timestamp"] = pd.to_datetime(BHF["timestamp"])
entries_before_030322 = BHF[BHF["timestamp"] < "2022-03-03"]
entries_after_030322 = BHF[BHF["timestamp"] >= "2022-03-03"]

print(f"Count entries before 03.03.2022: {len(entries_before_030322)}")
print(f"Count entries after 03.03.2022: {len(entries_after_030322)}")

# Let's say the unverified column proofs consistency----------------------

consistent_data = BHF[BHF["timestamp"] >= "2022-03-03"]
reliable_data = consistent_data[consistent_data["unverified"] == False]

print(f"Count consistent data: {len(reliable_data)}")

