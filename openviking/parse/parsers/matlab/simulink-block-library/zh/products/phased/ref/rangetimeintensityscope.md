---
type: simulink-block
title: 'Range-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Visualization'
documentation_page: 'rangetimeintensityscope'
documentation_source_path: 'ref/rangetimeintensityscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Range-Time Intensity Scope

## 端口

### 输入

### **X** — 输入数据，实值长度-*M* 向量

输入数据，指定为距离响应的实值长度-*M* 向量。每个向量对应于一行数据。该模块接受 single 精度数据类型输入，但会为显示将数据转换为 double 精度。

**数据类型:** `double` | `single`

## 参数

#### 数据和坐标轴

### **距离偏移 (m)** — 距离偏移 `0.0`（默认） | 正标量

距离偏移，指定为正标量。此参数定义显示第一列的距离值。单位是 meters。

#### 编程使用

|  |
| --- |
| **模块参数:**`RangeOffset` |
| **类型:**double |
| **值:**标量 |
| **默认值:**`0` |

**数据类型:** `double`

### **时间跨度 (s)** — 显示的时间跨度 `0.1`（默认） | 正标量

强度显示的时间跨度，指定为正标量。单位是 seconds。

#### 编程使用

|  |
| --- |
| **模块参数:**`TimeSpan` |
| **类型:**double |
| **值:**标量 |
| **默认值:**`1` |

**数据类型:** `double`

### **距离分辨率 (m)** — 样本之间的距离差 `1`（默认） | 正标量

样本之间的距离，指定为正标量。此参数定义示波器各列之间的距离。单位是 meters。

#### 编程使用

|  |
| --- |
| **模块参数:**`RangeResolution` |
| **类型:**double |
| **值:**正标量 |
| **默认值:**`25` |

**数据类型:** `double`

### **时间分辨率 (s)** — 行之间的时间差 `0.001`（默认） | 正标量

样本之间的时间间隔，指定为正标量。此参数定义示波器各行之间的时间间隔。单位是 seconds。

#### 编程使用

|  |
| --- |
| **模块参数:**`TimeResolution` |
| **类型:**double |
| **值:**正标量 |
| **默认值:**`0.00033356` |

**数据类型:** `double`

### **显示网格** — 显示笛卡尔网格覆盖 on（默认） | off

显示笛卡尔网格覆盖。要显示网格，请选中该复选框。

#### 编程使用

|  |
| --- |
| **模块参数:**`ShowGrid` |
| **类型:**logical |
| **值:**1 | 0 |
| **默认值:**`1` |

### **显示刻度** — 显示刻度值标签 on（默认） | off

在刻度标记上显示值标签。要显示标签，请选中该复选框。

#### 编程使用

|  |
| --- |
| **模块参数:**`ShowTicks` |
| **类型:**logical |
| **值:**1 | 0 |
| **默认值:**`1` |

#### 标签

### **距离标签** — 距离轴标签 `'Range (m)'`（默认） | string

距离轴标签，指定为 string。

**可调:** 是

#### 编程使用

|  |
| --- |
| **模块参数:**`RangeLabel` |
| **类型:**string |
| **值:**string |
| **默认值:**`'Range (m)'` |

**数据类型:** `char`

### **时间标签** — 时间轴标签 `Time History (s)'`（默认） | string

时间轴标签，指定为 string。

**可调:** 是

#### 编程使用

|  |
| --- |
| **模块参数:**`TimeLabel` |
| **类型:**string |
| **值:**string |
| **默认值:**`'Time History (s)'` |

**数据类型:** `string`

### **标题** — 窗口标题 `'Range vs. Time'`（默认） | string

窗口标题，指定为 string。

**可调:** 是

#### 编程使用

|  |
| --- |
| **模块参数:**`Title` |
| **类型:**string |
| **值:**string |
| **默认值:**`Range vs. Time'` |

**数据类型:** `char`

### **颜色栏标签** — 颜色栏 `'mag'`（默认） | string

颜色栏标签，指定为 string。

**可调:** 是

#### 编程使用

|  |
| --- |
| **模块参数:**`ColorBarLabel` |
| **类型:**string |
| **值:**string |
| **默认值:**`'mag'` |

**数据类型:** `string`

## 所属库

Phased Array System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可见性，但

## 版本历史

**在 R2022a 中引入**

## 描述

距离-时间强度示波器

Range-Tine Intensity Scope 模块创建一个距离响应强度随时间的滚动显示。输入由脉冲或 FMCW 信号的距离响应组成。每帧数据在示波器上创建一条新线。该示波器仅用作距离响应的显示。将响应用作输入对应于将 `phased.RTIScope` System object™ 的 `IQDataInput` 属性设置为 `false`。
