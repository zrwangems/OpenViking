---
type: simulink-block
title: 'Extended Kalman Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / State-Space Control Design and Estimation / State Estimation'
documentation_page: 'ekf_block'
documentation_source_path: 'ref/ekf_block.html'
language: en
---

# Extended Kalman Filter

## Ports

### Input

### **y1,y2,y3,y4,y5** — Measured system outputs vector

Measured system outputs corresponding to each measurement function
that you specify in the block. The number of ports equals the number
of measurement functions in your system. You can specify up to five
measurement functions. For example, if your system has two sensors,
you specify two measurement functions in the block. The first port **y1** is
available by default. When you click **Apply**,
the software generates port **y2** corresponding
to the second measurement function.

Specify the ports as *N*-dimensional vectors,
where *N* is the number of quantities measured by
the corresponding sensor. For example, if your system has one sensor
that measures the position and velocity of an object, then there is
only one port **y1**. The port is specified as a
2-dimensional vector with values corresponding to position and velocity.

#### Dependencies

The first port **y1** is available by default.
Ports **y2** to **y5** are generated
when you click **Add Measurement**, and click **Apply**.

**Data Types:** `single` | `double`

### **StateTransitionFcnInputs** — Additional optional input argument to state transition function scalar | vector | matrix

Additional optional input argument to the state transition function
`f` other than the state `x` and
process noise `w`. For information about state
transition functions see, State Transition and Measurement Functions.

Suppose that your system has nonadditive process noise, and the state
transition function `f` has the following form:

`x(k+1) =
f(x(k),w(k),StateTransitionFcnInputs)`

Here `k` is the time step, and
`StateTransitionFcnInputs` is an additional input
argument other than `x` and
`w`.

If you create `f` using a MATLAB® function (`.m` file), the software
generates the port **StateTransitionFcnInputs** when
you click **Apply**. You can specify the inputs to
this port as a scalar, vector, or matrix.

If your state transition function has more than one additional input,
use a Simulink Function (Simulink) block to
specify the function. When you use a Simulink Function
block, you provide the additional inputs directly to the Simulink
Function block using Inport (Simulink) blocks. No input
ports are generated for the additional inputs in the Extended
Kalman Filter block. For an example, see Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox).

#### Dependencies

This port is generated only if both of the following conditions
are satisfied:

- You specify `f` in
  **Function** using a MATLAB function, and `f` is on the
  MATLAB path.
- `f` requires only one additional input
  argument apart from `x` and
  `w`.

**Data Types:** `single` | `double`

### **MeasurementFcn1Inputs,MeasurementFcn2Inputs,MeasurementFcn3Inputs,MeasurementFcn4Inputs,MeasurementFcn5Inputs** — Additional optional input argument to each measurement function scalar | vector | matrix

Additional optional inputs to the measurement functions other than the
state `x` and measurement noise `v`.
For information about measurement functions see, State Transition and Measurement Functions.

**MeasurementFcn1Inputs** corresponds to the first
measurement function that you specify, and so on. For example, suppose
that your system has three sensors and nonadditive measurement noise,
and the three measurement functions `h1`,
`h2`, and `h3` have the following
form:

`y1[k] = h1(x[k],v1[k],MeasurementFcn1Inputs)`

`y2[k] = h2(x[k],v2[k],MeasurementFcn2Inputs)`

`y3[k] = h3(x[k],v3[k])`

Here `k` is the time step, and
`MeasurementFcn1Inputs` and
`MeasurementFcn2Inputs` are the additional input
arguments to `h1` and `h2`.

If you specify `h1`, `h2`, and
`h3` using MATLAB functions (`.m` files) in
**Function**, the software generates ports
**MeasurementFcn1Inputs** and
**MeasurementFcn2Inputs** when you click
**Apply**. You can specify the inputs to these
ports as scalars, vectors, or matrices.

If your measurement functions have more than one additional input,
use Simulink Function (Simulink) blocks
to specify the functions. When you use a Simulink
Function block, you provide the additional inputs directly
to the Simulink Function block using Inport (Simulink) blocks. No input
ports are generated for the additional inputs in the Extended
Kalman Filter block. For an example, see Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox).

#### Dependencies

A port corresponding to a measurement function
`h` is generated only if both of the following
conditions are satisfied:

- You specify `h` in
  **Function** using a MATLAB function, and `h` is on the
  MATLAB path.
