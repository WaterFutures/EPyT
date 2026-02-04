## Writes MSX File e.g.Net2.msx.
# This example contains: 
# 
# * Load a network. 
# * Set Input Arguments: Filename Section Title Section Options Section Species 
# Section Coefficients Section Terms Section Pipes Section Tanks Section Sources
# Section Quality Global Section Quality Section Parameters Section Patterns. 
# * Write MSX File.
# * Load MSX File. 
# * Compute. 
# * Unload libraries.

import os
from time import sleep

from epyt import networks
from epyt.epanet import epanet, epanetmsxapi

nets = networks.inp_files()
inpname = nets.net2_cl2
d = epanet(inpname)

msx = d.initializeMSXWrite()
msx.FILENAME = "cl2testwrite.msx"
msx.TITLE = "CL2 setMSXwrite"
msx.AREA_UNITS = 'FT2'
msx.RATE_UNITS = 'DAY'
msx.SOLVER = 'EUL'
msx.COUPLING = 'NONE'
msx.COMPILER = 'NONE'
msx.TIMESTEP = 1000
msx.ATOL = 0.001
msx.RTOL = 0.001

msx.SPECIES = {'BULK CL2 MG 0.01 0.001', 'BULK TRS MG 0.001 0.0012'}

msx.COEFFICIENTS = {'PARAMETER Kb 0.3', 'PARAMETER Kw 1'}
msx.TERMS = {'Kf 1.5826e-4 * RE^0.88 / D'}
msx.PIPES = {'RATE CL2 -Kb*CL2-(4/D)*Kw*Kf/(Kw+Kf)*CL2'}
msx.TANKS = {'RATE CL2 -Kb*CL2'}
msx.SOURCES = {'CONC 1 CL2 0.8 '}
msx.GLOBAL = {'Global CL2 0.5'}
msx.QUALITY = {'NODE 26 CL2 0.1'}
msx.PARAMETERS = {''}
msx.PATERNS = {''}
d.writeMSXFile(msx)
sleep(.5)

d.loadMSXFile(msx.FILENAME)
d.unloadMSX()
d.unload()
