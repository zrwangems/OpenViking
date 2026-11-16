---
type: simulink-block
title: '1D Controller [A(v),B(v),C(v),D(v)]'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Control'
documentation_page: '1dcontrolleravbvcvdv'
documentation_source_path: '1dcontrolleravbvcvdv.html'
language: zh-CN
chinese_source: worker-translation
---

# 1D Controller [A(v),B(v),C(v),D(v)]

## 端口

### 输入

### **y** — 飞机测量值向量

飞机测量值，指定为向量。

**数据类型：** `double`

### **v** — 调度变量向量

调度变量，指定为向量，且符合状态空间矩阵的维度。

**数据类型：** `double`
### 输出

### **u** — 作动器需求向量

作动器需求，指定为向量。

**数据类型：** `double`

## 参数

### **A 矩阵(v)** — 状态空间实现的 *A* 矩阵 `A1` (默认) | array

状态空间实现的 *A* 矩阵，指定为数组。在一维调度情况下，*A* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果 *v* 的第一个条目对应的 *A* 矩阵是单位矩阵，则 `A(:,:,1) = [1 0;0 1];`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `A` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'A1'` |

### **B 矩阵(v)** — 状态空间实现的 *B* 矩阵 `B1` (默认) | array

状态空间实现的 *B* 矩阵，指定为数组。在一维调度情况下，*B* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果 *v* 的第一个条目对应的 *B* 矩阵是单位矩阵，则 `B(:,:,1) = [1 0;0 1];`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `B` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'B1'` |

### **C 矩阵(v)** — 状态空间实现的 *C* 矩阵 `C1` (默认) | array

状态空间实现的 *C* 矩阵，指定为向量。在一维调度情况下，*C* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果 *v* 的第一个条目对应的 *C* 矩阵是单位矩阵，则 `C(:,:,1) = [1 0;0 1];`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `C` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'C1'` |

### **D 矩阵(v)** — *D* `D1` (默认) | array

状态空间实现的 *D* 矩阵，指定为数组。在一维调度情况下，*D* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果 *v* 的第一个条目对应的 *D* 矩阵是单位矩阵，则 `D(:,:,1) = [1 0;0 1];`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `D` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'D1'` |

### **调度变量断点** — 调度变量 `v_vec` 的断点 (默认) | vector

调度变量的断点，指定为向量。*v* 的长度必须与 *A*、*B*、*C* 和 *D* 的第三维大小相同。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AoA_vec` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'v_vec'` |

### **初始状态, x_initial** — 初始状态 `0` (默认) | vector

控制器的初始状态，例如状态向量 *x* 的初始值，指定为向量。向量的长度必须等于 *A* 的第一维大小。

#### 程序化使用

|  |
| --- |
| **模块参数**: `x_initial` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'0'` |

## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

实现取决于一个调度参数的增益调度状态空间控制器

1D Controller [A(v),B(v),C(v),D(v)] 模块实现一个增益调度状态空间控制器，如算法中所述。

此模块的输出是作动器需求，您可以将其输入到作动器模块。
