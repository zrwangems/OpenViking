---
type: simulink-block
title: 'PID Gain Scheduler'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'pidgainscheduler'
documentation_source_path: 'ug/pidgainscheduler.html'
language: en
---

# PID Gain Scheduler

## Ports
```yaml
ports:
- name: scheduling Variable
  summary: Scheduling variable scalar
  direction: input
- name: Breakpoints
  summary: Breakpoint data vector
  direction: input
- name: PID Gains
  summary: PID gain array bus
  direction: input
- name: P
  summary: Proportional gain vector
  direction: output
- name: I
  summary: Integral gain vector
  direction: output
- name: D
  summary: Derivative gain vector
  direction: output
- name: N
  summary: Derivative filter gain vector
  direction: output
```

### Input

### **scheduling Variable** — Scheduling variable scalar

Specify the scheduling variable. This signal indicates where in the operating range the
system is at a given time. The lookup tables use this signal to
determine the value of the PID gains.

### **Breakpoints** — Breakpoint data vector

Breakpoint data for gain scheduling, specified as a vector.

#### Dependencies

To enable this port, select **Use external
signal**.

### **PID Gains** — PID gain array bus

Stored PID gain array. Use this gain array along with the breakpoint
data to implement lookup table based gain scheduling.

This 4-element bus signal must contain the tuned PID gains
*P*, *I*, *D*,
and the filter coefficient *N*. These values correspond
to the `P`, `I`, `D`,
and `N` parameters in the expressions given in the
**Controller type** parameter. This bus signal
always has four elements, even if you are not tuning a PIDN
controller.

Typically, you obtain such an array using the PID Gains Store and Update block.

#### Dependencies

To enable this port, set **Method of obtaining
gains** to `Input to
block`
### Output

### **P** — Proportional gain vector

The block computes the gains using the breakpoint vector and PID gain
input array. The lookup method can use interpolation, extrapolation, or
the original values of the input gains.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has proportional action.

### **I** — Integral gain vector

The block computes the gains using the breakpoint vector and PID gain
input array. The lookup method can use interpolation, extrapolation, or
the original values of the input gains.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has integral action.

### **D** — Derivative gain vector

The block computes the gains using the breakpoint vector and PID gain
input array. The lookup method can use interpolation, extrapolation, or
the original values of the input gains.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has derivative action.

### **N** — Derivative filter gain vector

