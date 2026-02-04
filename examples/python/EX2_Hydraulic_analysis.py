""" Runs the hydraulic analysis of a network.

    This example contains:
      Load a network.
      Set simulation time duration.
      Hydraulic analysis using ENepanet binary file.
      Hydraulic analysis using EN functions.
      Hydraulic analysis step-by-step.
      Unload library.
"""
# Run hydraulic analysis of a network
from epyt import epanet
import time

# Load a network.
d = epanet('L-TOWN.inp', loadfile=True)

## Set simulation time duration.
hrs = 100
d.setTimeSimulationDuration(hrs*3600)

# # Hydraulic analysis using epanet2.exe binary file.
start_1 = time.time()
hyd_res_1 = d.getComputedTimeSeries_ENepanet()
stop_1 = time.time()
# hyd_res_1.disp()

# # Hydraulic analysis using epanet2.exe binary file.
start_2 = time.time()
hyd_res_2 = d.getComputedTimeSeries()
stop_2 = time.time()
# hyd_res_2.disp()

# Hydraulic analysis using the functions ENopenH, ENinit, ENrunH, ENgetnodevalue/&ENgetlinkvalue, ENnextH, ENcloseH.
# (This function contains events)
start_3 = time.time()
hyd_res_3 = d.getComputedHydraulicTimeSeries(['flow', 'pressure'])
stop_3 = time.time()
# hyd_res_3.disp()

# Hydraulic analysis step-by-step using the functions ENopenH, ENinit, ENrunH, ENgetnodevalue/&ENgetlinkvalue,
# ENnextH, ENcloseH. (This function contains events)

start_4 = time.time()
d.openHydraulicAnalysis()
d.initializeHydraulicAnalysis()
tstep, P, T_H, D, H, F = 1, [], [], [], [], []
while tstep > 0:
    t = d.runHydraulicAnalysis()
    P.append(d.getNodePressure())
    D.append(d.getNodeActualDemand())
    H.append(d.getNodeHydraulicHead())
    F.append(d.getLinkFlows())
    T_H.append(t)
    tstep = d.nextHydraulicAnalysisStep()
d.closeHydraulicAnalysis()
stop_4 = time.time()

# print(f'Pressure: {P}')
# print(f'Demand: {D}')
# print(f'Hydraulic Head {H}')
# print(f'Flow {F}')

# Using API functions
start_5 = time.time()
d.api.ENopenH()
d.api.ENinitH(d.ToolkitConstants.EN_NOSAVE)
tstep, P, T_H, F = 1, [], [], []
while tstep > 0:
    t = d.api.ENrunH()
    P.append(d.api.ENgetnodevalues(d.ToolkitConstants.EN_PRESSURE))
    # F.append(d.api.ENgetlinkvalues(d.ToolkitConstants.EN_FLOW))
    T_H.append(t)
    tstep = d.api.ENnextH()
d.api.ENcloseH()
stop_5 = time.time()

# Unload library.
d.unload()

print(f'Elapsed time for the function `getComputedTimeSeries_ENepanet` is: {stop_1 - start_1:.8f}')
print(f'Elapsed time for the function `getComputedTimeSeries` is: {stop_2 - start_2:.8f}')
print(f'Elapsed time for the function `getComputedHydraulicTimeSeries` is: {stop_3 - start_3:.8f}')
print(f'Elapsed time for `step-by-step` analysis is: {stop_4 - start_4:.8f}')
print(f'Elapsed time for `API step-by-step` analysis is: {stop_5 - start_5:.8f}')
