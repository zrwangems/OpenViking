---
type: simulink-block
title: 'Action Port'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Conditionally Executed Subsystems and Models / Other'
documentation_page: 'actionport'
documentation_source_path: 'slref/actionport.html'
language: zh-CN
chinese_source: official
---

# Action Port

## 端口

R2025b 官方文档未提供。

## 参数

### **恢复执行时的状态** — 选择内部状态的处理 **保持** (默认) | **重置**

选择当重新启用包含 Action Port 模块的子系统时如何处理内部状态。

**保持**
:   当子系统重新启用时，保留该子系统的以前状态值。各调用之间的以前状态值会保留，即使调用连接到 If 或 Switch Case 模块的其他子系统模块也是如此。

**重置**
:   当子系统重新启用时，重新初始化状态值。

    如果子系统的动作端口的逻辑表达式之前的计算结果为 false，然后计算结果变为 true，则该子系统会重新启用。在下面的示例中，`A` 和 `B` 两个执行子系统的 Action Port 模块的**恢复执行时的状态**参数都设置为**重置**。

    当 **case[1]** 为 `true` 时，执行子系统 **A**。当 **case [1]** 保持为 `true` 时，重复调用子系统 **A** 不会重置其状态值。相同的行为也适用于子系统 **B**。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitializeStates` |
| **类型**：字符向量 |
| **值**：`'held'` | `'reset'` |
| **默认值**：`'held'` |

### **传播可变大小信号的大小** — 选择何时传播可变大小信号 **仅当恢复执行时** (默认) | **执行期间**

选择何时传播可变大小信号。

**仅当恢复执行时**
:   仅当重新启用包含 Action Port 模块的子系统时，才传播可变大小信号。

**执行期间**
:   在每个时间步传播可变大小的信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`PropagateVarSize` |
| **类型**：字符向量 |
| **值**：`'Only when execution is resumed'` | `'During execution'` |
| **默认值**：`'Only when execution is resumed'` |

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

## 版本历史

**在 R2006a 之前推出**

## 描述

If Action Subsystem 或 Switch Case Action Subsystem 模块的动作信号的控制端口

The Action Port 模块控制下列子系统模块的执行：

- 连接到 If 模块的 If Action Subsystem 模块。
- 连接到 Switch Case 模块的 Switch Case Action Subsystem 模块。
- Stateflow® 图中基于 Simulink 的状态。请参阅Create and Edit Simulink Based States (Stateflow)。
