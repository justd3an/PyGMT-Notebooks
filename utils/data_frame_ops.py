import pandas as pd
import numpy as np

def threshold(data_frame, thresh_var, bounds, operators=('>=', '<=')):
    """
    Filter DataFrame based on threshold conditions
    
    Parameters:
    -----------
    data_frame : pandas.DataFrame
        Input DataFrame to filter
    thresh_var : str
        Column name to apply threshold on
    bounds : tuple
        (lower_bound, upper_bound) values
    operators : tuple
        Comparison operators to use ('>', '>=', '<', '<=', '==', '!=')
    
    Returns:
    --------
    pandas.DataFrame
        Filtered DataFrame
    """
    operator_map = {
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y
    }
    
    if len(operators) != len(bounds):
        raise ValueError("Number of operators must match number of bounds")
        
    conditions = []
    for op, bound in zip(operators, bounds):
        if op not in operator_map:
            raise ValueError(f"Unsupported operator: {op}")
        conditions.append(operator_map[op](data_frame[thresh_var], bound))
    
    return data_frame[np.logical_and.reduce(conditions)]