- `h` requires only one additional input
  argument apart from `x` and
  `v`.

**Data Types:** `single` | `double`

### **Q** — Time-varying process noise covariance scalar | vector | matrix

Time-varying process noise covariance, specified as a scalar,
vector, or matrix depending on the value of the **Process
noise** parameter:

- **Process noise** is `Additive` —
  Specify the covariance as a scalar, an *Ns*-element vector, or
  an *Ns*-by-*Ns* matrix, where
  *Ns* is the number of states of the system. Specify a
  scalar if there is no cross-correlation between process noise terms, and all the
  terms have the same variance. Specify a vector of length *Ns*,
  if there is no cross-correlation between process noise terms, but all the terms
  have different variances.
- **Process noise** is `Nonadditive` —
  Specify the covariance as a *W*-by-*W* matrix,
  where *W* is the number of process noise terms in the state
  transition function.

#### Dependencies

This port is generated if you specify the process noise covariance
as **Time-Varying**. The port appears when you click **Apply**.

**Data Types:** `single` | `double`

### **R1,R2,R3,R4,R5** — Time-varying measurement noise covariance matrix

Time-varying measurement noise covariances for up to five measurement
functions of the system, specified as matrices. The sizes of the matrices
depend on the value of the **Measurement noise** parameter
for the corresponding measurement function:

- **Measurement noise** is `Additive` —
  Specify the covariance as an *N*-by-*N* matrix,
  where *N* is the number of measurements of the system.
- **Measurement noise** is `Nonadditive` —
  Specify the covariance as a *V*-by-*V* matrix,
  where *V* is the number of measurement noise terms
  in the corresponding measurement function.

#### Dependencies

A port is generated if you specify the measurement noise covariance
as **Time-Varying** for the corresponding measurement
function. The port appears when you click **Apply**.

**Data Types:** `single` | `double`

### **Enable1,Enable2,Enable3,Enable4,Enable5** — Enable correction of estimated states when measured data is available scalar

Suppose that measured output data is not available at all time
points at the port **y1** that corresponds to the
first measurement function. Use a signal value other than `0` at
the **Enable1** port to enable the correction of
estimated states when measured data is available. Specify the port
value as `0` when measured data is not available.
Similarly, if measured output data is not available at all time points
at the port **y*`i`*** for
the *ith* measurement
function, specify the corresponding port **Enable*`i`*** as
a value other than `0`.

#### Dependencies

A port corresponding to a measurement function is generated
if you select **Add Enable port** for that measurement
function. The port appears when you click **Apply**.

**Data Types:** `single` | `double` | `Boolean`
### Output

### **xhat** — Estimated states vector

Estimated states, returned as a vector of size *Ns*, where
*Ns* is the number of states of the system. To access the
individual states, use the Selector (Simulink) block.

When the **Use the current measurements to improve state
estimates** parameter is selected, the block outputs the
corrected state estimate x^[k|k] at
time step `k`, estimated using measured outputs until
time `k`. If you clear this parameter, the block
returns the predicted state estimate x^[k|k−1] for
time `k`, estimated using measured output until a
previous time `k-1`. Clear this parameter if your
filter is in a feedback loop and there is an algebraic loop in your Simulink model.

**Data Types:** `single` | `double`

### **P** — State estimation error covariance matrix

State estimation error covariance, returned as an
*Ns*-by-*Ns* matrix, where *Ns*
is the number of states of the system. To access the individual covariances, use the
Selector (Simulink) block.

#### Dependencies

This port is generated if you select **Output state estimation error
covariance** in the **System Model** tab, and click
**Apply**.

**Data Types:** `single` | `double`

## Parameters

### System Model Tab

#### State Transition

### **Function** — State transition function name `myStateTransitionFcn` (default) | function name

The state transition function calculates the
*Ns*-element state vector of the system at time step
*k*+1, given the state vector at time step
*k*. *Ns* is the number of states
of the nonlinear system. You create the state transition function and
specify the function name in **Function**. For example,
if `vdpStateFcn.m` is the state transition function
that you created and saved, specify **Function** as
`vdpStateFcn`.

The inputs to the function you create depend on whether you specify
the process noise as additive or nonadditive in **Process
noise**.

