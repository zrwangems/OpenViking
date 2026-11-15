---
type: simulink-block
title: 'LLA to Flat Earth'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'llatoflatearth'
documentation_source_path: 'llatoflatearth.html'
language: zh-CN
chinese_source: worker-translation
---

# LLA to Flat Earth

## 端口

### 输入

### **μl** — 大地纬度和经度 2-by-1 向量

大地纬度和经度，指定为 2-by-1 向量，单位为 degrees。

**数据类型：** `double`

### **h** — 高度标量

高于输入参考高度的高度，指定为标量，单位与 flat Earth 位置相同。

**数据类型：** `double`

### **href** — 参考高度标量

从地球表面到 flat Earth 坐标系的参考高度，指定为标量，单位与 flat Earth 位置相同。参考高度是相对于地球坐标系估计的。

**数据类型：** `double`

### **μref lref** — 参考位置 2-by-1 向量

参考位置，指定为 2-by-1 向量，以纬度和经度的 degrees 表示，用于估计的原点和 flat Earth 坐标系的原点。如果要将参考位置指定为动态值，请使用此端口。

#### 依赖关系

要启用此端口，请选择 **输入参考位置和方向**。

**数据类型：** `double`

### **ψref** — flat Earth *x* 轴方向标量

用于将 flat Earth *x* 和 *y* 坐标转换为北向和东向坐标的角度，指定为标量。如果要将该角度指定为动态值，请使用此端口。

#### 依赖关系

要启用此端口，请选择 **输入参考位置和方向**。

**数据类型：** `double`

### 输出

### **Xe** — 位置 3-by-1 向量

flat Earth 坐标系中的位置，以向量形式返回。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (default) | `English`

参数和输出单位。

| 单位 | 位置 | 赤道半径 | 高度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **行星模型** — 行星模型 `Earth (WGS84)` (default) | `Custom`

要使用的行星模型，指定为 `Custom` 或 `Earth (WGS84)`。

#### 依赖关系

选择 `Custom` 选项会启用以下参数：

- **扁率**
- **行星赤道半径**

#### 程序化使用

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'Earth (WGS84)'` | `'Custom'` |
| **默认值**: `'Earth (WGS84)'` |

### **扁率** — 行星扁率 `1/298.257223563` (default) | scalar

行星的扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `F` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `1/298.257223563` |

### **行星赤道半径** — 行星赤道处半径 `6378137` (default) | scalar

行星赤道处的半径，指定为 double 标量，单位与 **单位** 参数相同。

#### 依赖关系

当 **行星模型** 设置为 `Custom` 时，此参数启用。

#### 程序化使用

|  |
| --- |
| **模块参数**: `R` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `6378137` |

### **输入参考位置和方向** — 输入参考位置和方向作为端口 `off` (default) | `on`

- 要启用用于转换 flat Earth 的参考位置和角度的输入端口，请选中此复选框。
- 要将参考位置和角度指定为静态值，请清除此复选框。

如果需要，请选中此复选框

#### 程序化使用

|  |
| --- |
| **模块参数**: `refPosPort` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **参考大地纬度和经度 (deg)** — 初始大地纬度和经度 `[0 10]` (default) | 2-by-1 vector

以纬度和经度表示的参考位置，指定为 2-by-1 向量，以 degrees 为单位。

#### 依赖关系

要启用此参数，请清除 **输入参考位置和方向** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `LL0` |
| **类型**: character vector |
| **值**: 2-by-1 vector |
| **默认值**: `[0 10]` |

### **局部切平面 x 轴方向（从北顺时针 degrees）** — 角度 `0` (default) | scalar

用于将 flat Earth（局部切平面）*x* 和 *y* 坐标转换为北向和东向坐标的角度，指定为 double 标量，以 degrees 为单位。

#### 依赖关系

要启用此参数，请清除 **输入参考位置和方向**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `psi` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `0` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

根据大地纬度、经度和高度估计 flat Earth 位置

LLA to Flat Earth 模块将大地纬度 (μ¯)、经度 (ι¯) 和高度 (*h*) 转换为 3-by-1 的 flat Earth 位置向量 (p¯)。纬度和经度值可以为任意值。但是，由于极点处的奇异性，纬度值 +90 和 -90 可能会返回意外值。有关 flat Earth（局部切平面）坐标系的详细信息，请参阅算法。
