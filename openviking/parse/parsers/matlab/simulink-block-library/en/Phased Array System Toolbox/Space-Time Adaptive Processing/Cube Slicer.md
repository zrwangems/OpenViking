---
type: simulink-block
title: 'Data Cube Slicer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2023b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'datacubeslicer'
documentation_source_path: 'ref/datacubeslicer.html'
language: en
---

# Data Cube Slicer

## Ports
```yaml
ports:
- name: X
  summary: Input data cube *M*-by-*Q*-by-*N* complex-valued array
  direction: input
  data_types: double
- name: Idx
  summary: Slice-plane index positive integer
  direction: input
  data_types: double
- name: Port_1
  summary: Output complex-valued matrix
  direction: output
  data_types: double
```

### Input

### **X** — Input data cube *M*-by-*Q*-by-*N* complex-valued array

Input data cube, specified as an
*M*-by-*Q*-by-*N*
complex-valued matrix.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Idx** — Slice-plane index positive integer

Slice-plane index, specified as a positive integer. This index selects
which slice to use to create the two-dimensional output.

**Data Types:** `double`
### Output

### **Port\_1** — Output complex-valued matrix

Collapsed data cube, returned as a complex-valued matrix.

- If you set the **Output Slice** parameter
  to `Angle-Doppler`, the slice is the
  constant-range or fast-time plane. The output has dimensions
  *Q*-by-*N*.
- If you set the **Output Slice**
  parameter to `Range-Doppler`, the slice is
  the constant-angle plane. The output has dimension
  *M*-by-*N*.
- If you set the **Output Slice** parameter
  to `Range-angle`, the slice is the
  constant-Doppler plane. The output has dimension
  *M*-by-*Q*.

**Data Types:** `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Output Slice
  summary: Output slice Angle-Doppler (default) | Range-Doppler | Range-angle
  group: ''
```

### **Output Slice** — Output slice `Angle-Doppler` (default) | `Range-Doppler` | `Range-angle`

Output slice, specified as `Angle-Doppler`,
`Range-Doppler`, or
`Range-angle`. The output slices
are:

| Slice plane | Slice dimensions |
| --- | --- |
| `Angle-Doppler` | *Q*-by-*N* |
| `Range-Doppler` | *M*-by-*N* |
| `Range-angle` | *M*-by-*Q* |
## Libraries

Phased Array System Toolbox / Space-Time Adaptive Processing

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Slice data cube along specified dimensions

The Data Cube Slicer block slices a data cube through a specified plane. The
input is a data cube of dimensions
*M*-by-*Q*-by-*N*. The first
dimension is range, or fast time. The second dimension is angle, or channels. The third
dimension is Doppler, or slow time.
