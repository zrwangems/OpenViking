---
type: simulink-block
title: 'Extended EMF Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'extendedemfobserver'
documentation_source_path: 'ref/extendedemfobserver.html'
language: en
---

# Extended EMF Observer

## Ports
```yaml
ports:
- name: Vα
  summary: '*α-*axis voltage scalar'
  direction: input
  data_types: single | double | fixed point
- name: Vβ
  summary: '*β-*axis voltage scalar'
  direction: input
  data_types: single | double | fixed point
- name: Iα
  summary: '*α-*axis current scalar'
  direction: input
  data_types: single | double | fixed point
- name: Iβ
  summary: '*β-*axis current scalar'
  direction: input
  data_types: single | double | fixed point
- name: Rst
  summary: Reset the block scalar
  direction: input
  data_types: single | double | fixed point
- name: ParameterBus
  summary: Computed parameters for Extended EMF Observer bus
  direction: input
  data_types: single | double
- name: θe
  summary: Electrical position of PMSM scalar
  direction: output
  data_types: single | double | fixed point
- name: Sin θe
  summary: Sine of electrical position of PMSM scalar
  direction: output
  data_types: single | double | fixed point
- name: Cos θe
  summary: Cosine of electrical position of PMSM scalar
  direction: output
  data_types: single | double | fixed point
- name: ⍵m
  summary: Mechanical speed of PMSM scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Vα** — *α-*axis voltage scalar

Per-unit voltage component along the *α*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vβ** — *β-*axis voltage scalar

Per-unit voltage component along the *β*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iα** — *α-*axis current scalar

Per-unit current component along the *α*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iβ** — *β-*axis current scalar

Per-unit current component along the *β*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Rst** — Reset the block scalar

The pulse (true value) that resets and restarts the processing of the block
algorithm.

**Data Types:** `single` | `double` | `fixed point`

### **ParameterBus** — Computed parameters for Extended EMF Observer bus

Computed parameters for the Extended EMF Observer block. The input
port accepts the following parameters:

- **Number of pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator q-axis inductance (H)**
- **Maximum application speed (RPM)**
- **EEMF observer gain**
- **EEMF filter cutoff frequency (Hz)**
- **Proportional (P)**
- **Integral (I)**
- **Speed filter cutoff frequency (Hz)**

Use this port along with the Compute
Parameter block to update the preceding block parameters optimally at
run-time.

#### Dependencies

To enable this port, select the **Use input port for computed parameters
(run-time motor swap)** parameter available in the **Advanced
Options** section.

**Data Types:** `single` | `double`
### Output

### **θe** — Electrical position of PMSM scalar

The estimated electrical position of the rotor.

#### Dependencies

To enable this port, set the **Position output** parameter to
`Electrical position`.

**Data Types:** `single` | `double` | `fixed point`

### **Sin θe** — Sine of electrical position of PMSM scalar

Sine of the estimated electrical position of the rotor.

#### Dependencies

To enable this port, set the **Position output** parameter to
`Sine and Cosine electrical position`.

**Data Types:** `single` | `double` | `fixed point`

### **Cos θe** — Cosine of electrical position of PMSM scalar

Cosine of the estimated electrical position of the rotor.

#### Dependencies

To enable this port, set the **Position output** parameter to
`Sine and Cosine electrical position`.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed of PMSM scalar

The estimated mechanical speed of the rotor.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Use input port for computed parameters (run-time motor swap)
  summary: Option to enable input port to accept computed parameters off (default) | on
  group: ''
- name: Input units
  summary: Units of block input SI unit (default) | Per-unit
  group: ''
- name: Position output
  summary: Type of position output Electrical position (default) | Sine and Cosine electrical position
  group: ''
- name: Discrete step size (s)
  summary: Sample time after which block executes again 50e-6 (default) | scalar
  group: ''
- name: Stator resistance (ohm)
  summary: Resistance 0.36 (default) | scalar
  group: Motor Parameters
- name: Stator d-axis inductance (H)
  summary: '*D*-axis inductance 0.2e-3 (default) | scalar'
  group: Motor Parameters
- name: Stator d-axis inductance (H)
  summary: '*Q*-axis inductance 0.2e-3 (default) | scalar'
  group: Motor Parameters
- name: Maximum application speed (RPM)
  summary: Maximum supported mechanical speed 6000 (default) | scalar
  group: Motor Parameters
- name: Number of pole pairs
  summary: Number of pole pairs available in motor 4 (default) | scalar
  group: Motor Parameters
- name: Maximum voltage (V)
  summary: Nominal voltage corresponding to one per unit 13.8564 (default) | scalar
  group: Motor Parameters
- name: Maximum current (A)
  summary: Nominal current corresponding to one per unit 21.4286 (default) | scalar
  group: Motor Parameters
- name: EEMF observer gain
  summary: Extended EMF observer gain 10 (default) | scalar
  group: Observer Parameters
- name: EEMF filter cutoff frequency (Hz)
  summary: Cutoff frequency of EEMF filter 7500 (default) | scalar
  group: Observer Parameters
- name: Proportional (P)
  summary: Proportional gain of speed observer 250 (default) | scalar
  group: Observer Parameters
- name: Integral (I)
  summary: Integral gain of the speed observer 200000 (default) | scalar
  group: Observer Parameters
- name: Number of data points for sine-cosine lookup table
  summary: Number of data points used for speed computation 1024 (default) | scalar
  group: Observer Parameters
- name: Speed filter cutoff frequency (Hz)
  summary: Cutoff frequency of speed filter 15 (default) | scalar
  group: Observer Parameters
- name: Position unit
  summary: Unit of position output Degrees (default) | Radians | Per-unit
  group: Datatypes
- name: Position data type
  summary: Data type of position output single (default) | double | fixed point
  group: Datatypes
- name: Speed unit
  summary: Unit of speed output Degrees/sec (default) | Radians/sec | RPM | Per-unit
  group: Datatypes
- name: Speed data type
  summary: Data type of speed output single (default) | double | fixed point
  group: Datatypes
- name: Table data type
  summary: Data type of table single (default) | double | fixed point
  group: Datatypes
```

