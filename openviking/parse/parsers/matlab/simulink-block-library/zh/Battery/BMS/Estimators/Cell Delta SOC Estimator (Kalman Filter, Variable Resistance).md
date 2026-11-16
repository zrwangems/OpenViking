---
type: simulink-block
title: 'Cell Delta SOC Estimator (Kalman Filter, Variable Resistance)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'celldeltasocestimatorkalmanfiltervariableresistance'
documentation_source_path: 'ref/celldeltasocestimatorkalmanfiltervariableresistance.html'
language: zh-CN
chinese_source: worker-translation
---

# Cell Delta SOC Estimator (Kalman Filter, Variable Resistance)

## 端口

### 输入

### **Current** — 电池电流，ampere 标量 | 向量

电池电流，以 ampere 为单位，指定为单个电芯的标量或多个电芯的向量。要将此输入指定为电芯电流向量，请选择 **Specify Current input as cell current(s)** 参数。

### **CellVoltage** — 电芯电压，volt 标量 | 向量

电芯电压，以 volt 为单位，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellTemperature**、**dInvCellAH** 和 **CellR0** 输入端口的尺寸。

### **CellTemperature** — 电芯温度，K 标量 | 向量

电芯温度，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellVoltage**、**dInvCellAH** 和 **CellR0** 输入端口的尺寸。

### **dInvCellAH** — 逆 delta 电芯容量，A\*Hr 标量 | 向量

电池的逆 delta 电芯容量，以 ampere-hour 为单位，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellVoltage**、**CellTemperature** 和 **CellR0** 输入端口的尺寸。

### **CellR0** — 电芯端子电阻，ohm 标量 | 向量

电芯的端子电阻，以 ohm 为单位，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellVoltage**、**CellTemperature** 和 **dInvCellAH** 输入端口的尺寸。

### **PackSOC** — 电池包平均 SOC，unitless 标量

电池包的平均 SOC，指定为标量。

### **Vdyn** — 电池包平均动态过电位电压，volt 标量

电池包的平均动态过电位电压，以 volt 为单位，指定为标量。

### 输出

### **CellSOC** — 电池电芯的 SOC 标量 | 向量

电池电芯的 SOC，返回为标量或向量。此输出端口的尺寸等于 **CellVoltage**、**CellTemperature** 和 **dInvCellAH** 输入端口的尺寸。

## 参数

### 主要

### **Specify Current input as cell current(s)** — 用于将电流输入端口指定为向量的选项 `off` (默认) | `on`

用于将 **Current** 输入端口的值指定为电芯电流向量的选项。如果选择此参数，则 **Current** 输入端口的值可以是标量，也可以是大小等于模块输入大小的向量。

### **Filter type** — Kalman 滤波器类型 `Extended Kalman filter` (默认) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池荷电状态的 Kalman 滤波器类型。

### **Alpha** — Alpha 系数 `1` (默认) | 范围 (0,1] 内的标量

控制 sigma 点分布的系数。模块在实现无迹 Kalman 滤波器和无迹 Kalman-Bucy 滤波器的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2` (默认) | 非负标量

与分布相关的系数。模块在实现无迹 Kalman 滤波器和无迹 Kalman-Bucy 滤波器时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0` (默认) | 范围 [0, 3] 内的标量

控制 sigma 点分布的系数。模块在实现无迹 Kalman 滤波器和无迹 Kalman-Bucy 滤波器的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声协方差 `0.0001` (默认) | 标量

状态中噪声的协方差。

### **Covariance of the measurement noise, R** — 测量噪声协方差 `0.7` (默认) | 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `1e-3` (默认) | 标量

初始状态误差的协方差。此参数定义状态初始化中的偏差。

### **Sample time (-1 for inherited)** — 模块采样时间 `1` (默认) | 0 | -1 | integer

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩膜子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩膜上的模块参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]` (默认) | 范围 [0, 1] 内的标量向量

荷电状态断点向量，定义指定查找数据的点。此向量的条目必须严格按升序排列。

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]` (默认) | 正标量向量

温度断点向量，定义指定查找数据的点。此向量必须严格按升序排列且大于 0 K。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **Terminal resistance, R0(SOC,T), (ohm)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (默认) | 正元素矩阵

在指定 SOC 和温度断点下电池串联电阻的查找数据。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` (默认) | 非负元素矩阵

在指定 SOC 下基本电池模型的开路电压查找数据，以 volt 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### 信号属性

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto` (默认) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在 `single` 和 `double` 精度下仿真模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

具有电芯 delta Kalman 滤波器和可变电阻的荷电状态估计器

Cell Delta SOC Estimator (Kalman Filter, Variable Resistance) 模块实现了一种估计器，它使用电芯 delta Kalman 滤波器计算电池的荷电状态 (SOC)。电池电芯的端子电阻是模块的输入，并且可以是可变的。delta SOC 是估计器的内部状态，电流是控制输入，电芯电压是测量值。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

对于连续时间仿真，将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

对于离散时间仿真，将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

此方程定义电芯 delta SOC：

ΔSOCi=SOCi−SOC¯,i=1,…,Ns,

其中 *SOC*i 是电芯 `i` 的荷电状态，SOC¯ 是电池包平均荷电状态，`Ns` 是串联连接的电芯数量。

此方程定义逆 delta 电芯容量：

ΔAHinv,i=AHinv,i−AHinv¯,

其中 AHinv,i=1AHi 是电芯 `i` 的逆电芯容量，AH¯inv=1AH¯ 是电池的平均逆容量。

delta SOC 的状态空间模型为

dΔSOCidt=−i⋅ΔAHinv,i3600Vt,i=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

其中 `Vt,i` 是电芯 `i` 的端子电压，*R*0 是端子电阻。

对于 Kalman 滤波算法，模块使用 dΔSOCi 作为状态，以及以下过程函数和观测函数：

f(ΔSOCi)=−i⋅ΔAHinv,i3600h(dΔSOCi)=V0(SOC¯+ΔSOCi,T¯)−iR0−V¯dyn

扩展 Kalman 滤波器 (EKF) 依赖每个时间步的线性化来近似非线性系统。为了在每个时间步进行线性化，算法在线计算以下 Jacobian 矩阵：

F=∂f∂ΔSOCi=0H=∂V0∂ΔSOCi

EKF 是一种离散时间算法。离散化后，Jacobian 矩阵为：

Fd=1Hd=∂V0∂ΔSOCi

无迹 Kalman 滤波器对一组 sigma 点使用非线性变换，算法确定性地选择这些点。

然后，模块使用以下方程计算电芯 SOC：

SOCi=SOC¯+ΔSOCi.

用于容量估计的 Kalman 滤波器实现遵循本节所述的单状态模型的 SOC Estimator (Kalman Filter) 模块中的理论。
