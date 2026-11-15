---
type: simulink-block
title: 'WGS84 Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'wgs84gravitymodel'
documentation_source_path: 'wgs84gravitymodel.html'
language: zh-CN
chinese_source: worker-translation
---

# WGS84 Gravity Model

## 端口

### 输入

### **μ l h** — 大地纬度、经度和高度中的位置三元素向量 | *M*×3 数组

在大地纬度、经度和高度中的位置，以所选单位指定为三元素向量或 *M*×3 数组。高度必须小于 20,000 m（约 65,620 feet）。

对于超出限制（0 到 20000 m）的输入，如果 action 输入指定为 'None' 或 'warning'，则扩展实现。但是，不建议将模块用于超出这些限制的输入。

**数据类型:** `double`

### **JD** — 儒略日标量 | 大于 2451545 的值

儒略日，指定为标量。年份必须晚于 2000 年 1 月 1 日（2451545）。

#### 依赖关系

要启用此端口，请选择 **输入儒略日**。

**数据类型:** `double`
### 输出

### **Output 1** — 重力三元素向量 | *M*×3 数组

北-东-地（NED）坐标系中的重力。

| 重力模型方法 | 输出 |
| --- | --- |
| 泰勒级数和闭合近似 | 仅输出正常重力（NED 坐标系中向下）。 |
| 精确 | 同时输出正常重力和切向重力（NED 坐标系中向下和向北）。 |

**数据类型:** `double`

## 参数

### **重力模型类型** — 重力模型方法 `WGS84 Taylor Series`（默认） | `WGS84 Close Approximation` | `WGS84 Exact`

计算重力的方法，指定为：

| 重力模型方法 | 输出 |
| --- | --- |
| `WGS84 Taylor Series` 和 `WGS84 Close Approximation` | 仅输出正常重力（NED 坐标系中向下）。 |
| `WGS84 Exact` | 同时输出正常重力和切向重力（NED 坐标系中向下和向北）。 |

#### 编程使用

|  |
| --- |
| **模块参数**: `model` |
| **类型**: character vector |
| **值**: `'WGS84 Taylor Series'` | `'WGS84 Close Approximation'` | `'WGS84 Exact'` |
| **默认值**: `'WGS84 Taylor Series'` |

### **单位** — 单位 `Metric (MKS)`（默认） | `English`

输入和输出单位，指定为：

| 单位 | 高度 | 重力 |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters per second squared |
| `English` | Feet | Feet per second squared |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **排除地球大气层** — 地球大气层 `on`（默认） | `off`

- 要排除地球重力场的大气质量，请选中此复选框。
- 要包含地球重力场的大气质量，请清除此复选框。

#### 依赖关系

要启用此复选框，请将 **重力模型类型** 设置为 `Type of gravity model WGS84 Close Approximation` 或 `WGS84 Exact`。

#### 编程使用

|  |
| --- |
| **模块参数**: `no_atmos` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **进动参考系** — 进动参考系 `on`（默认） | `off`

- 要使用国际天文学联合会（IAU）的地球角速度值和赤经中的进动率计算地球速度，请选中此复选框。
- 要使用以恒定角速度旋转的标准地球的角速度计算地球速度，请清除此复选框。

为获得赤经中的进动率，模块使用 **月**、**日** 和 **年** 从 Epoch J2000.0 计算儒略世纪。

#### 依赖关系

- 要启用此复选框，请将 **重力模型类型** 设置为 `Type of gravity model WGS84 Close Approximation` 或 `WGS84 Exact`。
- 清除此复选框会禁用 **输入儒略日** 参数和 **JD** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**: `precessing` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **输入儒略日** — 儒略日 `off`（默认） | `on`

- 要使用输入端口为模块指定儒略日，请选中此复选框。
- 要使用 **月**、**日** 和 **年** 的值计算儒略日，请清除此复选框。年份必须晚于 2000 年 1 月 1 日（2451545）。

#### 依赖关系

- 要启用 **JD** 端口，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `jd_loc` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **月** — 月 `January`（默认） | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于从 Epoch J2000.0 计算儒略世纪的月份。

#### 依赖关系

要启用此参数：

- 将 **重力模型类型** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **进动参考系**。

要禁用此参数，请选择 **输入儒略日**。

#### 编程使用

|  |
| --- |
| **模块参数**: `month` |
| **类型**: character vector |
| **值:** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**: `'January'` |

### **日** — 日 10（默认） | `1` 到 `31`

用于从 Epoch J2000.0 计算儒略世纪的天数。

#### 依赖关系

要启用此参数：

- 将 **重力模型类型** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **进动参考系**。

要禁用此参数，请选择 **输入儒略日**。

#### 编程使用

|  |
| --- |
| **模块参数:** `day` |
| **类型:** character vector |
| **值:** `'1'` 到 `'31'` |
| **默认值:** `'10'` |

### **年** — 年 2004（默认） | 任意年份

用于从 Epoch J2000.0 计算儒略世纪的年份。年份必须为 2000 或更大。

#### 依赖关系

要启用此参数：

- 将 **重力模型类型** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **进动参考系**。
- 要禁用此参数，请选择 **输入儒略日**。

#### 编程使用

|  |
| --- |
| **模块参数:** `year` |
| **类型:** character vector |
| **值:** 任意年份 |
| **默认值:** `'2004'` |

### **无离心效应** — 离心效应 `on`（默认） | `off`

- 要使计算的重力基于由正常重力势产生的纯吸引力，请选中此复选框。
- 要使计算的重力包含由地球角速度产生的离心力，请清除此复选框。

此选项仅适用于 **重力模型类型 WGS84 Close Approximation** 或 **WGS84 Exact**。

#### 编程使用

|  |
| --- |
| **模块参数**: `no_centrifugal` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **超出范围输入的操作** — 超出范围模块行为 `Warning`（默认） | `Error` | `None`

超出范围的模块行为，指定如下。

| 值 | 描述 |
| --- | --- |
| `None` | 无操作。模块对输入信号施加上限和下限。对于超出限制的输入，会扩展实现。 |
| `Warning` | 在诊断查看器中发出警告，模型仿真继续。对于加速器和快速加速器模式，将操作设置为 `Warning` 没有效果，模型的行为就像该操作设置为 `None` 一样。 |
| `Error` | MATLAB® 返回异常，模型仿真停止。对于加速器和快速加速器模式，将操作设置为 `Error` 没有效果，模型的行为就像该操作设置为 `None` 一样。 |

不建议将 WGS84 Gravity Model 用于超出限制的输入。

#### 编程使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现 1984 世界大地测量系统（WGS84）对地球重力的表示

WGS84 Gravity Model 模块实现世界大地测量系统（WGS84）的地心等位椭球的数学表示。模块输出是特定位置的地球重力。要控制重力精度，请使用 **重力模型类型** 参数。

模块图标显示从 **单位** 列表中选择的输入和输出单位。
