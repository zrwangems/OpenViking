---
type: simulink-block
title: 'Kalman Filter'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Online Estimation / Online State Estimation'
documentation_page: 'kalmanfilter'
documentation_source_path: 'ref/kalmanfilter.html'
language: en
---

# Kalman Filter

## Ports

### Input

### **u** — Known inputs scalar | vector

Known inputs `u(t)` or
`u[k]`.

#### Dependencies

To enable this port, select the **Add input port
u** parameter. This parameter is selected by
default.

### **y** — Measured outputs scalar | vector

Measured output `y[n]` to update the estimated
states.

### **A** — State matrix real matrix

*n*-by-*n* state (or system)
matrix.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input Port**.

### **B** — Input matrix real matrix

*n*-by-*p* input matrix.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input Port** and select the
**Add input port u** parameter.

### **C** — Output matrix real matrix

*q*-by-*p* output matrix.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input Port**.

### **D** — Feedthrough matrix real matrix

*q*-by-*p* feedthrough (or
feedforward) matrix. In cases where the system model does not have a
direct feedthrough, **D** is the zero matrix.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input Port** and select the
**Add input port u** parameter.

### **G** — Measured outputs real matrix

Noise transformation in the state-space equation.

#### Dependencies

To enable this port, select **Use G and H matrices
(default G=I and H=0)** parameter.

### **H** — Measured outputs real matrix

Noise transformation in the state-space equation.

#### Dependencies

To enable this port, select **Use G and H matrices
(default G=I and H=0)** parameter.

### **Q** — Process noise covariance matrix scalar | vector | matrix

Process noise covariance matrix, specified as one of the
following:

- Real nonnegative scalar. **Q** is an
  *Nw*-by-*Nw* diagonal
  matrix with the scalar on the diagonals. *Nw*
  is the number of process noise inputs in the model.
- Vector of real nonnegative scalars. **Q** is
  an *Nw*-by-*Nw* diagonal
  matrix with the elements of the vector on the diagonals of
  **Q**.
- *Nw*-by-*Nw* positive
  semi-definite matrix.

#### Dependencies

To enable this port, deselect the **Time-invariant
Q** parameter.

### **R** — Measurement noise covariance matrix scalar | vector | matrix

Measurement noise covariance matrix, specified as one of the
following:

- Real positive scalar. **R** is an
  *Ny*-by-*Ny* diagonal
  matrix with the scalar on the diagonals. *Ny*
  is the number of measured outputs in the model.
- Vector of real positive scalars. **R** is an
  *Ny*-by-*Ny* diagonal
  matrix with the elements of the vector on the diagonals of
  **R**.
- *Ny*-by-*Ny*
  positive-definite matrix.

#### Dependencies

To enable this port, deselect the **Time-invariant
R** parameter.

### **N** — Process and measurement noise cross-covariance matrix scalar | vector | matrix

Process and measurement noise cross-covariance matrix, specified as a
*Nw*-by-*Ny* matrix. The matrix [Q
N; NT R] must be positive definite.

#### Dependencies

To enable this port, deselect the **Time-invariant
N** parameter.

### **P0** — Initial state estimation error covariance scalar | vector | matrix

**P** matrix at the initial time.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input Port** and set the
**Source** parameter to **Input
Port**.

### **X0** — Initial state estimates scalar | vector

Estimated states at the initial time.

#### Dependencies

To enable this port, set the **Source** parameter
to **Input Port**.

### **Enable** — Control signal to enable measurement updates scalar

This port controls the measurement updates and takes a scalar
signal.

#### Dependencies

To enable this port, select **Add input port Enable to
control measurement updates** parameter.

### **Reset** — Control signal to reset state estimates scalar

Control signal to reset estimated states and the parameter covariance
matrix using specified initial values. See External Reset for
more information on when a reset is triggered.

#### Dependencies

To enable this port, set the **External reset**
parameter to any value other than **None**.
### Output

### **xhat** — Estimated states scalar | vector

Estimated states of the linear system.

### **yhat** — Estimated outputs scalar | vector

Estimated outputs of the linear system.

#### Dependencies

To enable this port, select **Output estimated model
output y** parameter.

### **Z** — State estimation error covariance matrix

Add **Z** output port to the block.

To enable this port, select **Output state estimation error
covariance Z** parameter.

#### Dependencies

To enable this port, set the **Time domain**
parameter to **Discrete-Time** and select
**Use the current measurement y[n] to improve
xhat[n]** parameter.

