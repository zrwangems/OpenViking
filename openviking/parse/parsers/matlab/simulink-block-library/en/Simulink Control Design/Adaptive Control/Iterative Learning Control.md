---
type: simulink-block
title: 'Iterative Learning Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'iterativelearningcontrol'
documentation_source_path: 'ug/iterativelearningcontrol.html'
language: en
---

# Iterative Learning Control

## Ports
```yaml
ports:
- name: error
  summary: Error signal scalar | vector
  direction: input
  data_types: single | double
- name: control/reset
  summary: ILC mode signal scalar
  direction: input
  data_types: Boolean
- name: u
  summary: Updated control signal scalar | vector
  direction: output
  data_types: single | double
```

### Input

### **error** — Error signal scalar | vector

Specify the error between the desired reference signal and output at
this port.

**Data Types:** `single` | `double`

### **control/reset** — ILC mode signal scalar

Specify the ILC mode signal at this port. At runtime, the block
switches between two modes: control and reset. In the control mode, the
block outputs
*uk*(*t*)
at the specified time points and measures the error between the desired
reference *r*(*t*) and output
*yk*(*t*).
At the end of the control mode, the block calculates the new control
sequence
*uk+1*(*t*)
to use in the next iteration. In the reset mode, the block output is 0.

Typically, you can use a signal that changes from 0 to 1 to switch to the control mode,
and from 1 to 0 to switch to the reset mode. The reset mode must be long
enough such that the reference signal in this mode brings the plant back
to its initial condition by the nominal controller.

**Data Types:** `Boolean`
### Output

### **u** — Updated control signal scalar | vector

Updated control signal for the *k*th iteration. The
block outputs
*uk*(*t*)
at the specified time points and measures the error between the desired
reference and output.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Sample time (Ts)
  summary: ILC sample time 0.01 (default) | positive scalar
  group: ''
  block_parameter: Ts
  values: '"0.01" (default) | positive scalar in quotes'
- name: Iteration duration (Tspan)
  summary: Iteration duration 1 (default) | positive scalar
  group: ''
  block_parameter: Tspan
  values: '"1" (default) | positive scalar in quotes'
- name: Data Type
  summary: Data type double (default) | single | <data type expression>
  group: ''
- name: ILC Algorithm
  summary: ILC algorithm Model free ILC (default) | Model based ILC
  group: ''
  block_parameter: Algorithm
  values: '"Model free ILC" (default) | "Model based ILC"'
- name: P-gain (gamma_p)
  summary: Proportional gain in model-free ILC 1 (default) | nonnegative scalar
  group: ''
  block_parameter: gamma_p
  values: '"1" (default) | nonnegative scalar in quotes'
- name: D-gain (gamma_d)
  summary: Derivative gain in model-free ILC 0 (default) | nonnegative scalar
  group: ''
  block_parameter: gamma_d
  values: '"0" (default) | nonnegative scalar in quotes'
- name: State Space Model
  summary: Model time domain Continuous time (default) | Discrete time (Ts)
  group: ''
  block_parameter: ModelTimeDomain
  values: '"Continuous time" (default) | "Discrete time (Ts)"'
- name: A, B, C
  summary: State-space model matrices 1 (default) | matrix
  group: ''
- name: ILC methods
  summary: Model-based ILC method Gradient based (default) | Inverse-model based
  group: ''
  block_parameter: ModelBasedILCType
  values: '"Gradient based" (default) | "Inverse-model based"'
- name: ILC Gain (gamma_gradient)
  summary: Gradient-based ILC gain 1 (default) | positive scalar
  group: ''
  block_parameter: gamma_grad
  values: '"1" (default) | positive scalar in quotes'
- name: ILC Gain (gamma_inverse)
  summary: Inverse-model-based ILC gain 1 (default)
  group: ''
  block_parameter: gamma_inverse
  values: '"1" (default) | positive scalar less than 2 in quotes'
- name: Enable first-order low-pass filter
  summary: Enable first-order low-pass filter off (default) | on
  group: ''
  block_parameter: LPFEnable
  values: '"off" (default) | "on"'
- name: Filter time constant (tau)
  summary: Filter time constant 1 (default) | positive scalar
  group: ''
  block_parameter: tau
  values: '"1" (default) | positive scalar in quotes'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample time (Ts)** — ILC sample time `0.01` (default) | positive scalar

Sample time of the ILC controller, specified as a positive scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **Values:** | `"0.01"` (default) | positive scalar in quotes |

**Example:** `set_param(gcb,"Ts","0.1")`

### **Iteration duration (Tspan)** — Iteration duration `1` (default) | positive scalar

Duration of one ILC iteration, specified as a positive scalar. This parameter determines
how many control actions the block provides in the control mode.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tspan` |
| **Values:** | `"1"` (default) | positive scalar in quotes |

**Example:** `set_param(gcb,"Tspan","10")`

### **Data Type** — Data type `double` (default) | `single` | `<data type expression>`

Specify the output data type.

The **Data Type Assistant** helps you set
data attributes. To use the **Data Type
Assistant**, click .

You can specify the following data types.

- `Built in` —
  `single` or
  `double` data types.
- `Expression` — Use a MATLAB expression
  that specifies the type.

For more information, see Specify Data Types Using Data Type Assistant.

### **ILC Algorithm** — ILC algorithm **Model free ILC** (default) | **Model based ILC**

ILC algorithm, specified as **Model free ILC** or
**Model based ILC**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Algorithm` |
| **Values:** | `"Model free ILC"` (default) | `"Model based ILC"` |

**Example:** `set_param(gcb,"Algorithm","Model based
ILC")`

