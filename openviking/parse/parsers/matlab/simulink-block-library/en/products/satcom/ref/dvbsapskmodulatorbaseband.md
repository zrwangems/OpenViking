---
type: simulink-block
title: 'DVBS-APSK Modulator Baseband'
family: 'satcom'
product_id: 'satcom'
product_name: 'Satellite Communications Toolbox'
documentation_release: R2025b
official_category: 'Signal Transmission'
documentation_page: 'dvbsapskmodulatorbaseband'
documentation_source_path: 'ref/dvbsapskmodulatorbaseband.html'
language: en
---

# DVBS-APSK Modulator Baseband

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The input
signal must be binary values or integers in the range [0,
(*M* – 1)], where *M* is the
**Modulation order**. This port is unnamed on the block.

**Note**

To process the input signal as binary elements, set the
**Input type** parameter value to
`Bit`. For binary inputs, the
number of rows must be an integer multiple of
log2(*M*). Groups of
log2(*M*) bits in a
column are mapped onto a symbol, with the first bit representing
the MSB and the last bit representing the LSB.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — DVB-S2/S2X/SH standard-specific APSK modulated signal scalar | vector | matrix

DVB-S2/S2X/SH standard-specific APSK modulated signal, returned as a complex scalar,
vector, or matrix. The output signal dimensions depend on the specified
**Input type** value. This port is unnamed on the
block.

| **Input type** | Dimensions of Output Signal |
| --- | --- |
| `Integer` | The output signal has the same dimensions as the input signal. |
| `Bit` | The number of rows in the output signal equals the number of rows in the input signal divided by log2(*M*), where *M* is the **Modulation order**. |

Use **Output data type** to specify the output data
type.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **DVB standard suffix** — Standard suffix `S2` (default) | `S2X` | `SH`

Standard suffix for DVB modulation variant, specified as
`S2`, `S2X`, or
`SH`.

### **Frame length** — Frame length `Normal` (default) | `Short`

Frame length, specified as `Normal` or
`Short`.

#### Dependencies

This parameter applies only when **DVB
standard suffix** is set to `S2`
or `S2X`.

### **Modulation order** — Modulation order `16` (default) | `8` | `32` | `64` | `256`

Modulation order, *M*, specified as a power of two. The modulation order
specifies the total number of points in the constellation of the output
signal. The list of valid modulation orders varies depending on the values
of **DVB
standard suffix** and **Frame
length**.

| **DVB standard suffix** | **Frame length** | **Modulation order** Options |
| --- | --- | --- |
| `S2` | `Normal` or `Short` | `16` or `32` |
| `S2X` | `Normal` | `8`, `16`, `32`, `64`, or `256` |
| `Short` | `16` or `32` |
| `SH` | Not applicable | `16` |

### **Code identifier** — Code identifier `2/3` | character vector

Code identifier, specified as a character vector. The list of valid code identifier
values varies depending on the specified values of **DVB
standard suffix**, **Frame
length**, and **Modulation order**. This table lists the options for
**Code identifier** values.

| **Modulation order** | **DVB standard suffix** | **Frame length** | **Code identifier** Options |
| --- | --- | --- | --- |
| `8` | `S2X` | `Normal` | `100/180` or `104/180` |
| `16` | `S2` or `S2X` | `Normal` | `2/3`, `3/4`, `4/5`, `5/6`, `8/9`, or `9/10` |
| `Short` | `2/3`, `3/4`, `4/5`, `5/6`, or `8/9` |
| `16` | `S2X` | `Normal` | `26/45`, `3/5`, `28/45`, `23/36`, `25/36`, `13/18`, `140/180`, `154/180`, `100/180`, `96/180`, `90/180`, `18/30`, or `20/30` |
| `Short` | `7/15`, `8/16`, `26/45`, `3/5`, or `32/45` |
| `32` | `S2` or `S2X` | `Normal` | `3/4`, `4/5`, `5/6`, `8/9`, or `9/10` |
| `Short` | `3/4`, `4/5`, `5/6`, or `8/9` |
| `32` | `S2X` | `Normal` | `128/180`, `132/180`, `140/180`, or `2/3` |
| `Short` | `2/3` or `32/45` |
| `64` | `S2X` | `Normal` | `128/180` , `132/180`, `7/9`, `4/5`, or `5/6` |
| `128` | `S2X` | `Normal` | `135/180` or `140/180` |
| 256 | `S2X` | `Normal` | `116/180`, `124/180`, `128/180`, `20/30`, or `135/180` |

For more information, refer to Tables 9 and 10 in the DVB-S2
standard [1] and Table 17a in
the DVB-S2X standard [2].

#### Dependencies

This parameter applies only when **DVB
standard suffix** is set to `S2`
or `S2X`.

### **Constellation scaling** — Constellation scaling `Outer radius as 1` (default) | `Unit average power`

Constellation scaling, specified as `Outer radius as
1` or `Unit average power`.

#### Dependencies

This parameter applies only when **DVB
standard suffix** is set to `S2`
or `S2X`.

### **Input type** — Input type `Integer` (default) | `Bit`

Input type, specified as `Integer` or
`Bit`. To use
`Integer`, the input signal must consist of
integers in the range [0, (*M* – 1)]. To use
`Bit`, the input data must contain binary
values, and the number of rows must be an integer multiple of
log2(*M*), where
*M* is the **Modulation order**.

### **Output data type** — Output data type `double` (default) | `single`

Output data type, specified as `double` or
`single`.

### **View Constellation** — Plot reference constellation `button`

To plot the reference constellation, click the **View
Constellation** button.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as:

- `Code generation` –– Simulate the
  model using generated C code. The first time you run a
  simulation, Simulink generates C code for the block. The C code is
  reused for subsequent simulations as long as the model does not
  change. This option requires additional startup time.
- `Interpreted execution` –– Simulate
  the model using the MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you
  can debug the source code of the block.

## Libraries

Satellite Communications Toolbox / Modulation / Digital Baseband Modulation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2024b: Moved to Satellite Communications Toolbox from Communications Toolbox

Previously, `DVBS-APSK Modulator Baseband` required Communications Toolbox™.

## Description

DVB-S2/S2X/SH standard-specific APSK modulation

The DVBS-APSK Modulator Baseband block modulates the input signal using Digital Video Broadcasting (DVB-S2/S2X/SH) standard-specific amplitude
phase shift keying (APSK) modulation.
