---
type: simulink-block
title: 'Power Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'poweramplifier'
documentation_source_path: 'ref/poweramplifier.html'
language: en
---

# Power Amplifier

## Ports

Not documented in R2025b.

## Parameters

### **Model** — Model type `Memory polynomial` (default) | `Generalized Hammerstein` | `Cross-Term Memory` | `Cross-Term Hammerstein`

Model type, specified as `Memory polynomial`,
`Generalized Hammerstein`,
`Cross-Term Memory`, or `Cross-Term
Hammerstein`. The following table summarizes the
characteristics of the different models:

| Model | Characterization Data | Type of Coefficients | In-Band Spectral Regrowth | Out-of-Band Harmonic Generation |
| --- | --- | --- | --- | --- |
| `Memory polynomial` (default) | Bandpass (I,Q) | Complex | Yes | No |
| `Generalized Hammerstein` | True passband | Real | Yes | Yes |
| `Cross-Term Memory` | Bandpass (I,Q) | Complex | Yes | No |
| `Cross-Term Hammerstein` | True passband | Real | Yes | Yes |

- `Memory polynomial` – This narrowband
  memory polynomial implementation (equation (19) of [1]) operates on the envelope of the input signal, does not
  generate new frequency components, and captures in-band spectral
  regrowth. Use this model to create a narrowband amplifier
  operating at high frequency.

  The output signal, at any instant of time, is the sum of all
  the elements of the following complex matrix of dimensions Memory Depth (mem)×Voltage Order (deg):

  [C11V0C12V0|V0|⋯C1,degV0|V0|deg−1C21V1C22V1|V1|⋯C2,degV1|V1|deg−1⋮⋮⋱⋮Cmem,1Vmem−1Cmem,2Vmem−1|Vmem−1|⋯Cmem,degVmem−1|Vmem−1|deg−1].

  In the matrix, the number of rows equals the number of memory
  terms, and the number of columns equals the degree of the
  nonlinearity. The signal subscript represents amount of
  delay.
- `Generalized Hammerstein` – This
  wideband memory polynomial implementation (equation (18) of
  [1]) operates on the envelope of the input signal, generates
  frequency components that are integral multiples of carrier
  frequencies, and captures in-band spectral regrowth. Increasing
  the degree of the nonlinearity increases the number of
  out-of-band frequencies generated. Use this model to create
  wideband amplifiers operating at low frequency.

  The output signal, at any instant of time, is the sum of all
  the elements of the following real matrix of dimensions Memory Depth (mem)×Voltage Order (deg):

  [C11V0C12V02⋯C1,degV0degC21V1C22V12⋯C2,degV1deg⋮⋮⋱⋮Cmem,1Vmem−1Cmem,2Vmem−12⋯Cmem,degVmem−1deg].

  In the matrix, the number of rows equals the number of memory
  terms, and the number of columns equals the degree of the
  nonlinearity. The signal subscript represents amount of
  delay.
- `Cross-Term Memory` – This narrowband
  memory polynomial implementation (equation (23) of [1]) operates on the envelope of the input signal, does not
  generate new frequency components, and captures in-band spectral
  regrowth. Use this model to create a narrowband amplifier
  operating at high frequency. The model includes leading and
  lagging memory terms and provides a generalized implementation
  of the memory polynomial model.

  The output signal, at any instant of time, is the sum of all
  the elements of a matrix specified by the element-by-element product

  **C** .\* **M**CTM,

  where **C** is a complex coefficient matrix of dimensions Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1} and

  MCTM=[V0V1⋮Vmem−1][1|V0||V1|⋯|Vmem−1||V0|2⋯|Vmem−1|2⋯|V0|deg−1⋯|Vmem−1|deg−1]=[V0V0|V0|V0|V1|⋯V0|Vmem−1|V0|V0|2⋯V0|Vmem−1|2⋯V0|V0|deg−1⋯V0|Vmem−1|deg−1V1V1|V0|V1|V1|⋯V1|Vmem−1|V1|V0|2⋯V1|Vmem−1|2⋯V1|V0|deg−1⋯V1|Vmem−1|deg−1⋮⋮⋮⋱⋮⋮⋱⋮⋱⋮⋱⋮Vmem−1Vmem−1|V0|Vmem−1|V1|⋯Vmem−1|Vmem−1|Vmem−1|V0|2⋯Vmem−1|Vmem−1|2⋯Vmem−1|V0|deg−1⋯Vmem−1|Vmem−1|deg−1].

  In the matrix, the number of rows equals the number of memory
  terms, and the number of columns is proportional to the degree
  of the nonlinearity and the number of memory terms. The signal
  subscript represents amount of delay. The additional columns
  that do not appear in the `Memory
  polynomial` model represent the cross terms.
