---
type: simulink-block
title: 'PID Gains Store and Update'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / PID Controller Tuning / Real-Time PID Autotuning'
documentation_page: 'pidgainsstoreandupdate'
documentation_source_path: 'ug/pidgainsstoreandupdate.html'
language: en
---

# PID Gains Store and Update

## Ports

### Input

### **tuned Gains** — Tuned PID gains bus

Specify the tuned PID gain values to store and route. Typically, you obtain these tuned
gains from the Closed-Loop PID Autotuner block.

This 4-element bus signal must contain the tuned PID gains
*P*, *I*, *D*,
and the filter coefficient *N*. These values correspond
to the `P`, `I`, `D`,
and `N` parameters in the expressions given in the
**Controller type** parameter. During autotuning,
initially, the values are 0, 0, 0, and 100, respectively. The
Closed-Loop PID Autotuner block updates the values
when the experiment ends. This bus signal always has four elements, even
if you are not tuning a PIDN controller.

### **scheduling Variable** — Scheduling variable scalar

Specify the scheduling variable. This signal indicates where in the operating range the
system is at a given time.

This signal also dictates when the gains change in a gain-scheduled
control application.

#### Dependencies

To enable this port, select **Use for gain
scheduling**.

### **Breakpoints** — Breakpoint data vector

Breakpoint data for gain scheduling, specified as a vector.

#### Dependencies

To enable this port, select **Use external
signal**.

### **Update Trigger** — Trigger control signal scalar

Control signal to trigger the update of gains.

#### Dependencies

To enable this port, set **Method to trigger gain
update** to **External
trigger**.
### Output

### **PID Gains Out** — PID gain array bus

Stored PID gain array. Use this gain array along with the breakpoint data to implement
lookup table based gain scheduling.

Use this port to specify a custom logic to route the gain
array.

To enable this port, set **Method of storing gains** to
`Output from block`.

## Parameters

### **Controller type** — PID controller type `P` (default) | `I` | `PI` | `PD` | `PDN` | `PID` | `PIDN`

Specify the type of the PID controller in your system. The controller type
indicates what actions are present in the controller. The following
controller types are available:

- `P` — Proportional only
- `I` — Integral only
- `PI` — Proportional and integral
- `PD` — Proportional and derivative
- `PDN` — Proportional and derivative with
  derivative filter
- `PID` — Proportional, integral, and
  derivative
- `PIDN` — Proportional, integral, and
  derivative with derivative filter

When you update a PID Controller block or custom PID
controller with tuned parameter values, make sure the controller type
matches.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ControllerType` |
| **Type:** string |
| **Values:** `"P"` | `"I"` | `"PI"` | `"PD"` | `"PDN"` | `"PID"` | `"PIDN"` |
| **Default:** `"PID"` |

### **Use for gain scheduling** — Enable block for gain scheduling `on` (default) | `off`

Use this option to enable the block for gain-scheduling applications.
Doing so allows you to specify breakpoints used with gain lookup.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseGainScheduling` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"on"` |

### **Save breakpoints in gain array** — Save breakpoints along with PID gains `off` (default) | `on`

Use this option to save breakpoints along with the stored gain array. The
PID Gain Scheduler block can interpret this combined data
for gain-scheduling applications.

#### Dependencies

To enable this parameter, select **Use for gain
scheduling**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaveBreakpoints` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Breakpoints** — Gain scheduling breakpoints `[1 2 3]` (default) | vector

Specify the gain-scheduling breakpoint data.

#### Dependencies

To enable this parameter, select **Use for gain
scheduling**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBreakpoints` |
| **Type:** vector |
| **Values:** vector of at least two elements |
| **Default:** `"[1 2 3]"` |

### **Number of breakpoints** — Number of breakpoints `3` (default) | positive scalar

Specify the number of breakpoints in the external breakpoints
signal.

#### Dependencies

To enable this parameter, select **Use for gain
scheduling** and **Use external
signal**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBreakpoints` |
| **Type:** scalar |
| **Values:** positive scalar |
| **Default:** `3` |

### **Use external signal** — Specify breakpoints from input port `off` (default) | `on`

Specify breakpoints from the block input port.

#### Dependencies

