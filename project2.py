#!/usr/bin/env python

import numpy as np

from laplace import LaplaceSolver


class LaplaceSolverMPI(LaplaceSolver):

    def __init__(self, comm, **kwargs):
        self.comm = comm
        self.rank = comm.rank
        self.size = comm.size
        # print('=======================')
        # print('rank: ', self.rank)
        # print('size: ', self.size)
        super().__init__(**kwargs)


    def set_boundary_condition(self, **kwargs):
        if self.rank == 0:
            super().set_boundary_condition(**kwargs)



#    def solve(self, max_iterations=10000, tolerence=1.0e-16, verbose=False):
#        """
#        1. distribute the rows of the solution matrix as evenly as possible
#        amoung the processers
#        """
#        n = np.array_split(self.u, self.size)
#        print('u: ', self.u)
#        print('n: ', n)
#        print('')
#        print('')
#
#        return
#
#
#
#    def get_solution(self):
#
#        return


if __name__ == "__main__":

    from mpi4py import MPI

    comm = MPI.COMM_WORLD

    solver = LaplaceSolverMPI(comm, nx=4, ny=3)
    print(solver.u)
    solver.set_boundary_condition(side='right', boundary_condition_function=lambda x,y: 5)
    solver.solve(verbose=True)
    u = solver.get_solution()
    if comm.rank == 0:
        print(u)
