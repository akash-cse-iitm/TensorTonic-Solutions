import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    #convert input to array
    x_arr = np.asarray(x, dtype=float)
    # NumPy automatically do division across the entire array structure
    value = 1.0 / (1.0 + np.exp(-x_arr))

    # A/Q "Return a float when x is a scalar." Checking np.isscalar(x) cecks scalars from array-like object to return float
    if np.isscalar(x):
     return float(value)
        
    return value
    
#Easy - 01.10.26