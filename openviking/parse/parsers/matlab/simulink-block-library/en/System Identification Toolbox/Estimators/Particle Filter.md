---
type: simulink-block
title: 'Particle Filter'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Estimators'
documentation_page: 'pf_block'
documentation_source_path: 'ref/pf_block.html'
language: en
---

# Particle Filter

## Ports
```yaml
ports:
- name: y1,y2,y3,y4,y5
  summary: Measured system outputs vector
  direction: input
- name: StateTransitionFcnInputs
  summary: Optional input argument to state transition function scalar | vector | matrix
  direction: input
- name: MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs
  summary: Optional input argument to each measurement likelihood function scalar | vector | matrix
  direction: input
- name: Enable1,Enable2,Enable3,Enable4,Enable5
  summary: Enable correction of estimated states when measured data is available scalar
  direction: input
- name: xhat
  summary: Estimated states vector
  direction: output
- name: P
  summary: State estimation error covariance matrix
  direction: output
- name: Particles
  summary: Particle values used for state estimation array
  direction: output
- name: Weights
  summary: Particle weights used for state estimation vector
  direction: output
```

### Input

### **y1,y2,y3,y4,y5** — Measured system outputs vector

Measured system outputs corresponding to each measurement likelihood
function that you specify in the block. The number of ports equals the
number of measurement likelihood functions in your system. You can
specify up to five measurement likelihood functions. For example, if
your system has two sensors, you specify two measurement likelihood
functions in the block. The first port **y1** is
available by default. Click **Add Measurement**, to
generate port **y2** corresponding to the second
measurement likelihood function.

Specify the ports as *N*-dimensional vectors, where
*N* is the number of quantities measured by the
corresponding sensor. For example, if your system has one sensor that
measures the position and velocity of an object, then there is only one
port **y1**. The port is specified as a two-dimensional
vector with values corresponding to position and velocity.

#### Dependencies

The first port **y1** is available by default. To
generate ports **y2** to **y5**,
click **Add Measurement**.

### **StateTransitionFcnInputs** — Optional input argument to state transition function scalar | vector | matrix

Optional input argument to the state transition function
`f` other than the state
`x`.

If you create `f` using a MATLAB® function (`.m` file), the software
generates the port **StateTransitionFcnInputs** when
you enter the name of your function, and click
**Apply**.

If your state transition function has more than one additional input,
use a Simulink Function (Simulink) block to
specify the function. When you use a Simulink Function
block, you provide the additional inputs directly to the Simulink
Function block using Inport (Simulink) blocks. No input
ports are generated for the additional inputs in the Particle
Filter block.

#### Dependencies

To generate this port, both of the following conditions should be
satisfied:

- You specify `f` in
  **Function** using a MATLAB function, and `f` is on the
  MATLAB path.
- `f` requires only one additional input
  argument apart from particles.

### **MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs** — Optional input argument to each measurement likelihood function scalar | vector | matrix

Optional inputs to the measurement likelihood functions other than the
state `x` and measurement `y`.

**MeasurementLikelihoodFcn1Inputs** corresponds to
the first measurement likelihood function that you specify, and so
on.

If you specify two measurement inputs using MATLAB functions (`.m` files) in
**Function**, the software generates ports
**MeasurementLikelihoodFcn1Inputs** and
**MeasurementLikelihoodFcn2Inputs** when you click
**Apply**. You can specify the inputs to these
ports as scalars, vectors, or matrices.

If your measurement likelihood functions have more than one
additional input, use Simulink Function (Simulink) blocks
to specify the functions. When you use a Simulink
Function block, you provide the additional inputs directly
to the Simulink Function block using Inport (Simulink) blocks. No input
ports are generated for the additional inputs in the Particle
Filter block.

#### Dependencies

To generate a port corresponding to a measurement likelihood
function `h`, both of the following conditions
should be satisfied:

- You specify measurement input `h` in
  **Function** using a MATLAB function, and `h` is on the
  MATLAB path.
- `h` requires only one additional input
  argument apart from particles and measurement.

### **Enable1,Enable2,Enable3,Enable4,Enable5** — Enable correction of estimated states when measured data is available scalar

Enable correction of estimated states when measured data is
available.

