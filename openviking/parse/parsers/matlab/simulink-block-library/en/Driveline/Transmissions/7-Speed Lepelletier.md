---
type: simulink-block
title: '7-Speed Lepelletier'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '7speedlepelletier'
documentation_source_path: 'ref/7speedlepelletier.html'
language: en
---

# 7-Speed Lepelletier

## Ports
```yaml
ports:
- name: Gear
  summary: Numerical input for the gear scalar
  direction: input
  data_types: single | double
- name: B
  summary: Base interface mechanical rotational
  direction: conserving
- name: F
  summary: Follower interface mechanical rotational
  direction: conserving
```

### Input

### **Gear** — Numerical input for the gear scalar

Specify -1 for reverse, 0 for neutral, and 1–7 for the forward
gears.

**Data Types:** `single` | `double`
### Conserving

### **B** — Base interface mechanical rotational

Conserving port associated with the base shaft.

### **F** — Follower interface mechanical rotational

Conserving port associated with the follower shaft.
## Parameters
```yaml
parameters:
- name: Initial gear
  summary: Gear state at the beginning of simulation Neutral (default) | 7 | 6 | 5 | 4 | 3 | 2 | 1 | Reverse
  group: ''
```

### **Initial gear** — Gear state at the beginning of simulation `Neutral` (default) | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

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

Clutch schedule for a seven-speed Lepelletier transmission

The 7–Speed Lepelletier block consists of one planetary gear set, one
Ravigneaux gear set, and six disk friction clutches. The transmission base shaft
connects to the ring gear of the planetary gear set. The follower shaft connects to the
ring gear of the Ravigneaux gear set. Three of the clutches control the power-flow paths
between the planetary and Ravigneaux gear sets. The other three clutches serve as
brakes, grounding various gears of the Ravigneaux set to the transmission
housing.

This diagram shows a seven-speed Lepelletier transmission. The labels for the gear
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
| A–C | Forward clutches that control the power-flow path |
| D–F | Forward, braking clutches |

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
- *N*RSS is the number of teeth
  in the Ravigneaux small sun gear.

The table shows the clutch schedule, drive-ratio expressions, drive-ratio default
values, and the power-flow diagrams for each gear of the 7-Speed
Lepelletier block.

The letters in the clutch schedule columns denote the brakes and clutches. A value
of `1` denotes a locked state and a value of `0`
an unlocked state. The clutch schedule generates these signals based on the Gear
port input signal. The signals are scaled through a Gain block and used as actuation
inputs in the clutch blocks.

The power-flow diagrams show the power-flow paths between input and output shafts
for each gear setting. Power flow is shown in orange. Connections to the
transmission housing (a mechanical ground) are shown in black.

| Gear | Clutch Schedule | | | | | | Drive Ratio Equation | Default Ratio | Power Flow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** | **F** |  |  |  |
| 7 | 0 | **1** | 0 | 0 | **1** | **1** | g21+g2 | 0.70 |  |
| 6 | **1** | **1** | 0 | 0 | 0 | **1** | g2(1+g1)g2(1+g1)+1 | 0.86 |  |
| 5 | **1** | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 4 | 0 | **1** | **1** | 0 | 0 | **1** | g3(1+g1)g3(1+g1)−1 | 1.17 |  |
| 3 | **1** | 0 | **1** | 0 | 0 | **1** | 1+g1g1 | 1.63 |  |
| 2 | 0 | 0 | **1** | 0 | **1** | **1** | (1+g1)(g3+g2)g1(1+g2) | 2.43 |  |
| 1 | 0 | 0 | **1** | **1** | 0 | **1** | g3(1+g1)g1 | 4.31 |  |
| R | **1** | 0 | 0 | **1** | 0 | **1** | −g2(1+g1)g1 | -3.82 |  |