The block computes the gains using the breakpoint vector and PID gain
input array. The lookup method can use interpolation, extrapolation, or
the original values of the input gains.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has a filtered derivative.
## Parameters
```yaml
parameters:
- name: Controller type
  summary: PID controller type P (default) | I | PI | PD | PDN | PID | PIDN
  group: ''
  block_parameter: ControllerType
  type: string
  values: '"P" | "I" | "PI" | "PD" | "PDN" | "PID" | "PIDN"'
  default: '"PID"'
- name: Breakpoints saved in gain array
  summary: Read breakpoints saved in gain array off (default) | on
  group: ''
  block_parameter: BPsInGainArray
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Breakpoints
  summary: Gain scheduling breakpoints [1 2 3] (default) | vector
  group: ''
  block_parameter: GainArrayBreakpoints
  type: string
  values: vector of at least two elements
  default: '"[1 2 3]"'
- name: Use external signal
  summary: Specify breakpoints from input port off (default) | on
  group: ''
  block_parameter: UseExternalBreakpoints
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Method of obtaining gains
  summary: Method of obtaining gains Data store memory (default) | Goto/from | Input to block
  group: ''
  block_parameter: GainSourceMethod
  type: string
  values: '"Data store memory" | "Goto/from" | "Input to block"'
  default: '"Data store memory"'
- name: P Gain Parameter Name
  summary: Proportional gain data name PGain (default) | string
  group: ''
  block_parameter: StoreGainsPParamName
  type: string
  default: '"PGain"'
- name: I Gain Parameter Name
  summary: Integral gain data name IGain (default) | string
  group: ''
  block_parameter: StoreGainsIParamName
  type: string
  default: '"IGain"'
- name: D Gain Parameter Name
  summary: Derivative gain data name DGain (default) | string
  group: ''
  block_parameter: StoreGainsDParamName
  type: string
  default: '"DGain"'
- name: N Gain Parameter Name
  summary: Filter gain data name NGain (default) | string
  group: ''
  block_parameter: StoreGainsNParamName
  type: string
  default: '"NGain"'
- name: Data type
  summary: Floating point precision Double (default) | Single
  group: ''
  block_parameter: BlockDataType
  type: string
  values: '"Double" | "Single"'
  default: '"Double"'
- name: P gain lookup method
  summary: Proportional gain lookup method Interpolation-Use End Values (default) | Interpolation-Extrapolation | Use Input
    Nearest | Use Input Below | Use Input Above
  group: ''
  block_parameter: PGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: I gain lookup method
  summary: Integral gain lookup method Interpolation-Use End Values (default) | Interpolation-Extrapolation | Use Input Nearest
    | Use Input Below | Use Input Above
  group: ''
  block_parameter: IGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: D gain lookup method
  summary: Derivative gain lookup method Interpolation-Use End Values (default) | Interpolation-Extrapolation | Use Input
    Nearest | Use Input Below | Use Input Above
  group: ''
  block_parameter: DGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: N gain lookup method
  summary: Derivative filter gain lookup method Interpolation-Use End Values (default) | Interpolation-Extrapolation | Use
    Input Nearest | Use Input Below | Use Input Above
  group: ''
  block_parameter: NGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: Saturate to max or min when overflows occur
  summary: Method of overflow action off (default) | on
  group: ''
  block_parameter: DoSatur
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding Output data type off (default) | on
  group: ''
  block_parameter: LockScale
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: ''
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
```

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

### **Breakpoints saved in gain array** — Read breakpoints saved in gain array `off` (default) | `on`

Enable this option when the gain array also contains the breakpoint data. Typically, you
obtain such an array when you store PID gains using the PID Gain
Store and Update block with **Save breakpoints in gain
array** enabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BPsInGainArray` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Breakpoints** — Gain scheduling breakpoints `[1 2 3]` (default) | vector

Specify the gain-scheduling breakpoint data.

#### Dependencies

To enable this parameter, disable **Breakpoints saved in gain
array**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GainArrayBreakpoints` |
| **Type:** string |
| **Values:** vector of at least two elements |
| **Default:** `"[1 2 3]"` |

### **Use external signal** — Specify breakpoints from input port `off` (default) | `on`

Specify breakpoints from the block input port.

#### Dependencies

To enable this parameter, disable **Breakpoints saved in gain
array**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseExternalBreakpoints` |
| **Type:** string |
| **Value** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Method of obtaining gains** — Method of obtaining gains `Data store memory` (default) | `Goto/from` | `Input to block`

Specify the method of obtaining gains.

- `Data store memory` — Use Data
  Store Memory blocks to read the gains. To do so, use the
  same name as the data store name in the Data Store
  Memory blocks created using the PID Gains Store
  and Update block.
- `Goto/from` — Use a From
  block tag to read the gains. To specify the tag name, use the
  **Parameter Name** parameter for each gain. You
  can specify these Goto tags created using the
  PID Gain Scheduler block to read and lookup the
  gains.
- `Input to block` — Use the **PID
  Gains** input port. You can feed the output signal of
  the PID Gain Scheduler block to this input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GainSourceMethod` |
| **Type:** string |
| **Values:** `"Data store memory"` | `"Goto/from"` | `"Input to block"` |
| **Default:** `"Data store memory"` |

### **P Gain Parameter Name** — Proportional gain data name `PGain` (default) | string

Specify the name of the data store or goto tag from which this block reads
the proportional gain parameter data.

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

### **I Gain Parameter Name** — Integral gain data name `IGain` (default) | string

Specify the name of the data store or goto tag from which this block reads
the integral gain parameter data.

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

