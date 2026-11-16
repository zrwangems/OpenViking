---
type: simulink-block
title: 'SOC Estimator (Adaptive Kalman Filter)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / State-of-Charge Estimators'
documentation_page: 'socestimatoradaptivekalmanfilter'
documentation_source_path: 'ref/socestimatoradaptivekalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# SOC Estimator (Adaptive Kalman Filter)

## 端口

### 输入

### **Current** — 电池电流 标量 | 向量

电池电流，以 ampere 为单位，对于单个单体指定为标量，对于多个单体指定为向量。要将此输入指定为单体电流向量，请选择 **Specify Current input as cell current(s)** 参数。

### **CellVoltage** — 单体电压 标量 | 向量

单体电压，以 volt 为单位，对于单个单体指定为标量，对于多个单体指定为向量。此输入端口的大小必须等于 **CellTemperature**、**InitialSOC** 和 **InitialR0** 输入端口的大小。

### **CellTemperature** — 单体温度 标量 | 向量

单体温度，对于单个单体指定为标量，对于多个单体指定为向量。此输入端口的大小必须等于 **CellVoltage**、**InitialSOC** 和 **InitialR0** 输入端口的大小。

### **InitialSOC** — 初始荷电状态 标量 | 向量

初始荷电状态，指定为范围 [0, 1] 内的标量或向量。此输入端口的大小必须等于 **CellVoltage**、**CellTemperature** 和 **InitialR0** 输入端口的大小。

### **InitialR0** — 初始端子电阻 标量 | 向量

初始端子电阻，指定为标量或向量。此输入端口的大小必须等于 **CellVoltage**、**CellTemperature** 和 **InitialSOC** 输入端口的大小。

### 输出

### **SOC** — 荷电状态 标量 | 向量

电池的荷电状态，以标量或向量形式返回。此输出端口的大小等于 **CellVoltage**、**CellTemperature**、**InitialSOC** 和 **InitialR0** 输入端口的大小。

### **R0** — 端子电阻 标量 | 向量

端子电阻，以标量或向量形式返回。此输出端口的大小等于 **CellVoltage**、**CellTemperature**、**InitialSOC** 和 **InitialR0** 输入端口的大小。

## 参数

### 主要

### **Specify Current input as cell current(s)** — 用于将电流输入端口指定为向量的选项 `on`（默认） | `off`

*自 R2023b 起*

用于将 **Current** 输入端口的值指定为单体电流向量的选项。如果选择此参数，则 **Current** 输入端口的值可以是标量，也可以是大小等于模块输入大小的向量。

### **Filter type** — Kalman 滤波器类型 `Extended Kalman filter`（默认） | `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池荷电状态和端子电阻的 Kalman 滤波器类型。

### **Alpha** — Alpha 系数 `1`（默认） | 范围 [0, 1] 内的标量

控制 sigma 点分布的系数。该模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2`（默认） | 非负标量

与分布相关的系数。该模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0`（默认） | 范围 [0, 3] 内的标量

控制 sigma 点分布的系数。该模块在实现 unscented Kalman filter 和 unscented Kalman-Bucy filter 的方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声的协方差 `[1e-6 0 0; 0 1e-6 0;0 0 1e-6]`（默认） | 标量矩阵

状态中噪声的协方差矩阵。

### **Covariance of the measurement noise, R** — 测量噪声的协方差 `0.1`（默认） | 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `[1e-5 0 0; 0 1 0; 0 0 1e-5]`（默认） | 标量矩阵

初始状态误差的协方差矩阵。此参数定义状态初始化时的偏差。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认） | 0 | -1 | integer

连续模块执行之间的时间。在执行期间，模块生成输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **Charge dynamics** — 用于对电池充电动态建模的选项 `One time-constant dynamics`（默认） | `Two time-constant dynamics`

*自 R2024a 起*

用于对电池充电动态建模的选项。此参数确定等效电路中并联 RC 段的数量：

- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)** 和 **First time constant, tau1(SOC,T), (s)** 参数指定极化电阻和时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)**、**First time constant, tau1(SOC,T), (s)**、**Second polarization resistance, R2(SOC,T), (ohm)** 和 **Second time constant, tau2(SOC,T), (s)** 参数指定极化电阻和时间常数。

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认） | 范围 [0, 1] 内的标量向量

荷电状态断点向量，定义指定 lookup data 的点。此向量的条目必须严格升序排列。模块根据 **Cell capacity, AH (A\*Hr)** 参数中指定的标称电池容量计算荷电状态值。SOC 是可用电池电量 *q*battery 与标称电池容量 *q*nom*(T,n)* 的比值。必须确保，对于每个温度值，当您对循环次数 *N* 等于 1 且 *δAH(n = 1, Tfade)* 等于 0 的新电池建模时，SOC 为 1 表示 **Cell capacity, AH (A\*Hr)** 参数对应元素的电池电量容量：。

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH.

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]`（默认） | 正标量向量

温度断点向量，定义指定 lookup data 的点。此向量必须严格升序且大于 0 K。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **First polarization resistance, R1(SOC,T), (ohm)** — 温度断点处的第一 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认） | 正值矩阵

在指定 SOC 和温度断点处，第一个并联 RC 电阻的查找数据，以 ohm 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **First time constant, tau1(SOC,T), (s)** — 温度断点处的第一 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认） | 正值矩阵

在指定 SOC 和温度断点处，第一个并联 RC 时间常数的查找数据，以 second 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Second polarization resistance, R2(SOC,T), (ohm)** — 温度断点处的第二 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认） | 正值矩阵

*自 R2024a 起*

在指定 SOC 和温度断点处，第二个并联 RC 电阻的查找数据，以 ohm 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **Second time constant, tau2(SOC,T), (s)** — 温度断点处的第二 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认） | 正值矩阵

*自 R2024a 起*

在指定 SOC 和温度断点处，第二个并联 RC 时间常数的查找数据，以 second 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]`（默认） | 非负值矩阵

在指定 SOC 处，基本电池模型的开路电压查找数据，以 volt 为单位。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Cell capacity, AH (A\*Hr)** — 完全充电时的电池容量 `27`（默认） | 非负标量

电池的单体容量，以 ampere-hour 为单位。模块通过将累积电量除以该值来计算荷电状态。模块通过对电池电流进行积分来计算累积电量。

### 信号属性

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认） | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真该模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2024a：使用具有两个时间常数充电动态的等效模型估计 SOC

现在，您可以使用具有两个时间常数充电动态的等效模型估计电池 SOC。

要选择具有两个时间常数充电动态的等效模型，请将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，并指定新增的 **Second polarization resistance, R2(SOC,T), (ohm)** 和 **Second time constant, tau2(SOC,T), (s)** 参数的值。

### R2023b：将 Current 输入的值指定为单体电流向量

现在，您可以将 **Current** 输入端口的值指定为单体电流向量。

要启用向量化输入，请选择 **Specify Current input as cell current(s)** 参数。如果选择此参数，则 **Current** 输入端口必须与其他输入具有相同的大小，并表示各个单体电流。

## 描述

使用自适应 Kalman 滤波器的荷电状态和端子电阻估计器

SOC Estimator (Adaptive Kalman Filter) 模块实现了一个估计器，该估计器使用 Kalman 滤波算法计算电池的荷电状态 (SOC) 和端子电阻。端子电阻 *R*0 是估计器的一个状态。

SOC 是释放容量 *C*releasable 与额定容量 *C*rated 的比值。制造商提供每个电池的额定容量值，该值表示电池中的最大电量：

SOC=CreleasableCrated.

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

对于连续时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将其转换为双精度浮点值以防止错误。

对于离散时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

这些图分别展示了具有单时间常数动态和双时间常数动态的电池等效电路：

对于将端电阻 *R*0 作为附加状态且具有双时间常数动态的等效电路，方程为：

dSOCdt=−i3600AHdV1dt=iC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)dV2dt=iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)dR0dt=0Vt=V0(SOC,T)−iR0−V1−V2

其中

