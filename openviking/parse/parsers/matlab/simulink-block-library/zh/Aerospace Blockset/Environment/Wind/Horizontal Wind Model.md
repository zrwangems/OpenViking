---
type: simulink-block
title: 'Horizontal Wind Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel'
documentation_source_path: 'horizontalwindmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model

## 端口

### 输入

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为表示平面地球坐标到机体轴坐标的 3×3 矩阵。

**数据类型：** `double`

### **Vwind** — 风速 1×3 向量

风速，指定为 1×3 向量，采用所选单位。

#### 依赖关系

要启用此参数，请将 **Wind speed source** 设置为 `External`。

**数据类型：** `double`

### **θwind** — 风向 标量

风向，指定为标量，以度为单位。风向为从地球 *x* 轴方向（北）顺时针方向的角度。风向定义为风来自的方向。

#### 依赖关系

要启用此参数，请将 **Wind direction source** 设置为 `External`。

**数据类型：** `double`
### 输出

### **Vwind** — 风速 3×3 矩阵

风速，返回为与 **DCM** 输入相同的机体坐标系参考下的三元素信号，采用指定单位。

**数据类型：** `double`

## 参数

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 风速 | 风速 |
| --- | --- | --- |
| `Metric (MKS)` | 米每秒 | 米每秒 |
| `English (Velocity in ft/s)` | 英尺每秒 | 英尺每秒 |
| `English (Velocity in kts)` | 节 | 节 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in kts)'` | `'English (Velocity in ft/s)'` |
| **默认值**：`'Metric (MKS)'` |

### **Wind speed source** — 风速源 `Internal`（默认）| `External`

风速源，指定为：

|  |  |
| --- | --- |
| `External` | 可变风速输入到模块 |
| `Internal` | 在掩码中指定的恒定风速 |

#### 依赖关系

- 将此参数设置为 `Internal` 会启用 **Wind speed at altitude**。
- 将此参数设置为 `External` 会启用 **Vwind** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Vw_source` |
| **类型**：字符向量 |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Wind speed at altitude (m/s)** — 风速 `15`（默认）| 标量

恒定风速，指定为双精度标量，采用指定单位。

#### 依赖关系

要启用此参数，请将 **Wind speed source** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Vwind` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'15'` |

### **Wind direction source** — 风向源 `Internal`（默认）| `External`

风向源，指定为：

|  |  |
| --- | --- |
| `External` | 可变风向输入到模块 |
| `Internal` | 在掩码中指定的恒定风向 |

#### 依赖关系

- 将此参数设置为 `Internal` 会启用 **Wind direction at altitude (degrees clockwise from north)**。
- 将此参数设置为 `External` 会启用 **θwind** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`W_source` |
| **类型**：字符向量 |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Wind direction at altitude (degrees clockwise from north)** — 风向 `0`（默认）

恒定风向，指定为标量，以从地球 *x* 轴方向（北）顺时针方向的度数为单位。风向是风来自的方向。

#### 依赖关系

要启用此参数，请将 **Wind direction source** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Wdeg` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将水平风变换为机体轴坐标

Horizontal Wind Model 模块计算机体轴坐标下的风速。

风由地球轴下的风速和风向指定。风速和风向可以是恒定的，也可以随时间变化。风向为从地球 *x* 轴方向（北）顺时针方向的度数为单位。风向定义为风来自的方向。使用方向余弦矩阵（DCM），风速被变换为机体轴坐标。
