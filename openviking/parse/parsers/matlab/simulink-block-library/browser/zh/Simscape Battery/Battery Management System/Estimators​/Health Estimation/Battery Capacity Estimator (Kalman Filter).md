---
type: simulink-block
title: 'Battery Capacity Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / Health Estimation'
documentation_page: 'batterycapacityestimatorkalmanfilter'
documentation_source_path: 'ref/batterycapacityestimatorkalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Capacity Estimator (Kalman Filter)

## 端口

### 输入

### **Current** — 电池电流，ampere 标量 | 向量

电池电流，以 ampere 为单位，指定为单个单体的标量或多个单体的向量。要将此输入指定为单体电流向量，请选择 **Specify Current input as cell current(s)** 参数。

### **CellSOC** — 单体荷电状态，无量纲标量 | 向量

一个或多个单体的荷电状态，指定为范围 [0, 1] 内条目的标量或向量。此输入端口的尺寸必须等于 **InitialCellAH** 输入端口的尺寸。

### **InitialCellAH** — 初始单体容量，A\*Hr 标量 | 向量

电池的初始单体容量，以 ampere-hour 为单位，指定为单个单体的标量或多个单体的向量。此输入端口的尺寸必须等于 **CellSOC** 输入端口的尺寸。

### 输出

### **CellAH** — 估计的单体容量 标量 | 向量

电池的估计单体容量，以 ampere-hour 为单位，以标量或向量形式返回。此输出端口的尺寸等于 **InitialCellAH** 输入端口的尺寸。

## 参数

### **Specify Current input as cell current(s)** — 用于将电流输入端口指定为向量的选项 `off`（默认） | `on`

用于将 **Current** 输入端口的值指定为单体电流向量的选项。如果选择此参数，则 **Current** 输入端口处的值可以是标量，也可以是大小等于模块输入大小的向量。

### **Filter type** — 卡尔曼滤波器类型 `Extended Kalman filter`（默认） | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池单体容量的卡尔曼滤波器类型。

### **Alpha** — Alpha 系数 `1`（默认） | [0, 1] 范围内的标量

控制 sigma 点散布的系数。该模块在其对无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器的方程实现中使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2`（默认） | 非负标量

与分布相关的系数。该模块在其对无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器的实现中使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0`（默认） | [0, 3] 范围内的标量

控制 sigma 点散布的系数。该模块在其对无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器的方程实现中使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声的协方差 `3e-4`（默认） | 标量

状态中噪声的协方差。

### **Covariance of the measurement noise, R** — 测量噪声的协方差 `5e-7`（默认） | 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `1e-8`（默认） | 标量 | 矩阵

初始状态误差的协方差。此参数定义状态初始化中的偏差。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认） | 0 | -1 | integer

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩膜子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在掩膜上提升模块参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认） | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真该模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数，轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

使用卡尔曼滤波器的电池容量估计器

Battery Capacity Estimator (Kalman Filter) 模块实现了一个估计器，该估计器使用卡尔曼滤波算法计算电池的单体容量。

将此模块与另一个估计电池荷电状态 (SOC) 的模块结合使用，例如 SOC Estimator (Kalman Filter) 或 SOC Estimator (Adaptive Kalman Filter)。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

对于连续时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

对于离散时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

为了估计电池容量，Battery Capacity Estimator (Kalman Filter) 模块从容量导数和 SOC 的方程开始：

dQdt=00=dSOCdt+i3600Q

其中

- *SOC* 是荷电状态。
- *i* 是电池单体的电流。
- *Q* 是以 Ampere-hour 为单位的容量。

第一个方程是状态方程。第二个方程是输出方程。

对于卡尔曼滤波算法，Battery Capacity Estimator (Kalman Filter) 模块将 *Q* 用作状态，并使用以下过程函数和观测函数：

f(Q)=0h(Q,SOC)=dSOCdt+i3600Q

**扩展卡尔曼滤波器**

此图显示了扩展卡尔曼滤波器 (EKF) 的结构：

EKF 技术依赖于在每个时间步进行线性化，以近似非线性系统。为了在每个时间步对系统进行线性化，该算法在线计算以下雅可比矩阵：

F=∂f∂Q=0H=∂h∂Q=−i3600Q2

EKF 是一种离散时间算法。离散化后，用于电池 SOC 估计的雅可比矩阵为：

Fd=1Hd=−iTs3600Q2

其中 *T*S 是采样时间。

有关 EKF 算法步骤实现的详细信息，请参阅 SOC Estimator (Kalman Filter) 模块的扩展卡尔曼滤波器一节。

**扩展卡尔曼-布西滤波器**

此图显示了扩展卡尔曼-布西滤波器 (EKBF) 的结构：

EKBF 是卡尔曼滤波器的连续时间变体。在连续时间中，预测和校正步骤是耦合的。

有关 EKF 算法步骤实现的详细信息，请参阅 SOC Estimator (Kalman Filter) 模块的扩展卡尔曼-布西滤波器一节。

**无迹卡尔曼滤波器**

此图显示了无迹卡尔曼滤波器 (UKF) 的结构：

EKF 通过仅使用展开式的一阶项，用从泰勒展开获得的线性方程局部近似非线性函数。在高度非线性系统中，这些解不够准确。

UKF 对算法确定性地选择的一组 sigma 点使用非线性变换。此技术称为 *无迹变换*。变换后点的均值和协方差矩阵精确到泰勒级数展开的二阶。

有关 EKF 算法步骤实现的详细信息，请参阅 SOC Estimator (Kalman Filter) 模块的无迹卡尔曼滤波器一节。

**无迹卡尔曼-布西滤波器**

此图说明了无迹卡尔曼-布西滤波器 (UKBF) 的结构：

推导出的 UKBF 连续时间滤波方程与 EKBF 方程类似。

有关 EKF 算法步骤实现的详细信息，请参阅 SOC Estimator (Kalman Filter) 模块的无迹卡尔曼-布西滤波器一节。