- **Process noise** is
  `Additive` — The state
  transition function *f* specifies how the
  states evolve as a function of state values at previous time
  step:

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`,

  where `x(k)` is the estimated state at time
  `k`, and `Us1,...,Usn` are
  any additional input arguments required by your state transition
  function, such as system inputs or the sample time. To see an
  example of a state transition function with additive process
  noise, type `edit vdpStateFcn` at the
  command line.
- **Process noise** is
  `Nonadditive` — The state
  transition function also specifies how the states evolve as a
  function of the process noise `w`:

  `x(k+1) =
  f(x(k),w(k),Us1(k),...,Usn(k))`.

For more information, see State Transition and Measurement Functions.

You can create *f* using a Simulink Function (Simulink) block or
as a MATLAB function (`.m` file).

- You can use a MATLAB function only if *f* has one
  additional input argument `Us1` other than
  `x` and `w`.

  `x(k+1) = f(x(k),w(k),Us1(k))`

  The software generates an additional input port
  **StateTransitionFcnInputs** to specify
  this argument.
- If you are using a Simulink Function block,
  specify `x` and `w` using
  Argument Inport (Simulink)
  blocks and the additional inputs `Us1,...,Usn`
  using Inport (Simulink) blocks in
  the Simulink Function block. The
  **Argument name** parameter of the Argument Inport (Simulink)
  and Argument
  Outport (Simulink) blocks in the Simulink
  Function block must be different from each other.
  You do not provide `Us1,...,Usn` to the
  Extended Kalman Filter block. For an example,
  see Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateTransitionFcn` |
| **Type:** character vector, string |
| **Default:**`'myStateTransitionFcn'` |

### **Jacobian** — Jacobian of state transition function `off` (default) | `on`

Jacobian of state transition function *f*, specified
as one of the following:

- `off` — The software computes the
  Jacobian numerically. This computation may increase processing
  time and numerical inaccuracy of the state estimation.
- `on` — You create a function to
  compute the Jacobian, and specify the name of the function in
  **Jacobian**. For example, if
  `vdpStateJacobianFcn.m` is the Jacobian
  function, specify **Jacobian** as
  `vdpStateJacobianFcn`. If you create the
  state transition function *f* using a Simulink Function (Simulink)
  block, then create the Jacobian using a Simulink
  Function block. If you create *f*
  using a MATLAB function (`.m` file), then create
  the Jacobian using a MATLAB function.

  The function calculates the partial derivatives of the state
  transition function with respect to the states and process
  noise. The number of inputs to the Jacobian function must equal
  the number of inputs of the state transition function and must
  be specified in the same order in both functions. The number of
  outputs of the Jacobian function depends on the
  **Process noise** parameter:

  - **Process noise** is
    `Additive` — The
    function calculates the partial derivative of the state
    transition function *f* with respect to
    the states (∂f/∂x). The output is an
    *Ns*-by-*Ns*
    Jacobian matrix, where *Ns* is the
    number of states.

    To see an example of a Jacobian function for additive
    process noise, type `edit
    vdpStateJacobianFcn` at the command
    line.
  - **Process noise** is
    `Nonadditive` — The
    function must also return a second output that is the
    partial derivative of the state transition function
    *f* with respect to the process
    noise terms (∂f/∂w). The second output is returned as an
    *Ns*-by-*W*
    matrix, where *W* is the number of
    process noise terms in the state transition
    function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`HasStateTransitionJacobianFcn` |
| **Type:** character vector |
| **Values:**`'off'`,`'on'` |
| **Default:**`'off'` |

|  |
| --- |
| **Block Parameter:**`StateTransitionJacobianFcn` |
| **Type:** character vector, string |
| **Default:**`''` |

### **Process noise** — Process noise characteristics `Additive` (default) | `Nonadditive`

Process noise characteristics, specified as one of the following
values:

- `Additive` — Process
  noise `w` is additive, and the state transition function *f* that
  you specify in **Function** has the following form:

  `x(k+1) = f(x(k),Us1(k),...,Usn(k))`,

  where `x(k)` is the estimated state at time `k`,
  and `Us1,...,Usn` are any additional input arguments
  required by your state transition function.
