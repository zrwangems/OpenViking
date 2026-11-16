---
type: simulink-block
title: 'Centrifugal Effect Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'centrifugaleffectmodel'
documentation_source_path: 'centrifugaleffectmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Centrifugal Effect Model

## 端口

### 输入

### **Xecef** — 行星中心行星固定坐标 m-by-3 矩阵

以行星中心为原点的行星中心行星固定坐标，指定为标量。如果 **Planet model** 的值为 `Earth`，则该矩阵包含地心地球固定（ECEF）坐标。该模块不使用显式单位。

**数据类型：** `double`

### **ω** — 行星自转速率 标量

行星自转速率，指定为标量，单位为 rad/sec。

#### 依赖关系

要启用此参数，请将 **Planetary rotational rate (rad/sec)** 设置为 `Custom`。

**数据类型：** `double`

### 输出

### **Output 1** — 重力值 m-by-3 数组

重力值，以 m-by-3 数组返回，沿行星中心行星固定坐标的 *x* 轴、*y* 轴和 *z* 轴，单位为 input distance units per second squared。

**数据类型：** `double`

## 参数

### **Planet model** — 行星模型 `Earth`（默认）| `Venus` | `Mercury` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

行星模型，指定为 `Mercury`、`Venus`、`Earth`、`Moon`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune` 或 `Custom`。该模块使用所选行星的自转来实现离心效应的数学表示。

#### 依赖关系

选择 `Custom` 会启用 **Planetary rotational rate (rad/sec)** 和 **Input planetary rotation rate** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'Mercury'` | `'Venus'` | `'Earth'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` |
| **默认值**: `'Earth'` |

### **Planetary rotational rate (rad/sec)** — 行星自转速率 `7.2921150e-05`（默认）| scalar

行星自转速率，以 radians per second 为单位。

如果要将行星自转速率指定为模块的输入，请参阅 **Input planetary rotation rate** 参数。

#### 依赖关系

选中 **Input planetary rotation rate** 复选框会禁用 **Planetary rotational rate (rad/sec)** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**: `omega` |
| **类型**: character vector |
| **值**: `'7.2921150e-05'` | scalar |
| **默认值**: `'7.2921150e-05'` |

### **Input planetary rotation rate** — 行星自转速率端口 `off`（默认）| `on`

选中此复选框以启用 ω 输入端口。然后，您可以将行星自转速率作为模块输入。

#### 依赖关系

选中此复选框会启用 ω，并禁用 **Planetary rotational rate (rad/sec)** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**: `rate_loc` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

实现行星重力的离心效应数学表示

Centrifugal Effect Model 模块实现行星重力的离心效应数学表示。重力离心效应是由于行星自转产生的离心力效应中的加速度部分。此模块使用行星自转速率实现该表示。您在旋转或非惯性坐标系中使用离心力值。
