---
type: simulink-block
title: 'Luenberger Observer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Observers\u200b'
documentation_page: 'luenbergerobserver'
documentation_source_path: 'ref/luenbergerobserver.html'
language: en
---

# Luenberger Observer

## Ports

### Input

### **u** — Control input vector

Input signal to the system whose state we want to estimate, specified
as a vector.

**Data Types:** `single` | `double`

### **y** — System output vector

Measured output of the system whose state we want to estimate,
specified as a vector.

**Data Types:** `single` | `double`
### Output

### **xhat** — State estimate vector

Estimate of the state of the system, specified as a vector.

**Data Types:** `single` | `double`

## Parameters

### **State-space parameterization** — State-space parameterization `Discrete-time` (default) | `Continuous-time`

Select the strategy for parameterizing the state-space matrices and
desired poles for the observer. The block implementation is discrete
regardless of this parameterization.

### **Discrete A matrix** — A matrix in discrete time 1 (default) | real scalar or matrix

State matrix of the discrete-time state-space model. The A matrix must be
square, with the number of rows and columns equal to the order of the
system.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Discrete-time`.

### **Discrete B matrix** — B matrix in discrete time 1 (default) | real scalar or matrix

Input matrix of the discrete-time state-space model. The B matrix must
have the number of rows equal to the order of the system, and the number of
columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Discrete-time`.

### **Discrete C matrix** — C matrix in discrete time 1 (default) | real scalar or matrix

Output matrix of the discrete-time state-space model. The C matrix must
have the number of rows equal the number of outputs of the system, and the
number of columns equal to the order of the system.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Discrete-time`.

### **Discrete D matrix** — D matrix in discrete time 1 (default) | real scalar or matrix

Feedthrough matrix of the discrete-time state-space model. The D matrix
must have the number of rows equal to the number of system outputs, and the
number of columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Discrete-time`.

### **Continuous A matrix** — A matrix in continuous time 1 (default) | real scalar or matrix

State matrix of the continuous-time state-space model. The A matrix must
be square, with the number of rows and columns equal to the order of the
system.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Continuous-time`.

### **Continuous B matrix** — B matrix in continuous time 1 (default) | real scalar or matrix

Input matrix of the continuous-time state-space model. The B matrix must
have the number of rows equal to the order of the system, and the number of
columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Continuous-time`.

### **Continuous C matrix** — C matrix in continuous time 1 (default) | real scalar or matrix

Output matrix of the continuous-time state-space model. The C matrix must
have the number of rows equal the number of outputs of the system, and the
number of columns equal to the order of the system.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Continuous-time`.

### **Continuous D matrix** — D matrix in continuous time 1 (default) | real scalar or matrix

Feedthrough matrix of the continuous-time state-space model. The D matrix
must have the number of rows equal to the number of system outputs, and the
number of columns equal to the number of system inputs.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Continuous-time`.

### **Observer design** — State-space parameterization `Desired eigenvalues` (default) | `Observer gain`

Select the strategy for parameterizing observer gain.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Discrete-time`.

### **Observer gain** — Observer gain 1 (default) | real scalar or matrix

Specify the observer gain that puts all eigenvalues of the matrix
*Ad-LdCd*
inside the unit circle. The gain matrix must have the number of rows equal
to number of system inputs and the number of columns equal to the order of
the system.

#### Dependencies

To enable this parameter, set:

- **State-space parameterization** to
  `Discrete-time`.
- **Observer design** to `Observer
  gain`.

### **Desired eigenvalues** — Observer eigenvalues 0 (default) | real vector

Specify the location of the eigenvalues:

- To have negative real part if **State-space
  parameterization** is set to
  `Continuous-time`. In this case,
  the eigenvalues of the continuous-time system are approximated
  to the discrete ones based on the **Discretization
  sample time**.
- To lie within the unit circle if **State-space
  parameterization** is set to
  `Discrete-time`.

The Observer gain is then calculated based on these
eigenvalues. The size of the vector should be the same as the system
order.

### **Initial conditions** — Initial conditions 0 (default) | real vector with length equal to system order

Select the initial condition of each state.

### **Discretization sample time** — Discretization sample time 0.1 (default) | positive real number

Value used to discretize the state space matrices and also approximate the
discrete-time eigenvalues.

#### Dependencies

To enable this parameter, set **State-space
parameterization** to
`Continuous-time`.

### **Sample time** — Sample time 0.1 (default) | -1 or positive real number

Value used to simulate the dynamics of the model. Choose the same value as
**Discretization sample time**, unless the block is
placed within a triggered subsystem, in which case you must set it to
-1.

## Libraries

Simscape / Electrical / Control / Observers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time Luenberger observer

The Luenberger Observer block implements a discrete time Luenberger
observer. Use this block to estimate the states of an observable system using:

- The discrete inputs and outputs of the system.
- A discrete state-space representation of the system.

The Luenberger Observer is also sometimes referred to as a state
observer or simply an observer.

You can control multi-input, multi-output systems by passing the output state vector
of this block to a State Feedback Controller block.

### Defining Equations

The block implements a discrete time Luenberger Observer using the backward Euler
method due to its simplicity and stability.

The estimator is given by this difference equation:

x^(k+1) =Adx^(k) +Bdu(k) + Ld(y(k) −y^(k)),

where:

- x^(k) is the
  *k*th estimated state
  vector.
- y^(k) is the
  *k*th estimated output
  vector.
- *u(k)* is the
  *k*th input
  vector.
- *y(k)* is the
  *k*th measured output
  vector.
- *Ad* is the discretized state
  matrix.
- *Bd* is the discretized input
  matrix.
- *Ld* is the discretized
  observer gain matrix.

The dynamics of the estimation error are described by:

e(k+1)=(Ad−LdCd)e(k),

where:

- *e(k)* is the
  *k*th error
  vector.
- *Cd* is the output
  matrix.

The estimation error converges to zero when
*Ad-LdCd*
has its eigenvalues inside the unit circle. Therefore, the value of
*Ld* should be such that this goal
is achieved. The block computes the observer gain by solving

LdT=GX−1,

where *G* is an arbitrary matrix and
*X* is obtained by solving the Sylvester equation:

AdTX−XΛ=CdTG.

Here, *Λ* is a matrix with the desired
eigenvalues, which are not the same as the eigenvalues of
*Ad*. This diagram shows the basic
structure of a discrete time Luenberger Observer.

### Assumptions

The system is observable, which is true if the state of the system can be
determined from the input and output in a finite time. Mathematically, this means
that the system observability matrix has full rank.

### Limitations

The desired eigenvalues are not the same as the eigenvalues of the open-loop
model.
