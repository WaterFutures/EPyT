""" This example runs the quality analysis of a network.

    The example contains:
        Load a network.
        Run Water Quality analysis of a network.
        Compute Quality step by step.
        Unload library.

    Based on EX3_Quality_analysis.m of EPANET-Matlab-Toolkit:
        https://github.com/MariosDem/EPANET-Matlab-Toolkit/blob/master/examples/EX3_Quality_analysis.m
"""
from epyt import epanet
import time

# Load a network.
d = epanet('Net2.inp')

# Run Water Quality analysis of a network (This function contains events)
tic = time.perf_counter()
qual_res = d.getComputedQualityTimeSeries()  # Value x Node, Value x Link
toc = time.perf_counter()
qual_res.disp()

# Compute Quality step by step.
tic = time.perf_counter()
d.solveCompleteHydraulics()
d.openQualityAnalysis()
d.initializeQualityAnalysis()
tleft, P, T, QsN, QsL = 1, [], [], [], []
while tleft > 0:
    t = d.runQualityAnalysis()
    P.append(d.getNodePressure())
    QsN.append(d.getNodeActualQuality())
    QsL.append(d.getLinkQuality())
    T.append(t)
    tleft = d.stepQualityAnalysisTimeLeft()

d.closeQualityAnalysis()
toc = time.perf_counter()

# API: Compute Quality step by step.
tic = time.perf_counter()
d.api.ENsolveH()
d.api.ENopenQ()
d.api.ENinitQ(d.ToolkitConstants.EN_SAVE)
tleft, T, QsN, QsL = 1, [], [], []
while tleft > 0:
    t = d.api.ENrunQ()
    QsN.append(d.api.ENgetnodevalues(d.ToolkitConstants.EN_QUALITY))
    QsL.append(d.api.ENgetlinkvalues(d.ToolkitConstants.EN_QUALITY))
    T.append(t)
    tleft = d.api.ENstepQ()

d.api.ENcloseQ()
toc = time.perf_counter()
d.printv(QsN)

print(f"getComputedQualityTimeSeries() runtime: {toc - tic:.6f} s")
print(f"Step-by-step (wrapper) runtime: {toc - tic:.6f} s")
print(f"Step-by-step (API) runtime: {toc - tic:.6f} s")

# Unload library
d.unload()
