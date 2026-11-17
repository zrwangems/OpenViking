---
type: simulink-block
title: 'ACIM Control Reference'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimcontrolreference'
documentation_source_path: '../mcb/ref/acimcontrolreference.html'
language: en
---

# ACIM Control Reference

## Ports
```yaml
ports:
- name: Tref
  summary: Reference torque value scalar
  direction: input
  data_types: single | double | fixed point
- name: ⍵m
  summary: Mechanical speed scalar
  direction: input
  data_types: single | double | fixed point
- name: Isdref
  summary: Reference *d*-axis stator current scalar
  direction: output
  data_types: single | double | fixed point
- name: Isqref
  summary: Reference *q*-axis stator current scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Tref** — Reference torque value scalar

Reference torque input value for which the block computes the reference
current.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed scalar

Reference mechanical speed value for which the block computes the reference
current.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Isdref** — Reference *d*-axis stator current scalar

Reference *d*-axis stator current value.

**Data Types:** `single` | `double` | `fixed point`

### **Isqref** — Reference *q*-axis stator current scalar

Reference *q*-axis stator current value.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of pole pairs
  summary: Number of pole pairs available in motor 2 (default) | scalar
  group: ''
- name: Rotor leakage inductance (H)
  summary: Leakage inductance of rotor winding 6.81e-3 (default) | scalar
  group: ''
- name: Magnetizing Inductance (H)
  summary: Magnetizing inductance of induction motor 30e-3 (default) | scalar
  group: ''
- name: Rated Flux (Wb)
  summary: Rated flux of motor 38.2e-3 (default) | scalar
  group: ''
- name: Rated Speed (rpm)
  summary: Rated speed of motor 1150 (default) | scalar
  group: ''
- name: Synchronous Speed (rpm)
  summary: Synchronous speed of motor 1500 (default) | scalar
  group: ''
- name: Max current (A)
  summary: Maximum phase current limit for motor (amperes) 3 (default) | scalar
  group: ''
- name: Input units
  summary: Unit of input values Per-Unit (PU) (default) | SI Units
  group: ''
- name: Base Current (A)
  summary: Base current for per-unit system 5.3611 (default) | scalar
  group: ''
- name: Base torque (Nm)
  summary: Base torque for per-unit system 0.50072 (default) | scalar
  group: ''
```

### **Number of pole pairs** — Number of pole pairs available in motor `2` (default) | scalar

Number of pole pairs available in the induction motor.

### **Rotor leakage inductance (H)** — Leakage inductance of rotor winding `6.81e-3` (default) | scalar

Inductance due to leakage flux linked to the rotor winding (in Henry).

### **Magnetizing Inductance (H)** — Magnetizing inductance of induction motor `30e-3` (default) | scalar

Inductance due to the magnetizing flux (in Henry).

### **Rated Flux (Wb)** — Rated flux of motor `38.2e-3` (default) | scalar

Rated flux of the induction motor (in Weber).

### **Rated Speed (rpm)** — Rated speed of motor `1150` (default) | scalar

Rated speed of the induction motor according to motor data sheet (in rpm).

### **Synchronous Speed (rpm)** — Synchronous speed of motor `1500` (default) | scalar

Synchronous speed of the induction motor (in rpm).

### **Max current (A)** — Maximum phase current limit for motor (amperes) `3` (default) | scalar

Maximum phase current limit for the induction motor (amperes).

### **Input units** — Unit of input values `Per-Unit (PU)` (default) | `SI Units`

Unit of the input values.

### **Base Current (A)** — Base current for per-unit system `5.3611` (default) | scalar

Base current (in Amperes) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base torque (Nm)** — Base torque for per-unit system `0.50072` (default) | scalar

Base torque (in Nm) for per-unit system. See Per-Unit System page for more
details.

This parameter is not configurable and uses a value that is internally computed
using other parameters.

#### Dependencies

