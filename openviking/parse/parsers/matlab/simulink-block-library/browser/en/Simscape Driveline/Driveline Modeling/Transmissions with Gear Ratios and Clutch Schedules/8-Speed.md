---
type: simulink-block
title: '8-Speed'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Transmissions with Gear Ratios and Clutch Schedules'
documentation_page: '8speed'
documentation_source_path: 'ref/8speed.html'
language: en
---

# 8-Speed

## Ports

### Input

### **Gear** — Numerical input for the gear scalar

Specify -1 for reverse, 0 for neutral, and 1–8 for the forward
gears.

**Data Types:** `single` | `double`
### Conserving

### **B** — Base interface mechanical rotational

Conserving port associated with the base shaft.

### **F** — Follower interface mechanical rotational

Conserving port associated with the follower shaft.

## Parameters

### **Initial gear** — Gear state at the beginning of simulation `Neutral` (default) | `8` | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

Sets the initial engagement or disengagement of the clutches using the
clutch schedule. When the transmission is in neutral, there is no power flow
from the base shaft to the follower shaft.

## Libraries

Simscape / Driveline / Transmissions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Clutch schedule for an eight-speed transmission

The 8-Speed block consists of four planetary gear sets and five
clutches. The base shaft connects to the:

- Planet gear carrier of the second planetary gear
- Other gears through three clutches that determine the power flow
  path.

The follower shaft connects to the planet gear carrier of the first and
fourth planetary gears. The other two clutches serve as brakes, grounding various gears
of planetary sets two and three to the transmission housing.

This diagram shows an eight-speed transmission. The labels for the gear components are
superimposed on the input and output gears. The table lists the gear and clutch
components that are labeled in the diagram.

| Label | Component |
| --- | --- |
| P.G.1–P.G.4 | Planetary gears, 1–4 |
| R | Ring gear |
| C | Planet gear carrier |
| S | Sun gear |
| C–E | Forward clutches that control the power flow path |
| A–B | Forward, braking clutches |

### Drive Ratios, Clutch Schedule, and Power Flow

The drive ratio between the transmission input and output shafts follows from the
elementary gear ratios specified for the gear blocks. The elementary gear ratios are

gx=NRxNSx,

where:

- *N*Rx
  is the number of teeth in the planetary ring gear x, where x = 1, 2, 3,
  and 4.
- *N*Sx
  is the number of teeth in the planetary sun gear x, where x = 1, 2, 3,
  and 4.

The table shows the clutch schedule, drive-ratio expressions, drive-ratio default
values, and the power-flow diagrams for each gear of the 8-Speed
block. The schedule and gear ratios are based on the manufacturer data for the GM
8L90 eight-speed automatic transmission.

The letters in the clutch schedule columns denote the brakes and clutches. A value
of `1` denotes a locked state and a value of `0`
an unlocked state. The clutch schedule generates these signals based on the Gear
port input signal. The signals are scaled through a Gain block and used as actuation
inputs in the clutch blocks.

The power-flow diagrams show the power flow paths between input and output shafts
for each gear setting. Power flow is shown in orange. Connections to the
transmission housing (a mechanical ground) are shown in black.

| Gear | Clutch Schedule | | | | | Drive Ratio Equation | Default Ratio | Power Flow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** |  |  |  |
| 8 | **1** | 0 | 0 | **1** | **1** | g21+g2 | 0.65 |  |
| 7 | **1** | 0 | **1** | **1** | 0 | g2(1+g1)1+g2(1+g1) | 0.85 |  |
| 6 | 0 | 0 | **1** | **1** | **1** | 1 | 1 |  |
| 5 | 0 | **1** | **1** | **1** | 0 | 1+g3g4(1+g3+g4+g2g4(1+g1)) | 1.27 |  |
| 4 | 0 | **1** | 0 | **1** | **1** | 1+g2+g31+g2 | 1.69 |  |
| 3 | 0 | **1** | **1** | 0 | **1** | (1+g3)(1+g4)1+g3+g4 | 2.07 |  |
| 2 | **1** | **1** | 0 | 0 | **1** | g2(g4+1)(1+g2) | 2.96 |  |
| 1 | **1** | **1** | **1** | 0 | 0 | 1+g4 | 4.55 |  |
| R | **1** | **1** | 0 | **1** | 0 | −g2(g1g4−1)(g2+1) | -3.91 |  |
