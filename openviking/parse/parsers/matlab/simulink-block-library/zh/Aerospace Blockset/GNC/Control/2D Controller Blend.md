---
type: simulink-block
title: '2D Controller Blend'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: '2dcontrollerblend'
documentation_source_path: '2dcontrollerblend.html'
language: zh-CN
chinese_source: worker-translation
---

# 2D Controller Blend

## 端口

### 输入

### **y** — 飞行器测量向量

飞行器测量值，指定为向量。

**数据类型：** `double`

### **v1** — 调度变量向量

调度变量，指定为向量，其维度与状态空间矩阵的维度一致。

**数据类型：** `double`

### **v2** — 调度变量向量

调度变量，指定为向量，其维度与状态空间矩阵的维度一致。

**数据类型：** `double`
### 输出

### **u** — 作动器需求向量

作动器需求，指定为向量。

**数据类型：** `double`

## 参数

### **A-matrix(v1,v2)** — 状态空间实现的 *A* 矩阵 A（默认）| 数组

状态空间实现的 *A* 矩阵。在二维混合的情况下，*A* 矩阵应具有四个维度，最后两个维度对应于调度变量 *v*1 和 *v*2。例如，如果对应于 *v*1 的第一个条目和 *v*2 的第一个条目的 *A* 矩阵为单位矩阵，则 `A(:,:,1,1) =
[1 0;0 1];`。

#### 编程使用

|  |
| --- |
| **模块参数**：`A` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'A'` |

### **B-matrix(v1,v2)** — 状态空间实现的 *B* 矩阵 A（默认）| 数组

状态空间实现的 *B* 矩阵。*B* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果对应于 *v* 的第一个条目的 *B* 矩阵为单位矩阵，则 `B(:,:,1) = [1
0;0 1];`。

#### 编程使用

|  |
| --- |
| **模块参数**：`B` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'B'` |

### **C-matrix(v1,v2)** — 状态空间实现的 *C* 矩阵 C（默认）| 数组

状态空间实现的 *C* 矩阵。*C* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果对应于 *v* 的第一个条目的 *C* 矩阵为单位矩阵，则 `C(:,:,1) = [1
0;0 1];`。

#### 编程使用

|  |
| --- |
| **模块参数**：`C` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'C'` |

### **D-matrix(v1,v2)** — 状态空间实现的 *D* 矩阵 C（默认）| 数组

状态空间实现的 *D* 矩阵。*D* 矩阵应具有三个维度，最后一个维度对应于调度变量 *v*。例如，如果对应于 *v* 的第一个条目的 *D* 矩阵为单位矩阵，则 `D(:,:,1) = [1
0;0 1];`。

#### 编程使用

|  |
| --- |
| **模块参数**：`D` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'D'` |

### **First scheduling variable (v1) breakpoints** — 第一个调度变量的断点 `v1_vec`（默认）| 向量

第一个调度变量的断点，指定为向量。*v*1 的长度应与 *A*、*B*、*C* 和 *D* 的第三维大小相同。

#### 编程使用

|  |
| --- |
| **模块参数**：`breakpoints_v1` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'v1_vec'` |

### **Second scheduling variable (v2) breakpoints** — 第二个调度变量的断点 `v2_vec`（默认）| 向量

第二个调度变量的断点，指定为向量。*v*2 的长度应与 *A*、*B*、*C* 和 *D* 的第四维大小相同。

#### 编程使用

|  |
| --- |
| **模块参数**：`breakpoints_v2` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'v2_vec'` |

### **Initial state, x\_initial** — 初始状态 `0`（默认）| 向量

控制器的初始状态向量，即状态向量 *x* 的初始值。其长度应等于 *A* 的第一维大小。

#### 编程使用

|  |
| --- |
| **模块参数**：`x_initial` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'0'` |

### **Poles of A(v)-H(v)\*C(v)** — 期望极点 `[-5 -2]`（默认）

对于即将接入的控制器，使用类似观测器的结构来确保控制器输出跟踪当前模块输出 *u*。观测器的极点在此对话框中定义为向量，极点数量等于 *A* 矩阵的维度。极点过快会导致传感器噪声传播，极点过慢会导致控制器输出无法跟踪 *u*。

#### 编程使用

|  |
| --- |
| **模块参数**：`vec_w` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'[-5 -2]'` |

## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过对状态空间控制器输出的线性插值实现二维状态空间控制器向量

2D Controller Blend 模块实现一组状态空间控制器设计。这些控制器并行运行，其输出根据当前飞行条件或工作点进行插值。这种实现方法的优点是，各个控制器设计的状态空间矩阵 *A*、*B*、*C* 和 *D* 不需要从一个设计点到下一个设计点平滑变化。该模块的输出是作动器需求，您可以将其输入到作动器模块。

对于 2D Controller Blend 模块，在任意给定时刻，会更新九个控制器设计。

当调度参数的值变化且需要运行的控制器索引发生变化时，即将接入的控制器的状态通过使用为 Self-Conditioned [A,B,C,D] 模块定义的自条件形式进行初始化。
