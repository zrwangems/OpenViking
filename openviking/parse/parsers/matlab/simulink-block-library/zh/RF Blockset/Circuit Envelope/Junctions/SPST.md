---
type: simulink-block
title: 'SPST'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'spst'
documentation_source_path: 'ref/spst.html'
language: zh-CN
chinese_source: worker-translation
---

# SPST

## 端口

### 输入

### **Vctl** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

### **Threshold voltage** — 阈值电压 `0`（默认）| 正标量

开关的阈值电压，指定为以伏特为单位的正标量。

### **Characterization** — 特性 `Resistance`（默认）| `Insertion loss`

开关的特性，指定为 `Resistance` 或 `Insertion loss`。

### **On resistance** — 导通电阻 `10`（默认）| 正标量

开关的导通电阻值，指定为以欧姆为单位的正标量。
当 **Characterization** 设置为 `Resistance` 时，**On resistance** 可用。

### **Off resistance** — 关断电阻 `1e-6`（默认）| 正标量

开关的关断电阻值，指定为以欧姆为单位的正标量。
当 **Characterization** 设置为 `Resistance` 时，**Off resistance** 可用。

### **Insertion loss (dB)** — 插入损耗 `1`（默认）| 标量

开关的插入损耗值，指定为以分贝为单位的正标量。
当 **Characterization** 设置为 `Insertion loss` 时，**Insertion loss (dB)** 可用。

### **Isolation (dB)** — 隔离度值 `70`（默认）| 标量

开关的隔离度值，指定为以分贝为单位的标量。
当 **Characterization** 设置为 `Insertion loss` 时，**Isolation (dB)** 可用。

### **Loading type** — 负载类型 `Reflective`（默认）| `Absorptive`

开关的负载类型，指定为 `Reflective` 或 `Absorptive`。

### **Port terminations (Ohm)** — 端口端接 `50`（默认）| 标量 | 大小为 1×2 的向量

与 `SPDT` 开关的阻抗条件匹配的端口端接，指定为以欧姆为单位的标量或以欧姆为单位的 1×2 向量，其中每个元素单位为欧姆。如果该值为标量，则输入端口和输出端口阻抗相同。如果该值为向量，则第一个值是模块输入端口所需的匹配，第二个值是输出端口所需的匹配。

**注意**

当您将 `SPST` 开关的 **Characterization** 设置为 `Insertion loss` 时，或者当您将 **Loading type** 设置为 `Absorptive` 时，**Port terminations** 可用。

### **Ground and hide reference terminals** — 接地并隐藏参考端子 开（默认）| 关

选择此参数可将参考端子内部接地并隐藏。要暴露参考端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

单刀单掷开关

SPST 模块对单刀单掷开关进行建模。此模块同时支持反射式和吸收式开关。控制信号是连接到模块 `Vctl` 端口的 Simulink® 信号。控制信号指定输出端口 `Out` 何时在输入端口 `In` 传输输入信号。