For example, consider that measured output data is not available at
all time points at the port **y1** that corresponds to
the first measurement likelihood function. Then, use a signal value
other than `0` at the **Enable1** port
to enable the correction of estimated states when measured data is
available. Specify the port value as `0` when measured
data is not available. Similarly, if measured output data is not
available at all time points at the port
**y*`i`*** for the
*ith* measurement
likelihood function, specify the corresponding port
**Enable*`i`*** as a
value other than `0`.

#### Dependencies

To generate a port corresponding to a measurement likelihood
function, select **Add Enable port** for that
measurement likelihood function. The port appears when you click
**Apply**.
### Output

### **xhat** — Estimated states vector

Estimated states, returned as a vector of size *Ns*,
where *Ns* is the number of states of the system. To
access the individual states, use the Selector (Simulink) block.

When the **Use the current measurements to improve state
estimates** parameter is selected, the block outputs the
corrected state estimate x^[k|k] at time step `k`, estimated using
measured outputs until time `k`. If you clear this
parameter, the block returns the predicted state estimate x^[k|k−1] for time `k`, estimated using
measured output until a previous time `k-1`. Clear this
parameter if your filter is in a feedback loop and there is an algebraic
loop in your Simulink® model.

### **P** — State estimation error covariance matrix

State estimation error covariance, returned as an
*Ns*-by-*Ns* matrix, where
*Ns* is the number of states of the system. To
access the individual covariances, use the Selector (Simulink) block.

You can output the error covariance only if you select
**Output state estimation error covariance** in the
**Block outputs, Multirate** tab, and click
**Apply**.

#### Dependencies

To enable this parameter, set the **State estimation
method** parameter in the **Block outputs,
Multirate** tab to `'Mean'`.

### **Particles** — Particle values used for state estimation array

Particle values used for state estimation, returned as an
*Ns*-by-*Np* or
*Np*-by-*Ns* array.
*Ns* is the number of states of the system, and
*Np* is the number of particles.

- If the `StateOrientation` parameter is
  specified as `'column'`, then
  **Particles** is returned as an
  *Ns*-by-*Np* array.
- If the `StateOrientation` parameter is
  specified as `'row'`, then
  **Particles** is returned as an
  *Np*-by-*Ns* array.

#### Dependencies

To generate this port, select **Output all
particles** in the **Block outputs,
Multirate** tab, and click
**Apply**.

### **Weights** — Particle weights used for state estimation vector

Particle weights used for state estimation, returned as a
1-by-*Np* or *Np*-by-1 vector,
where *Np* is the number of particles used for state
estimation.

- If the `StateOrientation` parameter is
  specified as `'column'`, then
  **Weights** is returned as a
  1-by-*Np* vector, where each weight is
  associated with the particle in the same column in the
  `Particles` array.
- If the `StateOrientation` parameter is
  specified as `'row'`, then
  **Weights** is returned as a
  *Np*-by-1 vector, where each weight is
  associated with the particle in the same row in the
  `Particles` array.

#### Dependencies

