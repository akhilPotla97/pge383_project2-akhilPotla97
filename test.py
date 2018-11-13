#!/usr/bin/env python

import os
import unittest
from mpi4py import MPI
import numpy as np

from project2 import LaplaceSolverMPI

class TestLaplaceSolverMPI(unittest.TestCase):

    def setUp(self):

        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.rank

    def test_top_bcs(self):
        
        solver = LaplaceSolverMPI(self.comm, nx=4, ny=3)
        solver.set_boundary_condition(side='top', boundary_condition_function=lambda x,y: 10)
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[0., 0., 0., 0.], [0., 4.09090909, 4.09090909,  0.], [10., 10., 10., 10.]]), atol=0.01) 

    def test_left_bc(self):
        
        solver = LaplaceSolverMPI(self.comm, nx=4,ny=4)
        solver.set_boundary_condition(side='left', boundary_condition_function=lambda x,y: 7)
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[7., 0., 0., 0.],[7., 2.625, 0.875, 0.], [7., 2.625, 0.875, 0.   ],[7., 0., 0., 0.]]) , atol=0.01)
    
    
    def test_right_bc(self):
        
        solver = LaplaceSolverMPI(self.comm, nx=4,ny=3)
        solver.set_boundary_condition(side='right', boundary_condition_function=lambda x,y: 5)
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[0., 0., 0.,5.], [0., 0.121212, 0.787879, 5.],[0., 0., 0., 5.]]), atol=0.01)
    
    
    def test_bottom_bc(self):
        solver = LaplaceSolverMPI(self.comm, nx=3,ny=3)
        solver.set_boundary_condition(side='bottom', boundary_condition_function=lambda x,y: 14)
        solver.solve()
        sol = solver.get_solution()
        if self.rank == 0:
            np.testing.assert_allclose(sol, np.array([[14., 14., 14.], [0.,3.5,0.],[0.,0.,0.]]), atol=0.01)




if __name__ == '__main__':
    unittest.main()
