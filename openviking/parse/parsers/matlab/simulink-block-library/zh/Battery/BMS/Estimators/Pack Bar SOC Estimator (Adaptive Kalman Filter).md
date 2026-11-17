---
type: simulink-block
title: 'Pack Bar SOC Estimator (Adaptive Kalman Filter)'
family: 'bms'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'packbarsocestimatoradaptivekalmanfilter'
documentation_source_path: 'ref/packbarsocestimatoradaptivekalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Pack Bar SOC Estimator (Adaptive Kalman Filter)

## 端口

### 输入

### **AverageCurrent** — 电池包的平均电流，ampere 标量

电池包的平均电流，以 ampere 为单位，指定为标量。

### **AverageVoltage** — 电池包的平均电压，volt 标量

电池包的平均电压，以 volt 为单位，指定为标量。

### **AverageTemperature** — 电池包的平均温度，K 标量

电池包的平均温度，指定为标量。

### **AverageAH** — 电池包的平均电量，A\*Hr 标量

电池包的平均电量，以 ampere-hour 为单位，指定为标量。

### **InitialSOC** — 初始荷电状态，[0,1] 范围内的无单位标量

初始荷电状态，指定为 [0,1] 范围内的标量。

### **InitialR0** — 初始端电阻，ohm 标量

初始端电阻，以 ohm 为单位，指定为标量。

### 输出

### **SOC** — 电池包的平均荷电状态，标量

电池包的平均荷电状态，以标量形式返回。

### **R0** — 电池包的平均端电阻，标量

电池包的平均端电阻，以标量形式返回。

### **Vdyn** — 电池包的平均动态过电位电压，标量

电池包的平均动态过电位电压，以标量形式返回。

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### 主要

### **Filter type** — 卡尔曼滤波器类型 `Extended Kalman filter` (default) | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池包平均荷电状态的卡尔曼滤波器类型。

### **Alpha** — Alpha 系数 `1` (default) | (0, 1] 范围内的标量

控制 sigma 点分布的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖项

要启用此参数，请将 **Filter type** 设置为
`Unscented Kalman filter` 或 `Unscented
Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2` (default) | 非负标量

与分布相关的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 时使用此参数。

#### 依赖项

要启用此参数，请将 **Filter type** 设置为
`Unscented Kalman filter` 或 `Unscented
Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0` (default) | [0, 3] 范围内的标量

控制 sigma 点分布的系数。此模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖项

要启用此参数，请将 **Filter type** 设置为
`Unscented Kalman filter` 或 `Unscented
Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声的协方差 `[1e-6 0 0;0 1e-6 0;0 0 1e-6]` (default) | `[1e-6 0 0 0;0 1e-6 0 0;0 0 1e-6 0;0 0 0 1e-6]` | 标量矩阵

状态中噪声的协方差矩阵。

如果将 **Charge dynamics** 参数设置为 `One time-constant dynamics`，请指定 `3`-by-`3` 矩阵；如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，请指定 `4`-by-`4` 矩阵。

### **Covariance of the measurement noise, R** — 测量噪声的协方差 `0.1` (default) | 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `[1e-5 0 0; 0 1 0; 0 0 1e-5]` (default) | `[1e-5 0 0 0; 0 1 0 0;0 0 1 0; 0 0 0 1e-5]` | 标量矩阵

初始状态误差的协方差矩阵。此参数定义状态初始化中的偏差。

如果将 **Charge dynamics** 参数设置为 `One time-constant dynamics`，请指定 `3`-by-`3` 矩阵；如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，请指定 `4`-by-`4` 矩阵。

### **Sample time (-1 for inherited)** — 模块采样时间 `1` (default) | 0 | -1 | 整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅在封装上提升模块参数。

#### 依赖项

要启用此参数，请将 **Filter type** 设置为
`Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **Charge dynamics** — 用于对电池充电动态建模的选项 `One time-constant dynamics` (default) | `Two time-constant dynamics`

用于对电池充电动态建模的选项。此参数确定等效电路中的并联 RC 段数：

- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)** 和 **First time constant, tau1(SOC,T), (s)** 参数指定极化电阻和时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)**；**First time constant, tau1(SOC,T), (s)**；**Second polarization resistance, R2(SOC,T), (ohm)**；和 **Second time constant, tau2(SOC,T), (s)** 参数指定极化电阻和时间常数。

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]` (default) | [0, 1] 范围内的标量向量

荷电状态断点向量，用于定义指定查找数据的点。此向量的条目必须严格按升序排列。

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]` (default) | 正标量向量

