---
type: simulink-block
title: 'World Magnetic Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'worldmagneticmodel'
documentation_source_path: 'worldmagneticmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# World Magnetic Model

## 端口

### 输入

### **h** — 椭球高度标量

WGS84 椭球上方的椭球高度，指定为标量，单位为所选单位。

**数据类型：** `double`

### **μ (deg)** — 纬度标量

纬度，指定为标量，单位为度。如果纬度超出范围，当 **Action for out-of-range** 输入设置为 `None` 或 `Warning` 时，模块会将其环绕到范围内。当 **Action for out-of-range** 设置为 `Error` 时，不会环绕。

**数据类型：** `double`

### **l (deg)** — 经度标量

经度，指定为标量，单位为度。如果经度超出范围，当 **Action for out-of-range** 输入设置为 `None` 或 `Warning` 时，模块会将其环绕到范围内。当 **Action for out-of-range** 设置为 `Error` 时，不会环绕。

**数据类型：** `double`

### **Decimal Year** — 期望年份标量

以十进制格式表示的期望年份，包含当年已过去的部分。该值为当前年份加上当年已过去的天数除以 365。

例如，要计算 2015 年 3 月 21 日的十进制年份 `dyear`：

```
dyear=decyear('21-March-2015','dd-mmm-yyyy')
```

```
dyear =
   2.0152e+03
```

**数据类型：** `double`
### 输出

### **Magnetic Field (nT)** — 磁场矢量

磁场，以矢量形式返回，单位为所选单位。磁场在 NED 坐标系中定义。

**数据类型：** `double`

### **Horizontal Intensity (nT)** — 水平强度标量

水平强度，以标量形式返回，单位为指定单位。

**数据类型：** `double`

### **Declination (deg)** — 磁偏角标量

磁偏角，以标量形式返回，单位为度。

**数据类型：** `double`

### **Inclination (deg)** — 磁倾角标量

磁倾角，以标量形式返回，单位为度。

**数据类型：** `double`

### **Total Intensity (nT)** — 总强度标量

总强度，以标量形式返回，单位为所选单位。

**数据类型：** `double`

## 参数

### **WMM coefficients** — World Magnetic Model 系数文件 `WMM2025 (2025-2030)`（默认）| `WMM2020 (2020-2025)` | `WMM2015 V2 (2015-2020)` | `WMM2000 (2000-2005)` | `WMM2005 (2005-2010)` | `WMM2010 (2010-2015)` | `WMM2015 V1 (2015-2020)` | `Custom`

World Magnetic Model 系数文件，从列表中选择。

- `WMM2000 (2000-2005)` — World Magnetic Model 2000 系数文件
- `WMM2005 (2005-2010)` — World Magnetic Model 2005 系数文件
- `WMM2010 (2010-2015)` — World Magnetic Model 2010 系数文件
- `WMM2015 V1 (2015-2020)` — World Magnetic Model 2015（v1）系数文件
- `WMM2015 V2 (2015-2020)` — World Magnetic Model 2015（v2）系数文件
- `WMM2020 (2020-2025)` — World Magnetic Model 2020 系数文件
- `WMM2025 (2025-2030)` — World Magnetic Model 2025 系数文件
- `Custom` — 指定您自己的 World Magnetic Model 系数文件。您可以从 The World Magnetic Model 下载 World Magnetic Model 系数文件。

#### 依赖

选择 `Custom` 会启用 **Custom .COF file** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `model` |
| **类型：** 字符向量 |
| **值：** `'WMM2025 (2025-2030)'` `'WMM2020 (2020-2025)'` | `'WMM2015 V2 (2015-2020)'` | `'WMM2000 (2000-2005)'` | `'WMM2005 (2005-2010)'` | `'WMM2010 (2010-2015)'` | `'WMM2015 V1 (2015-2020)'` | `'Custom'` |
| **默认值：** `'WMM2025 (2025-2030)'` |

### **Custom .COF file** — 自定义 World Magnetic Model 系数文件 `'WMM2025COF'`（默认）| 任意系数文件名

从 The World Magnetic Model 下载的 World Magnetic Model 系数文件。例如，如果您想下载尚未列在 **WMM coefficients** 列表中的系数文件。

#### 依赖

