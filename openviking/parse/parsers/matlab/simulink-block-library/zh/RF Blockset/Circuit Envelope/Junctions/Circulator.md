---
type: simulink-block
title: 'Circulator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'circulator'
documentation_source_path: 'ref/circulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Circulator

## 端口

R2025b 中未记录。

## 参数

### **Select component** — 环行器方向 `Circulator clockwise` (default) | `Circulator counter clockwise` | `Tee H-plane (S11=0)` | `Reciprocal phase shifter`

环行器方向，指定为：

- `Circulator clockwise`

  默认选项是 `Circulator clockwise`。
  `Circulator clockwise` 的 S 参数矩阵为：

  [001100010]

  `Circulator counter clockwise`

  `Circulator counter clockwise` 的 S 参数矩阵为：

  [010001100]
- `Tee H-plane (S11=0)`

  `Tee H-plane (S11=0)` 的 S 参数矩阵为：

  (010100001)
- `Reciprocal phase shifter`

  `Reciprocal phase shifter` 的 S 参数矩阵为：

  (0phase120phase120000phase33)(−j2)

### **Reference impedances (Ohm)** — 环行器的参考阻抗 `50` (default) | positive scalar | three-tuple vector

环行器的参考阻抗，指定为正标量或三元组向量。

**注意**

当所有端口的参考阻抗不相等时，Circulator 模块内部的模型会归一化到 50 ohms。

### **Phase shift, ports 1 and 2 (rad)** — 端口 1 和端口 2 中信号相移的角度 `0` (default) | positive scalar

端口 1 和端口 2 中信号相移的角度，指定为以 rad 表示的正标量。

### **Phase shift, ports 3 (rad)** — 端口 3 中信号相移的角度 `0` (default) | positive scalar

端口 3 中信号相移的角度，指定为以 rad 表示的正标量。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `on` (default) | `off`

选择此参数以将负端子接地并隐藏。要显示负端子，请清除此参数。通过显示这些端子，您可以将它们连接到模型的其它部分。

默认情况下，选中此选项。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2014a 中引入**

## 描述

使用 S 参数对理想频率无关环行器建模

使用 Circulator 模块在电路包络环境中对理想无源三端口环行器建模。环行器用于控制 RF 电路内部信号的方向和流动。Circulator 模块可根据参数选择使信号按顺时针或逆时针方向环行。
