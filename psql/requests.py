import psycopg
from . import DB_NAME, USERNAME, DB_KEY



def insert_request(zcta, api, endpoint, method, status_code, error_message = None, headers = None, parameters = None):
    with psycopg.connect(f"dbname={DB_NAME} user={USERNAME} password={DB_KEY}") as conn:
        with conn.cursor() as curr:

            curr.execute("""
                INSERT INTO requests (zcta, api, endpoint, method, headers, paramerters, status code, error_message)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """,
                (zcta, api, endpoint, method, headers, parameters, status_code, error_message))  