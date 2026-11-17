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

### **Pts1** — 点坐标 *M*×2 矩阵

点坐标，指定为基于 1 的 [*x* *y*] 点坐标的 *M*×2 矩阵，其中 *M* 表示点的数量。

该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Pts2** — 点坐标 *M*×2 矩阵

点坐标，指定为基于 1 的 [*x* *y*] 点坐标的 *M*×2 矩阵，其中 *M* 表示点的数量。

该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Num** — 有效点数量 标量

要在 **Pts1** 和 **Pts2** 中找到的有效点数量，指定为标量。当您启用 **Allow variable-size signal input** 参数时，此端口出现。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **TForm** — 变换 3×2 矩阵 | 3×3 矩阵

变换，返回为 3×2 或 3×3 矩阵。该模块为变换矩阵输出的数据类型与 **Pts1** 和 **Pts2** 图像点相同。

#### 依赖关系

- 当 **Pts1** 和 **Pts2** 为 single 或 double 时，输出变换矩阵也将具有 single 或 double 数据类型。
- 当 **Pts1** 和 **Pts2** 图像为内置整数时，可以选择将变换矩阵数据类型设置为 `Single` 或 `Double`。

**数据类型：** `single` | `double`

### **Inlier** — 使用的点 *M*×1 向量

用于计算 `TForm` 的点，返回为 *M*×1 向量。

#### 依赖关系

- 当您启用 **Output Boolean signal indicating which point pairs are inliers** 参数时，**Inlier** 端口出现。

**数据类型：** `Boolean`

## 参数

### **Transformation type** — 变换类型 `Affine`（默认）| `Nonreflective similarity` | `Projective`

将变换类型指定为 `Nonreflective similarity`、`Affine` 或 `Projective`。有关更详细的讨论，请参阅 Transformations。

#### 依赖关系

您可以根据变换类型设置其他参数：

- 对于 `Projective` 变换，您可以指定用于确定内点的标量代数距离阈值。
- 对于 `Affine` 或 `Nonreflective similarity` 变换，您可以指定用于确定内点的距离阈值（以像素为单位）。

### **Find and exclude outliers** — 查找并排除离群值 on（默认）| off

启用以从输入点中查找并排除离群值，并仅使用内点来计算变换矩阵。当您关闭此参数时，所有输入点都用于计算变换矩阵。

### **Method** — 查找离群值的方法 `RANdom SAmple Consensus (RANSAC)`（默认）| `Least Median of Squares`

选择查找离群值的方法为 `RANdom SAmple Consensus (RANSAC)` 或 `Least Median of Squares`。有关更详细的讨论，请参阅 RANSAC and Least Median Squares Algorithms。

#### 依赖关系

当您启用 **Find and exclude outliers** 复选框时，此参数出现。

### **Algebraic distance threshold for determining inliers** — 用于确定内点的代数距离阈值 1.5（默认）| 标量

指定用于确定内点的标量阈值。该阈值控制用于在 RANSAC 算法中查找代数距离的上限。

#### 依赖关系

当您将 **Method** 参数设置为 `Random Sample Consensus (RANSAC)` 并将 **Transformation type** 参数设置为 `Projective` 时，此参数出现。

### **Distance threshold for determining inliers (in pixels)** — 用于确定内点的距离阈值（以像素为单位）`1.5`（默认）| 标量

指定一个点与其对应点的投影位置之间可以相差的最大距离。

#### 依赖关系

当您将 **Method** 参数设置为 `Random Sample Consensus (RANSAC)` 并将 **Transformation type** 参数的值设置为 `Nonreflective similarity` 或 `Affine` 时，此参数出现。

### **Determine number of random samplings using** — 确定随机采样次数的方式 `Specified value`（默认）| `Desired confidence`

选择 `Specified value` 以输入随机采样次数的正整数值。选择 `Desired confidence` 以将随机采样次数设置为百分比和最大数量。

#### 依赖关系

当您选中 **Find and exclude outliers** 复选框，并将 **Method** 参数的值设置为 `Random Sample Consensus (RANSAC)` 时，此参数出现。

### **Number of random samplings** — 随机采样次数 `500`（默认）| 标量

指定算法要执行的随机采样次数。

#### 依赖关系

当您将 **Determine number of random samplings using** 参数的值设置为 `Specified value` 时，此参数出现。

### **Desired confidence (in %)** — 期望置信度（以 % 为单位）`99`（默认）| 标量

通过输入 `0` 到 `100` 之间的数字来指定期望置信度的百分比。该值表示算法找到可以通过变换矩阵映射的最大点组的概率。

#### 依赖关系

当您将 **Determine number of random samplings using** 参数设置为 `Desired confidence` 时，此参数出现。

### **Maximum number of random samplings** — 最大随机采样次数 `1000`（默认）| 整数

指定最大随机采样次数的整数值。

#### 依赖关系

当您将 **Method** 参数设置为 `Random Sample Consensus (RANSAC)` 并将 **Determine number of random samplings using** 参数的值设置为 `Desired confidence` 时，此参数出现。

### **Stop sampling earlier when a specified percentage of point pairs are determined to be inlier** — 提前停止采样 off（默认）| on

启用此参数以在找到一定百分比的输入点为内点时停止随机采样。

#### 依赖关系

当您将 **Method** 参数设置为 `Random Sample Consensus (RANSAC)` 时，此参数出现。

### **Perform additional iterative refinement of the transformation matrix** — 执行变换矩阵的额外迭代细化 off（默认）| on

指定是否对变换矩阵执行细化。

#### 依赖关系

当您选中 **Find and exclude outliers** 复选框时，此参数出现。

### **Output Boolean signal indicating which point pairs are inliers** — 输出布尔信号 off（默认）| on

启用此参数以输出用于计算变换矩阵的内点点对。

#### 依赖关系

- 当您选中 **Find and exclude outliers** 复选框时，此参数出现。
- 该模块不会将此参数用于有符号或 double 数据类型的点。

### **When Pts1 and Pts2 are built-in integers, set transformation matrix date type to** — 设置变换矩阵数据类型 `Single`（默认）| `Double`

当输入点为内置整数时，将变换矩阵数据类型指定为 `Single` 或 `Double`。

#### 依赖关系

该模块不会将此参数用于有符号或 double 数据类型的点。

### **Allow variable-sized signal input** — 允许可变大小信号输入 on（默认）| off

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
| a 当您将 FFT implementation 参数设置为 FFTW，或当变换长度不是 2 的幂时，生成的代码将限制在 MATLAB 主机计算机上。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2008a 中引入**

## 描述

从匹配点对估计几何变换

使用 Estimate Geometric Transformation 模块查找将两幅图像之间最多数量的点对进行映射的变换矩阵。*点对* 是指输入图像中的一个点及其在使用变换矩阵创建的图像上的相关点。您可以选择使用 RANdom SAmple Consensus (RANSAC) 或 Least Median Squares 算法来排除离群值并计算变换矩阵。您也可以使用所有输入点来计算变换矩阵。
