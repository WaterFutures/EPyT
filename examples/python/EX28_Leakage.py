# EPyT (EPANET 2.3) — FAVAD leakage demo

import numpy as np
import matplotlib.pyplot as plt
from epyt import epanet


def main():
    # ===== Input file =====
    INP = "Net1.inp"
    d = epanet(INP)

    q_unit = d.getFlowUnits()
    p_unit = d.getOptionsPressureUnits()
    print(f"[Units] Flow={q_unit} | Pressure={p_unit}")

    # ===== Simulation settings =====
    SIM_HOURS = 24
    HYD_STEP_MIN = 60

    d.setTimeSimulationDuration(SIM_HOURS * 3600)
    d.setTimeHydraulicStep(HYD_STEP_MIN * 60)

    n_links = d.getLinkCount()

    # ===== Apply leakage to multiple links =====
    # (LinkID, LC1, LC2)
    leak_links = [
        ("21", 1.0, 0.10),
        ("12", 0.8, 0.05),
        ("31", 0.9, 0.08),
    ]

    print("\n===== APPLY LEAKAGE =====")
    leak_link_ids = [x[0] for x in leak_links]
    leak_link_indices = []

    for link_id, lc1, lc2 in leak_links:
        link_idx = d.getLinkIndex(link_id)
        if (link_idx is None) or (link_idx <= 0):
            raise ValueError(f'Link ID "{link_id}" not found.')

        leak_link_indices.append(link_idx)

        d.setLinkLeakArea(link_idx, lc1)
        d.setLinkExpansionProperties(link_idx, lc2)

        print(f"Applied leakage to link {link_id} (index {link_idx}): LC1={lc1:.6g}, LC2={lc2:.6g}")

    # ===== Run hydraulics and retrieve time series =====
    # EPyT expects strings (not lists) for each attribute
    res = d.getComputedHydraulicTimeSeries([
        "linkleakagerate",
        "nodeleakageflow",
        "emitterflow",
        "demanddelivered",
        "demandrequested"]
    )

    time_s = np.asarray(res.Time).reshape(-1)
    time_h = time_s / 3600.0

    leak_link_ts = np.asarray(res.LinkLeakageRate)  # [time x links] (L/s)
    leak_node_ts = np.asarray(res.NodeLeakageFlow)  # [time x nodes] (L/s)

    # ===== Core results: totals, averages, peak, volumes =====
    total_leak_ts_lps = np.nansum(leak_link_ts, axis=1)
    avg_total_leak_lps = float(np.nanmean(total_leak_ts_lps))

    if time_s.size >= 2:
        total_leaked_volume_m3 = float(np.trapezoid(total_leak_ts_lps, time_s) / 1000.0)  # (L/s)*s -> L -> m^3
    else:
        total_leaked_volume_m3 = float("nan")

    idx_peak = int(np.nanargmax(total_leak_ts_lps))
    peak_total_leak_lps = float(total_leak_ts_lps[idx_peak])
    t_peak_h = float(time_h[idx_peak])

    print("\n===== LEAKAGE SUMMARY =====")
    print(f"Average total leakage   : {avg_total_leak_lps:.3f} L/s")
    print(f"Peak total leakage      : {peak_total_leak_lps:.3f} L/s at t = {t_peak_h:.2f} h")
    print(f"Total leaked volume     : {total_leaked_volume_m3:.2f} m3/day (over {SIM_HOURS} h)")

    # ===== Per-link mean leakage and peak snapshot =====
    avg_leak_per_link_lps = np.nanmean(leak_link_ts, axis=0).reshape(-1)  # [links]
    leak_at_peak_lps = leak_link_ts[idx_peak, :].reshape(-1)              # [links]

    # ===== Links by mean leakage =====
    topN = 3
    sorted_ix = np.argsort(-avg_leak_per_link_lps)  # descending
    topN = min(topN, n_links)

    top_link_index = sorted_ix[:topN] + 1  # EPANET link indexing is 1-based
    top_link_leak = avg_leak_per_link_lps[sorted_ix[:topN]]

    top_link_id = []
    for idx0 in sorted_ix[:topN]:
        idx1 = int(idx0 + 1)
        top_link_id.append(str(d.getLinkNameID(idx1)))

    print(f"\nTop-{topN} links by MEAN leakage (L/s):")
    for rank in range(topN):
        print(f"{rank+1:>2}. LinkIndex={int(top_link_index[rank])} | LinkID={top_link_id[rank]} | MeanLeak_LPS={top_link_leak[rank]:.6g}")

    # ===== Consistency checks for ALL leaky links (end nodes for each link) =====
    print("\n===== CONSISTENCY CHECKS (per leaky link) =====")
    tol_L = 0.01

    for link_id, link_idx in zip(leak_link_ids, leak_link_indices):
        nodes = d.getLinkNodesIndex(link_idx)  # [node1, node2] (1-based)
        node1 = int(nodes[0])
        node2 = int(nodes[1])

        # numpy uses 0-based indices
        node_cols = [node1 - 1, node2 - 1]
        link_col = link_idx - 1

        leak_nodes_total = float(np.nansum(leak_node_ts[:, node_cols]))
        leak_link_total = float(np.nansum(leak_link_ts[:, link_col]))
        abs_diff = abs(leak_link_total - leak_nodes_total)

        print(
            f"Link {link_id} (idx {link_idx}) nodes ({node1},{node2}): "
            f"LinkSum={leak_link_total:.4f} | NodeSum={leak_nodes_total:.4f} | Diff={abs_diff:.4f}"
        )

        if not (abs_diff < tol_L):
            raise AssertionError(f"Leak mismatch for link {link_id}: link != nodes (Diff={abs_diff})")

    # ===== Plots =====
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle("Leakage Results")

    # 1) Total leakage over time
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(time_h, total_leak_ts_lps, linewidth=1.5)
    ax1.grid(True)
    ax1.set_xlabel("Time (h)")
    ax1.set_ylabel("Total leakage (L/s)")
    ax1.set_title("Total leakage time series")
    ax1.plot(time_h[idx_peak], peak_total_leak_lps, marker="o")
    ax1.text(time_h[idx_peak], peak_total_leak_lps, f"  Peak {peak_total_leak_lps:.2f} L/s @ {t_peak_h:.2f} h", va="bottom")

    # 2) Leakage over time for each leaky link
    ax2 = plt.subplot(2, 2, 2)
    for link_id, link_idx in zip(leak_link_ids, leak_link_indices):
        ax2.plot(time_h, leak_link_ts[:, link_idx - 1], linewidth=1.5, label=f"Link {link_id}")
    ax2.grid(True)
    ax2.set_xlabel("Time (h)")
    ax2.set_ylabel("Leakage (L/s)")
    ax2.set_title("Leakage on selected links")
    ax2.legend()

    # 3) Links bar (mean leakage)
    ax3 = plt.subplot(2, 2, 3)
    ax3.bar(np.arange(1, topN + 1), top_link_leak)
    ax3.grid(True)
    ax3.set_xlabel("Rank")
    ax3.set_ylabel("Mean leakage (L/s)")
    ax3.set_title("Links by mean leakage")
    ax3.set_xticks(np.arange(1, topN + 1))
    ax3.set_xticklabels(top_link_id)

    # 4) Sum of leakage at end nodes (per leaky link)
    ax4 = plt.subplot(2, 2, 4)
    for link_id, link_idx in zip(leak_link_ids, leak_link_indices):
        nodes = d.getLinkNodesIndex(link_idx)
        node_cols = [int(nodes[0]) - 1, int(nodes[1]) - 1]
        ax4.plot(time_h, np.nansum(leak_node_ts[:, node_cols], axis=1), linewidth=1.5, label=f"Nodes of {link_id}")
    ax4.grid(True)
    ax4.set_xlabel("Time (h)")
    ax4.set_ylabel("End-node leakage (L/s)")
    ax4.set_title("Leakage at end nodes of selected links")
    ax4.legend()

    plt.tight_layout()
    plt.show()

    # ===== Close EPANET object =====
    d.unload()

if __name__ == "__main__":
    main()