- `Nonadditive` — Process
  noise is nonadditive, and the state transition function specifies
  how the states evolve as a function of the state *and* process
  noise at the previous time step:

  `x(k+1) = f(x(k),w(k),Us1(k),...,Usn(k))`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HasAdditiveProcessNoise` |
| **Type:** character vector |
| **Values:** `'Additive'`, `'Nonadditive'` |
| **Default:** `'Additive'` |

### **Covariance** — Time-invariant process noise covariance `1` (default) | scalar | vector | matrix

Time-invariant process noise covariance, specified as a scalar,
vector, or matrix depending on the value of the **Process
noise** parameter:

- **Process noise** is `Additive` —
  Specify the covariance as a scalar, an *Ns*-element vector, or
  an *Ns*-by-*Ns* matrix, where
  *Ns* is the number of states of the system. Specify a
  scalar if there is no cross-correlation between process noise terms and all the
  terms have the same variance. Specify a vector of length *Ns*,
  if there is no cross-correlation between process noise terms but all the terms
  have different variances.
- **Process noise** is `Nonadditive` —
  Specify the covariance as a *W*-by-*W* matrix,
  where *W* is the number of process noise terms.

If the process noise covariance is time-varying, select **Time-varying**.
The block generates input port **Q** to specify the
time-varying covariance.

#### Dependencies

This parameter is enabled if you do not specify the process
noise as **Time-Varying**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ProcessNoise` |
| **Type:** character vector, string |
| **Default:** `'1'` |

### **Time-varying** — Time-varying process noise covariance `'off'` (default) | `'on'`

If you select this parameter, the block includes an additional
input port **Q** to specify the time-varying process
noise covariance.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HasTimeVaryingProcessNoise` |
| **Type:** character vector |
| **Values:** `'off'`, `'on'` |
| **Default:** `'off'` |

#### Initialization

### **Initial state** — Initial state estimate `0` (default) | vector

Initial state estimate value, specified as an *Ns*-element vector, where
*Ns* is the number of states in the system. Specify the initial
state values based on your knowledge of the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialState` |
| **Type:** character vector, string |
| **Default:** `'0'` |

### **Initial covariance** — State estimation error covariance `1` (default) | scalar | vector | matrix

State estimation error covariance, specified as a scalar, an *Ns*-element
vector, or an *Ns*-by-*Ns* matrix, where
*Ns* is the number of states of the system. If you specify a scalar
or vector, the software creates an *Ns*-by-*Ns*
diagonal matrix with the scalar or vector elements on the diagonal.

