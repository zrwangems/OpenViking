---
type: simulink-block
title: 'SOC Estimator (Kalman Filter, Variable Capacity)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'socestimatorkalmanfiltervariablecapacity'
documentation_source_path: 'ref/socestimatorkalmanfiltervariablecapacity.html'
language: zh-CN
chinese_source: worker-translation
---

# SOC Estimator (Kalman Filter, Variable Capacity)

## 端口
```yaml
ports:
- name: Current
  summary: 电池电流标量 | 向量
  direction: input
- name: CellVoltage
  summary: 电芯电压标量 | 向量
  direction: input
- name: CellTemperature
  summary: 电芯温度标量 | 向量
  direction: input
- name: CellAH
  summary: 电芯温度标量 | 向量
  direction: input
- name: InitialSOC
  summary: 初始荷电状态标量 | 向量
  direction: input
- name: SOC
  summary: 荷电状态标量 | 向量
  direction: output
```

### 输入

### **Current** — 电池电流标量 | 向量

电池电流，单位为安培，指定为单个电芯的标量或多个电芯的向量。要将此输入指定为电芯电流向量，请选择 **Specify Current input as cell current(s)** 参数。

### **CellVoltage** — 电芯电压标量 | 向量

电芯电压，单位为伏特，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellTemperature**、**CellAH** 和 **InitialSOC** 输入端口的尺寸。

### **CellTemperature** — 电芯温度标量 | 向量

电芯温度，指定为单个电芯的标量或多个电芯的向量。此输入端口的尺寸必须等于 **CellVoltage**、**CellAH** 和 **InitialSOC** 输入端口的尺寸。

### **CellAH** — 电芯温度标量 | 向量

电池的电芯容量，单位为安培小时，指定为单个电芯的标量或多个电芯的向量。该模块通过将累积电荷除以该值来计算 SOC。该模块通过对电池电流进行积分来计算累积电荷。

此输入端口的尺寸必须等于 **CellTemperature**、**CellVoltage** 和 **InitialSOC** 输入端口的尺寸。

### **InitialSOC** — 初始荷电状态标量 | 向量

初始荷电状态，指定为范围 [0, 1] 内的标量或向量。此输入端口的尺寸必须等于 **CellVoltage**、**CellTemperature** 和 **CellAH** 输入端口的尺寸。
### 输出

### **SOC** — 荷电状态标量 | 向量

电池的荷电状态，以标量或向量形式返回。此输出端口的尺寸等于 **CellVoltage**、**CellTemperature**、**CellAH** 和 **InitialSOC** 输入端口的尺寸。
## 参数
```yaml
parameters:
- name: Specify Current input as cell current(s)
  summary: 将电流输入端口指定为向量的选项 off（默认）| on
  group: 主
- name: Filter type
  summary: 卡尔曼滤波器类型 Extended Kalman filter（默认）| Extended Kalman-Bucy filter | Unscented Kalman filter | Unscented Kalman-Bucy
    filter
  group: 主
- name: Alpha
  summary: Alpha 系数 1（默认）| 范围 [0, 1] 内的标量
  group: 主
- name: Beta
  summary: Beta 系数 2（默认）| 非负标量
  group: 主
- name: Kappa
  summary: Kappa 系数 0（默认）| 范围 [0, 3] 内的标量
  group: 主
- name: Covariance of the process noise, Q
  summary: 过程噪声协方差 [1e-6 0; 0 1e-6]（默认）| 标量矩阵
  group: 主
- name: Covariance of the measurement noise, R
  summary: 测量噪声协方差 0.1（默认）| 标量
  group: 主
- name: Initial state error covariance, P0
  summary: 初始状态误差协方差 [1e-5 0; 0 1]（默认）| 标量矩阵
  group: 主
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 1（默认）| 0 | -1 | 整数
  group: 主
- name: Charge dynamics
  summary: 对电池充电动态建模的选项 One time-constant dynamics（默认）| Two time-constant dynamics
  group: 系统模型
- name: Vector of state-of-charge values, SOC (-)
  summary: SOC 断点 [0, .1, .25, .5, .75, .9, 1]（默认）| 范围 [0, 1] 内的标量向量
  group: 系统模型
- name: Vector of temperatures, T
  summary: 温度断点 [278, 293, 313]（默认）| 正标量向量
  group: 系统模型
- name: Terminal resistance, R0(SOC,T), (ohm)
  summary: 带温度断点的 R0 查找表 [.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091;
    .0113, .0085, .0089; .0116, .0085, .0089]（默认）| 正元素矩阵
  group: 系统模型
- name: First polarization resistance, R1(SOC,T), (ohm)
  summary: 温度断点处的第一 RC 电阻 [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023,
    .0014; .0033, .0018, .0011; .0028, .0017, .0011]（默认）| 正元素矩阵
  group: 系统模型
- name: First time constant, tau1(SOC,T), (s)
  summary: 温度断点处的第一 RC 时间常数 [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]（默认）| 正元素矩阵
  group: 系统模型
- name: Second polarization resistance, R2(SOC,T), (ohm)
  summary: 温度断点处的第二 RC 电阻 [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023,
    .0014; .0033, .0018, .0011; .0028, .0017, .0011]（默认）| 正元素矩阵
  group: 系统模型
- name: Second time constant, tau2(SOC,T), (s)
  summary: 温度断点处的第二 RC 时间常数 [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]（默认）| 正元素矩阵
  group: 系统模型
- name: No-load voltage, V0(SOC,T), (V)
  summary: '*V*0 查找表 [3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08,
    4.08; 4.19, 4.19, 4.19]（默认）| 非负元素矩阵'
  group: 系统模型
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认）| double | single | <data type expression>'
  group: 信号属性
```

