---
type: simulink-block
title: 'Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Verification Utilities'
documentation_page: 'implies'
documentation_source_path: 'ref/implies.html'
language: en
---

# Implies

## Ports
```yaml
ports:
- name: Values
  summary: Input signal scalar | cell array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### Input

### **Values** — Input signal scalar | cell array

The Implies block accepts signals of all numeric data
types supported by the Simulink software. For a discussion on the data types supported by
the Simulink software, see Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Design Verifier / Verification Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2009a**

## Description

Specify condition that produces a certain response

The Implies block lets you specify a condition to produce a given
response; for example, when you press the brake pedal on a car, the cruise control
mechanism becomes disabled. If input A is true and input B is false, the output is
false; for all other pairs of inputs, the output is
true.

You can use the Implies block in
any model, not just when you run the Simulink®
Design Verifier™ software.
