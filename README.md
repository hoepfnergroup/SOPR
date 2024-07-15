# Structure-Optimized Potential Refinement (SOPR)

## General Information
Source code for running the Structure-Optimized Potential Refinement (SOPR) approach to optimize atomic pair potentials that are benchmarked to the radial distribution functions of simple liquids. 

SOPR is an iterative predictor-corrector numerical method to determine the unique structure-optimized pair potential for a given radial distribution function. The provided jupyter notebook is an example code designed for analyzing experimental diffraction measurements in monoatomic liquids (eg. noble gases, metals, etc) applied to liquid neon at 42K. See (J. Phys. Chem. Lett. 2022, 13, 49, 11512–11520) for details on the algorithm as well as discussions on the motivations to constructing force fields from experimental measurements of liquid structure.    

## Required Software for Monatomic Structure Refinement
sopr_v1.1:
  updates:
    - New inverse squared-exponential kernel to improve Gaussian process regression of the tabulated refinement potential.
    - Updated to newest HOOMD and Freud versions as of July, 2024.
    - Improved figure readability and comments.
    
HOOMD_Blue ver 4.7.0: https://hoomd-blue.readthedocs.io/en/latest/installation.html <br />
Freud ver 3.1.0: https://freud.readthedocs.io/en/latest/ <br />

## Version History
SOPR v0.2 - Monatomic liquid radial distribution function potential refinement using squared-exponential kernel Gaussian processes.

SOPR v1.1 - Updates to Gaussian process kernel to reduce spurious long-range potential oscillations as well as HOOMD and Freud package versions.

## Acknowledgement
The source code development was supported by the National Science Foundation under award number CBET-1847340. Developed at the University of Utah, Department of Chemical Engineering by Brennon Shanks and Michael P. Hoepfner.  

## Cite 
Shanks, B. L., Potoff, J. J. & Hoepfner, M. P. Transferable Force Fields from Experimental Scattering Data with Machine Learning Assisted Structure Refinement. J. Phys. Chem. Lett. 13, 11512–11520 (2022).

