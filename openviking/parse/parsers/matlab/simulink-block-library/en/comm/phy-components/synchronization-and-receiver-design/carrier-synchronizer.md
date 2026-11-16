---
type: simulink-block
title: 'Carrier Synchronizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'carriersynchronizer'
documentation_source_path: 'ref/carriersynchronizer.html'
language: en
---

# Carrier Synchronizer

## Ports

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or vector.

This port is unnamed on the block.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Phase corrected output signal scalar | column vector

Phase corrected output signal, returned as a scalar or column vector
with the same data type and length as the input signal. The output
signal adjusts the input signal compensating for carrier frequency and
phase offsets in signals that use single-carrier modulation
schemes.

This port is unnamed on the block until the **Estimated phase
error output port** parameter is selected.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **PhEst** — Phase estimate in radians scalar | column vector

Phase estimate in radians, returned as a scalar or column vector with
the same length as the input signal.

#### Dependencies

To enable this port, select the **Estimated phase
error output port** parameter.

**Data Types:** `double` | `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Modulation** — Modulation type `QAM` (default) | `8PSK` | `BPSK` | `OQPSK` | `PAM` | `QPSK`

Modulation type, specified as `QAM`,
`8PSK`, `BPSK`,
`OQPSK`, `PAM`, or
`QPSK`.

### **Modulation phase offset** — Modulation phase offset method `Auto` (default) | `Custom`

Modulation phase offset method, specified as
`Auto` or
`Custom`.

- `Auto` — Apply the traditional offset for
  the specified modulation type.

  | Modulation | Phase Offset (radians) |
  | --- | --- |
  | `BPSK`, `QAM`, or `PAM` | 0 |
  | `OQPSK` or `QPSK` | *π*/4 |
  | `8PSK` | *π*/8 |
- `Custom` — Specify a user-defined phase
  offset with the CustomPhaseOffset property.

**Tunable:** Yes

### **Custom phase offset (radians)** — Custom phase offset in radians `0` (default) | scalar

Custom phase offset in radians, specified as a scalar.

#### Dependencies

This parameter applies when you set **Modulation
phase offset** to
`Custom`.

### **Samples per symbol** — Number of samples per symbol `2` (default) | positive integer

Number of samples per symbol, specified as a positive integer.

**Tunable:** Yes

### **Damping factor** — Damping factor of loop `0.707` (default) | positive scalar

Damping factor of the loop, specified as a positive scalar.

**Tunable:** Yes

### **Normalized loop bandwidth** — Normalized bandwidth of loop `0.01` (default) | scalar

Normalized bandwidth of the loop, specified as a scalar in the range
(0,1]. The loop bandwidth is normalized by the sample rate of the
synchronizer.

Decreasing the loop bandwidth reduces the synchronizer convergence time
but also reduces the pull-in range of the synchronizer.

**Tunable:** Yes

### **Estimated phase error output port** — Enable estimated phase error output port `on` (default) | `off`

Select this check box to provide the estimated phase error to output port
**phEst**.

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

Communications Toolbox / Synchronization

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Compensate for carrier frequency offset

The Carrier Synchronizer block compensates for carrier frequency and phase
offsets in signals that use single-carrier modulation schemes. The carrier synchronizer
algorithm is compatible with BPSK, QPSK, OQPSK, 8-PSK, PAM, and rectangular QAM
modulation schemes.

**Note**

Modulation-type dependent phase ambiguities may be introduced by the
synchronization algorithm. For more information, see Potential Phase Ambiguity.

This icon shows the block without optional port.
