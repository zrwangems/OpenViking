---
type: simulink-block
title: '6-Speed Lepelletier'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '6speedlepelletier'
documentation_source_path: 'ref/6speedlepelletier.html'
language: en
---

# 6-Speed Lepelletier

## Ports

### Input

### **Gear** — Numerical input for the gear scalar

Specify -1 for reverse, 0 for neutral, and 1–6 for the forward
gears.

**Data Types:** `single` | `double`
### Conserving

### **B** — Base interface mechanical rotational

Conserving port associated with the base shaft.

### **F** — Follower interface mechanical rotational

Conserving port associated with the follower shaft.

## Parameters

### **Initial gear** — Gear state at the beginning of simulation `Neutral` (default) | `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

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

Clutch schedule for a six-speed Lepelletier transmission

The 6-Speed Lepelletier consists of one planetary gear set, one
Ravigneaux gear set, and five disk friction clutches. The transmission base shaft
connects to the ring gear of the planetary gear set. The follower shaft connects to the
ring gear of the Ravigneaux gear set. Three of the clutches control the power flow paths
between the planetary and Ravigneaux gear sets. The other two clutches serve as brakes,
grounding various gears of the Ravigneaux set to the transmission housing.

This diagram shows a six-speed Lepelletier transmission. The labels for the gear
components are superimposed on the input and output gears. The table lists the gear and
clutch components that are labeled in the diagram.

| Label | Component |
| --- | --- |
| P.G. | Planetary gear |
| R.G. | Ravigneaux gear |
| R | Ring gear |
| C | Planet gear carrier |
| S | Sun gear |
| SL | Large sun gear |
| SS | Small sun gear |
| A–C | Forward clutches that control the power flow path |
| D–E | Forward, braking clutches |

### Drive Ratios, Clutch Schedule, and Power Flow

The drive ratio between the transmission input and output shafts follows from the
elementary gear ratios specified for the gear blocks. The elementary gear ratios are

g1=NPRNPS,

g2=NRRNRSL,

and

g3=NRRNRSS,

where:

- *N*PR is the number of teeth
  in the planetary ring gear.
- *N*PS is the number of teeth
  in the planetary sun gear.
- *N*RR is the number of teeth
  in the Ravigneaux ring gear.
- *N*RSL is the number of teeth
  in the Ravigneaux large sun gear.
- *N*RRS is the number of teeth
  in the Ravigneaux small sun gear.

The table shows the clutch schedule, drive-ratio expressions,
drive-ratio default values, and the power-flow diagrams for each gear of the
6-Speed Lepelletier block.

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
| 6 | 0 | **1** | 0 | 0 | **1** | g21+g2 | 0.69 |  |
| 5 | **1** | **1** | 0 | 0 | 0 | g2g2+1/(1+g1) | 0.87 |  |
| 4 | 0 | **1** | **1** | 0 | 0 | g3(1+g1)g3(1+g1)−1 | 1.14 |  |
| 3 | **1** | 0 | **1** | 0 | 0 | 1+g1g1 | 1.50 |  |
| 2 | 0 | 0 | **1** | 0 | **1** | (1+g1)(g3+g2)g1(1+g2) | 2.31 |  |
| 1 | 0 | 0 | **1** | **1** | 0 | g3(1+g1)g1 | 4.12 |  |
| R | **1** | 0 | 0 | **1** | 0 | −g2(1+g1)g1 | -3.36 |  |
