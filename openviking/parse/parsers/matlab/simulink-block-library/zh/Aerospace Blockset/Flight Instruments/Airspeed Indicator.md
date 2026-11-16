---
type: simulink-block
title: 'Airspeed Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'airspeedindicator'
documentation_source_path: 'airspeedindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Airspeed Indicator

## 端口

在 R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 信号名称

连接到要显示的信号，从信号名称列表中选择。

要查看来自信号的数据，请在模型中选择一个信号。该信号将显示在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 连接该信号。

该表为连接到模块的信号提供一行。如果模型中未选择任何信号，或者模块未连接到任何信号，则该表为空。

### **Minimum** — 最小刻度值 40（默认） | 有限 | double | 标量

最小刻度值，指定为以 knots 为单位的有限 double 标量值。

#### 依赖关系

**Minimum** 刻度值必须小于 **Maximum** 刻度值。

#### 编程用法

|  |
| --- |
| **模块参数**: `Limits` |
| **类型**: double |
| **值**: 向量 |
| **默认值**: `[40 400]`，其中 `40` 是最小值 |

### **Maximum** — 最大刻度值 400（默认） | 有限 | double | 标量

指定最大刻度值，指定为以 knots 为单位的有限 double 标量值。

#### 依赖关系

**Maximum** 刻度值必须大于 **Minimum** 刻度值。

#### 编程用法

|  |
| --- |
| **模块参数**: `Limits` |
| **类型**: double |
| **值**: 向量 |
| **默认值**: `[40 400]`，其中 `400` 是最大值 |

### **Scale Colors** — 色带范围 0（默认） | double | 标量

超出刻度的色带范围，指定为有限 double 标量值。指定要在仪表上显示的颜色范围的最小值和最大值。

要添加新颜色，点击 `+`。要删除颜色，点击 `-`。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScaleColors` |
| **类型**: *n*-by-1 struct array |
| **值**: 包含元素 `Min`、`Max` 和 `Color` 的 struct array |

### **Label** — 已连接信号的名称 `Top`（默认） | `Bottom` | `Hide`

已连接信号的名称。

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

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块在代码生成时被忽略。

## 版本历史

**在 R2016a 中引入**

## 描述

显示飞机空速的测量值

Airspeed Indicator 模块显示以 knots 为单位的飞机空速测量值。

默认情况下，次刻度表示 10-knot 增量，主刻度表示 40-knot 增量。参数 **Minimum** 和 **Maximum** 确定仪表上的最小值和最大值。刻度的数量和分布是固定的，这意味着第一个和最后一个刻度显示最小值和最大值。中间的刻度在最小值和最大值之间均匀分布。对于主刻度，刻度的分布为 (**Maximum**-**Minimum**)/9。对于次刻度，刻度的分布为 (**Maximum**-**Minimum**)/36。

空速指示器具有刻度色条，允许第一个色条重叠，并显示在不同的半径处。此不同半径使该模块能够针对飞机空速和失速速度准确地表示襟翼放出时的最大速度 (VFE) 和襟翼放出时的失速速度 (VSO)。

**提示**

为了便于理解和调试模型，您可以在普通模式和加速模式仿真期间修改模型中的仪表模块连接。
