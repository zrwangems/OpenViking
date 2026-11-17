---
type: simulink-block
title: 'Discrete Varying Observer Form'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingobserverform'
documentation_source_path: 'ref/discretevaryingobserverform.html'
language: en
---

# Discrete Varying Observer Form

## Ports
```yaml
ports:
- name: yk
  summary: Measurement signal scalar | vector
  direction: input
- name: A
  summary: Plant state matrix matrix
  direction: input
- name: B
  summary: Plant input matrix matrix
  direction: input
- name: C
  summary: Plant output matrix matrix
  direction: input
- name: D
  summary: Plant feedforward matrix matrix
  direction: input
- name: K
  summary: State-feedback matrix matrix
  direction: input
- name: L
  summary: State-observer matrix matrix
  direction: input
- name: uk
  summary: Control signal scalar | vector
  direction: output
- name: xk
  summary: Estimated plant state vector vector
  direction: output
- name: xk+1
  summary: Estimated next state vector vector
  direction: output
```

### Input

### **yk** — Measurement signal scalar | vector

Measured plant output signal.

### **A** — Plant state matrix matrix

Plant state matrix of dimensions *Nx*-by-*Nx*, where *Nx* is
the number of plant states.

### **B** — Plant input matrix matrix

Plant input matrix of dimensions *Nx*-by-*Nu*, where *Nu* is
the number of plant inputs.

### **C** — Plant output matrix matrix

Plant output matrix of dimensions *Ny*-by-*Nx*, where *Ny* is
the number of plant outputs.

### **D** — Plant feedforward matrix matrix

Plant feedforward matrix of dimensions *Ny*-by-*Nu*.

### **K** — State-feedback matrix matrix

State-feedback matrix of dimensions *Nu*-by-*Nx*.

### **L** — State-observer matrix matrix

State-observer matrix of dimensions *Nx*-by-*Ny*.
### Output

### **uk** — Control signal scalar | vector

Control signal (plant input).

### **xk** — Estimated plant state vector vector

Vector of estimated plant states.

#### Dependencies

To enable this port, select the **Output states**
parameter.

### **xk+1** — Estimated next state vector vector

Estimated state values at next time step.

#### Dependencies

To enable this port, select the **Output state
updates** parameter.
## Parameters
```yaml
parameters:
- name: Initial conditions
  summary: System initial conditions 0 (default) | scalar | vector
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time –1 (default) | positive scalar
  group: ''
- name: Output states
  summary: Provide state output on (default) | off
  group: ''
- name: Output state derivatives
  summary: Provide state updates on (default) | off
  group: ''
```

### **Initial conditions** — System initial conditions 0 (default) | scalar | vector

Initial state values, specified as a scalar or a vector whose length is
the number of plant states.

### **Sample time (-1 for inherited)** — Block sample time –1 (default) | positive scalar

Block sample time, specified as either –1 (inherited sample time) or a
positive scalar value.

### **Output states** — Provide state output on (default) | off

Select to enable the estimated states output port,
**xe**.

### **Output state derivatives** — Provide state updates on (default) | off

Select to enable the estimated state updates output port,
**xk+1**.
## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time observer-form state-space model with varying matrix values

Use this block to implement a discrete-time varying state-space model in observer
form. The system matrices *A*, *B*,
*C*, and *D* describe the plant dynamics, and the
matrices *K* and *L* specify the state-feedback and
state-observer gains, respectively. Feed the instantaneous values of these matrices to
the corresponding input ports. The observer form is given by:

xk+1=Axk+Buk+Lεkuk=−Kxkεk=yk−Cxk−Duk,

where *uk* is the plant input (control
signal), *yk* is the plant output,
*xk* is the estimated state, and
*εk* is the innovation, the difference
between the predicted and measured plant output. The observer form works well for gain
scheduling of state-space controllers. In particular, the state
*xk* tracks the plant state, and all
controllers are expressed with the same state coordinates.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the **K** matrix depend on the control signal
**uk**. If you have such dependence,
the resulting equation *uk* =
–*K*(*uk*)*xk*
 creates an algebraic loop, because computing the block output
value requires knowing the block output value. This algebraic loop is prone to
instability and divergence. Instead, try expressing **K** in terms
of the time *t* and the block input
**yk**.

For similar reasons, avoid making **A**, **B**,
or **L** depend on the
**uk+1** output.
