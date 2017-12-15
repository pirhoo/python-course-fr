"""
Create a notebook containing code from a script.

Convert one: python py2ipynb.py exercises/01_hello_world.py
Convert all: find exercises/*.py -exec python py2ipynb.py {} \;
"""
import sys

import nbformat
from os import path
from nbformat.v4 import new_notebook, new_code_cell

pyfile = path.basename(sys.argv[1])
ipynbfile = sys.argv[1].replace('.py', '.ipynb')

nb = new_notebook()
nb.cells.append(new_code_cell('%load ' + pyfile))
nbformat.write(nb, ipynbfile)

print("Created: %s" % ipynbfile)
