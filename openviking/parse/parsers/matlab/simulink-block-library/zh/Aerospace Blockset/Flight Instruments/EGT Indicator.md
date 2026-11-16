---
type: simulink-block
title: 'Exhaust Gas Temperature (EGT) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2023b
official_category: 'Flight Instruments'
documentation_page: 'exhaustgastemperatureegtindicator'
documentation_source_path: 'exhaustgastemperatureegtindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Exhaust Gas Temperature (EGT) Indicator

## 端口

R2025b 中未记录。

## 参数

### **连接** — 连接到信号，信号名称

连接到要显示的信号，从信号名称列表中选择。

要查看来自信号的数据，请在模型中选择一个信号。该信号会出现在 **连接** 表中。选择要显示的信号旁边的选项按钮。单击 **应用** 以连接该信号。

该表中有一行用于连接到模块的信号。如果模型中没有选择任何信号，或者模块未连接到任何信号，则该表为空。

### **最小值** — 最小刻度标记值 0（默认）| 有限 | double | 标量

最小刻度标记值，指定为有限 double 或标量值，单位为 ft/min。

#### 依赖关系

**最小值** 刻度值必须小于 **最大值** 刻度值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Limits` |
| **类型**: double |
| **值**: double scalar |
| **默认值**: `[0 1000]`，其中 `0` 是最小值 |

### **最大值** — 最大刻度标记值 1000（默认）| 有限 | double | 标量

指定最大刻度标记值，指定为有限 double 或标量值，单位为 ft/min。

#### 依赖关系

**最大值** 刻度值必须大于 **最小值** 刻度值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Limits` |
| **类型**: double |
| **值**: double scalar |
| **默认值**: `[0 1000]`，其中 `1000` 是最大值 |

### **刻度颜色** — 色带范围 0（默认）| double | 标量

刻度外侧色带的范围，指定为有限 double 或标量值。指定要在仪表上显示的最小和最大颜色范围。

要添加新颜色，请单击 `+`。要移除颜色，请单击 `-`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ScaleColors` |
| **类型**: *n*-by-1 struct array |
| **值**: 包含元素 `Min`、`Max` 和 `Color` 的 struct array |

### **标签** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签，显示在模块顶部或底部，或隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明文本。

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

显示发动机排气温度 (EGT) 的测量值

EGT Indicator 模块显示发动机排气温度 (EGT) 的温度测量值，单位为 Celsius。

此模块使用以下两种方式显示值：

- 仪表上的指针。主刻度为 (**最大值**-**最小值**)/1,000 degrees，次刻度为 (**最大值**-**最小值**)/200 degrees Celsius。
- 数字指示器。指示器的工作范围从 **最小值** 到 **最大值** degrees Celsius。

如果信号值低于 **最小值**，则指针显示低于 **最小值** 的值 5 degrees，数字显示区显示 **最小值** 的值。如果值超过 **最大值** 的值，则指针显示超过最大刻度 5 degrees，数字显示区显示 **最大值** 的值。

**提示**

为了便于理解和调试模型，您可以在 normal 和 accelerator mode 仿真期间修改模型中的仪表模块连接。
