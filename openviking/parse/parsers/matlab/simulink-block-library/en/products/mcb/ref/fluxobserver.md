---
type: simulink-block
title: 'Flux Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Sensorless Estimators'
documentation_page: 'fluxobserver'
documentation_source_path: 'ref/fluxobserver.html'
language: en
---

# Flux Observer

## Ports

### Input

### **Vα** — *α-*axis voltage scalar

Voltage component along the *α*-axis in the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vβ** — *β-*axis voltage scalar

Voltage component along the *β*-axis in the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iα** — *α-*axis current scalar

Current along the *α*-axis in the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iβ** — *β-*axis current scalar

Current along the *β*-axis in the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Rst** — Reset block scalar

The pulse (true value) that resets the block algorithm.

**Data Types:** `single` | `double` | `fixed point`

### **ParameterBus** — Computed parameters for flux observer bus

Computed parameters for the Flux Observer block. The input port
accepts the following parameters:

- **Pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator leakage inductance (H)**
- **Rotor leakage inductance (H)**
- **Magnetizing inductance (H)**
- **Cutoff frequency (Hz)**

Use this port along with the Compute
Parameter block to update the preceding block parameters optimally at
run-time.

#### Dependencies

To enable this port, select the **Use input port for computed parameters
(run-time motor swap)** parameter available in the **Advanced
Options** section.

**Data Types:** `single` | `double`
### Output

### **θe** — Electrical position of motor scalar

The electrical position of the rotor as estimated by the block.

#### Dependencies

To enable this port, select the **Position** option in the
**Block output** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **Ψ** — Rotor flux of motor scalar

The magnetic flux of the rotor as estimated by the block.

#### Dependencies

To enable this port, select the **Flux** option in the
**Block output** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **Te** — Electrical torque of motor scalar

The electrical torque of the motor as estimated by the block.

#### Dependencies

To enable this port, select the **Torque** option in the
**Block output** parameter.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Parameters

### **Motor selection** — Type of motor `PMSM` (default) | `ACIM`

Select the type of motor from the types that the block supports.

### **Support 16-bit fixedpoint datatype** — Support the data type of 16-bit fixed-point `off` (default) | `on`

To process 16-bit fixed-point inputs and perform computation using 16-bit
fixed-point data type, select this parameter. To use a data type other than 16-bit
fixed point, clear this parameter.

If you select this parameter:

- The block sets the **Input unit** parameter to
  `Per-unit`.
- The block selects the **Position** option in the
  **Block output** parameter because it does not support flux and
  torque computations when using the 16-bit data type.

### **Input unit** — Unit of voltage and current inputs `SI unit` (default) | `Per-unit`

Select the unit of the *α*- and *β*-axes voltage
and current input values.

### **Base voltage (V)** — Nominal voltage corresponding to one per-unit `13.86` (default) | scalar

The maximum phase voltage applied to the motor. For details, see Per-Unit System.

#### Dependencies

To enable this parameter, set **Input unit** to
`Per-unit`.

### **Base current (A)** — Nominal current corresponding to one per-unit `19.3` (default) | scalar

The maximum measurable current supplied to the motor. For details, see Per-Unit System.

#### Dependencies

To enable this parameter, set **Input unit** to
`Per-unit`.

### **Block output** — Block output options **Position** | **Flux** | **Torque**

Select one or more quantities that you want the block to compute and display in
the block output.

**Note**

You must select at least one value. The block displays an error message if you
click **Ok** or **Apply** without selecting a
value.

### **Pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

#### Dependencies

To enable this parameter:

- Select the **Torque** option in the **Block
  output** parameter.
- Clear the **Use input port for computed parameters (run-time motor
  swap)** parameter available in the **Advanced
  Options** section.

### **Stator resistance (ohm)** — Stator winding resistance `0.36` (default) | scalar

Stator phase winding resistance of the motor in ohms.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Stator d-axis inductance (H)** — Stator winding inductance along *d*-axis `0.2e-3` (default) | scalar

Stator winding inductance of the motor along the *d*-axis in
henries.

#### Dependencies

To enable this parameter:

- Set **Motor selection** to
  `PMSM`.
- Clear the **Use input port for computed parameters (run-time motor
  swap)** parameter available in the **Advanced
  Options** section.

### **Stator leakage inductance (H)** — Leakage inductance of stator winding `0.0068` (default) | scalar

Leakage inductance of the induction motor stator winding in henries.

