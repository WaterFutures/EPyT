from epyt import epanet

# Model + time settings

d = epanet('ky10.inp')
TIME_H     = 24 * 3600          # 24 hours
HYD_STEP   = 15 * 60            # 15 min
PAT_STEP   = 15 * 60
RPT_STEP   = 15 * 60

LINK_LEAK_AREA = 3e-7
EMITTER_COEFF = 0.002

d.setTimeSimulationDuration(TIME_H)
d.setTimeHydraulicStep(HYD_STEP)
d.setTimePatternStep(PAT_STEP)
d.setTimeReportingStep(RPT_STEP)

linkID  = d.getLinkNameID(10)
pipe_ix = d.getLinkIndex(linkID)

nodeID  = d.getNodeNameID(10)
junc_ix = d.getNodeIndex(nodeID)

# Apply leakage settings

d.setLinkLeakArea(pipe_ix, LINK_LEAK_AREA)
d.setLinkExpansionProperties(pipe_ix, 0.5)   # example elasticity coefficient

d.setNodeEmitterCoeff(junc_ix, EMITTER_COEFF)

p_unit = d.getOptionsPressureUnits()
q_unit = d.getFlowUnits()

print(f"[Units] Flow={q_unit} | Pressure={p_unit} ")
print(f"[Params] LinkLeakArea={LINK_LEAK_AREA:g} m^2 | EmitterCoeff={EMITTER_COEFF:g}")

# Run hydraulics

d.openHydraulicAnalysis()
d.initializeHydraulicAnalysis()

t = 0.0
while True:
    d.runHydraulicAnalysis()

    # Leakages
    leak_pipe = d.getLinkLeakageRate(pipe_ix)
    leak_node = d.getNodeLeakageFlow(junc_ix)
    emitter   = d.getNodeEmitterFlow(junc_ix)

    # Demand
    dem_req   = d.getConsumerDemandRequested(junc_ix)
    dem_del   = d.getConsumerDemandDelivered(junc_ix)

    # Optional diagnostics
    Pj = d.getNodePressure(junc_ix)

    total_out = max(dem_del + leak_pipe + leak_node + emitter, 1e-12)
    leak_share = 100.0 * (leak_pipe + leak_node + emitter) / total_out

    print(
        f"t={t:5.0f}s | P={Pj:7.3f} {p_unit:>3} | "
        f"PipeLeak={leak_pipe:9.4f} | NodeLeak={leak_node:9.4f} | Emitter={emitter:8.4f} | "
        f"DemReq={dem_req:8.3f} | DemDel={dem_del:8.3f} | LeakShare={leak_share:5.1f}%"
    )

    dt = d.nextHydraulicAnalysisStep()
    if dt <= 0:
        break
    t += dt

d.closeHydraulicAnalysis()
d.unload()