#!/usr/bin/python3
""" calculate gps coordinates """
import numpy as nm
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import sys
"""cneter longitude, center latitude, longitude, latitude, radius in distance unit, distance unit """
def within_a_radius(center_long, center_lat, long, lat, R, ditance_unit = 'km'):
    """ Calculates a distance between center point
        and any other point"""
    #convert decimal degrees to radians
    center_long, center_lat, long, lat = map(radians, [center_long, center_lat, long, lat])

    #formula
    dlong = long - center_long
    dlat = lat - center_lat
    a = sin(dlat / 2) ** 2 + cos(center_lat) * cos(lat) * sin(dlong / 2) ** 2
    c = 2 * asin(sqrt(a))

    # this number (small r) is used for radius of earth in kilometers or miles. 
    # if you want to use miles insetad of KM, use distance_unit = m instead.

    if ditance_unit == 'km':
        r = 6371
    elif ditance_unit == 'm':
        r = 3956
    else:
        sys.exit("Error: distance_unit must be either km or m.")
    
    # final calculation
    if (R >= c * r):
        return True
    else:
        return False
    
AAU = '9.0335, 38.7637'
BEMB = '9.03146, 38.78672'
my_loc ='9.03481,38.761211'

print(within_a_radius(38.761211, 9.03481, 38.78672, 9.03146, 2.5, 'km'));