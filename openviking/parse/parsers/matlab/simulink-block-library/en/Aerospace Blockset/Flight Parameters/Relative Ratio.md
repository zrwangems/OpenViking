---
type: simulink-block
title: 'Relative Ratio'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'relativeratio'
documentation_source_path: 'relativeratio.html'
language: en
---

# Relative Ratio

## Ports
```yaml
ports:
- name: Mach
  summary: Mach number scalar
  direction: input
  data_types: double
- name: γ
  summary: Ratio scalar
  direction: input
  data_types: double
- name: To
  summary: Static temperature scalar
  direction: input
  data_types: double
- name: Po
  summary: Static pressure scalar
  direction: input
  data_types: double
- name: ρo
  summary: Static density scalar
  direction: input
  data_types: double
- name: θ
  summary: Relative temperature ratio scalar
  direction: output
  data_types: double
- name: sqrt(θ)
  summary: Square root of relative temperature ratio scalar
  direction: output
  data_types: double
- name: δ
  summary: Relative pressure ratio scalar
  direction: output
  data_types: double
- name: σ
  summary: Relative density ratio scalar
  direction: output
  data_types: double
```

### Input

### **Mach** — Mach number scalar

Mach number, specified as a scalar.

**Data Types:** `double`

### **γ** — Ratio scalar

Ratio between the specific heat at constant pressure
(*Cp*) and the specific
heat at constant volume (*Cv*),
specified as a scalar. For example, (*γ* =
*Cp*/*Cv*).

**Data Types:** `double`

### **To** — Static temperature scalar

Static temperature, specified as a scalar.

**Data Types:** `double`

### **Po** — Static pressure scalar

Static pressure, specified as a scalar.

**Data Types:** `double`

### **ρo** — Static density scalar

Static density, specified as a scalar.

**Data Types:** `double`
### Output

### **θ** — Relative temperature ratio scalar

Relative temperature ratio (*θ*), returned as a
scalar.

#### Dependencies

To enable this port, select **Theta**.

**Data Types:** `double`

### **sqrt(θ)** — Square root of relative temperature ratio scalar

Square root of the relative temperature ratio ( θ), returned as a scalar.

#### Dependencies

To enable this port, select **Square root of theta**.

**Data Types:** `double`

### **δ** — Relative pressure ratio scalar

Relative pressure ratio, (*δ*), returned as a scalar.

#### Dependencies

To enable this port, select **Delta**.

**Data Types:** `double`

### **σ** — Relative density ratio scalar

Relative density ratio, (*σ*), returned as a scalar.

#### Dependencies

To enable this port, select **Sigma**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Units Metric (MKS) (default) | English
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Theta
  summary: Relative temperature ratio on (default) | off
  group: ''
  block_parameter: theta
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Square root of theta
  summary: Square root of relative temperature ratio on (default) | off
  group: ''
  block_parameter: sq_theta
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Delta
  summary: Relative pressure ratio on (default) | off
  group: ''
  block_parameter: delta
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Sigma
  summary: Relative density ratio on (default) | off
  group: ''
  block_parameter: sigma
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Units** — Units `Metric (MKS)` (default) | `English`

Input units, specified as:

| Units | Tstatic | Pstatic | rho\_static |
| --- | --- | --- | --- |
| `Metric (MKS)` | Kelvin | Pascal | Kilograms per cubic meter |
| `English` | Degrees Rankine | Pound force per square inch | Slug per cubic foot |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Theta** — Relative temperature ratio `on` (default) | `off`

When selected, the block calculates the relative temperature ratio
(*θ*) and static temperature is a required
input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `theta` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Square root of theta** — Square root of relative temperature ratio `on` (default) | `off`

When selected, the block calculates the square root of relative
temperature ratio ( θ) and static temperature is a required input.

#### Dependencies

Selecting this check box enables the sqrt(θ) output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sq_theta` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Delta** — Relative pressure ratio `on` (default) | `off`

When selected, the block calculates the relative pressure ratio
(*δ*) and static pressure is a required input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `delta` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Sigma** — Relative density ratio `on` (default) | `off`

When selected, the block the relative density ratio (*σ*)
and static density is a required input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sigma` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |
## Libraries

Aerospace Blockset / Flight Parameters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate relative atmospheric ratios

The Relative Ratio block computes the relative atmospheric
ratios, including the relative temperature ratio (*θ*), θ, relative pressure ratio (*δ*), and relative density
ratio (*σ*).

*θ* represents the ratio of the air stream temperature at a chosen
reference station relative to sea level standard atmospheric conditions:

θ=TT0.

*δ* represents the ratio of the air stream pressure at a chosen reference
station relative to sea level standard atmospheric conditions:

δ=PP0.

*σ* represents the ratio of the air stream density at a chosen reference
station relative to sea level standard atmospheric conditions:

σ=ρρ0.

The Relative Ratio block icon displays the input units selected from the **Units** parameter.
