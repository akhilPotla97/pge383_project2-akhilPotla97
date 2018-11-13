# Project 2

For this project, you'll modify the `LaplaceSolver` class from [Homework Assignment 10](https://github.com/PGE383-HPC-Fall2018/assignment10) to run in parallel with `mpi4py`.  In the file [project2.py](project2.py), you'll find a new class `LaplaceSolverMPI` that inherits from `LaplaceSolver`.  You need to complete the `solve()` and `get_solution()` functions.  

The `solve()` function should partition and distribute the solution matrix `u` (by rows) as evenly as possible among the parallel ranks.  You will need to use `send()` and `recv()` calls to send the top/bottom rows from adjacent processors when needed to act as "boundary conditions" on the local (to processor) grid.  This is often referred to as "ghosting".  You should then be able to call the `iterate()` function from the `LaplaceSolver` class without modifications.

Keep in mind that the error returned from `iterate()` will only be the error for each local grid, but you want to stop iterating only once the global error is below `tolerence`.  You will need to devise a scheme to compute and communicate the global errors to each processor so they will all stop iterating at the same time.  It's probably not necessary to perform this communication every single iteration.

The `get_solution()` should gather the total solution back to the rank 0 processor as a single two-dimensional NumPy array.  Be careful not to double include any of the data you may have "ghosted" during the iteration.

## Testing

If you would like to check to see if your solution is correct, run the following command at the Terminal command line:

```bash
>mpiexec -np 2 python test.py
>mpiexec -np 3 python test.py
```
