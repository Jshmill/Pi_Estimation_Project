# Estimating π with a Checkerboard

Repository containing Python scripts to estimate π using a Monte Carlo method
based on a checkerboard pattern.

## Pi_estimation.py

The original script simulates dropping differently sized disks onto a
checkerboard and calculates the probability of the disks touching so many
squares around it, which can be used to estimate the value of π.

## 3d_pi_estimation.py

This script extends the original 2D estimation to a 3D version, where spheres
are dropped onto a 3D checkerboard. The estimation of π is then based on the
probability of the spheres touching a certain number of cubes around them.

## Run

To run either of the scripts, ensure you have Python installed on your system.
You can execute the scripts using the command line:

```bash
python pi_estimation.py
```

or

```bash
python 3d_pi_estimation.py
```
