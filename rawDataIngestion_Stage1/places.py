import asyncio
import aiohttp
import os


API_KEY = os.getenv("Places_Aggregate")


URL = "https://areainsights.googleapis.com/v1:computeInsights" 


def get_header (key):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": key,
    }
    return headers


def get_payload(coor):
    lat, long, radius = coor
    radius = int(round(radius))
    payload = {
        "insights": ["INSIGHT_COUNT"],
        "filter": {
            "locationFilter": {
                "circle": {
                    "radius": 1409,
                    "latLng": {
                        "latitude": lat,
                        "longitude": long,
                        },
                    },
                },
                "typeFilter": {
                    "includedTypes": [
                        "barber_shop",
                        "nail_salon",
                        "tailor",
                        "bagel_shop",
                        "donut_shop",
                        "ice_cream_shop",
                        "juice_shop",
                        "tea_house",
                        "candy_store",
                        "butcher_shop",
                        "asian_grocery_store", 
                    ]
                },
            "operatingStatus": [
                "OPERATING_STATUS_OPERATIONAL",
            ],
            "priceLevels": [
                "PRICE_LEVEL_MODERATE",
                "PRICE_LEVEL_INEXPENSIVE"
            ],
        },
    }
    return payload





async def places_tasks(session, coordinate, endpoint):
    async with session.post(url=endpoint, headers=get_header(API_KEY), json=get_payload(coordinate[2])) as resp:
        status = resp.status      ###################################
        try: 
            response = await resp.json()
        except aiohttp.ContentTypeError:
            response = await resp.text() 
            insert_requests(coordinate[0], )######################################################
        return coordinate[0], response



async def func(coordinate):
    async with aiohttp.ClientSession() as session:
        tasks = [places_tasks(session,  coordinate, URL)]

        results = await asyncio.gather(*tasks)

        for z ,r in results:
            print(f"{z} :   {r}")
            

coordinates = (90694, (47.6031739999818, -122.3512549998386, 47.61851099976298, -122.32135299996169), (47.61084249987239,-122.33630399990014,1409.8593630867806))




asyncio.run(func(coordinates))





