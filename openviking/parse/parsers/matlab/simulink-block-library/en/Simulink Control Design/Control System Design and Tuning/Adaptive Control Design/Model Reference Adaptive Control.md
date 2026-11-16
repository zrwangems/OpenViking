---
type: simulink-block
title: 'Model Reference Adaptive Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Adaptive Control Design'
documentation_page: 'modelreferenceadaptivecontrol'
documentation_source_path: 'ug/modelreferenceadaptivecontrol.html'
language: en
---

# Model Reference Adaptive Control

## Ports

### Input

### **r** — Reference signal scalar signal | vector signal

Provide the reference signal for the controlled system to follow.

### **state** — Controlled system state vector signal

Provide the current state vector from the controlled system.

### **phi** — Disturbance model features vector signal | matrix signal

Provide custom disturbance model features.

#### Dependencies

To enable this input port, set the **Feature type** parameter
to `Use External Source for Feature`.
### Output

### **u** — Control input scalar signal | matrix signal

Connect the control input signal to the input of the controlled system. The
control input is a vector signal with length equal to the number of control inputs in
the controlled system.

### **u\_ad** — Disturbance and uncertainty estimate scalar signal | matrix signal

The disturbance and uncertainty estimate is the product of the disturbance model
features and the disturbance model weight vector. You can use this signal to compare
the estimated disturbance model with the actual disturbances in your system.

#### Dependencies

To enable this output port, select the **Output disturbance/uncertainty
estimate** parameter.

### **Ahat** — Estimator state matrix matrix signal

Use this port to output the estimated state matrix for the estimator plant
model.

#### Dependencies

This output port is used for indirect MRAC. To enable this port, first select
the **Indirect** algorithm option. Then, select the
**Output estimated parameters** parameter.

### **Bhat** — Estimator control effective matrix vector signal | matrix signal

Use this port to output the estimated control effective matrix for the estimator
plant model.

#### Dependencies

This output port is used for indirect MRAC. To enable this port, first select
the **Indirect** algorithm option. Then, select the
**Output estimated parameters** parameter.

## Parameters

### System

Select an MRAC algorithm and specify nominal, reference, and estimator model
dynamics.

### **A** — Nominal model state matrix `0` (default) | square matrix

Specify the state matrix for the nominal model as an
*N*-by-*N* matrix, where *N* is
the number of states in the controlled system.

#### Dependencies

This parameter is used for direct MRAC. To enable this parameter, select the
**Direct** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'A'` |
| **Type:** character vector |
| **Values:** square matrix |
| **Default:** `'0'` |

### **B** — Nominal model control effective matrix `1` (default) | vector | matrix

Specify the control effective matrix of the nominal model as a nonzero
*N*-by-*M* matrix, where *N* is
the number of states in the controlled system and *M* is the number
of control inputs in the controlled system.

#### Dependencies

This parameter is used for direct MRAC. To enable this parameter, select the
**Direct** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'B'` |
| **Type:** character vector |
| **Values:** vector | matrix |
| **Default:** `'1'` |

### **Am** — Reference model state matrix `-1` (default) | matrix

Specify the state matrix for the reference model as a matrix with the same
dimensions as parameter **A**. For a stable reference model,
**Am** must be a Hurwitz matrix for which every eigenvalue must
have a strictly negative real part.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Am'` |
| **Type:** character vector |
| **Values:** square matrix |
| **Default:** `'-1'` |

### **Bm** — Reference model control effective matrix `1` (default) | vector | matrix

Specify the control effective matrix of the reference model as a nonzero matrix
with the same dimensions as parameter **B**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Bm'` |
| **Type:** character vector |
| **Values:** vector | matrix |
| **Default:** `'[0;4]'` |

### **Ahat** — Estimator plant model state matrix `0` (default) | square matrix

Specify the state matrix for the estimator plant model as an
*N*-by-*N* matrix, where *N* is
the number of states in the controlled system.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Ahat'` |
| **Type:** character vector |
| **Values:** square matrix |
| **Default:** `'0'` |

