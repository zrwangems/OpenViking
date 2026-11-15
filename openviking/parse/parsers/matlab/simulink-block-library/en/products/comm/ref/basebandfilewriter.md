---
type: simulink-block
title: 'Baseband File Writer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Sources and Sinks / File IO'
documentation_page: 'basebandfilewriter'
documentation_source_path: 'ref/basebandfilewriter.html'
language: en
---

# Baseband File Writer

## Ports

### Input

### **Port\_1** — Baseband signal scalar | vector | matrix

This port accepts a baseband signal to be saved under the filename
specified by the **Baseband file name** parameter. The
saved signal is always complex.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Baseband file name** — Name of baseband file to write `untitled.bb` (default) | character vector

Name of the baseband file to write, specified as a character
vector.

To specify the location where the file is saved, click
**Browse**.

### **Center frequency (Hz)** — Center frequency of baseband signal `1e8` (default) | nonnegative scalar

Center frequency of the baseband signal in Hz, specified as a positive
scalar or row vector. When this property is a row vector, each element is
the center frequency of a channel in a multichannel signal. The vector
length equal the number of columns in the input signal **Port\_1**.

### **Metadata (structure or object)** — Data describing baseband signal empty structure (`struct()`) (default) | structure | object

Data describing the baseband signal, specified as a scalar structure or
object.

**Data Types:** `struct` | `object`

### **Number of latest samples to write** — Number of samples to write `inf` (default) | positive integer

Number of samples to save, specified as a positive integer or
`Inf`.

- To write all of the baseband signal samples to a file, set
  this property to `inf`.
- To write only the last `NumSamplesToWrite`
  samples to a file, set this property to a positive
  integer.

### **Simulate using** — Select simulation mode `Code generation` (default) | `Interpreted execution`

`Code generation`
:   On the first model run, simulate and generate code for the
    block using only MATLAB® functions supported for code generation. If the
    structure of the block does not change, subsequent model runs do
    not regenerate the code.

`Interpreted execution`
:   Simulate model using all supported MATLAB functions. Choosing this option can slow
    simulation performance.

## Libraries

Communications Toolbox / Comm Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Support writing objects to metadata

The Baseband File Writer block now supports writing objects and
structures-of-structures to the saved metadata.

## Description

Write baseband signals to file

The Baseband File Writer block writes a baseband signal to a specific
type of binary file. Baseband signals are typically down-converted from a nonzero center
frequency to 0 Hz. Sample rate, which is determined by the input signal sample time and
frame size, and center frequency are saved when the signal is written to a file.
