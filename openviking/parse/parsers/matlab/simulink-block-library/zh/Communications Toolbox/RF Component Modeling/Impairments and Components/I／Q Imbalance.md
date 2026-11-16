---
type: simulink-block
title: 'I/Q Imbalance'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'iqimbalance'
documentation_source_path: 'ref/iqimbalance.html'
language: zh-CN
chinese_source: worker-translation
---

# I/Q Imbalance

## 端口

### 输入

### **In1** — 复信号 标量 | 向量

复信号，指定为标量或向量。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out1** — 输出信号 标量 | 向量

输出信号，返回为标量或向量。此输出与输入信号具有相同的维度和数据类型。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **I/Q amplitude imbalance (dB)** — I/Q 幅度不平衡 `0`（默认）| 标量

以信号功率的 decibels 为单位的 I/Q 幅度不平衡，指定为标量。有关详细信息，请参阅算法。

### **I/Q phase imbalance (deg)** — I/Q 相位不平衡 `0`（默认）| 标量

I/Q 幅度不平衡，以 degrees 为单位，指定为标量。

### **I dc offset** — 同相分量 DC 偏移 `0`（默认）| 标量

同相分量 DC 偏移，指定为标量。

### **Q dc offset** — 正交分量 DC 偏移 `0`（默认）| 标量

正交分量 DC 偏移，指定为标量。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对复信号应用 I/Q 不平衡

I/Q Imbalance 模块对复信号应用同相和正交不平衡。此模块对同相和正交信号分量应用幅度不平衡、相位不平衡和 DC 偏移。有关详细信息，请参阅 I/Q Imbalance 实现和算法。