### **P** — State estimation error covariance matrix

Add **P** output port to the block.

To enable this port, select **Output state estimation error
covariance P** parameter.

#### Dependencies

To enable this port, set the **Time domain**
parameter to **Continuous-Time** or set the
**Time domain** parameter to
**Discrete-Time** and deselect **Use
the current measurement y[n] to improve xhat[n]**
parameter.

**Note**

- All input ports except **Enable** and
  **Reset** must have the same data type (single or
  double).
- **Enable** and **Reset** ports
  support `single`, `double`,
  `int8`, `uint8`,
  `int16`, `uint16`,
  `int32`, `uint32`, and boolean
  data types.

## Parameters

### Filter Settings

### **Time domain** — Specify whether to estimate continuous-time or discrete-time states `Discrete-Time` (default) | `Continuous-Time`

- `Discrete-Time` (default) —
  Block estimates discrete-time states.
- `Continuous-Time` — Block
  estimates continuous-time states.

  When the Kalman Filter block is in a model with
  synchronous state control (see the State Control (HDL Coder)
  block), you cannot select
  **Continuous-Time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeDomain` |
| **Type:** string, character vector |
| **Values:** `"Discrete-Time"` | `"Continuous-Time"` |
| **Default:** `"Discrete-Time"` |

### **Use the current measurement y[n] to improve xhat[n]** — Update output state estimates using the measure outputs `on` (default) | `off`

Use the current estimator variant of the discrete-time Kalman filter.
When this parameter is not selected, the delayed estimator (variant) is
used.

This parameter is available only when **Time domain**
is **Discrete-Time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseCurrentEstimator` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Sample Time** — Block sample time `-1` (default) | `non-negative scalar`

Block sample time, specified as `-1` or a positive
scalar.

The default value is `-1`, which implies that the
block inherits its sample time based on the context of the block within
the model. All block input ports must have the same sample time.

#### Dependencies

This parameter is available only when **Time
domain** is **Discrete-Time** and
**Model source** is **Individual A, B,
C, D matrices** or **Input port**.
When **Model source** is **LTI State-Space
Variable**, the block takes its sample time from the
LTI state-space variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** string, character vector |
| **Values:** `"-1"` | scalar |
| **Default:** `"-1"` |

### Model Parameters

#### System Model

### **Model source** — Specify how the A, B, C, D matrices are provided to the block `LTI State-Space Variable` (default) | `Individual A, B, C, D matrices` | `Input port`

- `LTI State-Space
  Variable` — Use the model specified in
  **Variable**. The default value is
  `ss(0.95,1,1,0)`. The sample time of the
  model must match the **Time domain** parameter;
  that is, the model must be discrete-time if **Time
  domain** is discrete-time.
- `Individual A, B, C, D matrices`
  — Specify the **A**,
  **B**, **C**, and
  **D** in the block parameters.
- `Input port`
  — Specify the **A**,
  **B**, **C**,
  **D** matrices as input signals to the
  Kalman Filter block. If you select this option, the block
  includes additional input ports **A**,
  **B**, **C**,
  **D**. You must also specify
  **Number of states**, **Number of
  inputs**, and **Number of
  outputs** in the block parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ModelSource` |
| **Type:** string, character vector |
| **Values:** `"LTI State-Space Variable"` | `"Individual A, B, C, D matrices"` | `"Input port"` |
| **Default:** `"LTI State-Space Variable"` |

### **A** — State Matrix `0.95` (default)

Specify the **A** matrix. It must be real and square.
The default value is `0.95`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Individual A, B, C, D
matrices**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** string, character vector |
| **Values:** `"real matrix"` |
| **Default:** `"0.95"` |

### **B** — Input Matrix `1` (default)

Specify the **B** matrix. It must be real and have as
many rows as the **A** matrix. The default value is
`1`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Individual A, B, C, D
matrices**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** string, character vector |
| **Values:** `"real matrix"` |
| **Default:** `"1"` |

### **C** — Output Matrix `1` (default)

Specify the **C** matrix. It must be real and have as
many columns as the **A** matrix. The default value is
`1`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Individual A, B, C, D
matrices**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** string, character vector |
| **Values:** `"real matrix"` |
| **Default:** `"1"` |

### **D** — Feedthrough Matrix `0` (default)

Specify the **D** matrix. It must be real and must
have as many rows as the **C** matrix and as many
columns as the **B** matrix. The default value is
`0`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Individual A, B, C, D
matrices**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** string, character vector |
| **Values:** `"real matrix"` |
| **Default:** `"0"` |

### **Number of states** — Number of states to be estimated `1` (default) | `non-negative scalar`

Number of states to be estimated, specified as a positive integer. The
default value is `1`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfStates` |
| **Type:** string, character vector |
| **Values:** `"1"` | `scalar` |
| **Default:** `"1"` |

