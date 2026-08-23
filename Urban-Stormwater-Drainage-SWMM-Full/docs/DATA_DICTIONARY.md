# Data Dictionary

## rainfall_sensitivity.csv

- `case`: rainfall multiplier label.
- `rainfall_mm`: total rainfall depth.
- `surface_runoff_mm`: SWMM runoff depth.
- `peak_outfall_m3s`: peak discharge at the outfall.
- `total_flooding_m3`: network flooding volume.
- `J7_flooding_m3`: flooding volume at junction J7.
- `C5_peak_flow_m3s`: peak flow through conduit C5.
- `C5_max_full`: maximum flow/full-flow ratio reported for C5.
- `runoff_continuity_error_pct`: runoff continuity error.
- `routing_continuity_error_pct`: routing continuity error.

## urbanization_sensitivity.csv

Same hydraulic outputs, with `imperviousness_change_pp` giving the uniform increase in imperviousness in percentage points.

## pipe_capacity_sensitivity.csv

- `C5_diameter_m`: tested C5 diameter.
- `flood_reduction_vs_baseline_pct`: percentage reduction in flooding relative to the 0.75 m baseline.

## network_parameters.csv

Contains baseline subcatchment, node and conduit parameters used to construct the conceptual model.

## design_storm.csv

Stores the base synthetic rainfall intensity pattern `P`. Scenario `.inp` files apply the required scaling to this pattern.