To generate this port, select **Output weights**
in the **Block outputs, Multirate** tab, and click
**Apply**.
## Parameters
```yaml
parameters:
- name: Function
  summary: State transition function name 'vdpParticleFilterStateFcn' (default) | function name
  group: System Model Tab
  block_parameter: StateTransitionFcn
  type: character vector, string
  default: '''vdpParticleFilterStateFcn'''
- name: Number of Particles
  summary: Number of particles used in the filter 1000 (default) | positive scalar integer
  group: System Model Tab
  block_parameter: NumberOfParticles
  type: positive scalar integer
  default: '1000'
- name: Distribution
  summary: Initial distribution of particles 'Gaussian' (default) | 'Uniform' | 'Custom'
  group: System Model Tab
  block_parameter: InitialDistribution
  type: character vector
  values: '''Gaussian'', ''Uniform'', ''Custom'''
  default: '''Gaussian'''
- name: Mean
  summary: Initial mean value of particles [0;0] (default) | vector
  group: System Model Tab
  block_parameter: InitialMean
  type: array
  default: '[0,0]'
- name: Covariance
  summary: Initial covariance of particles 1 (default) | scalar | vector | matrix
  group: System Model Tab
  block_parameter: InitialCovariance
  type: scalar, vector, or matrix
  default: '1'
- name: Circular Variables
  summary: Circular variables used for state estimation 0 (default) | scalar | vector
  group: System Model Tab
  block_parameter: CircularVariables
  type: scalar, vector
  default: '0'
- name: State Orientation
  summary: Orientation of input system states 'column' (default) | 'row'
  group: System Model Tab
  block_parameter: StateOrientation
  type: character vector
  values: '''column'', ''row'''
  default: '''column'''
- name: State bounds
  summary: Initial bounds on system states [-3 3;-3 3] (default) | array
  group: System Model Tab
  block_parameter: InitialStateBounds
  type: array
  default: '[-3 3;-3 3]'
- name: Particles
  summary: Custom particle distribution for state estimation [] (default) | array
  group: System Model Tab
  block_parameter: InitialParticles
  type: array
  default: '[]'
- name: Weights
  summary: Custom particle weight values for state estimation [] (default) | vector of positive values
  group: System Model Tab
  block_parameter: InitialWeights
  type: vector of positive values
  default: '[]'
- name: Function
  summary: Measurement likelihood function name 'vdpMeasurementLikelihoodFcn' (default) | function name
  group: System Model Tab
  block_parameter: MeasurementLikelihoodFcn1, MeasurementLikelihoodFcn2, MeasurementLikelihoodFcn3, MeasurementLikelihoodFcn4,
    MeasurementLikelihoodFcn5
  type: character vector, string
  default: '''vdpMeasurementLikelihoodFcn'''
- name: Add Enable Port
  summary: Enable correction of estimated states only when measured data is available off (default) | on
  group: System Model Tab
  block_parameter: HasMeasurementEnablePort1, HasMeasurementEnablePort2, HasMeasurementEnablePort3, HasMeasurementEnablePort4,
    HasMeasurementEnablePort5
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Resampling method
  summary: Method used for particle resampling 'Multinomial' (default) | 'Systemic' | 'Stratified'
  group: System Model Tab
  block_parameter: ResamplingMethod
  type: character vector
  values: '''Multinomial'', ''Systemic'', ''Stratified'''
  default: '''Multinomial'''
- name: Trigger method
  summary: Method to determine when resampling occurs 'Ratio' (default) | 'Interval'
  group: System Model Tab
  block_parameter: TriggerMethod
  type: character vector
  values: '''Ratio'', ''Interval'''
  default: '''Ratio'''
- name: Minimum effective particle ratio
  summary: Minimum desired ratio of the effective number of particles to the total number of particles 0.5 (default) | positive
    scalar
  group: System Model Tab
  block_parameter: MinEffectiveParticleRatio
  type: scalar
  values: Range [0,1]
  default: '0.5'
- name: Sampling Interval
  summary: Fixed interval between resampling 1 (default) | positive scalar integer
  group: System Model Tab
  block_parameter: SamplingInterval
  type: positive scalar integer
  default: '1'
- name: Randomness
  summary: Whether the random numbers are repeatable 'Repeatable' (default) | 'Not repeatable'
  group: System Model Tab
  block_parameter: Randomness
  type: character vector
  values: '''Repeatable'', ''Not repeatable'''
  default: '''Repeatable'''
- name: Seed
  summary: Seed value for repeatable random numbers 0 (default) | scalar
  group: System Model Tab
  block_parameter: Seed
  type: scalar
  default: '0'
- name: Data type
  summary: Data type for block parameters double (default) | single
  group: System Model Tab
  block_parameter: DataType
  type: character vector
  values: '''single'', ''double'''
  default: '''double'''
- name: Sample time
  summary: Block sample time 1 (default) | positive scalar
  group: System Model Tab
  block_parameter: SampleTime
  type: character vector, string
  default: '''1'''
- name: State Estimation Method
  summary: Method used for extracting a state estimate from particles 'Mean' (default) | 'MaxWeight' | 'None'
  group: Block Outputs, Multirate Tab
  block_parameter: StateEstimationMethod
  type: character vector, string
  values: '''Mean'', ''MaxWeight'', ''None'''
  default: '''Mean'''
- name: Output all particles
  summary: Output all particles 'off' (default) | 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputParticles
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Output weights
  summary: Output particle weights 'off' (default) | 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputWeights
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Output state estimation error covariance
  summary: Output state estimation error covariance 'off' (default) | 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: OutputStateCovariance
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Use the current measurements to improve state estimates
  summary: Option to use current measurements for state estimation 'on' (default) | 'off'
  group: Block Outputs, Multirate Tab
  block_parameter: UseCurrentEstimator
  type: character vector
  values: '''on'', ''off'''
  default: '''on'''
- name: Enable multirate operation
  summary: Enable specification of different sample times for state transition and measurement likelihood functions 'off'
    (default) | 'on'
  group: Block Outputs, Multirate Tab
  block_parameter: EnableMultirate
  type: character vector
  values: '''off'', ''on'''
  default: '''off'''
- name: Sample times
  summary: State transition and measurement likelihood function sample times positive scalar
  group: Block Outputs, Multirate Tab
  block_parameter: StateTransitionFcnSampleTime, MeasurementLikelihoodFcn1SampleTime1, MeasurementLikelihoodFcn1SampleTime2,
    MeasurementLikelihoodFcn1SampleTime3, MeasurementLikelihoodFcn1SampleTime4, MeasurementLikelihoodFcn1SampleTime5
  type: character vector, string
  default: '''1'''
```

