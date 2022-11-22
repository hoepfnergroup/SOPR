# Structure-Optimized Potential Refinement (SOPR)
 
## General Information
Source code for running the Structure-Optimized Potential Refinement (SOPR) approach to optimize atomic pair potentials that are benchmarked to pair distribution functions. 

SOPR is an iterative predictor-corrector numerical method to determine the unique structure-optimized pair potential for a given radial distribution function. The provided jupyter notebook is an example code designed for analyzing experimental diffraction measurements in monoatomic liquids (eg. noble gases, metals, etc) applied to liquid neon at 42K. See (citation) for details on the algorithm as well as discussions on the motivations to constructing force fields from experimental measurements of liquid structure.    

## Required Software
HOOMD_Blue ver 3.0.0: https://hoomd-blue.readthedocs.io/en/latest/installation.html <br />
Freud ver 2.8.0: https://freud.readthedocs.io/en/latest/ <br />

## Version History
SOPR v0.2 is designed for monatomic liquids that are benchmarked to real-space (r) isotropic pair distrubution functions. 

## Acknowledgement
The source code development was supported by the National Science Foundation under award number CBET-1847340. Developed at the University of Utah, Department of Chemical Engineering by Brennon Shanks and Michael P. Hoepfner.  
