spatial_analysis
==================

Analysis of spatial and genetic distance data in Python. Integrates Mantel tests, partial Mantel tests and AMOVA.

Description
----------

As currently built, this script takes condensed matrices of distance data and genetic data. 

Or, if running a partial Mantel test, a third matrix of potentially correlated data.


Requirements
----------

- Python 3
- NumPy
- SciPy
- Mantel
- PypeR

I am working to write an AMOVA script for python, but until then please install the 'ade4' package in your R console with the following command:
```r
install.packages('ade4')
```

References
----------

Although I have included the code for both Mantel and PypeR in this repository, please refer to the respective download pages for both of those software packages for updates.

Mantel: https://github.com/jwcarr/MantelTest

PypeR: https://sourceforge.net/projects/rinpy/
PypeR paper: https://www.jstatsoft.org/article/view/v035c02/v35c02.pdf

License
----------

This code is distributed under a GNU General Public License v3.0