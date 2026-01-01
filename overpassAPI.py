import requests
import json

url = "https://overpass-api.de/api/interpreter"

down_lat = 47.605
up_lat = 47.6325

left_long = -122.3335
right_long = -122.3075




query = f"""
[out:json];
(
  node["highway"="bus_stop"]({down_lat},{left_long},{up_lat},{right_long});
);
out count;
"""


reqObj = requests.post(url, data={"data": query})



with open("overpassOutput.json", 'w') as f:
    json.dump(reqObj.json(), f)