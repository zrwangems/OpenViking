---
type: simulink-block
title: 'Divider'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'divider'
documentation_source_path: 'ref/divider.html'
language: zh-CN
chinese_source: worker-translation
---

# Divider

## 端口

未在 R2025b 中记录。

## 参数

### **Select component** — 功分器类型 `T power divider`（默认）| `Resistive power divider` | `Wilkinson power divider` | `Tee H-plane (S33=0)` | `Tee E-plane`

功分器类型，指定为：

- `T power divider`

  `T-power divider` 的 S 参数矩阵为：

  [s11s21s31s21s22s32s31s32s33]

  其中：

  - s11 = (z23
    –z1) / (z23 +
    z1)
  - s22 = (z13
    –z2) / (z13 +
    z2)
  - s33 = (z12
    –z3) / (z12 +
    z3)
  - s21 = (1+
    s11) \* sqrt(z1 / z2)
  - s31 = (1+
    s11) \* sqrt(z1 / z3)
  - s32 = (1+
    s22) \* sqrt(z2 / z3)
  - z12 = z1 \*
    z2 / (z1 + z2)
  - z13 = z1 \*
    z3 / (z1 + z3)
  - z23 = z2 \*
    z3 / (z2 + z3)
  - z1 = Z0(1),
    z2 = Z0(2), z3 = Z0(3)
  - 参考阻抗：Z0 = [z1,
    z2, z3 ]

- `Resistive power divider`

  `Resistive power divider` 的 S 参数矩阵为：

  [01/21/21/201/21/21/20]

  当您选择此选项时，以下参数可用：

- `Wilkinson power divider`

  `Wilkinson power divider` 的 S 参数矩阵为：

  [0-j/2-j/2-j/200-j/200]

  **注意**

  - 对于 DC 载波 (0 Hz) 频率，Wilkinson power divider 是零矩阵。
  - 从 R2021a 开始，当您选择 `Wilkinson power divider` 组件时，Divider 模块中的端口位置已更改。有关详细信息，请参阅版本历史。

- `Tee H-plane (S33=0)`

  `Tee H-plane (S33=0)` 是对称、无损和互易的。S 参数矩阵为：

  (−1121−12220)2

- `Tee E-plane`

  `Tee E-plane` 是对称、无损和互易的。S 参数矩阵为：

  (11211−22−20)2

### **Number of divider outports** — Wilkinson 功分器输出端口数量 `2`（默认）| 范围 (`1`, `65`] 内的非负整数

Wilkinson 功分器输出端口数量，指定为范围 (`1`, `65`] 内的非负整数。

#### 依赖关系

要启用此参数，请将 **Select Component** 设置为 `Wilkinson power divider`。

### **Reference impedances (Ohm)** — 功分器的参考阻抗 `50`（默认）| 正标量 | 三元组向量

功分器的参考阻抗，指定为正标量或三元组向量。

**注意**

当所有端口的参考阻抗不相等时，Divider 模块内部的模型会归一化到 50 ohms。

### **Ground and hide negative terminals** — 将 RF 电路端口接地 `on`（默认）| `off`

选择此参数以将负极端口接地并隐藏。要暴露负极端口，请清除该参数。通过暴露这些端口，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

### R2022b: 对具有最多 65 个端口的 Wilkinson 功分器建模

使用 Divider 模块对具有多于两个且最多 65 个输出端口的 Wilkinson 功分器进行建模。使用 **Number of divider outports** 设置输出端口的数量。

### R2021a: Divider 模块中 Wilkinson power divider 组件的端口位置已更改

当您选择 `Wilkinson power divider` 组件时，Divider 模块中的端口位置已更改。在此版本之前，端口 1 和 3 位于与端口 2 相对的同侧。此版本中，端口 2 和 3 一起出现在与端口 1 相对的一侧。

使用带有 `Wilkinson power divider` 组件的 Divider 模块的现有模型可能需要更新，以确保没有断开的连接。使用 Simulink® Upgrade Advisor 中的 RF Blockset 检查来识别并重新连接现有模型中断开的端口连接。有关详细信息，请参阅 Check model for RF Blockset Divider blocks using Wilkinson power divider component with broken connections.

## 描述

使用 S 参数对理想的频率无关功分器或合路器进行建模

Divider 模块在电路包络环境中将功分器或合路器建模为 S 参数模型。在功分器中，输入功率从一个端口进入，分路，并从不同端口输出。

要使用功分器对具有 32 元件混合波束成形天线的 66 GHz QPSK RF 发射和接收系统进行建模和仿真，请参阅 Modeling RF mmWave Transmitter with Hybrid Beamforming 示例中的 Transmit Subarrays 部分。
