---
type: simulink-block
title: 'Aerodynamic Forces and Moments'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Aerodynamics'
documentation_page: 'aerodynamicforcesandmoments'
documentation_source_path: 'aerodynamicforcesandmoments.html'
language: zh-CN
chinese_source: worker-translation
---

# Aerodynamic Forces and Moments

## 端口

### 输入

### **Coef** — 气动系数六元素向量

用于力和力矩的气动系数（在所选输入轴中），指定为向量。这些系数根据轴的选择排列成向量：

| 输入轴 | 输入向量 |
| --- | --- |
| Body | （轴向力 *C*x，侧向力 *C*y，法向力 *C*z，滚转力矩 *C*l，俯仰力矩 *C*m，偏航力矩 *C*n） |
| Stability | （阻力 *C*D(β=0)，侧向力 *C*y，升力 *C*L，滚转力矩 *C*l，俯仰力矩 *C*m，偏航力矩 *C*n） |
| Wind | （阻力 *C*D，侧风力 *C*c，升力 *C*L，滚转力矩 *C*l，俯仰力矩 *C*m，偏航力矩 *C*n） |

**数据类型：** `double`

### **qbar** — 动压标量 | 三元素向量

动压，指定为 1×3 数组。

**数据类型：** `double`

### **CG** — 重心三元素向量

重心，指定为 1×3 向量。

**数据类型：** `double`

### **CP** — 压力中心三元素向量

压力中心，指定为 1×3 向量。只要模型的其余部分反映对力矩参考点的使用，这也可以视为任意通用力矩参考点。

**数据类型：** `double`

### **Vb** — 机体轴中的速度三元素向量

机体轴中的速度。指定为 1×3 向量。

#### 依赖关系

如果 **输入轴** 参数设置为 `Wind` 或 `Stability`，则启用此端口。

**数据类型：** `double`
### 输出

### **F** — 气动力三元素向量

气动力（在所选输出轴中），返回为三元素向量，在重心处沿 *x* 轴、*y* 轴和 *z* 轴。

**数据类型：** `double`

### **M** — 气动力矩三元素向量

气动力矩（在所选输出轴中），返回为三元素向量，在重心处沿 *x* 轴、*y* 轴和 *z* 轴。

**数据类型：** `double`

## 参数

### **输入轴** — 输入系数的坐标系 `Body`（默认） | `Stability` | `Wind`

输入系数的坐标系，指定为 `Body`（默认）、`Stability` 或 `Wind`。

#### 依赖关系

选择 `Stability` 或 `Wind` 会启用输入端口 Port\_5。

#### 编程用法

|  |
| --- |
| **模块参数**: `inputAxes` |
| **类型**: character vector |
| **值**: `'Body'` | `'Stability'` | `'Wind'` |
| **默认值**: `'Body'` |

### **力轴** — 气动力坐标系 `Body`（默认） | `Stability` | `Wind`

气动力坐标系，指定为 `Body`（默认）、`Stability` 或 `Wind`。

#### 依赖关系

选择 `Stability` 或 `Wind` 会启用输入端口 Port\_5。

#### 编程用法

|  |
| --- |
| **模块参数**: `outputForcesAxes` |
| **类型**: character vector |
| **值**: `'Body'` | `'Stability'` | `'Wind'` |
| **默认值**: `'Body'` |

### **力矩轴** — 气动力矩坐标系 `Body`（默认） | `Stability` | `Wind`

气动力矩坐标系，指定为 `Body`（默认）、`Stability` 或 `Wind`。

#### 依赖关系

选择 `Stability` 或 `Wind` 会启用输入端口 Port\_5。

#### 编程用法

|  |
| --- |
| **模块参数**: `outputMomentAxes` |
| **类型**: character vector |
| **值**: `'Body'` | `'Stability'` | `'Wind'` |
| **默认值**: `'Body'` |

### **参考面积** — 参考面积 `1`（默认） | 任意 double 值

用于计算气动力和力矩的参考面积，指定为任意 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**: `S` |
| **类型**: character vector |
| **值**: 任意 double 值 |
| **默认值**: `'1'` |

### **参考展长** — 参考展长 `1`（默认） | 任意 double 值

用于计算 *x* 轴和 *z* 轴中气动力矩的参考展长，指定为任意 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**: `b` |
| **类型**: character vector |
| **值**: 任意 double 值 |
| **默认值**: `'1'` |

### **参考长度** — 参考长度 `1`（默认） | 任意 double 值

用于计算 *y* 轴中气动力矩的参考长度，指定为任意 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**: `cbar` |
| **类型**: character vector |
| **值**: 任意 double 值 |
| **默认值**: `'1'` |

## 所属库

Aerospace Blockset / Aerodynamics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用气动系数、动压、重心、压力中心和速度计算气动力和力矩

Aerodynamic Forces and Moments 模块计算绕重心的气动力和气动力矩。

Aerodynamic Forces and Moments 模块的端口标签会根据从 **输入轴**、**力轴** 和 **力矩轴** 列表中选择的坐标系而变化。