- *SOC* 是荷电状态。
- *i* 是电流。
- *V*0 是无负载电压。
- *V*t 是端电压。
- *AH* 是安时额定容量。
- *R*1 是第一极化电阻。
- *C*1 是第一并联 RC 电容。
- *R*2 是第二极化电阻。
- *C*2 是第二并联 RC 电容。
- *T* 是温度。
- *V*1 是第一个 RC 网络两端的极化电压。
- *V*2 是第二个 RC 网络两端的极化电压。

第一个并联部分的时间常数 *τ*1 通过关系式 C1=τ1/R1 将第一极化电阻 *R*1 和第一并联 RC 电容 *C*1 关联起来。

第二个并联部分的时间常数 *τ*2 通过关系式 C2=τ2/R2 将第二极化电阻 *R*2 和第二并联 RC 电容 *C*2 关联起来。

对于 Kalman 滤波算法，该模块使用此状态以及这些非线性过程函数和观测函数：

x=[SOCV1R0]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)0]h(x,i)=V0(SOC,T)−iR0−V1

如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，则对于 Kalman 滤波算法，该模块使用此状态以及这些过程函数和观测函数：

x=[SOCV1V2R0]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)0]h(x,i)=V0(SOC,T)−iR0−V1−V2

**扩展 Kalman 滤波器**

该图展示了扩展 Kalman 滤波器（EKF）的结构：

EKF 技术依赖于在每个时间步进行线性化来近似非线性系统。为了在每个时间步对系统进行线性化，该算法在线计算以下 Jacobian：

F=∂f∂xH=∂h∂x

EKF 是一种离散时间算法。离散化后，用于电池 SOC 估计的 Jacobian 为：

Fd=[1000e−TSR1C10001]Hd=[∂VOC∂SOC−1−i]

其中 *T*S 是采样时间，*V*OC 是开路电压。

EKF 算法包括以下阶段：

- **初始化**

  - x^(0|0)⁠— 使用时间步 0 的测量值在时间步 0 的状态估计。
  - P^(0|0)⁠— 使用时间步 0 的测量值在时间步 0 的状态估计误差协方差矩阵。
- **预测**

  - 将状态向前投影（*a priori*）：

    x^(k+1|k)=f(x^(k|k),i).
  - 将误差协方差向前投影：

    P^(k+1|k)=Fd(k)P^(k|k)FdT(k)+Q,

    其中 **Q** 是过程噪声的协方差。
- **校正**

  - 计算 Kalman 增益：

    K(k+1)=P^(k+1|k)HdT(k)(Hd(k)P^(k+1|k)HdT(k)+R)−1,

    其中 *R* 是测量噪声的协方差。
  - 使用测量 *y(k)* 更新估计（*a posteriori*）：

    x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k)−h(x^(k|k),i)).
  - 更新误差协方差：

    P^(k+1|k+1)=(I−K(k+1)Hd)P^(k+1|k).

**扩展 Kalman-Bucy 滤波器**

该图展示了扩展 Kalman-Bucy 滤波器（EKBF）的结构：

EKBF 是 Kalman 滤波器的连续时间变体。在连续时间中，预测和校正步骤是耦合的。EKBF 算法包括以下阶段：

- **初始化**

  - x^(t0)⁠— 时间 *t*0 的状态估计。
  - P^(t0)⁠— 时间 *t*0 的状态估计误差协方差矩阵。
- **预测-校正 EKBF 算法**

  K(t)=P(t)HT(t)R−1(t)dx^(t)dt=f(x^(t),i(t))+K(t)(Vt(t)−h(x^(t),i(t)))dP(t)dt=F(t)P(t)+P(t)FT(t)+Q(t)−K(t)H(t)P(t)

  其中：

  F(t)=∂f∂xH(t)=∂h∂x

**无迹 Kalman 滤波器**

该图展示了无迹 Kalman 滤波器（UKF）的结构：

EKF 通过仅使用展开的第一项，以从 Taylor 展开获得的线性方程来局部近似非线性函数。在高度非线性的系统中，这些解不是很准确。