### System Model Tab

#### State Transition

### **Function** — State transition function name `'vdpParticleFilterStateFcn'` (default) | function name

The particle filter state transition function calculates the particles
at time step *k+1*, given particles at time step
*k* per the dynamics of your system and process
noise. This function has the syntax:

```
particlesNext = f(particles, param1, param2, ...)
```

where, *particles* and
*particlesNext* have dimensions
*Ns*-by-*Np* if **State
Orientation** is specified as `'column'`,
or *Np*-by-*Ns* if **State
Orientation** is specified as `'row'`.
Also, `param_i` represents optional input arguments you
may specify. For more information on optional input arguments, see StateTransitionFcnInputs.

You create the state transition function and specify the function name
in **Function**. For example, if
`vdpParticleFilterStateFcn.m` is the state
transition function that you created and saved, specify
**Function** as
`'vdpParticleFilterStateFcn'`.

You can create **Function** using a Simulink Function (Simulink) block or
as a MATLAB function (`.m` file).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateTransitionFcn` |
| **Type:** character vector, string |
| **Default:**`'vdpParticleFilterStateFcn'` |

#### Initialization

### **Number of Particles** — Number of particles used in the filter 1000 (default) | positive scalar integer

Number of particles used in the filter, specified as a positive scalar
integer. Each particle represents a state hypothesis in the system. A
higher number of particles increases the state estimation accuracy, but
also increases the computational effort required to run the
filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumberOfParticles` |
| **Type:** positive scalar integer |
| **Default:**`1000` |

### **Distribution** — Initial distribution of particles `'Gaussian'` (default) | `'Uniform'` | `'Custom'`

Initial distribution of particles, specified as
`'Gaussian'`, `'Uniform'`, or
`'Custom'`.

If you choose `'Gaussian'`, the initial set of
particles or state hypotheses are distributed per the multivariate
Gaussian distribution, where you specify the **Mean**
and **Covariance**. The initial weight of all particles
is assumed to be equal.

If you choose `'Uniform'`, the initial set of
particles are distributed per the uniform distribution, where you
specify the upper and lower **State bounds**. The
initial weight of all particles is assumed to be equal.

`'Custom'` allows you to specify your own set of
initial particles and their weights. You can use arbitrary probability
distributions for **Particles** and
**Weights** to initialize the filter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialDistribution` |
| **Type:** character vector |
| **Values:**`'Gaussian'`, `'Uniform'`, `'Custom'` |
| **Default:**`'Gaussian'` |

### **Mean** — Initial mean value of particles [0;0] (default) | vector

Initial mean value of particles, specified as a vector. The number of
states to be estimated defines the length of the vector.

#### Dependencies

To enable this parameter, set the
**Distribution** parameter in the
**System model** tab to
`Gaussian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialMean` |
| **Type:** array |
| **Default:**`[0,0]` |

### **Covariance** — Initial covariance of particles 1 (default) | scalar | vector | matrix

Initial covariance of particles, specified as a scalar, vector, or
matrix.

If **Covariance** is specified as:

- A scalar, then it must be positive. The covariance is assumed
  to be a [*Ns*
  *Ns*] matrix with this scalar on the diagonals.
  Here, *Ns* is the number of states.
- A vector, then each element must be positive. The covariance
  is assumed to be a [*Ns*
  *Ns*] matrix with the elements of the vector on
  the diagonals.
- A matrix, then it must be positive semidefinite.

#### Dependencies

To enable this parameter, set the
**Distribution** parameter in the
**System model** tab to
`Gaussian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialCovariance` |
| **Type:** scalar, vector, or matrix |
| **Default:**`1` |

### **Circular Variables** — Circular variables used for state estimation 0 (default) | scalar | vector

Circular variables used for state estimation, specified as a scalar,
or *Ns*-element vector, where *Ns* is
the number of states.

If **Circular Variables** is specified as a scalar,
the software extends it to a vector where each element is equal to this
scalar. Circular (or angular) distributions use a probability density
function with a range of [`-π`
`π`]. Use circular variables if some of the states in
your system represent angular quantities like the orientation of an
object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CircularVariables` |
| **Type:** scalar, vector |
| **Default:**`0` |