Specify a high value for the covariance when you do not have
confidence in the initial state values that you specify in **Initial
state**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStateCovariance` |
| **Type:** character vector, string |
| **Default:** `'1'` |

#### Measurement

### **Function** — Measurement function name `myMeasurementFcn` (default) | function name

The measurement function calculates the *N*-element
output measurement vector of the nonlinear system at time step
*k*, given the state vector at time step
*k*. You create the measurement function and
specify the function name in **Function**. For example,
if `vdpMeasurementFcn.m` is the measurement function
that you created and saved, specify **Function** as
`vdpMeasurementFcn`.

The inputs to the function you create depend on whether you specify
the measurement noise as additive or nonadditive in
**Measurement noise**.

- **Measurement noise** is
  `Additive` — The measurement
  function *h* specifies how the measurements
  evolve as a function of state Values:

  `y(k) = h(x(k),Um1(k),...,Umn(k))`,

  where `y(k)` and `x(k)` are
  the estimated output and estimated state at time
  `k`, and `Um1,...,Umn` are
  any optional input arguments required by your measurement
  function. For example, if you are using a sensor for tracking an
  object, an additional input could be the sensor position.

  To see an example of a measurement function with additive
  process noise, type `edit
  vdpMeasurementFcn` at the command line.
- **Measurement noise** is
  `Nonadditive`— The
  measurement function also specifies how the output measurement
  evolves as a function of the measurement noise
  `v`:

  `y(k) =
  h(x(k),v(k),Um1(k),...,Umn(k))`.

  To see an example of a measurement function with nonadditive
  process noise, type `edit
  vdpMeasurementNonAdditiveNoiseFcn`.

For more information, see State Transition and Measurement Functions.

You can create *h* using a Simulink Function (Simulink) block or
as a MATLAB function (`.m` file).

- You can use a MATLAB function only if *h* has one
  additional input argument `Um1` other than
  `x` and `v`.

  `y[k] = h(x[k],v[k],Um1(k))`

  The software generates an additional input port
  **MeasurementFcn*`i`*Inputs**
  to specify this argument for the *i*th
  measurement function.
- If you are using a Simulink Function block,
  specify `x` and `v` using
  Argument Inport (Simulink)
  blocks and the additional inputs `Um1,...,Umn`
  using Inport (Simulink) blocks in
  the Simulink Function block. The
  **Argument name** parameter of the Argument Inport (Simulink)
  and Argument
  Outport (Simulink) blocks in the Simulink
  Function block must be different from each other.
  You do not provide `Um1,...,Umn` to the
  Extended Kalman Filter block. For an example,
  see Online State Estimation Using Identified Nonlinear Models (System Identification Toolbox).

If you have multiple sensors in your system, you can specify multiple
measurement functions. You can specify up to five measurement functions
using the **Add Measurement** button. To remove
measurement functions, use **Remove
Measurement**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`MeasurementFcn1`, `MeasurementFcn2`, `MeasurementFcn3`, `MeasurementFcn4`, `MeasurementFcn5` |
| **Type:** character vector, string |
| **Default:**`'myMeasurementFcn'` |

### **Jacobian** — Jacobian of measurement function `off` (default) | `on`

Jacobian of measurement function *h*, specified as
one of the following:

- `off` — The software computes the
  Jacobian numerically. This computation may increase processing
  time and numerical inaccuracy of the state estimation.
- `on` — You create a function to
  compute the Jacobian of the measurement function
  *h*, and specify the name of the function
  in **Jacobian**. For example, if
  `vdpMeasurementJacobianFcn.m` is the
  Jacobian function, specify
  `MeasurementJacobianFcn` as
  `vdpMeasurementJacobianFcn`. If you create
  *h* using a Simulink Function (Simulink)
  block, then create the Jacobian using a Simulink
  Function block. If you create *h*
  using a MATLAB function (`.m` file), then create
  the Jacobian using a MATLAB function.

  The function calculates the partial derivatives of the
  measurement function *h* with respect to the
  states and measurement noise. The number of inputs to the
  Jacobian function must equal the number of inputs to the
  measurement function and must be specified in the same order in
  both functions. The number of outputs of the Jacobian function
  depends on the **Measurement noise**
  parameter:

  - **Measurement noise** is
    `Additive` — The
    function calculates the partial derivatives of the
    measurement function with respect to the states (∂h/∂x). The output is as an
    *N*-by-*Ns*
    Jacobian matrix, where *N* is the
    number of measurements of the system and
    *Ns* is the number of
    states.

    To see an example of a Jacobian function for additive
    measurement noise, type `edit
    vdpMeasurementJacobianFcn` at the command
    line.
  - **Measurement noise** is
    `Nonadditive` — The
    function also returns a second output that is the
    partial derivative of the measurement function with
    respect to the measurement noise terms (∂h/∂v). The second output is returned as an
    *N*-by-*V*
    Jacobian matrix, where *V* is the
    number of measurement noise terms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`HasMeasurementJacobianFcn1`, `HasMeasurementJacobianFcn2`, `HasMeasurementJacobianFcn3`, `HasMeasurementJacobianFcn4`,`HasMeasurementJacobianFcn5` |
| **Type:** character vector |
| **Values:**`'off'`,`'on'` |
| **Default:**`'off'` |

|  |
| --- |
| **Block Parameter:**`MeasurementJacobianFcn1`, `MeasurementJacobianFcn2`, `MeasurementJacobianFcn3`, `MeasurementJacobianFcn4`, `MeasurementJacobianFcn5` |
| **Type:** character vector |
| **Default:**`''` |

### **Measurement noise** — Measurement noise characteristics `Additive` (default) | `Nonadditive`

Measurement noise characteristics, specified as one of the following
values:

- `Additive` — Measurement
  noise `v` is additive, and the measurement function *h* that
  you specify in **Function** has the following form:

  `y(k) = h(x(k),Um1(k),...,Umn(k))`,

  where `y(k)` and `x(k)` are
  the estimated output and estimated state at time `k`,
  and `Um1,...,Umn` are any optional input arguments
  required by your measurement function.
- `Nonadditive` — Measurement
  noise is nonadditive, and the measurement function specifies how the
  output measurement evolves as a function of the state *and* measurement
  noise:

  `y(k) = h(x(k),v(k),Um1(k),...,Umn(k))`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HasAdditiveMeasurementNoise1`, `HasAdditiveMeasurementNoise2`, `HasAdditiveMeasurementNoise3`, `HasAdditiveMeasurementNoise4`, `HasAdditiveMeasurementNoise5` |
