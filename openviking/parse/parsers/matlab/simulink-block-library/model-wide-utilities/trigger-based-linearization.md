---
type: simulink-block
title: 'Trigger-Based Linearization'
family: model-wide-utilities
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'triggerbasedlinearization'
---

# Trigger-Based Linearization

Generate linear models in base workspace when triggered

## Libraries

Simulink / Model-Wide Utilities

## Description

When triggered, this block calls `linmod` or `dlinmod` to create a linear model for the system at the current operating point. No trimming is performed. The linear model is stored in the base workspace as a structure, along with information about the operating point at which the snapshot was taken. Multiple snapshots are appended to form an array of structures.

**Note**

`linmod` and `dlinmod` provide only basic
linearization functionality. For full linearization functionality, use Simulink®
Control Design™ software. For more information, see Choose Linearization Tools (Simulink Control Design).

The block sets the following model parameters to the indicated values:

- `BufferReuse = 'off'`
- `BlockReductionOpt = 'off'`

The name of the structure used to save the snapshots is the
name of the model appended by `_Trigger_Based_Linearization`,
for example, `vdp_Trigger_Based_Linearization`. The structure has the following fields:

| Field | Description |
| --- | --- |
| `a` | The A matrix of the linearization |
| `b` | The B matrix of the linearization |
| `c` | The C matrix of the linearization |
| `d` | The D matrix of the linearization |
| `StateName` | Names of the model's states |
| `OutputName` | Names of the model's output ports |
| `InputName` | Names of the model's input ports |
| `OperPoin`t | A structure that specifies the operating point of the linearization. The structure specifies the value of the model's states (`OperPoint.x`) and inputs (`OperPoint.u`) at the operating point time (`OperPoint.t`). |
| `Ts` | The sample time of the linearization for a discrete linearization |

**Tip**

Use the Timed-Based Linearization block to
generate linear models at predetermined times.

## Ports

### Input

### **Port\_1** — Input signal scalar

Input trigger signal, specified as a scalar. Specify the type of event that triggers
generation of a linear model using the **Trigger type**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Trigger type** — Signal type that triggers generation of a linear model `rising` | `falling` | `either` | `function-call`

Type of event on the trigger input signal that triggers generation of a linear model. You
can select:

- `rising` — Trigger execution of subsystem
  or model when the trigger signal rises from a negative or zero value
  to a positive value. If the initial value is negative, a rising
  signal to zero triggers execution.
- `falling` — Trigger execution of
  subsystem or model when the trigger signal falls from a positive or
  a zero value to a negative value. If the initial value is positive,
  a falling signal to zero triggers execution.
- `either` — Trigger execution of subsystem
  or model when the trigger signal is either rising or falling.
- `function-call` — Trigger execution of
  subsystem or model when the trigger signal is a function-call event
  from a Stateflow® chart, Function-Call
  Generator block, S-Function block, or
  Hit Crossing
  block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerType` |
| **Type:** character vector |
| **Values:** `'rising'` | `'falling'` | `'either'` | `'function-call'` |
| **Default:** `'rising'` |

### **Sample time (of linearized model)** — Sample time `0` (default) | scalar | vector

Specify a sample time for the linear model. To create a continuous-time model using
`linmod`, specify a sample
time of `0`. Otherwise, to create a discrete-time model
using `dlinmod`, specify a
positive sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
