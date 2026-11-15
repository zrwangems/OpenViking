---
type: simulink-block
title: 'Extender'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'extender'
documentation_source_path: 'ref/extender.html'
language: en
---

# Extender

## Ports

### Input

### **Port\_1** — Input signal specified as boolean boolean

The inputs of the Extender block are of boolean
type.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Output signal returns as boolean boolean

The outputs of the Extender block are of boolean
type.

**Data Types:** `Boolean`

## Parameters

### **External reset** — specify whether the block can be reset off (default) | on

Specify whether an external Boolean reset signal can reset the block
extension. The reset signal also resets the infinite extension. The infinite
extension with an external reset is an indefinite extension until the
external reset signal becomes `true`.

### **Extension Period** — specify a fixed number of time steps for extension `Finite` (default) | `Infinite`

Select `Finite` (the default) to specify a fixed
number of time steps for extension. Select
`Infinite` to specify indefinite
extension.

### **Time steps for extension** — specify the number of time steps for extending the true duration 3 (default) | boolean

For finite extension, specify the number of time steps for extending the
true duration (minimum is `1`).

## Libraries

Simulink Design Verifier / Temporal Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Extend true duration of input

The Extender block extends the true duration of the input signal by a
fixed number of steps (finite extension mode) or indefinitely.

*True duration* of a signal is consecutive time steps during
which a signal is `true`.
