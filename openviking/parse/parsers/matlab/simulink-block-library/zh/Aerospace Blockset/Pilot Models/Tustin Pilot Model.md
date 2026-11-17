---
type: simulink-block
title: 'Tustin Pilot Model'
family: 'aeroblks'
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
```yaml
ports:
- name: x com
  summary: 信号指令 标量
  direction: input
  data_types: double
- name: x
  summary: 由飞行员控制的信号 标量
  direction: input
  data_types: double
- name: u
  summary: 飞机指令 标量
  direction: output
  data_types: double
```

### 输入

### **x com** — 信号指令 标量

由飞行员模型控制的信号指令，指定为标量。

**数据类型：** `double`

### **x** — 由飞行员控制的信号 标量

由飞行员控制的信号，指定为标量。

**数据类型：** `double`
### 输出

### **u** — 飞机指令 标量

飞机指令，以标量形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Pilot gain
  summary: 飞行员增益 1（默认）| 标量
  group: ''
  block_parameter: Kp
  type: 字符向量
  values: 双精度标量
  default: '''1'''
- name: Pilot time delay(s)
  summary: 飞行员时间延迟 0.1（默认）| 标量
  group: ''
  block_parameter: time_delay
  type: 字符向量
  values: 双精度标量
  default: '''0.1'''
- name: Pilot lead constant
  summary: 飞行员超前常数 5（默认）| 标量
  group: ''
  block_parameter: T
  type: 字符向量
  values: 双精度标量
  default: '''5'''
```

### **Pilot gain** — 飞行员增益 `1`（默认）| 标量

飞行员增益，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Kp` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'1'` |

### **Pilot time delay(s)** — 飞行员时间延迟 `0.1`（默认）| 标量

飞行员总时间延迟，指定为双精度标量，单位为秒。该值通常在 0.1 秒到 0.2 秒之间。

#### 编程使用

|  |
| --- |
| **模块参数**：`time_delay` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.1'` |

### **Pilot lead constant** — 飞行员超前常数 `5`（默认）| 标量

飞行员超前常数，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`T` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'5'` |
## 所属库

Aerospace Blockset / Pilot Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

表示 Tustin 飞行员模型

Tustin Pilot Model 模块表示 A. Tustin 在 *The Nature of the Operator's Response in Manual Control, and its Implications for Controller Design* [1] 中描述的飞行员模型。在对人类飞行员模型进行建模时，与 Crossover Pilot Model 和 Precision Pilot Model 模块所提供的精度相比，使用此模块的精度最低。此模块所需的输入比那些模块少，并且提供更好的性能。但是，结果可能不太准确。

此飞行员模型是一个单输入单输出（SISO）模型，表示人类行为，并基于算法中描述的传递函数。

此模块具有非线性行为。如果您想要对该模块进行线性化（例如，使用 `linearize`（Simulink Control Design）函数或某个 `linmod` 函数），您可能需要更改 Pade 近似阶数。Tustin Pilot Model 模块实现默认将 Transport Delay 模块的 **Pade order (for linearization)** 参数设置为 `2`。要更改此值，请使用 `set_param` 函数，例如：

```
set_param(gcb,'pade','3')
```

**注意**

`linmod` 函数仅提供基本的线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅 Choose Linearization Tools (Simulink Control Design)。
