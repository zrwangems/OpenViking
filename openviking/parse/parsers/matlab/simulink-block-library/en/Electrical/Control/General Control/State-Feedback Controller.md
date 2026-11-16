---
type: simulink-block
title: 'State-Feedback Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'statefeedbackcontroller'
documentation_source_path: 'ref/statefeedbackcontroller.html'
language: en
---

# State-Feedback Controller

## Ports

### Input

### **r** — Plant reference scalar

Plant system reference signal.

**Data Types:** `single` | `double`

### **x** — State vector vector

Measured or estimated system state vector.

**Data Types:** `single` | `double`

### **Reset** — Integrator reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `Boolean`

### **y** — Plant output scalar

Plant system output signal.

**Data Types:** `single` | `double`
### Output

### **u** — Controller output scalar

Control system output signal.

**Data Types:** `single` | `double`

## Parameters

### **State-feedback design** — Controller generation `State-feedback gain` (default) | `Desired eigenvalues`

Select the strategy for parameterizing controller gain:

- `State-feedback gain` — Specify the
  controller gain directly
- `Desired eigenvalues` — Specify the
  plant model and desired eigenvalues from which to generate the
  controller gain

### **State-feedback parameterization** — State-feedback parameterization `Discrete-time` (default) | `Continuous-time`

Select the strategy for parameterizing the state-space matrices and
desired poles for the controller. The block implementation is discrete
regardless of this parameterization.

#### Dependencies

To enable this parameter, set **State-feedback
design** to `Desired
eigenvalues`.

### **Controller matrix** — Controller matrix [1 1] (default) | matrix

Controller feedback matrix. To determine the controller matrix, if you
have a license for Control System Toolbox™, use the `lqr` or `lqi`
function.

#### Dependencies

To enable this parameter, set **State-feedback
design** to `State-feedback
gain`.

### **Discrete-time A matrix** — A matrix in discrete time 1 (default) | real scalar or matrix

State matrix of the discrete-time state-space model. The A matrix must be
square, with the number of rows and columns equal to the order of the
system.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Discrete-time`.

### **Discrete-time B matrix** — B matrix in discrete time 1 (default) | real scalar or matrix

Input matrix of the discrete-time state-space model. The B matrix must
have the number of rows equal to the order of the system, and the number of
columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Discrete-time`.

### **Discrete-time C matrix** — C matrix in discrete time 1 (default) | real scalar or matrix

Output matrix of the discrete-time state-space model. The C matrix must
have the number of rows equal the number of outputs of the system, and the
number of columns equal to the order of the system.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Discrete-time`.

### **Discrete-time D matrix** — D matrix in discrete time 1 (default) | real scalar or matrix

Feedthrough matrix of the discrete-time state-space model. The D matrix
must have the number of rows equal to the number of system outputs, and the
number of columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Discrete-time`.

### **Continuous-time A matrix** — A matrix in continuous time 1 (default) | real scalar or matrix

State matrix of the continuous-time state-space model. The A matrix must
be square, with the number of rows and columns equal to the order of the
system.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Continuous-time`.

### **Continuous-time B matrix** — B matrix in continuous time 1 (default) | real scalar or matrix

Input matrix of the continuous-time state-space model. The B matrix must
have the number of rows equal to the order of the system, and the number of
columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Continuous-time`.

### **Continuous-time C matrix** — C matrix in continuous time 1 (default) | real scalar or matrix

Output matrix of the continuous-time state-space model. The C matrix must
have the number of rows equal the number of outputs of the system, and the
number of columns equal to the order of the system.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Continuous-time`.

### **Continuous-time D matrix** — D matrix in continuous time 1 (default) | real scalar or matrix

Feedthrough matrix of the continuous-time state-space model. The D matrix
must have the number of rows equal to the number of system outputs, and the
number of columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Continuous-time`.

### **Discretization sample time** — Discretization sample time 0.1 (default) | positive real number

Value used to discretize the state space matrices and also approximate the
discrete-time eigenvalues.

#### Dependencies

To enable this parameter, set **State-feedback
parameterization** to
`Continuous-time` and **Sample time
(-1 for inherited)** to `-1`.

### **Desired eigenvalues (discrete)** — Observer eigenvalues 0 (default) | real vector

Specify the location of the eigenvalues to lie within the unit circle. The
controller gain is then calculated based on these eigenvalues. The size of
the vector must be equal to the system order plus the number of
outputs.

### **Control action upper limit** — *umax* `5` (default) | scalar greater than the value of the **Control action lower limit** parameter

Upper limit for the control output signal.

### **Control action lower limit** — *umin* `0` (default) | scalar

Lower limit for the control output signal.

### **Sample time (-1 for inherited)** — Sampling interval `-1` (default) | default value or a positive number

Time interval between samples. If the block is
inside a triggered subsystem, inherit the sample time by setting this
parameter to `-1`. If this block is in a continuous
variable-step model, specify the sample time explicitly. For more
information, see What Is Sample Time? and
Specify Sample Time.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time state-feedback controller with integral action

The State-Feedback Controller block implements a discrete-time
state-feedback controller with integral action. Use this block to control linear systems
with single or multiple inputs and single or multiple outputs. The integral action
serves to eliminate steady-state error in the controlled outputs. You can define the
controller using a precomputed optimal gain or use the state-space model of your system
to generate this gain using pole placement.

### Equations

The integral of the tracking error, *xi*,
is an additional state that ensures zero steady-state error for the closed-loop
system. The extended state vector is

xe=[xxi],

Where:

- *x* is the state vector.
- *xi* is the integral of the
  tracking error.
- *xe* is the extended state
  vector.

Therefore, the control action is

u=Kxe,

Where:

- *K* is the feedback matrix, that is, the pole
  placement.
- *u* is the controller output.

### Assumptions

System state measurement and estimation occur outside the controller.
