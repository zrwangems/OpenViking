---
type: simulink-block
title: 'Monostable Flip-Flop'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'monostableflipflop'
documentation_source_path: 'ref/monostableflipflop.html'
language: zh-CN
chinese_source: worker-translation
---

# Monostable Flip-Flop

## 端口

### 输入

### **Trigger** — 触发器触发 `0` | `1`

触发器的输入触发信号。

**数据类型：** `Boolean`
### 输出

### **Q** — 触发器输出 `0` | `1`

触发器输出信号。

**数据类型：** `Boolean`

## 参数

### **变化检测** — 触发信号的变化 `Rising edge`（默认）| `Falling edge` | `Either edge`

用于输出脉冲生成的变化检测策略。

### **初始输出** — 触发器初始输出 `0`（默认）| scalar

触发器的初始输出。

### **脉冲持续时间 (s)** — 输出脉冲持续时间 `0.01`（默认）| positive scalar

输出脉冲的持续时间，以 s 为单位。

### **采样时间** — 模块采样时间 `0.001`（默认）| 0 | positive scalar

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于离散时间操作，将采样时间设置为正值。对于连续时间操作，将采样时间设置为 `0`。

如果此模块位于掩码子系统或允许连续和离散操作的其他变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

Raising edge, falling edge, either edge 单稳态触发器

Monostable Flip-Flop（或单稳态多谐振荡器）模块在被外部触发时生成指定持续时间的单个输出脉冲。外部触发是 Boolean 信号。当检测到外部触发信号发生变化时，触发脉冲生成。变化检测可以是：

- Rising edge
- Falling edge
- Either edge

当输出为 true 时，外部触发信号的变化没有影响。

单稳态触发器的操作如下图所示：
