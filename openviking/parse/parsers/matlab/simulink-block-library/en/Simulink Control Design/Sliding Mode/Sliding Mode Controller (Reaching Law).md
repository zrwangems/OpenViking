---
type: simulink-block
title: 'Sliding Mode Controller (Reaching Law)'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Sliding Mode'
documentation_page: 'slidingmodecontrollerreachinglaw'
documentation_source_path: 'ug/slidingmodecontrollerreachinglaw.html'
language: en
---

# Sliding Mode Controller (Reaching Law)

## Ports
```yaml
ports:
- name: x
  summary: System states vector
  direction: input
  data_types: single | double
- name: f(x)
  summary: System dynamics function vector
  direction: input
  data_types: single | double
- name: g(x)
  summary: Input function vector
  direction: input
  data_types: single | double
- name: x.ref
  summary: State reference trajectories vector
  direction: input
- name: x.ref.dot
  summary: Derivative of state reference trajectories vector
  direction: input
- name: u
  summary: Control action vector
  direction: output
- name: s(x)
  summary: Sliding variable value vector
  direction: output
```

### Input

### **x** — System states vector

System states, specified as an
*nx*-by-1 signal, where
*nx* is the number of
states.

**Data Types:** `single` | `double`

### **f(x)** — System dynamics function vector

System dynamics function *f*(*x*) in
the systems characterized by the equation x˙=f(x)+g(x)u.

Connect this port to an
*nx*-by-1 signal, where
*nx* is the number of
states.

**Data Types:** `single` | `double`

### **g(x)** — Input function vector

Input function *g*(*x*) in the
systems characterized by the equation x˙=f(x)+g(x)u.

Connect this port to an
*nx*-by-*nu*
signal, where *nx* is the number
of states and *nu* is the number
of inputs.

**Data Types:** `single` | `double`

### **x.ref** — State reference trajectories vector

State reference trajectory to follow in the tracking mode, specified
as an *nx*-by-1 signal, where
*nx* is the number of
states.

#### Dependencies

To enable this port, set **Task Mode** to **Tracking
Mode**.

### **x.ref.dot** — Derivative of state reference trajectories vector

Derivative of state reference trajectory to follow in the tracking
mode, specified as an *nx*-by-1
signal, where *nx* is the number
of states.

Use this port when you want to provide the derivative of state
reference trajectories from an external input. Otherwise, the block
computes the derivative during simulation.

#### Dependencies

To enable this port:

- Set **Task Mode** to **Tracking
  Mode**.
- Enable **Use externally sourced
  derivative**.
### Output

### **u** — Control action vector

Computed control action, returned as an
*nu*-by-1 signal, where
*nu* is the number of
inputs.

### **s(x)** — Sliding variable value vector

Sliding variable value, returned as an *nu*-by-1
signal, where *nu* is the number
of inputs.

#### Dependencies

To enable this port, enable the **Output Switching
Function** parameter.
## Parameters
```yaml
parameters:
- name: Task Mode
  summary: Block operation mode Regulation Mode (default) | Tracking Mode
  group: Sliding Surface Tab
  block_parameter: TaskMode
  values: '"Regulation Mode" (default) | "Tracking Mode"'
- name: Sliding Coefficient Matrix (C)
  summary: Sliding coefficient matrix 1 (default) | scalar | column vector | matrix
  group: Sliding Surface Tab
  block_parameter: SlidingMatrix
  values: 1 (default) | scalar in quotes | column vector in quotes | matrix in quotes
- name: Use externally sourced derivative
  summary: Specify derivative of state reference externally off (default) | on
  group: Sliding Surface Tab
  block_parameter: EnableTrackingDerivative
  values: '"off" (default) | "on"'
- name: Output Switching Function
  summary: Output switching function off (default) | on
  group: Sliding Surface Tab
  block_parameter: EnableSwitchingFunction
  values: '"off" (default) | "on"'
- name: Reaching Law
  summary: Reaching law Constant Rate (default) | Exponential | Power Rate
  group: Reaching Law Tab
  block_parameter: ReachingLaw
  values: '"Constant Rate" (default) | "Exponential" | "Power Rate"'
- name: Reaching Rate (Eta)
  summary: Reaching rate 0.01 (default) | positive scalar | column vector
  group: Reaching Law Tab
  block_parameter: ReachingRate
  values: '"0.01" (default) | positive scalar in quotes | column vector in quotes'
- name: Control Gain (K)
  summary: Control gain 0.01 (default) | positive scalar | column vector
  group: Reaching Law Tab
  block_parameter: ControlGain
  values: '"0.01" (default) | positive scalar in quotes | column vector in quotes'
- name: Power Rate Exponent (Alpha)
  summary: Power rate exponent 0.01 (default) | positive scalar between 0 and 1 | column vector of positive values between
    0 and 1
  group: Reaching Law Tab
  block_parameter: PowerRate
  values: '"0.01" (default) | positive scalar between 0 and 1 in quotes | column vector of positive values between 0 and 1
    in quotes'
- name: Select Boundary Layer
  summary: Boundary layer function Sign (default) | Relay | Hyperbolic Tangent | Saturation
  group: Reaching Law Tab
  block_parameter: BoundaryLayer
  values: '"Sign" (default) | "Relay" | "Hyperbolic Tangent" | "Saturation"'
- name: Enable zero-crossing detection
  summary: Enable zero-crossing detection off (default) | on
  group: Reaching Law Tab
  block_parameter: ZeroCross
  values: '"off" (default) | "on"'
- name: Phi
  summary: Boundary layer thickness 0.01 (default) | positive scalar | column vector
  group: Reaching Law Tab
  block_parameter: Phi
  values: '"0.01" (default) | positive scalar in quotes | column vector in quotes'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Sliding Surface Tab

### **Task Mode** — Block operation mode **Regulation Mode** (default) | **Tracking Mode**

Block operation mode, specified as one of the following:

- **Regulation Mode** — Use this mode when
  you want to stabilize the system at a fixed point, that is,
  bring all the states *x* to zero.
- **Tracking Mode** — Use this mode when you
  want the system states to follow a reference trajectory
  *xref*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TaskMode` |