### **Number of inputs** — Number of known inputs `1` (default) | `non-negative scalar`

Number of known inputs in the model, specified as a positive integer.
The default value is `1`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfInputs` |
| **Type:** string, character vector |
| **Values:** `"1"` | `scalar` |
| **Default:** `"1"` |

### **Number of outputs** — Number of measured output `1` (default) | `non-negative scalar`

Number of measured outputs in the model, specified as a positive
integer. The default value is `1`.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfOutputs` |
| **Type:** string, character vector |
| **Values:**`"1"` | `scalar` |
| **Default:** `"1"` |

#### Initial Estimates

### **Source** — Specify how to enter the initial state estimates and initial state estimation error covariance `Dialog` (default) | `Input port`

- `Dialog` — Specify the values
  directly in the dialog boxes.
- `Input port` — Inherit the
  values from input ports. The default is `10`.
  The block includes an additional input port
  **X0**. A second additional input port
  **P0** is added when time-varying Kalman
  filter is used. **X0** and
  **P0** must satisfy the same conditions as
  the parameters Initial states x[0] and State estimation error
  covariance P[0], respectively.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialEstimateSource` |
| **Type:** string, character vector |
| **Values:** `"Dialog"` | `"Input port"` |
| **Default:** `"Dialog"` |

### **Initial states x[0]** — Specify the initial state estimate `0` (default) | `scalar` | `vector`

Specify the initial state estimate as a real scalar or vector. If you
specify a scalar, all initial state estimates are set to this scalar. If
you specify a vector, the length of the vector must match with the
number of states in the model. The default is
`0`.

#### Dependencies

To enable this port, set the **Source** parameter
to **Dialog**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `X0` |
| **Type:** string, character vector |
| **Values:** `"0"` | `scalar` | `vector` |
| **Default:** `"0"` |

### **State estimation error covariance P[0]** — Specify the initial state estimation error covariance `10` (default) | `scalar` | `vector` | `matrix`

Specify the initial state estimation error covariance P[0] for a
discrete-time Kalman filter or P(0) for continuous-time. This parameter
must be specified as one of the following:

- Real nonnegative scalar. **P** is an
  *Ns*-by-*Ns* diagonal
  matrix with the scalar on the diagonals. *Ns*
  is the number of states in the model.
- Vector of real nonnegative scalars. **P** is
  an *Ns*-by-*Ns* diagonal
  matrix with the elements of the vector on the diagonals of
  **P**.
- *Ns*-by-*Ns* positive
  semi-definite matrix.

#### Dependencies

To enable this port, set the **Model source**
parameter to **Input port** and
**Source** parameter to
**Dialog**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `P0` |
| **Type:** string, character vector |
| **Values:** `"10"` | `scalar` | `vector` | `matrix` |
| **Default:** `"10"` |

#### Noise Characteristics

### **Use the Kalman Gain K from the model variable** — Specify whether to use pre-identified Kalman Gain contained in state-space plant model `off` (default) | `on`

Specify whether to use the pre-identified Kalman Gain present in the
state-space model specified by **Variable**.

#### Dependencies

To enable this parameter, you must meet the following
conditions:

- The **Model source** is set to
  **LTI State-Space Variable** and
  **Variable** is an identified
  state-space model (`idss`) with a
  nonzero **K** matrix.
- Select the **Time Invariant Q**,
  **Time Invariant R**, and
  **Time Invariant N** parameters.
- If the **Use G and H matrices (default G=I and
  H=0)**  parameter is selected, the
  **Time Invariant G** and **Time
  Invariant H** parameters must also be
  selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseK` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Use G and H matrices (default G=I and H=0)** — Specify whether to use non-default values for G and H matrices `off` (default) | `on`

