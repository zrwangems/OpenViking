---
type: simulink-block
title: 'Matrix Interpolation'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Additional Lookup Tables'
documentation_page: 'matrixinterpolation'
documentation_source_path: '../simulink/ref_extras/matrixinterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Interpolation

## 端口

### 输入

### **k1** — 表的第一个维度的索引 `k1` 标量

表的第一个维度的索引 `k1`。

**数据类型：** `single` | `double`

### **f1** — 表的第一个维度的小数 `f1` 标量

表的第一个维度的小数 `f1`。

**数据类型：** `single` | `double`

### **kn** — 表的第 n 个维度的索引 `kn` 标量

表的第 n 个维度的索引 `kn`。

**数据类型：** `single` | `double`

### **fn** — 表的第 n 个维度的小数 `fn` 标量

表的第 n 个维度的小数 `fn`。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — N 维函数的近似值 标量 | 向量 | 矩阵 | N 维数组

N 维函数的近似值，通过使用输入索引 `k` 和小数 `f` 的值对表数据进行插值（或外插）计算得出。

**数据类型：** `single` | `double`

## 参数

### **Interpolation method** — 插值方法 `Linear`（默认）| `Nearest` | `Flat`

选择如何在断点之间对表数据进行插值。选择 `Flat`、`Nearest` 或 `Linear`。有关详细信息，请参阅插值方法。

#### 编程使用

|  |
| --- |
| **模块参数**：`InterpMethod` |
| **类型**：character vector |
| **值**：`'Flat' | 'Nearest' | 'Linear'` |
| **默认值**：`'Linear'` |

### **Extrapolation method** — 外插方法 `Clip`（默认）| `Linear`

如果输入中的索引 *k* 和小数 *f* 超出断点范围，选择如何对表数据进行外插。选择 `Clip` 或 `Linear`。有关详细信息，请参阅外插方法。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExtrapMethod` |
| **类型**：character vector |
| **值**：`'Clip' | 'Linear'` |
| **默认值**：`'Clip'` |

### **Interpolate Dimension** — 查找表的维度数 `1`（默认）| `2` | `3`

通过指定 `1` 到 `3` 之间的整数来输入查找表的维度数。此参数决定：

- 表的自变量数量以及模块输入的数量。
- 要指定的断点输入集数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`InterpolateDimension` |
| **类型**：character vector |
| **值**：`'1' | '2' | '3'` |
| **默认值**：`'1'` |

### **Table data** — 输出值表 `1:1:10`（默认）| 向量 | 矩阵 | N 维数组

输入输出值表。表数据的维度数必须等于断点维度数与矩阵维度数之和，因为对于此模块，每个数据点都是一个矩阵。

有关如何在 MATLAB® 中构造多维数组的信息，请参阅多维数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`TableData` |
| **类型**：character vector |
| **值**：vector | matrix | N-D array |
| **默认值**：`'1:1:10'` |

### **Simulate using** — 仿真模式 `Code generation` | `Interpreted execution`

选择仿真模式。

- `Code generation` — 在首次模型运行时，使用仅支持代码生成的 MATLAB 函数对 MATLAB System 模块进行仿真并生成代码。如果模块的结构不变，后续模型运行不会重新生成代码。

  如果仿真模式为 `Code generation`，系统对象最多接受 32 个输入。
- `Interpreted execution` — 使用所有支持的 MATLAB 函数对模型进行仿真。选择此选项可能会降低仿真性能。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：character vector |
| **值**：`'Code generation' | 'Interpreted execution'` |
| **默认值**：`'Code generation'` |

## 所属库

Simulink Extras / Additional Lookup Tables

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

在矩阵之间进行插值

Matrix Interpolation 模块通过使用预先计算好的索引和分数值，对 N 维表执行插值（或外插）。每个数据点可以是一个矩阵。它支持最多三个断点维度的插值。如果你为断点指定 *n* 个维度，并且表中的每个数据点是一个具有 *m* 个维度的矩阵，那么你的表数据维度数量为 *m+n*。表数据的最后 *n* 个维度必须是每个插值维度中断点的长度。矩阵的前 *m* 个维度各自是一个数据点。
