import numpy as np

def tikonov_inverse(F:np.ndarray,k = 0.1):
    return np.matmul(np.linalg.inv((np.matmul(F.transpose(),F)+k*np.identity(F.shape[0]))),F.transpose())

def tikonov_est(F:np.ndarray,d:np.ndarray,k = 0.1):
    return np.matmul(tikonov_inverse(F,k),d)

