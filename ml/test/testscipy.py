#!/usr/bin/env python3
# Author Zuxing Gu

import numpy as np
from scipy import sparse

eye = np.eye(4)
print("NumPy array:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("CSR matrix:\n{}".format(sparse_matrix))

data = np.ones(4)
row = np.arange(4)
col = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row, col)))
print("COO:\n{}".format(eye_coo))
