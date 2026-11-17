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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Select component
  summary: 环行器方向 Circulator clockwise（默认）| Circulator counter clockwise | Tee H-plane (S11=0) | Reciprocal phase shifter
  group: ''
- name: Reference impedances (Ohm)
  summary: 环行器的参考阻抗 50（默认）| 正标量 | 三元组向量
  group: ''
- name: Phase shift, ports 1 and 2 (rad)
  summary: 端口 1 和端口 2 中信号的相位偏移角度 0（默认）| 正标量
  group: ''
- name: Phase shift, ports 3 (rad)
  summary: 端口 3 中信号的相位偏移角度 0（默认）| 正标量
  group: ''
- name: Ground and hide negative terminals
  summary: 将 RF 电路端子接地 on（默认）| off
  group: ''
```

### **Select component** — 环行器方向 `Circulator clockwise`（默认）| `Circulator counter clockwise` | `Tee H-plane (S11=0)` | `Reciprocal phase shifter`

环行器方向，指定为：

- `Circulator clockwise`

  默认选项为 `Circulator clockwise`。
  `Circulator clockwise` 的 s 参数矩阵为：

  [001100010]

  `Circulator counter clockwise`

  `Circulator counter clockwise` 的 s 参数矩阵为：

  [010001100]
- `Tee H-plane (S11=0)`

  `Tee H-plane (S11=0)` 的 s 参数矩阵为：

  (010100001)
- `Reciprocal phase shifter`

  `Reciprocal phase shifter` 的 s 参数矩阵为：

  (0phase120phase120000phase33)(−j2)

### **Reference impedances (Ohm)** — 环行器的参考阻抗 `50`（默认）| 正标量 | 三元组向量

环行器的参考阻抗，指定为正标量或三元组向量。

**注意**

当所有端口的参考阻抗不相等时，Circulator 模块内部的模型会归一化到 50 欧姆。

### **Phase shift, ports 1 and 2 (rad)** — 端口 1 和端口 2 中信号的相位偏移角度 `0`（默认）| 正标量

端口 1 和端口 2 中信号的相位偏移角度，以弧度为单位指定为正标量。

### **Phase shift, ports 3 (rad)** — 端口 3 中信号的相位偏移角度 `0`（默认）| 正标量

端口 3 中信号的相位偏移角度，以弧度为单位指定为正标量。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `on`（默认）| `off`

选择此参数可将负极端子接地并隐藏。
要暴露负极端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其它部分。

默认情况下，此选项处于选中状态。
## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

使用 S 参数对理想频率无关环行器进行建模

使用 Circulator 模块在电路包络环境中对理想无源三端口环行器进行建模。环行器用于控制 RF 电路内部的信号方向和流动。根据参数选择，Circulator 模块可以使信号沿顺时针或逆时针方向环行。
