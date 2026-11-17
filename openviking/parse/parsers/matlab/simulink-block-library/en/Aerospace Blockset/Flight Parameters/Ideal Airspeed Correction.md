---
type: simulink-block
title: 'Ideal Airspeed Correction'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'idealairspeedcorrection'
documentation_source_path: 'idealairspeedcorrection.html'
language: en
---

# Ideal Airspeed Correction

## Ports
```yaml
ports:
- name: TAS
  summary: True input airspeed scalar
  direction: input
  data_types: double
- name: EAS
  summary: Equivalent input airspeed scalar
  direction: input
  data_types: double
- name: CAS
  summary: Calibrated input airspeed scalar
  direction: input
  data_types: double
- name: a
  summary: Speed of sound scalar
  direction: input
  data_types: double
- name: P0
  summary: Static pressure scalar
  direction: input
  data_types: double
- name: EAS
  summary: Equivalent output airspeed scalar
  direction: output
  data_types: double
- name: CAS
  summary: Calibrated output airspeed scalar
  direction: output
  data_types: double
- name: TAS
  summary: True output airspeed scalar
  direction: output
  data_types: double
```

### Input

### **TAS** — True input airspeed scalar

True input airspeed, specified as a scalar, in the units specified by
the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`TAS`.

**Data Types:** `double`

### **EAS** — Equivalent input airspeed scalar

Equivalent input airspeed, specified as a scalar, in the units
specified by the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`EAS`.

**Data Types:** `double`

### **CAS** — Calibrated input airspeed scalar

Calibrated input airspeed, specified as a scalar, in the units
specified by the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`EAS`.

**Data Types:** `double`

### **a** — Speed of sound scalar

Speed of sound, specified as a scalar, in the units specified by the
**Units** parameter.

**Data Types:** `double`

### **P0** — Static pressure scalar

Static pressure, specified as a scalar, in the units specified by the
**Units** parameter.

**Data Types:** `double`
### Output

### **EAS** — Equivalent output airspeed scalar

Equivalent output airspeed, returned as a scalar, in the units
specified by the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`TAS` or `CAS`
and **Airspeed output** to
`EAS`.

**Data Types:** `double`

### **CAS** — Calibrated output airspeed scalar

Calibrated output airspeed, returned as a scalar, in the units
specified by the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`TAS` or `EAS`
and **Airspeed output** to
`CAS`.

**Data Types:** `double`

### **TAS** — True output airspeed scalar

True output airspeed, returned as a scalar, in the units specified by
the **Units** parameter.

#### Dependencies

To enable this port, set **Airspeed input** to
`CAS` or `EAS`
and **Airspeed output** to
`TAS`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Airspeed input
  summary: Airspeed input type TAS (default) | EAS | CAS
  group: ''
  block_parameter: vel_in
  type: character vector
  values: '''TAS'' | ''EAS'' | ''CAS'''
  default: '''TAS'''
- name: Airspeed output
  summary: Airspeed output type EAS (default) | CAS | TAS
  group: ''
  block_parameter: vel_out_tas, vel_out_cas, vel_out_eas, depending on the input velocity type, vel_in. For more information,
    see the airspeed output type table.
  type: character vector
  values: '''EAS'' | ''CAS''''TAS'''
  default: '''EAS'''
- name: Method
  summary: Method for computing conversion factor Table Lookup (default) | Equation
  group: ''
  block_parameter: method
  type: character vector
  values: '''Table Lookup'' | ''Equation'''
  default: '''Table Lookup'''
