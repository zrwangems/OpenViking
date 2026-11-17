---
type: simulink-block
title: 'Extended State Observer'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Disturbance Observer'
documentation_page: 'extendedstateobserver'
documentation_source_path: 'ug/extendedstateobserver.html'
language: en
---

# Extended State Observer

## Ports
```yaml
ports:
- name: u
  summary: Known inputs scalar | vector
  direction: input
- name: y
  summary: Measured outputs scalar | vector
  direction: input
- name: A
  summary: State matrix scalar | vector | matrix
  direction: input
- name: Bu
  summary: Input matrix scalar | vector | matrix
  direction: input
- name: Cm
  summary: Output matrix scalar | vector | matrix
  direction: input
- name: Bd
  summary: Disturbance matrix scalar | vector | matrix
  direction: input
- name: S0
  summary: Initial conditions scalar | vector
  direction: input
- name: L
  summary: Observer matrix scalar | vector | matrix
  direction: input
- name: dhat
  summary: Estimated disturbances vector
  direction: output
- name: xhat
  summary: Estimated states vector
  direction: output
```

### Input

### **u** — Known inputs scalar | vector

Specify the known inputs of the model as an
*Nu*-by-1 signal, where
*Nu* is the number of inputs in the
model.

### **y** — Measured outputs scalar | vector

Specify the measured outputs of the model
*Ny*-by-1 signal, where
*Ny* is the number of outputs in the
model.

### **A** — State matrix scalar | vector | matrix

Specify the state matrix as an
*Nx*-by-*Nx*
signal, where *Nx* is the number of states in
the model.

#### Dependencies

To enable this port, select the **Use external source for model matrices
(A,Bu,Cm)** and **Use external source for L**
parameters.

### **Bu** — Input matrix scalar | vector | matrix

Specify the input matrix as an
*Nx*-by-*Nu*
signal, where *Nx* is the number of states and
*Nu* is the number of inputs in the
model.

#### Dependencies

To enable this port, select the **Use external source for model matrices
(A,Bu,Cm)** and **Use external source for L**
parameters.

### **Cm** — Output matrix scalar | vector | matrix

Specify the output matrix as an
*Ny*-by-*Nx*
signal, where *Nx* is the number of states and
*Ny* is the number of outputs in the
model.

#### Dependencies

To enable this port, select the **Use external source for model matrices
(A,Bu,Cm)** and **Use external source for L**
parameters.

### **Bd** — Disturbance matrix scalar | vector | matrix

Specify the disturbance matrix as an
*Nx*-by-*Nd*
signal, where *Nx* is the number of states and
*Nd* is the number of disturbances in the
model.

#### Dependencies

To enable this port, select the **Use external source for matrix
Bd** and **Use external source for L**
parameters.

### **S0** — Initial conditions scalar | vector

Specify the initial conditions for the extended states as a scalar or vector with
length *Nx* +
*Nd*, where
*Nx* is the number of states and
*Nd* is the number of disturbances int the
model.

#### Dependencies

To enable this port, select **Use external source for initial conditions
S0 (x0,d0)**.

### **L** — Observer matrix scalar | vector | matrix

Specify the observer matrix as an
(*Nx*+*Nd*)-by-*Ny*
signal.

#### Dependencies

To enable this port, select **Use external source for matrix
L**.
### Output

### **dhat** — Estimated disturbances vector

Estimated disturbances in the model, returned as an
*Nd*-by-1 signal, where
*Nd* is the number of disturbances in the
model.

### **xhat** — Estimated states vector

Estimated states of the model, returned as an
*Nx*-by-1 signal, where
*Nx* is the number of states in the
model.

#### Dependencies

