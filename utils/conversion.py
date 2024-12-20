import numpy as np
import pandas as pd
from vtkmodules.util.numpy_support import vtk_to_numpy as vtn

OUTER_RADIUS = 6378137 # Outer radius in meters
ECCENTRICITY =0.081819190842622 # WGS84 eccentricity


def conv_to_lat(x, y, z):
    """Function for converting 3D coordinates to Latitude. 

    Args:
        x (float): x coordinate of the point?
        y (float): y coordinate
        z (float): z coordinate

    Returns:
        (float) : Returns the Latitude in degrees
    """
    return np.rad2deg(np.arctan2(z, np.sqrt(x*x + y*y)))


def conv_to_long(x,y):
    """Function for converting 3D coordinates to Longitude

    Args:
        x (float): x coordinate
        y (float): y coordinate

    Returns:
        (float): Returns the Longitude in Degrees
        
    """
    
    return np.rad2deg(np.arctan2(y,x))
    
def calcDepth(x,y,z, lat):
    """Function for calculating the depth

    Args:
        x (float): _description_
        y (float): _description_
        z (float): _description_
        lat (degrees): The Latitude

    Returns:
        float: Returns the Depth in kilometers
    """
    N = OUTER_RADIUS/(1 - (ECCENTRICITY*ECCENTRICITY) * np.sin(np.radians(lat)) * np.sin(np.radians(lat)))
    return (N - np.sqrt((x*x) + (y*y) + (z*z)))*0.001

def conv_to_dataframe(data):
    """Function for converting the data to a pandas dataframe

    Args:
        data (list): List of data

    Returns:
        (pandas.DataFrame): Returns a pandas dataframe
    """
    point_coords = vtn(data.GetPoints().GetData())
    melt_fraction = vtn(data.GetPointData().GetArray("melt_fraction"))

    x_coords, y_coords, z_coords = point_coords.T

    lattitude = conv_to_lat(x_coords, y_coords, z_coords)
    longitude = conv_to_long(x_coords, y_coords)
    depth = calcDepth(x_coords, y_coords, z_coords, lattitude)


    data_frame = pd.DataFrame({
        'Latitude': lattitude,
        'Longitude': longitude,
        'MeltFraction': melt_fraction,
        'Depth': depth
        })


    return data_frame 