### **State Orientation** — Orientation of input system states `'column'` (default) | `'row'`

Orientation of system states, specified as `'column'`
or `'row'`.

If **State Orientation** is specified as:

- `'column'`, then the first input argument to
  the state transition and measurement likelihood function is
  [*Ns*
  *Np*]. In this case,
  *ith* column
  of this matrix is the
  *ith* particle
  (state hypothesis). Also, the states estimates
  **xhat** is output as a
  [*Ns* 1] vector. Here,
  *Ns* is the number of states, and
  *Np* is the number of particles.
- `'row'`, then the first input argument to the
  state transition and measurement likelihood function is
  [*Np*
  *Ns*], and each row of this matrix contains a
  particle. Also, the states estimates **xhat**
  is output as a [1 *Ns*] vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateOrientation` |
| **Type:** character vector |
| **Values:**`'column'`, `'row'` |
| **Default:**`'column'` |

### **State bounds** — Initial bounds on system states [-3 3;-3 3] (default) | array

Initial bounds on system states, specified as an
*Ns*-by-2 array, where *Ns* is the
number of states.

The *ith* row lists the
lower and upper bound of the uniform distribution for the initial
distribution of particles of the
*ith* state.

#### Dependencies

To enable this parameter, set the
**Distribution** parameter in the
**System model** tab to
`Uniform`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialStateBounds` |
| **Type:** array |
| **Default:** `[-3 3;-3 3]` |

### **Particles** — Custom particle distribution for state estimation [] (default) | array

Custom particle distribution for state estimation, specified as an
*Ns*-by-*Np* or
*Np*-by-*Ns* array.
*Ns* is the number of states of the system, and
*Np* is the number of particles.

You choose a distribution, create a probability distribution object
for it using the `makedist` function, and generate
particles of the desired distribution using the
`random` function.

- If the `StateOrientation` parameter is
  `'column'`, then specify
  **Particles** as an
  *Ns*-by-*Np* array.

  For example,

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Ns,Np);
  ```
- If the `StateOrientation` parameter is
  `'row'`, then specify
  **Particles** as an
  *Np*-by-*Ns* array.

  For example,

  ```
  pd = makedist('Poisson');
  Particles = random(pd,Np,Ns);
  ```

#### Dependencies

To enable this parameter, set the
**Distribution** parameter in the
**System model** tab to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialParticles` |
| **Type:** array |
| **Default:**`[]` |

### **Weights** — Custom particle weight values for state estimation [] (default) | vector of positive values

Custom particle weight values for state estimation, specified as a
1-by-*Np* or *Np*-by-1 vector of
positive values, where *Np* is the number of particles
used for state estimation.

- If the `StateOrientation` parameter is
  `'column'`, then specify
  **Weights** as a 1-by-*Np*
  vector. Each weight in the vector is associated with the
  particle in the same column in the
  `Particles` array.

  For example,

  ```
  Weights = ones(1,Np)/Np;
  ```
- If the `StateOrientation` parameter is
  `'row'`, then specify
  **Weights** as a *Np*-by-1
  vector. Each weight in the vector is associated with the
  particle in the same row in the `Particles`
  array.

  For example,

  ```
  Weights = ones(Np,1)/Np;
  ```

#### Dependencies

To enable this parameter, set the
**Distribution** parameter in the
**System model** tab to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`InitialWeights` |
| **Type:** vector of positive values |
| **Default:**`[]` |

#### Measurement

### **Function** — Measurement likelihood function name `'vdpMeasurementLikelihoodFcn'` (default) | function name

The measurement likelihood function calculates the likelihood of
particles (state hypotheses) using the sensor measurements. For each
state hypothesis (particle), the function first calculates an
*Nm*-element measurement hypothesis vector. Then
the likelihood of each measurement hypothesis is calculated based on the
sensor measurement and the measurement noise probability distribution.
This function has the
syntax:

