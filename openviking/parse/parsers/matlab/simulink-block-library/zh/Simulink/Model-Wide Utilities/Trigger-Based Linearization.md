---
type: simulink-block
title: 'Trigger-Based Linearization'
family: 'model-wide-utilities'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'triggerbasedlinearization'
documentation_source_path: 'slref/triggerbasedlinearization.html'
language: zh-CN
chinese_source: worker-translation
---

# Trigger-Based Linearization

## 端口

### 输入

### **Port\_1** — 输入信号标量

输入触发信号，指定为标量。使用**触发类型**参数指定触发线性模型生成的事件类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **触发类型** — 触发线性模型生成的信号类型 `rising` | `falling` | `either` | `function-call`

触发输入信号上触发线性模型生成的事件类型。可以选择：

- `rising` — 当触发信号从负值或零值上升为正值时，触发子系统或模型的执行。如果初始值为负，则上升至零的信号会触发执行。
- `falling` — 当触发信号从正值或零值下降为负值时，触发子系统或模型的执行。如果初始值为正，则下降至零的信号会触发执行。
- `either` — 当触发信号上升或下降时，触发子系统或模型的执行。
- `function-call` — 当触发信号是来自 Stateflow® 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块的函数调用事件时，触发子系统或模型的执行。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TriggerType` |
| **类型：** 字符向量 |
| **值：** `'rising'` | `'falling'` | `'either'` | `'function-call'` |
| **默认值：** `'rising'` |

### **采样时间（线性化模型）** — 采样时间 `0`（默认） | 标量 | 向量

为线性模型指定采样时间。要使用 `linmod` 创建连续时间模型，请指定采样时间 `0`。否则，要使用 `dlinmod` 创建离散时间模型，请指定正采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
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

**早于 R2006a 引入**

## 描述

触发时在基础工作区中生成线性模型

触发时，此模块调用 `linmod` 或 `dlinmod` 为系统在当前工作点创建线性模型。不执行修剪。线性模型作为结构体存储在基础工作区中，并带有拍摄快照时工作点的信息。多个快照会追加形成结构体数组。

**注意**

`linmod` 和 `dlinmod` 仅提供基本的线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅选择线性化工具 (Simulink Control Design)。

该模块将以下模型参数设置为指示的值：

- `BufferReuse = 'off'`
- `BlockReductionOpt = 'off'`

用于保存快照的结构体名称是模型名称后附加 `_Trigger_Based_Linearization`，例如 `vdp_Trigger_Based_Linearization`。该结构体具有以下字段：

| 字段 | 描述 |
| --- | --- |
| `a` | 线性化的 A 矩阵 |
| `b` | 线性化的 B 矩阵 |
| `c` | 线性化的 C 矩阵 |
| `d` | 线性化的 D 矩阵 |
| `StateName` | 模型状态的名称 |
| `OutputName` | 模型输出端口的名称 |
| `InputName` | 模型输入端口的名称 |
| `OperPoin`t | 指定线性化工作点的结构体。该结构体指定工作点时间（`OperPoint.t`）下模型状态（`OperPoint.x`）和输入（`OperPoint.u`）的值。 |
| `Ts` | 离散线性化的采样时间 |

**提示**

使用 Timed-Based Linearization 模块在预定时间生成线性模型。
