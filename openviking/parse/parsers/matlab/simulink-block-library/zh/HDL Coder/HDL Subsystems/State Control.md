---
type: simulink-block
title: 'State Control'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Subsystems'
documentation_page: 'statecontrol'
documentation_source_path: 'ref/statecontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# State Control

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: State control
  summary: 选择状态控制类型 Synchronous（默认）| Classic
  group: ''
```

### **State control** — 选择状态控制类型 `Synchronous`（默认）| `Classic`

指定使用同步语义还是经典语义。默认值为 `Synchronous`。
## 所属库

HDL Coder / HDL Subsystems

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有单一的默认 HDL 架构。HDL Coder 不会生成特定于 State Control 模块的 HDL 代码。您对 State Control 模块的设置会影响子系统内其他具有状态的模块。

## 版本历史

**在 R2016a 中引入**

## 描述

为具有状态的模块指定同步复位和使能行为

使用 State Control 模块在默认 Simulink® 仿真行为和同步硬件仿真行为之间切换子系统行为。

- 对于默认 Simulink 仿真行为，将 **State control** 设置为 `Classic`。`Classic` 模式下的仿真行为与您在子系统中不使用 State Control 模块时相同。
- 对于同步硬件仿真行为，将 **State control** 设置为 `Synchronous`。`Synchronous` 模式下的 State Control 模块改善了具有状态的模块或具有复位或使能端口的模块的 HDL 仿真行为。当使用该模块的 `Synchronous` 模式时，生成的 HDL 代码使用更少的硬件资源，并且 Simulink 仿真行为与数字硬件的行为更加接近。

请参阅 Synchronous Subsystem Behavior with the State Control Block。