### **Adapt Ahat** — Option to adapt estimator plant model state matrix `on` (default) | `off`

When you select this parameter, the controller adapts the estimator plant model
state matrix.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'ALrEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Learning rate (gamma\_a)** — Learning rate for adapting estimator plant model state matrix `1` (default) | finite positive scalar

Use this parameter to control the rate at which the controller adapts the
estimator plant model state matrix. A larger value increases the size of the
updates.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, first select
the **Indirect** algorithm option. Then, select the **Adapt
Ahat** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma_a'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'1'` |

### **Use learning modification** — Option to enable learning modification for updating the estimator model state matrix `on` (default) | `off`

To add robustness at higher gains, select this option to add a momentum term to
the estimator model state matrix updates. Configure the learning modification on the
**Learning Modification** tab.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, first select
the **Indirect** algorithm option. Then, select the **Adapt
Ahat** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'ALrEnableMod'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Bhat** — Estimator plant model control effective matrix `1` (default) | vector | matrix

Specify the control effective matrix of the estimator plant model as a nonzero
*N*-by-*M* matrix, where *N* is
the number of states in the controlled system and *M* is the number
of control inputs in the controlled system.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Bhat'` |
| **Type:** character vector |
| **Values:** vector | matrix |
| **Default:** `'1'` |

### **Adapt Bhat** — Option to adapt estimator plant model control effective matrix `on` (default) | `off`

When you select this parameter, the controller adapts the estimator plant model
control effective matrix.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'BLrEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Learning rate (gamma\_b)** — Learning rate for adapting estimator plant model control effective matrix `1` (default) | finite positive scalar

Use this parameter to control the rate at which the controller adapts the
estimator plant model control effective matrix. A larger value increases the size of
the updates.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, first select
the **Indirect** algorithm option. Then, select the **Adapt
Bhat** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma_a'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'1'` |

### **Use learning modification** — Option to enable learning modification for updating the estimator model control effective matrix `on` (default) | `off`

To add robustness at higher gains, select this option to add a momentum term to
the estimator model control effective matrix updates. Configure the learning
modification on the **Learning Modification** tab.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, first select
the **Indirect** algorithm option. Then, select the **Adapt
Bhat** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'BLrEnableMod'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Specify estimator feedback gain** — Option to enable specification of estimator feedback gain `off` (default) | `on`

To specify the estimator feedback gain, first select this parameter. Then, specify
the **Estimator feedback gain** parameter.

If you do not select this parameter, the estimator uses a default feedback gain
equal to the **Am** parameter.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'externalKTauEnable'` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Estimator feedback gain** — Estimator feedback gain `-1` (default) | matrix

To use the **Am** matrix as the default estimator feedback gain,
specify this parameter as `-1`. Otherwise, specify the feedback gain
as a Hurwitz matrix with the same dimensions as **Am**.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, first select
the **Indirect** algorithm option. Then, select the
**Specify estimator feedback gain** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'k_tau'` |
| **Type:** character vector |
| **Values:** `-1` | matrix |
| **Default:** `'-1'` |

### **Output estimated parameters** — Option to output estimator state and control effective matrices `off` (default) | `on`

Select this parameter to add the **Ahat** and
**Bhat** output ports for the estimator state and control effective
matrix values, respectively.

#### Dependencies

This parameter is used for indirect MRAC. To enable this parameter, select the
**Indirect** algorithm option.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'estParamOutput'` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### Control Gains

Define initial feedback and feedforward gains for model matching when using direct MRAC.
You can configure the block to update these control gains and adjust the corresponding
learning rates. To enable the parameters on this tab, select the **Direct**
algorithm option.

### **Feedback gains** — Feedback gains for model matching `0` (default) | finite scalar | matrix of finite values

Initial feedback gain values. If you do not select the **Adapt feedback
gains** parameter, then the controller holds the specified feedback gains
at these initial values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'kx'` |
| **Type:** character vector |
| **Values:** finite scalar | matrix of finite values |
| **Default:** `'0'` |

### **Adapt feedback gains** — Option to adapt feedback gains `on` (default) | `off`

