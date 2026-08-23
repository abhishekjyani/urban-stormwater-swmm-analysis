# Methodology

## 1. Baseline drainage model

A conceptual 12-ha urban drainage network was created with six subcatchments, seven junctions, eight conduits, and one free outfall. Dynamic Wave routing was used to capture surcharge and flooding behavior. Horton infiltration was used for pervious areas.

## 2. Subcatchment surface parameters

For all subcatchments:

- Manning n, impervious: 0.013
- Manning n, pervious: 0.24
- Depression storage, impervious: 1.5 mm
- Depression storage, pervious: 5 mm

Horton infiltration:

- Maximum infiltration: 75 mm/h
- Minimum infiltration: 10 mm/h
- Decay coefficient: 2 h^-1
- Drying time: 7 d

Detailed geometry and baseline imperviousness are listed in `results/network_parameters.csv`.

## 3. Rainfall forcing

A synthetic 2-hour intensity pattern was defined at 10-minute intervals. Scenario multipliers of 0.6, 0.8, 1.0, 1.2, and 1.4 were applied without changing the storm shape.

The baseline 0.6P event gives 66 mm total rainfall.

## 4. Rainfall sensitivity

Only rainfall magnitude was changed. Land-use and pipe-network parameters were held fixed. Outputs compared were:

- surface runoff depth,
- peak outfall discharge,
- total flooding volume,
- flooding at J7,
- C5 peak flow and Max/Full ratio,
- continuity errors.

## 5. Urbanization sensitivity

Rainfall remained fixed at 0.6P. Imperviousness was increased uniformly by +15 and +30 percentage points across the six subcatchments.

## 6. Capacity sensitivity

Rainfall and land-use conditions remained fixed at the baseline. Only C5 diameter was changed:

- 0.75 m baseline,
- 0.90 m,
- 1.05 m.

Flood reduction was calculated as:

`100 * (V_flood,baseline - V_flood,case) / V_flood,baseline`

## 7. Numerical checks

Runoff and routing continuity errors were recorded from each SWMM report. Global continuity errors remained small for all cases. Non-converging routing-step percentages should still be checked when interpreting local hydraulic details.
