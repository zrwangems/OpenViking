---
type: simulink-block
title: '1D Self-Conditioned [A(v),B(v),C(v),D(v)]'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Control'
documentation_page: '1dselfconditionedavbvcvdv'
documentation_source_path: '1dselfconditionedavbvcvdv.html'
language: zh-CN
chinese_source: worker-translation
---

# 1D Self-Conditioned [A(v),B(v),C(v),D(v)]

## 端口

### 输入

### **y** — 飞机测量向量

飞机测量，指定为向量。

**数据类型：** `double`

### **v** — 调度变量向量

调度变量，指定为向量，按状态空间矩阵的维度排序。

**数据类型：** `double`

### **u\_meas** — 测量的作动器位置向量

测量的作动器位置，指定为向量。

**数据类型：** `double`
### 输出

### **u\_dem** — 作动器需求向量

作动器需求，指定为向量。

**数据类型：** `double`

## 参数

### **A 矩阵(v)** — 状态空间实现的 *A* 矩阵 `A`（默认）| array

状态空间实现的 *A* 矩阵。*A* 矩阵应具有三个维度，最后一个维度对应调度变量 *v*。例如，如果对应于 *v* 第一个元素的 *A* 矩阵是单位矩阵，则 `A(:,:,1) = [1 0;0 1];`。

#### 编程用法

|  |
| --- |
| **模块参数**: `A` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'A'` |

### **B 矩阵(v)** — 状态空间实现的 *B* 矩阵 `B`（默认）| array

状态空间实现的 *B* 矩阵。*B* 矩阵应具有三个维度，最后一个维度对应调度变量 *v*。例如，如果对应于 *v* 第一个元素的 *B* 矩阵是单位矩阵，则 `B(:,:,1) = [1 0;0 1];`。

#### 编程用法

|  |
| --- |
| **模块参数**: `B` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'B'` |

### **C 矩阵(v)** — 状态空间实现的 *C* 矩阵 `C`（默认）| array

状态空间实现的 *C* 矩阵。*C* 矩阵应具有三个维度，最后一个维度对应调度变量 *v*。例如，如果对应于 *v* 第一个元素的 *C* 矩阵是单位矩阵，则 `C(:,:,1) = [1 0;0 1];`。

#### 编程用法

|  |
| --- |
| **模块参数**: `C` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'C'` |

### **D 矩阵(v)** — 状态空间实现的 *D* 矩阵 `D`（默认）| array

状态空间实现的 *D* 矩阵。*D* 矩阵应具有三个维度，最后一个维度对应调度变量 *v*。例如，如果对应于 *v* 第一个元素的 *D* 矩阵是单位矩阵，则 `D(:,:,1) = [1 0;0 1];`。

#### 编程用法

|  |
| --- |
| **模块参数**: `D` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'D'` |

### **调度变量断点** — 调度变量 `v_vec` 的断点（默认）| vector

第一个调度变量的断点向量。*v* 的长度应与 *A*、*B*、*C* 和 *D* 的第三维大小相同。

#### 编程用法

|  |
| --- |
| **模块参数**: `breakpoints_v` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'v_vec'` |

### **初始状态, x\_initial** — 初始状态 `0`（默认）| vector

控制器的初始状态向量，即状态向量 *x* 的初始值。其长度应等于 *A* 的第一维大小。

#### 编程用法

|  |
| --- |
| **模块参数**: `x_initial` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'0'` |

### **A(v)-H(v)\*C(v) 的极点** — 期望极点 `[-5 -2]`（默认）| vector

*A*-*HC* 的期望极点，指定为向量。对于调度参数 *v* 的所有值，极点均分配到相同位置。因此，定义的极点位置数应等于 *A* 矩阵的第一维长度。

#### 编程用法

|  |
| --- |
| **模块参数**: `vec_w` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'[-5 -2]'` |

## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

实现取决于一个调度参数的、自条件形式的增益调度状态空间控制器

1D Self-Conditioned [A(v),B(v),C(v),D(v)] 模块实现如算法中定义的增益调度状态空间控制器。

此模块的输出是作动器需求，您可以将其输入到作动器模块。
