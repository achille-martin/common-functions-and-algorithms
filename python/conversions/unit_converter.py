#!/usr/bin/env python3

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

# Function used to map an angle to [-pi; pi] interval
def wrap_to_pi(angle):
    while angle > math.pi:
        angle = angle - 2.0*math.pi
    while angle < -math.pi:
        angle = angle + 2.0*math.pi
    return angle

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
