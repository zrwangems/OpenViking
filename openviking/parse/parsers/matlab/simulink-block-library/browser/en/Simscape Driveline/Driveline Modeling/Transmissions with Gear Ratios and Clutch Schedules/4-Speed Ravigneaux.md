---
type: simulink-block
title: '4-Speed Ravigneaux'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Transmissions with Gear Ratios and Clutch Schedules'
documentation_page: '4speedravigneaux'
documentation_source_path: 'ref/4speedravigneaux.html'
language: en
---

# 4-Speed Ravigneaux

## Ports

### Input

### **Gear** — Numerical input for the gear scalar

Specify -1 for reverse, 0 for neutral, and 1–4 for the forward
gears.

**Data Types:** `single` | `double`
### Conserving

### **B** — Base interface mechanical rotational

Conserving port associated with the base shaft.

### **F** — Follower interface mechanical rotational

Conserving port associated with the follower shaft.

## Parameters

### **Initial gear** — Gear state at the beginning of simulation `Neutral` (default) | `4` | `3` | `2` | `1` | `Reverse`

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

Clutch schedule for a four-speed Ravigneaux transmission

The 4-Speed Ravigneaux block consists of one Ravigneaux gear set and
five clutches. The follower shaft connects to the ring gear of the Ravigneaux set. Three
of the clutches determine the gears that the base shaft connects to for power transfer.
The other two clutches serve as brakes, grounding various gears of the Ravigneaux set to
the transmission housing.

This diagram shows a four-speed Ravigneaux gear transmission. The labels for the gear
components are superimposed on the input and output gears. The table lists the gear and
clutch components that are labeled in the diagram.

| Label | Component |
| --- | --- |
| R.G. | Ravigneaux gear |
| R | Ring gear |
| C | Planet gear carrier |
| SL | Large sun gear |
| SS | Small sun gear |
| A–C | Forward clutches that control the power flow path |
| D–E | Forward, braking clutches |

### Drive Ratios, Clutch Schedule, and Power Flow

The drive ratio between the transmission input and output shafts follows from the
elementary gear ratios specified for the gear blocks. The elementary gear ratios are

g1=NRNSL,

and

g2=NRNSS,

where:

- *N*R is the number of teeth in
  the Ravigneaux ring gear.
- *N*SL is the number of teeth
  in the Ravigneaux large sun gear.
- *N*SS is the number of teeth
  in the Ravigneaux small sun gear.

The table shows the clutch schedule, drive-ratio expressions, drive-ratio default
values, and the power-flow diagrams for each gear of the 4-Speed
Ravigneaux block.

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
| 4 | **1** | 0 | 0 | 0 | **1** | g11+g1 | 0.67 |  |
| 3 | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 2 | 0 | **1** | 0 | 0 | **1** | g1+g21+g1 | 1.67 |  |
| 1 | 0 | **1** | 0 | **1** | 0 | g2 | 3 |  |
| E | 0 | 0 | **1** | **1** | 0 | −g1 | -2 |  |
