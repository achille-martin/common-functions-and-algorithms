#!/usr/bin/env python3

# MIT License

# Copyright (c) 2023-2024 Achille MARTIN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math
import numpy as np

importer_folder = os.path.dirname(
    os.path.realpath(__file__)
)
parent_of_importer_folder = os.path.join(
    importer_folder,
    os.path.pardir,
)
sys.path.append(parent_of_importer_folder)
from conversions.unit_converter import unit_converter

def rot_matrix(axis, angle_deg, rotation_type='3D'):
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

    rotation_type: str
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
    
    if rotation_type == '2D':
        rot_array = np.array(
            [
                [math.cos(angle_rad), -math.sin(angle_rad)],
                [math.sin(angle_rad), math.cos(angle_rad)],
            ]
        )
    
    elif rotation_type == '3D':
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
            Array type {rotation_type} NOT handled yet
            """
        )

    return rot_array
