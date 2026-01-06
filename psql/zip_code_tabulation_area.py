import psycopg
from . import DB_NAME, USERNAME, DB_KEY

def get_zcta (lbound = None, ubound = None):
    zcta= []

    with psycopg.connect(f"dbname={DB_NAME} user={USERNAME} password={DB_KEY}") as conn:
        with conn.cursor() as curr:

            if ubound is None and lbound is  None:
                curr.execute("""
                    SELECT zcta FROM zcta
                """)
            elif ubound is None and lbound is not None: 
                curr.execute(f"""
                    SELECT zcta FROM zcta OFFSET {lbound} 
                """)
            elif lbound is None and ubound is not None:
                curr.execute(f"""
                    SELECT zcta FROM zcta FIRST {ubound} ROWS ONLY
                """)        
            else:
                curr.execute(f"""
                    SELECT zcta FROM zcta OFFSET {lbound} FETCH FIRST {ubound - lbound} ROWS ONLY
                """)
            for (z,) in curr: 
                zcta.append(z)  
    return zcta 
