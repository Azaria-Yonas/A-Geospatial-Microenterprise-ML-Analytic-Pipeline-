from placesAPI import get_places
import psycopg as pg





DB_KEY = os.getenv("dbKey")
USER = os.getenv("psqlUser")






with pg.connect(f"dbname = myfirstrun user = {USER} password={DB_KEY}") as con:

    with con.cursor() as cur:


        cur.execute(f"""
            SELECT center_lat, center_long, radius FROM locations;   
        """)




        cur.execute(f"""INSERT INTO responses (places_api) VALUES (%s)

        """, (get_places()))


