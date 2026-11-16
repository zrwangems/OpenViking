---
type: simulink-block
title: '10-Speed'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '10speed'
documentation_source_path: 'ref/10speed.html'
language: en
---

# 10-Speed

## Ports

### Input

### **Gear** — Numerical input for the gear scalar

Specify -1 for reverse, 0 for neutral, and 1–10 for the forward
gears.

**Data Types:** `single` | `double`
### Conserving

### **B** — Base interface mechanical rotational

Conserving port associated with the base shaft.

### **F** — Follower interface mechanical rotational

Conserving port associated with the follower shaft.

## Parameters

### **Initial gear** — Gear state at the beginning of simulation `Neutral` (default) | `10` | `9` | `8` | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

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

**Introduced in R2018a**

## Description

Clutch schedule for a 10-speed transmission

The 10-Speed transmission block consists of four
planetary gear sets and six clutches. The follower shaft connects to the planet gear
carrier of the fourth planetary gear. Four of the clutches determine the power flow path
for the base shaft. The other two clutches serve as brakes, grounding various gears of
the planetary sets to the transmission housing.

This diagram shows a 10-speed transmission. The labels for the gear components are
superimposed on the input and output gears. The table lists the gear and clutch
components that are labeled in the diagram. Power elements are shown in orange. Braking
elements are shown in black.

| Label | Component |
| --- | --- |
| PG1–PG4 | Planetary gears, 1–4 |
| R*x* | Ring gear of planetary gear *x* |
| C*x* | Planet gear carrier of planetary gear *x* |
| S*x* | Sun gear of planetary gear *x* |
| C, D, E, F | Clutches that control the power flow path |
| A, B | Braking clutches |

### Drive Ratios, Clutch Schedule, and Power Flow

The drive ratio between the transmission input and output shafts follows from the
elementary gear ratios specified for the gear blocks. The elementary gear ratios are

gx=NRxNSx,

where:

- *N*Rx
  is the number of teeth in the planetary ring gear *x*,
  where *x* = 1, 2, 3, and 4.
- *N*Sx
  is the number of teeth in the planetary sun gear *x*,
  where *x* = 1, 2, 3, and 4

The table shows the clutch schedule, drive-ratio expressions, drive-ratio default
values, and the power-flow diagrams for each gear of the
10-Speed block. The schedule and gear ratios are
based on the manufacturer data for a 10R80 10-speed automatic transmission.

The letters in the clutch schedule columns denote the brakes and clutches. A value
of `1` denotes a locked state and a value of `0`
an unlocked state. The clutch schedule generates these signals based on the Gear
port input signal. The signals are scaled through a Gain block and used as actuation
inputs in the clutch blocks.

The power-flow diagrams show the power flow paths between input and output shafts
for each gear setting. Power flow is shown in orange. Connections to the
transmission housing (a mechanical ground) are shown in black.

| Gear | Clutch Schedule | | | | | | Drive Ratio Equation | Default Ratio | Power Flow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** | **F** |  |  |  |
| 10 | 0 | **1** | **1** | **1** | 0 | **1** | g21+g2 | 0.64 |  |
| 9 | 0 | **1** | **1** | 0 | **1** | **1** | g2(1+g4)(g2(1+g4))+g4 | 0.69 |  |
| 8 | 0 | **1** | 0 | **1** | **1** | **1** | g2(1+g3)(1+g4)(g2(1+g3)(1+g4))+g4 | 0.85 |  |
| 7 | 0 | 0 | **1** | **1** | **1** | **1** | 1 | 1 |  |
| 6 | **1** | 0 | 0 | **1** | **1** | **1** | (1+g4)(1+g1+g2(1+g3))(1+g4)(1+g2(1+g3))+g1 | 1.27 |  |
| 5 | **1** | 0 | **1** | 0 | **1** | **1** | (1+g1+g2)(1+g4)(1+g2)(1+g4)+g1 | 1.52 |  |
| 4 | **1** | 0 | **1** | **1** | 0 | **1** | 1+g1+g21+g2 | 1.76 |  |
| 3 | **1** | 0 | **1** | **1** | **1** | 0 | (1+g1)(1+g4)1+g1+g4 | 2.14 |  |
| 2 | **1** | **1** | **1** | **1** | 0 | 0 | g2(1+g4)1+g2 | 2.99 |  |
| 1 | **1** | **1** | 0 | **1** | **1** | 0 | 1+g4 | 4.70 |  |
| R | **1** | **1** | 0 | **1** | 0 | **1** | −g2g3(1+g4)(1+g2) | -4.79 |  |
