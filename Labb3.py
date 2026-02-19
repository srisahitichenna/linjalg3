#%%
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

        #Minsta kvadratmetoden X = ((A^T )* A)^-1 * (A^T)*Y
        AT = A.T #transponent
        ATA = np.matmul(AT, A) 
        inv_ATA = np.linalg.inv(ATA)
        ATY = np.matmul(AT, Y)
        X = np.matmul(inv_ATA, ATY)

#%%
def upg2(): 
    random = np.random.rand(8,2) #skapar 8x2 matris, med tal 0-0.999
    p = (1 + 2*random) #från 1-2.99?
    return p
upg2()



