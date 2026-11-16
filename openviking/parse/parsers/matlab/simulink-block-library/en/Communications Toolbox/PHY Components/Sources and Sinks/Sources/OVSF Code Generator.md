---
type: simulink-block
title: 'OVSF Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Sources and Sinks / Sources'
documentation_page: 'ovsfcodegenerator'
documentation_source_path: 'ref/ovsfcodegenerator.html'
language: en
---

# OVSF Code Generator

## Ports

### Output

### **Out** — Output data column vector

Output data, returned as a binary-valued column vector containing the OVSF code
generated from a set of orthogonal codes.

**Data Types:** `double` | `int8`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Code length** — Code length `64` (default) | positive integer

Length of the generated code, specified as a positive integer power of 2. The code length
value is the spreading factor of the code. For more information, see Spread Spectrum.

The spreading factor is the length of the code selected from the OVSF code
matrix. OVSF codes are defined as the rows of an
*N*-by-*N* matrix,
*C**N*. The
**Code
index** parameter specifies the row of the
*C*N matrix as the code of
interest. For more information, see Orthogonal Variable Spreading Factor Codes.

### **Code index** — Row index of OVSF code matrix `60` (default) | integer

Row index of the OVSF code matrix, specified as an integer in the range [0,
(*N* – 1)], where *N* is the spreading
factor as specified by the value of the **Code
length** parameter. OVSF codes are defined as the rows of an
*N*-by-*N* matrix,
*C**N*. The
value of this property specifies the row of the
*C*N matrix as the code of
interest. For more information, see Recovering and Reconstructing OVSF Codes.

### **Sample time** — Sample time, in seconds `1` (default) | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

### **Samples per frame** — Number of OVSF chips output `1` (default) | positive integer

Number of OVSF code chips output, specified as a positive integer. Each time the block
runs, it outputs the first **Samples per frame** chips of
the OVSF code specified by the **Code
length** and **Code
index** property values. For more information, see Spread Spectrum.

For information on the relationship between **Sample
time** and **Samples per frame**, see Sample Timing.

### **Output data type** — Output type `double` (default) | `int8`

Output data type, specified as `double` or
`int8`.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Comm Sources / Sequence Generators

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink no longer allows you to use the OVSF Code Generator block version available
before R2015b.

Existing models automatically update to load the OVSF Code Generator block version
announced in Source blocks output frames of contiguous time samples but do not use frame attribute. For more
information on block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).

## Description

Generate OVSF code

The OVSF Code Generator block generates a code from an orthogonal variable spreading
factor (OVSF) matrix. Use OVSF codes to preserve orthogonality between different
channels in a spread spectrum communications system. For more information, see Algorithms.