To enable this parameter, select **Use for gain
scheduling**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseExternalBreakpoints` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Gain index tolerance** — Gain index tolerance `1e-3` (default) | nonegative scalar

Specify the tolerance between the scheduling variable and the breakpoints.
To determine which breakpoint to update in the array, the block compares the
scheduling variable with the breakpoint array and uses this tolerance value
to determine the closest value.

#### Dependencies

To enable this parameter, select **Use for gain
scheduling**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GainIndexTolerance` |
| **Type:** scalar |
| **Values:** nonnegative scalar |
| **Default:** `1e-3` |

### **Method of storing gains** — Method of storing gains `Data store memory` (default) | `Goto/from` | `Output from block`

Specify the method of storing gains.

- `Data store memory` — Use Data
  Store Memory blocks to store the gains. To create the
  data store blocks, first specify a name for the data store using
  **Parameter Name** parameter for each gain,
  then click the **Add Data Store Memory blocks to
  model** button. The PID Gains Store and
  Update block creates Data Store Memory
  blocks in the top-level of the model. You can specify these data
  store names directly in the PID Gain Scheduler block
  to perform lookup table based gain scheduling.
- `Goto/from` — Use Goto and
  From blocks to route the gains. To specify a
  Goto tag, use the **Parameter
  Name** parameter for each gain. You can specify these
  Goto tags directly in the PID Gain
  Scheduler block to read and lookup the gains.
- `Output from block` — Use the
  **PID Gains Out** output port. You can feed
  this output signal directly into the PID Gain
  Scheduler block.

Use the **Gain initial conditions** parameters to specify
the initial values of gains. The block uses the initial values when the
tuned gained are not available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerUpdateMethod` |
| **Type:** string |
| **Values:** `"Data store memory"` | `"Goto/from"` | `"Output from block"` |
| **Default:** `"Data store memory"` |

### **P Gain Parameter Name** — Proportional gain data name `PGain` (default) | string

Specify the name of the data store or goto tag for the proportional gain
data.

#### Dependencies

To enable this parameter, set

- **Controller type** to a controller type that
  has proportional action.
- **Method of obtaining gains** to
  `Data store memory` or
  `Goto/from`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StoreGainsPParamName` |
| **Type:** string |
| **Default:** `"PGain"` |

### **P Gain initial conditions** — Proportional gain initial value `0` (default) | scalar | vector

Specify the initial value of the proportional gain as a scalar or vector.
The block uses this value when tuned gains data from the external sources
(like Closed-Loop PID Autotuner) is not available.

- Scalar — The block uses this value for all breakpoints.
- Vector — Specify a vector of same length as
  **Breakpoints**. The block uses the initial
  value at the index corresponding to the current breakpoint.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has proportional action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PGainInitialConditions` |
| **Type:** scalar | vector |
| **Default:** 0 |

### **I Gain Parameter Name** — Integral gain data name `IGain` (default) | string

Specify the name of the data store or goto tag for the integral gain
data.

#### Dependencies

To enable this parameter, set

- **Controller type** to a controller type that
  has integral action.
- **Method of obtaining gains** to
  `Data store memory` or
  `Goto/from`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StoreGainsIParamName` |
| **Type:** string |
| **Default:** `"IGain"` |

### **I Gain initial conditions** — Integral gain initial value `0` (default) | scalar | vector

Specify the initial value of the integral gain as a scalar or vector. The
block uses this value when tuned gains data from the external sources (like
Closed-Loop PID Autotuner) is not available.

- Scalar — The block uses this value for all breakpoints.
- Vector — Specify a vector of same length as
  **Breakpoints**. The block uses the initial
  value at the index corresponding to the current breakpoint.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IGainInitialConditions` |
| **Type:** scalar | vector |
| **Default:** 0 |

### **D Gain Parameter Name** — Derivative gain data name `DGain` (default) | string

Specify the name of the data store or goto tag for the derivative gain
data.

#### Dependencies

To enable this parameter, set

- **Controller type** to a controller type that
  has derivative action.
- **Method of obtaining gains** to
  `Data store memory` or
  `Goto/from`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StoreGainsDParamName` |
| **Type:** string |
| **Default:** `"DGain"` |

### **D Gain initial conditions** — Derivative gain initial value `0` (default) | scalar | vector

