---
type: simulink-block
title: 'ACIM Slip Speed Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'acimslipspeedestimator'
documentation_source_path: 'ref/acimslipspeedestimator.html'
language: en
---

# ACIM Slip Speed Estimator

## Ports

### Input

### **Isdref** — Reference *d*-axis stator current scalar

Reference *d*-axis stator current.

**Data Types:** `single` | `double` | `fixed point`

### **Isqref** — Reference *q*-axis stator current scalar

Reference *q*-axis stator current.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **⍵mslip** — Slip speed of induction motor scalar

Mechanical slip speed of the rotor that the block computes.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Number of pole pairs** — Number of pole pairs available in motor `2` (default) | scalar

Number of pole pairs available in the induction motor.

### **Rotor resistance (Ohm)** — Rotor resistance of motor `1.05` (default) | scalar

Rotor resistance of the induction motor in Ohms.

### **Rotor leakage inductance (H)** — Leakage inductance of rotor winding `6.81e-3` (default) | scalar

Inductance due to leakage flux linked to the rotor winding (in Henry).

### **Magnetizing inductance (H)** — Magnetizing inductance of induction motor `30e-3` (default) | scalar

Inductance due to the magnetizing flux (in Henry).

### **Output saturation (rpm)** — Saturation value for the block output `150` (default) | scalar

Saturation value for the block output (in rpm).

### **Input units** — Unit of input values `Per-Unit (PU)` (default) | SI Units

Unit of the input values.

### **Base speed (rpm)** — Base speed for per-unit system `1500` (default) | scalar

Base speed (in rpm) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

## Libraries

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020b**

## Description

Calculate slip speed of AC induction motor

The ACIM Slip Speed Estimator block computes the mechanical slip speed
(difference between the synchronous speed and rotor speed) of the induction motor.

The block accepts the reference values of *d*- and
*q*-axis currents and outputs the computed slip speed of the induction
motor.

### Equations

These equations describe the utilization of the slip speed value for field-oriented
control (FOC) of the induction motor:

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

If we keep the rotor flux as constant and the *d*-axis is aligned to
the rotor flux reference frame, then we can imply:

λrd=Lmisd

This block implements the preceding calculations as:

ωslip= (1p)(1τr)(isqrefisdref)

For detailed set of equations and assumptions, see Mathematical Model of Induction Motor.

where:

- ωe\_slip is the electrical slip speed of the rotor (Radians/ sec).
- ωslip is the mechanical slip speed of the rotor (Radians/ sec).
- ωe is the electrical speed corresponding to frequency of stator voltages
  (Radians/ sec).
- ωm is the rotor mechanical speed (Radians/ sec).
- ωr is the rotor electrical speed (Radians/ sec).
- Lm is the magnetizing inductance of the motor (Henry).
- Rr is the rotor resistance referred to stator (Ohms).
- isdref and isqref are the reference stator *d*- and
  *q*-axis currents (Amperes).
- τr is the rotor time constant (sec).
- λrd is the *d*-axis flux linkage of the rotor
  (Weber).