| **Values:** | `"Regulation Mode"` (default) | `"Tracking Mode"` |

**Example:** `set_param(gcb,"TaskMode","Tracking
Mode")`

### **Sliding Coefficient Matrix (C)** — Sliding coefficient matrix `1` (default) | scalar | column vector | matrix

Sliding coefficient matrix (*C*), specified as an
*nx*-by-*nu*
matrix, where *nx* is the number
of states and *nu* is the number
of control inputs.

The matrix *C* determines the hyperplane to which the sliding mode
control drives the system states.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SlidingMatrix` |
| **Values:** | `1` (default) | scalar in quotes | column vector in quotes | matrix in quotes |

**Example:** `set_param(gcb,"SlidingMatrix","[1;2]")`

### **Use externally sourced derivative** — Specify derivative of state reference externally `off` (default) | `on`

Select to specify the derivative of state reference signal externally
at the input port **x.ref.dot**.

#### Dependencies

To enable this parameter, set **Task Mode** to **Tracking
Mode**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EnableTrackingDerivative` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,"EnableTrackingDerivative","on")`

### **Output Switching Function** — Output switching function `off` (default) | `on`

Select to return the sliding surface value at an output port
**s(x)**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EnableSwitchingFunction` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,"EnableSwitchingFunction","on")`

### Reaching Law Tab

### **Reaching Law** — Reaching law `Constant Rate` (default) | `Exponential` | `Power Rate`

Reaching law
*h*(*s*(*x*)) for
the sliding surface, specified as one of the following.

- `Constant Rate` — h(s(x))=−ηiθ(si)

  This law provides a constant rate to reach the sliding
  surface. Here,
  *θ*(*si*)
  is the boundary layer and
  *ηi* is the reaching
  rate of the *i*th control input.
- `Exponential` — h(s(x))=−ηiθ(si)−Kisi

  This law adds a term proportional to the sliding variable and
  provides a more aggressive convergence when the state deviation
  is significant. Here,
  *Ki* is the control
  gain term that scales the control effort associated with the
  *i*th sliding variable.
- `Power Rate` — h(s(x))i=−ηi|si|αθ(si)

  This law provides fast reaching speed when the state is far
  away from the sliding surface, but reduces the speed as the
  state gets near. This ensures reduced chattering and provides
  fast convergence.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ReachingLaw` |
| **Values:** | `"Constant Rate"` (default) | `"Exponential"` | `"Power Rate"` |

**Example:** `set_param(gcb,"ReachingLaw","Power
Rate")`

### **Reaching Rate (Eta)** — Reaching rate `0.01` (default) | positive scalar | column vector

Reaching rate (*η*), specified as a positive scalar
or a column vector of positive values with length equal to the number of
control inputs.

Reaching rate determines the rate at which the system trajectory
approaches the sliding surface. A larger value of *η*
results in a faster convergence to the sliding surface but can also lead
to higher control effort, which is not desirable in all cases due to
potential issues like actuator saturation or increased
chattering.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ReachingRate` |
| **Values:** | `"0.01"` (default) | positive scalar in quotes | column vector in quotes |

**Example:** `set_param(gcb,"ReachingRate","0.05")`

### **Control Gain (K)** — Control gain `0.01` (default) | positive scalar | column vector

Control gain of the proportional term in the exponential reaching law, specified as a
positive scalar or column vector of length equal to the number of
control inputs. In the exponential reaching law, this term increases the
control effort proportional to the deviation from the sliding
surface.

#### Dependencies

To enable this parameter, set **Reaching Law** to
`Exponential`.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ControlGain` |
| **Values:** | `"0.01"` (default) | positive scalar in quotes | column vector in quotes |

