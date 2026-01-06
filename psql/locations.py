import psycopg
from . import DB_NAME, USERNAME, DB_KEY


def insert_into_locations (zcta,bbox):
    with psycopg.connect(f"dbname={DB_NAME} user={USERNAME} password={DB_KEY}") as conn:
        with conn.cursor() as cur:
            if bbox is (None): 
                cur.execute("""
                    INSERT INTO locations(zcta, down_lat, left_long, up_lat, right_long)
                    VALUES (%s, %s, %s, %s, %s);
                """,
                (zcta, 0 , 0 , 0 , 0))
            else:
                cur.execute("""
                    INSERT INTO locations(zcta, down_lat, left_long, up_lat, right_long)
                    VALUES (%s, %s, %s, %s, %s);
                """,
                (zcta, bbox[0], bbox[1], bbox[2], bbox[3]))  