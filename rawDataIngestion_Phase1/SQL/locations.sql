CREATE TABLE locations (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    locationName VARCHAR(255) NOT NULL,
    down_lat FLOAT NOT NULL,
    left_long FLOAT NOT NULL,
    up_lat FLOAT NOT NULL,
    right_long FLOAT NOT NULL,
    center_lat DOUBLE PRECISION GENERATED ALWAYS AS ((down_lat + up_lat) / 2) STORED,
    center_long DOUBLE PRECISION GENERATED ALWAYS AS ((left_long + right_long) / 2) STORED,
    radius DOUBLE PRECISION GENERATED ALWAYS AS (
        sqrt(
            power((((down_lat + up_lat) / 2) - down_lat) * 111320, 2) +
            power(((((left_long + right_long) / 2) - left_long) * 111320 * cos(radians(((down_lat + up_lat) / 2)))), 2)
        )
    ) STORED
    
)




-- I Primarily created this table to store information used to make the API requests
-- I originally used radius.py to calculate the radius and I have left more information as to why 