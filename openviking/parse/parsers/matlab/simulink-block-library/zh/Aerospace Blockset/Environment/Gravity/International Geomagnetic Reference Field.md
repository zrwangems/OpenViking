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

纬度，指定为标量，单位为度。此模块接受大于 90 且小于 -90 的纬度值。

**数据类型：** `double`

### **l (deg)** — 经度标量

经度，指定为标量，单位为度。此模块接受大于 180 且小于 -180 的范围。

**数据类型：** `double`

### **dyear** — 期望年份标量

期望年份，采用十进制格式，以包含当年已过去的部分。该值为当前年份加上当年已过去的天数除以 365。要计算 2015 年 3 月 21 日的十进制年份 `dyear`：

```
dyear=decyear('21-March-2015','dd-mmm-yyyy')
```

#### 依赖关系

要启用此端口，请选择 **Input decimal year**。

**数据类型：** `double`
### 输出

### **XYZ** — 磁场矢量

磁场，以矢量形式返回，采用所选单位。此矢量的分量位于北-东-地（NED）参考坐标系中。

**数据类型：** `double`

### **H** — 水平强度标量

水平强度，以标量形式返回，采用所选单位。

**数据类型：** `double`

### **D** — 磁偏角标量

磁偏角，以标量形式返回，单位为度。

**数据类型：** `double`

### **l** — 磁倾角标量

磁倾角，以标量形式返回，单位为度。

**数据类型：** `double`

### **F** — 总强度标量

总强度，以标量形式返回，采用所选单位。

**数据类型：** `double`

### **DXDYDZ** — 磁场长期变化矢量

磁场长期变化，以矢量形式返回，采用所选单位每年。

#### 依赖关系

要启用此端口，请选择 **Output secular variation**。

**数据类型：** `double`

### **DH** — 水平强度长期变化标量

水平强度长期变化，以标量形式返回，采用所选单位每年。

#### 依赖关系

要启用此端口，请选择 **Output secular variation**。

**数据类型：** `double`

### **DD** — 磁偏角长期变化标量

磁偏角长期变化，以标量形式返回，单位为分每年。

#### 依赖关系

要启用此端口，请选择 **Output secular variation**。

**数据类型：** `double`

### **DI** — 磁倾角长期变化标量

磁倾角长期变化，以标量形式返回，单位为分每年。

#### 依赖关系

要启用此端口，请选择 **Output secular variation**。

**数据类型：** `double`

### **DF** — 总强度长期变化标量

总强度长期变化，以标量形式返回，采用所选单位每年。

#### 依赖关系

要启用此端口，请选择 **Output secular variation**。

**数据类型：** `double`

## 参数

### **Generation** — International Geomagnetic Reference Field 代 `IGRF-14`（默认）| `IGRF-13` | `IGRF-11` | `IGRF-12`

International Geomagnetic Reference Field 代，从 `IGRF-14`、`IGRF-13`、`IGRF-12` 或 `IGRF-11` 中选择。

#### 程序化使用

|  |
| --- |
| **模块参数：** `generation` |
| **类型：** 字符向量 |
| **值：** `'IGRF-14'` | `'IGRF-13'` | `'IGRF-12'` | `'IGRF-11'` | |
| **默认：** `'IGRF-14'` |

**数据类型：** `char` | `string`

### **Units** — 单位 `Metric (MKS)`（默认）| `English`

参数和输出单位，指定为：

| 单位 | 高度 |
| --- | --- |
| `Metric (MKS)` | 米 |
| `English` | 英尺 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** 字符向量 |
| **值：** `'Metric (MKS)'` | `'English'` |
| **默认：** `'Metric (MKS)'` |

### **Input decimal year** — 期望年份 `on`（默认）| `off`

- 要使用输入端口指定十进制年份，请选中此复选框。
- 要使用 **Month**、**Day** 和 **Year** 的值指定十进制年份，请清除此复选框。

#### 依赖关系

要启用 **Month**、**Day** 和 **Year**，请清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `time_in` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Month** — 输入月份 `January`（默认）| `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算十进制年份的月份。

#### 依赖关系

要启用此参数，请清除 **Input decimal year**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `month` |
| **类型：** 字符向量 |
| **值：** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认：** `'January'` |

### **Day** — 输入日期 1（默认）| `1` 到 `31`

用于计算十进制年份的日期。

#### 依赖关系

要启用此参数，请清除 **Input decimal year**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `day` |
| **类型：** 字符向量 |
| **值：** `'1'` 到 `'31'` |
| **默认：** `'1'` |

### **Year** — 输入年份 `2025`（默认）| `1900` 到 `2030`

用于计算十进制年份的年份，指定为 `1900` 到 `2030`。

#### 依赖关系

要启用此参数，请清除 **Input decimal year**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `year` |
| **类型：** 字符向量 |
| **值：** 任意年份 |
| **默认：** `'2025'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 诊断查看器中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**： 字符向量 |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认**： `'Warning'` |

### **Output secular variance** — 长期变化 `on`（默认）| `off`

选中此复选框可启用长期变化（年变化率）与非长期变化的输出。否则，请清除此复选框。

| 长期变化 | 描述 |
| --- | --- |
| 磁场 | 磁场矢量，单位为纳特斯拉（nT）。*Z* 为垂直分量（+ve 向下） |
| 水平强度 | 水平强度，单位为纳特斯拉（nT） |
| 磁偏角 | 磁偏角，单位为度（+ve 向东） |
| 磁倾角 | 磁倾角，单位为度（+ve 向下） |
| 总强度 | 总强度，单位为纳特斯拉（nT） |
| SV 磁场 | 磁场长期变化 |
| SV 水平强度 | 水平强度长期变化 |
| SV 磁偏角 | 磁偏角长期变化，即真北与磁场矢量之间的夹角（正向东） |
| SV 磁倾角 | 磁倾角长期变化，即水平面与磁场矢量之间的夹角（正向向下） |
| SV 总强度 | 总强度长期变化 |

清除此复选框仅启用非长期变化：

- 磁场
- 水平强度
- 磁偏角
- 磁倾角
- 总强度

#### 程序化使用

|  |
| --- |
| **模块参数：** `sv_out` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：International Geomagnetic Reference Field 模块现在支持 International Geomagnetic Reference Field 第 14 代（IGRF-14）

International Geomagnetic Reference Field 模块现在支持 International Geomagnetic Reference Field 第 14 代（IGRF-14）。

## 描述

使用 International Geomagnetic Reference Field 计算地球磁场和长期变化

International Geomagnetic Reference Field 模块使用所选的 International Geomagnetic Reference Field 代计算地球磁场和长期变化。它使用所选的 International Geomagnetic Reference Field 代在给定位置和时间计算地球磁场和长期变化。