When you select this parameter, the controller adapts the feedback gains based on
the difference between the states of the controlled system and the reference
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'FBLrEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Learning rate (gamma\_x)** — Learning rate for adapting feedback gains `1` (default) | finite positive scalar

Use this parameter to control the rate at which the controller adapts the feedback
gains. A larger value increases the size of the gain updates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma_kx'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'1'` |

### **Use learning modification** — Option to enable learning modification for updating the feedback gains `on` (default) | `off`

To add robustness at higher gains, select this option to add a momentum term to
the feedback gain updates. Configure the learning modification on the
**Learning Modification** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'FBLrEnableMod'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Feedforward gains** — Feedforward gains for model matching `0` (default) | finite scalar | matrix of finite values

Initial feedforward gain values. If you do not select the **Adapt
feedforward gains** parameter, then the controller holds the specified
feedforward gains at these initial values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'kr'` |
| **Type:** character vector |
| **Values:** finite scalar | matrix of finite values |
| **Default:** `'0'` |

### **Adapt feedforward gains** — Option to adapt feedforward gains `on` (default) | `off`

When you select this parameter, the controller adapts the feedforward gains based
on the difference between the states of the controlled system and the reference
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'FFLrEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Learning rate (gamma\_r)** — Learning rate for adapting feedforward gains `1` (default) | finite positive scalar

Use this parameter to control the rate at which the controller adapts the
feedforward gains. A larger value increases the size of the gain updates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma_kr'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'1'` |

### **Use learning modification** — Option to enable learning modification for updating the feedforward gains `on` (default) | `off`

To add robustness at higher gains, select this option to add a momentum term to
the feedforward gain updates. Configure the learning modification on the
**Learning Modification** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'FFLrEnableMod'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Disturbance Model

Configure the disturbance and uncertainty model used by the block. During operation, the
block adapts the disturbance model parameters.

### **Enable disturbance adaptation** — Option to enable adaptation to system disturbances and uncertainties `on` (default) | `off`

When you select this parameter, the controller uses a disturbance model to
estimate the uncertainty and external disturbances in the controlled system. The
controller adapts the parameters of the disturbance model based on the error between
the states of the controlled system and reference model.

The disturbance model has the form
*wT**ϕ*(*x*).

- *ϕ*(*x*) is the disturbance model feature
  vector. To configure the feature vector, use the **Feature type**
  parameter.
- *wT* is a weighting matrix that
  contains disturbance model parameters. The controller adjusts its disturbance and
  uncertainty model by adapting these parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'AdaptEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Learning rate (gamma\_w)** — Learning rate for adapting disturbance model parameters `1` (default) | finite positive scalar

Use this parameter to control the rate at which the controller adapts the
disturbance model parameters. A larger value increases the size of the parameter
updates.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'100'` |

### **Use learning modification** — Option to enable learning modification for updating disturbance model parameters `on` (default) | `off`

To add robustness at higher gains, select this option to add a momentum term to
the disturbance parameter updates. Configure the learning modification on the
**Learning Modification** tab.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'WLrEnableMod'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Channel learning rate (Q)** — Channel learning rate used for the Lyapunov solution `1` (default) | finite positive scalar | vector of length *N* containing positive finite values | symmetric positive definite matrix of size *N*-by-*N*

The channel learning rate *Q* is a weighting matrix for state
tracking errors in the Lyapunov function for the error dynamics. The larger the value
of *Q*, the faster the tracking error goes to zero. However, a larger
value of *Q* also creates larger transients and a less robust
system.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Q'` |
| **Type:** character vector |
| **Values:** finite positive scalar | vector of positive values | symmetric positive definite matrix |
| **Default:** `'1'` |

### **Feature type** — Disturbance model feature type `State` (default) | `Radial Basis Function` | `Single Hidden Layer Network` | `Use External Source for Feature`

Select one of the following types for the disturbance model feature vector.

- `State` — Use the states from the controlled plant as
  the disturbance model. This option can underrepresent the uncertainty and
  therefore perform poorly.
- `Radial Basis Function` — Use Gaussian radial basis
  functions to create the feature vector.
