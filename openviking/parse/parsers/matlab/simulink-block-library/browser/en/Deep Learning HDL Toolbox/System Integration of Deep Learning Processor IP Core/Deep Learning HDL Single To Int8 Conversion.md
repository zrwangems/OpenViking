---
type: simulink-block
title: 'Deep Learning HDL Single To Int8 Conversion'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlsingletoint8conversion'
documentation_source_path: 'ref/deeplearninghdlsingletoint8conversion.html'
language: en
---

# Deep Learning HDL Single To Int8 Conversion

## Ports

### Input

### **Input Data** — Single-precision input data scalar | vector

Single-precision input data specified as a scalar or vector.

**Data Types:** `single`

### **Exponent** — Conversion exponent scalar

Conversion exponent, specified as a scalar. You must connect this input port to a
Constant block. The value of the Constant block must
be the output of the `getSingleToInt8ConversionExponent` method.

**Data Types:** `int8`

### **ValidIn** — Valid signal scalar

Valid signal, specified as a Boolean scalar.

**Data Types:** `Boolean`
### Output

### **Out** — 8-bit signed integer data scalar | vector

8-bit integer data returned as an `int8` data type scalar or
vector.

**Data Types:** `int8`

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

Convert single-precision data to 8-bit signed integer data

The Deep Learning HDL Single To Int8 Conversion block converts
single-precision data to 8-bit signed integer data. To add the block, at the MATLAB® command line,
enter:

```
open_system("dlhdlutils")
```
