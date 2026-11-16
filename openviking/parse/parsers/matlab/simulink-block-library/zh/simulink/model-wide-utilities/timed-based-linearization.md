---
type: simulink-block
title: 'Timed-Based Linearization'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Model-Wide Utilities'
documentation_page: 'timedbasedlinearization'
documentation_source_path: 'slref/timedbasedlinearization.html'
language: zh-CN
chinese_source: worker-translation
---

# Timed-Based Linearization

## 端口

R2025b 中未记录。

## 参数

### **线性化时间** — 生成线性模型的时间 `1`（默认）| scalar | vector

希望模块生成线性模型的时间。如果希望模块在多个时间步生成线性模型，请输入时间向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizationTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'1'` |

### **采样时间（线性化模型的）** — 采样时间 `0`（默认）| scalar | vector

为线性模型指定采样时间。要使用 `linmod` 创建连续时间模型，请指定采样时间 `0`。否则，要使用 `dlinmod` 创建离散时间模型，请指定正采样时间。

#### 程序化使用

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
| **数据类型** |  |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010a 中引入**

## 描述

在特定时间于基础工作区中生成线性模型

当仿真时钟达到 **线性化时间** 参数指定的时间时，此模块会调用 `linmod` 或 `dlinmod` 为系统创建线性模型。不执行配平。线性模型连同拍摄快照时的工作点信息一起作为结构体存储在基础工作区中。多个快照会追加形成结构体数组。

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
| `Ts` | 离散线性化的采样时间 |

**提示**

要有条件地生成模型，请使用 Trigger-Based Linearization 模块。
