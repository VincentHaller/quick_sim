# Vincent Haller, 29/11/2023
# This contains the functions to help orientate between matrix and vector orientations. 
#%%
import numpy as np

#%%

def py_loc_vector(dimensions:list, location:list):
    """
        Takes matrix location turns it into vector location

            Parameters:
                dimenstions: list of integers.
                location: list of integers
            
            Returns:
                vector_loc: integer, matrix location in vector form.
    """
    len_dim = len(dimensions)
    vector_loc = 0
    mult_value = 1
    
    for i in range(len_dim):
        vector_loc += mult_value * location[(len_dim-1) - i]
        mult_value *= dimensions[(len_dim-1) - i]
    
    return vector_loc


def py_loc_matrix(dimensions:list, location:int):
    """
        Takes vector locaiton turns it into matrix location

        Parameters:
            dimensions: list of integers
            location: integer

        Returns:
            matrix_loc: list of integers, vector location in matrix form.
    """
    len_dim = len(dimensions)
    matrix_loc = np.zeros_like(dimensions)

    mult_value = 1
    for i in range(1, len_dim):
        mult_value *= dimensions[i]

    for i in range(len_dim):
        matrix_loc[i] = int(location // mult_value)
        location %= mult_value
        if i < (len_dim - 1):
            mult_value /= dimensions[i + 1]

    return matrix_loc