### 主

### **Specify Current input as cell current(s)** — 将电流输入端口指定为向量的选项 `off`（默认）| `on`

将 **Current** 输入端口的值指定为电芯电流向量的选项。如果选择此参数，**Current** 输入端口的值可以是标量或尺寸等于模块输入尺寸的向量。

### **Filter type** — 卡尔曼滤波器类型 `Extended Kalman filter`（默认）| `Extended Kalman-Bucy filter` | `Unscented Kalman filter` | `Unscented Kalman-Bucy filter`

此模块用于估计电池荷电状态的卡尔曼滤波器类型。

### **Alpha** — Alpha 系数 `1`（默认）| 范围 [0, 1] 内的标量

控制 sigma 点分布的系数。该模块在实现无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Beta** — Beta 系数 `2`（默认）| 非负标量

与分布相关的系数。该模块在实现无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Kappa** — Kappa 系数 `0`（默认）| 范围 [0, 3] 内的标量

控制 sigma 点分布的系数。该模块在实现无迹卡尔曼滤波器和无迹卡尔曼-布西滤波器方程时使用此参数。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Unscented Kalman filter` 或 `Unscented Kalman-Bucy filter`。

### **Covariance of the process noise, Q** — 过程噪声协方差 `[1e-6 0; 0 1e-6]`（默认）| 标量矩阵

状态中噪声的 `2`×`2` 协方差矩阵。

### **Covariance of the measurement noise, R** — 测量噪声协方差 `0.1`（默认）| 标量

测量中噪声的协方差。

### **Initial state error covariance, P0** — 初始状态误差协方差 `[1e-5 0; 0 1]`（默认）| 标量矩阵

初始状态误差的 `2`×`2` 协方差矩阵。此参数定义状态初始化时的偏差。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认）| 0 | -1 | 整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`。

### 系统模型

### **Charge dynamics** — 对电池充电动态建模的选项 `One time-constant dynamics`（默认）| `Two time-constant dynamics`

*自 R2024a 起*

对电池充电动态建模的选项。此参数确定等效电路中的并联 RC 段数：

- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)** 和 **First time constant, tau1(SOC,T), (s)** 参数指定极化电阻和时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First polarization resistance, R1(SOC,T), (ohm)**、**First time constant, tau1(SOC,T), (s)**、**Second polarization resistance, R2(SOC,T), (ohm)** 和 **Second time constant, tau2(SOC,T), (s)** 参数指定极化电阻和时间常数。

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围 [0, 1] 内的标量向量

