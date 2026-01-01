import psycopg as pg
import os

DB_KEY = os.getenv("dbKey")
USER = os.getenv("psqlUser")

con = pg.connect(f"dbname = myfirstrun user = {USER} password={DB_KEY}")
curr = con.cursor()

curr.execute("""
    SELECT (up_lat, down_lat, left_long, right_long, center_lat, center_long, radius) FROM locations
""")

coordinates = curr


tasks = []

for coor in coordinates:
    tasks



































con.close()