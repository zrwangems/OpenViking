---
type: simulink-block
title: 'International Geomagnetic Reference Field'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'internationalgeomagneticreferencefield'
documentation_source_path: 'internationalgeomagneticreferencefield.html'
language: zh-CN
chinese_source: worker-translation
---

# International Geomagnetic Reference Field

## 端口

### 输入

### **h** — 高度标量

高度，指定为标量，采用所选单位。

**数据类型：** `double`

### **μ (deg)** — 纬度标量

纬度，指定为以 degrees 为单位的标量。此模块接受大于 90 且小于 -90 的纬度值。

**数据类型：** `double`

### **l (deg)** — 经度标量

经度，指定为以 degrees 为单位的标量。此模块接受大于 180 且小于 -180 的范围。

**数据类型：** `double`

### **dyear** — 期望年份标量

期望年份，采用十进制格式，以包含当年已经过去的任何部分。该值为当前年份加上当年已经过去的天数除以 365。要计算 2015 年 3 月 21 日的十进制年份 `dyear`：

```
dyear=decyear('21-March-2015','dd-mmm-yyyy')
```

#### 依赖关系

要启用此端口，请选择 **输入十进制年份**。

**数据类型：** `double`

### 输出

### **XYZ** — 磁场矢量

磁场，以矢量形式返回，采用所选单位。此矢量的分量位于北-东-地 (NED) 参考坐标系中。

**数据类型：** `double`

### **H** — 水平强度标量

水平强度，以标量形式返回，采用所选单位。

**数据类型：** `double`

### **D** — 磁偏角标量

磁偏角，以标量形式返回，以 degrees 为单位。

**数据类型：** `double`

### **l** — 磁倾角标量

磁倾角，以标量形式返回，以 degrees 为单位。

**数据类型：** `double`

### **F** — 总强度标量

总强度，以标量形式返回，采用所选单位。

**数据类型：** `double`

### **DXDYDZ** — 磁场长期变化矢量

磁场的长期变化，以矢量形式返回，采用所选单位 per year。

#### 依赖关系

要启用此端口，请选择 **输出长期变化**。

**数据类型：** `double`

### **DH** — 水平强度长期变化标量

水平强度的长期变化，以标量形式返回，采用所选单位 per year。

#### 依赖关系

要启用此端口，请选择 **输出长期变化**。

**数据类型：** `double`

### **DD** — 磁偏角长期变化标量

磁偏角的长期变化，以标量形式返回，以 minutes per year 为单位。

#### 依赖关系

要启用此端口，请选择 **输出长期变化**。

**数据类型：** `double`

### **DI** — 磁倾角长期变化标量

磁倾角的长期变化，以标量形式返回，以 minutes per year 为单位。

#### 依赖关系

要启用此端口，请选择 **输出长期变化**。

**数据类型：** `double`

### **DF** — 总强度长期变化标量

总强度的长期变化，以标量形式返回，采用所选单位 per year。

#### 依赖关系

要启用此端口，请选择 **输出长期变化**。

**数据类型：** `double`

## 参数

### **代次** — 国际地磁参考场代次 `IGRF-14` (默认) | `IGRF-13` | `IGRF-11` | `IGRF-12`

国际地磁参考场代次，从 `IGRF-14`、`IGRF-13`、`IGRF-12` 或 `IGRF-11` 中选择。

#### 程序化使用

|  |
| --- |
| **模块参数：** `generation` |
| **类型：** character vector |
| **值：** `'IGRF-14'` | `'IGRF-13'` | `'IGRF-12'` | `'IGRF-11'` | |
| **默认值：** `'IGRF-14'` |

**数据类型：** `char` | `string`

### **单位** — 单位 `Metric (MKS)` (默认) | `English`

参数和输出单位，指定为：

| 单位 | 高度 |
| --- | --- |
| `Metric (MKS)` | Meters |
| `English` | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `'Metric (MKS)'` | `'English'` |
| **默认值：** `'Metric (MKS)'` |

### **输入十进制年份** — 期望年份 `on` (默认) | `off`

- 要使用输入端口指定十进制年份，请选中此复选框。
- 要使用 **月份**、**日** 和 **年份** 的值指定十进制年份，请清除此复选框。

#### 依赖关系

要启用 **月份**、**日** 和 **年份**，请清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `time_in` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **月份** — 输入月份 `January` (默认) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算十进制年份的月份。

#### 依赖关系

要启用此参数，请清除 **输入十进制年份**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `month` |
| **类型：** character vector |
| **值：** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值：** `'January'` |

### **日** — 输入日 1 (默认) | `1` 到 `31`

用于计算十进制年份的日。

#### 依赖关系

要启用此参数，请清除 **输入十进制年份**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `day` |
| **类型：** character vector |
| **值：** `'1'` 到 `'31'` |
| **默认值：** `'1'` |

### **年份** — 输入年份 `2025` (默认) | `1900` 到 `2030`

用于计算十进制年份的年份，指定为 `1900` 到 `2030`。

#### 依赖关系

要启用此参数，请清除 **输入十进制年份**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `year` |
| **类型：** character vector |
| **值：** 任意年份 |
| **默认值：** `'2025'` |

### **输入超出范围时的操作** — 超出范围的模块行为 `None` (默认) | `Warning` | `Error`

超出范围的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` (默认) | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

### **输出长期变化** — 长期变化 `on` (默认) | `off`

选中此复选框可启用长期变化（年变化率）以及非长期变化量的输出。否则，清除此复选框。

| 长期变化 | 描述 |
| --- | --- |
| 磁场 | 磁场矢量，以 nanotesla (nT) 为单位。*Z* 是垂直分量（向下为正） |
| 水平强度 | 水平强度，以 nanotesla (nT) 为单位 |
| 磁偏角 | 磁偏角，以 degrees 为单位（向东为正） |
| 磁倾角 | 磁倾角，以 degrees 为单位（向下为正） |
| 总强度 | 总强度，以 nanotesla (nT) 为单位 |
| SV 磁场 | 磁场的长期变化 |
| SV 水平强度 | 水平强度的长期变化 |
| SV 磁偏角 | 磁偏角的长期变化，即真北与磁场矢量之间的角度（向东为正） |
| SV 磁倾角 | 磁倾角的长期变化，即水平面与磁场矢量之间的角度（向下为正） |
| SV 总强度 | 总强度的长期变化 |

清除此复选框以仅启用非长期变化量：

- 磁场
- 水平强度
- 磁偏角
- 磁倾角
- 总强度

#### 程序化使用

|  |
| --- |
| **模块参数：** `sv_out` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：International Geomagnetic Reference Field 模块现在支持国际地磁参考场第 14 代 (IGRF-14)

International Geomagnetic Reference Field 模块现在支持国际地磁参考场第 14 代 (IGRF-14)。

## 描述

使用 International Geomagnetic Reference Field 计算地球磁场和长期变化

International Geomagnetic Reference Field 模块使用选定的 International Geomagnetic Reference Field 代次计算地球磁场和长期变化。它使用选定的 International Geomagnetic Reference Field 代次计算某一位置和时间处的地球磁场和长期变化。