定义指定查找数据点的 SOC 断点向量。此向量的元素必须严格按升序排列。该模块根据 **CellAH** 输入端口的值指定的标称电池容量来计算 SOC 值。SOC 是可用电池电荷 *q*battery 与标称电池容量 *q*nom*(T,n)* 的比值。您必须确保，对于每个温度值，当您对循环次数 *N* 等于 1 且 *δAH(n = 1, Tfade)* 等于 0 的新电池建模时，SOC 为 1 表示 **CellAH** 输入端口对应元素的电池电荷容量。

SOC=qbatteryqnom(T,n)  for N=1  and  δAH(n,Tfade)=0,  qnom(T,n)=AH。

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]`（默认）| 正标量向量

定义指定查找数据点的温度断点向量。此向量必须严格升序且大于 0 K。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **Terminal resistance, R0(SOC,T), (ohm)** — 带温度断点的 R0 查找表 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 正元素矩阵

在指定 SOC 和温度断点处电池串联电阻的查找数据。

### **First polarization resistance, R1(SOC,T), (ohm)** — 温度断点处的第一 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认）| 正元素矩阵

在指定 SOC 和温度断点处第一并联 RC 电阻的查找数据，单位为欧姆。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### **First time constant, tau1(SOC,T), (s)** — 温度断点处的第一 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认）| 正元素矩阵

在指定 SOC 和温度断点处第一并联 RC 时间常数的查找数据，单位为秒。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### **Second polarization resistance, R2(SOC,T), (ohm)** — 温度断点处的第二 RC 电阻 `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]`（默认）| 正元素矩阵

*自 R2024a 起*

在指定 SOC 和温度断点处第二并联 RC 电阻的查找数据，单位为欧姆。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **Second time constant, tau2(SOC,T), (s)** — 温度断点处的第二 RC 时间常数 `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]`（默认）| 正元素矩阵

*自 R2024a 起*

在指定 SOC 和温度断点处第二并联 RC 时间常数的查找数据，单位为秒。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]`（默认）| 非负元素矩阵

在指定 SOC 处基本电池模型开路电压的查找数据，单位为伏特。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### 信号属性

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以在 `single` 和 `double` 精度下仿真该模块。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。
## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2024a：使用具有两个时间常数充电动态的等效模型估计 SOC

您现在可以使用具有两个时间常数充电动态的等效模型来估计电池 SOC。

要选择具有两个时间常数充电动态的等效模型，请将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，并指定新的 **Second polarization resistance, R2(SOC,T), (ohm)** 和 **Second time constant, tau2(SOC,T), (s)** 参数的值。

## 描述

使用卡尔曼滤波器和可变容量的荷电状态估计器

SOC Estimator (Kalman Filter, Variable Capacity) 模块实现了一个估计器，它使用卡尔曼滤波算法计算电池的荷电状态 (SOC)。电池的电芯容量是该模块的输入。

SOC 是释放容量 *C*releasable 与额定容量 *C*rated 的比值。制造商提供每个电池的额定容量值，它表示电池中的最大电荷量：

SOC=CreleasableCrated.

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型必须为 `single`。

