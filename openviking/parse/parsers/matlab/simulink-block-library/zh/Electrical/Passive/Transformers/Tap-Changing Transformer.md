---
type: simulink-block
title: 'Tap-Changing Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'tapchangingtransformer'
documentation_source_path: 'ref/tapchangingtransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Tap-Changing Transformer

## 端口
```yaml
ports:
- name: 1+
  summary: 线路 1 正极端子电气
  direction: conserving
- name: 1-
  summary: 线路 1 负极端子电气
  direction: conserving
- name: 2+
  summary: 线路 2 正极端子电气
  direction: conserving
- name: 2-
  summary: 线路 2 负极端子电气
  direction: conserving
- name: c
  summary: 控制输入物理
  direction: conserving
```

### 守恒端口

### **1+** — 线路 1 正极端子电气

与线路 1 正极端子关联的电气守恒端口。

### **1-** — 线路 1 负极端子电气

与线路 1 负极端子关联的电气守恒端口。

### **2+** — 线路 2 正极端子电气

与线路 2 正极端子关联的电气守恒端口。

### **2-** — 线路 2 负极端子电气

与线路 2 负极端子关联的电气守恒端口。

### **c** — 控制输入物理

指定输入控制值的输入物理信号。
## 参数
```yaml
parameters:
- name: Turns ratio (primary/secondary)
  summary: 匝数比 1（默认）| 正数
  group: 标称
- name: Primary leakage inductance
  summary: 线路 1 漏电感 1e-6 H（默认）| 正数
  group: 标称
- name: Secondary leakage inductance
  summary: 线路 2 漏电感 1e-6 H（默认）| 正数
  group: 标称
- name: Core-loss resistance
  summary: 互感电阻 1e6 Ohm（默认）| 零或正数
  group: 标称
- name: Magnetization inductance
  summary: 磁化电感 100e-6 H（默认）| 正数
  group: 标称
- name: Primary series resistance
  summary: 线路 1 串联电阻 0 Ohm（默认）| 零或正数
  group: 标称
- name: Secondary series resistance
  summary: 线路 2 串联电阻 0 Ohm（默认）| 零或正数
  group: 标称
- name: Primary leakage conductance
  summary: 线路 1 漏电导 0 1/Ohm（默认）| 零或正数
  group: 标称
- name: Secondary leakage conductance
  summary: 线路 2 漏电导 0 1/Ohm（默认）| 零或正数
  group: 标称
- name: Tap-changer location
  summary: 分接头绕组 Primary（默认）| Secondary
  group: 分接头
- name: Minimum tap index (nominal=0)
  summary: 最小分接头位置 -5（默认）| 零或负整数
  group: 分接头
- name: Maximum tap index (nominal=0)
  summary: 最大分接头位置 5（默认）| 零或正整数
  group: 分接头
- name: Change per tap (%)
  summary: 分接头变化步长 1 %（默认）| 正数
  group: 分接头
- name: Control threshold
  summary: 偏移阈值 0.5（默认）
  group: 分接头
```

### 标称

### **Turns ratio (primary/secondary)** — 匝数比 `1`（默认）| 正数

变压器在标称分接头位置处的匝数比。匝数比定义为主绕组匝数除以副绕组匝数。

### **Primary leakage inductance** — 线路 1 漏电感 `1e-6` `H`（默认）| 正数

主绕组的漏电感。

### **Secondary leakage inductance** — 线路 2 漏电感 `1e-6` `H`（默认）| 正数

副绕组的漏电感。

### **Core-loss resistance** — 互感电阻 `1e6` `Ohm`（默认）| 零或正数

变压器的互感电阻。

### **Magnetization inductance** — 磁化电感 `100e-6` `H`（默认）| 正数

变压器的磁化电感。

### **Primary series resistance** — 线路 1 串联电阻 `0` `Ohm`（默认）| 零或正数

主绕组的串联电阻。

### **Secondary series resistance** — 线路 2 串联电阻 `0` `Ohm`（默认）| 零或正数

副绕组的串联电阻。

### **Primary leakage conductance** — 线路 1 漏电导 `0` `1/Ohm`（默认）| 零或正数

主绕组的漏电导。在某些电路拓扑中，将此值设置为非零以实现数值收敛。

### **Secondary leakage conductance** — 线路 2 漏电导 `0` `1/Ohm`（默认）| 零或正数

副绕组的漏电导。在某些电路拓扑中，将此值设置为非零以实现数值收敛。

### 分接头

### **Tap-changer location** — 分接头绕组 `Primary`（默认）| `Secondary`

指定分接头位于主绕组还是副绕组上。

### **Minimum tap index (nominal=0)** — 最小分接头位置 `-5`（默认）| 零或负整数

分接头的最小允许位置。

### **Maximum tap index (nominal=0)** — 最大分接头位置 `5`（默认）| 零或正整数

分接头的最大允许位置。

### **Change per tap (%)** — 分接头变化步长 `1` `%`（默认）| 正数

分接头绕组每个分接头位置步长的匝数百分比变化。设置此值时应使最小和最大分接头索引处的绝对百分比变化小于 `100` `%`。

### **Control threshold** — 偏移阈值 `0.5`（默认）

分接头改变位置时的控制值。要降低分接头位置，施加小于此值负值的控制信号 **c**。要增加分接头位置，施加大于此值的控制信号 **c**。
## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

单相有载调压变压器

Tap-Changing Transformer 模块表示单相有载调压变压器。您可以在仿真期间使用控制输入来改变变压器的匝数比。

使用此组件可在仿真期间调节或改变线性变压器的输出电压。要对饱和效应进行建模，请考虑使用 Nonlinear Transformer 模块。

### 工作原理

使用控制输入 **c** 来改变变压器的分接头位置。

- 将 **c** 增加到 **Control threshold** *t* 以上，使分接头位置 *p* 增加一。
- 将 **c** 减小到 **Control threshold** 的负值以下，使分接头位置 *p* 减少一。

下图显示了分接头对控制输入的响应。

图中：

- *N0* 是分接头绕组的标称匝数。
- *δ* 是每个分接头位置步长的匝数百分比变化。使用 **Change per tap (%)** 参数指定此值。
- *pmin* 和 *pmax* 是最小和最大允许分接头索引。使用 **Minimum tap index (nominal=0)** 和 **Maximum tap index (nominal=0)** 参数指定这些值。

要选择分接头绕组，请使用 **Tap-changer location** 参数。总匝数比 *n* 取决于此位置：

- `Primary`

  n=Np(N0,δ,p)Ns=n0(1+δp100)
- `Secondary`

  n=NpNs(N0,δ,p)=n0(1+δp100)−1

其中 *n0* 是变压器的标称匝数比。

### 等效电路

等效电路如图所示。

其中：

- *Rp* 和 *Rs* 分别是主绕组和副绕组的串联电阻。分接头位置的变化会影响这些值。
- *Llp* 和 *Lls* 分别是主绕组和副绕组的漏电感。分接头位置的变化会影响这些值。
- *Rm* 和 *M* 分别是磁化电阻和电感。分接头位置的变化会影响这些值。
- *n* 是变压器的匝数比。
- *Gp* 和 *Gs* 分别是主绕组和副绕组的漏电导。分接头位置的变化不会影响这些值。
