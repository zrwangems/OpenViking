---
type: simulink-block
title: 'Power Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'poweramplifieridealizedbaseband'
documentation_source_path: 'ref/poweramplifieridealizedbaseband.html'
language: en
---

# Power Amplifier

## Ports

### Input

### **Port\_1** — Time-dependent input signal column

Time-dependent input signal, specified as a column. A column represents
consecutive points in time.

**Data Types:** `double` | `single`
### Output

### **Port\_1** — Time-dependent output signal complex column

Time-dependent output signal, returned as a complex column. The output
time-dependent signal is equal in size to the input time dependent signal.

**Data Types:** `double` | `single`

## Parameters

### **Model** — Model to design amplifier `Memory polynomial` (default) | `Cross-term memory`

Use either the `Memory polynomial` model or the
`Cross-term memory` model to design the power amplifier. The
following table summarizes the characteristics of the two models.

| Model | Characterization Data | Type of Coefficients | In-Band Spectral Regrowth | Out-of-Band Harmonic Generation |
| --- | --- | --- | --- | --- |
| `Memory polynomial` (default) | Bandpass (I,Q) | 2-D Complex matrix | Yes | No |
| `Cross-term memory` | Bandpass (I,Q) | 2-D Complex matrix | Yes | No |

For more information, see Model Type in Power Amplifier Block.

The **Model Type** parameter
has been renamed to **Model**. *(since R2024a)*

### **Coefficient matrix** — Coefficient matrix `1+0i` (default) | 2-D complex matrix

Coefficient matrix, specified as a 2-D complex matrix for the `Memory
polynomial` and `Cross-term memory` models.

For the `Memory polynomial` and `Cross-term
memory` models, you can identify the complex coefficient matrix based on
the measured complex (I,Q) output-vs.-input amplifier characteristic. As an example, see
the helper function in Coefficient Matrix Computation.

The size of the matrix depends on the number of delays and the degree of the system nonlinearity.

- For the `Memory polynomial` model, the matrix has
  dimensions Memory Depth (mem)×Voltage Order (deg).
- For the `Cross-term memory` model, the matrix has
  dimensions Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1}.

### **Measured interval of PA data (s)** — Sample time of measured input-output data `1e-6` (default) | positive scalar

Sample time of the input-output data that the block uses to construct the
coefficient matrix, specified in seconds.

The **Time interval of measured PA
data (s)** parameter has been renamed to **Measured interval of PA
data (s)**. *(since R2023b)*

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as one of the following:

- `Code generation` — Simulate model using generated C
  code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is faster than
  `Interpreted execution`.
- `Interpreted execution` — Simulate model using the
  MATLAB® interpreter. This option shortens startup time speed, but the speed
  of the subsequent simulations is slower than `Code
  generation`. In this mode, you can debug the source code of the
  block.

## Libraries

RF Blockset / Idealized Baseband

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024a: Parameter of Power Amplifier block from Idealized Baseband library renamed

The following in the Power Amplifier block in the Idealized baseband
library has been renamed or changed:

- The **Model Type** parameter has been renamed to
  **Model**.
- The `Cross-Term Memory` value in the
  **Model** parameter has been renamed to `Cross-term
  memory`.
- The default value of the **Coefficient Matrix** parameter has
  been updated to `1+0i` from `1`.

When you open a model created before R2024a containing the Power
Amplifier block, the software replaces the:

- **Model Type** parameter with the **Model**
  parameter.
- `Cross-Term Memory` value with the `Cross-term
  memory` value.
- Default value of the **Coefficient Matrix** parameter from
  `1` to `1+0i`.

### R2023b: Parameter of Power Amplifier block from Idealized Baseband library renamed

The **Time interval of measured PA data (s)** parameter in the
Power Amplifier block in the Idealized baseband library has been renamed to
**Measured interval of PA data (s)**.

When you open a model created before R2023b containing the Power Amplifer
block, the software replaces the **Time interval of measured PA data (s)**
parameter name with **Measured interval of PA data (s)**.

## Description

Model narrowband power amplifier with memory

The Power Amplifier block models a two-port power amplifier using a memory
polynomial expression derived from the Volterra series. The Volterra series models the
nonlinear relationship between input and output signals. This block includes memory effects:
the output response depends on the current input signal and the input signal at previous
times. Use this block when transmitting narrowband signals into your RF system.

The Power Amplifier block mask icons are dynamic and show the model
specified in the **Model** parameter.

| Model: `Memory polynomial` | Model: `Cross-term memory` |
| --- | --- |
| Power Amplifier block icon with Model parameter set to Memory Polynomial. | Power Amplifier block icon with Model parameter set to Cross-Term Memory. |
