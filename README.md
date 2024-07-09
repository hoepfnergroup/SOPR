# Structure-Optimized Potential Refinement (SOPR)

## General Information
Source code for running the Structure-Optimized Potential Refinement (SOPR) approach to optimize atomic pair potentials that are benchmarked to the radial distribution functions of simple liquids. 

SOPR is an iterative predictor-corrector numerical method to determine the unique structure-optimized pair potential for a given radial distribution function. The provided jupyter notebook is an example code designed for analyzing experimental diffraction measurements in monoatomic liquids (eg. noble gases, metals, etc) applied to liquid neon at 42K. See (J. Phys. Chem. Lett. 2022, 13, 49, 11512–11520) for details on the algorithm as well as discussions on the motivations to constructing force fields from experimental measurements of liquid structure.    

## Required Software for Monatomic Structure Refinement
HOOMD_Blue ver 4.7.0: https://hoomd-blue.readthedocs.io/en/latest/installation.html <br />
Freud ver 3.1.0: https://freud.readthedocs.io/en/latest/ <br />

## Version History
SOPR v1.1 is designed for monatomic liquids that are benchmarked to real-space (r) isotropic pair distrubution functions. 

## Acknowledgement
The source code development was supported by the National Science Foundation under award number CBET-1847340. Developed at the University of Utah, Department of Chemical Engineering by Brennon Shanks and Michael P. Hoepfner.  
