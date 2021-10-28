# NASICON_KMC_paper_data
Source code to reproduce NASICON KMC simulation
Author: Zeyu Deng
Email: dengzeyu@gmail.com

# Prerequisites Python libraries:
python numpy scipy pandas numba tables

# Steps:
1. Go into kmc folder
2. python run_kmc.py comp structure_index T 
comp is the parametric composition from 0 to 1, for Na<sub>1+x</sub>Zr<sub>2</sub>Si<sub>x</sub>P<sub>3-x</sub>O<sub>12</sub>, x = 3-3*comp
structure_index can be any integer from 0 to 49
T is temperature in Kelvin

# Example
python run_kmc.py 0.1 1 573
