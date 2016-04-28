spatial_analysis
==================

Analysis of spatial and genetic distance data in Python. Integrates Mantel tests, partial Mantel tests and AMOVA.

Description
----------

As currently built, this script takes non-redundant matrices of distance data and genetic data. Or, if running a partial Mantel test, a third matrix of potentially correlated data.

These matrices should be provided in the user-provided input directory as .csv files, as follows:
- The genetic distance file must have the  file name starting with 'gen'
- The geographic distance file must have the  file name starting with 'geo'
- The control data (for partial mantel) file must have the file name starting with 'control'


Requirements
----------

- Python 3
- NumPy
- SciPy
- Mantel

I am working to write an AMOVA script for python, but until then please install the 'ade4' package in your R console with the following command:
```r
install.packages('ade4')
```


References
----------

Although I have included the code for Mantel in this repository, please refer to the download page for that software package for updates.

Mantel: https://github.com/jwcarr/MantelTest


License
----------

This code is distributed under a GNU General Public License v3.0.

Please refer to the website for Mantel for that license.