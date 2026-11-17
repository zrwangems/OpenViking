---
type: simulink-block
title: 'DCT Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Transmission Controllers'
documentation_page: 'dctcontroller'
documentation_source_path: 'ref/dctcontroller.html'
language: en
---

# DCT Controller

## Ports
```yaml
ports:
- name: GearReq
  summary: Gear number to engage scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: NomGear
  summary: Nominal gear for shifting scalar
  direction: output
- name: CltchACmd
  summary: Command for odd-numbered gears scalar
  direction: output
- name: CltchBCmd
  summary: Command for even-numbered gears scalar
  direction: output
```

### Inputs

### **GearReq** — Gear number to engage `scalar`

Gear number request, *Greq*.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | Description | Variable |
| --- | --- | --- |
| `GearReq` | Gear number request | *Greq* |
| `GearEngd` | Nominal gear commanded by the controller | *Go* |
| `GearEffct` | Effective gear | NA |
| `CltchACmd` | Clutch pressure command for odd-numbered gears, between `0` and `1` | NA |
| `CltchBCmd` | Clutch pressure command for even-numbered gears, between `0` and `1` | NA |

### **NomGear** — Nominal gear for shifting `scalar`

Nominal gear for shifting. The Dual Clutch Transmission block
uses this signal for the smooth application of inertial, efficiency,
gear ratio, and damping parameters.

### **CltchACmd** — Command for odd-numbered gears `scalar`

Clutch pressure command for odd-numbered gears, between
`0` and `1`.

### **CltchBCmd** — Command for even-numbered gears `scalar`

Clutch pressure command for even-numbered gears, between
`0` and `1`.
## Parameters
```yaml
parameters:
- name: Initial gear, G_o
  summary: Engaged gear 0 (default) | scalar
  group: ''
  block_parameter: G_o
  values: 0 (default) | scalar
- name: Clutch actuation time, tc
  summary: Time .1 (default) | scalar
  group: ''
  block_parameter: tc
  values: .1 (default) | scalar
- name: Synchronizer time, ts
  summary: Time .01 (default) | scalar
  group: ''
  block_parameter: ts
  values: .01 (default) | scalar
- name: Sample period, dt
  summary: Time -1 (default) | scalar
  group: ''
  block_parameter: dt
  values: -1 (default) | scalar
- name: Start simulation with clutch locked
  summary: Select to initially lock clutch off (default) | on
  group: ''
  block_parameter: ClutchLocked
  values: off (default) | on
- name: Start simulation with synchronizer locked
  summary: Select to initially lock synchronizer off (default) | on
  group: ''
  block_parameter: SynchLocked
  values: off (default) | on
```

### **Initial gear, G\_o** — Engaged gear `0` (default) | `scalar`

Initial gear to engage,
*Go*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `G_o` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch actuation time, tc** — Time `.1` (default) | `scalar`

Time required to engage and disengage the clutch during shift events,
*tc*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tc` |
| **Values:** | `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Synchronizer time, ts** — Time `.01` (default) | `scalar`

Time required for gear selection and synchronization,
*ts*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ts` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Sample period, dt** — Time `-1` (default) | `scalar`

Sample period, *dt*, in s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `dt` |
| **Values:** | `-1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Start simulation with clutch locked** — Select to initially lock clutch `off` (default) | `on`

Selecting this parameter initially locks the clutch.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ClutchLocked` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Start simulation with synchronizer locked** — Select to initially lock synchronizer `off` (default) | `on`

Selecting this parameter initially locks the synchronizer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SynchLocked` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |
## Libraries

Powertrain Blockset / Transmission / Transmission Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Dual clutch transmission controller

The DCT Controller block implements a dual clutch
transmission (DCT) controller. You can specify the clutch open, close,
and synchronization timing parameters. The block determines the clutch
commands using integrator-based timers and latching logic that is
based on the specified timing parameters and gear request.
