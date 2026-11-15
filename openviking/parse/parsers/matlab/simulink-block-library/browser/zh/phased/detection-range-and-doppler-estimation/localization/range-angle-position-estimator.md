---
type: simulink-block
title: 'Range-Angle Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Localization'
documentation_page: 'rangeanglepositionestimator'
documentation_source_path: 'ref/rangeanglepositionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Range-Angle Position Estimator

## 端口

### 输入

### **RngEst** — 距离测量（meters）实值 1-by-*K* 向量 | 实值 *J*-by-*L* 矩阵

双基地距离或距离和测量，指定为实值 1-by-*K* 向量或实值 *J*-by-*L* 矩阵。

- 当 **RngEst** 为实值 1-by-*K* 向量时，该测量表示针对 *K* 个目标在一个发射锚点和一个接收锚点处测得的双基地距离或距离和测量。
- 当 **RngEst** 为实值 *J*-by-*L* 矩阵时，该测量表示在 *J* 个发射锚点和 *L* 个接收锚点处测得的双基地距离或距离和测量。

单位是 meters。

**示例：** `[1000 2000]`

**数据类型：** `single` | `double`

### **AngEst** — 到达角估计（degrees）实值 1-by-*L* 行向量 | 实值 2-by-*L* 矩阵

- 当 **RngEst** 为实值 *J*-by-*L* 矩阵时，`angest` 应为实值长度为 *L* 的行向量或 2-by-*L* 矩阵。当 **AngEst** 为行向量时，它表示在 *L* 个接收锚点处测得的方位角。当 **AngEst** 为矩阵时，其第一行表示方位角，第二行表示在 *L* 个接收锚点处测得的仰角。
- 当 **RngEst** 为实值 1-by-*K* 向量时，**AngEst** 应为实值 *K* 元素行向量或 2-by-*K* 矩阵。

**示例：** `[10 20]`

**数据类型：** `single` | `double`

### **RngVar** — 距离方差（meters-squared）`[]`（默认）| 正实值 *J*-by-*L* 矩阵 | 正实值长度为 *K* 的行向量

距离方差，指定为空矩阵或正实值 *J*-by-*L* 矩阵或正实值长度为 *K* 的行向量。当 **RngVar** 为空时，方差估计未知，并且对于所有目标均设为一。

- 当 **RngVar** 为 *J*-by-*L* 矩阵时，它表示在 *J*-*L* 个锚点对处测得的目标的双基地距离或距离和估计的方差。当 **RngVar** 为空时，方差估计未知，并且对于所有锚点对均设为单位值。单位是 meters-squared。
- 当 **RngVar** 为长度为 K 的向量时，它表示在一个锚点对处测得的 *K* 个目标的双基地距离或距离和估计的方差。

**示例：** `[10 15]`

#### 依赖关系

要启用此端口，请选中 **Enable known variance input** 复选框。

**数据类型：** `single` | `double`

### **AngVar** — 角度方差（degrees-squared）`[]` | 实值 1-by-*L* 行向量 | 实值 2-by-*L* 矩阵

角度测量方差，指定为空、实值 1-by-*L* 行向量或正实值 2-by-*L* 矩阵。当 **AngVar** 为向量时，它表示在 *L* 个接收锚点处测得的目标的方位角方差估计。当 **AngVar** 为矩阵时，它表示在 *L* 个接收锚点处测得的目标的角度方差估计。当 **AngVar** 为空时，方差估计未知，并且对于所有 *L* 个接收锚点均设为一。当测量准确时，我们可以将对应方差设为空。

**示例：** `[.10 .15]`

#### 依赖关系

要启用此端口，请选中 **Enable known variance input** 复选框。

**数据类型：** `single` | `double`

### **AnchorPos** — 锚点位置（meters）实值 *Q*-by-*J* 矩阵

锚点位置，指定为实值 *Q*-by-*J* 矩阵。*J* 是锚点数量。每列表示不同锚点的位置。位置可以是二维或三维。对于二维位置，*Q=2*；对于三维位置，*Q=3*。`txpos` 的第 *j* 列表示第 *j* 个发射器在 *Q* 维笛卡尔空间中的位置。单位是 meters。

**示例：** `[20 31 –16; 13 64 –44]`

**数据类型：** `single` | `double`
### 输出

### **TgtPosEst** — 目标位置估计（meters）实值 *Q*-by-1 向量

目标位置估计，返回为实值 *Q*-by-1 向量或实值 *Q*-by-*K* 矩阵，表示估计的 *K* 个目标位置。单位是 meters。

**数据类型：** `single` | `double`

### **TgtPosCov** — 估计的目标位置协方差（meters-squared）实值 *Q*-by-*Q* 矩阵 | 实值 *Q*-by-*Q*-by-*K* 数组

当输入包含一个目标的 *JL* 个锚点对时，`tgtposcov` 为 *Q*-by-*Q* 矩阵，它是实值半正定对称矩阵，表示估计的目标位置协方差。当输入包含 *K* 个目标的 1 个锚点对时，`tgtposcov` 为 *Q*-by-*Q*-by-*K* 数组，其中每页是实值半正定对称矩阵，表示估计的目标位置协方差。单位是 meters-squared。

#### 依赖关系

要启用此端口，请选中 **Output covariances of position estimates** 复选框。

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，于 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Enable known variance input** — 启用已知方差输入 on（默认）| off

选中此复选框以允许来自 **RngVar** 和 **AngVar** 端口的输入。

**数据类型：** `Boolean`

### **Output covariances of position estimates** — 输出位置估计的协方差 off（默认）| on

选中此复选框以从 **TgtPosCov** 端口输出位置协方差估计。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行该模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但是如果您更改任何模块参数，则该模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用距离-角度测量估计目标位置

Range-Angle Position Estimator 模块使用距离-角度测量估计目标位置。
