import numpy as np
def steer_generate():
    A = np.zeros([121,2],dtype=complex)
    D_X  = np.repeat(np.array(([0.5])),2)
    for i in np.arange(-60, 61, 1):
        Vector = np.exp(-1j * 2 * np.pi * np.sin(np.deg2rad(i)) * D_X)
        A[i + 60,:] = Vector
    return A