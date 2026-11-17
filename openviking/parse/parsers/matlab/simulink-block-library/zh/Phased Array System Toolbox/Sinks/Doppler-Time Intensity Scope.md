---
type: simulink-block
title: 'Doppler-Time Intensity Scope'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'dopplertimeintensityscope'
documentation_source_path: 'ref/dopplertimeintensityscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Doppler-Time Intensity Scope

## 端口

### 输入

### **X** — 输入数据，实值长度-*M* 向量

输入数据，指定为多普勒响应的实值长度-*M* 向量。每个向量对应一行数据。该模块接受单精度数据类型输入，但会将数据转换为双精度以进行显示。

**数据类型：** `double` | `single`

## 参数

### **Doppler Output** — 多普勒输出域 `'Frequency'`（默认）| `'Speed'`

多普勒输出域，指定为 `'Frequency'` 或 `'Speed'`。如果将此属性设置为 `'Frequency'`，则多普勒域为多普勒频移。单位为 Hz。如果将此属性设置为 `'Speed'`，则多普勒域为径向速度。单位为 m/s。

#### 编程使用

|  |
| --- |
| **模块参数：**`DopplerOutput` |
| **类型：**字符向量 |
| **值：**`'Frequency'` | `'Speed'` |
| **默认：**`'Frequency'` |

**数据类型：** `string`

### **Propagation Speed (m/s)** — 信号传播速度 `physconst("LightSpeed")`（默认）| 正标量

信号传播速度，指定为正标量。要获取 SI 单位下的光速，请使用 `physconst`。单位为米/秒。

**示例：** `3e8`

#### 编程使用

|  |
| --- |
| **模块参数：**`PropagationSpeed` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`physconst("LightSpeed")` |

**数据类型：** `double`

### **Doppler Offset (Hz)** — 多普勒轴偏移 `0.0`（默认）| 标量

多普勒轴偏移，指定为标量。此属性对多普勒轴施加频率偏移。单位为 Hz。

#### 编程使用

|  |
| --- |
| **模块参数：**`DopplerOffset` |
| **类型：**double |
| **值：**标量 |
| **默认：**`0` |

**数据类型：** `double`

### **Time Span (s)** — 显示的时间跨度 `0.100`（默认）| 正标量

强度显示的时间跨度，指定为正标量。单位为秒。

#### 编程使用

|  |
| --- |
| **模块参数：**`TimeSpan` |
| **类型：**double |
| **值：**标量 |
| **默认：**`0.1` |

**数据类型：** `double`

### **Operating Frequency (Hz)** — 工作频率 `300e6`（默认）| 正标量

工作频率，指定为正标量。单位为 Hz。

#### 编程使用

|  |
| --- |
| **模块参数：**`OperatingFrequency` |
| **类型：**double |
| **值：**标量 |
| **默认：**`300000000` |

**数据类型：** `double`

### **Doppler Resolution (Hz)** — 采样之间的多普勒间隔 `1.0`（默认）| 正标量

采样之间的多普勒间隔，指定为正标量。此属性定义示波器列之间的多普勒频率差。单位为 Hz。

#### 编程使用

|  |
| --- |
| **模块参数：**`DopplerResolution` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`1` |

**数据类型：** `double`

### **Time Resolution (s)** — 行之间的时间差 `0.001`（默认）| 正标量

采样之间的时间间隔，指定为正标量。此属性定义示波器行之间的时间持续时间。单位为秒。

#### 编程使用

|  |
| --- |
| **模块参数：**`TimeResolution` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`0.001` |

**数据类型：** `double`

### **Show Grid** — 显示笛卡尔网格 开（默认）| 关

显示笛卡尔网格叠加。要显示网格，请选中该复选框。

#### 编程使用

|  |
| --- |
| **模块参数：**`ShowGrid` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认：**`1` |

### **Show Ticks** — 显示刻度值标签 开（默认）| 关

在刻度标记上显示值标签。要显示标签，请选中该复选框。

#### 编程使用

|  |
| --- |
| **模块参数：**`ShowTicks` |
| **类型：**logical |
| **值：**1 | 0 |
| **默认：**`1` |

#### 标签

### **Time Label** — 时间轴标签 `'Time (s)'`（默认）| 字符串

时间轴标签，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`TimeLabel` |
| **类型：**string |
| **值：**string |
| **默认：**`'Time History (s)'` |

**数据类型：** `string`

### **Colorbar Label** — 颜色条标签 `'dB'`（默认）| 字符串

颜色条标签，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`ColorBarLabel` |
| **类型：**string |
| **值：**string |
| **默认：**`'dB'` |

**数据类型：** `string`

### **Title** — 窗口标题 `'Doppler vs. Time'`（默认）| 字符串

窗口标题，指定为字符串。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：**`Title` |
| **类型：**string |
| **值：**string |
| **默认：**`'Doppler vs. Time'` |

**数据类型：** `char`

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

此模块可用于在生成代码的系统中进行仿真可视化，但不会包含在生成的代码中。

## 版本历史

**在 R2022a 中引入**

## 描述

多普勒-时间强度示波器

Doppler-Time Intensity Scope 模块创建一个多普勒响应强度随时间变化的滚动显示。输入由脉冲或 FMCW 信号的多普勒响应组成。每一帧数据在示波器上创建一条新线。该示波器仅用作多普勒响应的显示。将响应用作输入对应于将 `phased.DTIScope` System object™ 的 `IQDataInput` 属性设置为 `false`。
