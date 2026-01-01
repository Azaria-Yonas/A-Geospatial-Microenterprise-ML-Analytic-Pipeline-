BEGIN;

INSERT INTO locations (locationName, down_lat, left_long, up_lat, right_long)
VALUES
  ('Capitol Hill, Seattle, WA',      47.6050, -122.3335, 47.6325, -122.3075),
  ('Jackson Heights, Queens, NY',    40.7400,  -73.9205, 40.7645,  -73.8575),
  ('Mission District, San Francisco, CA', 37.7480, -122.4310, 37.7750, -122.4040),
  ('Koreatown, Los Angeles, CA',     34.0470, -118.3095, 34.0705, -118.2910),
  ('Pilsen, Chicago, IL',            41.8440,  -87.6880, 41.8615,  -87.6460);

COMMIT;




--I Used BBOX finder to generate this coordinates: http://bboxfinder.com/#0.000000,0.000000,0.000000,0.000000
