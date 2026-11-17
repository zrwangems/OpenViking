---
type: simulink-block
title: 'Goto Tag Visibility'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'gototagvisibility'
documentation_source_path: 'slref/gototagvisibility.html'
language: zh-CN
chinese_source: worker-translation
---

# Goto Tag Visibility

## 端口

R2025b 中未记录。

## 参数

### **Goto tag** — 其可见性由该模块位置定义的 Goto 模块标签 `A`（默认）| ...

其可见性由该模块位置定义的 Goto 模块标签。使用指定标签的 From 和 Goto 模块必须位于同一子系统内，或位于模型中 Goto Tag Visibility 模块下方的任意层级，且不得跨越非虚拟子系统边界，即原子子系统、条件执行子系统、函数调用子系统或模型引用的边界。作用域标签名用花括号（`{}`）括起。

#### 提示

如果使用多个 From 和 Goto Tag Visibility 模块引用同一个 Goto 标签，可以同时重命名所有模块中的该标签。使用 Goto 模块对话框中的 **Rename All** 按钮。或者，当您更改 Goto 模块图标上的标签时，按 **Shift+Enter** 将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `GotoTag` |
| **类型：** 字符向量 |
| **值：** `'A'` | `...` |
| **默认：** `'A'` |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

定义 Goto 模块标签的作用域

Goto Tag Visibility 模块定义具有 `scoped` 可见性的 Goto 模块标签的可访问性。您为 **Goto tag** 模块参数指定的值可由包含 Goto Tag Visibility 模块的同一子系统中的 From 模块以及模型层级中位于其下方的子系统中的 From 模块访问。

对于 **Tag Visibility** 参数值为 `scoped` 的 Goto 模块，需要 Goto Tag Visibility 模块。如果标签可见性为 `local` 或 `global`，则不需要 Goto Tag Visibility 模块。该模块显示用花括号（`{}`）括起的标签名。

**注意**

掩码系统中的 `scoped` Goto 模块仅在该子系统及其包含的非虚拟子系统中可见。如果运行或更新框图时，Goto Tag Visibility 模块在框图中所在的层级低于掩码子系统中对应的 `scoped` Goto 模块，Simulink® 将生成错误。

在 Simulink Editor 中，选择 Goto Tag Visibility 模块可高亮显示对应的 Goto 和 From 模块。当对应的 From 或 Goto 模块不在当前框图中时，将高亮显示包含该模块的 Subsystem 模块。

要在打开的框图或新选项卡中显示对应模块，请选择 Goto Tag Visibility 模块并暂停在省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的已打开框图或新选项卡。
