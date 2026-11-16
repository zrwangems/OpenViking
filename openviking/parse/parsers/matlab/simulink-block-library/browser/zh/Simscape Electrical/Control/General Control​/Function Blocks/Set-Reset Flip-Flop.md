---
type: simulink-block
title: 'Set-Reset Flip-Flop'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'setresetflipflop'
documentation_source_path: 'ref/setresetflipflop.html'
language: zh-CN
chinese_source: worker-translation
---

# Set-Reset Flip-Flop

## 端口

### 输入

### **Set** — 置位输入信号 `0` | `1`

触发状态变化的输入信号。

**数据类型：** `Boolean`

### **Reset** — 复位输入信号 `0` | `1`

复位状态变化的输入信号。

**数据类型：** `Boolean`
### 输出

### **Q** — 输出信号 `0` | `1`

输出信号 **Q**，其维度和数据类型与输入**信号**相同。

**数据类型：** `Boolean`

### **!Q** — 互补输出信号 `0` | `1`

输出信号 **!Q**，其维度和数据类型与输入**信号**相同。

**数据类型：** `Boolean`

## 参数

### **未定义状态时的优先级** — 状态优先级 `Set` (default) | `Reset`

未定义状态的优先级，即当 *Set* 和 *Reset* 均为 `true` 时。

### **Q 状态的初始条件** — 输出 Q 的初始值 `0` (default) | `1`

*Q* 状态的初始条件。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1` (default) | `0` | 正标量

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

置位-复位触发器或双稳态多谐振荡器

Set-Reset Flip-Flop 模块实现置位-复位触发器或双稳态多谐振荡器。

除非施加外部触发，否则模块保持输出信号 Q 和 !Q。外部触发（*Set*）会产生状态变化，该状态变化将一直保持，直到施加第二个外部触发（*Reset*）。

下表显示了模块输入信号和输出信号之间的关系。

| Set | Reset | Q | !Q |
| --- | --- | --- | --- |
| 0 | 0 | 上一个 Q | 上一个 !Q |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 未定义 | 未定义 |

当状态未定义时，优先级作为外部参数提供。
