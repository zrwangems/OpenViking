---
type: simulink-block
title: 'Zonal Harmonic Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'zonalharmonicgravitymodel'
documentation_source_path: 'zonalharmonicgravitymodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Zonal Harmonic Gravity Model

## 端口

### 输入

### **Xecef** — 行星中心行星固连坐标 m-by-3 矩阵

行星中心行星固连坐标，指定为 *m*-by-3 矩阵，从行星中心起算，以所选长度单位表示。如果 **行星模型** 的值为 `Earth`，则此矩阵包含地心地球固连 (ECEF) 坐标。

**数据类型：** `double`
### 输出

### **gecef** — 重力值 m-by-3 数组

重力值，以 *m*-by-3 数组返回，位于行星中心行星固连坐标的 x 轴、y 轴和 z 轴方向，以所选长度单位每秒平方表示。

**数据类型：** `double`

## 参数

### **单位** — 输入单位 `Metric (MKS)`（默认） | `English`

输入单位，指定为：

| 单位 | 位置 | 赤道半径 | 引力参数 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters cubed per second squared |
| `English` | Feet | Feet | Feet cubed per second squared |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **阶数** — 谐波模型的阶数 `4`（默认） | `2` | `3`

谐波模型的阶数，指定为。

- `2` — 二阶，J2。最重要或最大的球谐项，它考虑了行星的扁率。
- `3` — 三阶，J3。
- `4` — 四阶，J4（默认）。

#### 编程用法

|  |
| --- |
| **模块参数**：`degree` |
| **类型**：character vector |
| **值**：`'2'` | `'3'` | `'4'` |
| **默认值**：`'4'` |

### **超出范围输入的操作** — 超出范围输入行为 `Warning`（默认） | `Error` | `None`

超出范围输入行为，指定为：

| 值 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error` | MATLAB® 返回异常，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### **行星模型** — 行星模型 `Mercury`（默认） | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

行星模型，指定为 `Mercury`、`Venus`、`Earth`、`Moon`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune` 或 `Custom`。

选择 `Custom` 可让您指定自己的行星模型。

- 选择 `Mercury`、`Venus`、`Moon`、`Uranus` 或 `Neptune` 会将阶数限制为 `2`。
- 选择 `Mars` 会将阶数限制为 `3`。

#### 依赖关系

选择 `Custom` 会启用 **赤道半径**、**引力参数** 和 **J values rate** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Mercury'` | `'Venus'` | `'Earth'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` |
| **默认值**：`'Earth'` |

### **赤道半径** — 行星赤道半径 `6378136.3`（默认） | scalar

行星赤道半径，指定为标量，以 **单位** 参数定义的长度单位表示。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`R` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'6378136.3'` |

### **引力参数** — 行星引力参数 `398600441500000`（默认） | scalar

行星引力参数，指定为标量，以 **单位** 参数定义的长度单位的三次方每秒平方表示。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`GM` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'398600441500000'` |

### **J 值** — 带谐系数 `[1.0826269e-03 -2.5323000e-06 -1.6204000e-06]`（默认） | 3-element array

带谐系数，指定为 3 元素数组。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`jvalue` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[1.0826269e-03 -2.5323000e-06 -1.6204000e-06]'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

计算行星重力的带谐表示

Zonal Harmonic Gravity Model 模块基于行星引力势计算特定位置处行星重力的带谐表示。此模块提供了一种便捷方式，用于描述行星表面之外的行星引力场。

默认情况下，该模块使用地球的四阶带谐系数计算带谐重力。它还允许您指定二阶或三阶带谐系数。

有关模块实现中每颗行星的行星参数值的信息，请参阅算法。
