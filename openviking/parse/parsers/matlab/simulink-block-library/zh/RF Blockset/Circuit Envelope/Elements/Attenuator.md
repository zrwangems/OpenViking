---
type: simulink-block
title: 'Attenuator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'attenuator'
documentation_source_path: 'ref/attenuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Attenuator

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Attenuation (dB)
  summary: 插入损耗或衰减水平 3（默认）| 标量
  group: ''
- name: Input impedance (Ohm)
  summary: 输入阻抗 50（默认）| 标量
  group: ''
- name: Output impedance (Ohm)
  summary: 输出阻抗 50（默认）| 标量
  group: ''
- name: Simulate noise
  summary: 仿真热噪声 on（默认）| off
  group: ''
- name: Ground and hide negative terminals
  summary: 接地并隐藏 RF 电路端子 on（默认）| off
  group: ''
```

### **Attenuation (dB)** — 插入损耗或衰减水平 `3`（默认）| 标量

要应用于信号的插入损耗或衰减水平，以 dB 为单位指定为标量。

### **Input impedance (Ohm)** — 输入阻抗 `50`（默认）| 标量

衰减器的输入阻抗，以欧姆为单位指定为标量。

### **Output impedance (Ohm)** — 输出阻抗 `50`（默认）| 标量

衰减器的输出阻抗，以欧姆为单位指定为标量。

### **Simulate noise** — 仿真热噪声 on（默认）| off

选择此参数以仿真衰减器中的热噪声。您必须在 Configuration 模块中选择 **Simulate noise**。

此参数插入一个电流噪声源，其单边功率密度为 4
*k**T*/*R*
A2/Hz，其中：

- *T* 是 Configuration 模块中 **Temperature** 参数的值。单位为开尔文度。
- *k* 是玻尔兹曼常数。

### **Ground and hide negative terminals** — 接地并隐藏 RF 电路端子 on（默认）| off

选择此参数以接地并隐藏负端子。要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其它部分。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

### R2021b：Attenuator 模块图标已更新

从 R2021b 开始，Attenuator 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Attenuator 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

为 RF 电路建模衰减器

Attenuator 模块按给定因子衰减信号功率，该因子称为以 dB 为单位的*插入损耗*。通常，该模块在输入和输出端口处匹配 RF 电路的阻抗。您可以使用衰减器来衰减输入信号的功率以保护 RF 电路。

Attenuator 模块掩码图标是动态的，并指示所应用噪声参数的当前状态。此表显示了此模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Simulate noise 设置为 on 时的 Attenuator 模块图标。 | Simulate noise 设置为 off 时的 Attenuator 模块图标。 |