### **Use input port for computed parameters (run-time motor swap)** — Option to enable input port to accept computed parameters `off` (default) | on

Select this parameter to enable the **ParameterBus** input port and
disable the following parameters:

- **Number of pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator q-axis inductance (H)**
- **Maximum application speed (RPM)**
- **EEMF observer gain**
- **EEMF filter cutoff frequency (Hz)**
- **Proportional (P)**
- **Integral (I)**
- **Speed filter cutoff frequency (Hz)**

This parameter enables you to use the input port along with the Compute Parameter
block to update block parameters optimally at run-time.

### **Input units** — Units of block input `SI unit` (default) | `Per-unit`

Units of inputs to the block.

### **Position output** — Type of position output `Electrical position` (default) | `Sine and Cosine electrical position`

Type of positions that the block outputs.

- `Electrical position` — Select this value to enable the
  `θe` port.
- `Sine and Cosine electrical position` — Select this
  value to enable the `Sin θe` and
  `Cos θe` ports.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between two consecutive instances of block
execution.

### Motor Parameters

### **Stator resistance (ohm)** — Resistance `0.36` (default) | scalar

Stator phase winding resistance (in ohm).

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Stator d-axis inductance (H)** — *D*-axis inductance `0.2e-3` (default) | scalar

Stator phase winding inductance (in Henry) along the *d*-axis of
the rotating *d-q* reference frame.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Stator d-axis inductance (H)** — *Q*-axis inductance `0.2e-3` (default) | scalar

Stator phase winding inductance (in Henry) along the *q*-axis of
the rotating *d-q* reference frame.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Maximum application speed (RPM)** — Maximum supported mechanical speed `6000` (default) | scalar

Maximum mechanical speed (in RPM) that the block can support. If you set the speed
to a value higher than this value, the block generates incorrect outputs.

**Note**

The block uses this parameter to filter out noise in the estimated speed
signal.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Maximum voltage (V)** — Nominal voltage corresponding to one per unit `13.8564` (default) | scalar

The maximum phase voltage applied to the PMSM. For details, see Per-Unit System.

### **Maximum current (A)** — Nominal current corresponding to one per unit `21.4286` (default) | scalar

The maximum measurable current supplied to the PMSM. For details, see Per-Unit System.

### Observer Parameters

### **EEMF observer gain** — Extended EMF observer gain `10` (default) | scalar

Gain of the linear extended EMF state observer.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **EEMF filter cutoff frequency (Hz)** — Cutoff frequency of EEMF filter `7500` (default) | scalar

Cutoff frequency of the lowpass filter that the block uses to remove noise in the
estimated back-EMF value.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Proportional (P)** — Proportional gain of speed observer `250` (default) | scalar

