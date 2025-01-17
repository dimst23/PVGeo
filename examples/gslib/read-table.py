"""
Read GSLib Table
~~~~~~~~~~~~~~~~

Read any GSLib file as a table :class:`pyvist.Table`

"""
from pyvista import examples

from PVGeo.grids import TableToTimeGrid
from PVGeo.gslib import GSLibReader

###############################################################################

# points_url = 'http://www.trainingimages.org/uploads/3/4/7/0/34703305/sundarbans.zip'
filename, _ = examples.downloads._download_file('sundarbans.SGEMS.zip')

reader = GSLibReader()
table = reader.apply(filename)
# Print the file header
print(reader.get_file_header())

###############################################################################
table

###############################################################################
# From inspecting the header, we realize that this dataset is gridded, so let's
# use the :class:`PVGeo.grid.TableToTimeGrid` filter to create a
# :class:`pyvista.UniformGrid` of that dataset.

# 1200 x, 1750 y, 1 z, 1 t
grid = TableToTimeGrid(extent=(1200, 1750, 1, 1), order='F').apply(table)
grid

###############################################################################
grid.plot(cpos='xy')