To enable this port, select **Output estimated model states
xhat**.
## Parameters
```yaml
parameters:
- name: Time domain
  summary: Controller time domain discrete-time (default) | continuous-time
  group: Parameters Tab
- name: LTI state-space variable
  summary: Known plant dynamics ss object | idss object
  group: Parameters Tab
- name: Use external source for model matrices (A,Bu,Cm)
  summary: Specify model matrices at block input ports off (default) | on
  group: Parameters Tab
- name: Number of states
  summary: Number of states in the model 1 (default) | positive integer
  group: Parameters Tab
- name: Number of inputs
  summary: Number of inputs in the model 1 (default) | positive integer
  group: Parameters Tab
- name: Number of outputs
  summary: Number of outputs in the model 1 (default) | positive integer
  group: Parameters Tab
- name: Specify gain k (such that Bd = k\*Bu)
  summary: Gain value for computing disturbance input matrix 1 (default) | nonzero scalar
  group: Parameters Tab
- name: Use external source for matrix Bd
  summary: Specify disturbance matrix at block input port off (default) | on
  group: Parameters Tab
- name: Number of disturbances
  summary: Number of disturbances in the model 1 (default) | positive integer
  group: Parameters Tab
- name: Initial conditions
  summary: Initial conditions for the extended states 0 (default) | scalar | vector
  group: Parameters Tab
- name: Use external source for initial conditions S0 (x0,d0)
  summary: Specify initial conditions at block input port off (default) | on
  group: Parameters Tab
- name: Bandwidth (rad/s)
  summary: Observer bandwidth 1 (default) | positive scalar
  group: Tuning Tab
- name: Spacing (rad/s)
  summary: Observer bandwidth spacing 0.01 (default) | positive scalar
  group: Tuning Tab
- name: Use external source for matrix L
  summary: Specify observer matrix at block input port off (default) | on
  group: Tuning Tab
- name: Data type
  summary: Floating point precision double (default) | single
  group: Block Tab
- name: Time delay
  summary: Specify time delays 1 (default) | positive scalar | vector
  group: Block Tab
- name: Output estimated model states xhat
  summary: Output estimated states at block output port on (default) | off
  group: Block Tab
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Parameters Tab

### **Time domain** — Controller time domain **discrete-time** (default) | **continuous-time**

Specify the controller time domain.

When you select **discrete-time**, specify the sample time using
the **Sample time** parameter.

### **LTI state-space variable** — Known plant dynamics `ss` object | `idss` object

Specify the known plant dynamics as a state-space model object. You can obtain
this model from a physical representation or an approximation of the plant.

### **Use external source for model matrices (A,Bu,Cm)** — Specify model matrices at block input ports `off` (default) | `on`

Select this option to specify the model matrices *A*,
*Bu*, and
*Cm* using the block input ports
**A**, **Bu**, and **Cm**,
respectively.

#### Dependencies

To enable this parameter, you must also select the **Use external source
for L** parameter.

### **Number of states** — Number of states in the model `1` (default) | positive integer

When you specify model matrices as block inputs, use this parameter to specify the
number of states in the model.

#### Dependencies

To enable this parameter, select the **Use external source for model
matrices (A,Bu,Cm)** and **Use external source for L**
parameters.

### **Number of inputs** — Number of inputs in the model `1` (default) | positive integer

When you specify model matrices as block inputs, use this parameter to specify the
number of inputs in the model.

#### Dependencies

To enable this parameter, select the **Use external source for model
matrices (A,Bu,Cm)** and **Use external source for L**
parameters.

### **Number of outputs** — Number of outputs in the model `1` (default) | positive integer

When you specify model matrices as block inputs, use this parameter to specify the
number of outputs in the model.

#### Dependencies

To enable this parameter, select the **Use external source for model
matrices (A,Bu,Cm)** and **Use external source for L**
parameters.

### **Specify gain k (such that Bd = k\*Bu)** — Gain value for computing disturbance input matrix `1` (default) | nonzero scalar

Specify the gain value *k* for computing disturbance matrix
*Bd* such that *Bd* =
*k×Bu*.

### **Use external source for matrix Bd** — Specify disturbance matrix at block input port `off` (default) | `on`

Select this option to specify the disturbance matrix
*Bd* using the block input port
**Bd**.

#### Dependencies

To enable this parameter, you must also select the **Use external source
for L** parameter.

### **Number of disturbances** — Number of disturbances in the model `1` (default) | positive integer

When you specify disturbance matrices as a block input, use this parameter to
specify the number of inputs in the model.

#### Dependencies

To enable this parameter, select the **Use external source for matrix
Bd** and **Use external source for L**
parameters.

### **Initial conditions** — Initial conditions for the extended states `0` (default) | scalar | vector

Specify the initial conditions for the extended states as a scalar or vector with
length *Nx* +
*Nd*, where
*Nx* is the number of states and
*Nd* is the number of disturbances int the
model.

### **Use external source for initial conditions S0 (x0,d0)** — Specify initial conditions at block input port `off` (default) | `on`

Select this option to specify the initial conditions using the block input port
**S0**.

### Tuning Tab

### **Bandwidth (rad/s)** — Observer bandwidth `1` (default) | positive scalar

Specify the observer bandwidth *ωo* as a
positive scalar.

### **Spacing (rad/s)** — Observer bandwidth spacing `0.01` (default) | positive scalar

Specify the spacing for the closed-loop poles. For given observer bandwidth
*ωo* and pole spacing
*δ*, the block places the closed-loop poles at [ωoωo+δωo+δ×2…ωo+δ×n], where *n* is the number of closed-loop
poles.

### **Use external source for matrix L** — Specify observer matrix at block input port `off` (default) | `on`

Select this option to specify the observer matrix using the block input port
**L**.

### Block Tab

### **Data type** — Floating point precision `double` (default) | `single`

Specify the floating-point precision based on simulation environment or hardware
requirements.

For continuous-time models, the block only supports `double` data
type.

### **Time delay** — Specify time delays `1` (default) | positive scalar | vector

Specify time delays in the model as a scalar or vector of length
*Nu*, where
*Nu* is the number of inputs in the
model.

For discrete-time models, specify the delay as an integer multiple
*k* of the sample time. The delay in discrete time is given by *Td* =
*k*×*Ts*.

#### Dependencies

To enable this parameter, select the **Specify input delays**
parameter.

### **Output estimated model states xhat** — Output estimated states at block output port `on` (default) | `off`

Select this option to output estimated model states at the block output
**xhat**.
## Libraries

Simulink Control Design / Disturbance Observer

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Estimate states and disturbances of a system

The Extended State Observer block lets you design an extended state
observer (ESO) algorithm to estimate and compensate for disturbances of linear time-invariant
or linear time-varying systems. These disturbances represent total disturbances, including
unknown dynamics and internal and external disturbances. Use this block to estimate the states
and disturbances of a given discrete-time or continuous-time system based on the system input
and output.

The block requires you to specify system dynamics in the following form.

x˙/x+=Ax+Buu+Bddym=Cmx

Here:

- *x* is the plant states
- x˙ is the state derivative in continuous time and
  *x+* is the state update
  *x*[*k*+1] in discrete time.
- *A*, *Bu*, and
  *Cm* are the plant dynamics.
- *ym* is the measurable plant output.
- *Bd* is the disturbance input matrix.
- *d* is the total disturbances in the model, including unknown
  dynamics and internal and external disturbances.

The block does not require you to provide an actual model of the plant. You can specify
the dynamics obtained from a physical representation or an approximation of the plant.
Therefore, the accuracy of estimation will depend on the accuracy of the plant approximation
you provide.

For more information, see Control Design and Disturbance Compensation Using Extended State Observers.