By default `G=I` and `H=0`. If you
select this option, you must specify **G** and
**H** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseGH` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **G** — Specify the G matrix `1` (default) | `non-negative scalar` | `vector` | `matrix`

It must be a real matrix with as many rows as the
**A** matrix. The default value is
`1`.

#### Dependencies

To enable this parameter, select **Use G and H matrices
(default G=I and H=0)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `G` |
| **Type:** string, character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `"1"` |

### **Time-invariant G** — Specify the G matrix is time invariant `on` (default) | `off`

If you unselect this option, the block includes an additional input
port **G**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeInvariantG` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **H** — Specify the H matrix `0` (default) | `non-negative scalar` | `vector` | `matrix`

It must be a real matrix with as many rows as the
**C** matrix and as many columns as the
**G** matrix. The default value is
`0`.

#### Dependencies

To enable this parameter, select **Use G and H matrices
(default G=I and H=0)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `H` |
| **Type:** string, character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `"0"` |

### **Time-invariant H** — Specify the H matrix is time invariant `on` (default) | `off`

If you unselect this option, the block includes an additional input
port **H**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeInvariantH` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Number of process noise inputs** — Process noise inputs `1` (default) | `non-negative scalar`

Specify the number of process noise inputs in the model. The default
value is `1`.

#### Dependencies

This parameter is available only when **Time-invariant
G** and **Time-invariant H** are
deselected. Otherwise, this information is inferred from the
**G** or **H** matrix.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfProcessNoiseInputs` |
| **Type:** string, character vector |
| **Values:** scalar |
| **Default:** `"1"` |

### **Q** — Process noise covariance matrix `0.05` (default) | `non-negative scalar` | `vector` | `matrix`

Specified as one of the following:

- Real nonnegative scalar. **Q** is an
  *Nw*-by-*Nw* diagonal
  matrix with the scalar on the diagonals. *Nw*
  is the number of process noise inputs in the model.
- Vector of real nonnegative scalars. **Q** is
  an *Nw*-by-*Nw* diagonal
  matrix with the elements of the vector on the diagonals of
  **Q**.
- *Nw*-by-*Nw* positive
  semi-definite matrix.

#### Dependencies

To enable this parameter, select the **Time-invariant
Q** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Q` |
| **Type:** string, character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `"0.05"` |

### **Time-invariant Q** — Specify if Q matrix is time invariant `on` (default) | `off`

If you deselect this parameter, the block includes an additional
input port **Q**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeInvariantQ` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **R** — Measurement noise covariance matrix `1` (default) | `non-negative scalar` | `vector` | `matrix`

Specified as one of the following:

- Real positive scalar. **R** is an
  *Ny*-by-*Ny* diagonal
  matrix with the scalar on the diagonals. *Ny*
  is the number of measured outputs in the model.
- Vector of real positive scalars. **R** is an
  *Ny*-by-*Ny* diagonal
  matrix with the elements of the vector on the diagonals of
  **R**.
- *Ny*-by-*Ny*
  positive-definite matrix.

#### Dependencies

To enable this parameter, select the **Time-invariant
R** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `R` |
| **Type:** string, character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `"1"` |

### **Time-invariant R** — Specify if R matrix is time invariant `on` (default) | `off`

If you deselect this parameter, the block includes an additional
input port **R**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeInvariantR` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **N** — Process and measurement noise cross-covariance matrix `0` (default) | `non-negative scalar` | `vector` | `matrix`

Specify this parameter as a
*Nw*-by-*Ny* matrix. The matrix [Q
N; NT R] must be positive definite.

#### Dependencies

To enable this parameter, select the **Time-invariant
N** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `N` |
| **Type:** string, character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `"0"` |

### **Time-invariant N** — Specify if N matrix is time invariant `on` (default) | `off`

If you deselect this parameter, the block includes an additional
input port **N**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeInvariantN` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### Options

#### Additional Inports

### **Add input port u** — Specify if model contains known inputs `on` (default) | `off`

