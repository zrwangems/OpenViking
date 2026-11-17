---
type: simulink-block
title: 'Free Space Path Loss'
family: 'rf-impairments-and-components'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'freespacepathloss'
documentation_source_path: 'ref/freespacepathloss.html'
language: zh-CN
chinese_source: worker-translation
---

# Free Space Path Loss

## 端口

### 输入

### **In1** — 复数信号标量 | 列向量

复数信号，指定为标量或列向量。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out1** — 输出信号标量 | 向量

输出信号，以标量或列向量形式返回。此输出与输入信号具有相同的维度和数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **Mode** — 损耗计算模式 `Decibels`（默认） | `Distance and Frequency`

损耗计算模式，指定为以下选项之一。

- `Decibels` — 使用 **Loss (dB)** 参数指定损耗。
- `Distance and Frequency` — 使用 **Distance (km)** 和 **Carrier frequency (MHz)** 参数计算损耗。

### **Loss (dB)** — 功率损耗 `10`（默认） | 标量

功率损耗，以 dB 为单位，指定为标量。模块图标上显示的 dB 数值仅为显示目的而进行了舍入。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Decibels`。

### **Distance (km)** — 发射机与接收机之间的距离 `0.100`（默认） | 标量

发射机与接收机之间的距离，以 km 为单位，指定为标量。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Distance and Frequency`。

### **Carrier frequency (MHz)** — 载波频率 `1920`（默认） | 标量

载波频率，以 MHz 为单位，指定为标量。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Distance and Frequency`。

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

**R2006a 之前引入**

## 描述

对复数信号应用自由空间路径损耗

Free Space Path Loss 模块对复数信号应用自由空间路径损耗。该模块模拟由于发射机与接收机之间的距离而导致的信号功率损耗。**Mode** 参数指示是以 dB 为单位指定损耗，还是基于距离和 RF 信号频率计算损耗。