**Example:** `set_param(gcb,"ControlGain","2")`

### **Power Rate Exponent (Alpha)** — Power rate exponent `0.01` (default) | positive scalar between 0 and 1 | column vector of positive values between 0 and 1

Exponent value in the power rate reaching law, specified as a positive
scalar between 0 and 1 or column vector of length equal to the number of
control inputs. This parameter determines the nonlinearity of the
control action with respect to the distance from the sliding surface.
Specifically, it adjusts how the control effort scales with the
magnitude of the sliding variable. The value of *α*
influences the smoothness of the approach to the sliding surface. The
lower values lead to a softer approach and potentially reduce
chattering.

#### Dependencies

To enable this parameter, set **Reaching Law** to
`Power Rate`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PowerRate` |
| **Values:** | `"0.01"` (default) | positive scalar between 0 and 1 in quotes | column vector of positive values between 0 and 1 in quotes |

**Example:** `set_param(gcb,"PowerRate","0.02")`

### **Select Boundary Layer** — Boundary layer function `Sign` (default) | `Relay` | `Hyperbolic Tangent` | `Saturation`

Boundary layer function, specified as one of the following:

- `Sign` — θ(s)=sgn(s(x))

  This option uses the default signum function and switches
  between –1 and 1 discontinuously.
- `Relay` — θ(s)=s|s|+ϕ

  This option uses a relay function to define the switching
  boundary around the sliding surface.
- `Hyperbolic Tangent` — θ(s)=tanh(sϕ)

  This option uses a hyperbolic tangent function to define the
  switching boundary around the sliding surface.
- `Saturation` — θ(s)={1s>ϕkss≤ϕ−1s<−ϕk=1ϕ

  This option uses a saturation function to smoothly interpolate
  between –1 and 1 when the sliding variable is within the
  boundary layer [*–ϕ*,*ϕ*],
  which reduces the high-frequency switching.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BoundaryLayer` |
| **Values:** | `"Sign"` (default) | `"Relay"` | `"Hyperbolic Tangent"` | `"Saturation"` |

**Example:** `set_param(gcb,""BoundaryLayer,"Saturation")`

### **Enable zero-crossing detection** — Enable zero-crossing detection `off` (default) | `on`

Select to enable zero-crossing detection. For more information, see
Zero-Crossing Detection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ZeroCross` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,"ZeroCross","on")`

### **Phi** — Boundary layer thickness `0.01` (default) | positive scalar | column vector

Boundary layer thickness parameter, specified as a positive scalar or
column vector of length equal to the number of control inputs.

This parameter defines the boundary layer thickness around the sliding
surface. A larger **Phi** value results in less
chattering but can increase the steady-state error. Conversely, a
smaller **Phi** value can reduce steady-state error but
increase chattering.

#### Dependencies

To enable this parameter, set **Select Boundary
Layer** to any one of these values:

- `Relay`
- `Hyperbolic Tangent`
- `Saturation`

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Phi` |
| **Values:** | `"0.01"` (default) | positive scalar in quotes | column vector in quotes |

**Example:** `set_param(gcb,"Phi","0.05")`
## Libraries

Simulink Control Design / Sliding Mode

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Design sliding mode controller based on reaching law

Sliding Mode Control (SMC) is a robust control strategy that brings the system state
trajectory to a specified sliding surface and maintains it there. This approach is
advantageous for systems requiring high levels of precision and robustness, especially
in the presence of disturbances and uncertainties. Once the system reaches the sliding
surface, SMC ensures that it stays on this path despite any external or internal changes
to system dynamics.

The Sliding Mode Controller block enables you to implement SMC for
nonlinear systems characterized by the equation x˙=f(x)+g(x)u. Using this block, you can create a compensator which uses a reaching
law, a method that dynamically adjusts control actions to guide the system states toward
the sliding surface efficiently. The block provides the following two modes of
operation:

- Regulation mode

  u=(CTg(x))−1(−CTf(x)+h(s(x)))s(x)=CTx
- Tracking mode

  u=(CTg(x))−1(CTx˙ref−CTf(x)+h(s(x)))s(x)=CT(xref−x)

Here, *C* is the sliding coefficient matrix,
*s*(*x*) is the switching function, and
*h*(*s*(*x*)) is the reaching
law.

Additionally, SMC minimizes chattering effects, a common challenge in control systems
characterized by rapid oscillation or high-frequency switching of the control signal.
The block allows you to customize the sliding surface and adjust the reaching law
parameters. This enables you to tune the control strategy to your specific system
dynamics and objectives, enhancing the system stability and response under varying
conditions.

For more information about SMC, see Sliding Mode Control.
