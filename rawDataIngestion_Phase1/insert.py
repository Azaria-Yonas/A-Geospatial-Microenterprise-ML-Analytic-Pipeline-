import psycopg
from placesAPI import get_places





with psycopg.connect("dbname = myfirstrun user = postgres password=Password") as con:

    with con.cursor() as cur:

        cur.execute(f"""

        """)
