---
type: simulink-block
title: 'SPnT'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'spnt'
documentation_source_path: 'ref/spnt.html'
language: zh-CN
chinese_source: worker-translation
---

# SPnT

## 端口
```yaml
ports:
- name: Ctl
  summary: Simulink 控制信号标量
  direction: input
  data_types: double
```

### 输入

### **Ctl** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Insertion loss (dB)
  summary: 开关插入损耗 1（默认）| 标量
  group: ''
- name: Isolation (dB)
  summary: 开关隔离值 70（默认）| 标量
  group: ''
- name: Loading type
  summary: 开关类型 Absorptive（默认）| Reflective
  group: ''
- name: Number of outputs
  summary: 开关的输出数量 2（默认）| 标量
  group: ''
- name: Port terminations (Ohm)
  summary: 端口端接 50（默认）| 标量
  group: ''
- name: Ground and hide reference terminals
  summary: 将 RF 电路参考端子接地 开（默认）| 关
  group: ''
```

#### 主

### **Insertion loss (dB)** — 开关插入损耗 `1`（默认）| 标量

开关的插入损耗值，指定为以分贝为单位的有限标量。
指定的插入损耗值应大于零且小于开关的隔离值。有关公式，请参阅插入损耗。

### **Isolation (dB)** — 开关隔离值 `70`（默认）| 标量

开关的隔离值，指定为以分贝为单位的标量。指定的隔离值应大于开关的插入损耗值。有关公式，请参阅隔离。

### **Loading type** — 开关类型 `Absorptive`（默认）| `Reflective`

开关类型，指定为 `Absorptive` 或 `Reflective`。

### **Number of outputs** — 开关的输出数量 `2`（默认）| 标量

开关的输出数量，指定为标量。输出数量必须大于或等于二，或小于或等于八。

### **Port terminations (Ohm)** — 端口端接 `50`（默认）| 标量

端口端接，表示所有输入和输出端口所需的匹配，指定为以欧姆为单位的标量。如果将 **Load type** 设置为 `Absorptive`，则所有断开输出端口处的阻抗为 **Port terminations** 中指定的值。

### **Ground and hide reference terminals** — 将 RF 电路参考端子接地 开（默认）| 关

选择此参数可在内部将参考端子接地并隐藏。要暴露参考端子，请清除此参数。通过暴露此端子，您可以将其连接到模型的其它部分。
## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

单刀多掷开关

SPnT 模块对单刀多掷开关进行建模。此模块同时支持反射式和吸收式开关。您可以为开关指定二到八个输出端口。控制信号是连接到模块 `Ctl` 端口的 Simulink® 信号。控制信号指定哪个输出端口传输输入信号。当 `Ctl` 端口的输入值介于 1 和输出端口数量之间时，`Ctl` 信号值将舍入到最接近的整数。与该整数值对应的输出端口传输数据。如果舍入后的 `Ctl` 信号值不对应任何输出端口，则所有输出端口均关闭。