要启用此参数，请为 **WMM coefficients** 参数选择 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：** `customFile` |
| **类型：** 字符向量 |
| **值：** `'WMM2025.COF'` | 任意系数文件名 |
| **默认值：** `'WMM2025.COF'` |

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English`

输入和输出单位：

| 单位 | 高度 | 磁场 | 水平强度 | 总强度 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | 米 | 纳特斯拉 | 纳特斯拉 | 纳特斯拉 |
| `English` | 英尺 | 纳高斯 | 纳高斯 | 纳高斯 |

#### 编程用法

|  |
| --- |
| **模块参数：** `units` |
| **类型：** 字符向量 |
| **值：** `'Metric (MKS)'` | `'English'` |
| **默认值：** `'Metric (MKS)'` |

### **Input decimal year** — 输入十进制年份 开（默认）| 关

- 要通过 World Magnetic Model 2015 模块的输入端口指定十进制年份，请选中此复选框
- 要使用 **Month**、**Day** 和 **Year** 的值指定十进制年份，请清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `time_in` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Month** — 输入月份 `January`（默认）| `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算十进制年份的月份。

#### 依赖

要启用此参数，请选择 **Input decimal year**。

#### 编程用法

|  |
| --- |
| **模块参数：** `month` |
| **类型：** 字符向量 |
| **值：** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值：** `'January'` |

### **Day** — 输入日期 1（默认）| `1` 到 `31`

用于计算十进制年份的日期。

#### 依赖

要启用此参数，请选择 **Input decimal year**。

#### 编程用法

|  |
| --- |
| **模块参数：** `day` |
| **类型：** 字符向量 |
| **值：** `'1'` 到 `'31'` |
| **默认值：** `'1'` |

### **Year** — 输入年份 2025（默认）| 任意年份

用于计算十进制年份的年份。

#### 依赖

要启用此参数，请选择 **Input decimal year**。

#### 编程用法

|  |
| --- |
| **模块参数：** `year` |
| **类型：** 字符向量 |
| **值：** 任意年份 |
| **默认值：** `'2025'` |

### **Action for out-of-range input** — 超出范围操作 `Error`（默认）| `Warning` | `None`

超出范围的模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 诊断查看器中显示错误，模型仿真停止。 |

如果经度或纬度超出范围，当 **Action for out-of-range** 输入设置为 `None` 或 `Warning` 时，模块会将其环绕到范围内。当 **Action for out-of-range** 设置为 `Error` 时，不会环绕。

当 **Action for out-of-range** 设置为 `None` 或 `Warning` 时，World Magnetic Model 模块接受超出范围的高度输入（小于 -1000 m 或大于 850000 m）。但是，对于这些值，模块输出可能不准确或不可靠。World Magnetic Model 仅在 -1000 m 到 850000 m 之间有效。

#### 编程用法

|  |
| --- |
| **模块参数：** `action` |
| **类型：** 字符向量 |
| **值：** `'Error'` | `'Warning'` | `'None'` |
| **默认值：** `'Error'` |

### **Output horizontal intensity** — 输出水平强度 开（默认）| `off`

要输出水平强度值，请选中此复选框。否则，请清除此复选框。

#### 依赖

要启用 **Horizontal Intensity** 输出端口，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `h_out` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Output declination** — 输出磁偏角 开（默认）| `off`

要输出磁偏角（真北与磁场矢量之间的夹角，向东为正），请选中此复选框。否则，请清除此复选框。

#### 依赖

要启用 **Declination** 输出端口，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `dec_out` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Output inclination** — 输出磁倾角 开（默认）| `off`

要输出磁倾角（水平面与磁场矢量之间的夹角，向下为正），请选中此复选框。否则，请清除此复选框。

#### 依赖

要启用 **Inclination** 输出端口，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `inc_out` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Output total intensity** — 输出总强度 开（默认）| `off`

要输出总强度，请选中此复选框。否则，请清除此复选框。

#### 依赖

要启用 **Total Intensity** 输出端口，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `ti_out` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2025a：World Magnetic Model 模块现在支持 World Magnetic Model (WMM) WMM2025

World Magnetic Model 模块现在支持 World Magnetic Model (WMM) WMM2025。

## 描述

使用 World Magnetic Model 计算特定位置和时间的地球磁场

World Magnetic Model 模块实现了美国国家地理空间情报局 (NGA) World Magnetic Model 的数学表示。World Magnetic Model 模块计算指定位置和时间的地球磁场矢量、水平强度、磁偏角、磁倾角和总强度。参考坐标系为北-东-下 (NED)。

**注意**

使用此模块对 -1,000 m 到 850,000 m 米之间的高度的地球磁场进行建模。
