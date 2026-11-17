---
type: simulink-block
title: 'Range-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'rangetimeintensityscope'
documentation_source_path: 'ref/rangetimeintensityscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Range-Time Intensity Scope

## 端口

### 输入

### **X** — 输入数据，实值长度-*M* 向量

输入数据，指定为距离响应的实值长度-*M* 向量。每个向量对应一行数据。该模块接受单精度数据类型输入，但会将数据转换为双精度以进行显示。

**数据类型：** `double` | `single`

## 参数

#### 数据和坐标轴

### **Range Offset (m)** — 距离偏移 `0.0`（默认）| 正标量

距离偏移，指定为正标量。该参数定义显示第一列的距离值。单位为米。

#### 程序化使用

|  |
| --- |
| **模块参数：**`RangeOffset` |
| **类型：**double |
| **值：**标量 |
| **默认：**`0` |

**数据类型：** `double`

### **Time Span (s)** — 显示的时间跨度 `0.1`（默认）| 正标量

强度显示的时间跨度，指定为正标量。单位为秒。

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeSpan` |
| **类型：**double |
| **值：**标量 |
| **默认：**`1` |

**数据类型：** `double`

### **Range Resolution (m)** — 采样之间的距离差 `1`（默认）| 正标量

采样之间的距离，指定为正标量。该参数定义示波器列之间的距离。单位为米。

#### 程序化使用

|  |
| --- |
| **模块参数：**`RangeResolution` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`25` |

**数据类型：** `double`

### **Time Resolution (s)** — 行之间的时间差 `0.001`（默认）| 正标量

采样之间的时间间隔，指定为正标量。该参数定义示波器行之间的时间间隔。单位为秒。

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeResolution` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`0.00033356` |

**数据类型：** `double`

### **Show Grid** — 显示笛卡尔网格叠加 on（默认）| off

显示笛卡尔网格叠加。要显示网格，请选中该复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ShowGrid` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认：**`1` |

### **Show Ticks** — 显示刻度值标签 on（默认）| off

在刻度标记上显示值标签。要显示标签，请选中该复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ShowTicks` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认：**`1` |

#### 标签

### **Range Label** — 距离轴标签 `'Range (m)'`（默认）| 字符串

距离轴标签，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`RangeLabel` |
| **类型：**string |
| **值：**字符串 |
| **默认：**`'Range (m)'` |

**数据类型：** `char`

### **Time Label** — 时间轴标签 `Time History (s)'`（默认）| 字符串

时间轴标签，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeLabel` |
| **类型：**string |
| **值：**字符串 |
| **默认：**`'Time History (s)'` |

**数据类型：** `string`

### **Title** — 窗口标题 `'Range vs. Time'`（默认）| 字符串

窗口标题，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`Title` |
| **类型：**string |
| **值：**字符串 |
| **默认：**`Range vs. Time'` |

**数据类型：** `char`

### **Colorbar Label** — 颜色条 `'mag'`（默认）| 字符串

颜色条标签，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`ColorBarLabel` |
| **类型：**string |
| **值：**字符串 |
| **默认：**`'mag'` |

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

此模块可用于生成代码的系统中的仿真可视化，但

## 版本历史

**在 R2022a 中引入**

## 描述

距离-时间强度显示

距离-时间强度显示模块创建一个距离响应强度随时间的滚动显示。输入由脉冲或 FMCW 信号的距离响应组成。每一帧数据在显示上创建一条新线。该显示仅用作距离响应的显示。将响应用作输入对应于将 `phased.RTIScope` System object™ 的 `IQDataInput` 属性设置为 `false`。