- `Single Hidden Layer Network` — Use a neural network
  with a single-hidden layer.
- `Use External Source for Feature` — Add the
  **phi** input port to the block. Use this port to provide your
  own custom feature vector.

For more information on when to use each type of feature vector, see Disturbance and Uncertainty Model.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'FeatureTypeOptions'` |
| **Type:** character vector |
| **Values:** `'Radial Basis Function'` | `'State'` | `'Single Hidden Layer Network'` | `'Use External Source for Feature'` |
| **Default:** `'Radial Basis Function'` |

### **Number of RBF centers** — Number of radial basis function centers for disturbance model `20` (default) | positive integer

Number of radial basis function (RBF) centers to use in the disturbance model. The
RBF centers are evenly spaced across the span defined by the **Centers
min** and **Centers max** parameters.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Radial Basis Function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'nCen'` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:** `'20'` |

### **Centers min** — Lower limit for radial basis function centers `-1` (default) | finite scalar | vector

Specify the lower limits for the radial basis function centers. If you specify a
scalar value, the same minimum is used for all basis functions. Otherwise, you must
specify a vector with length equal to the **Number of RBF centers**
parameter.

The **Centers min** parameter must be less than the
**Centers max** parameter.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Radial Basis Function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'cSpanMin'` |
| **Type:** character vector |
| **Values:** finite scalar | vector |
| **Default:** `'-1'` |

### **Centers max** — Upper limit for radial basis function centers `1` (default) | finite scalar | vector

Specify the upper limits for the radial basis function centers. If you specify a
scalar value, the same maximum is used for all basis functions. Otherwise, you must
specify a vector with length equal to the **Number of RBF centers**
parameter.

The **Centers max** parameter must be greater than the
**Centers min** parameter.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Radial Basis Function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'cSpanMax'` |
| **Type:** character vector |
| **Values:** finite scalar | vector |
| **Default:** `'1'` |

### **Bandwidth** — Radial basis function standard deviation `5` (default) | positive scalar | vector

Specify the standard deviation for the Gaussian basis function kernel. If you
specify a scalar value, the same standard deviation is used for all basis functions.
Otherwise, you must specify a vector with length equal to the **Number of RBF
centers** parameter.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Radial Basis Function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'cSig'` |
| **Type:** character vector |
| **Values:** positive scalar | vector |
| **Default:** `'5'` |

### **Number of neurons in hidden layer** — Number of neurons `10` (default) | positive integer

Specify the number of neurons in the hidden layer of the neural network. In
general, a network with more neurons can approximate more complex nonlinear
disturbances. Though, too many neurons can produce a noisy disturbance
estimate.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Single Hidden Layer Network`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'shlHiddenLayerSize'` |
| **Type:** character vector |
| **Values:** positive scalar | vector |
| **Default:** `'10'` |

### **Hidden layer learning rate (gamma\_v)** — Learning rate for updating neural network weights `0.1` (default) | positive scalar

Use this parameter to control the rate at which the controller adapts the weights
of the neural network. A larger value increases the size of the weight updates.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter and set the **Feature type**
parameter to `Single Hidden Layer Network`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'gamma_V'` |
| **Type:** character vector |
| **Values:** positive scalar | vector |
| **Default:** `'0.1'` |

### **Output disturbance/uncertancy estimate** — Option to output disturbance and uncertainty estimate `on` (default) | `off`

Select this parameter to add the **u\_ad** output port.

#### Dependencies

To enable this parameter, select the **Enable disturbance
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'adaptiveCntrlOutport'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Learning Modification

To add robustness at higher gains, you can modify the parameter updates to include a
momentum term. The equations in the **Parameter Update Equations** section
show the update formulas for the current block configuration.

### **Modification Methods** — Modification method for updating parameters `None` (default) | `e-Modification` | `Sigma Modification`

Select one of the following options for computing the momentum term that is added
to the parameter updates.

- `Sigma Modification` — The momentum term is the
  product of the momentum weight parameter *σ* and the current
  parameter values.
