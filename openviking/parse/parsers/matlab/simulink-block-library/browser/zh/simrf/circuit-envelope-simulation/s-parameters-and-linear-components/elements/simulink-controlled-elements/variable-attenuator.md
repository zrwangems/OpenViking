---
type: simulink-block
title: 'Variable Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Simulink Controlled Elements'
documentation_page: 'variableattenuator'
documentation_source_path: 'ref/variableattenuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Attenuator

## 端口

### 输入

### **Att** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。此控制信号是以 dB 为单位的 *插入损耗*。

**数据类型：** `double`

## 参数

### **最小衰减 (dB)** — 插入损耗或衰减的最低值 `0.001` (默认) | 标量

要应用于信号的插入损耗或衰减的最低值，指定为以 dB 为单位的标量。

### **最大衰减 (dB)** — 插入损耗或衰减的最高值 `1000` (默认) | 标量

要应用于信号的插入损耗或衰减的最高值，指定为以 dB 为单位的标量。

### **输入阻抗 (Ohm)** — 输入阻抗 `50` (默认) | 标量

衰减器的输入阻抗，指定为以 ohms 为单位的标量。

### **输出阻抗 (Ohm)** — 输出阻抗 `50` (默认) | 标量

衰减器的输出阻抗，指定为以 ohms 为单位的标量。

### **模拟噪声** — 模拟热噪声 on (默认) | off

选择此参数以模拟衰减器中的热噪声。您必须在 Configuration 模块中选择 **模拟噪声**。

此参数插入一个电流噪声源，其单边功率密度为 4 *k**T*/*R* A2/Hz，其中：

- *T* 是 Configuration 模块中 **温度** 参数的值。单位为 degrees Kelvin。
- *k* 是玻尔兹曼常数。

### **接地并隐藏负极端子** — 将 RF 电路端子接地 on (默认) | off

选择此参数以接地并隐藏负极端子。要暴露负极端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

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

对可变衰减器建模

Variable Attenuator 模块通过称为 *插入损耗* 的给定因子（单位为 dB）来衰减信号功率。使用 Variable Attenuator 模块，您可以在仿真期间改变输入 Simulink® 信号的衰减。通常，该模块在输入和输出端口处匹配 RF 电路的阻抗。您可以使用衰减器来减弱输入信号的功率，以保护 RF 电路。

Variable Attenuator 模块的封装图标是动态的，并显示所应用噪声参数的当前状态。下表显示了此模块上的图标如何根据模块上 **模拟噪声** 参数的状态而变化。

| 模拟噪声：`on` | 模拟噪声：`off` |
| --- | --- |
| 当模拟噪声设置为 on 时的 Variable Attenuator 模块图标。 | 当模拟噪声设置为 off 时的 Variable Attenuator 模块图标。 |
