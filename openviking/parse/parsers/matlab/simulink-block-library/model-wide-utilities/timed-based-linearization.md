---
type: simulink-block
title: 'Timed-Based Linearization'
family: model-wide-utilities
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'timedbasedlinearization'
---

# Timed-Based Linearization

Generate linear models in base workspace at specific times

## 中文

在指定时间于基础工作区中生成线性模型

### 库

Simulink / Model-Wide Utilities

### 描述

当仿真时钟达到 **线性化时间** 参数指定的时间时，此模块会调用 `linmod` 或 `dlinmod` 为系统创建线性模型。不执行配平。该线性模型与获取快照时的工作点信息一起以结构体形式存储在基础工作区中。多个快照会追加在一起，形成一个结构体数组。

**注意**

`linmod` 和 `dlinmod` 仅提供基本线性化功能。要获得完整线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅选择线性化工具 (Simulink Control Design)。

此模块将以下模型参数设置为指示的值：

- `BufferReuse = 'off'`
- `BlockReductionOpt = 'off'`

用于保存快照的结构体名称是模型名称后附加 `_Timed_Based_Linearization`，例如 `vdp_Timed_Based_Linearization`。该结构体具有以下字段：

| 字段 | 描述 |
| --- | --- |
| `a` | 线性化的 A 矩阵 |
| `b` | 线性化的 B 矩阵 |
| `c` | 线性化的 C 矩阵 |
| `d` | 线性化的 D 矩阵 |
| `StateName` | 模型的状态名称 |
| `OutputName` | 模型的输出端口名称 |
| `InputName` | 模型的输入端口名称 |
| `OperPoint` | 指定线性化工作点的结构体。该结构体指定工作点时间（`OperPoint.t`）。不使用状态（`OperPoint.x`）和输入（`OperPoint.u`）字段。 |
| `Ts` | 用于离散线性化的线性化采样时间 |

**提示**

要有条件地生成模型，请使用 Trigger-Based Linearization 模块。

### 参数

#### **线性化时间** — 生成线性模型的时间 `1` (默认) | scalar | vector

希望此模块生成线性模型的时间。如果希望此模块在多个时间步生成线性模型，请输入时间向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizationTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'1'` |

#### **采样时间（线性化模型的）** — 采样时间 `0` (默认) | scalar | vector

为线性模型指定采样时间。要使用 `linmod` 创建连续时间模型，请指定采样时间为 `0`。否则，要使用 `dlinmod` 创建离散时间模型，请指定正采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 版本历史

**在 R2010a 中引入**

## Libraries

Simulink / Model-Wide Utilities

## Description

This block calls `linmod` or `dlinmod` to create a linear model for the system when the simulation
clock reaches the time specified by the **Linearization
time** parameter. No trimming is performed. The linear model is stored in
the base workspace as a structure, along with information about the operating point at
which the snapshot was taken. Multiple snapshots are appended to form an array of
structures.

**Note**

`linmod` and `dlinmod` provide only basic
linearization functionality. For full linearization functionality, use Simulink®
Control Design™ software. For more information, see Choose Linearization Tools (Simulink Control Design).

The block sets the following model parameters to the indicated values:

- `BufferReuse = 'off'`
- `BlockReductionOpt = 'off'`

The name of the structure used to save the snapshots is the name of the model appended
by `_Timed_Based_Linearization`, for example,
`vdp_Timed_Based_Linearization`. The structure has the following
fields:

| Field | Description |
| --- | --- |
| `a` | The A matrix of the linearization |
| `b` | The B matrix of the linearization |
| `c` | The C matrix of the linearization |
| `d` | The D matrix of the linearization |
| `StateName` | Names of the model's states |
| `OutputName` | Names of the model's output ports |
| `InputName` | Names of the model's input ports |
| `OperPoint` | A structure that specifies the operating point of the linearization. The structure specifies the operating point time (`OperPoint.t`). The states (`OperPoint.x`) and inputs (`OperPoint.u`) fields are not used. |
| `Ts` | The sample time of the linearization for a discrete linearization |

**Tip**

To generate models conditionally, use the Trigger-Based Linearization
block.

## Parameters

### **Linearization time** — Time at which to generate a linear model `1` (default) | scalar | vector

Time at which you want the block to generate a linear model. Enter a
vector of times if you want the block to generate linear models at more than
one time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizationTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

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
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Version History

**Introduced in R2010a**
