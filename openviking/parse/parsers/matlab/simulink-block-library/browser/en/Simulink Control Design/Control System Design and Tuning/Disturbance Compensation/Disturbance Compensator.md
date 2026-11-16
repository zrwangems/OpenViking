---
type: simulink-block
title: 'Disturbance Compensator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Disturbance Compensation'
documentation_page: 'disturbancecompensator'
documentation_source_path: 'ug/disturbancecompensator.html'
language: en
---

# Disturbance Compensator

## Ports

### Input

### **u0** — Nominal controller inputs scalar | vector

Specify the nominal controller inputs of the model as an
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

### **Kd** — Compensation gain matrix scalar | vector | matrix

Specify the compensation gain matrix *Kd*
as
an*Nu*-by-*Nd*
signal.

#### Dependencies

To enable this port, select **Use external source for matrix
Kd**.
### Output

### **u** — Modified control input scalar

Modified control input, returned as an
*Nu*-by-1 signal, where
*Nu* is the number of inputs in the
model.

### **dhat** — Estimated disturbances vector

Estimated disturbances in the model, returned as an
*Nd*-by-1 signal, where
*Nd* is the number of disturbances in the
model.

#### Dependencies

To enable this port, select **Output estimated disturbances
dhat**.

### **xhat** — Estimated states vector

Estimated states of the model, returned as an
*Nx*-by-1 signal, where
*Nx* is the number of states in the
model.

#### Dependencies

To enable this port, select **Output estimated model states
xhat**.

## Parameters

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

### **Use external source for matrix Kd** — Specify compensation gain matrix at block input port `off` (default) | `on`

Select this option to specify the observer matrix using the block input port
**Kd**.

### Block Tab

### **Limit output (u)** — Limit block output to specified saturation limits `off` (default) | `on`

Option to limit block output to specified saturation limits. Specify the output
saturation limits using the **Upper limit** and **Lower
limit** parameters.

### **Upper limit** — Upper saturation limit for block output `inf` (default) | scalar

Specify the upper limit for the block output. The block output is held at this
value whenever it would otherwise exceed this value.

#### Dependencies

To enable this parameter, select the **Limit output (u)**
parameter.

### **Lower limit** — Lower saturation limit for block output `–inf` (default) | scalar

Specify the lower limit for the block output. The block output is held at this
value whenever it would otherwise go below this value.

#### Dependencies

To enable this parameter, select the **Limit output (u)**
parameter.

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

### **Output estimated model states xhat** — Output estimated states at block output port `off` (default) | `on`

Select this option to output estimated model states at the block output
**xhat**.

### **Output estimated model states dhat** — Output estimated disturbances at block output port `off` (default) | `on`

Select this option to output estimated model states at the block output
**dhat**.

## Libraries

Simulink Control Design / Disturbance Observer

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Modify control actions to compensate for unknown dynamics and disturbances

Use the Disturbance Compensator block to modify control actions of a
nominal controller to reject and compensate for disturbances in your model. To compensate for
disturbances, the Disturbance Compensator block uses an extended state observer
to estimate total disturbances in the model and returns the modified controller actions you
can use as plant input.

The block extends the implementation of ESO as follows.

x˙/x+=Ax+Buu+Bddym=Cmxu=u0+Kdd^

Here:

- *x* is the plant states.
- x˙ is the state derivative in continuous time and
  *x+* is the state update
  *x*[*k*+1] in discrete time.
- *A*, *Bu*, and
  *Cm* are the plant dynamics.
- *ym* is the measurable plant output.
- *Bd* is the disturbance input matrix.
- *d* is the total disturbances in the model, including unknown
  dynamics and internal and external disturbances.
- *u* is the modified controller action.
- *u0* is the nominal controller action.
- *Kd* is the compensation gain matrix.

The block does not require you to provide an actual model of the plant. You can specify
the dynamics obtained from a physical representation or an approximation of the plant.
Therefore, the accuracy of disturbance rejection will depend on the accuracy of the plant
approximation you provide.

For more information, see Control Design and Disturbance Compensation Using Extended State Observers.