Select this option if your model contains known inputs
`u(t)` or `u[k]`. The parameter is
selected by default. Deselecting this parameter removes the input port
**u** from the block and removes the
**B**, **D** and **Number
of inputs** parameters from the block dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AddInputPort` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Add input port Enable to control measurement updates** — Control the measurement updates `off` (default) | `on`

Select this option if you want to control the measurement updates. The
block includes an additional inport **Enable**. The
**Enable** input port takes a scalar signal. This
parameter is not selected by default.

By default the block does measurement updates at each time step to
improve the state and output estimates x^ and y^ based on measured outputs. The measurement update is
skipped for the current sample time when the signal in the
**Enable** port is `0`.
Concretely, the equation for state estimates become x^˙(t)=A(t)x^(t)+B(t)u(t) for a continuous-time Kalman filter and x^[n+1|n]=A[n]x^[n|n−1]+B[n]u[n] for discrete-time.

**Note**

Enabling the **Enable** port allows measurement
updates to be controlled. By default, Kalman Filter
does the measurement updates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AddEnablePort` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **External Reset** — Option to reset estimated states and parameter covariance matrix using specified initial values `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

This parameter helps control when the block is reset. Suppose you
reset the block at a time step, `t`. If the block is
enabled at `t`, the software uses the initial parameter
values specified either in the block dialog or the input ports
**P0** and **X0** to estimate the
states. In other words, at `t`, the block performs a
time update and, if it is enabled, a measurement update after the reset.
The block outputs these updated estimates.

Specify one of the following:

- `None` (Default) — Estimated
  states x^ and state estimation error covariance matrix
  **P** values are not reset.
- `Rising` — Triggers a reset
  when the control signal rises from a negative or zero value to a
  positive value. If the initial value is negative, rising to zero
  triggers a reset.
- `Falling` — Triggers a reset
  when the control signal falls from a positive or zero value to a
  negative value. If the initial value is positive, falling to
  zero triggers a reset.
- `Either` — Triggers a reset
  when the control signal is either rising or falling.
- `Level` — Triggers a reset in
  either of these cases:

  - The control signal is nonzero at the current time
    step.
  - The control signal changes from nonzero at the
    previous time step to zero at the current time
    step.
- `Level hold` — Triggers reset
  when the control signal is nonzero at the current time
  step.

When you choose an option other than `None`,
a **Reset** input port is added to the block to provide
the reset control input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExternalReset` |
| **Type:** string, character vector |
| **Values:** `"None"` | `"Rising"` | `"Falling"` | `"Either"` | `"Level"` | `"Level hold"` |
| **Default:** `"None"` |

#### Additional Outports

### **Output estimated model output y** — Include estimated model outputs `off` (default) | `on`

Add a y^ output port to the block to output the estimated model
outputs. The parameter is not selected by default.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputEstimatedY` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Output state estimation error covariance Z** — Add Z output port to the block `off` (default) | `on`

Add a **Z** output port to the block. The
**Z** matrix is provided only when **Time
domain** is **Discrete-Time** and the
**Use the current measurement y[n] to improve
xhat[n]** parameter is selected. Otherwise, the
**P** matrix, as described in the Algorithms
section, is provided.

This parameter is not selected by default.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputZ` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Output state estimation error covariance P** — Add P output port to the block `off` (default) | `on`

Add a **P** output port to the block. This parameter
is not selected by default.

#### Dependencies

To enable this port, set the **Time domain**
parameter to **Continuous-Time** or set the
**Time domain** parameter to
**Discrete-Time** and deselect **Use
the current measurement y[n] to improve xhat[n]**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputP` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

## Libraries

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2014b**

### R2021a: Kalman Filter block: Numerical changes

Starting in 2021a, numerical improvements in the algorithms used by the
Kalman Filter block might produce results that are different from
the results you obtained using previous versions.

## Description

Estimate states of discrete-time or continuous-time linear system

Use the Kalman Filter block to estimate states of a state-space plant
model given process and measurement noise covariance data. The state-space model can be
time-varying. A steady-state Kalman filter implementation is used if the state-space
model and noise covariance matrices are all time-invariant, and a time-varying Kalman
filter is used otherwise.

A Kalman filter provides the optimal solution to the continuous or discrete estimation
problems in Continuous-Time Estimation and Discrete-Time Estimation.

The Kalman Filter block differs from the `kalman` (Control System Toolbox) command in the following ways:

- When you call `kalman(sys,...)`, it assumes that
  `sys` includes the `G` and
  `H` matrices. Specifically, `sys.B` is of
  the form `[B G]` and `sys.D` is of the form
  `[D H]`. When you provide a LTI variable to the
  Kalman Filter block, it does not assume that the LTI variable
  provided contains `G` and `H`. They are
  optional and separate.
- The filter created by the `kalman` command outputs
  `[yhat;xhat]` by default. The block outputs only
  `xhat` by default.
- The `Kalman` command can output both `P`
  and `Z` covariance matrices for discrete-time systems. The
  block can only output `P` or `Z` for such
  systems.
