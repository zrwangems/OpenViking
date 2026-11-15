---
type: simulink-block
title: 'Sliding Mode Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Sensorless Estimators'
documentation_page: 'slidingmodeobserver'
documentation_source_path: 'ref/slidingmodeobserver.html'
language: en
---

# Sliding Mode Observer

## Ports

### Input

### **Vα** — *α*-axis voltage scalar

Voltage component along the *α*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vβ** — *β*-axis voltage scalar

Voltage component along the *β*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iα** — *α*-axis current scalar

Current component along the *α*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iβ** — *β*-axis current scalar

Current component along the *β*-axis of the stationary
*αβ* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Rst** — Reset the block scalar

The pulse (true value) that resets and restarts the processing of the block
algorithm.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **θe** — Electrical position of PMSM scalar

The estimated electrical position of the rotor.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed of PMSM scalar

The estimated mechanical speed of the rotor.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input units** — Unit of block inputs `SI unit` (default) | `Per-unit`

Unit of the input voltage and current components along the *α*-axis
and *β*-axis of the stationary *αβ* reference
frame.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

### Motor parameters

### **Stator resistance (ohm)** — Resistance `0.36` (default) | scalar

Stator phase winding resistance (in ohm).

### **Stator inductance (H)** — Inductance `0.2e-3` (default) | scalar

Stator phase winding inductance (in Henry).

### **Maximum application speed (RPM)** — Maximum supported mechanical speed `6000` (default) | scalar

Maximum mechanical speed (in RPM) that the block can support. For a speed beyond
this value, the block generates incorrect outputs.

**Note**

The block uses this parameter to filter out noise in the estimated speed
signal.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

### **Base voltage (V)** — Nominal voltage corresponding to one per unit `13.8564` (default) | scalar

The maximum phase voltage applied to the PMSM. For details, see Per-Unit System.

### **Base current (A)** — Nominal current corresponding to one per unit `21.4286` (default) | scalar

The maximum measurable current supplied to the PMSM. For details, see Per-Unit System.

**Note**

The Sliding Mode Observer block might occasionally display the warning
message `Wrap on overflow detected`.

### Observer Parameters

### **Back-emf observer gain** — Sliding mode observer gain for back-emf `0.9` (default) | scalar

The gain that ensures the convergence of the back-emf observer.

### **Current observer gain** — Sliding mode observer gain for current `0.50881` (default) | scalar

The gain that ensures the convergence of the current observer.

### **Filter cut-off frequency (Hz)** — Cut-off frequency of internal filter `1200` (default) | scalar

The cut-off frequency of the internal low-pass IIR filter. The cut-off frequency
value must be greater than or equal to the maximum electrical frequency.

Click **Compute default parameters** to calculate approximate
observer gains and the filter coefficient and update these fields. For this calculation, we
set *g* to `0.9`, computed *m* at twice
the rated speed, and set *η* to 1.1(bmg).

### Datatypes

### **Position unit** — Unit of position output `Radians` (default) | `Degrees` | `Per unit`

Unit of the position output.

### **Position data type** — Data type of position output `single` (default) | `double` | `fixed point`

Data type of the position output.

### **Speed unit** — Unit of speed output `RPM` (default) | `Degrees/sec` | `Radians/sec` | `Per unit`

Unit of the speed output.

### **Speed data type** — Data type of speed output `single` (default) | `double` | `fixed point`

Data type of the speed output.

## Libraries

Motor Control Blockset / Sensorless Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2021b**

## Description

Compute electrical position and mechanical speed of a surface-mount PMSM

The Sliding Mode Observer block computes the electrical position and
mechanical speed of a Surface Mount PMSM by using the voltage and current values along the
*α*- and *β*-axes of the stationary *αβ*
reference frame.

### Equations

These equations describe the discrete-time operation of a PMSM:

iαβ(k+1)=Aiαβ(k)+Bvαβ(k)−Beαβ(k)

eαβ(k+1)=eαβ(k)+Tsωe(k)Jeαβ(k)

J=[0−110]

Φ=[−RL00−RL]

A=eΦTs

B=∫0TseΦτdτ=[b00b]

b=1−e−RTs/LR

These equations describe the discrete-time sliding mode observer operation of a surface
mount PMSM:

i^αβ(k+1)=Ai^αβ(k)+Bvαβ(k)−Be^αβ(k)−ηSign(i˜αβ(k))

e^αβ(k+1)=e^αβ(k)+B−1g(i˜αβ(k)−Ai˜αβ(k−1)+ηSign(i˜αβ(k−1)))

i˜αβ(k)=i^αβ(k)−iαβ(k)

e˜αβ(k)=e^αβ(k)−eαβ(k)

If the back EMF observer fulfils the conditions |eαβ(k+1)−eαβ(k)|≤m and g∈(0,1), there exists a *k0*, such
that:

e˜αβ(k)<mg

If the sliding mode observer fulfils these conditions:

- g∈(0,1)
- |eαβ(k+1)−eαβ(k)|≤m
- η>bmg

then there exists a *k=k0*, such that for
*k≥k0*:

|i˜αβ(k)|≤η+bmg

where:

- *eα* and
  *iα* are the stator back EMF and current for
  the *α*-axis.
- *eβ* and
  *iβ* are the stator back EMF and current for
  the *β*-axis.
- *ẽα* and
  *ĩα* are the errors in the stator back EMF and
  current for the *α*-axis.
- *ẽβ* and
  *ĩβ* are the errors in the stator back EMF and
  current for the *β*-axis.
- *vα* and
  *vβ* are the stator supply voltages.
- *R* is the stator resistance.
- *L* is the stator inductance.
- *g* is the back EMF observer gain.
- *η* is the current observer gain.
- *ωe* is the electrical angular
  velocity.
- *Ts* is the sampling period.
- *k* is the sample count.

### Tuning Sliding Mode Observer

Use these steps to tune the block using the **Current observer gain**
(*η*) and **Back-emf observer gain**
(*g*) parameters.

- Select a back-emf observer gain (*g*) value such that g∈(0,1). Bringing *g* close to the value
  `1`, results in less error in the estimated back-emf. However, this
  makes convergence slow.
- Select a value of *m* based on the block sample time and maximum
  slope of the operating back-emf (such that |eαβ(k+1)−eαβ(k)|≤m).
- Select a current observer gain (*η*) value based on
  *b*, *m*, and *g* (such that η>bmg).

**Note**

The block functions correctly when you tune the sliding mode observer gains.

When using open-loop control to run a motor, compute the rotor position using both
sliding mode observer and an actual sensor hardware and compare the computed position
values. If the difference is acceptable, the block functions correctly. Otherwise,
manually tune the sliding mode observer gains to ensure that the block functions
accurately.

The transition from open-loop control to closed-loop control may fail due to noise in
the currents and voltages. To make a successful transition, try reducing the value of the
**Filter cut-off frequency (Hz)** parameter.
