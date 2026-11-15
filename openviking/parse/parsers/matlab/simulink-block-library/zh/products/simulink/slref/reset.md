---
type: simulink-block
title: 'Reset'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Conditionally Executed Subsystems and Models / Other'
documentation_page: 'reset'
documentation_source_path: 'slref/reset.html'
language: zh-CN
chinese_source: official
---

# Reset

## 端口

R2025b 官方文档未提供。

## 参数

### **重置触发器类型** — 选择触发事件的类型 **电平** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平保持**

选择用于重置子系统模块状态的触发信号的类型。

**电平**
:   当触发信号在当前时间步为非零值或者从上一个时间步的非零值更改为当前时间步的零值时重置模块状态。

**上升沿**
:   当触发信号从零上升到正值或从负值上升到正值时重置模块状态。

**下降沿**
:   当触发信号从正值下降到零或从正值下降到负值时重置模块状态。

**任一沿**
:   当触发信号从零变为非零值或改变符号时重置模块状态。

**电平保持**
:   当触发信号在当前时间步为非零值时重置模块状态。

#### 编程用法

|  |
| --- |
| **模块参数**：`ResetTriggerType` |
| **类型**：字符向量 |
| **值**：`'level'` | `'rising'` | `'falling'` | `'either'` | `'level hold'` |
| **默认值**：`'level'` |

### **传播可变大小信号的大小** — 选择何时传播可变大小信号 **执行期间** (默认) | **仅在启用时**

选择何时传播可变大小信号。

**执行期间**
:   在每个时间步传播可变大小的信号。

**仅在重置时**
:   当重置包含 Reset 端口模块的 Subsystem 模块时，传播可变大小的信号。如果您选择此选项，采样时间必须为周期性采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`PropagateVarSize` |
| **类型：**字符向量 |
| **值：**`'During execution'` | `'Only when resetting'` |
| **默认值：**`'During execution'` |

### **启用过零检测** — 控制过零检测 on (默认) | off

控制过零检测。

on
:   检测过零点。

off
:   不检测过零点。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

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

**在 R2015a 中推出**

### R2025a: 支持封装工作区和模型工作区中的变体控制项变量

您可以在封装工作区和模型工作区中定义变体控制项变量以控制 Reset Function 模块中的活动变体，前提是**生成预处理器条件句**参数为 `off`。

## 描述

可重置子系统的控制模块

Subsystem 模块根级上放置的 Reset 模块向模块添加一个控制端口。当连接到该端口的信号发生触发重置的事件时，子系统的模块状态将重置为其初始条件。请参阅Resettable Subsystem。
