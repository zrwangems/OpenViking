---
type: simulink-block
title: 'Deep Learning HDL Int8 To Single Conversion'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlint8tosingleconversion'
documentation_source_path: 'ref/deeplearninghdlint8tosingleconversion.html'
language: en
---

# Deep Learning HDL Int8 To Single Conversion

## Ports

### Input

### **Input Data** — 8-bit signed integer data scalar | vector

8-bit signed integer data specified as an `int8` data type scalar
or vector.

**Data Types:** `int8`

### **Exponent** — Conversion exponent scalar

Conversion exponent, specified as a scalar. You must connect this input port to a
Constant block. The value of the Constant block must
be the output of the `getInt8ToSingleConversionExponent` method.

**Data Types:** `int8`

### **ValidIn** — Valid signal scalar

Valid signal, specified as a Boolean scalar.

**Data Types:** `Boolean`
### Output

### **Out** — Single-precision data scalar | vector

Single-precision data returned as a `single` data type scalar or
vector.

**Data Types:** `single`

### **ValidOut** — Valid signal scalar

Valid signal, returned as a Boolean scalar.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Convert 8-bit signed integer data to single-precision data

The Deep Learning HDL Int8 To Single Conversion block converts 8-bit signed
integer data to single-precision data. To add the block, at the MATLAB® command line,
enter:

```
open_system("dlhdlutils")
```
