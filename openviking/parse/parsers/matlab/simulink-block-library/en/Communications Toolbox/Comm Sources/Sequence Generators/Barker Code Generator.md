---
type: simulink-block
title: 'Barker Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'barkercodegenerator'
documentation_source_path: 'ref/barkercodegenerator.html'
language: en
---

# Barker Code Generator

## Ports
```yaml
ports:
- name: output
  summary: Barker code frame column vector
  direction: output
```

### Output

### **output** — Barker code frame column vector

Barker code frame, returned as a column vector. If the frame length
exceeds the Barker code length, the block fills the frame by repeating
the Barker code.

#### Dependencies

Set the data type of the output with the **Output data
type** parameter.
## Parameters
```yaml
parameters:
- name: Code length
  summary: Length of generated code 7 (default) | 1 | 2 | 3 | 4 | 5 | 11 | 13
  group: ''
- name: Sample time
  summary: Output sample time 1 (default) | -1 | positive scalar
  group: ''
- name: Samples per frame
  summary: Samples per output frame 1 (default) | positive integer
  group: ''
- name: Output data type
  summary: Output data type double (default) | int8
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Code length** — Length of generated code `7` (default) | `1` | `2` | `3` | `4` | `5` | `11` | `13`

Length of the generated code, specified as `1`,
`2`, `3`, `4`,
`5`, `7`, `11`, or
`13`. For more information, see Barker Codes.

**Example:** `2` outputs the Barker code
[–1;1].

### **Sample time** — Output sample time `1` (default) | -1 | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

### **Samples per frame** — Samples per output frame `1` (default) | positive integer

Samples per output frame, specified as a positive integer. If
**Samples per frame** is *M*, the
block outputs a frame containing *M* samples comprised of
length *N* Barker code sequences. *N* is
the length of the generated code, which is set by the **Code
length** parameter. When *M* is not an integer
multiple of *N*, consecutive frames maintain continuity of
the Barker code across frame boundaries.

For information on the relationship between **Sample
time** and **Samples per frame**, see Sample Timing.

### **Output data type** — Output data type `double` (default) | `int8`

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

Communications Toolbox Communications Toolbox / Comm Sources / Sequence Generators

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Does not support integer only code generation.

## Version History

**Introduced before R2006a**

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink no longer allows you to use the Barker Code Generator block version available
before R2015b.

Existing models automatically update to load the Barker Code Generator block version
announced in Source blocks output frames of contiguous time samples but do not use frame attribute. For more
information on block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).

## Description

Generate bipolar Barker Code

The Barker Code Generator block generates a bipolar Barker code. The short length and low
correlation sidelobes make Barker codes useful for frame synchronization in digital
communications systems. For more information, see Barker Codes.