### **P-gain (gamma\_p)** — Proportional gain in model-free ILC `1` (default) | nonnegative scalar

Proportional gain (*γp*) in the
model-free ILC update law, specified as a nonnegative scalar. The model-free
ILC update law is defined as follows:

uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t))).

#### Dependencies

To enable this parameter, set **ILC Algorithm** to
**Model free ILC**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma_p` |
| **Values:** | `"1"` (default) | nonnegative scalar in quotes |

**Example:** `set_param(gcb,"gamma_p","5")`

### **D-gain (gamma\_d)** — Derivative gain in model-free ILC `0` (default) | nonnegative scalar

Derivative gain *γd* in the
model-free ILC update law, specified as a nonnegative scalar. The model-free
ILC update law is defined as follows:

uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t))).

#### Dependencies

To enable this parameter, set **ILC Algorithm** to
**Model free ILC**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma_d` |
| **Values:** | `"0"` (default) | nonnegative scalar in quotes |

**Example:** `set_param(gcb,"gamma_d","1")`

### **State Space Model** — Model time domain **Continuous time** (default) | **Discrete time (Ts)**

Time domain of the state-space model in model-based ILC, specified as
**Continuous time** or **Discrete time
(Ts)**. The sample time of the model must be equal to the ILC
sample time specified using the **Sample time
(Ts)**.

#### Dependencies

To enable this parameter, set **ILC Algorithm** to
**Model based ILC**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ModelTimeDomain` |
| **Values:** | `"Continuous time"` (default) | `"Discrete time (Ts)"` |

**Example:** `set_param(gcb,"ModelTimeDomain","Discrete time
(Ts)")`

### **A**, **B**, **C** — State-space model matrices `1` (default) | matrix

Specify the matrices of the nominal or approximate state-space model for
the model-based ILC algorithm. The block requires you to specify the plant
dynamics in the following form:

x(t+1)=Ax(t)+Bu(t)y(t)=Cx(t).

#### Dependencies

To enable these parameters, set **ILC Algorithm** to
**Model based ILC**.

### **ILC methods** — Model-based ILC method **Gradient based** (default) | **Inverse-model based**

Model-based ILC method, specified as **Gradient based**
or **Inverse-model based**.

#### Dependencies

To enable this parameter, set **ILC Algorithm** to **Model
based ILC**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ModelBasedILCType` |
| **Values:** | `"Gradient based"` (default) | `"Inverse-model based"` |

**Example:** `set_param(gcb,"ModelBasedILCType","Inverse-model
based")`

### **ILC Gain (gamma\_gradient)** — Gradient-based ILC gain `1` (default) | positive scalar

Gradient-based ILC gain, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **ILC Algorithm** to **Model
based ILC** and **ILC methods** to
**Gradient based**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma_grad` |
| **Values:** | `"1"` (default) | positive scalar in quotes |

**Example:** `set_param(gcb,"gamma_grad","2")`

### **ILC Gain (gamma\_inverse)** — Inverse-model-based ILC gain `1` (default)

Inverse-model-based ILC gain, specified as a positive scalar less than
2.

#### Dependencies

To enable this parameter, set **ILC Algorithm** to **Model
based ILC** and **ILC methods** to
**Inverse-model based**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma_inverse` |
| **Values:** | `"1"` (default) | positive scalar less than 2 in quotes |

**Example:** `set_param(gcb,"gamma_inverse","1.5")`

### **Enable first-order low-pass filter** — Enable first-order low-pass filter `off` (default) | `on`

Select this parameter to apply a first-order low-pass filter to the ILC
update law.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LPFEnable` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,"LPFEnable","on")`

### **Filter time constant (tau)** — Filter time constant `1` (default) | positive scalar

Time constant of the first-order low-pass filter, specified as a positive
scalar.

#### Dependencies

To enable this parameter, select **Enable first-order low-pass
filter**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau` |
| **Values:** | `"1"` (default) | positive scalar in quotes |

**Example:** `set_param(gcb,"tau","10")`
## Libraries

Simulink Control Design / Adaptive Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Design iterative learning controller for repetitive control tasks

Iterative learning control (ILC) is an improvement in run-to-run control. This method uses
frequent measurements in the form of the error trajectory from the previous batch run to
update the control signal for the subsequent batch run. ILC improves the performance of
systems that execute repeated operations, starting at the same initial operating
condition. You can use ILC in many practical industrial systems in manufacturing,
robotics, and chemical processing, where mass production on an assembly line requires
repetition.

The Iterative Learning Control block provides the following
configurations:

- Model-free ILC — This method does not require prior knowledge of the system
  dynamics and uses proportional-derivative (PD) error feedback to update the
  control history. The model-free ILC update law is:

  uk+1(t)=Q(q)(uk(t)+γpek(t+1)+γd(ek(t+1)−ek(t))).

  Here, *γp* is the proportional gain,
  *γd* is the derivative gain, and
  *Q*(*q*) is the first-order low-pass
  filter. Depending on the choice of PD gain, you can choose to implement P-type,
  D-type, or PD-type ILC. This method is applicable only to SISO systems.
- Model-based ILC — This method is a more general form of ILC and is applicable
  to continuous-time and discrete-time LTI state-space systems of the following
  form:

  xk(t+1)=Axk(t)+Buk(t),x(0)=x0,yk(t)=Cxk(t).

  Additionally, this method allows you to use either of the following two update
  methods:

  - Gradient-based ILC — uk+1(t)=Q(q)(uk(t)+γGTek(t))
  - Inverse-model based ILC — uk+1(t)=Q(q)(uk(t)+γG−1ek(t))

For more information about ILC, see Iterative Learning Control.
