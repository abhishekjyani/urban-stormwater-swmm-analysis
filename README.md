# Urban Stormwater Drainage Network Modelling using EPA SWMM

A reproducible **EPA SWMM 5.2** project investigating how rainfall intensity, urbanization, and conduit capacity affect flooding in a conceptual 12-ha urban drainage network.

> **Scope:** This is a conceptual sensitivity/design study using a synthetic storm. It is not a calibrated model of a specific city and the rainfall cases should not be interpreted as return-period storms.

![Model layout](docs/swmm_model_layout.png)

## Objectives

- Develop a 12-ha urban stormwater drainage network in EPA SWMM.
- Evaluate flooding response to increasing rainfall magnitude.
- Quantify the effect of increasing imperviousness under the same storm.
- Identify the critical hydraulic bottleneck and test conduit-capacity upgrades.
- Check continuity errors and compare scenarios using Python.

## Model configuration

| Item | Configuration |
|---|---|
| Catchment area | 12 ha |
| Subcatchments | 6 |
| Junctions | 7 |
| Conduits | 8 |
| Outfall | 1 |
| Flow units | CMS |
| Infiltration | Horton |
| Routing | Dynamic Wave |
| Surcharge method | Extran |
| Reporting step | 1 min |
| Wet-weather runoff step | 1 min |
| Dry-weather step | 1 h |
| Routing step | 30 s |
| Simulation duration | 6 h |

Baseline Horton parameters: maximum infiltration = 75 mm/h, minimum infiltration = 10 mm/h, decay = 2 h^-1, drying time = 7 d.

## Synthetic design storm

The base temporal pattern `P` is stored in [`results/design_storm.csv`](results/design_storm.csv). The baseline case uses **0.6P**, corresponding to **66 mm total rainfall**. Rainfall-sensitivity cases retain the same temporal pattern and scale the magnitude to 0.8P, 1.0P, 1.2P, and 1.4P.

## Scenario 1 — Rainfall sensitivity

| Case | Rainfall (mm) | Runoff (mm) | Peak outfall (m³/s) | Flooding (m³) | C5 Max/Full |
|---|---:|---:|---:|---:|---:|
| 0.6P | 66 | 42.574 | 1.174 | 202 | 1.67 |
| 0.8P | 88 | 63.151 | 1.245 | 1,367 | 1.77 |
| 1.0P | 110 | 84.414 | 1.288 | 3,096 | 1.83 |
| 1.2P | 132 | 105.928 | 1.308 | 5,064 | 1.86 |
| 1.4P | 154 | 127.516 | 1.308 | 7,230 | 1.86 |

The peak outfall discharge approaches a plateau near **1.31 m³/s**, while flooding continues to increase sharply. This indicates that the network becomes capacity-limited under larger rainfall inputs.

![Rainfall vs flooding](figures/rainfall_vs_flooding.png)

![Rainfall vs peak outfall](figures/rainfall_vs_peak_outfall.png)

## Scenario 2 — Urbanization sensitivity

Rainfall is held at the 0.6P baseline while imperviousness is increased by 15 and 30 percentage points.

| Case | Imperviousness change | Runoff (mm) | Peak outfall (m³/s) | Flooding (m³) |
|---|---:|---:|---:|---:|
| U1 | 0 pp | 42.574 | 1.174 | 202 |
| U2 | +15 pp | 51.274 | 1.229 | 675 |
| U3 | +30 pp | 59.565 | 1.251 | 1,255 |

A **30-percentage-point increase in imperviousness** increased flooding from **202 to 1,255 m³** under identical rainfall.

![Urbanization vs flooding](figures/urbanization_vs_flooding.png)

## Scenario 3 — Critical conduit capacity

The downstream conduit **C5** was identified as the principal hydraulic bottleneck. Its baseline diameter of 0.75 m was increased while rainfall and land use remained unchanged.

| C5 diameter (m) | Peak outfall (m³/s) | Flooding (m³) | C5 Max/Full | Flood reduction |
|---:|---:|---:|---:|---:|
| 0.75 | 1.174 | 202 | 1.67 | — |
| 0.90 | 1.348 | 17 | 1.18 | 91.6% |
| 1.05 | 1.394 | 5 | 0.81 | 97.5% |

Increasing C5 from **0.75 m to 0.90 m reduced simulated flooding by 91.6%**. The additional increase to 1.05 m produced a smaller incremental benefit, illustrating diminishing hydraulic returns.

![C5 diameter vs flooding](figures/c5_diameter_vs_flooding.png)

![C5 diameter vs utilization](figures/c5_diameter_vs_max_full.png)

## Numerical checks

Across the scenarios, runoff continuity errors were approximately **-0.007% to -0.009%**, and routing continuity errors were approximately **-0.103% to -0.251%**. These small global continuity errors support the internal mass-balance consistency of the simulations.

Some runs showed a non-zero fraction of routing steps that did not fully converge internally. Therefore, the project is presented as a **conceptual comparative sensitivity study**, not a calibrated or validation-grade urban drainage model.

## Repository structure

```text
Urban-Stormwater-Drainage-SWMM/
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── model/        # SWMM .inp files for all scenarios
├── reports/      # SWMM .rpt output files
├── results/      # Clean CSV summaries and model parameters
├── figures/      # Final comparison plots
├── python/       # Reproducible plotting script
├── docs/         # Methodology, data dictionary and upload guide
└── report/       # Full technical report (PDF + DOCX)
```

## Reproducing the SWMM simulations

1. Install **EPA SWMM 5.2**.
2. Open any file in `model/`.
3. Run the simulation.
4. Compare the generated report with the corresponding file in `reports/`.
5. Use the CSV files in `results/` for cross-scenario analysis.

## Reproducing the plots

```bash
pip install -r requirements.txt
python python/plot_results.py
```

The script reads the CSV files in `results/` and regenerates the comparison figures.

## Practical engineering relevance

This workflow demonstrates how SWMM can be used for preliminary drainage planning and sensitivity analysis to assess:

- storm-sewer capacity under rainfall intensification,
- effects of urbanization and increased imperviousness,
- identification of hydraulically overloaded conduits,
- evaluation of pipe-upgrade alternatives,
- prioritization of drainage interventions before detailed design.

## Technical report

The complete methodology, model setup, scenario analysis, engineering interpretation, practical applications, numerical checks, limitations and references are available in:

- [`report/Urban_Stormwater_SWMM_Technical_Report.pdf`](report/Urban_Stormwater_SWMM_Technical_Report.pdf)
- [`report/Urban_Stormwater_SWMM_Technical_Report.docx`](report/Urban_Stormwater_SWMM_Technical_Report.docx)

## Limitations

- Conceptual network; no field calibration or observed flood validation.
- Synthetic storm rather than a site-specific IDF-derived design event.
- No cost optimization was performed for pipe upgrades.
- Results should be interpreted comparatively rather than as predictions for a real drainage system.

## Software

- EPA SWMM 5.2
- Python 3
- pandas
- matplotlib
