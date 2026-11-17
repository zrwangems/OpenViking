---
type: simulink-block
title: 'Variable Phase Shift'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variablephaseshift'
documentation_source_path: 'ref/variablephaseshift.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Phase Shift

## 端口
```yaml
ports:
- name: Phase
  summary: Simulink 控制信号标量
  direction: input
  data_types: double
```

### 输入

### **Phase** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Phase shift unit
  summary: 用于控制电路相位的角度单位 rad（默认）| deg
  group: ''
- name: Reference impedances (Ohm)
  summary: 移相器的参考阻抗 50（默认）| 实正标量向量 | 实标量
  group: ''
- name: Ground and hide negative terminals
  summary: 将 RF 电路端子接地 on（默认）| off
  group: ''
```

### **Phase shift unit** — 用于控制电路相位的角度单位 `rad`（默认）| `deg`

用于控制信号相位的角度单位，指定为 `rad` 表示弧度或 `deg` 表示度。

### **Reference impedances (Ohm)** — 移相器的参考阻抗 `50`（默认）| 实正标量向量 | 实标量

移相器的参考阻抗，指定为以欧姆为单位的标量或正标量向量。

**注意**

对于非 50 欧姆的参考阻抗，Phase Shift 模块内部的模型会归一化到 50 欧姆。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 on（默认）| off

选择此参数可将负极端子接地并隐藏。要暴露负极端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其它部分。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

### R2021b：Variable Phase Shift 模块图标已更新

从 R2021b 开始，Variable Phase Shift 模块图标已更新。当您打开在 R2021b 之前创建的包含 Variable Phase Shift 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对可变相位设备进行建模

Variable Phase Shift 模块控制 RF Blockset™ 电路输出信号的相位。该模块使用 Simulink® 信号来控制电路的相位。一个输入端子用于 Simulink 控制信号，一个输入端子用于 RF Blockset 信号。

移相器通常用于相控阵天线系统。在这些系统中，电子控制的移相器在空间中对天线波束进行转向。移相器也用于测试和测量系统。
