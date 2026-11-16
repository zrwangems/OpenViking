---
type: simulink-block
title: 'Pilot Joystick'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Animation Support Utilities'
documentation_page: 'pilotjoystick'
documentation_source_path: 'pilotjoystick.html'
language: en
---

# Pilot Joystick

## Ports

### Output

### **roll** — Roll range [-1, 1]

Roll command, specified in the range [-1, 1], that corresponds to the joystick left and
right directions.

#### Dependencies

To enable this port, set **Output configuration** to
`FourAxis`.

**Data Types:** `double`

### **pitch** — Pitch range [-1, 1]

Pitch command, specified in the range [-1, 1], that corresponds to the joystick forward
or down and back and up directions.

#### Dependencies

This output port is enabled when the **Output
configuration** parameter is set to
`FourAxis`.

**Data Types:** `double`

### **yaw** — Yaw range [-1, 1]

Yaw command, specified in the range [-1, 1], that corresponds to the joystick twist left
and twist right directions.

#### Dependencies

To enable this port, set **Output configuration** to
`FourAxis`.

**Data Types:** `double`

### **throttle** — Throttle range [ 0, 1]

Throttle command, specified in the range [0, 1], that corresponds to the joystick min
and max position.

#### Dependencies

To enable this port, set **Output configuration** to
`FourAxis`.

**Data Types:** `double`

## Parameters

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

### **Output configuration** — Joystick output configuration `FourAxis` (default) | `AllOutputs`

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

**Introduced before R2006a**

### R2023b: Pilot Joystick Block Update

The Pilot Joystick  block now supports up to 16 joysticks.

## Description

Provide joystick interface on Windows platform

The Pilot Joystick block provides a pilot joystick interface for a Windows® platform. Roll, pitch, yaw, and throttle are mapped to the joystick
*X*, *Y*, *R*, and
*Z* channels respectively.

The Pilot Joystick and Pilot Joystick All blocks are
alternative configurations of the same block.

- Pilot Joystick — Outputs four axes.
- Pilot Joystick All — Outputs all channels.

To generate deployable code, select one of the configuration parameter Microsoft®
Visual Studio® C++ `nmake` toolchains from **Code Generation** > **Toolchain**.
