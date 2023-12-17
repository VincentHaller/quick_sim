cimport cython
# cimport openmp

import numpy as np
cimport numpy as np


cdef extern from "../C_code/simulation.h":
    int i, j
    double mult
    cdef void simulate( double *out, int N, int h, int exp )


@cython.boundscheck(False)
@cython.cdivision(True)
cpdef c_simulation(int N, int h, int exp):

    cdef:
        double[:, :] out = np.empty([N, h])

    simulate( &out[0, 0], N, h, exp )

    return np.asarray(out)
