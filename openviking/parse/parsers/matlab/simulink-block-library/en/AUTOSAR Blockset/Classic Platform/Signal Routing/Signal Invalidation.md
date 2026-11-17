---
type: simulink-block
title: 'Signal Invalidation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Signal Routing'
documentation_page: 'signalinvalidation'
documentation_source_path: 'ref/signalinvalidation.html'
language: en
---

# Signal Invalidation

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data value numeric value
  direction: input
  data_types: single | double | base integer | Boolean | fixed point | enumerated | bus
- name: Port_2
  summary: Invalidation control flag true | false
  direction: input
  data_types: Boolean
- name: Port_1
  summary: Output data value numeric value
  direction: output
  data_types: single | double | base integer | Boolean | fixed point | enumerated | bus
```

### Input

### **Port\_1** — Input data value numeric value

Input data value to be relayed if valid.

**Example:**  4

**Data Types:** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — Invalidation control flag `true` | `false`

The invalidation control flag determines whether the input data value is valid and
can be relayed (`false`), or is invalid and must be handled based on
an invalidation policy (`true`).

**Example:**
`false`

**Data Types:** `Boolean`
### Output

### **Port\_1** — Output data value numeric value

Output data value produced by the combination of the input data value and the
invalidation control flag.

**Data Types:** `single` | `double` | `base integer` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Signal invalidation policy
  summary: Invalidation policy Keep (default) | Replace | DontInvalidate
  group: ''
  block_parameter: InvalidationPolicy
  type: character vector
  values: '''Keep'' | ''Replace'' | ''DontInvalidate'''
  default: '''Keep'''
- name: Initial value
  summary: Data element initial value 0 (default) | double
  group: ''
  block_parameter: InitialOutput
  type: character vector
  values: real finite values
  default: '''0'''
```

### **Signal invalidation policy** — Invalidation policy `Keep` (default) | `Replace` | `DontInvalidate`

Specify an AUTOSAR data element invalidation policy, which determines how an invalid
data element is handled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InvalidationPolicy` |
| **Type:** character vector |
| **Values:** `'Keep' | 'Replace' | 'DontInvalidate'` |
| **Default:** `'Keep'` |

### **Initial value** — Data element initial value 0 (default) | double

Specify a data element initial value. If the input data value is flagged as invalid,
and if the **Signal invalidation policy** is
`Replace`, the software replaces the input data value with
the specified initial value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector |
| **Values:** real finite values |
| **Default:** `'0'` |
## Libraries

AUTOSAR Blockset / Classic Platform / Signal Routing

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Control AUTOSAR root outport data element invalidation

Relay the first input, a data value, to the output, based on the value of the second
input, an invalidation control flag.

If the input data value is valid (invalidation control flag is `false`),
the software relays the input data value to the output.

If the input data value is invalid (invalidation control flag is `true`),
the resulting action is determined by the value of the block parameter **Signal
invalidation policy**:

- `Keep` - Replace the input data value with the last valid
  signal value.
- `Replace` - Replace the input data value with the value of
  the block parameter **Initial value**.
- `DontInvalidate` - Do not replace the input data
  value.

This block must be connected directly to a root outport block. It cannot be used within a
reusable subsystem.