Specify the initial value of the derivative gain as a scalar or vector.
The block uses this value when tuned gains data from the external sources
(like Closed-Loop PID Autotuner) is not available.

- Scalar — The block uses this value for all breakpoints.
- Vector — Specify a vector of same length as
  **Breakpoints**. The block uses the initial
  value at the index corresponding to the current breakpoint.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has derivative action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DGainInitialConditions` |
| **Type:** scalar | vector |
| **Default:** 0 |

### **N Gain Parameter Name** — Filter gain data name `NGain` (default) | string

Specify the name of the data store or goto tag for the derivative filter
gain data.

#### Dependencies

To enable this parameter, set

- **Controller type** to a controller type that
  has a filtered derivative.
- **Method of obtaining gains** to
  `Data store memory` or
  `Goto/from`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StoreGainsNParamName` |
| **Type:** string |
| **Default:** `"NGain"` |

### **N Gain initial conditions** — Filter gain initial value `100` (default) | scalar | vector

Specify the initial value of the derivative filter gain as a scalar or
vector. The block uses this value when tuned gains data from the external
sources (like Closed-Loop PID Autotuner) is not
available.

- Scalar — The block uses this value for all breakpoints.
- Vector — Specify a vector of same length as
  **Breakpoints**. The block uses the initial
  value at the index corresponding to the current breakpoint.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has a filtered derivative.

#### Dependencies

To enable this parameter, set **Method of storing
gains** to `Data store memory` or
`Goto/from`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NGainInitialConditions` |
| **Type:** scalar | vector |
| **Default:** 100 |

### **Method to trigger gain update** — Update trigger method **Detect change in PID gains** (default) | **External trigger**

Specify the method to trigger gain update.

- **Detect change in PID gains** — Update the gains
  automatically when there is a change in the input gains.
- **External trigger** — Use an external signal to
  trigger the gains update.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerUpdateMethod` |
| **Type:** string |
| **Values:** `"Detect change in PID gains"` | `"External trigger"` |
| **Default:** `"Detect change in PID gains"` |

### **Number of samples to delay update** — Number of samples to delay update `1` (default) | nonnegative scalar

Number of samples to delay the gains update following the trigger event. Use this option
to delay updating the gains in order to give the autotuning algorithm enough
time to calculate the gains.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumUpdateDelays` |
| **Type:** scalar |
| **Values:** nonnegative scalar |
| **Default:** `1` |

### **Sample time (-1 for inherited)** — Sample time `-1` (default) | positive scalar

Specify the sample time. In your autotuning applications, this sample time
must match with the controller sample time specified in the PID
Controller and Closed-Loop PID Autotuner
blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** scalar |
| **Values:** positive scalar | –1 |
| **Default:** `–1` |

### **Data Type** — Floating point precision `Double` (default) | `Single`

Specify the floating-point precision based on simulation environment or
hardware requirements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BlockDataType` |
| **Type:** string |
| **Values:** `"Double"` | `"Single"` |
| **Default:** `"Double"` |

## Libraries

Simulink Control Design / Autotuning

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Store and update tuned PID gains tuned using Closed-Loop PID Autotuner

The PID Gains Store and Update block lets you write the gains obtained from
the Closed-Loop PID
Autotuner block to a memory location or route them as a signal. Use this
block to manage the gains obtained at various operating points during the autotuning
process.

Typically, tuning a gain-scheduled controller is a complex process. It requires you to run
multiple simulations for tuning at each operating point and provide a logic to store PID
gains at that operating point. Using this block, along with the Change Operating
Points and PID Gain
Scheduler blocks, helps you implement a streamlined workflow for autotuning
gain-scheduled PID controllers over an operating range in a single run. To do so, use
this workflow.

1. Switch between predefined or snapshot operating point data during the
   simulation using the Change Operating Points block.
2. Perform autotuning at the operating points using Closed-Loop PID
   Autotuner.
3. Store the PID gains corresponding to the operating point in an array using
   PID Gains Store and Update block.
4. Perform lookup table based gain scheduling from the array using the PID
   Gain Scheduler block.

On a high level, you can use these blocks to implement the gain-scheduled workflow as
shown in this diagram.

Diagram of a gain-scheduled system, with Closed-Loop PID Autotuner, PID Controller, Change Operating Points, Gain Scheduler, and PID Gains Store and Update blocks.