#### Dependencies

To enable this parameter:

- Set **Motor selection** to
  `ACIM`.
- Clear the **Use input port for computed parameters (run-time motor
  swap)** parameter available in the **Advanced
  Options** section.

### **Rotor leakage inductance (H)** — Leakage inductance of rotor winding `0.0068` (default) | scalar

Leakage inductance of the induction motor rotor winding in henries.

#### Dependencies

To enable this parameter:

- Set **Motor selection** to
  `ACIM`.
- Clear the **Use input port for computed parameters (run-time motor
  swap)** parameter available in the **Advanced
  Options** section.

### **Magnetizing inductance (H)** — Magnetizing inductance of induction motor `0.0300` (default) | scalar

Magnetizing inductance of the induction motor in henries.

#### Dependencies

To enable this parameter:

- Set **Motor selection** to
  `ACIM`.
- Clear the **Use input port for computed parameters (run-time motor
  swap)** parameter available in the **Advanced
  Options** section.

### **Cutoff frequency (Hz)** — Cutoff frequency of internal highpass filter `3.1863` (default) | scalar

Cutoff frequency of the internal highpass filter (that filters noise) in
hertz.

The Flux Observer block uses an internal first-order IIR highpass
filter. Set the **Cutoff frequency (Hz)** for this filter to a value
that is lower than the electrical frequency corresponding to the minimum speed of the
motor. For example, you can enter a value that is one-tenth of the minimum frequency
of the motor currents. However, you can adjust this value to determine a more accurate
cutoff frequency that generates the desired block output.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Discrete step size (s)** — Interval between consecutive block executions `50e-6` (default) | scalar

The fixed time interval in seconds between two consecutive instances of block
execution.

### **Use input port for computed parameters (run-time motor swap)** — Option to enable input port to accept computed parameters `off` (default) | on

Select this parameter to enable the **ParameterBus** input port
and disable the following parameters:

- **Pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator leakage inductance (H)**
- **Rotor leakage inductance (H)**
- **Magnetizing inductance (H)**
- **Cutoff frequency (Hz)**

This parameter enables you to use the input port along with the Compute
Parameter block to update block parameters optimally at run-time.

### Datatypes

### **Position unit** — Unit of electrical position output `Radians` (default) | `Degrees` | `Per-unit`

Unit of the electrical position output.

#### Dependencies

To enable this parameter, select the **Position** option in the
**Block output** parameter.

### **Position datatype** — Data type of electrical position output `single` (default) | `double` | `fixed point`

Data type of the electrical position output.

#### Dependencies

To enable this parameter, select the **Position** option in the
**Block output** parameter.

### **Flux unit** — Unit of magnetic flux output `Weber` (default) | `Per-unit`

Unit of the magnetic flux output.

#### Dependencies

To enable this parameter, select the **Flux** option in the
**Block output** parameter.

### **Per unit flux (Wb)** — Flux corresponding to one per-unit `0.1` (default) | scalar

Flux value (in weber) corresponding to one per-unit. For details about the
per-unit system, see Per-Unit System.

#### Dependencies

To enable this parameter:

- Select the **Flux** option in the **Block
  output** parameter.
- Set the **Flux unit** parameter to
  `Per-unit`.

### **Flux datatype** — Data type of magnetic flux output `single` (default) | `double` | `fixed point`

Data type of the magnetic flux output.

#### Dependencies

To enable this parameter, select the **Flux** option in the
**Block output** parameter.

### **Torque unit** — Unit of electrical torque output `Nm` (default) | `Per-unit`

Unit of the electrical torque output.

#### Dependencies

To enable this parameter, select the **Torque** option in the
**Block output** parameter.

### **Per unit torque (Nm)** — Torque corresponding to one per-unit `100` (default) | scalar

Torque value (in Nm) corresponding to one per-unit. For details about the per-unit
system, see Per-Unit System.

#### Dependencies

To enable this parameter:

- Select the **Torque** option in the **Block
  output** parameter.
- Set the **Torque unit** parameter to
  `Per-unit`.

### **Torque datatype** — Data type of electrical torque output `single` (default) | `double` | `fixed point`

Data type of the electrical torque output.

#### Dependencies

To enable this parameter, select the **Torque** option in the
**Block output** parameter.

## Libraries

Motor Control Blockset HDL Support / Sensorless Estimators Motor Control Blockset / Sensorless Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

**Restrictions**

