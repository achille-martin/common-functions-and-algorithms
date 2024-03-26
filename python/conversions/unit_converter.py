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
from enum import Enum

# Enum of unit aliases
class UnitAlias(Enum):
    # Angles
    ## DEG
    degree = "DEG"
    degrees = "DEG"
    deg = "DEG"
    DEGREE = "DEG"
    DEGREES = "DEG"
    DEG = "DEG"
    ## RAD
    radian = "RAD"
    radians = "RAD"
    rad = "RAD"
    RADIAN = "RAD"
    RADIANS = "RAD"
    RAD = "RAD"

# Function used to map an angle (in rad) to [-pi; pi] interval
def wrap_to_pi(angle_rad):
    while angle_rad > math.pi:
        angle_rad = angle_rad - 2.0*math.pi
    while angle_rad < -math.pi:
        angle_rad = angle_rad + 2.0*math.pi
    return angle_rad

def unit_converter(values, from_unit, to_unit):
    """
    Convert a list of values or single value
    from a specific unit to a specific unit
  
    Parameters
    ----------
    values: iterable of float or single float
        A list of numbers
 
    from_unit: str
        Unit of the input values
        All input values must have same unit

    to_unit: str
        Unit of the output

    Returns
    -------
    iterable of float or single float
        Converted values to desired unit
    """
    
    converted_values = None

    # Convert single value to list for practicality
    single_value_input_flag = False
    if not isinstance(values, list):
        single_value_input_flag = True
        values = [values]

    from_unit_alias = UnitAlias[from_unit].value
    to_unit_alias = UnitAlias[to_unit].value

    # Angles
    if from_unit_alias == 'DEG' and to_unit_alias == 'RAD':
        converted_values = [
            wrap_to_pi(value * math.pi/180.0)
            for value in values
        ] 

    elif from_unit_alias == 'RAD' and to_unit_alias == 'DEG':
        converted_values = [
            wrap_to_pi(value) * 180.0/math.pi
            for value in values
        ] 

    else:
        raise Exception(
            f"""
            Conversion from {from_unit} to {to_unit_si}
            NOT handled yet
            """
        )

    # Return single value or list depending on input
    if single_value_input_flag:
        return converted_values[0]
    else:
        return converted_values
