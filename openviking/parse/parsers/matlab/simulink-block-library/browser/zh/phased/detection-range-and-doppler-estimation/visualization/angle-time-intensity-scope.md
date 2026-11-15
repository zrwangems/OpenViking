---
type: simulink-block
title: 'Angle-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Visualization'
documentation_page: 'angletimeintensityscope'
documentation_source_path: 'ref/angletimeintensityscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Angle-Time Intensity Scope

## 端口

### 输入

### **X** — 输入数据实值长度-*M* 向量

输入数据，指定为角度响应的实值长度-*M* 向量。每个向量对应一行数据。该模块可以接受 single 精度数据类型输入，但会将数据转换为 double 精度以进行显示。

**数据类型：** `double` | `single`

## 参数

### **角度偏移 (degree)** — 角度偏移 `0.0`（默认）| 标量

角度偏移，指定为标量。此属性定义显示第一列的角度值。单位为 degrees。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AngleOffset` |
| **类型：**double |
| **值：**`scalar` | |
| **默认值：**0.0 |

**数据类型：** `double`

### **角度分辨率 (degree)** — 样本之间的角度差 `1.0`（默认）| 正标量

样本之间的角度间隔，指定为正标量。此属性定义示波器各列之间的角度差。单位为 degrees。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AngleResolution` |
| **类型：**double |
| **值：**`positive scalar` | |
| **默认值：**0.0 |

**数据类型：** `double`

### **时间跨度 (s)** — 显示的时间跨度 `Auto`（默认）

强度显示的时间跨度，指定为正标量。当 **时间跨度 (s)** 设置为 `Auto` 时，仿真在仿真的默认 **stop time** 处停止。单位为 seconds。

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeSpan` |
| **类型：**double |
| **值：**标量 |
| **默认值：**`0.1` |

**数据类型：** `double`

### **时间分辨率 (s)** — 行之间的时间差 `Auto`（默认）

行之间的时间间隔，指定为正标量。此属性定义示波器各行之间的持续时间。当 **时间分辨率 (s)** 参数设置为 `Auto` 时，模块在仿真期间使用 **Compiled Sample Time** 值。在所有其他时间，模块使用此参数指定的值。单位为 seconds。

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeResolution` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`0.001` |

**数据类型：** `double`

### **网格** — 显示笛卡尔网格叠加 on（默认）| off

显示笛卡尔网格叠加。要显示网格，请选中该复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ShowGrid` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认值：**`1` |

### **刻度** — 显示刻度值标签 on（默认）| off

在刻度线上显示值标签。要显示标签，请选中该复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ShowTicks` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认值：**`1` |

#### 标签

### **角度标签** — 角度轴标签 `'Angle (degree)'`（默认）| character vector | string

角度轴标签，指定为 character vector 或 string。

**示例：** `'Angle (rad)'`

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：**`AngleLabel` |
| **类型：**string |
| **值：**string |
| **默认值：**`'Angle (degree)'` |

**数据类型：** `char` | `string`

### **时间标签** — 时间轴标签 `'Time History (s)'`（默认）| string

时间轴标签，指定为 string。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeLabel` |
| **类型：**string |
| **值：**string |
| **默认值：**`'Time History (s)'` |

**数据类型：** `string`

### **标题** — 窗口标题 `'Angle vs. Time'`（默认）| string

窗口标题，指定为 string。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：**`Title` |
| **类型：**string |
| **值：**string |
| **默认值：**`'Doppler vs. Time'` |

**数据类型：** `char`

### **颜色栏标签** — 颜色栏标签 `'dB'`（默认）| string

颜色栏标签，指定为 string。

**可调：** Yes

#### 程序化使用

|  |
| --- |
| **模块参数：**`ColorBarLabel` |
| **类型：**string |
| **值：**string |
| **默认值：**`'dB'` |

**数据类型：** `string`

## 所属库

Phased Array System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可视化，但不包含在生成的代码中。

## 版本历史

**在 R2022b 中引入**

## 描述

角度-时间强度示波器

Angle-Time Intensity Scope 模块创建一个角度响应强度随时间变化的滚动显示。输入由脉冲或 FMCW 信号的角度响应组成。每帧数据在示波器上创建一条新线。示波器用作角度响应的显示。