```
likelihood = h(particles, measurement, param1, param2, ...)
```

where,
*likelihood* is an *Np*-element
vector, where *Np* is the number of particles.
*particles* have dimensions
*Ns*-by-*Np* if **State
Orientation** is specified as `'column'`,
or *Np*-by-*Ns* if **State
Orientation** is specified as `'row'`.
*measurement* is an *Nm*-element
vector where, *Nm* is the number of measurements your
sensor provides. *param\_i* represents optional input
arguments you may specify. For more information on optional input
arguments, see MeasurementLikelihoodFcn1Inputs,...,MeasurementLikelihoodFcn5Inputs.

You create the measurement likelihood function and specify the
function name in **Function**. For example, if
`vdpMeasurementLikelihoodFcn.m` is the measurement
likelihood function that you created and saved, specify
**Function** as
`'vdpMeasurementLikelihoodFcn'`.

You can create **Function** using a Simulink Function (Simulink) block or
as a MATLAB function (`.m` file).

- You can use a MATLAB function only if *h* has zero or
  one additional input argument `param_i` other
  than **Particles** and
  **Measurement**.

  The software generates an additional input port
  **MeasurementLikelihoodFcn*`i`*Inputs**
  to specify this argument for the
  *ith*
  measurement likelihood function, and click
  **Apply**.
- If you are using a Simulink Function block,
  specify `x` and `y` using
  Argument Inport (Simulink)
  blocks and the additional inputs `param_i`
  using Inport (Simulink) blocks in
  the Simulink Function block. You do not provide
  `param_i` to the Particle
  Filter block.

If you have multiple sensors in your system, you can specify multiple
measurement likelihood functions. You can specify up to five measurement
likelihood functions using the **Add Measurement**
button. To remove measurement likelihood functions, use **Remove
Measurement**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`MeasurementLikelihoodFcn1`, `MeasurementLikelihoodFcn2`, `MeasurementLikelihoodFcn3`, `MeasurementLikelihoodFcn4`, `MeasurementLikelihoodFcn5` |
| **Type:** character vector, string |
| **Default:**`'vdpMeasurementLikelihoodFcn'` |

### **Add Enable Port** — Enable correction of estimated states only when measured data is available `off` (default) | `on`

Suppose that measured output data is not available at all time points
at the port **y1** that corresponds to the first
measurement likelihood function. To generate an input port
**Enable1**, select **Add Enable
port**. Use a signal at this port to enable the correction
of estimated states only when measured data is available. Similarly, if
measured output data is not available at all time points at the port
**y*`i`*** for the
*ith* measurement
likelihood function, select the corresponding **Add Enable
port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`HasMeasurementEnablePort1`, `HasMeasurementEnablePort2`, `HasMeasurementEnablePort3`, `HasMeasurementEnablePort4`, `HasMeasurementEnablePort5` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

#### Resampling

### **Resampling method** — Method used for particle resampling `'Multinomial'` (default) | `'Systemic'` | `'Stratified'`

Method used for particle resampling, specified as one of the
following:

- `'Multinomial'` — Multinomial resampling,
  also called simplified random sampling, generates
  `N` random numbers independently from the
  uniform distribution in the open interval
  `(0,1)` and uses them to select particles
  proportional to their weight.
- `'Stratified'` — Stratified resampling
  divides the whole population of particles into subsets called
  strata. It pre-partitions the `(0,1)` interval
  into `N` disjoint sub-intervals of size
  `1/N`. The random numbers are drawn
  independently in each of these sub-intervals and the sample
  indices chosen in the strata.
