import asyncio
import aiohttp
import json


URL = "https://overpass-api.de/api/interpreter"

def get_query (bbox):
    query = f"""
        [out:json][timeout:180];
        (
        /* Transit (bus) */
        node["highway"="bus_stop"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        node["public_transport"="platform"]["bus"="yes"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        node["public_transport"="stop_position"]["bus"="yes"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        node["amenity"="bus_station"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        way["amenity"="bus_station"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        relation["amenity"="bus_station"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});

        /* Crosswalks */
        node["highway"="crossing"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        way["highway"="crossing"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});

        /* Sidewalk / walk infra */
        way["highway"~"^(footway|pedestrian)$"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        way["highway"]["sidewalk"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});

        /* Human-scale streets */
        way["highway"~"^(living_street|residential|unclassified|tertiary|service)$"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
        );
        out tags;
    """
    return query

async def overpass_tasks (sessions, url, coordinates):
    async with sessions.post(url, data={"data": get_query(coordinates[1])}) as resp:
        response = await resp.json()
        return coordinates[0], response



async def func(url, coordinates):
    async with aiohttp.ClientSession() as session:
        task = [overpass_tasks(session, url, coordinates)]

        results = await asyncio.gather(*task)

        for z, r in results:
            print (z) 
            with open("output.json", "w", encoding="utf-8") as j:
                json.dump(r, j, ensure_ascii=False, indent=2)


coordinates = (90694, (47.6031739999818, -122.3512549998386, 47.61851099976298, -122.32135299996169), (47.61084249987239,-122.33630399990014,1409.8593630867806))

asyncio.run(func(URL, coordinates))