To display this parameter, set **Input units** to
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
| **FlattenHierarchy** | Remove ACIM Control Reference block hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020b**

## Description

Compute reference currents for field-oriented control of induction motor

The ACIM Control Reference block computes the *d*-axis and
*q*-axis reference currents for the field-oriented control (and
field-weakening) operation.

The block accepts the reference torque and feedback mechanical speed and outputs the
corresponding *d*- and *q*-axes reference currents.

The block computes the reference current values by solving mathematical relationships. The
calculations use the SI unit system. When working with the Per-Unit (PU) system (with the
**Input units** parameter set to `Per-Unit (PU)`),
the block converts PU input signals to SI units to perform the computations and converts them
back to PU values at the output.

These equations describe how the block computes the reference *d*-axis
and *q*-axis current values.

### Mathematical Model of Induction Motor

These model equations describe the dynamics of induction motor in the rotor flux
reference frame:

The machine inductances are represented as,

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

Stator voltages are represented as,

vsd= Rsisd+σLsdisddt+LmLrdλrddt−ωeσLsisq

vsq= Rsisq+σLsdisqdt+LmLrωeλrd+ωeσLsisd

In the preceding equations, the flux linkages can be represented as,

λsd= LmLrλrd+σLsisd

λsq= σLsisq

τrdλrddt+ λrd=Lmisd

If we keep the rotor flux as constant and the *d*-axis is aligned to
the rotor flux reference frame, then we can imply:

λrd=Lmisd

λrq=0

These equations describe the mechanical dynamics,

Te=32p(LmLr)λrdisq

Te− TL=Jdωmdt +Bωm

These equations describe the slip speed,

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

### Reference Current Computation

These equations show computation of the reference currents,

isd\_0=λrdLm

isq\_req= Tref32p(LmLr)λrd

The reference currents are computed differently for operation below base speed and field
weakening region,

If ωm≤ ωrated:

isd\_sat=min(isd\_0,imax)

If ωm> ωrated:

isd\_fw=isd\_0(ωratedωm)

isd\_sat=min(isd\_fw,imax)

These equations indicate the *q*-axis current computation,

isq\_lim= imax2− isd\_sat2

isq\_sat=sat(isq\_lim,isq\_req)

The block outputs the following values,

isdref=isd\_sat

isqref=isq\_sat

where:

- p is the number of pole pairs of the motor.
- Rs is the stator phase winding resistance (Ohms).
- Rr is the rotor resistance referred to stator (Ohms).
- Lls is the stator leakage inductance (Henry).
- Llr is the rotor leakage inductance (Henry).
- Ls is the stator inductance (Henry).
- Lm is the magnetizing inductance (Henry).
- Lr is the rotor inductance referred to stator (Henry).
- σ is the total leakage factor of the induction motor.
- τr is the rotor time constant (sec).
- vsd and vsq are the stator *d*- and *q*-axis
  voltages (Volts).
- isd and isq are the stator *d*- and *q*-axis
  currents (Amperes).
- isd\_0 is the rated *d*-axis current of the stator also
  known as magnetizing current (Amperes).
- imax is the maximum phase current (peak) of the motor (Amperes).
- λsd is the *d*-axis flux linkage of the stator
  (Weber).
- λsq is the *q*-axis flux linkage of the stator
  (Weber).
- λrd is the *d*-axis flux linkage of the rotor
  (Weber).
- λrq is the *q*-axis flux linkage of the rotor
  (Weber).
- ωe\_slip is the electrical slip speed of the rotor (Radians/ sec).
- ωslip is the mechanical slip speed of the rotor (Radians/ sec).
- ωe is the electrical speed corresponding to frequency of stator voltages
  (Radians/ sec).
- ωm is the rotor mechanical speed (Radians/ sec).
- ωr is the rotor electrical speed (Radians/ sec).
- ωrated is the rated mechanical speed of the motor (Radians/ sec).
- Te is the electromechanical torque produced by the motor (Nm).
