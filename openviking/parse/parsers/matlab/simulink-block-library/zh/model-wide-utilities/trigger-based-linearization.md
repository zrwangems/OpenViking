---
type: simulink-block
title: 'Trigger-Based Linearization'
family: model-wide-utilities
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'triggerbasedlinearization'
language: zh-CN
chinese_source: worker-translation
---

# Trigger-Based Linearization

## 端口

### 输入

### **Port\_1** — 输入信号标量

输入触发信号，指定为标量。使用 **触发类型** 参数指定触发线性模型生成的事件类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **触发类型** — 触发线性模型生成的信号类型 `rising` | `falling` | `either` | `function-call`

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

### **采样时间（线性化模型的）** — 采样时间 `0`（默认） | scalar | vector

为线性模型指定采样时间。要使用 `linmod` 创建连续时间模型，请将采样时间指定为 `0`。否则，要使用 `dlinmod` 创建离散时间模型，请指定正采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0'` |

## 所属库

Simulink / Model-Wide Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

触发时在基础工作区中生成线性模型

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
