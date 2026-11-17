---
type: simulink-block
title: 'VGA'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'vga'
documentation_source_path: 'ref/vga.html'
language: zh-CN
chinese_source: worker-translation
---

# VGA

## 端口
```yaml
ports:
- name: Gain
  summary: 功率增益信号标量
  direction: input
  data_types: double
- name: IP2
  summary: 二阶截点信号标量
  direction: input
  data_types: double
- name: IP3
  summary: 三阶截点信号标量
  direction: input
  data_types: double
```

### 输入

### **Gain** — 功率增益信号标量

功率增益信号，指定为以 dB 为单位的标量。功率增益信号是 Simulink 信号。

**数据类型：** `double`

### **IP2** — 二阶截点信号标量

二阶截点信号，指定为以 dBm 为单位的标量。二阶截点信号是 Simulink 信号。

**数据类型：** `double`

### **IP3** — 三阶截点信号标量

三阶截点信号，指定为以 dBm 为单位的标量。三阶截点信号是 Simulink 信号。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Input impedance (Ohm)
  summary: VGA 的输入阻抗 50（默认）| 标量
  group: ''
- name: Output impedance (Ohm)
  summary: VGA 的输出阻抗 50（默认）| 正标量
  group: ''
- name: Intercept points convention
  summary: 输入参考或输出参考约定 Output（默认）| Input
  group: ''
- name: Ground and hide negative terminals
  summary: 接地并隐藏负端子 on（默认）| off
  group: ''
```

### **Input impedance (Ohm)** — VGA 的输入阻抗 `50`（默认）| 标量

VGA 的输入阻抗，指定为以欧姆为单位的标量。

### **Output impedance (Ohm)** — VGA 的输出阻抗 `50`（默认）| 正标量

VGA 的输出阻抗，指定为以欧姆为单位的标量。

### **Intercept points convention** — 输入参考或输出参考约定 `Output`（默认）| `Input`

IP2 或 IP3 截点的输入参考或输出参考约定，指定为 `Input` 或 `Output`。

### **Ground and hide negative terminals** — 接地并隐藏负端子 `on`（默认）| `off`

接地并隐藏负端子，指定为 `on` 或 `off`。选择此参数可在内部将负端子接地并隐藏。清除该选项可暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

对可变增益放大器进行建模

VGA 模块对 RF Blockset™ 可变增益放大器（VGA）进行建模。Simulink® 信号控制非线性增益。

三个 Simulink 输入端口为 `Gain`、`IP2`（二阶截点）和 `IP3`（三阶截点）。端口 `In` 是 RF Blockset 电压输入，端口 `OUT` 是 RF Blockset 电压输出。