Proportional gain of the speed observer used by the block.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Integral (I)** — Integral gain of the speed observer `200000` (default) | scalar

Integral gain of the speed observer used by the block.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### **Number of data points for sine-cosine lookup table** — Number of data points used for speed computation `1024` (default) | scalar

Number of data points in the lookup table that the speed observer uses to compute
speed from the extended back-EMF value.

### **Speed filter cutoff frequency (Hz)** — Cutoff frequency of speed filter `15` (default) | scalar

Cutoff frequency of the lowpass filter that the block uses to remove noise in the
estimated speed.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

### Datatypes

### **Position unit** — Unit of position output `Degrees` (default) | `Radians` | `Per-unit`

Unit of the position output.

### **Position data type** — Data type of position output `single` (default) | `double` | `fixed point`

Data type of the position output.

### **Speed unit** — Unit of speed output `Degrees/sec` (default) | `Radians/sec` | `RPM` | `Per-unit`

Unit of the speed output.

### **Speed data type** — Data type of speed output `single` (default) | `double` | `fixed point`

Data type of the speed output.

### **Table data type** — Data type of table `single` (default) | `double` | `fixed point`

Data type of the table.
## Libraries

Motor Control Blockset / Sensorless Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2023a**

## Description

Compute electrical position and mechanical speed of permanent magnet synchronous motor (PMSM)

The Extended EMF Observer block computes the electrical position,
*θe* (or sin
*θe* and cos
*θe*), in addition to the mechanical speed of the
PMSM from the measured voltage and current in the stationary *αβ* reference
frame.

The block includes a linear extended EMF state observer that estimates the extended
back-EMF. It uses a lowpass filter to remove any noise in the estimated back-EMF value. In
addition, the block includes a speed feedforward-based quadrature phase-locked loop (PLL) that
acts as a speed observer. The speed observer uses the computed extended back-EMF to determine
the motor speed. It calculates speed with zero error even during constant angular
acceleration. The block then computes the position output from the estimated motor electrical
speed.

In addition, you can use the advanced options to enable the
**ParameterBus** input port, which you can use with the Compute Parameter block
to update the block parameters optimally at run-time. You can use this functionality when
motor parameters can change over time, for example, while building applications that may
require swapping of motors at run-time.

### Equations

The IPMSM state equation is defined as:

[i·e·]=[A11A120A22][ie]+[B10]v+[0W]i=C[ie]

These equations describe the reduced order PMSM state model:

i·=A11i+A12e+B1ve·=A22e

Extended back-EMF, e={(Ld−Lq)(ωreid−i·q)+ωreKE}[−sinθrecosθre]

This equation describes the reduced dimensional state observer:

e^·=(A^22−ξA12)e^+ξ(i·−A^11i−B1v)

These equations describe the extended EMF observer parameters:

A22−ξA12=ωreJ−(αI+βJ)(−1Ld)Iξ=(αI+βJ)

To ensure convergence, if you set β=ωre×Ld and set *α* to a negative value, then the extended EMF
observer gain can be determined as:

Extended EMF ​observer gain=−αLd

where:

- i=[iαiβ], e=[eαeβ], and v=[vαvβ].
- W=(Ld−Lq)(ωreid·−iq··)[−sinθrecosθre].
- A=[A11A120A22], B=[B10], and C=[I0].
- A11=−(RLd)I+(ωre(Ld−Lq)Ld)J, A12=(−1Ld)I, and A22=ωreJ.
- B1=(1Ld)I, I=[1001], and J=[0−110].

  **Note**

  A and C are an observable pair.
- "·" and "··" are the first-order and second-order differential operators,
  respectively.
- *vα* and
  *vβ* are the stator voltages along the
  *α*- and *β*-axes, respectively.
- *iα* and
  *iβ* are the stator currents along the
  *α*- and *β*-axes, respectively.
- *eα* and
  *eβ* are the extended back-EMF along the
  *α*- and *β*-axes, respectively.
- *id* and
  *iq* are the stator currents along the
  *d*- and *q*-axes, respectively.
- *R* is the stator resistance of PMSM.
- *Ld* and
  *Lq* are the stator inductances of PMSM across
  *d* and *q* axes, respectively.
- *KE* is the EMF constant.
- *ωre* is the angular velocity at electrical
  angle.
- *θre* is the rotor position at electrical
  angle.
- e^, A^22, and A^11 are the estimated values.
- *ξ* is the feedback gain.
