---
type: simulink-block
title: 'Relative Ratio'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Flight Parameters'
documentation_page: 'relativeratio'
documentation_source_path: 'relativeratio.html'
language: zh-CN
chinese_source: worker-translation
---

# Relative Ratio

## 端口

### 输入

### **Mach** — 马赫数标量

马赫数，指定为标量。

**数据类型：** `double`

### **γ** — 比值标量

定压比热 (*Cp*) 与定容比热 (*Cv*) 之间的比值，指定为标量。例如，(*γ* = *Cp*/*Cv*)。

**数据类型：** `double`

### **To** — 静温标量

静温，指定为标量。

**数据类型：** `double`

### **Po** — 静压标量

静压，指定为标量。

**数据类型：** `double`

### **ρo** — 静密度标量

静密度，指定为标量。

**数据类型：** `double`
### 输出

### **θ** — 相对温度比标量

相对温度比 (*θ*)，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Theta**。

**数据类型：** `double`

### **sqrt(θ)** — 相对温度比的平方根标量

相对温度比的平方根 ( θ)，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Square root of theta**。

**数据类型：** `double`

### **δ** — 相对压力比标量

相对压力比，(*δ*)，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Delta**。

**数据类型：** `double`

### **σ** — 相对密度比标量

相对密度比，(*σ*)，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Sigma**。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)` (默认) | `English`

输入单位，指定为：

| Units | Tstatic | Pstatic | rho\_static |
| --- | --- | --- | --- |
| `Metric (MKS)` | Kelvin | Pascal | Kilograms per cubic meter |
| `English` | Degrees Rankine | Pound force per square inch | Slug per cubic foot |

#### 编程用法

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **Theta** — 相对温度比 `on` (默认) | `off`

选中时，该模块计算相对温度比 (*θ*)，并且静温是必需输入。

#### 编程用法

|  |
| --- |
| **模块参数**: `theta` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Square root of theta** — 相对温度比的平方根 `on` (默认) | `off`

选中时，该模块计算相对温度比的平方根 ( θ)，并且静温是必需输入。

#### 依赖关系

选中此复选框会启用 sqrt(θ) 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数**: `sq_theta` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Delta** — 相对压力比 `on` (默认) | `off`

选中时，该模块计算相对压力比 (*δ*)，并且静压是必需输入。

#### 编程用法

|  |
| --- |
| **模块参数**: `delta` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Sigma** — 相对密度比 `on` (默认) | `off`

选中时，该模块计算相对密度比 (*σ*)，并且静密度是必需输入。

#### 编程用法

|  |
| --- |
| **模块参数**: `sigma` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算相对大气比率

Relative Ratio 模块计算相对大气比率，包括相对温度比 (*θ*)、θ、相对压力比 (*δ*) 和相对密度比 (*σ*)。

*θ* 表示所选参考站处气流温度相对于海平面标准大气条件的比值：

θ=TT0.

*δ* 表示所选参考站处气流压力相对于海平面标准大气条件的比值：

δ=PP0.

*σ* 表示所选参考站处气流密度相对于海平面标准大气条件的比值：

σ=ρρ0.

Relative Ratio 模块图标显示从 **Units** 参数中选择的输入单位。
