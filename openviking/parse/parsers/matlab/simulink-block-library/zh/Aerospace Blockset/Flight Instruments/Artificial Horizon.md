---
type: simulink-block
title: 'Artificial Horizon'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'artificialhorizon'
documentation_source_path: 'artificialhorizon.html'
language: zh-CN
chinese_source: worker-translation
---

# Artificial Horizon

## 端口

R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 信号名称 | 二元素信号

连接到用于显示的二元素信号，从信号名称列表中选择。该二元素信号由横滚和俯仰在 Mux 模块中组合而成，单位为度。您连接并显示该组合信号。此输入不能是总线信号。

要查看来自信号的数据，请在模型中选择一个信号。该信号会出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

该表中有一行用于连接到该模块的信号。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则该表为空。

要查看来自信号的数据，请在模型中选择一个信号。该信号会出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

该表中有一行用于连接到该模块的信号。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则该表为空。

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签，显示在模块顶部或底部，或隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明文本。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |

## 所属库

Aerospace Blockset / Flight Instruments

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

表示飞机相对于地平线的姿态

Artificial Horizon 模块表示飞机相对于地平线的姿态，并以度为单位显示横滚和俯仰：

- 横滚值不能超过 +/– 90 度。
- 俯仰值不能超过 +/– 30 度。

如果值超过最大值，仪表的显示最大值和最小值不会改变。

横滚值的变化会相应地影响仪表半圆以及位于黑色弧线上的刻度。俯仰值的变化会影响刻度和半圆的分布。

在 Mux 模块中按以下顺序组合横滚和俯仰信号：

1. 横滚
2. 俯仰

**提示**

为了便于理解和调试您的模型，您可以在正常和加速模式仿真期间修改模型中的仪表模块连接。
