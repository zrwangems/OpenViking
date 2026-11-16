---
type: simulink-block
title: 'SPST'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
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

### **阈值电压** — 阈值电压 `0`（默认）| 正标量

开关的阈值电压，指定为以 volts 为单位的正标量。

### **特性表征** — 特性表征 `Resistance`（默认）| `Insertion loss`

开关的特性表征，指定为 `Resistance` 或 `Insertion loss`。

### **导通电阻** — 导通电阻 `10`（默认）| 正标量

开关的导通电阻值，指定为以 ohms 为单位的正标量。
当将 **特性表征** 设置为 `Resistance` 时，**导通电阻** 可用。

### **关断电阻** — 关断电阻 `1e-6`（默认）| 正标量

开关的关断电阻值，指定为以 ohms 为单位的正标量。
当将 **特性表征** 设置为 `Resistance` 时，**关断电阻** 可用。

### **插入损耗 (dB)** — 插入损耗 `1`（默认）| 标量

开关的插入损耗值，指定为以 decibels 为单位的正标量。
当将 **特性表征** 设置为 `Insertion loss` 时，**插入损耗 (dB)** 可用。

### **隔离度 (dB)** — 隔离度值 `70`（默认）| 标量

开关的隔离度值，指定为以 decibels 为单位的标量。
当将 **特性表征** 设置为 `Insertion loss` 时，**隔离度 (dB)** 可用。

### **负载类型** — 负载类型 `Reflective`（默认）| `Absorptive`

开关的负载类型，指定为 `Reflective` 或 `Absorptive`。

### **端口端接 (Ohm)** — 端口端接 `50`（默认）| 标量 | 大小为 1-by-2 的向量

与 `SPDT` 开关的阻抗条件匹配的端口端接，指定为以 ohms 为单位的标量，或指定为大小为 1-by-2 的向量，其中每个元素的单位均为 ohms。如果该值为标量，则输入端口和输出端口的阻抗相同。如果该值为向量，则第一个值是在模块的输入端口处所需的匹配，第二个值是在输出端口处所需的匹配。

**注意**

当将 `SPST` 开关的 **特性表征** 设置为 `Insertion loss`，或将 **负载类型** 设置为 `Absorptive` 时，**端口端接** 可用。

### **接地并隐藏参考端子** — 将 RF 电路端子接地 on（默认）| off

选择此参数可在内部将参考端子接地并隐藏它们。要暴露参考端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

单刀单掷开关

SPST 模块对单刀单掷开关进行建模。此模块同时支持反射式和吸收式开关。控制信号是连接到模块 `Vctl` 端口的 Simulink® 信号。控制信号指定输出端口 `Out` 何时传输输入端口 `In` 处的输入信号。
