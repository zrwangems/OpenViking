---
type: simulink-block
title: 'Iddata Sink'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'iddatasink'
documentation_source_path: 'ref/iddatasink.html'
language: en
---

# Iddata Sink

## Ports
```yaml
ports:
- name: Input
  summary: Input of iddata object scalar | vector
  direction: input
  data_types: double
- name: Output
  summary: Output of iddata object scalar | vector
  direction: input
  data_types: double
```

### Input

### **Input** — Input of `iddata` object scalar | vector

Input of `iddata` object, specified as a scalar for
single-input data. For multichannel data with *Nu*
inputs, specify `Input` as a vector of length
*Nu*.

**Data Types:** `double`

### **Output** — Output of `iddata` object scalar | vector

Output of `iddata` object, specified as a scalar for
single-output data. For multichannel data with *Ny*
outputs, specify `Output` as a vector of length
*Ny*.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: IDDATA Name
  summary: Name of iddata object data (default) | variable name
  group: ''
- name: Sample Time
  summary: Sample time in seconds 0.1 (default) | finite positive number
  group: ''
```

### **IDDATA Name** — Name of `iddata` object `data` (default) | variable name

Name of `iddata` object, specified as a MATLAB variable name. The object is exported with this name to the
MATLAB workspace.

### **Sample Time** — Sample time in seconds `0.1` (default) | finite positive number

Sample time in seconds, specified as a finite positive number. The
`iddata` object stores the input and output signals,
sampled at the sample time that you specify.
## Libraries

System Identification Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008a**

## Description

Export simulation data as iddata object to MATLAB workspace

The Iddata Sink block exports simulation data as an `iddata` object to the MATLAB® workspace. The object stores the input and simulated output signals,
sampled at the sample time that you specify. If you simulate your model from the model
window, the block exports the object to the MATLAB base workspace. If you simulate the model programmatically, the object is
exported to the MATLAB caller workspace. The caller workspace is the workspace of the function
that called the currently running function.