对于连续时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman-Bucy filter` 或 `Unscented Kalman-Bucy filter`。

**注意**

此模块的连续时间实现仅在双精度浮点仿真中工作。如果您提供单精度浮点参数和输入，此模块会将它们转换为双精度浮点值以防止错误。

对于离散时间仿真，请将 **Filter type** 参数设置为 `Extended Kalman filter` 或 `Unscented Kalman filter`，并将 **Sample time (-1 for inherited)** 参数设置为正值或 `-1`。

### 方程

这些图分别展示了具有单时间常数动态特性和双时间常数动态特性的电池等效电路：

具有双时间常数动态特性的等效电路方程为：

dSOCdt=−i3600AHdV1dt=iC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)dV2dt=iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)Vt=V0(SOC,T)−iR0−V1−V2

其中

- *SOC* 是荷电状态。
- *i* 是电流。
- *V*0 是开路电压。
- *V*t 是端电压。
- *AH* 是安时额定容量。
- *R*1 是第一极化电阻。
- *C*1 是第一并联 RC 电容。
- *R*2 是第二极化电阻。
- *C*2 是第二并联 RC 电容。
- *T* 是温度。
- *V*1 是第一个 RC 网络上的极化电压。
- *V*2 是第二个 RC 网络上的极化电压。

第一个并联部分的时间常数 *τ*1 通过关系式 C1=τ1/R1 将第一极化电阻 *R*1 与第一并联 RC 电容 *C*1 关联起来。

第二个并联部分的时间常数 *τ*2 通过关系式 C2=τ2/R2 将第二极化电阻 *R*2 与第二并联 RC 电容 *C*2 关联起来。

对于卡尔曼滤波算法，该模块使用以下状态以及这些过程函数和观测函数：

x=[SOCV1]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)]h(x,i)=V0(SOC,T)−iR0−V1

如果将 **Charge dynamics** 参数设置为 `Two time-constant dynamics`，则对于卡尔曼滤波算法，该模块使用以下状态以及这些过程函数和观测函数：

x=[SOCV1V2]Tf(x,i)=[−i3600AHiC1(SOC,T)−V1R1(SOC,T)C1(SOC,T)iC2(SOC,T)−V2R2(SOC,T)C2(SOC,T)]h(x,i)=V0(SOC,T)−iR0−V1−V2

**扩展卡尔曼滤波器**

此图展示了扩展卡尔曼滤波器（EKF）的结构：

EKF 技术依赖每个时间步的线性化来近似非线性系统。为了在每个时间步对系统进行线性化，该算法在线计算以下雅可比矩阵：

F=∂f∂xH=∂h∂x

EKF 是一种离散时间算法。离散化后，用于电池 SOC 估计的雅可比矩阵为：

Fd=[100e−TSR1C1]Hd=[∂VOC∂SOC−1]

其中 *T*S 是采样时间，*V*OC 是开路电压。

EKF 算法包括以下阶段：

- **初始化**

  - x^(0|0)⁠——使用时间步 0 的测量值在时间步 0 的状态估计。
  - P^(0|0)⁠——使用时间步 0 的测量值在时间步 0 的状态估计误差协方差矩阵。
- **预测**

  - 将状态向前投影（*先验*）：

    x^(k+1|k)=f(x^(k|k),i)。
  - 将误差协方差向前投影：

    P^(k+1|k)=Fd(k)P^(k|k)FdT(k)+Q，

    其中 **Q** 是过程噪声的协方差。
- **校正**

  - 计算卡尔曼增益：

    K(k+1)=P^(k+1|k)HdT(k)(Hd(k)P^(k+1|k)HdT(k)+R)−1，

    其中 *R* 是测量噪声的协方差。
  - 使用测量值 *y(k)* 更新估计（*后验*）：

    x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k)−h(x^(k|k),i))。
  - 更新误差协方差：

    P^(k+1|k+1)=(I−K(k+1)Hd)P^(k+1|k)。

**扩展卡尔曼-布西滤波器**

此图展示了扩展卡尔曼-布西滤波器（EKBF）的结构：

EKBF 是卡尔曼滤波器的连续时间变体。在连续时间中，预测步骤和校正步骤是耦合的。

- **初始化**

  - x^(t0)⁠——在时间 *t*0 的状态估计。
  - P^(t0)⁠——在时间 *t*0 的状态估计误差协方差矩阵。
- **预测-校正 EKBF 算法**

  K(t)=P(t)HT(t)R−1(t)dx^(t)dt=f(x^(t),i(t))+K(t)(Vt(t)−h(x^(t),i(t)))dP(t)dt=F(t)P(t)+P(t)FT(t)+Q(t)−K(t)H(t)P(t)

  其中：

  F(t)=∂f∂xH(t)=∂h∂x

**无迹卡尔曼滤波器**

此图展示了无迹卡尔曼滤波器（UKF）的结构：

EKF 通过仅使用泰勒展开的第一项，用由泰勒展开获得的线性方程局部近似非线性函数。在高度非线性的系统中，这些解不是很准确。

UKF 对一组 sigma 点使用非线性变换，这些点由算法确定性地选择。这种技术称为*无迹变换*。变换后点的均值和协方差矩阵在泰勒级数展开的二阶范围内是准确的。

UKF 算法遵循以下步骤：

- **初始化**

  - x^(0|0)⁠——使用时间步 0 的测量值在时间步 0 的状态估计。
  - P^(0|0)⁠——使用时间步 0 的测量值在时间步 0 的状态估计误差协方差矩阵。
- 生成 sigma 点，并计算每个点的均值权重和协方差权重。

  - 选择 sigma 点 *x(i)(k|k)*

    x(i)(k|k)={x^(k+1|k)i=1x^(k+1|k)+((n+λ)P(k|k))ii=2,…,n+1x^(k+1|k)−((n+λ)P(k|k))ii=n+2,…,2n+1Wm(i)={λn+λi=112(n+λ)i≠1Wc(i)={λn+λ+(1−α2+β)i=112(n+λ)i≠1

    其中：

    - *n* 是状态向量 *x* 的维度。
    - λ=α2(n+κ)−n, α∈[0,1] 描述 sigma 点与均值点之间的距离。在正态分布中，*β =* 2 且 *κ =* 0。
    - ((n+λ)P)i 是 cP 的第 *i* 行或第 *i* 列。该模块通过使用数值高效且稳定的方法（例如 Cholesky 分解）来计算矩阵平方根。
- 执行系统状态矩阵的第一次估计：

  x^(i)(k+1|k)=f(x^(i)(k|k),i(k))x^(k+1|k)=∑i=12n+1Wm(i)x^(i)(k+1|k)
- 执行状态变量协方差矩阵的第一次估计：

  P(k+1|k)=∑i=12n+1Wc(i)(x^(i)(k+1|k)−x^(k+1|k))⋅(x^(i)(k+1|k)−x^(k+1|k))T+Q
- 估计测量变量：

  Vt(i)(k+1|k)=h(x^(i)(k+1|k),i(k))V^t(k+1|k)=∑i=12n+1Wm(i)V^t(i)(k+1|k)
- 估计测量的协方差（*Py*）以及测量与状态之间的协方差（*Pxy*）：

  Py=∑i=12n+1Wc(i)(V^t(i)(k+1|k)−V^t(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T+RPxy=∑i=12n+1(x^(i)(k+1|k)−x^(k+1|k))⋅(V^t(i)(k+1|k)−V^t(k+1|k))T
- 计算卡尔曼滤波器增益：

  K(k+1)=PxyPy−1
- 执行状态矩阵和状态变量协方差的第二次更新：

  x^(k+1|k+1)=x^(k+1|k)+K(k+1)(Vt(k+1)−V^t(k+1|k))P(k+1|k+1)=P(k+1|k)−K(k+1)PyKT(k+1)

**无迹卡尔曼-布西滤波器**

此图展示了无迹卡尔曼-布西滤波器（UKBF）的整体结构：

UKBF 推导出的连续时间滤波方程与 EKBF 方程类似。

由于 UKF 在其 sigma 点中使用矩阵平方根，该算法通过将滤波器表述为 sigma 点的微分方程来获得 UKBF 的平方根版本。平方根 UKBF 的方程为：

K(t)=X(t)WhT(X(t),t)R−1(t)M(t)=A−1(t)[X(t)WfT(X(t),t)+f(X(t),t)WXT(t)+Q(t)−K(t)R(t)KT(t)]A−T(t)dXi(t)dt=f(X(t),t)wm+K(t)(Vt(t)−h(X(t),t)wm)+c[0A(t)Φ(M(t))−A(t)Φ(M(t))]i

其中

- X(t)=[m(t)…m(t)]+c[0A(t)−A(t)] 是 sigma 点矩阵。
- Φij(M(t))={Mij(t),i>j0.5Mij(t),i=j0,i<j 是一个函数，返回参数的下对角部分。
- wm=[Wm(1)⋯Wm(2n+1)]T
- W=(1−[wm⋯wm])diag(Wc(1)⋯Wc(2n+1))(I−[wm⋯wm])T
- c=α2(n+κ)
- [0A(t)Φ(M(t))−A(t)Φ(M(t))]i 是参数矩阵的第 *i* 列。