| **Type:** character vector |
| **Values:** `'Additive'`, `'Nonadditive'` |
| **Default:** `'Additive'` |

### **Enable measurement wrapping** — Enable measurement wrapping `off` (default) | `on`

Select this parameter to enable measurement wrapping to estimate states when you have
circular measurements that are independent of your model states. If you select this
parameter, then the measurement function you specify must include the following two outputs:

1. The measurement, specified as a *N*-element output measurement vector of the nonlinear system at
   time step *k*, given the state vector at
   time step *k*. *N* is the number of measurements of the system.
2. The measurement wrapping bounds, specified as an
   *N*-by-`2` matrix where, the first
   column provides the minimum measurement bound and the second column provides
   the maximum measurement bound.

Enabling the **Enable measurement wrapping**
check box wraps the measurement residuals in a defined bound, which helps to prevent the
filter from divergence due to incorrect measurement residual values. For an example, see
State Estimation with Wrapped Measurements Using Extended Kalman Filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`EnableMeasurementWrapping1`, `EnableMeasurementWrapping2`, `EnableMeasurementWrapping3`, `EnableMeasurementWrapping4`, `EnableMeasurementWrapping5` |
| **Type:** character vector |
| **Values:** `'off'`, `'on'` |
| **Default:** `'off'` |

### **Covariance** — Time-invariant process noise covariance `1` (default) | scalar | vector | matrix

Time-invariant process noise covariance, specified as a scalar,
vector, or matrix depending on the value of the **Process
noise** parameter:

- **Process noise** is
  `Additive` — Specify the covariance
  as a scalar, an *Ns*-element vector, or an
  *Ns*-by-*Ns* matrix, where
  *Ns* is the number of states of the system.
  Specify a scalar if there is no cross-correlation between
  process noise terms and all the terms have the same variance.
  Specify a vector of length *Ns*, if there is no
  cross-correlation between process noise terms but all the terms
  have different variances.
- **Process noise** is
  `Nonadditive` — Specify the
  covariance as a *W*-by-*W*
  matrix, where *W* is the number of process
  noise terms.

If the process noise covariance is time-varying, select
**Time-varying**. The block generates input port
**Q** to specify the time-varying
covariance.

#### Dependencies

This parameter is enabled if you do not specify the process noise
as **Time-Varying**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ProcessNoise` |
| **Type:** character vector, string |
| **Default:**`'1'` |

### **Time-varying** — Time-varying measurement noise covariance `off` (default) | `on`

If you select this parameter for the measurement noise covariance of
the first measurement function, the block includes an additional input
port **R1**. You specify the time-varying measurement
noise covariance in **R1**. Similarly, if you select
**Time-varying**  for the
*ith* measurement
function, the block includes an additional input port
**R*`i`*** to specify
the time-varying measurement noise covariance for that function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`HasTimeVaryingMeasurementNoise1`, `HasTimeVaryingMeasurementNoise2`, `HasTimeVaryingMeasurementNoise3`, `HasTimeVaryingMeasurementNoise4`, `HasTimeVaryingMeasurementNoise5` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

### **Add Enable Port** — Enable correction of estimated states only when measured data is available `off` (default) | `on`

Suppose that measured output data is not available at all time
points at the port **y1** that corresponds to the
first measurement function. Select **Add Enable port** to
generate an input port **Enable1**. Use a signal
at this port to enable the correction of estimated states only when
measured data is available. Similarly, if measured output data is
not available at all time points at the port **y*`i`*** for
the *ith* measurement
function, select the corresponding **Add Enable port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **Type:** character vector |
| **Values:** `'off'`, `'on'` |
| **Default:** `'off'` |

#### Settings

### **Use the current measurements to improve state estimates** — Choose between corrected or predicted state estimate `on` (default) | `off`

When this parameter is selected, the block outputs the corrected
state estimate x^[k|k] at
time step `k`, estimated using measured outputs until
time `k`. If you clear this parameter, the block
returns the predicted state estimate x^[k|k−1] for
time `k`, estimated using measured output until a
previous time `k-1`. Clear this parameter if your
filter is in a feedback loop and there is an algebraic loop in your Simulink model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseCurrentEstimator` |
| **Type:** character vector |
| **Values:** `'off'`, `'on'` |
| **Default:** `'on'` |

