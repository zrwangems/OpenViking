---
type: simulink-block
title: 'Pack Bar SOC Estimator (Kalman Filter)'
family: 'bms'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'packbarsocestimatorkalmanfilter'
documentation_source_path: 'ref/packbarsocestimatorkalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Pack Bar SOC Estimator (Kalman Filter)

## 端口

### 输入

### **AverageCurrent** — 电池组的平均电流，ampere 标量

电池组的平均电流，以 ampere 为单位，指定为标量。

### **AverageVoltage** — 电池组的平均电压，volt 标量

电池组的平均电压，以 volt 为单位，指定为标量。

### **AverageTemperature** — 电池组的平均温度，K 标量

电池组的平均温度，指定为标量。

### **AverageAH** — 电池组的平均电荷量，A\*Hr 标量

电池组的平均电荷量，以 ampere-hour 为单位，指定为标量。

### **InitialSOC** — 初始荷电状态，范围 [0,1] 内的无量纲标量

初始荷电状态，指定为范围 [0,1] 内的标量。
### 输出

### **SOC** — 电池组的平均荷电状态标量

电池组的平均荷电状态，以标量形式返回。

### **Vdyn** — 电池组的平均动态过电位电压标量

电池组的平均动态过电位电压，以标量形式返回。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Filter type** — Kalman 滤波器类型 `Extended Kalman filter`（默认）| `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池组平均荷电状态的 Kalman 滤波器类型。

### **Alpha** — Alpha 系数 `1`（默认）| 范围 (0, 1] 中的标量

控制 sigma 点分布范围的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2`（默认）| 非负标量

与分布相关的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0`（默认）| 范围 [0, 3] 中的标量

控制 sigma 点分布范围的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声的协方差 `[1e-6 0; 0 1e-6]`（默认）| `[1e-6 0 0;0 1e-6 0;0 0 1e-6]` | 标量矩阵

状态中噪声的协方差矩阵。

如果将 **Charge dynamics** 参数设置为 `One time-constant dynamics`，请指定 `2`-by-`2` 矩阵；如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，请指定 `3`-by-`3` 矩阵。

### **Covariance of the measurement noise, R** — 测量噪声的协方差 `0.1`（默认）| 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `[1e-5 0; 0 1]`（默认）| `[1e-5 0 0; 0 1 0;0 0 1]` | 标量矩阵

初始状态误差的协方差矩阵。此参数定义状态初始化中的偏差。

如果将 **Charge dynamics** 参数设置为 `One time-constant dynamics`，请指定 `2`-by-`2` 矩阵；如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，请指定 `3`-by-`3` 矩阵。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认）| 0 | -1 | 整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关更多信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关更多信息，请参阅 Promote Block Parameters on a Mask。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **Charge dynamics** — 为电池充电动态建模的选项 `One time-constant dynamics`（默认）| `Two time-constant dynamics`

用于为电池充电动态建模的选项。此参数确定等效电路中并联 RC 段的数量：

- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)** 和 **First time constant, tau1(SOC,T), (s)** 参数指定极化电阻和时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)**；**First time constant, tau1(SOC,T), (s)**；**Second polarization resistance, R2(SOC,T), (ohm)**；和 **Second time constant, tau2(SOC,T), (s)** 参数指定极化电阻和时间常数。

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围 [0, 1] 中的标量向量

荷电状态断点向量，用于定义您指定查找数据的点。此向量的条目必须严格按升序排列。

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]`（默认）| 正标量向量

温度断点向量，用于定义您指定查找数据的点。此向量必须严格按升序排列且大于 0 K。此参数的物理单位必须与 **AverageTemperature** 输入端口的物理单位相同。

### **Terminal resistance, R0(SOC,T), (ohm)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 正元素矩阵

在指定的 SOC 和温度断点处，电池串联电阻的查找数据。

### **First polarization resistance, R1(SOC,T), (ohm)** — 温度断点处的第一 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认）| 正元素矩阵

在指定的 SOC 和温度断点处，第一并联 RC 电阻的查找数据，以 ohm 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **First time constant, tau1(SOC,T), (s)** — 温度断点处的第一 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认）| 正元素矩阵

在指定的 SOC 和温度断点处，第一并联 RC 时间常数的查找数据，以 second 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Second polarization resistance, R2(SOC,T), (ohm)** — 温度断点处的第二 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认）| 正元素矩阵

在指定的 SOC 和温度断点处，第二并联 RC 电阻的查找数据，以 ohm 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **Second time constant, tau2(SOC,T), (s)** — 温度断点处的第二 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认）| 正元素矩阵

在指定的 SOC 和温度断点处，第二并联 RC 时间常数的查找数据，以 seconds 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]`（默认）| 非负元素矩阵

在指定 SOC 处，基本电池模型的开路电压的查找数据，以 volt 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### 信号属性

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 可以在 `single` 和 `double` 精度下仿真模块。必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

未在 R2025b 中记载。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 Kalman 滤波器的电池组平均荷电状态估计器

Pack Bar SOC Estimator (Kalman Filter) 模块实现一个估计器，该估计器使用 Kalman 滤波算法计算电池组的平均荷电状态 (SOC)。平均荷电状态和极化电压是估计器的内部状态，电流是控制输入，平均电池组电压是测量值。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

对于连续时间仿真，将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将其转换为双精度浮点值以防止错误。

对于离散时间仿真，将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

bar 滤波技术估计电池组的平均状态。具有两个时间常数动态的电池组平均数学模型方程如下：

dSOC¯dt=−i3600⋅AH¯dV1¯dt=iC1(SOC¯,T¯)−V1¯R1(SOC¯,T¯)⋅C1(SOC¯,T¯)dV2¯dt=iC2(SOC¯,T¯)−V2¯R2(SOC¯,T¯)⋅C2(SOC¯,T¯)V¯t=V0(SOC¯,T¯)−iR0¯−V1¯−V2¯

其中：

- SOC¯=1Ns∑i=1NsSOCi 是电池组的平均荷电状态。
- *i* 是电流。
- *V*0 是无负载电压。
- Vt¯ 是电池组的平均端电压。
- AH¯ 是电池组的平均 ampere-hour 额定值。
- R0¯ 是电池组的端电阻。
- *R*1 是第一极化电阻。
- *C*1 是第一并联 RC 电容。
- *R*2 是第二极化电阻。
- *C*2 是第二并联 RC 电容。
- T¯ 是电池组的平均温度。
- V1¯ 是第一 RC 网络上的极化电压。
- V2¯ 是第二 RC 网络上的极化电压。

第一并联段的时间常数 *τ*1 通过关系式 C1=τ1/R1 将第一极化电阻 *R*1 与第一并联 RC 电容 *C*1 关联起来。

第二并联段的时间常数 *τ*2 通过关系式 C2=τ2/R2 将第二极化电阻 *R*2 与第二并联 RC 电容 *C*2 关联起来。

对于串联连接的电池单体，单体电流相等。在对电池进行均衡时，单体电流可能不相等，必须对电流取平均值。

bar 滤波器的输出是电池组的估计平均荷电状态 SOC¯，以及平均动态过电位电压 Vdyn¯=V1¯+V2¯。

要详细了解此模块各 Kalman 滤波算法的内部实现和方程，请参阅 SOC Estimator (Kalman Filter) 模块的 Equations 部分。
