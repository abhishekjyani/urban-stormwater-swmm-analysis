from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

rain = pd.read_csv(RESULTS / "rainfall_sensitivity.csv")
urb = pd.read_csv(RESULTS / "urbanization_sensitivity.csv")
cap = pd.read_csv(RESULTS / "pipe_capacity_sensitivity.csv")


def save_plot(x, y, xlabel, ylabel, title, filename, marker="o"):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(x, y, marker=marker)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURES / filename, dpi=220)
    plt.close(fig)


save_plot(
    rain["rainfall_mm"], rain["total_flooding_m3"],
    "Rainfall depth (mm)", "Total flooding (m³)",
    "Rainfall Sensitivity of Network Flooding", "rainfall_vs_flooding.png"
)

save_plot(
    rain["rainfall_mm"], rain["peak_outfall_m3s"],
    "Rainfall depth (mm)", "Peak outfall discharge (m³/s)",
    "Rainfall Sensitivity of Peak Outfall Discharge", "rainfall_vs_peak_outfall.png"
)

save_plot(
    urb["imperviousness_change_pp"], urb["total_flooding_m3"],
    "Increase in imperviousness (percentage points)", "Total flooding (m³)",
    "Urbanization Sensitivity of Network Flooding", "urbanization_vs_flooding.png"
)

save_plot(
    cap["C5_diameter_m"], cap["total_flooding_m3"],
    "C5 diameter (m)", "Total flooding (m³)",
    "Effect of C5 Capacity on Flooding", "c5_diameter_vs_flooding.png"
)

save_plot(
    cap["C5_diameter_m"], cap["C5_max_full"],
    "C5 diameter (m)", "C5 Max/Full ratio (-)",
    "Effect of C5 Diameter on Hydraulic Utilization", "c5_diameter_vs_max_full.png"
)

print(f"Plots written to: {FIGURES}")