- `e-Modification` — Scale the sigma-modification
  momentum term by the magnitude of the error value
- `None` — Do not use learning modification.

To specify *σ*, use the **Sigma**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'modChoice'` |
| **Type:** character vector |
| **Values:** `'Sigma Modification'` | `'e-Modification'` | `'None'` |
| **Default:** `'Sigma Modification'` |

### **Sigma** — Momentum weight for parameter updates `0.1` (default) | scalar

Specify the value for the momentum weight term. A larger value increases the size
of the parameter updates gain and parameter updates.

#### Dependencies

To enable this parameter, set the **Modification Methods**
parameter to either `Sigma Modification` or
`e-Modification`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'sigma_val'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'0.1'` |

### **Use discrete-time integration in adaptation** — Use discrete-time integration in adaptation `off` (default) | `on`

*Since R2024b*

Select to use discrete-time integration for parameter updates. Doing so allows you
to generate code for embedded systems that require a user-specified sample
time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'DiscreteEnable'` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Sample time** — Sample time `0.05` (default) | finite positive scalar

*Since R2024b*

Sample time for discrete-time integration, specified as a finite positive
scalar.

#### Dependencies

To enable this parameter, select the **Use discrete-time integration in
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Ts'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'0.05'` |

### **Integration method** — Discrete integration method `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

*Since R2024b*

Specify the discrete integration formula for calculating the integral in parameter
update equations as one of the following:

- `Forward Euler` — Tsz−1
- `Backward Euler` — Tszz−1
- `Trapezoidal` — Ts2z+1z−1

#### Dependencies

To enable this parameter, select the **Use discrete-time integration in
adaptation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'IntegrationMethods'` |
| **Type:** character vector |
| **Values:** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **Default:** `'Forward Euler'` |

## Libraries

Simulink Control Design / Adaptive Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2024b: Support for embedded code generation

You can now configure the Model Reference Adaptive Control block to use discrete-time
integration for parameter updates. Doing so allows you to generate code for embedded systems
that require a user-specified sample time. To use discrete-time integration, on the
**Learning Modification** tab, enable **Use discrete-time integration in adaptation**. You can then specify a desired
sample time and discrete integration method for parameter updates.

### R2023b: Library location changed

The Model Reference Adaptive Control block is now in the
**Simulink Control Design/Adaptive Control** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links for
Model Reference Adaptive Control blocks update automatically.

### R2023a: Single hidden layer disturbance model

You can now model disturbances and uncertainty in your system using a single hidden
layer (SHL) neural network. An SHL neural network is a universal function approximator,
which can be useful for modeling unstructured uncertainty in your system.

To learn the disturbance model, the MRAC controller adapts the weights of the hidden
layer and output layer of the neural network. You can configure the SHL neural network model
by specifying the number of neurons in the hidden layer and the learning rate.

### R2022a: Indirect model reference adaptive control

The Model Reference Adaptive Control block now supports indirect model
reference adaptive control (MRAC). Previously, the block supported only direct MRAC.

Direct MRAC computes control actions to make an uncertain controlled system track the
behavior of a given reference plant model. However, indirect MRAC estimates the parameters
of the uncertain system and derives the control signal based on the estimated
parameters.

## Description

Compute control actions to make controlled system track reference model

The Model Reference Adaptive Control block computes control actions to make
an uncertain controlled system track the behavior of a given reference plant model. Using this
block, you can implement the following model reference adaptive control (MRAC) algorithms.

- Direct MRAC — Estimate the following controller gains and compute control actions
  using the estimated controller.

  - Feedback gains that relate the state of the controlled system to the control
    signal.
  - Feedforward gains that relate the reference signal to the control signal.
- Indirect MRAC — Estimate the following matrices of the uncertain controlled system and
  derive control actions based on the estimated model.

  - State matrix *A*
  - Control effective matrix *B*

Both direct and indirect MRAC also estimate a model of the external disturbances and
uncertainty in the system being controlled and use this model when computing control
actions.

In both cases, based on the real-time tracking error, the controller can update the
estimated parameters and disturbance model.

For more information, see Model Reference Adaptive Control.
