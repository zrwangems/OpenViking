---
type: simulink-block
title: 'Varying Observer Form'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / LPV and LTV Models / Continuous-Time Varying Systems'
documentation_page: 'varyingobserverform'
documentation_source_path: 'ref/varyingobserverform.html'
language: en
---

# Varying Observer Form

## Ports

### Input

### **y** — Measurement signal scalar | vector

Measured plant output signal.

### **A** — Plant state matrix matrix

Plant state matrix of dimensions *Nx*-by-*Nx*, where *Nx* is
the number of plant states.

### **B** — Plant input matrix matrix

Plant input matrix of dimensions *Nx*-by-*Nu*, where *Nu* is
the number of plant inputs.

### **C** — Plant output matrix matrix

Plant output matrix *Ny*-by-*Nx*, where *Ny* is
the number of plant outputs.

### **D** — Plant feedforward matrix matrix

Plant feedforward matrix of dimensions *Ny*-by-*Nu*.

### **K** — State-feedback matrix matrix

State-feedback matrix of dimensions *Nu*-by-*Nx*.

### **L** — State-observer matrix matrix

State-observer matrix of dimensions *Nx*-by-*Ny*.
### Output

### **u** — Control signal scalar | vector

Control signal (plant input).

### **xe** — Estimated plant state vector vector

Vector of estimated plant states.

#### Dependencies

To enable this port, select the **Output states**
parameter.

### **dxe** — Estimated state derivatives vector

Derivatives of the corresponding estimated states in
**xe**.

#### Dependencies

To enable this port, select the **Output state
updates** parameter.

## Parameters

### **Initial conditions** — System initial conditions 0 (default) | scalar | vector

Initial state values, specified as a scalar or a vector whose length is
the number of plant states.

### **State names (e.g., 'position')** — Plant state names `''` (default) | character vector | cell array

To identify plant states, specify state names as a:

- character vector, for a one-state plant.
- Cell array of character vectors, for a multistate
  plant.

### **Output states** — Provide state output on (default) | off

Select to enable the estimated states output port,
**xe**.

### **Output state derivatives** — Provide state derivatives on (default) | off

Select to enable the estimated state derivatives output port,
**dxe**.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Observer-form state-space model with varying matrix values

Use this block to implement a continuous-time varying state-space model in observer
form. The system matrices *A*, *B*,
*C*, and *D* describe the plant dynamics, and the
matrices *K* and *L* specify the state-feedback and
state-observer gains, respectively. Feed the instantaneous values of these matrices to
the corresponding input ports. The observer form is given by:

dxe=Axe+Bu+Lεu=−Kxeε=y−Cxe−Du,

where *u* is the plant input (control signal), *y*
is the plant output, *xe* is the estimated
state, and *ε* is the innovation, the difference between the predicted
and measured plant output. The observer form works well for gain scheduling of
state-space controllers. In particular, the state
*xe* tracks the plant state, and all
controllers are expressed with the same state coordinates.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the **K** matrix depend on the control signal
**u**. If you have such dependence, the resulting equation *u* =
–*K*(*u*)*xe*
 creates an algebraic loop, because computing the block output
value requires knowing the block output value. This algebraic loop is prone to
instability and divergence. Instead, try expressing **K** in terms
of the time *t* and the block input **y**.

For similar reasons, avoid making **A** and
**B** depend on the
**dxe** output.
