---
type: simulink-block
title: 'Revolutions Per Minute (RPM) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2023b
official_category: 'Flight Instruments'
documentation_page: 'revolutionsperminuterpmindicator'
documentation_source_path: 'revolutionsperminuterpmindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Revolutions Per Minute (RPM) Indicator

## 端口

R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 信号名称

连接到要显示的信号，从信号名称列表中选择。

要查看信号中的数据，请在模型中选择一个信号。该信号会显示在 **Connection** 表中。选择要显示的信号旁边的选项按钮。单击 **Apply** 以连接该信号。

该表为连接到模块的信号保留一行。如果模型中没有选择任何信号，或者模块未连接到任何信号，则该表为空。

### **Scale Colors** — 色带范围 0（默认）| double | scalar

刻度外侧色带的范围，指定为有限 double 或标量值。指定要在仪表上显示的最小和最大颜色范围。

要添加新颜色，请单击 `+`。要删除颜色，请单击 `-`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScaleColors` |
| **类型**：*n*-by-1 struct array |
| **值**：包含元素 `Min`、`Max` 和 `Color` 的 struct array |

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签，显示在模块顶部或底部，或者隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明性文本。

#### 编程用法

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

此模块在代码生成时将被忽略。

## 版本历史

**在 R2016a 中引入**

## 描述

以 RPM 百分比显示发动机每分钟转数（RPM）的测量值

RPM Indicator 模块以 RPM 百分比显示发动机每分钟转数的测量值。

RPM 的值范围从 0 到 110 %。小刻度表示 5 % RPM 的增量，大刻度表示 10 % RPM 的增量。

**提示**

为了便于理解和调试您的模型，您可以在正常模式和加速器模式仿真期间修改模型中的仪表模块连接。