- The block supports HDL code generation only when you set the **Motor
  selection** parameter to `PMSM`.
- The block does not support HDL code generation when:

  - Input or output signals have mixed datatypes.
  - The parameter **Support 16-bit fixedpoint datatype** is
    selected.
  - Input or output signals have fixed point datatype of size less than 16
    bits.
- The block needs native floating point library to support fixed point datatype with
  HDL code generation.
- If you run third-party (3p) simulation, the block may show a minor mismatch (of
  the order `1e-7`) in the simulation results because of an internal
  trigonometric function that uses the floating point datatype.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute electrical position, magnetic flux, and electrical torque of rotor

The Flux Observer block computes the electrical position, magnetic flux,
and electrical torque of a surface-mount permanent magnet synchronous motor (SPMSM) or an
induction motor by using the per unit voltage and current values along the
*α-* and *β*-axes in the stationary *αβ*
reference frame.

The block also accepts 16-bit fixed-point data type inputs. To perform mathematical
operations on 16-bit fixed-point data type signals, the block uses optimized implementation of
equations for maintaining the best possible precision.

In addition, you can use the advanced options to enable the
**ParameterBus** input port, which you can use with the Compute Parameter block
to update the block parameters optimally at run-time. You can use this functionality when
motor parameters can change over time, for example, while building applications that may
require swapping of motors at run-time.

### Equations

These equations describe how the block computes the electrical position, magnetic flux,
and electrical torque for an SPMSM in the *αβ* reference frame.

ψα= ∫​(Vα−IαR)dt− (Ls⋅Iα)

ψβ= ∫​(Vβ−IβR)dt− (Ls⋅Iβ)

If (Vα−IαR)=v1(t) and (Vβ−IβR)=v2(t)

Then, the following Laplace transforms represent the integral terms available in
*Ψα* and
*Ψβ*:

L(∫​v1(t)dt)=1sL(v1(t))=1sv1(s)L(∫​v2(t)dt)=1sL(v2(t))=1sv2(s)

The block uses low-pass filter (LPF) based integrator to compute these integral
terms.

If the input electrical speed of the motor
(*ωe*) is much greater than the speed corresponding
to the cutoff frequency of LPF-based integrator
(*ωc*), then

L(∫​v1(t)dt)=1(s+ωc)v1(s)L(∫​v2(t)dt)=1(s+ωc)v2(s)

The LPF-based integrator does not allow any DC offset (in the block inputs) to ramp up
the block output. For example, consider an input function *X(s)=k/s*
corresponding to a step input *x(t) = k\*u(t)*. Using the preceding transfer
function of the LPF-based integrator, G(s)=1(s+ωc), we obtain:

Y(s)=G(s)X(s)=ks(s+ωc)=kωc(1s)−kωc(1s+ωc)Y(t)=kωcu(t)−kωcexp(−ωct)u(t)

According to the preceding equation, the step response of the LPF integrator
asymptotically settles to a DC value (that depends on the magnitude of the step input).
Whereas the step response of a pure integrator is a ramp function. Using a highpass filter
at the LPF integrator output eliminates the DC offset (present in the input)
completely.

ψ= ψα2+ψβ2

Te=32P(ψαIβ−ψβIα)

θe= tan−1ψβψα

These equations describe how the block computes the rotor electrical position, rotor
magnetic flux, and electrical torque for an induction motor.

ψα=LrLm (∫​(Vα−IαR)dt− σLsIα)

ψβ=LrLm (∫​(Vβ−IβR)dt− σLsIβ)

σ=1−Lm2Lr⋅Ls

ψ= ψα2+ψβ2

Te=32⋅P⋅LmLr(ψαIβ−ψβIα)

θe= tan−1ψβψα

where:

- Vα and Vβ are the *α-*axis and *β-*axis
  voltages (volts).
- Iα and Iβ are the *α-*axis and *β-*axis
  current (amperes).
- R is the stator resistance of the motor (ohms).
- Ls is the stator inductance of the motor (henry).
- Lr is the rotor inductance of the motor (henry).
- Lm is the magnetizing inductance of the motor (henry).
- σ is the total leakage factor of the induction motor.
- P is the number of motor pole pairs.
- ψ is the rotor magnetic flux (weber).
- ψα and ψβ are the rotor magnetic fluxes along the *α-* and
  *β-*axes (weber).
- Te is the electrical torque of the rotor (Nm).
- θe is the electrical position of the rotor (radians).
