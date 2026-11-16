---
type: simulink-block
title: 'SPDT'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'spdt'
documentation_source_path: 'ref/spdt.html'
language: zh-CN
chinese_source: worker-translation
---

# SPDT

## 端口

### 输入

### **Vctl** — Simulink 控制信号 scalar

Simulink 控制信号，指定为 scalar。

**数据类型：** `double`

## 参数

### **Threshold voltage** — Threshold voltage `0`（默认）| positive scalar

开关的 Threshold voltage，指定为以 volts 为单位的 positive scalar。

### **Characterization** — Characterization `Resistance`（默认）| `Insertion loss`

开关的 Characterization，指定为 `Resistance`
或 `Insertion loss`。

### **On resistance** — On resistance `10`（默认）| positive scalar

开关的 On resistance 值，指定为以 ohms 为单位的 positive scalar。
当您将 **Characterization** 设置为 `Resistance` 时，
**On resistance** 可用。

### **Off resistance** — Off resistance `1e-6`（默认）| positive scalar

开关的 Off resistance 值，指定为以 ohms 为单位的 positive scalar。
当您将 **Characterization** 设置为 `Resistance` 时，
**Off resistance** 可用。

### **Insertion loss (dB)** — Insertion loss `1`（默认）| scalar

开关的 Insertion loss 值，指定为以 decibels 为单位的 positive scalar。
当您将 **Characterization** 设置为 `Insertion
loss` 时，**Insertion loss (dB)** 可用。

### **Isolation (dB)** — Isolation value `70`（默认）| scalar

开关的 Isolation 值，指定为以 decibels 为单位的 scalar。
当您将 **Characterization** 设置为 `Insertion
loss` 时，**Isolation (dB)** 可用。

### **Loading type** — Loading type `Reflective`（默认）| `Absorptive`

开关的 Loading type，指定为 `Reflective` 或
`Absorptive`。

### **Port terminations (Ohm)** — Port terminations `50`（默认）| scalar | vector of size 1-by-3

与 `SPDT` 开关的阻抗条件匹配的 Port terminations，指定为以 ohms 为单位的 scalar 或大小为 1-by-3 且每个元素单位均为 ohms 的 vector。如果该值为 scalar，则所有三个（输入端口和两个输出端口）阻抗相同。如果该值为 vector，则第一个值是模块的输入端口处所需的匹配，另外两个值必须相同，并表示两个输出端口处所需的匹配。

**注意**

当您将 `SPDT` 开关的 **Characterization** 设置为
`Insertion loss`，或将 **Loading
type** 设置为 `Absorptive` 时，**Port terminations** 可用。

### **Ground and hide reference terminals** — 将 RF 电路端子接地 on（默认）| off

选择此参数可在内部将参考端子接地并隐藏。要暴露参考端子，请清除此参数。通过暴露这些端子，可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

单刀双掷开关

SPDT 模块对单刀双掷开关进行建模。此模块同时支持 reflective 和 absorptive 开关。控制信号是连接到模块 `Vctl` 端口的 Simulink® 信号。控制信号指定哪个输出端口传输输入信号 `In`。

- 如果控制电压小于阈值电压，则模块将输入信号传输到第一个输出端口 `Out1`。
- 如果控制电压大于或等于阈值电压，则模块将输入信号传输到第二个输出端口 `Out2`。

两个不同的电阻器调节用于将输入信号从输入端口传输到任一输出端口的导电路径。
