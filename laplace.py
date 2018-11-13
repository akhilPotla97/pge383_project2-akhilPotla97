#!/usr/bin/env python

import numpy as np

class Grid:
    """
        Simple class to generate a computational grid and apply boundary conditions.
    """
    
    def __init__(self, nx=10, ny=10, xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0):
        
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.nx, self.ny = nx, ny
        
        self.dx = (xmax - xmin) / (nx - 1)
        
        self.dy = (ymax - ymin) / (ny - 1)
        
        self.u = np.zeros((ny, nx), dtype=np.double)


    def set_boundary_condition(self, side, boundary_condition_function = lambda x,y: 0.0):
    
        xmin, ymin = self.xmin, self.ymin
        
        xmax, ymax = self.xmax, self.ymax
        
        x = np.arange(xmin, xmax, self.dx)
        
        y = np.arange(ymin, ymax, self.dy)
        
        if side == 'bottom':
            self.u[0 ,:] = boundary_condition_function(xmin, y)
        elif side == 'top':
            self.u[-1 ,:] = boundary_condition_function(xmax, y)
        elif side == 'left':
            self.u[:, 0] = boundary_condition_function(x, ymin)
        elif side == 'right':
            self.u[:, -1] = boundary_condition_function(x, ymax)
        

class LaplaceSolver(Grid):
    """
        Class that solves the Laplace equation in 2D 
    """
    
    def iterate(self):
        """
            A Python (slow) implementation of a finite difference iteration
        """
        
        u = self.u
        
        nx, ny = u.shape        
        
        dx2, dy2 = self.dx ** 2, self.dy ** 2
        
        err = 0.0
        
        for i in range(1, nx - 1):
            
            for j in range(1, ny - 1):
                
                tmp = u[i,j]
                
                u[i,j] = ((u[i-1, j] + u[i+1, j]) * dy2 +
                          (u[i, j-1] + u[i, j+1]) * dx2) / (dx2 + dy2) / 2
                
                diff = u[i,j] - tmp
                
                err += diff * diff

        return np.sqrt(err)
    
                
    def solve(self, max_iterations=10000, tolerance=1.0e-16, quiet=False):        
        """
            Calls iterate() sequentially until the error is reduced below a tolerance.
        """
        
        for i in range(max_iterations):
        
            error = self.iterate()
            
            if error < tolerance:
                if not quiet:
                    print("Solution converged in " + str(i) + " iterations.")
                break
                
    def get_solution(self):
        return self.u
