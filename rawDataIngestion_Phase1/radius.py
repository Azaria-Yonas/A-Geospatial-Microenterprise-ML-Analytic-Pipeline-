# The Locations table recives a bounding box (bbox) to query the Overpass API
# but does not recieve coordinates for the use of the Places API (new). 

# One thing to note is that bbox is basically the smallest axis-aligned rectangle that
# fully encloses a region on the Earth’s surface. It contains four values (east, west,
# north, and south bounds) and it is a convinient way of storing spatial area as to 
# storing pairs

# The issue is the, bbox coordinates can't be used by the Places API (new), as it requires
# (long, lat) coordinates for a point (the center) and a radius to generate result 
# within that circular area.

# As a result I decided to calculate the coordinate parameters for the Places ApI (new) 
# using the bbox coordinates. The center coordinates are generated and stored as the mid 
# point of the longitude and latitude. 

# And to calculate the radius, I use this script which calculates the diagonal and equates 
# half of it to the radius.  Password


import math


def calcRadius (cen_long, cen_lat, left_long, down_lat):
    x = (cen_lat - down_lat) * 111_320                                            # converting degrees to meters
    y = (cen_long - left_long) * 111_320 * math.cos(math.radians(cen_lat))

    return math.sqrt(x**2 + y**2)






# print(calcRadius (-122.3205, 47.61875, -122.3335,  47.605))  # Capitol Hill, Seattle, WA
# print(calcRadius (-73.889, 40.75225, -73.9205,  40.74))  # Jackson Heights, Queens, NY 




