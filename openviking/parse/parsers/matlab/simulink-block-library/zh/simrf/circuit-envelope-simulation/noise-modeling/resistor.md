---
type: simulink-block
title: 'Resistor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Basic Components'
documentation_page: 'resistor'
documentation_source_path: 'ref/resistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Resistor

## 端口

R2025b 中未记录。

## 参数

### **Resistance** — 电阻值 `50 Ohm`（默认） | 以 ohms 为单位的实数

电阻值，指定为大于零的实数，单位为 ohms。从相应的下拉菜单中指定电阻的单位。

### **Simulate noise** — 模拟热噪声 `on`（默认） | `off`

选择此参数，以模拟电阻中的热噪声。然后，在 Configuration 模块对话框中，还要选中 **Simulate noise** 复选框。默认情况下，两个 **Simulate noise** 复选框都处于选中状态。

此参数插入一个电流噪声源，其单边功率密度为 4
*k**T*/*R*
A2/Hz，其中：

- k 是玻尔兹曼常数
- T 是 **Temperature** 参数的值，
  单位为 Kelvin。（也位于 Configuration 模块中。）

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

### R2021b: Resistor 模块图标已更新

从 R2021b 开始，Resistor 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Resistor 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

为电路包络分析建立电阻模型

Resistor 模块在 RF Blockset™ 电路包络仿真环境中对电阻进行建模。有关 RF 仿真的介绍，请参阅示例 Simulate High Frequency Components。

该模块实现以下关系

v(t)=Ri(t)

其中：

- *R* 表示电阻，作为温度的函数。
- *i*(*t*) 表示在时间 *t* 流过电容器的电流。
- *v*(*t*) 表示在时间 *t* 电容器两端之间的电压。

RF Blockset 电流和电压信号由 Configuration 模块中指定的每个频率 *fk* 处的同相（*Ik*）和正交（*Qk*）分量组成：

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t

Resistor 模块封装图标是动态的，并指示所应用噪声参数的当前状态。此表显示了此模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: on | Simulate noise: off |
| --- | --- |
| Simulate noise 设置为 on 时的 Resistor 模块图标。 | Simulate noise 设置为 off 时的 Resistor 模块图标。 |

要了解如何使用 Resistor 模块设计输出匹配网络，请打开 *RF Receiver Front End* 子系统，并在 Radar System Modeling 示例中选择 *Linear* → *Output Matching*。
