---
type: simulink-block
title: '4-Speed CR-CR'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '4speedcrcr'
documentation_source_path: 'ref/4speedcrcr.html'
language: en
---

# 4-Speed CR-CR

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

Specify -1 for reverse, 0 for neutral, and 1–4 for the forward
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
  summary: Gear state at the beginning of simulation Neutral (default) | 4 | 3 | 2 | 1 | Reverse
  group: ''
```

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

Clutch schedule for a four-speed carrier ring-carrier ring transmission

The 4-Speed CR-CR block consists of two planetary gear sets and five
disk friction clutches. The follower shaft connects to the planet gear carrier of the
output planetary gear and the ring gear of the input planetary gear. The clutches are
configured to implement four ratios, one reverse ratio, and neutral. The reverse clutch
and two of the clutches determine which gears the base shaft connects to. The other two
clutches act as brakes, grounding various gears of the planetary sets to the
transmission housing.

This diagram shows a four-speed carrier ring-carrier ring transmission. The labels for
the gear components are superimposed on the input and output gears. The table lists the
gear and clutch components that are labeled in the diagram.

| Label | Component |
| --- | --- |
| I.P.G. | Input planetary gear |
| O.P.G. | Output planetary gear |
| R | Ring gear |
| C | Planet gear carrier |
| S | Sun gear |
| R | Reverse clutch |
| A–B | Forward clutches that control the power flow path |
| C–D | Forward, braking clutches |

### Drive Ratios, Clutch Schedule, and Power Flow

The drive ratio between the transmission input and output shafts follows from the
elementary gear ratios specified for the gear blocks. The elementary gear ratios are

g1=NRINSI,

and

g2=NRONSO,

where:

- *N*RI is the number of teeth
  in the planetary ring gear on the input shaft side.
- *N*SI is the number of teeth
  in the planetary sun gear on the input shaft side.
- *N*RO is the number of teeth
  in the planetary ring gear on the output shaft side.
- *N*SO is the number of teeth
  in the planetary sun gear on the output shaft side.

The table shows the clutch schedule, drive-ratio expressions, drive-ratio default
values, and the power-flow diagrams for each gear of the 4-Speed
CR-CR block.

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
|  | **A** | **B** | **C** | **D** | **R** |  |  |  |
| 4 | 0 | **1** | **1** | 0 | 0 | g11+g1 | 0.67 |  |
| 3 | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 2 | **1** | 0 | **1** | 0 | 0 | g1+g2+11+g1 | 1.67 |  |
| 1 | **1** | 0 | 0 | **1** | 0 | g2+1 | 3 |  |
| R | 0 | 0 | 0 | **1** | **1** | −g1 | -2 |  |
