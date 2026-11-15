---
type: simulink-block
title: 'Revolutions Per Minute (RPM) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Instruments'
documentation_page: 'revolutionsperminuterpmindicator'
documentation_source_path: 'revolutionsperminuterpmindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Revolutions Per Minute (RPM) Indicator

## 端口

R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 signal name

连接到要显示的信号，从信号名称列表中选择。

要查看来自某个信号的数据，请在模型中选择一个信号。该信号会出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **应用** 以连接该信号。

该表为连接到该模块的信号保留一行。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则该表为空。

### **Scale Colors** — 色带范围 0 (default) | double | scalar

标尺外侧色带的范围，指定为有限 double 或 scalar 值。指定要在仪表上显示的最小和最大颜色范围。

要添加新颜色，请点击 `+`。要移除颜色，请点击 `-`。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScaleColors` |
| **类型**: *n*-by-1 struct array |
| **值**: 包含 `Min`、`Max` 和 `Color` 元素的 struct array |

### **Label** — 模块标签位置 `Top` (default) | `Bottom` | `Hide`

模块标签，显示在模块顶部或底部，或隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明文本。

#### 编程用法

|  |
| --- |
| **模块参数**: `LabelPosition` |
| **类型**: character vector |
| **值**: `'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**: `'Top'` |

## 所属库

Aerospace Blockset / Flight Instruments

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块在代码生成时被忽略。

## 版本历史

**在 R2016a 中引入**

## 描述

显示发动机每分钟转数 (RPM) 的测量值，以 RPM 百分比表示

RPM Indicator 模块显示发动机每分钟转数的测量值，以 RPM 百分比表示。

RPM 值的范围为 0 到 110 %。次刻度表示 5 % RPM 的增量，主刻度表示 10 % RPM 的增量。

**提示**

为了便于理解和调试模型，您可以在正常和加速器模式仿真期间修改模型中的仪表模块连接。
