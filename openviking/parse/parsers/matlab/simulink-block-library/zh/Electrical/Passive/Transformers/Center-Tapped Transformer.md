---
type: simulink-block
title: 'Center-Tapped Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'centertappedtransformer'
documentation_source_path: 'ref/centertappedtransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Center-Tapped Transformer

## 端口

### 守恒端口

### **1+** — 一次绕组正极性电气端口

与一次绕组正极性相关联的电气守恒端口。

### **1-** — 一次绕组负极性电气端口

与一次绕组负极性相关联的电气守恒端口。

### **2+** — 二次绕组正极性电气端口

与二次绕组正极性相关联的电气守恒端口。

### **2-** — 二次绕组负极性电气端口

与二次绕组负极性相关联的电气守恒端口。

### **c** — 二次绕组中心抽头电气端口

与二次绕组中心抽头相关联的电气守恒端口。

## 参数

### **Modeling option** — 用于选择对理想或非理想中心抽头变压器进行建模的选项 `Ideal`（默认）| `Non-Ideal`

用于选择对理想或非理想中心抽头变压器进行建模的选项。如果将此参数设置为 `Non-Ideal`，则该模块还会对绕组、基本磁阻和涡流进行建模。

### **Winding ratio** — 变压器的绕组比 `1`（默认）| 正标量

变压器的绕组比，等于一次线圈匝数与二次线圈匝数之比。

### **Center tap position (0~1)** — 中心抽头在二次绕组上的位置 `0.5`（默认）| 范围 (0, 1) 内的标量

中心抽头在二次绕组上的位置。

### **Primary winding resistance** — 一次绕组的串联电阻 `0.01` `Ohm`（默认）| 正标量

一次绕组的串联电阻。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

### **Primary leakage inductance** — 一次绕组的漏电感 `0.0001` `H`（默认）| 正标量

一次绕组的漏电感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

### **Secondary winding resistance** — 二次绕组的串联电阻 `0.01` `Ohm`（默认）| 正标量

二次绕组的串联电阻。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

### **Secondary leakage inductance** — 二次绕组的漏电感 `0.0001` `H`（默认）| 正标量

二次绕组的漏电感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

### **Magnetization resistance** — 变压器的磁化电阻 `100` `Ohm`（默认）| 正标量

变压器的磁化电阻。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

### **Magnetization inductance** — 变压器的磁化电感 `0.04` `H`（默认）| 正标量

变压器的磁化电感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Non-Ideal`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

单相中心抽头变压器

Center-Tapped Transformer 模块实现了一个中心抽头变压器。在开关电源应用中，您经常在全波整流器内使用中心抽头变压器，这需要从交流输入获得完整的直流输出。

连接到 Center-Tapped Transformer 模块一次绕组和二次绕组的两个电气网络必须各自拥有自己的 Electrical Reference 模块。通常，您还需要将二次绕组的中心抽头连接到 Electrical Reference 模块。

### 方程

此图显示了当您将 **Modeling option** 参数设置为 `Ideal` 时 Center-Tapped Transformer 模块的等效电路：

此图显示了当您将 **Modeling option** 参数设置为 `Non-Ideal` 时 Center-Tapped Transformer 模块的等效电路：

您必须确定模块掩码中的电气域参数与等效电路模型中使用的磁域参数之间的关系：

- *n* 是 **Winding ratio** 参数的值。
- *L*1 是 **Primary leakage inductance** 参数的值。
- *R*m 是 **Magnetization resistance** 参数的值。
- *L*m 是 **Magnetization inductance** 参数的值。
- *T* 是 **Center tap position (0~1)** 参数的值。
- *L*2 是 **Secondary leakage inductance** 参数的值。
- *Rw*2 是 **Secondary winding resistance** 参数的值。
- R1=n2L1 是一次绕组漏磁阻。
- R=n2Lm 是并联磁化电阻。
- Leddy=n2Rm 是涡流回路的电导。
- R2=(1−T)2+T2L2 是二次绕组漏磁阻。
- Rw2p=Rw2(1−T) 是二次上绕组电阻。
- Rw2n=Rw2T 是二次下绕组电阻。
