---
type: simulink-block
title: 'Altimeter'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'altimeter'
documentation_source_path: 'altimeter.html'
language: zh-CN
chinese_source: worker-translation
---

# Altimeter

## 端口

R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 signal name

连接到要显示的信号，从信号名称列表中选择。

要查看来自某个信号的数据，请在模型中选择一个信号。该信号会出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

该表有一行，用于连接到模块的信号。如果模型中没有选择任何信号，或者模块未连接到任何信号，则该表为空。

### **Label** — 模块标签位置 `Top`（默认） | `Bottom` | `Hide`

模块标签，显示在模块的顶部或底部，或隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明性文本。

#### 程序化使用

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

显示飞机高度测量值

Altimeter Indicator 模块以 feet 为单位显示海平面以上的高度，也称为气压高度。该模块使用仪表上的指针和数字指示器显示高度值。

- 仪表有 10 个主刻度。每个主刻度内有五个次刻度。该仪表有三个指针。使用这些指针，高度计只能准确显示 0 到 100,000 feet 之间的高度。

  - 对于最长指针，一个小刻度增量表示 20 feet，主刻度表示 100 feet。
  - 对于第二长指针，次刻度表示 200 feet，主刻度表示 1,000 feet。
  - 对于最短指针，次刻度表示 2,000 feet，主刻度表示 10,000 feet。
- 对于数字显示，该模块以 0 到 9,999 feet 之间的数字字符显示值。当数字显示值达到 10,000 feet 时，仪表将值显示为低于 10,000 feet 的剩余值。例如，12,345 feet 显示为 2,345 feet。当值小于 0（低于海平面）时，该模块显示 `0`。指针会显示适当的值，除非值低于海平面或超过 100,000 feet。低于海平面时，指针设置为 `0`；超过 100,000 时，指针保持在 100,000。

**提示**

为了便于理解和调试模型，您可以在正常模式和加速器模式仿真期间修改模型中的仪表模块连接。
