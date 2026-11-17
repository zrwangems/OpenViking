---
type: simulink-block
title: 'Unidirectional Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'unidirectionalclutch'
documentation_source_path: 'ref/unidirectionalclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Unidirectional Clutch

## 端口

### 守恒端口

### **H** — 轮毂速度 机械旋转

轮毂驱动轴轴线的速度。

### **R** — 齿圈速度 机械旋转

齿圈驱动轴轴线的速度。

## 参数

### **Transmission direction** — 相对旋转方向 `From hub to ring for positive rotation`（默认）| `From hub to ring for negative rotation`

离合器锁止并传递扭矩时所对应的相对旋转方向。

### **Initial state** — 离合器初始状态 `Unlocked`（默认）| `Locked`

仿真开始时离合器的状态。离合器可以处于两种状态之一：锁止和解锁。锁止的离合器约束基轴和从动轴以相同速度旋转，即作为一个整体旋转。解锁的离合器允许两根轴以不同速度旋转，从而导致离合器片之间打滑。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

沿单一方向传递动力的离合器

Unidirectional Clutch 模块基于耦合的齿圈-轮毂对理想单向离合器进行建模。当轮毂和齿圈的相对速度变为正值或负值时，它会传递扭矩，具体取决于您如何设置传动方向。有关模型详细信息，请参见方程。

### 方程

该图显示了单向离合器的几何结构。该表汇总了单向离合器变量。

如果锁止，离合器将扭矩从轮毂传递到齿圈。如果解锁，离合器不传递扭矩。离合器不存在解锁但接合（传递扭矩）的状态。相对角速度（滑差）*ω* 是轮毂角速度 *ωH* 相对于齿圈速度 *ωR* 的值，即 *ω*=*ωH* – *ωR*。

Unidirectional Clutch 模块实现单向离合器的理想模型，不包含任何内部动力学，例如滚子和弹簧。

**锁止条件**

传动方向决定锁止条件。

- 如果您选择正方向传动，则当 *ω* = *ω*H – *ω*R ≥ 0 且从正值变为零时，离合器锁止。滑差 *ω* 随后保持为零，并且离合器传递扭矩。

  如果传动系统动力学随后在仿真中导致 *ω* < 0，则离合器会突然解锁并停止传递扭矩。
- 如果您选择负方向传动，则当 *ω* = *ω*H – *ω*R ≤ 0 且从负值变为零时，离合器锁止。滑差 *ω* 随后保持为零，并且离合器传递扭矩。

  如果传动系统动力学随后在仿真中导致 *ω* > 0，则离合器会突然解锁并停止传递扭矩。

例如，正方向下的锁止和扭矩传递如下。

- 当轮毂比齿圈旋转得更快（*ω* > 0）时，轮毂和齿圈之间预先设置的小间隙被消除。弹簧加载的滚子楔入轮毂和齿圈之间，使两者接触、锁止并一起旋转；*ω* 重置为零。（图中的旋转约定为顺时针。）
- 如果齿圈比轮毂旋转得更快（*ω* < 0），则滚子被推离接触，离合器解锁。

有关离合器示意图，请参见方程。

**离合器耗散的功率**

单向离合器是理想的，不耗散功率。离合器要么解锁并且不施加动摩擦力，要么锁止（无滑差）并且仅施加静摩擦力。
