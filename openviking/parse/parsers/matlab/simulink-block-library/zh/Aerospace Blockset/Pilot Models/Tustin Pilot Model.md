---
type: simulink-block
title: 'Tustin Pilot Model'
family: 'pilot-models'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'tustinpilotmodel'
documentation_source_path: 'tustinpilotmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Tustin Pilot Model

## 端口

### 输入

### **x com** — 信号指令标量

驾驶员模型控制的信号指令，指定为标量。

**数据类型：** `double`

### **x** — 由驾驶员控制的信号标量

由驾驶员控制的信号，指定为标量。

**数据类型：** `double`
### 输出

### **u** — 飞机指令标量

飞机指令，以标量形式返回。

**数据类型：** `double`

## 参数

### **驾驶员增益** — 驾驶员增益 `1`（默认） | 标量

驾驶员增益，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Kp` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1'` |

### **驾驶员时间延迟(s)** — 驾驶员时间延迟 `0.1`（默认） | 标量

总驾驶员时间延迟，指定为 double 标量，以 seconds 为单位。该值通常在 0.1 s 到 0.2 s 范围内。

#### 程序化使用

|  |
| --- |
| **模块参数**: `time_delay` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.1'` |

### **驾驶员超前常数** — 驾驶员超前常数 `5`（默认） | 标量

驾驶员超前常数，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `T` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'5'` |

## 所属库

Aerospace Blockset / Pilot Models

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

表示 Tustin 驾驶员模型

Tustin Pilot Model 模块表示 A. Tustin 在 *The Nature of the Operator’s Response in Manual Control, and its Implications for Controller Design* [1] 中描述的驾驶员模型。在建模人类驾驶员模型时，与 Crossover Pilot Model 和 Precision Pilot Model 模块提供的精度相比，使用此模块可获得最低精度。此模块比那些模块需要更少的输入，并提供更好的性能。但是，结果可能不太准确。

此驾驶员模型是一个单输入、单输出 (SISO) 模型，表示人类行为，并基于算法中描述的传递函数。

此模块具有非线性行为。如果要线性化此模块（例如，使用 `linearize` (Simulink Control Design) 函数或某个 `linmod` 函数），可能需要更改 Pade 逼近阶数。Tustin Pilot Model 模块实现包含 Transport Delay 模块，其 **Pade order (for linearization)** 参数默认设置为 `2`。要更改此值，请使用 `set_param` 函数，例如：

```
set_param(gcb,'pade','3')
```

**注意**

`linmod` 函数仅提供基本的线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅选择线性化工具 (Simulink Control Design)。
