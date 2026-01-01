import requests
import os
import json


import asyncio
import aiohttp

API_KEY = os.getenv("PLACES_API_KEY")




async def get_places(API_KEY):
    locations = (
        (47.61875,-122.32050000000001,1815.0587612792363),
        (40.752250000000004,-73.88900000000001,2985.9520835134917),
        (37.7615,-122.41749999999999,1915.7245753473562),
        (34.05875,-118.30025,1561.6117398602387),
        (41.85275,-87.667,1995.2006199723253)
    )

    url = "https://places.googleapis.com/v1/places:searchNearby"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.rating"
    }
    async with aiohttp.ClientSession() as session:

        with open("output.json", "a", encoding="utf-8") as f:  
            for l in locations:
                body = {
                    "includedPrimaryTypes": ["barber_shop"],
                    "locationRestriction": {
                        "circle": {
                            "center": {"latitude": l[0], "longitude": l[1]},
                            "radius": l[2]
                        }
                    }
                }

                async with session.post(url, headers=headers, json=body) as response:
                    data = await response.json()

                json.dump(data, f)
                f.write("\n")

asyncio.run(get_places( API_KEY))


##############################################################################################################################################################################################################################################################################################################################################################

# import requests
# import os
# import json


# API_KEY = os.getenv("PLACES_API_KEY")


# longitude = -122.3965
# latitude = 37.7937
# radius = 500


# url = "https://places.googleapis.com/v1/places:searchNearby"

# headers = {
#     "Content-Type": "application/json",
#     "X-Goog-Api-Key": API_KEY,
#     "X-Goog-FieldMask": "places.displayName.text"
# }

# body = {
#     "includedPrimaryTypes": ["restaurant"],
#     "maxResultCount": 10,
#     "locationRestriction": {
#         "circle": {
#             "center": {
#                 "latitude": latitude,
#                 "longitude": longitude
#             },
#             "radius": radius
#         }
#     }
# }

# con = requests.post(url, headers=headers, json=body)
# con.raise_for_status()



# with open("output.json", 'w') as f:
#     json.dump(con.json(), f)