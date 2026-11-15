---
type: simulink-block
title: 'Trigger-Based Linearization'
family: model-wide-utilities
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'triggerbasedlinearization'
---

# Trigger-Based Linearization

Generate linear models in base workspace when triggered

## 中文

触发时在基础工作区中生成线性模型

### 库

Simulink / Model-Wide Utilities

### 说明

当被触发时，此模块会调用 `linmod` 或 `dlinmod`，在当前工作点为系统创建线性模型。不执行配平。线性模型以结构体形式存储在基础工作区中，同时存储拍摄快照时所在工作点的信息。多个快照会追加，形成一个结构体数组。

**注意**

`linmod` 和 `dlinmod` 仅提供基本的线性化功能。要使用完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅 Choose Linearization Tools (Simulink Control Design)。

该模块将以下模型参数设置为指定值：

- `BufferReuse = 'off'`
- `BlockReductionOpt = 'off'`

用于保存快照的结构体名称是模型名称追加 `_Trigger_Based_Linearization`，例如 `vdp_Trigger_Based_Linearization`。该结构体包含以下字段：

| 字段 | 说明 |
| --- | --- |
| `a` | 线性化的 A 矩阵 |
| `b` | 线性化的 B 矩阵 |
| `c` | 线性化的 C 矩阵 |
| `d` | 线性化的 D 矩阵 |
| `StateName` | 模型状态名称 |
| `OutputName` | 模型输出端口名称 |
| `InputName` | 模型输入端口名称 |
| `OperPoint` | 指定线性化工作点的结构体。该结构体指定工作点时间 (`OperPoint.t`) 处模型状态 (`OperPoint.x`) 和输入 (`OperPoint.u`) 的值。 |
| `Ts` | 离散线性化的采样时间 |

**提示**

使用 Timed-Based Linearization 模块在预定时间生成线性模型。

### 端口

#### 输入

#### **Port\_1** — 输入信号标量

输入触发信号，指定为标量。使用 **触发类型** 参数指定触发线性模型生成的事件类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **触发类型** — 触发线性模型生成的信号类型 `rising` | `falling` | `either` | `function-call`

触发输入信号上触发线性模型生成的事件类型。您可以选择：

- `rising` — 当触发信号从负值或零上升至正值时，触发子系统或模型执行。如果初始值为负值，则上升至零的信号会触发执行。
- `falling` — 当触发信号从正值或零下降至负值时，触发子系统或模型执行。如果初始值为正值，则下降至零的信号会触发执行。
- `either` — 当触发信号上升或下降时，触发子系统或模型执行。
- `function-call` — 当触发信号是来自 Stateflow® 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块的函数调用事件时，触发子系统或模型执行。

#### 编程用法

|  |
| --- |
| **模块参数：** `TriggerType` |
| **类型：** character vector |
| **值：** `'rising'` | `'falling'` | `'either'` | `'function-call'` |
| **默认值：** `'rising'` |

#### **采样时间（线性化模型的）** — 采样时间 `0`（默认） | scalar | vector

为线性模型指定采样时间。要使用 `linmod` 创建连续时间模型，请将采样时间指定为 `0`。否则，要使用 `dlinmod` 创建离散时间模型，请指定正采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

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
