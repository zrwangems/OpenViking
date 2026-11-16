---
type: simulink-block
title: 'Estimate Geometric Transformation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'estimategeometrictransformation'
documentation_source_path: 'ref/estimategeometrictransformation.html'
language: zh-CN
chinese_source: worker-translation
---

# Estimate Geometric Transformation

## 端口

### 输入

### **Pts1** — 点坐标 *M*-by-2 矩阵

点坐标，指定为一个 *M*-by-2 矩阵，其中包含基于 1 的 [*x* *y*] 点坐标，其中 *M* 表示点数。

该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Pts2** — 点坐标 *M*-by-2 矩阵

点坐标，指定为一个 *M*-by-2 矩阵，其中包含基于 1 的 [*x* *y*] 点坐标，其中 *M* 表示点数。

该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Num** — 有效点数量 标量

要在 **Pts1** 和 **Pts2** 中查找的有效点数量，指定为标量。当您启用 **允许可变大小信号输入** 参数时，此端口出现。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **TForm** — 变换 3-by-2 矩阵 | 3-by-3 矩阵

变换，以 3-by-2 矩阵或 3-by-3 矩阵形式返回。该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

#### 依赖关系

- 当 **Pts1** 和 **Pts2** 为 single 或 double 时，输出的变换矩阵也将具有 single 或 double 数据类型。
- 当 **Pts1** 和 **Pts2** 图像为内置整数时，可以选择将变换矩阵数据类型设置为 `Single` 或 `Double`。

**数据类型：** `single` | `double`

### **Inlier** — 使用的点 *M*-by-1 向量

用于计算 `TForm` 的点，以 *M*-by-1 向量形式返回。

#### 依赖关系

- 当您启用 **输出指示哪些点对为内点的 Boolean 信号** 参数时，**Inlier** 端口出现。

**数据类型：** `Boolean`

## 参数

### **变换类型** — 变换类型 `Affine` (默认) | `Nonreflective similarity` | `Projective`

将变换类型指定为 `Nonreflective similarity`、`Affine` 或 `Projective`。有关更详细的讨论，请参阅变换。

#### 依赖关系

您可以根据变换类型设置其他参数：

- 对于 `Projective` 变换，您可以指定用于确定内点的标量代数距离阈值。
- 对于 `Affine` 或 `Nonreflective similarity` 变换，您可以指定用于确定内点的距离阈值（以 pixels 为单位）。

### **查找并排除离群点** — 查找并排除离群点 on (默认) | off

启用以查找并排除输入点中的离群点，并仅使用内点计算变换矩阵。当您关闭此参数时，将使用所有输入点计算变换矩阵。

### **方法** — 查找离群点的方法 `RANdom SAmple Consensus (RANSAC)` (默认) | `Least Median of Squares`

选择查找离群点的方法为 `RANdom SAmple Consensus (RANSAC)` 或 `Least Median of Squares`。有关更详细的讨论，请参阅 RANSAC 和 Least Median Squares 算法。

#### 依赖关系

当您启用 **查找并排除离群点** 复选框时，此参数出现。

### **用于确定内点的代数距离阈值** — 用于确定内点的代数距离阈值 1.5 (默认) | 标量

指定用于确定内点的标量阈值。该阈值控制 RANSAC 算法中用于查找代数距离的上限。

#### 依赖关系

当您将 **方法** 参数设置为 `Random Sample Consensus (RANSAC)`，并将 **变换类型** 参数设置为 `Projective` 时，此参数出现。

### **用于确定内点的距离阈值（以 pixels 为单位）** — 用于确定内点的距离阈值（以 pixels 为单位） `1.5` (默认) | 标量

指定一个点与其对应点的投影位置之间可允许差异的距离上限。

#### 依赖关系

当您将 **方法** 参数设置为 `Random Sample Consensus (RANSAC)`，并将 **变换类型** 参数的值设置为 `Nonreflective similarity` 或 `Affine` 时，此参数出现。

### **用于确定随机采样数的方式** — 用于确定随机采样数的方式 `Specified value` (默认) | `Desired confidence`

选择 `Specified value` 可输入随机采样数的正整数值。选择 `Desired confidence` 可将随机采样数设置为百分比和最大数量。

#### 依赖关系

当您选中 **查找并排除离群点** 复选框，并将 **方法** 参数的值设置为 `Random Sample Consensus (RANSAC)` 时，此参数出现。

### **随机采样数** — 随机采样数 `500` (默认) | 标量

指定算法要执行的随机采样数。

#### 依赖关系

当您将 **用于确定随机采样数的方式** 参数的值设置为 `Specified value` 时，此参数出现。

### **期望置信度（以 % 为单位）** — 期望置信度（以 % 为单位） `99` (默认) | 标量

通过输入 `0` 到 `100` 之间的数字来指定期望置信度百分比。该值表示算法找到可由变换矩阵映射的最大点组的概率。

#### 依赖关系

当您将 **用于确定随机采样数的方式** 参数设置为 `Desired confidence` 时，此参数出现。

### **最大随机采样数** — 最大随机采样数 `1000` (默认) | integer

指定最大随机采样数的整数值。

#### 依赖关系

当您将 **方法** 参数设置为 `Random Sample Consensus (RANSAC)`，并将 **用于确定随机采样数的方式** 参数的值设置为 `Desired confidence` 时，此参数出现。

### **当指定百分比的点对确定为内点时提前停止采样** — 停止采样 off (默认) | on

启用此参数可在已找到一定百分比的输入点作为内点时停止随机采样。

#### 依赖关系

当您将 **方法** 参数设置为 `Random Sample Consensus (RANSAC)` 时，此参数出现。

### **对变换矩阵执行额外的迭代细化** — 执行额外的迭代细化 off (默认) | on

指定是否对变换矩阵执行细化。

#### 依赖关系

当您选中 **查找并排除离群点** 复选框时，此参数出现。

### **输出指示哪些点对为内点的 Boolean 信号** — 输出 Boolean 信号 off (默认) | on

启用此参数可输出用于计算变换矩阵的内点点对。

#### 依赖关系

- 当您选中 **查找并排除离群点** 复选框时，此参数出现。
- 对于 signed 或 double 数据类型的点，该模块不会使用此参数。

### **当 Pts1 和 Pts2 为内置整数时，将变换矩阵数据类型设置为** — 设置变换矩阵数据类型 `Single` (默认) | `Double`

当输入点为内置整数时，将变换矩阵数据类型指定为 `Single` 或 `Double`。

#### 依赖关系

对于 signed 或 double 数据类型的点，该模块不会使用此参数。

### **允许可变大小信号输入** — 允许可变大小信号输入 on (默认) | off

启用此参数以允许可变大小信号输入。

#### 依赖关系

## 所属库

Computer Vision Toolbox / Geometric Transformations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integera` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 当您将 FFT implementation 参数设置为 FFTW，或者变换长度不是 2 的幂时，生成的代码将仅限于 MATLAB 宿主计算机。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2008a 中引入**

## 描述

从匹配点对估计几何变换

使用 Estimate Geometric Transformation 模块查找可在两幅图像之间映射最多点对的变换矩阵。*点对* 指输入图像中的点以及使用变换矩阵创建的图像上的其关联点。您可以选择使用 RANdom SAmple Consensus (RANSAC) 或 Least Median Squares 算法来排除离群点并计算变换矩阵。您也可以使用所有输入点计算变换矩阵。
