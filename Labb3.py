import numpy as np
import matplotlib as mpl

def uppgift1(punkter):
    
    n = len (punkter)

    #Tomma matriser
    A = np.zeros((n, 4))
    Y = np.zeros((n, 1))

    # Loopa igenom varje punkt
    for j in range(n):

        # Plocka ut a_j och b_j direkt
        a_j = punkter[j, 0]
        b_j = punkter[j, 1]

        # Fyll A enligt uppgiften
        A[j, 0] = a_j**3
        A[j, 1] = a_j**2
        A[j, 2] = a_j
        A[j, 3] = 1

        # Fyll Y
        Y[j, 0] = b_j