UKF 对算法确定性地选择的一组 sigma 点使用非线性变换。该技术称为 *无迹变换*。变换后点的均值和协方差矩阵精确到 Taylor 级数展开的二阶。

UKF 算法遵循以下步骤：

- **初始化**

  - x^(0|0)⁠— 使用时间步 0 的测量值在时间步 0 的状态估计。
  - P^(0|0)⁠— 使用时间步 0 的测量值在时间步 0 的状态估计误差协方差矩阵。
- 生成 sigma 点，并为每个点计算均值权重和协方差权重。

  - 选择 sigma 点 *x(i)(k|k)*

    x(i)(k|k)={x^(k+1|k)i=1x^(k+1|k)+((n+λ)P(k|k))ii=2,…,n+1x^(k+1|k)−((n+λ)P(k|k))ii=n+2,…,2n+1Wm(i)={λn+λi=112(n+λ)i≠1Wc(i)={λn+λ+(1−α2+β)i=112(n+λ)i≠1

    其中：

    - *n* 是状态向量 *x* 的维数。
    - λ=α2(n+κ)−n, α∈[0,1] 描述 sigma 点与均值点之间的距离。在正态分布中，*β =* 2 且 *κ =* 0。
    - ((n+λ)P)i 是 cP 的第 *i* 行或列。该模块使用数值高效且稳定的方法（例如 Cholesky 分解）计算矩阵平方根。
- 执行系统状态矩阵的第一次估计：

  x^(i)(k+1|k)=f(x^(i)(k|k),i(k))x^(k+1|k)=∑i=12n+1Wm(i)x^(i)(k+1|k)
- 执行状态变量协方差矩阵的第一次估计：

  P(k+1|k)=∑i=12n+1Wc(i)(x^(i)(k+1|k)−x^(k+1|k))⋅(x^(i)(k+1|k)−x^(k+1|k))T+Q
- 估计测量变量：

  Vt(i)(k+1|k)=h(x^(i)(k+1|k),i(k))V^t(k+1|k)=∑i=12n+1Wm(i)V^t(i)(k+1|k)
- 估计测量的协方差（*Py*）以及测量与状态之间的协方差（*Pxy*）：

  Py=∑i=12n+1Wc(i)(V^t(i)(k+1|k)−V^t(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T+RPxy=∑i=12n+1(x^(i)(k+1|k)−x^(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T
- 计算 Kalman 滤波器增益：

  K(k+1)=PxyPy−1
- 执行状态矩阵和状态变量协方差的第二次更新：

  x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k+1)−V^t(k+1|k))P(k+1|k+1)=P(k+1|k)−K(k+1)PyKT(k+1)

**无迹 Kalman-Bucy 滤波器**

该图展示了无迹 Kalman-Bucy 滤波器（UKBF）的结构：

推导出的 UKBF 连续时间滤波方程与 EKBF 方程相似。

由于 UKF 在其 sigma 点中使用矩阵平方根，该算法通过将滤波器表示为 sigma 点的微分方程来获得 UKBF 的平方根版本。平方根 UKBF 的方程为：

K(t)=X(t)WhT(X(t),t)R−1(t)M(t)=A−1(t)[X(t)WfT(X(t),t)+f(X(t),t)WXT(t)+Q(t)−K(t)R(t)KT(t)]A−T(t)dXi(t)dt=f(X(t),t)wm+K(t)(Vt(t)−h(X(t),t)wm)+c[0A(t)Φ(M(t))−A(t)Φ(M(t))]i

其中

- X(t)=[m(t)…m(t)]+c[0A(t)−A(t)] 是 sigma 点矩阵。
- Φij(M(t))={Mij(t),i>j0.5Mij(t),i=j0,i<j 是一个返回参数下三角部分的函数。
- wm=[Wm(1)⋯Wm(2n+1)]T
- W=(1−[wm⋯wm])diag(Wc(1)⋯Wc(2n+1))(I−[wm⋯wm])T
- c=α2(n+κ)
- [0A(t)Φ(M(t))−A(t)Φ(M(t))]i 是参数矩阵的第 *i* 列。
