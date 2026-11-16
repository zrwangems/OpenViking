---
type: simulink-block
title: 'Iddata Source'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'iddatasource'
documentation_source_path: 'ref/iddatasource.html'
language: en
---

# Iddata Source

## Ports

### Output

### **Input** — Input data stored in `iddata` object scalar | vector

Input data stored in `iddata` object, returned as a
scalar for single-input data and a vector of length
*Nu* for multichannel data with
*Nu* inputs. If `z` is the
`iddata` object, the output at this port at
simulation time *t* is `z.InputData`
at time *t*. If *t* is greater than
`z.SamplingInstants(end)`, the maximum time in
`z`, the input data is returned as
`0` for each input channel.

**Data Types:** `double`

### **Output** — Output data stored in `iddata` object scalar | vector

Output data stored in `iddata` object, returned as a
scalar for single-output data and as a vector of length
*Ny* for multichannel data with
*Ny* outputs. If `z` is the
`iddata` object, the output at this port at
simulation time *t* is `z.OutputData`
at time *t*. If *t* is greater than
`z.SamplingInstants(end)`, the maximum time in
`z`, the output data is returned as
`0` for each output channel.

**Data Types:** `double`

## Parameters

### **IDDATA object** — Time-domain data to be imported `iddata(1,1)` (default) | `iddata` object

Time-domain data that is to be imported, specified as an
`iddata` object that you have created in the
MATLAB workspace. The `iddata` object must contain
only one experiment. For a multiple-experiment `iddata`
object `z`, to specify an `iddata` object
for experiment number `kexp`, specify **IDDATA
object** as `getexp(z,kexp)`.

### **Start time** — Start time for signals in `iddata` object `-1` (default) | non-negative real scalar

Start time for signals in the `iddata` object, specified
as `-1` or a non-negative real scalar. The default value of
`-1` means that this start time matches that of the
Simulink model. To specify the start time of the signals to be the same as
that of the `iddata` object, set the **Start
time** to `data.Tstart`, where
`data` is the `iddata` object.

## Libraries

System Identification Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Import time-domain data stored in iddata object in MATLAB workspace

The Iddata Source block imports the input-output time-domain data
stored in an `iddata` object in the MATLAB® workspace. You can use this block to import data for simulating a model in
Simulink®.
