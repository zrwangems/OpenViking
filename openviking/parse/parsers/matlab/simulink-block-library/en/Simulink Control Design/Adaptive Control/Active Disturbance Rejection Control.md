---
type: simulink-block
title: 'Active Disturbance Rejection Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'activedisturbancerejectioncontrol'
documentation_source_path: 'ug/activedisturbancerejectioncontrol.html'
language: en
---

# Active Disturbance Rejection Control

## Ports

### Input

### **r** — Reference signal scalar

Provide the reference signal for the controlled system to
follow.

### **y** — Plant output scalar

Provide the output signal of the plant.
### Output

### **u** — Control input scalar

Connect the control input signal to the plant input.

### **xhat** — Estimated extended states vector

Estimated extended states of the plant model from the extended state
observer.

If the **Model type** is
**first-order**, **xhat** is a
vector of length two, with estimated states y^ and f^(t).

If the **Model type** is
**second-order**, **xhat** is a
vector of length three, with estimated states y^, y˙^, and f^(t).

#### Dependencies

To enable this output port, select the **Estimated extended states**
parameter.

## Parameters

### Parameters Tab

### **Time domain** — Controller time domain **discrete-time** (default) | **continuous-time**

Specify the controller time domain.

When you select **discrete-time**, specify the sample
time using the **Sample time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'time_domain'` |
| **Type:** character vector |
| **Values:** `'discrete-time'` | `'continuous-time'` |
| **Default:** `'discrete-time'` |

### **Sample time** — Controller sample time `0.01` (default) | finite positive scalar

Specify the sample time value for the discrete-time controller.

#### Dependencies

To enable this parameter, set the **Time domain**
parameter to **discrete-time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'Ts'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'0.01'` |

### **Model type** — Plant order type **first-order** (default) | **second-order**

Specify the model type of your plant as one of the following.

- **first-order** — Select this option if your
  plant exhibits first-order dynamic system behavior.
- **second-order** — Select this option if your
  plant exhibits second-order dynamic system behavior.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'model_type'` |
| **Type:** character vector |
| **Values:** `'first-order'` | `'second-order'` |
| **Default:** `'first-order'` |

### **Critical gain** — Critical gain `1` (default) | finite nonzero scalar

Specify the critical gain *b*0
that describes the model behavior.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'b0'` |
| **Type:** character vector |
| **Values:** finite nonzero scalar |
| **Default:** `'1'` |

### **Controller bandwidth (rad/sec)** — Controller bandwidth `1` (default) | finite positive scalar

Specify the controller bandwidth. This parameter determines the speed
of the controller response. In general, a faster response requires a
larger controller bandwidth.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'wc'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'1'` |

### **Observer bandwidth (rad/sec)** — Observer bandwidth `10` (default) | finite positive scalar

Specify the observer bandwidth. Typically, this is set to 5 to 10
times the controller bandwidth so that the observer converges faster
than the controller.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'wo'` |
| **Type:** character vector |
| **Values:** finite positive scalar |
| **Default:** `'10'` |

### Block Tab

### **Initial conditions** — Initial state values for extended state observer `0` (default) | scalar | vector

Specify the initial state values for extended state observer as a
scalar or vector of length *n*.

If **Model type** is
**first-order**, *n* = 2.
Otherwise, *n* = 3.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'x0'` |
| **Type:** character vector |
| **Values:** finite scalar | vector |
| **Default:** `'0'` |

### **Limit output (u)** — Limit block output to specified saturation limits `off` (default) | `on`

Option to limit block output to specified saturation limits. Specify
the output saturation limits using the **Upper limit**
and **Lower limit** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'ulim_checkbox'` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Upper limit** — Upper saturation limit for block output `inf` (default) | scalar

Specify the upper limit for the block output. The block output is held
at this value whenever it would otherwise exceed this value.

#### Dependencies

To enable this parameter, select the **Limit
output** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'umax'` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'inf'` |

### **Lower limit** — Lower saturation limit for block output `–inf` (default) | scalar

Specify the lower limit for the block output. The block output is held
at this value whenever it would otherwise go below this value.

#### Dependencies

To enable this parameter, select the **Limit
output** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'umin'` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'–inf'` |

### **Estimated extended states (xhat)** — Output estimated states from observer `off` (default) | `on`

Option to output states from the extended state observer.

If the **Model type** is
**first-order**, the block outputs y^ and f^(t).

If the **Model type** is
**second-order**, the block outputs y^, y˙^, and f^(t).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'xhat_checkbox'` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Libraries

Simulink Control Design / Adaptive Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2023b: Library location changed

The Active Disturbance Rejection Control block is now in the
**Simulink Control Design/Adaptive Control** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links
for Active Disturbance Rejection Control blocks update
automatically.

## Description

Design controller for plants with unknown dynamics and disturbances

The Active Disturbance Rejection Control block lets you design active
disturbance rejection control (ADRC) for a plant with unknown dynamics and internal and
external disturbances. ADRC is a model-free control technique that requires only an
approximation of the plant dynamics to design controllers that provide robust
disturbance rejection.

The block uses a first-order or second-order model approximation of the known system
dynamics along with the unknown dynamics and disturbances modeled as an extended state
of the plant. Typically, you determine this order from the open-loop step response of
your plant in the operating range.

- First-order approximation — y˙(t)=b0u(t)+f(t)
- Second-order approximation — y¨(t)=b0u(t)+f(t)

Here:

- *y*(*t*) is the plant output.
- *u*(*t*) is the input signal.
- *b*0 is the critical gain, which is
  the estimated gain that describes the plant response to an input
  *u*(*t*).
- *f*(*t*) is the total disturbance, which
  includes unknown dynamics and other disturbances.

The block uses an extended state observer (ESO) to estimate
*f*(*t*) and implements disturbance rejection
control by reducing the effect of estimated disturbances on the known part of model
approximation. To tune ADRC, set appropriate time domain, model type and critical gain,
controller and observer bandwidths, and initial conditions.

For more information, see Active Disturbance Rejection Control.
