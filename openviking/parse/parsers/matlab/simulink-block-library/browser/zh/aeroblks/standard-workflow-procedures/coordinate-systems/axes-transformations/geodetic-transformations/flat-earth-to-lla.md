---
type: simulink-block
title: 'Flat Earth to LLA'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'flatearthtolla'
documentation_source_path: 'flatearthtolla.html'
language: zh-CN
chinese_source: worker-translation
---

# Flat Earth to LLA

## 端口

### 输入

### **Xe** — 平地坐标系中的位置 3×1 向量

平地坐标系中的位置，指定为 3×1 向量。

**数据类型:** `double`

### **href** — 参考高度 标量

从地球表面到平地坐标系（相对于地球坐标系）的参考高度，指定为标量，单位与平地位置相同。

**数据类型:** `double`

### **μref lref** — 参考位置 2×1 向量

参考位置，指定为 2×1 向量，以纬度和经度的度数为单位，用于估计的原点和平地坐标系的原点。如果要将参考位置指定为动态值，请使用此端口。

#### 依赖关系

如果选中 **输入参考位置和方向** 复选框，则启用此端口。

**数据类型:** `double`

### **ψref** — 平地 *x* 轴方向 标量

用于将平地 *x* 和 *y* 坐标转换为北向和东向坐标的角度，指定为标量。如果要将该角度指定为动态值，请使用此端口。

#### 依赖关系

如果选中 **输入参考位置和方向** 复选框，则启用此端口。

**数据类型:** `double`
### 输出

### **μ l** — 大地纬度和经度 2×1 向量

大地纬度和经度，以 2×1 向量形式返回，单位为度。

**数据类型:** `double`

### **h** — 高度 标量

高于输入参考高度的高度，以标量形式返回，单位与平地位置相同。

**数据类型:** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (默认) | `English`

参数和输出单位。

| 单位 | 位置 | 赤道半径 | 高度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### 编程用法

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **行星模型** — 行星模型 `Earth (WGS84)` (默认) | `Custom`

要使用的行星模型，指定为 `Custom` 或 `Earth (WGS84)`。

#### 依赖关系

选择 `Custom` 选项会启用以下参数：

- **扁率**
- **行星赤道半径**

#### 编程用法

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'Earth (WGS84)'` | `'Custom'` |
| **默认值**: `'Earth (WGS84)'` |

### **扁率** — 行星扁率 `1/298.257223563` (默认) | 标量

行星扁率，指定为 double scalar。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**: `F` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `1/298.257223563` |

### **行星赤道半径** — 行星赤道半径 `6378137` (默认) | 标量

行星赤道半径，指定为 double scalar，单位与 **单位** 参数相同。

#### 依赖关系

当 **行星模型** 设置为 `Custom` 时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数**: `R` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `6378137` |

### **输入参考位置和方向** — 作为端口的输入参考位置和方向 `off` (默认) | `on`

- 要启用用于参考位置和角度的输入端口以转换平地，请选中此复选框。
- 要将参考位置和角度指定为静态值，请清除此复选框。

如果需要，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `refPosPort` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **参考大地纬度和经度（度）** — 初始大地纬度和经度 `[0 10]` (默认) | 2×1 向量

参考位置，以纬度和经度指定，指定为 2×1 向量，单位为度。

#### 依赖关系

要启用此参数，请清除 **输入参考位置和方向** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `LL0` |
| **类型**: character vector |
| **值**: 2×1 向量 |
| **默认值**: `[0 10]` |

### **局部切平面 x 轴方向（从北顺时针的度数）** — 角度 `0` (默认) | 标量

用于将平地（局部切平面）*x* 和 *y* 坐标转换为北向和东向坐标的角度，指定为 scalar double，单位为度。

#### 依赖关系

要启用此参数，请清除 **输入参考位置和方向**。

#### 编程用法

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

**在 R2006a 之前引入**

## 描述

根据平地位置估计大地纬度、经度和高度

Flat Earth to LLA 模块将 3×1 的平地位置向量 (p¯) 转换为大地纬度 (μ¯)、经度 (ι¯) 和高度 (*h*)。有关平地（局部切平面）坐标系的详细信息，请参阅算法。
