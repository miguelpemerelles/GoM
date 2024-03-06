import  numpy as np
#import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import scipy
from scipy.signal import convolve2d

class game_of_life(object):
    def __init__(self, N) -> None:
        self.N = N
        self.total_N = N*N
        self.lattice = np.ones((N, N))
        randoms = np.random.random((N,N))
        self.lattice[randoms>= 0.75] = 1
        self.lattice[randoms < 0.75] = 0

    def glider(self): #Single glider initializer          
        self.lattice = np.zeros((self.N,self.N))
        self.lattice[24][25] = 1 
        self.lattice[25][26] = 1 
        self.lattice[26][24] = 1 
        self.lattice[26][25] = 1 
        self.lattice[26][26] = 1

    def blinker(self):
        self.lattice = np.zeros((self.N,self.N))
        self.lattice[24][25] = 1
        self.lattice[25][25] = 1
        self.lattice[26][25] = 1

    def beehive(self):
        self.lattice = np.zeros((self.N,self.N))
        self.lattice[2][3] = 1 
        self.lattice[3][4] = 1 
        self.lattice[4][4] = 1 
        self.lattice[3][2] = 1 
        self.lattice[4][2] = 1 
        self.lattice[5][3] = 1 

    def nearest_neighbours(self, i, j):
        nn = [((i-1)%self.N, j), (i, (j-1)%self.N), ((i+1)%self.N, j), (i, (j+1)%self.N), ((i-1)%self.N, (j-1)%self.N), ((i+1)%self.N, (j-1)%self.N), ((i-1)%self.N, (j+1)%self.N), ((i+1)%self.N, (j+1)%self.N)]
        return nn
    

    def is_at_boundary(self, i, j):
        if i == 0 or j == 0: #i == self.N or j == self.N:
            return True
        """nearest_neighbors = self.nearest_neighbours(i, j)
        for n in nearest_neighbors:
            if n[0] == 0 or n[0] == self.N or n[1] == 0 or n[1] == self.N:
                return True"""
        return False
        """for neighbor_i, neighbor_j in nearest_neighbors:
            # Check if the neighbor is outside the lattice boundaries
            if neighbor_i < 0 or neighbor_i >= self.N or neighbor_j < 0 or neighbor_j >= self.N:
                return True  # Point is at the boundary
        return False  # Point is not at the boundary"""
    """
    def update_lattice(self):
        new_lattice = np.copy(self.lattice)
        for i in range(self.N):
            for j in range(self.N):
                point = self.lattice[i, j]
                nn = self.nearest_neighbours(i, j)
                sum = 0
                for n in nn:
                    sum += self.lattice[n[0], n[1]]
                #print(sum)
                if point == 1:
                    if sum != 2 and sum != 3:
                        new_lattice[i, j] = 0
                elif point == 0:
                    if sum == 3:
                        new_lattice[i, j] = 1
        self.lattice = new_lattice
    """
    def count(self):
        active = np.sum(self.lattice)
        return active
    
    def update_lattice(self):
        kernel = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]])

        convolved = convolve2d(self.lattice, kernel, mode='same', boundary='wrap')

        new_lattice = np.where((self.lattice == 1) & ((convolved < 2) | (convolved > 3)), 0, self.lattice)
        new_lattice = np.where((self.lattice == 0) & (convolved == 3), 1, new_lattice)

        self.lattice = new_lattice
    

