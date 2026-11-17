---
type: simulink-block
title: 'Cauer Thermal Model'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'cauerthermalmodel'
documentation_source_path: 'ref/cauerthermalmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Cauer Thermal Model

## 端口

### 守恒端口

### **A** — 半导体各层第一个表面的热端口

与半导体各层第一个表面相关联的热守恒端口。

### **B** — 半导体最后一层第二个表面的热端口

与半导体最后一层第二个表面相关联的热守恒端口。

## 参数

### **Parameterize Cauer model using Foster coefficient data** — 使用 Foster 系数数据参数化 Cauer 模型 `Off`（默认）| `On`

是否使用 Foster 模型的系数数据来参数化 Cauer 模型。

### **Thermal resistance data** — 热阻 `1e-3 * [2.6468, 3.8701, 1.2007, .8824]` `K/W`（默认）

热阻向量。

#### 依赖关系

要启用此参数，请清除 **Parameterize Cauer model using Foster coefficient data** 参数。

### **Thermal time constant data** — 热时间常数 `[.0086, .054, .3624, 1.651]` `s`（默认）

热时间常数向量。

#### 依赖关系

要启用此参数，请清除 **Parameterize Cauer model using Foster coefficient data** 参数。

### **Thermal resistance data (Foster)** — 从 Foster 数据参数化的热阻 `[.0016, .0043, .0013, .0014]` `K/W`（默认）

使用 Foster 模型数据参数化的热阻向量。

#### 依赖关系

要启用此参数，请选中 **Parameterize Cauer model using Foster coefficient data** 参数。

### **Thermal time constant data (Foster)** — 从 Foster 数据参数化的热时间常数 `[.0068, .064, .32, 2]` `s`（默认）

使用 Foster 模型数据参数化的热时间常数向量。

#### 依赖关系

要启用此参数，请选中 **Parameterize Cauer model using Foster coefficient data** 参数。

## 所属库

Simscape / Electrical / Passive / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2022b：移除 **R** 端口和 **Show absolute reference port** 参数

Cauer Thermal Model 模块不再支持外部 **R** 端口。参考温度设置为 `0` Kelvin。在您的模型中，请删除先前连接到 Cauer Thermal Model 模块 **R** 端口的模块。

## 描述

通过半导体模块多层结构的热传递

Cauer Thermal Model 模块表示通过半导体模块多层结构的热传递。一个 Cauer Thermal Model 包含多个 Cauer Thermal Model Element 组件。该图显示了 Cauer Thermal Model Element 的等效电路。

Cauer 热模型的多层结构包括芯片、焊料、基板和底座。描述 Cauer 热模型的其他术语有：

- 连分式电路
- T 模型
- 梯形网络

该图显示了 Cauer Thermal Model 的等效电路。

**R** 处的温度等于绝对零度。

### 方程

每个 Cauer 热模型元素的定义方程为

Cthermal=τRthermal，

QAB=TABRthermal，

以及

QAR=CthermaldTARdt，

其中：

- *Cthermal* 是热容。
- *τ* 是热时间常数。
- *Rthermal* 是热阻。
- *QAB* 是通过材料的热流。
- *TAB* 是材料层之间的温差。
- *QAR* 是通过热容的热流。
- *TAR* 是热容两端的温度降。

### 从 Foster 系数参数化 Cauer 模型

半导体器件的数据手册通常使用 Foster 系数来指定热模型。然而，Cauer 热模型更为有用，因为您可以将其扩展为包含额外的热组件，例如散热器以及辐射或对流元件。

要从 Foster 热模型数据参数化 Cauer Thermal Model 模块，请选中 **Parameterize Cauer model using Foster coefficient data** 参数。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

要指定每个热容的初始温度，请设置 **Vector of thermal mass temperatures** 变量的值。此向量的长度必须等于 Cauer 热模型元素的数量。它对应于模型中每个热容两端的温度降。