- name: Subsonic airspeeds only
  summary: Use with subsonic airspeed off (default) | on
  group: ''
  block_parameter: SubOnly
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
```

### **Units** — Units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as:

| Units | Airspeed Input | Speed of Sound | Air Pressure | Airspeed Output |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters per second | Meters per second | Pascal | Meters per second |
| `English (Velocity in ft/s)` | Feet per second | Feet per second | Pound force per square inch | Feet per second |
| `English (Velocity in kts)` | Knots | Knots | Pound force per square inch | Knots |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Airspeed input** — Airspeed input type `TAS` (default) | `EAS` | `CAS`

Airspeed input type, specified as:

|  |  |
| --- | --- |
| `TAS` | True airspeed |
| `EAS` | Equivalent airspeed |
| `CAS` | Calibrated airspeed |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `vel_in` |
| **Type**: character vector |
| **Values**: `'TAS'` | `'EAS'` | `'CAS'` |
| **Default**: `'TAS'` |

### **Airspeed output** — Airspeed output type `EAS` (default) | `CAS` | `TAS`

Airspeed output type, specified as:

| Airspeed Input | Airspeed Output |
| --- | --- |
| `TAS` | EAS (equivalent airspeed) |
| CAS (calibrated airspeed) |
| `EAS` | TAS (true airspeed) |
| CAS (calibrated airspeed) |
| `CAS` | TAS (true airspeed) |
| EAS (equivalent airspeed) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `vel_out_tas`, `vel_out_cas`, `vel_out_eas`, depending on the input velocity type, `vel_in`. For more information, see the airspeed output type table. |
| **Type**: character vector |
| **Values**: `'EAS'` | `'CAS'``'TAS'` |
| **Default**: `'EAS'` |

### **Method** — Method for computing conversion factor `Table Lookup` (default) | `Equation`

Method for computing the conversion factor, specified as:

|  |  |
| --- | --- |
| `Table Lookup` | (Default) Generate output airspeed by looking up or estimating table values based on block inputs.  If the **Subsonic airspeeds only** check box is selected, the Ideal Airspeed Correction block generates code that includes subsonic (Mach < 1) lookup table data.  If the **Subsonic airspeeds only** check box is cleared, the Ideal Airspeed Correction block generates code that includes all (Mach < 5) lookup table data. Beyond Mach 5, the block uses the `equation` method.  The `Table Lookup` method is not recommended for either of these instances:  - Speed of sound less than 200 m/s or greater   than 350 m/s. - Static pressure less than 1000 Pa or greater   than 106,500 Pa.  Using the `Table Lookup` method in these instances causes inaccuracies. |
| `Equation` | Compute output airspeed directly using block input values.  Calculations involving supersonic airspeeds (greater than Mach 1) require an iterative computation. If the function does not find a solution within 30 iterations, it displays an error message.  The block does not include lookup table data in generated code. |

The Ideal Airspeed Correction block automatically uses the
`Equation` method for any of these
instances:

- Conversion with **Airspeed input** set to
  `TAS` and **Airspeed
  output** set to `EAS`.
- Conversion with **Airspeed input** set to
  `EAS` and **Airspeed
  output** set to `TAS`.
- Conversion when block input airspeed is greater than five times
  the speed of sound at sea level (approximately 1700 m/s).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `method` |
| **Type**: character vector |
| **Values**: `'Table Lookup'` | `'Equation'` |
| **Default**: `'Table Lookup'` |

### **Subsonic airspeeds only** — Use with subsonic airspeed `off` (default) | `on`

Select this check box to use this block only with subsonic airspeed
(airspeeds less than Mach 1) applications. Selecting this check box may
improve performance.

The block generates code as follows:

- If this check box is selected, the Ideal Airspeed
  Correction block generates code that includes subsonic
  (Mach < 1) lookup table data if **Method** is
  set to `Table Lookup`.

  Selecting this check box displays the **Action for
  out-of-range input** parameter.
- If this check box is cleared, the Ideal Airspeed
  Correction block generates code that includes all (Mach
  < 5) lookup table data if **Method** is set to
  `Table Lookup`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SubOnly` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Action for out-of-range input** — Out-of-range block behavior None (default) | `Warning` | `Error`

Out-of-range block behavior, where airspeed is greater than Mach 1,
specified as follows.

| Value | Description |
| --- | --- |
| `None` | Does not display warning or error. |
| `Warning` | Displays warning and indicates that the airspeed is greater than Mach 1. |
| `Error` | Displays error and indicates that the airspeed is greater than Mach 1. |

#### Dependencies

This parameter is enabled only if the **Subsonic airspeeds
only** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |
## Libraries

Aerospace Blockset / Flight Parameters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate equivalent airspeed (EAS), calibrated airspeed (CAS), or true airspeed (TAS) from each other

The Ideal Airspeed Correction block calculates one of these airspeeds from one of the other two airspeeds:

- Equivalent airspeed (EAS)
- Calibrated airspeed (CAS)
- True airspeed (TAS)
