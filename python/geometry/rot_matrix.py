#!/usr/bin/env python3

import math
import numpy as np
from scripts.unit_converter import unit_converter

def rot_matrix(axis, angle_deg, array_type='3D'):
    """
    Get the rotation array 
    for a specified angle around a specified axis
  
    Parameters
    ----------
    axis: str
        The axis around which the rotation occurs
        'x', 'y' or 'z'
  
    angle_deg: float
        Angle of rotation around axis in degrees
        The sign of the angle depends on the right-hand rule rotation

    array_type: str
        The type of array returned
        '2D' is implemented
        '3D' is implemented

    Returns
    -------
    Numpy array
        Array describing the rotation desired
    """
    
    rot_array = None
    
    angle_rad = unit_converter(angle_deg, 'DEG', 'RAD') 
    
    if array_type == '2D':
        rot_array = np.array(
            [
                [math.cos(angle_rad), -math.sin(angle_rad)],
                [math.sin(angle_rad), math.cos(angle_rad)],
            ]
        )
    
    elif array_type == '3D':
        if axis == 'x':
            rot_array = np.array(
                [
                    [1, 0, 0],
                    [0, math.cos(angle_rad), -math.sin(angle_rad)],
                    [0, math.sin(angle_rad), math.cos(angle_rad)],
                ]
            )
        
        elif axis == 'y':
            rot_array = np.array(
                [
                    [math.cos(angle_rad), 0, math.sin(angle_rad)],
                    [0, 1, 0],
                    [-math.sin(angle_rad), 0, math.cos(angle_rad)],
                ]
            )

        elif axis == 'z':
            rot_array = np.array(
                [
                    [math.cos(angle_rad), -math.sin(angle_rad), 0],
                    [math.sin(angle_rad), math.cos(angle_rad), 0],
                    [0, 0, 1],
                ]
            )

        else:
            raise Exception(
                f"""
                Axis {axis} is NOT recognised
                Try with 'x', 'y' or 'z'
                """
            )

    else:
        raise Exception(
            f"""
            Array type {array_type} NOT handled yet
            """
        )

    return rot_array
