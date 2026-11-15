---
type: simulink-block
title: 'Exhaust Gas Temperature (EGT) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Instruments'
documentation_page: 'exhaustgastemperatureegtindicator'
documentation_source_path: 'exhaustgastemperatureegtindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Exhaust Gas Temperature (EGT) Indicator

## 端口

R2025b 中未记录。

## 参数

### **Connection** — 连接到信号 信号名称

连接到要显示的信号，从信号名称列表中选择。

要查看来自信号的数据，请在模型中选择一个信号。该信号会显示在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

该表为连接到模块的信号包含一行。如果模型中没有选择任何信号，或者模块未连接到任何信号，则该表为空。

### **Minimum** — 最小刻度标记值 0（默认） | finite | double | scalar

最小刻度标记值，指定为 finite double 或 scalar value，单位为 ft/min。

#### 依赖关系

**Minimum** 刻度值必须小于 **Minimum** 刻度值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Limits` |
| **类型**：double |
| **值**：double scalar |
| **默认值**：`[0 1000]`，其中 `0` 是最小值 |

### **Maximum** — 最大刻度标记值 1000（默认） | finite | double | scalar

指定最大刻度标记值，指定为 finite double 或 scalar value，单位为 ft/min..

#### 依赖关系

**Maximum** 刻度值必须大于 **Maximum** 刻度值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Limits` |
| **类型**：double |
| **值**：double scalar |
| **默认值**：`[0 1000]`，其中 `1000` 是最大值 |

### **Scale Colors** — 色带范围 0（默认） | double | scalar

刻度外侧色带的范围，指定为 finite double 或 scalar value。指定要在仪表上显示的最小和最大颜色范围。

要添加新颜色，请点击 `+`。要移除颜色，请点击 `-`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScaleColors` |
| **类型**：*n*-by-1 struct array |
| **值**：包含 `Min`、`Max` 和 `Color` 元素的 struct array |

### **Label** — 模块标签位置 `Top`（默认） | `Bottom` | `Hide`

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

此模块在代码生成时会被忽略。

## 版本历史

**在 R2016a 中引入**

## 描述

显示发动机排气温度 (EGT) 的测量值

EGT Indicator 模块以 Celsius 为单位显示发动机排气温度 (EGT) 的温度测量值。

此模块使用以下两种方式显示值：

- 仪表上的指针。主刻度为 (**Maximum**-**Minimum**)/1,000 degrees，次刻度为 (**Maximum**-**Minimum**)/200 degrees Celsius。
- 数字指示器。指示器的工作范围从 **Minimum** 到 **Maximum** degrees Celsius。

如果信号值低于 **Minimum**，则指针显示为 **Minimum** 值以下 5 degrees，数值显示区显示 **Minimum** 值。如果值超过 **Maximum** 值，则指针显示为最大刻度以上 5 degrees，数值显示区显示 **Maximum** 值。

**提示**

为了便于理解和调试模型，你可以在正常模式和加速模式仿真期间修改模型中的仪表模块连接。