- `'Systematic'` — Systematic resampling is
  similar to stratified resampling as it also makes use of strata.
  One distinction is that it only draws one random number from the
  open interval `(0,1/N)` and the remaining
  sample points are calculated deterministically at a fixed
  `1/N` step size.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ResamplingMethod` |
| **Type:** character vector |
| **Values:**`'Multinomial'`, `'Systemic'`, `'Stratified'` |
| **Default:**`'Multinomial'` |

### **Trigger method** — Method to determine when resampling occurs `'Ratio'` (default) | `'Interval'`

Method to determine when resampling occurs, specified as either
`'Ratio'` or `'Interval'`. The
`'Ratio'` value triggers resampling based on the
ratio of effective total particles. The `'Interval'`
value triggers resampling at regular time steps of the particle filter
operation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`TriggerMethod` |
| **Type:** character vector |
| **Values:**`'Ratio'`, `'Interval'` |
| **Default:**`'Ratio'` |

### **Minimum effective particle ratio** — Minimum desired ratio of the effective number of particles to the total number of particles 0.5 (default) | positive scalar

Minimum desired ratio of the effective number of particles to the
total number of particles, specified as a positive scalar. The effective
number of particles is a measure of how well the current set of
particles approximates the posterior distribution. A lower effective
particle ratio implies that a lower number of particles are contributing
to the estimation and resampling is required.

If the ratio of the effective number of particles to the total number
of particles falls below the minimum effective particle ratio, a
resampling step is triggered.

Specify minimum effective particle ratio as any value from 0 through
1.

#### Dependencies

To enable this parameter, set the **Trigger
method** parameter in the **System
model** tab to `Ratio`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`MinEffectiveParticleRatio` |
| **Type:** scalar |
| **Values:**  Range `[0,1]` |
| **Default:**`0.5` |

### **Sampling Interval** — Fixed interval between resampling 1 (default) | positive scalar integer

Fixed interval between resampling, specified as a positive scalar
integer. The sampling interval determines during which correction steps
the resampling is executed. For example, a value of two means the
resampling is executed every second correction step. A value of
`inf` means that resampling is never
executed.

#### Dependencies

To enable this parameter, set the **Trigger
method** parameter in the **System
model** tab to `Interval`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SamplingInterval` |
| **Type:** positive scalar integer |
| **Default:**`1` |

#### Random Number Generator Options

### **Randomness** — Whether the random numbers are repeatable `'Repeatable'` (default) | `'Not repeatable'`

Whether the random numbers are repeatable, specified as either
`'Repeatable'` or `'Not
repeatable'`. If you want to be able to produce the same
result more than once, set **Randomness** to
`'Repeatable'`, and specify the same random number
generator seed value in **Seed**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Randomness` |
| **Type:** character vector |
| **Values:**  `'Repeatable'`, `'Not repeatable'` |
| **Default:**`'Repeatable'` |

### **Seed** — Seed value for repeatable random numbers 0 (default) | scalar

Seed value for repeatable random numbers, specified as a
scalar.

#### Dependencies

To enable this parameter, set the **Randomness**
parameter in the **System model** tab to
`'Repeatable'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Seed` |
| **Type:** scalar |
| **Default:**`0` |

#### Settings

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

Block sample time, specified as a positive scalar.

Use the **Sample time** parameter if your state
transition and all measurement likelihood functions have the same sample
time. Otherwise, select the **Enable multirate
operation** option in the **Multirate**
tab, and specify sample times in the same tab.

#### Dependencies

To enable this parameter, set the **Enable multirate
operation** parameter in the **Block output,
Multirate** tab to `off`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SampleTime` |
| **Type:** character vector, string |
| **Default:**`'1'` |

### Block Outputs, Multirate Tab

#### Outputs

### **State Estimation Method** — Method used for extracting a state estimate from particles `'Mean'` (default) | `'MaxWeight'` | `'None'`

Method used for extracting a state estimate from particles, specified
as one of the following:

- `'Mean'` — The Particle
  Filter block outputs the weighted mean of the
  particles, depending on the parameters
  **Weights** and
  **Particles**, as the state
  estimate.
- `'Maxweight'` — The Particle
  Filter block outputs the particle with the
  highest weight as the state estimate.
- `'None'` — Use this option to implement a
  custom state estimation method by accessing all particles
  using the **Output all particles**
  parameter from the **Block outputs,
  Multirate** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateEstimationMethod` |
| **Type:** character vector, string |
| **Values:**  `'Mean'`, `'MaxWeight'`, `'None'` |
| **Default:**`'Mean'` |

### **Output all particles** — Output all particles `'off'` (default) | `'on'`

If you select this parameter, an output port for particles used in the
estimation, **Particles** is generated in the
block.

- If the `StateOrientation` parameter is
  specified as `'column'`, then the particles are
  output as an *Ns*-by-*Np*
  array. *Ns* is the number of states of the
  system, and *Np* is the number of
  particles.
- If the `StateOrientation` parameter is
  specified as `'row'`, then the particles are
  output as an *Np*-by-*Ns*
  array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputParticles` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

### **Output weights** — Output particle weights `'off'` (default) | `'on'`

If you select this parameter, an output port for particle weights used
in the estimation, **Weights** is generated in the
block.

