---
type: simulink-block
title: 'Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Basic Components'
documentation_page: 'attenuator'
documentation_source_path: 'ref/attenuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Attenuator

## 端口

未在 R2025b 中记录。

## 参数

### **Attenuation (dB)** — 插入损耗或衰减的电平 `3`（默认）| scalar

要应用于信号的插入损耗或衰减电平，指定为以 dB 为单位的 scalar。

### **Input impedance (Ohm)** — 输入阻抗 `50`（默认）| scalar

衰减器的输入阻抗，指定为以 ohms 为单位的 scalar。

### **Output impedance (Ohm)** — 输出阻抗 `50`（默认）| scalar

衰减器的输出阻抗，指定为以 ohms 为单位的 scalar。

### **Simulate noise** — 模拟热噪声 on（默认）| off

选择此参数以模拟衰减器中的热噪声。
您必须在 Configuration 模块中选择 **Simulate noise**。

此参数插入一个电流噪声源，其单边功率密度为 4
*k**T**/*R*
A2/Hz，其中：

- *T* 是 Configuration 模块中 **Temperature** 参数的值。单位为 degrees Kelvin。
- *k* 是玻尔兹曼常数。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 on（默认）| off

选择此参数以将负极端子接地并隐藏。
要显示负极端子，清除此参数。通过显示这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

### R2021b：Attenuator 模块图标已更新

从 R2021b 开始，Attenuator 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Attenuator 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

为 RF 电路建模衰减器

Attenuator 模块按给定因子衰减信号功率，该因子称为 *Insertion Loss*，单位为 dB。通常，该模块在输入和输出端口匹配 RF 电路的阻抗。您可以使用衰减器来降低输入信号的功率，以保护 RF 电路。

Attenuator 模块封装图标是动态的，并指示所应用噪声参数的当前状态。此表显示此模块上的图标如何根据该模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| 当 Simulate noise 设置为 on 时的 Attenuator 模块图标。 | 当 Simulate noise 设置为 off 时的 Attenuator 模块图标。 |
