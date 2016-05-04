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

This program currently works with Linux operating systems, but has not yet been tested on Windows.

I am working to write an AMOVA script for python, but until then please install the 'ade4' package in your R console with the following command (I haven't gotten this to work with my script, so ignore this for now):
```r
install.packages('ade4')
```

Input commands
--------------

- --in_dir: input directory containing your 2 or 3 .csv data files
- --out_dir: where you want your results files to go
- --sim: enter 'y' to simulate data, or 'n' to skip
- --m: enter 'f' to perform a full mantel test, 'p' to perform a partial mantel test, or 'n' to skip

Note: if you are running a full mantel test, you only need two input data files, a 'gen' and a 'geo' file. For the partial mantel test, you need a third input file with a name that starts with 'control'. Example input files are provided in the spatial_analysis repository.

Example of input commands for Linux:

```
python spatial_analysis.py --in_dir /Users/home/spatial_analysis/ --out_dir /Users/home/spatial_analysis/results/ --sim n --m p
```


References
----------

Although I have included the code for Mantel in this repository, please refer to the download page for that software package for updates.

Mantel: https://github.com/jwcarr/MantelTest


License
----------

This code is distributed under a GNU General Public License v3.0.

Please refer to the website for Mantel for that license.