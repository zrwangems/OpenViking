---
type: simulink-block
title: 'Variable Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableattenuator'
documentation_source_path: 'ref/variableattenuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Attenuator

## 端口

### 输入

### **Att** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。此控制信号是以 dB 为单位的*插入损耗*。

**数据类型：** `double`

## 参数

### **Minimum attenuation (dB)** — 插入损耗或衰减的最低值 `0.001`（默认值）| 标量

要应用于信号的插入损耗或衰减的最低值，指定为以 dB 为单位的标量。

### **Maximum attenuation (dB)** — 插入损耗或衰减的最高值 `1000`（默认值）| 标量

要应用于信号的插入损耗或衰减的最高值，指定为以 dB 为单位的标量。

### **Input impedance (Ohm)** — 输入阻抗 `50`（默认值）| 标量

衰减器的输入阻抗，指定为以欧姆为单位的标量。

### **Output impedance (Ohm)** — 输出阻抗 `50`（默认值）| 标量

衰减器的输出阻抗，指定为以欧姆为单位的标量。

### **Simulate noise** — 仿真热噪声 on（默认值）| off

选择此参数以仿真衰减器中的热噪声。您必须在 Configuration 模块中选择 **Simulate noise**。

此参数插入一个单边功率密度为 4 *k**T*/*R* A2/Hz 的电流噪声源，其中：

- *T* 是 Configuration 模块中 **Temperature** 参数的值。单位为开尔文度。
- *k* 是玻尔兹曼常数。

### **Ground and hide negative terminals** — 接地并隐藏 RF 电路端子 on（默认值）| off

选择此参数以接地并隐藏负端子。要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

### R2021b：Variable Attenuator 模块图标已更新

从 R2021b 开始，Variable Attenuator 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Variable Attenuator 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对可变衰减器进行建模

Variable Attenuator 模块以称为*插入损耗*的给定因子（以 dB 为单位）衰减信号功率。使用 Variable Attenuator 模块，您可以在仿真期间改变输入 Simulink® 信号的衰减量。通常，该模块在输入和输出端口处匹配 RF 电路的阻抗。您可以使用衰减器来抑制输入信号的功率以保护 RF 电路。

Variable Attenuator 模块掩码图标是动态的，并显示所应用噪声参数的当前状态。下表显示了此模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise：`on` | Simulate noise：`off` |
| --- | --- |
| Simulate noise 设置为 on 时的 Variable Attenuator 模块图标。 | Simulate noise 设置为 off 时的 Variable Attenuator 模块图标。 |
