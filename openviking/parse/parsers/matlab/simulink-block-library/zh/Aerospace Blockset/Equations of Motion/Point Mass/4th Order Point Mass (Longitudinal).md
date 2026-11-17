---
type: simulink-block
title: '4th Order Point Mass (Longitudinal)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '4thorderpointmasslongitudinal'
documentation_source_path: '4thorderpointmasslongitudinal.html'
language: zh-CN
chinese_source: worker-translation
---

# 4th Order Point Mass (Longitudinal)

## 端口

### 输入

### **Fx(N)** — *x* 轴方向的力 标量 | 数组

*x* 轴方向的力，指定为标量或数组，采用所选单位。

**数据类型：** `double`

### **Fz(N)** — *z* 轴方向的力 标量 | 数组

*z* 轴方向的力，指定为标量或数组，采用所选单位。

**数据类型：** `double`
### 输出

### **ɣ** — 航迹角 标量 | 数组

航迹角，以标量或数组形式返回，单位为弧度。

**数据类型：** `double`

### **V** — 空速 标量 | 数组

空速，以标量或数组形式返回，采用所选单位。

**数据类型：** `double`

### **XEast** — 下程或向东飞行距离 标量 | 数组

下程或向东飞行距离，以标量或数组形式返回，采用所选单位。

**数据类型：** `double`

### **XUp** — 高度或向上飞行距离 标量 | 数组

高度或向上飞行距离，以标量或数组形式返回，采用所选单位。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 力 | 速度 | 位置 | 质量 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | 牛顿 | 米每秒 | 米 | 千克 |
| `English (Velocity in ft/s)` | 磅 | 英尺每秒 | 英尺 | 斯勒格 |
| `English (Velocity in kts)` | 磅 | 节 | 英尺 | 斯勒格 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Initial flight path angle** — 初始航迹角 `0`（默认）| 标量 | 向量

质点（一个或多个）的初始航迹角，指定为标量或向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`gamma0` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

### **Initial airspeed** — 初始空速 `100`（默认）| 标量 | 向量

质点（一个或多个）的初始空速，指定为标量或向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`V0` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'100'` |

### **Initial downrange [East]** — 初始下程 `0`（默认）| 标量 | 向量

质点（一个或多个）的初始下程，指定为标量或向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`x0` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

### **Initial altitude [Up]** — 质点的初始高度 `0`（默认）| 标量 | 向量

质点（一个或多个）的初始高度，指定为标量或向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`h0` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

### **Initial mass** — 质点质量 `1.0`（默认）| 标量 | 向量

质点（一个或多个）的质量，指定为标量或向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass0` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'1.0'` |

## 所属库

Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算四阶质点

4th Order Point Mass (Longitudinal) 模块执行单个质点或多个质点的平移运动计算。有关单个质点或多个质量平移运动系统的详细信息，请参阅 Algorithms。

4th Order Point Mass (Longitudinal) 模块的端口标签会根据从 **Units** 列表中选择的输入和输出单位而变化。
