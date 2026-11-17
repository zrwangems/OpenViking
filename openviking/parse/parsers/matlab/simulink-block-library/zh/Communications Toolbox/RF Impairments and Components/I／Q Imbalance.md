---
type: simulink-block
title: 'I/Q Imbalance'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
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
**复数支持：** 是
### 输出

### **Out1** — 输出信号 标量 | 向量

输出信号，以标量或向量形式返回。该输出的维度和数据类型与输入信号相同。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **I/Q amplitude imbalance (dB)** — I/Q 幅度不平衡 `0`（默认）| 标量

信号功率的 I/Q 幅度不平衡，以分贝为单位，指定为标量。有关详细信息，请参阅算法。

### **I/Q phase imbalance (deg)** — I/Q 相位不平衡 `0`（默认）| 标量

I/Q 幅度不平衡，以度为单位，指定为标量。

### **I dc offset** — 同相分量直流偏移 `0`（默认）| 标量

同相分量直流偏移，指定为标量。

### **Q dc offset** — 正交分量直流偏移 `0`（默认）| 标量

正交分量直流偏移，指定为标量。

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

I/Q Imbalance 模块对复信号应用同相和正交不平衡。该模块对同相和正交信号分量应用幅度不平衡、相位不平衡和直流偏移。有关详细信息，请参阅 I/Q Imbalance Implementation 和 Algorithms。