### **D Gain Parameter Name** — Derivative gain data name `DGain` (default) | string

Specify the name of the data store or goto tag from which this block reads
the derivative gain parameter data.

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

### **N Gain Parameter Name** — Filter gain data name `NGain` (default) | string

Specify the name of the data store or goto tag from which this block reads
the filter gain parameter data.

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

### **Data type** — Floating point precision `Double` (default) | `Single`

Specify the floating-point precision based on simulation environment or
hardware requirements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BlockDataType` |
| **Type:** string |
| **Values:** `"Double"` | `"Single"` |
| **Default:** `"Double"` |

### **P gain lookup method** — Proportional gain lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the lookup method you select to the input vectors
of breakpoint data (**Breakpoints**) and table data
(**PID Gains**). For details, see How the Block Generates Output.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has proportional action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PGainLookUpMeth` |
| **Type:** string |
| **Values:** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **Default:** `"Use Input Above"` |

### **I gain lookup method** — Integral gain lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the lookup method you select to the
input vectors of breakpoint data (**Breakpoints**) and
table data (**PID Gains**). For details, see How the Block Generates Output.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IGainLookUpMeth` |
| **Type:** string |
| **Values:** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **Default:** `"Use Input Above"` |

### **D gain lookup method** — Derivative gain lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the lookup method you select to the
input vectors of breakpoint data (**Breakpoints**) and
table data (**PID Gains**). For details, see How the Block Generates Output.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has derivative action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DGainLookUpMeth` |
| **Type:** string |
| **Values:** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **Default:** `"Use Input Above"` |

### **N gain lookup method** — Derivative filter gain lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the lookup method you select to the
input vectors of breakpoint data (**Breakpoints**) and
table data (**PID Gains**). For details, see How the Block Generates Output.

#### Dependencies

To enable this port, set **Controller type** to a
controller type that has a filtered derivative.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NGainLookUpMeth` |
| **Type:** string |
| **Values:** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **Default:** `"Use Input Above"` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or
minimum value that the data type can represent. Otherwise, overflows
wrap.

When you select this check box, saturation applies to every internal
operation on the block, not just the output or result. In general, the code
generation process can detect when overflow is not possible. In this case,
the code generator does not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** string |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** string |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more
information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB® rounding function into the mask field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `"Ceiling"` | `"Convergent"` | `"Floor"` | `"Nearest"` | `"Round"` | `"Simplest"` | `"Zero"` |
| **Default:** `"Floor"` |
## Libraries

Simulink Control Design / Autotuning

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Lookup table based gain scheduling with PID array

The PID Gain Scheduler block lets you lookup PID gains for the current state
of the system from an array of gains, the corresponding breakpoint data, and the
scheduling variable. The block uses lookup tables to associate specific PID gains with
corresponding breakpoint values and provides dynamically adjusted PID gains based on the
current operating point (scheduling variable). You can use these gains as inputs to the
PID controller or other relevant blocks within the model. The lookup method can use
interpolation, extrapolation, or the original values of the input gains.

Typically, tuning a gain-scheduled controller is a complex process. It requires you to
run multiple simulations for tuning at each operating point and provide a logic to store
PID gains at that operating point. Using this block, along with the Change Operating
Points and PID Gains Store
and Update blocks, helps you implement a streamlined workflow for autotuning
gain-scheduled PID controllers over an operating range in a single simulation. To do so,
use this workflow.

1. Switch between predefined or snapshot operating point data during the
   simulation using the Change Operating Points block.
2. Perform autotuning at the operating points using Closed-Loop PID Autotuner.
3. Store the PID gains corresponding to the operating point in an array using
   PID Gains Store and Update block.
4. Perform lookup table based gain scheduling from the array using the PID
   Gain Scheduler block.

On a high level, you can use these blocks to implement the gain-scheduled workflow as
shown in this diagram.

Diagram of a gain-scheduled system, with Closed-Loop PID Autotuner, PID Controller, Change Operating Points, Gain Scheduler, and PID Gains Store and Update blocks.
