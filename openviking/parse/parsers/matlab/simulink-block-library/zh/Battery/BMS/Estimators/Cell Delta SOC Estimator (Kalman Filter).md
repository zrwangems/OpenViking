---
type: simulink-block
title: 'Cell Delta SOC Estimator (Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'celldeltasocestimatorkalmanfilter'
documentation_source_path: 'ref/celldeltasocestimatorkalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Cell Delta SOC Estimator (Kalman Filter)

## 端口

### 输入

### **Current** — 电池电流，ampere 标量 | 向量

电池电流，单位为 ampere，指定为单个单体的标量或多个单体的向量。要将此输入指定为单体电流向量，请选择 **将 Current 输入指定为单体电流** 参数。

### **CellVoltage** — 单体电压，volt 标量 | 向量

单体电压，单位为 volt，指定为单个单体的标量或多个单体的向量。此输入端口的大小必须等于 **CellTemperature** 和 **dInvCellAH** 输入端口的大小。

### **CellTemperature** — 单体温度，K 标量 | 向量

单体温度，指定为单个单体的标量或多个单体的向量。此输入端口的大小必须等于 **CellVoltage** 和 **dInvCellAH** 输入端口的大小。

### **dInvCellAH** — 逆 delta 单体容量，A\*Hr 标量 | 向量

电池的逆 delta 单体容量，单位为 ampere-hour，指定为单个单体的标量或多个单体的向量。此输入端口的大小必须等于 **CellVoltage**、**CellTemperature** 和 **CellR0** 输入端口的大小。

### **PackSOC** — 电池包平均 SOC，unitless 标量

电池包的平均 SOC，指定为标量。

### **Vdyn** — 电池包平均动态过电位电压，volt 标量

电池包的平均动态过电位电压，单位为 volt，指定为标量。

### 输出

### **CellSOC** — 电池单体 SOC 标量 | 向量

电池单体的 SOC，返回为标量或向量。此输出端口的大小等于 **CellVoltage**、**CellTemperature** 和 **dInvCellAH** 输入端口的大小。

## 参数

### 主要

### **将 Current 输入指定为单体电流** — 将电流输入端口指定为向量的选项 `off`（默认）| `on`

用于将 **Current** 输入端口的值指定为单体电流向量的选项。如果选择此参数，**Current** 输入端口处的值可以是标量，也可以是大小等于模块输入大小的向量。

### **滤波器类型** — Kalman 滤波器类型 `Extended Kalman filter`（默认）| `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池荷电状态的 Kalman 滤波器类型。

### **Alpha** — Alpha 系数 `1`（默认）| 范围 (0,1] 内的标量

控制 sigma 点分布的系数。模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2`（默认）| 非负标量

与分布相关的系数。模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 时使用此参数。

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0`（默认）| 范围 [0, 3] 内的标量

控制 sigma 点分布的系数。模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **过程噪声协方差，Q** — 过程噪声的协方差 `0.0001`（默认）| 标量

状态中噪声的协方差。

### **测量噪声协方差，R** — 测量噪声的协方差 `0.7`（默认）| 标量

测量中噪声的协方差。

### **初始状态误差协方差，P0** — 初始状态误差协方差 `1e-3`（默认）| 标量

初始状态误差的协方差。此参数定义状态初始化中的偏差。

### **采样时间（-1 表示继承）** — 模块采样时间 `1`（默认）| 0 | -1 | integer

连续模块执行之间的时间。执行期间，模块生成输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **荷电状态值向量，SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围 [0, 1] 内的标量向量

定义指定查找数据所使用的点的荷电状态断点向量。此向量的各项必须严格递增。

### **温度向量，T** — 温度断点 `[278, 293, 313]`（默认）| 正标量向量

定义指定查找数据所使用的点的温度断点向量。此向量必须严格递增且大于 0 K。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **端子电阻，R0(SOC,T)，(ohm)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 正项矩阵

指定 SOC 和温度断点处电池串联电阻的查找数据。

### **空载电压，V0(SOC,T)，(V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]`（默认）| 非负项矩阵

指定 SOC 处基本电池模型两端开路电压的查找数据，单位为 volt。此矩阵的行数等于 **荷电状态值向量，SOC (-)** 参数的大小。此矩阵的列数等于 **温度向量，T** 参数的大小。

### 信号属性

### **算法数据类型** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以对模块进行
  `single` 和 `double`
  精度的仿真。您必须将输入和参数显式提供为
  `single` 或
  `double`。
- `double` — 模块算法将所有输入和参数转换为
  `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为
  `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

State of charge estimator with cell delta Kalman filter

使用 cell delta Kalman filter 的荷电状态估计器

Cell Delta SOC Estimator (Kalman Filter) 模块实现了一个估计器，该估计器使用 cell delta Kalman filter 计算电池的荷电状态 (SOC)。delta SOC 是估计器内部状态，电流是控制输入，单体电压是测量值。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，所有输入和参数（**采样时间（-1 表示继承）** 参数除外）的数据类型都必须为 `single`。

对于连续时间仿真，请将 **滤波器类型** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅适用于双精度浮点仿真。如果您提供单精度浮点参数和输入，此模块会将其转换为双精度浮点值以防止错误。

对于离散时间仿真，请将 **滤波器类型** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **采样时间（-1 表示继承）** 参数设置为正值或 `-1`。

### 方程

此方程定义单体 delta SOC：

ΔSOCi=SOCi−SOC¯,i=1,…,Ns,

其中 *SOC*i 是单体 `i` 的荷电状态，SOC¯ 是电池包平均荷电状态，`Ns` 是串联连接的单体数量。

此方程定义逆 delta 单体容量：

ΔAHinv,i=AHinv,i−AHinv¯,

其中 AHinv,i=1AHi 是单体 `i` 的逆容量，AH¯inv=1AH¯ 是电池的平均逆容量。

delta SOC 的状态空间模型为

dΔSOCidt=−i⋅ΔAHinv,i3600Vt,i=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

其中 `Vt,i` 是单体 `i` 的端子电压，*R0* 是端子电阻。

对于 Kalman 滤波器算法，模块使用 dΔSOCi 作为状态，并使用以下过程函数和观测函数：

f(ΔSOCi)=−i⋅ΔAHinv,i3600h(dΔSOCi)=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

扩展 Kalman 滤波器 (EKF) 依靠每个时间步的线性化来近似非线性系统。为了在每个时间步进行线性化，算法在线计算以下 Jacobian：

F=∂f∂ΔSOCi=0H=∂V0∂ΔSOCi

EKF 是离散时间算法。离散化后，Jacobian 为：

Fd=1Hd=∂V0∂ΔSOCi

unscented Kalman filter 对一组 sigma 点使用非线性变换，这些点由算法确定性地选择。

然后模块使用此方程计算单体 SOC：

SOCi=SOC¯+ΔSOCi.

用于容量估计的 Kalman 滤波器实现遵循本节中所述的单状态模型的 SOC Estimator (Kalman Filter) 模块中的理论。