温度断点向量，用于定义指定查找数据的点。此向量必须严格按升序排列且大于 0 K。此参数的物理单位必须与 **AverageTemperature** 输入端口相同。

### **Terminal resistance, R0(SOC,T), (ohm)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | 正条目矩阵

在指定 SOC 和温度断点处电池串联电阻的查找数据。

### **First polarization resistance, R1(SOC,T), (ohm)** — 温度断点处的第一 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | 正条目矩阵

在指定 SOC 和温度断点处第一个并联 RC 电阻的查找数据，单位为 ohm。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **First time constant, tau1(SOC,T), (s)** — 温度断点处的第一 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | 正条目矩阵

在指定 SOC 和温度断点处第一个并联 RC 时间常数的查找数据，单位为 second。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Second polarization resistance, R2(SOC,T), (ohm)** — 温度断点处的第二 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` (default) | 正条目矩阵

在指定 SOC 和温度断点处第二个并联 RC 电阻的查找数据，单位为 ohm。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖项

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **Second time constant, tau2(SOC,T), (s)** — 温度断点处的第二 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` (default) | 正条目矩阵

在指定 SOC 和温度断点处第二个并联 RC 时间常数的查找数据，单位为 seconds。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖项

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` (default) | 非负条目矩阵

在指定 SOC 处基础电池模型两端开路电压的查找数据，单位为 volt。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### 信号属性

### **Algorithm data type** — 用于为模块算法选择数据类型的选项 `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于为模块算法选择数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以使用 `single` 和 `double` 精度仿真此模块。必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

使用卡尔曼滤波器的电池包平均荷电状态和端电阻估计器

Pack Bar SOC Estimator (Adaptive Kalman Filter) 模块实现一个估计器，它通过使用卡尔曼滤波算法计算电池包的平均荷电状态 (SOC) 和端电阻。平均荷电状态、极化电压和平均端电阻是估计器的内部状态，电流是控制输入，电池包平均电压是测量值。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型必须为 `single`。

对于连续时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

对于离散时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

bar filter 技术估计电池包的平均状态。具有 two time-constant dynamics 的电池包平均数学模型方程为：

dSOC¯dt=−i3600⋅AH¯dV1¯dt=iC1(SOC¯,T¯)−V1¯R1(SOC¯,T¯)⋅C1(SOC¯,T¯)dV2¯dt=iC2(SOC¯,T¯)−V2¯R2(SOC¯,T¯)⋅C2(SOC¯,T¯)dR0¯dt=0V¯t=V0(SOC¯,T¯)−iR0¯−V1¯−V2¯

其中：

- SOC¯=1Ns∑i=1NsSOCi 是电池包的平均荷电状态。
- *i* 是电流。
- *V*0 是空载电压。
- Vt¯ 是电池包的平均端电压。
- AH¯ 是电池包的平均 ampere-hour 额定值。
- R0¯ 是电池包的端电阻。
- *R*1 是第一极化电阻。
- *C*1 是第一并联 RC 电容。
- *R*2 是第二极化电阻。
- *C*2 是第二并联 RC 电容。
- T¯ 是电池包的平均温度。
- V1¯ 是第一个 RC 网络上的极化电压。
- V2¯ 是第二个 RC 网络上的极化电压。

第一个并联支路的时间常数 *τ*1 使用关系式 C1=τ1/R1 将第一极化电阻 *R*1 和第一并联 RC 电容 *C*1 关联起来。

第二个并联支路的时间常数 *τ*2 使用关系式 C2=τ2/R2 将第二极化电阻 *R*2 和第二并联 RC 电容 *C*2 关联起来。

对于串联连接的电池，电池电流相等。当对电池进行均衡时，电池电流可能不相等，必须对电流取平均。

bar filter 的输出是电池包的估计平均荷电状态 SOC¯、平均动态过电位电压 Vdyn¯=V1¯+V2¯ 和平均端电阻 R0¯。

要详细了解此模块每个 Kalman filter 算法的内部实现和方程，请参阅 SOC Estimator (Kalman Filter) 模块的方程部分。
