---
type: simulink-block
title: 'Induction Machine Direct Torque Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrol'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrol.html'
language: en
---

# Induction Machine Direct Torque Control

## Ports

### Input

### **FluxRef** — Flux scalar

Reference stator flux.

**Data Types:** `single` | `double`

### **TqRef** — Torque scalar

Reference torque.

**Data Types:** `single` | `double`

### **vabc** — Voltage vector

Stator phase voltages.

**Data Types:** `single` | `double`

### **iabc** — Current vector

Stator phase currents.

**Data Types:** `single` | `double`
### Output

### **G** — Gate pulses vector | `0` or `1`

Inverter gate pulses. The block does not consider any dead
time.

**Data Types:** `single` | `double`

## Parameters

### **Stator resistance (Ohm)** — Resistance `0.25` (default) | positive scalar

Resistance of the machine stator.

### **Number of pole pairs** — Pole number `1` (default) | positive integer

Number of machine pole pairs.

### **Flux hysteresis bandwidth (Wb)** — Flux `0.02` (default) | positive scalar

Total bandwidth distributed symmetrically around the flux set
point.

### **Torque hysteresis bandwidth (N\*m)** — Torque `10` (default) | positive scalar

Total bandwidth distributed symmetrically around the set point.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Induction machine DTC

The Induction Machine Direct Torque Control block implements an
induction machine direct torque control (DTC) structure. The figure shows the equivalent
circuit for the block.

### Equations

To estimate the torque and flux, the Induction Machine Direct Torque
Control block discretizes the machine voltage equations in the
stationary *ɑβ* reference frame using the backward Euler method.
The discrete-time equations for stator fluxes in the *ɑβ* frame are:

ψα=(vα−iαRs)Tszz−1

and

ψβ=(vβ−iβRs)Tszz−1

where:

- *vɑ* is
  *ɑ*-axis voltage.
- *iɑ* is
  *ɑ*-axis current.
- *Rs* is the stator
  resistance.
- *Ψɑ* is the
  *ɑ*-axis stator flux.
- *vβ* is
  *β*-axis voltage.
- *iβ* is
  *β*-axis current.
- *Ψβ* is the
  *β*-axis stator flux.

The block calculates the torque and flux as:

T=3p2(ψαiβ−ψβiα)

and

ψs=ψα2+ψβ2

where:

- *p* is the number of pole pairs.
- *Ψs* is the stator
  flux.

To detect flux and torque estimation errors, the block uses hysteresis
comparators. The figure shows hysteresis comparators and the associated switching sectors.

The table shows the optimum switching for an inverter high-side
system.

| *cΨ*, *cT**S*(*θ*) | | *S0* | *S1* | *S2* | *S3* | *S4* | *S5* |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cΨ = 1 | *cT* = 1 | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` |
| *cT* = 0 | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` |
| *cT* = -1 | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` |
| cΨ = 0 | *cT* = 1 | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` |
| *cT* = 0 | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` |
| *cT* = -1 | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` |

### Assumptions and Limitations

- The power inverter dead times are not considered. For hardware
  implementation, add the dead time externally.
