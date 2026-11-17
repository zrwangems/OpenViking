---
type: simulink-block
title: 'Variable Resistor'
family: 'circuit-envelope'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableresistor'
documentation_source_path: 'ref/variableresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Resistor

## 端口

### 输入

### **R** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

### **Simulate noise** — 模拟热噪声 `on`（默认） | `off`

选择此参数，以模拟可变电阻器中的热噪声。然后，在 Configuration 模块对话框中，还要选中 **Simulate noise** 复选框。默认情况下，两个 **Simulate noise** 复选框均处于选中状态。

此参数会插入一个电流噪声源，其单边功率密度为 4 *k**T*/*R* A2/Hz，其中：

- k 是玻尔兹曼常数
- T 是 **Temperature** 参数的值，单位为 degrees Kelvin。（也位于 Configuration 模块中。）

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

### R2021b：Variable Resistor 模块图标已更新

从 R2021b 开始，Variable Resistor 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开一个在 R2021b 之前创建的包含 Variable Resistor 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

对可变电阻器建模

Variable Resistor 模块使用 Simulink® 控制的电阻（单位为 ohms）来控制 RF Blockset™ 反馈电路的输出。电阻的最小值 (*Rmin*) 是由 RF Blockset 定义的常量，与 Simulink 控制信号无关。该模块有两个电端子。一个端子用于 Simulink 控制信号，另一个端子用于 RF Blockset 信号。

Variable Resistor 模块封装图标是动态的，并显示所应用噪声参数的当前状态。下表显示了此模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Simulate noise 设置为 on 时的 Variable Resistor 模块图标。 | Simulate noise 设置为 off 时的 Variable Resistor 模块图标。 |
