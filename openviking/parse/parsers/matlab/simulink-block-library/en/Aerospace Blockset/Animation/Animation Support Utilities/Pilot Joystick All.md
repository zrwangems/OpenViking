---
type: simulink-block
title: 'Pilot Joystick All'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Animation Support Utilities'
documentation_page: 'pilotjoystickall'
documentation_source_path: 'pilotjoystickall.html'
language: en
---

# Pilot Joystick All

## Ports
```yaml
ports:
- name: analog
  summary: Analog output range [-1, 1] | range [ 0, 1]
  direction: output
  data_types: double
- name: buttons
  summary: Button flagword with 32 button states
  direction: output
  data_types: uint32
- name: POV
  summary: Point-of-view hat
  direction: output
  data_types: double
```

### Output

### **analog** — Analog output range [-1, 1] | range [ 0, 1]

Analog output, returned according to:

| Array Number | Channel | Output Range | Joystick | Description |
| --- | --- | --- | --- | --- |
| `1` | X | [-1, 1] | [left, right] | Roll command |
| `2` | Y | [-1, 1] | [forward/down, back/up] | Pitch command |
| `3` | Z | [ 0, 1] | [min, max] | Throttle command |
| `4` | R | [-1, 1] | [left, right] | Yaw command |
| `5` | U | [ 0, 1] | [min, max] | U channel value |
| `6` | V | [ 0, 1] | [min, max] | V channel value |

**Data Types:** `double`

### **buttons** — Button flagword with 32 button states

Button output, returned as a flagword containing up to 32 button states on the buttons
channel. Bit 0 is button 1, Bit 1 is button 2, and so forth.

**Data Types:** `uint32`

### **POV** — Point-of-view hat

Point-of-view, returned as a hat value in degrees on the POV channel. Zero degrees is
straight ahead, 90 degrees is to the left, and so forth.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Joystick ID
  summary: Joystick ID Joystick1 (default) | Joystick2 | Joystick3 | Joystick4 | Joystick5 | Joystick6 | Joystick7 | Joystick8
    | Joystick9 | Joystick10 | Joystick11 | Joystick12 | Joystick13 | Joystick14 | Joystick15 | Joystick16 | None
  group: ''
  block_parameter: JoystickID
  type: character vector
  values: Joystick1 | Joystick2 | Joystick3 | Joystick4 | Joystick5 | Joystick6 | Joystick7 | Joystick8 | Joystick9 | Joystick10
    | Joystick11 | Joystick12 | Joystick13 | Joystick14 | Joystick15 | Joystick16 | None
  default: '''Joystick1'''
- name: Output configuration
  summary: Joystick output configuration AllOutputs (default) | FourAxis
  group: ''
  block_parameter: OutputConfiguration
  type: character vector
  values: FourAxis | AllOutputs
  default: '''FourAxis'''
- name: Sample time
  summary: Sample time 1/30 (default) | -1 | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''1/30'''
```

### **Joystick ID** — Joystick ID `Joystick1` (default) | `Joystick2` | `Joystick3` | `Joystick4` | `Joystick5` | `Joystick6` | `Joystick7` | `Joystick8` | `Joystick9` | `Joystick10` | `Joystick11` | `Joystick12` | `Joystick13` | `Joystick14` | `Joystick15` | `Joystick16` | `None`

Specify the joystick ID as

- `Joystick1`
- `Joystick2`
- `Joystick3`
- `Joystick4`
- `Joystick5`
- `Joystick6`
- `Joystick7`
- `Joystick8`
- `Joystick9`
- `Joystick10`
- `Joystick11`
- `Joystick12`
- `Joystick13`
- `Joystick14`
- `Joystick15`
- `Joystick16`
- `None`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `JoystickID` |
| **Type**: character vector |
| **Values**: `Joystick1` | `Joystick2` | `Joystick3` | `Joystick4` | `Joystick5` | `Joystick6` | `Joystick7` | `Joystick8` | `Joystick9` | `Joystick10` | `Joystick11` | `Joystick12` | `Joystick13` | `Joystick14` | `Joystick15` | `Joystick16` | `None` |
| **Default**: `'Joystick1'` |

### **Output configuration** — Joystick output configuration `AllOutputs` (default) | `FourAxis`

Joystick output configuration, specified as
`FourAxis` or
`AllOutputs`. For more information on the
`AllOutputs` configuration, see Pilot Joystick All.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputConfiguration` |
| **Type**: character vector |
| **Values**: `FourAxis` | `AllOutputs` |
| **Default**: `'FourAxis'` |

### **Sample time** — Sample time `1/30` (default) | `-1` | scalar

Specify the sample time (-1 for inherited), specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1/30'` |
## Libraries

Aerospace Blockset / Animation / Animation Support Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

### R2023b: Pilot Joystick All Block Update

The Pilot Joystick All block now supports up to 16
joysticks.

## Description

Provide joystick interface in All Outputs configuration on Windows platform

The Pilot Joystick All block provides a pilot joystick interface for a Windows® platform. Roll, pitch, yaw, and throttle are mapped to the joystick
*X*, *Y*, *R*, and
*Z* channels respectively.

The Pilot Joystick and Pilot Joystick All blocks are
alternative configurations of the same block.

- Pilot Joystick — Outputs four axes.
- Pilot Joystick All — Outputs all channels.

To generate deployable code, select one of the configuration parameter Microsoft®
Visual Studio® C++ `nmake` toolchains from **Code Generation** > **Toolchain**.
