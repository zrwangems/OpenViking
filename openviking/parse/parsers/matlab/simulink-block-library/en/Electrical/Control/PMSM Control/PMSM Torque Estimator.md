---
type: simulink-block
title: 'PMSM Torque Estimator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmtorqueestimator'
documentation_source_path: 'ref/pmsmtorqueestimator.html'
language: en
---

# PMSM Torque Estimator

## Ports

### Input

### **idq** — Stator currents vector

Stator direct and quadrature currents of the PMSM, in A.

**Data Types:** `single` | `double`
### Output

### **TqEst** — Torque estimate scalar

Estimated mechanical torque value of the PMSM, in N\*m.

**Data Types:** `single` | `double`

## Parameters

### **Machine parameters** — Parameter selection strategy `Constant parameters` (default) | `Lookup table based parameters`

Specify the type of machine parameters, which can be in the form of
constant values or tabulated data.

### **Number of pole pairs** — Pole pairs `8` (default) | positive integer

Number of permanent magnet pole pairs on the rotor.

### **D-axis current vector, id (A)** — D-axis current breakpoint vector `[-200,0,200]``A` (default) | monotonically increasing vector

Direct-axis current vector used in the lookup tables for parameters
determination.

### **Q-axis current vector, iq (A)** — Q-axis current breakpoint vector `[-200,0,200]``A` (default) | monotonically increasing vector

Quadrature-axis current vector used in the lookup tables for parameters
determination.

### **Ld matrix, Ld(id,iq) (H)** — D-axis inductance lookup data `0.0002 * ones(3, 3)``H` (default) | positive matrix

*Ld* matrix used as lookup table
data.

### **Lq matrix, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.0002 * ones(3, 3)``H` (default) | positive matrix

*Lq* matrix used as lookup table
data.

### **Permanent magnet flux linkage matrix, PM(id,iq) (Wb)** — Flux linkage lookup data `0.04 * ones(3, 3)``Wb` (default) | real matrix

Permanent magnet flux linkage matrix used in the lookup table.

### **D-axis inductance (H)** — Inductance of d-axis `0.0002` (default) | positive scalar

Direct-axis inductance.

### **Q-axis inductance (H)** — Inductance of q-axis `0.0002` (default) | positive scalar

Quadrature-axis inductance.

### **Permanent magnet flux linkage (Wb)** — PM Flux Linkage `0.04``Wb` (default) | positive scalar

Peak permanent magnet flux linkage.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `-1` or positive number

Sample time for the block (-1 for inherited). If you use this block inside
a triggered subsystem, set the sample time to `-1`. If you
use this block in a continuous variable-step model, set the sample time
explicitly.

## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Estimate permanent magnet synchronous machine torque

The PMSM Torque Estimator block implements a torque estimator for
permanent magnet synchronous machines (PMSM).

Use this block to estimate the mechanical torque of a motor when it is not directly
measurable. The block estimates torque using known machine parameters and the measured
phase current vector in the *dq0* reference frame.

Use the Park Transform
block to convert the measured phase current vector in the *abc*
reference frame to the *dq0* reference frame.

### Equations

The block estimates the mechanical torque
*Te* of the PMSM using the torque
equation in the *d*-*q* rotor reference frame:

Te=3p2(ψmiq+(Ld−Lq)idiq),

where

- *p* is the number of pole pairs of the PMSM.
- *ψm* is the flux linkage of
  the permanent magnet.
- *Ld* and
  *Lq* are the
  *d*- and *q*-axis inductances of
  the PMSM.
- *id* and
  *iq* are the
  *d*- and *q*-axis currents of the
  PMSM.

In practice, the machine parameters are not constants and depend on
some physical phenomena. You can choose to define these parameters simply as
constants or, more realistically, as functions of currents by using lookup
tables.

### Assumptions

The machine parameters are known.