- `Cross-Term Hammerstein` – This
  wideband memory polynomial implementation operates on the
  envelope of the input signal, generates frequency components
  that are integral multiples of carrier frequencies, and captures
  in-band spectral regrowth. Increasing the order of the
  nonlinearity increases the number of out-of-band frequencies
  generated. Use this model to create wideband amplifiers
  operating at low frequency.

  The output signal, at any instant of time, is the sum of all
  the elements of a matrix specified by the element-by-element product

  **C** .\* **M**CTH,

  where **C** is a complex coefficient matrix of dimensions Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1} and

  MCTH=[V0V1⋮Vmem−1][1V0V1⋯Vmem−1V02⋯Vmem−12⋯V0deg−1⋯Vmem−1deg−1]=[V0V02V0V1⋯V0Vmem−1V03⋯V0Vmem−12⋯V0deg⋯V0Vmem−1deg−1V1V1V0V12⋯V1Vmem−1V1V02⋯V1Vmem−12⋯V1V0deg−1⋯V1Vmem−1deg−1⋮⋮⋮⋱⋮⋮⋱⋮⋱⋮⋱⋮Vmem−1Vmem−1V0Vmem−1V1⋯Vmem−12Vmem−1V02⋯Vmem−13⋯Vmem−1V0deg−1⋯Vmem−1deg].

  In the matrix, the number of rows equals the number of memory
  terms, and the number of columns is proportional to the degree
  of the nonlinearity and the number of memory terms. The signal
  subscript represents amount of delay. The additional columns
  that do not appear in the `Generalized
  Hammerstein` model represent the cross
  terms.

### **Coefficient Matrix** — Coefficient matrix 1 (default) | complex matrix | real matrix

Coefficient matrix, specified as a complex matrix for the
`Memory polynomial` and `Cross-Term
Memory` models and as a real matrix for the
`Generalized Hammerstein` and
`Cross-Term Hammerstein` models.

- For the `Memory polynomial` and
  `Cross-Term Memory` models, you can
  identify the complex coefficient matrix based on the measured
  complex (I,Q) output-vs.-input amplifier characteristic. As an
  example, see the helper function in Coefficient Matrix Computation.
- For the `Generalized Hammerstein` and
  `Cross-Term Hammerstein` models,
  you can identify the real coefficient matrix based on the
  measured real passband output-vs.-input amplifier
  characteristic.

The size of the matrix depends on the number of delays and the degree of
the system nonlinearity.

- For the `Memory polynomial` and
  `Generalized Hammerstein` models,
  the matrix has dimensions Memory Depth (mem)×Voltage Order (deg).
- For the `Cross-Term Memory` and
  `Cross-Term Hammerstein` models,
  the matrix has dimensions Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1}.

### **Measured interval of PA data (s)** — Sample interval of input-output data `1e-6` (default) | real positive scalar

Sample interval of the input-output data, which the block uses to define
the coefficient matrix, specified as a real positive scalar.

The **Coefficient Sample
Time (s)** parameter has been renamed to **Measured
interval of PA data (s)**. *(since R2023b)*

**Note**

To improve model accuracy, specify the **Measured interval of
PA data (s)** parameter to be equal to or larger than the
**Step size**
parameter in the Configuration block.

### **Rin (ohm)** — Input resistance `50` (default) | real positive scalar

Input resistance, specified as a real positive scalar.

### **Rout (ohm)** — Output resistance `50` (default) | real positive scalar

Output resistance, specified as a real positive scalar.

### **Ground and hide negative terminals** — Ground RF circuit terminals on (default) | off

Select this parameter to ground and hide the negative terminals. Clear the
parameter to expose the negative terminals. By exposing these terminals, you
can connect them to other parts of your model.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

### R2023b: Parameter of Power Amplifier block from Circuit Envelope library renamed

The **Coefficient Sample Time (s)** parameter in the Power
Amplifier block in the Circuit Envelope library has been renamed to
**Measured interval of PA data (s)**.

When you open a model created before R2023b containing the Power
Amplifier block, the software replaces the **Coefficient Sample
Time (s)** parameter name with **Measured interval of PA data
(s)**.

### R2021b: Power Amplifier block icon updated

Starting in R2021b, the Power Amplifier block icon is now updated.
When you open a model created before R2021b containing a Power
Amplifier block, the software replaces the block icon with the R2021b
version.

## Description

Model power amplifier with memory

The Power Amplifier block models two-port power amplifiers. A memory
polynomial expression derived from the Volterra series models the nonlinear relationship
between input and output signals. This power amplifier includes memory effects because
the output response depends on the current input signal and the input signal at previous
times. These power amplifiers are useful when transmitting wideband or narrowband
signals.
