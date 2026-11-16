---
type: simulink-block
title: 'Tx'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'tx'
documentation_source_path: 'ref/tx.html'
language: en
---

# Tx

## Ports

### Input

### **WaveIn** — Input signal scalar | vector

Input signal, specified as a waveform.

**Data Types:** `double`
### Output

### **WaveOut** — Modified output data scalar | vector

Modified output data that includes the effect of a lossy printed circuit board
transmission line model according to the method outlined in [1].

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

SerDes Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Transmitter block with default settings

Restore the transmitter component to default values set by the SerDes Designer
app. If you replaced a transmitter component by an AMI block, and now
wish to restore it to the original transmitter component exported by the app, you can use this
block.
