---
type: simulink-block
title: 'State Control'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Hierarchical Designs and Synchronous Hardware Behavior'
documentation_page: 'statecontrol'
documentation_source_path: 'ref/statecontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# State Control

## 端口

在 R2025b 中未记录。

## 参数

### **状态控制** — 选择状态控制类型 `Synchronous`（默认） | `Classic`

指定使用同步语义还是经典语义。默认值为
`Synchronous`。

## 所属库

HDL Coder / HDL Subsystems

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成
使用 HDL Coder™ 生成 VHDL、Verilog 和 SystemVerilog 代码，用于 FPGA 和 ASIC 设计。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块具有单一默认 HDL 架构。HDL Coder 不会生成特定于 State Control 模块的 HDL 代码。State Control 模块的设置方式会影响子系统内其他具有状态的模块。

## 版本历史

**在 R2016a 中引入**

## 描述

为具有状态的模块指定同步复位和使能行为

使用 State Control 模块可在默认 Simulink® 仿真行为与同步硬件仿真行为之间切换子系统行为。

- 对于默认 Simulink 仿真行为，将 **状态控制** 设置为 `Classic`。在 `Classic` 模式下的仿真行为与在子系统内不使用 State Control 模块时相同。
- 对于同步硬件仿真行为，将 **状态控制** 设置为 `Synchronous`。处于 `Synchronous` 模式的 State Control 模块可改善具有状态的模块或者具有复位或使能端口的模块的 HDL 仿真行为。使用该模块的 `Synchronous` 模式时，生成的 HDL 代码使用更少的硬件资源，并且 Simulink 仿真行为与数字硬件的行为紧密匹配。

请参阅使用 State Control 模块的同步子系统行为。