### **Output state estimation error covariance** — Output state estimation error covariance `off` (default) | `on`

If you select this parameter, a state estimation error covariance output port
**P** is generated in the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputStateCovariance` |
| **Type:** character vector |
| **Values:**`'off'`,`'on'` |
| **Default:** `'off'` |

### **Data type** — Data type for block parameters `double` (default) | `single`

Use this parameter to specify the data type for all block parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector |
| **Values:** `'single'`, `'double'` |
| **Default:** `'double'` |

### **Sample time** — Block sample time `1` (default) | positive scalar

Block sample time, specified as a positive scalar. If the sample
times of your state transition and measurement functions are different,
select **Enable multirate operation** in the **Multirate** tab,
and specify the sample times in the **Multirate** tab
instead.

#### Dependencies

This parameter is available if in the **Multirate** tab,
the **Enable multirate operation** parameter is `off`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector, string |
| **Default:** `'1'` |

### Multirate Tab

### **Enable multirate operation** — Enable specification of different sample times for state transition and measurement functions `off` (default) | `on`

Select this parameter if the sample times of the state transition
and measurement functions are different. You specify the sample times
in the **Multirate** tab, in **Sample time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnableMultirate` |
| **Type:** character vector |
| **Values:** `'off'`, `'on'` |
| **Default:** `'off'` |

### **Sample times** — State transition and measurement function sample times positive scalar

If the sample times for state transition and measurement functions are different,
specify **Sample time**. Specify the sample times for the measurement
functions as positive integer multiples of the state transition sample time. The sample
times you specify correspond to the following input ports:

- Ports corresponding to state transition function — Additional input to
  state transition function **StateTransitionFcnInputs** and
  time-varying process noise covariance **Q**. The sample times
  of these ports must always equal the state transition function sample time, but
  can differ from the sample time of the measurement functions.
- Ports corresponding to *ith*
  measurement function — Measured output
  **y*`i`***, additional input to
  measurement function
  **MeasurementFcn*`i`*Inputs**,
  enable signal at port **Enable*`i`***,
  and time-varying measurement noise covariance
  **R*`i`***. The sample times of
  these ports for the same measurement function must always be the same, but can
  differ from the sample time for the state transition function and other
  measurement functions.

#### Dependencies

This parameter is available if in the **Multirate** tab, the
**Enable multirate operation** parameter is
`on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateTransitionFcnSampleTime`, `MeasurementFcn1SampleTime1`, `MeasurementFcn1SampleTime2`, `MeasurementFcn1SampleTime3`, `MeasurementFcn1SampleTime4`, `MeasurementFcn1SampleTime5` |
| **Type:** character vector, string |
| **Default:** `'1'` |

## Libraries

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The state transition, measurement, and Jacobian functions that you specify must
use only the MATLAB commands and Simulink blocks that support code generation. For a list of blocks that support
code generation, see Blocks Supported for Code Generation (Simulink Coder). For a list of
commands that support code generation, see Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder).

Generated code uses an algorithm that is different from the algorithm that the
Extended Kalman Filter block itself uses. You might see some
numerical differences in the results obtained using the two methods.

## Version History

**Introduced in R2017a**

### R2020b: Numerical Changes

Starting in R2020b, numerical improvements in the Extended Kalman
Filter algorithm might produce results that are different from the
results you obtained in previous versions.

## Description

Estimate states of discrete-time nonlinear system using extended Kalman filter

The Extended Kalman Filter block estimates the states of a
discrete-time nonlinear system using the first-order discrete-time extended Kalman
filter algorithm.

Consider a plant with states *x*, input *u*, output
*y*, process noise *w*, and measurement noise
*v*. Assume that you can represent the plant as a nonlinear
system.

Using the state transition and measurement functions of the system and the extended
Kalman filter algorithm, the block produces state estimates x^ for the current time step. For information about the algorithm, see
Extended and Unscented Kalman Filter Algorithms for Online State Estimation.

You create the nonlinear state transition function and measurement functions for the
system and specify these functions in the block. The block supports state estimation of
a system with multiple sensors that are operating at different sampling rates. You can
specify up to five measurement functions, each corresponding to a sensor in the system.
You can also specify the Jacobians of the state transition and measurement functions. If
you do not specify them, the software numerically computes the Jacobians. For more
information, see State Transition and Measurement Functions.