- If the `StateOrientation` parameter is
  specified as `'column'`, then the particle
  weights are output as a 1-by-*Np* vector. Here,
  where each weight is associated with the particle in the same
  column in the `Particles` array.
  *Np* is the number of particles used for
  state estimation.
- If the `StateOrientation` parameter is
  specified as `'row'`, then the particle weights
  are output as a *Np*-by-1 vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputWeights` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

### **Output state estimation error covariance** — Output state estimation error covariance `'off'` (default) | `'on'`

If you select this parameter, a state estimation error covariance
output port, **P** is generated in the block.

#### Dependencies

To enable this parameter, set the **State estimation
method** parameter in the **Block outputs,
Multirate** tab to `'Mean'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputStateCovariance` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

### **Use the current measurements to improve state estimates** — Option to use current measurements for state estimation `'on'` (default) | `'off'`

When this parameter is selected, the block outputs the corrected state
estimate x^[k|k] at time step `k`, estimated using
measured outputs until time `k`. If you clear this
parameter, the block returns the predicted state estimate x^[k|k−1] for time `k`, estimated using
measured output until a previous time `k-1`. Clear this
parameter if your filter is in a feedback loop and there is an algebraic
loop in your Simulink model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`UseCurrentEstimator` |
| **Type:** character vector |
| **Values:**`'on'`, `'off'` |
| **Default:**`'on'` |

#### Multirate

### **Enable multirate operation** — Enable specification of different sample times for state transition and measurement likelihood functions `'off'` (default) | `'on'`

Select this parameter if the sample times of the state transition or
any of the measurement likelihood functions differ from the rest. You
specify the sample times in the **Multirate** tab, in
**Sample time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`EnableMultirate` |
| **Type:** character vector |
| **Values:**`'off'`, `'on'` |
| **Default:**`'off'` |

### **Sample times** — State transition and measurement likelihood function sample times positive scalar

If the sample times for state transition and measurement likelihood
functions are different, specify **Sample time**.
Specify the sample times for the measurement functions as positive
integer multiples of the state transition sample time. The sample times
you specify correspond to the following input ports:

- Ports corresponding to state transition function — Additional
  input to state transition function
  **StateTransitionFcnInputs**. The sample
  times of these ports must always equal the state transition
  function sample time, but can differ from the sample time of the
  measurement likelihood functions.
- Ports corresponding to
  *ith*
  measurement likelihood function — Measured output
  **y*`i`***,
  additional input to measurement likelihood function
  **MeasurementLikelihoodFcn*`i`*Inputs**,
  enable signal at port
  **Enable*`i`***.
  The sample times of these ports for the same measurement
  likelihood function must always be the same, but can differ from
  the sample time for the state transition function and other
  measurement likelihood functions.

#### Dependencies

To enable this parameter, set the **Enable multirate
operation** parameter in the **Block outputs,
Multirate** tab to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`StateTransitionFcnSampleTime`, `MeasurementLikelihoodFcn1SampleTime1`, `MeasurementLikelihoodFcn1SampleTime2`, `MeasurementLikelihoodFcn1SampleTime3`, `MeasurementLikelihoodFcn1SampleTime4`, `MeasurementLikelihoodFcn1SampleTime5` |
| **Type:** character vector, string |
| **Default:**`'1'` |
## Libraries

Control System Toolbox / State Estimation System Identification Toolbox / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The state transition and measurement likelihood functions that you specify must
use only the MATLAB commands and Simulink blocks that support code generation. For a list of blocks that support
code generation, see Blocks Supported for Code Generation (Simulink Coder). For a list of
commands that support code generation, see Functions and Objects Supported for C/C++ Code Generation (MATLAB Coder).

## Version History

**Introduced in R2018a**

## Description

Estimate states of discrete-time nonlinear system using particle filter

The Particle Filter block estimates the states of a discrete-time
nonlinear system using the discrete-time particle filter algorithm.

Consider a plant with states *x*, input *u*, output
*m*, process noise *w*, and measurement
*y*. Assume that you can represent the plant as a nonlinear
system.

The algorithm computes the state estimates x^ of the nonlinear system using the state transition and measurement
likelihood functions you specify.

You create the nonlinear state transition function and measurement likelihood
functions for the system and specify these functions in the block. The block supports
state estimation of a system with multiple sensors that are operating at different
sampling rates. You can specify up to five measurement likelihood functions, each
corresponding to a sensor in the system.
