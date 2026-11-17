---
type: simulink-block
title: 'Battery Power Estimator'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'batterypowerestimator'
documentation_source_path: 'ref/batterypowerestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Power Estimator

## 端口

### 输入

### **CellSOC** — 单体荷电状态，无量纲标量 | 向量

一个或多个单体的荷电状态，指定为范围在 [0,1] 内的标量或向量。此输入端口的尺寸必须等于 **CellTemperature** 输入端口的尺寸，并且等于 **Number of series modules, Ns** 参数的值。

### **CellTemperature** — 单体温度，K 标量 | 向量

单体温度，对于单个单体指定为标量，对于多个单体指定为向量。此输入端口的尺寸必须等于 **CellSOC** 输入端口的尺寸，并且等于 **Number of series modules, Ns** 参数的值。
### 输出

### **MaxPowerDischarging** — 电池放电最大功率，W 标量

在预测时域内电池放电的最大功率。

### **MaxPowerCharging** — 电池充电最大功率，W 标量

在预测时域内电池充电的最大功率。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 电池

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| 范围在 [0, 1] 内的标量向量

荷电状态断点的向量，用于定义指定查找数据的点。此向量的元素必须严格按升序排列。模块根据 **Cell capacity, AH (A\*Hr)** 参数中指定的标称电池容量计算荷电状态值。SOC 是可用电池电荷 *q*battery 与标称电池容量 *q*nom*(T,n)* 的比值。请确保，对于每个温度值，当您对循环次数 *N* 等于 1 且 *δAH(n = 1, Tfade)* 等于 0 的新电池进行建模时，SOC 为 1 表示对应于 **Cell capacity, AH (A\*Hr)** 参数相应元素的电池电荷容量：

SOC=qbatteryqnom(T,n)  for N=1  and  δAH(n,Tfade)=0,  qnom(T,n)=AH.

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]`（默认）| 正标量向量

温度断点的向量，用于定义指定查找数据的点。此向量必须严格按升序排列且大于 0 K。此参数的物理单位必须与 **CellTemperature** 输入端口的物理单位相同。

### **No-load voltage, V0(SOC,T), (V)** — *V*0 查找表 `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]`（默认）| 非负元素矩阵

在指定 SOC 下基本电池模型开路电压的查找数据，单位为伏特。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### **Charging pulse test resistance, R0Dt(SOC,T), (ohm)** — `Δt` 秒脉冲期间的充电电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 非负元素矩阵

`Δt` 秒脉冲期间的充电电阻。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### **Discharging pulse test resistance, R0Dt(SOC,T), (ohm)** — `Δt` 秒脉冲期间的放电电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 非负元素矩阵

`Δt` 秒脉冲期间的放电电阻。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的尺寸。此矩阵的列数等于 **Vector of temperatures, T** 参数的尺寸。

### **Cell capacity, AH (A\*Hr)** — 完全充电时的电池容量 `27`（默认）| 非负标量

电池的单体容量，单位为安培小时。模块通过将累积电荷除以此值来计算荷电状态。模块通过对电池电流进行积分来计算累积电荷。

### **Number of series modules, Ns** — 串联模块数 `10`（默认）| 正标量

电池组内串联连接的模块数。

### **Number of parallel modules, Np** — 并联模块数 `1`（默认）| 正标量

电池组内并联连接的模块数。

### **Charging efficiency ratio** — 充电效率比 `1`（默认）| 范围在 (0,1] 内的非负标量

充电效率比。

### 限值

### **Minimum cell voltage (V)** — 单体最小电压 `2.5`（默认）| 正标量

电池单体的最小电压，单位为伏特。此参数的值必须小于 **Maximum cell voltage (V)** 参数的值。

### **Maximum cell voltage (V)** — 单体最大电压 `4.5`（默认）| 正标量

电池单体的最大电压，单位为伏特。此参数的值必须大于 **Minimum cell voltage (V)** 参数的值。

### **Minimum state of charge, SOCmin(-)** — 最小荷电状态 `0.1`（默认）| 范围在 [0,1] 内的非负标量

电池单体的最小荷电状态。此参数的值必须小于 **Maximum state of charge, SOCmin(-)** 参数的值。

### **Maximum state of charge, SOCmax(-)** — 最大荷电状态 `0.9`（默认）| 范围在 [0,1] 内的非负标量

电池单体的最大荷电状态。此参数的值必须大于 **Minimum state of charge, SOCmax(-)** 参数的值。

### **Minimum pack current (A)** — 电池组最小电流 `-200`（默认）| 负标量

电池组的最小电流，单位为安培。此参数的值必须小于 **Maximum pack current (A)** 参数的值。如果将此值设置为 `-inf`，模块将忽略此参数。

### **Maximum pack current (A)** — 电池组最大电流 `200`（默认）| 正标量

电池组的最大电流，单位为安培。此参数的值必须大于 **Minimum pack current (A)** 参数的值。如果将此值设置为 `inf`，模块将忽略此参数。

### **Minimum cell power (W)** — 电池单体最小功率 `-inf`（默认）| 负标量

电池单体的最小功率，单位为瓦特。此参数的值必须小于 **Maximum cell power (W)** 参数的值。如果将此值设置为 `-inf`，模块将忽略此参数。

### **Maximum cell power (W)** — 电池单体最大功率 `inf`（默认）| 正标量

电池单体的最大功率，单位为瓦特。此参数的值必须大于 **Minimum cell power (W)** 参数的值。如果将此值设置为 `inf`，模块将忽略此参数。

### **Time horizon (s)** — 时间范围 `10`（默认）| 正标量

模块计算电池组最大充电和放电功率能力的时间，单位为秒。

### 信号属性

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度对模块进行仿真。您必须将输入和参数显式提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

计算电池组在时间范围内的最大充电和放电功率

Battery Power Estimator 模块计算电池组在指定时间范围内的最大充电和放电功率能力。此模块遵循的符号约定为：在电池充电过程中，电流和功率为正值。

此图显示了模块的结构：

### 方程

为了估计电池组的最大充电和放电功率能力，Battery Power Estimator 模块使用混合脉冲功率特性 (HPPC) 方法 [1]。

脉冲测试电压（Y 轴）与时间（X 轴）的关系图

为了计算放电和充电电流，模块使用以下方程：

idischg,volt,n=−V0(SOC,T)−vminRdischgDtichg,volt,n=−V0(SOC,T)−vmaxRchgDt

其中：

- `V0(SOC,T)` 是开路电压。
- `vmin` 和 `vmax` 是最小和最大单体电压。
- `RdischgDt` 和 `RchgDt` 是 `Δt` 秒脉冲期间的放电和充电电阻。
- `idischg,volt,n` 和 `ichg,volt,n` 是基于电压约束的第 `n` 个单体的放电和充电电流。

对于恒定电流 `in`，荷电状态 (SOC) 关系为

SOCn(t+Δt)=SOCn(t)−η Δt in 3600 Q,

其中：

- *Q* 是以安培小时为单位的容量。
- *SOCn* 是第 *n* 个单体的荷电状态。
- *η* 是效率因子，对于放电 *η* = *1*，对于充电 *η* ≤ `1`。

最小和最大允许值限制电池组中所有单体的荷电状态，使得

SOCmin≤SOCn(t)≤SOCmax.

然后模块基于 SOC 计算电流限值：

idischg,SOC,n=−3600⋅Q⋅(SOCn−SOCmin)Δtichg,SOC,n=−3600⋅Q⋅(SOCn−SOCmax)ηΔt

为了计算整个电池组的放电和充电电流，模块使用以下方程：

idischg=max(imin,maxnidischg,SOC,n,maxnidischg,volt,n)ichg=min(imax,minnichg,SOC,n,minnichg,volt,n)

最后，模块计算预测时域 `Δt` 的充电和放电功率限值：

Pmax,dischg=Npmax(NsPmin,∑n=1Nsidischg(V0(SOCn(t)−idischgΔt3600 Q,T)−idischgRdischgDt))Pmin,chg=Npmin(NsPmax,∑n=1Nsichg(V0(SOCn(t)−ichgηΔt3600 Q,T)−ichgRchgDt))

其中 *Np* 是并联模块数，*Ns* 是串联模块数。

### 假设和限制

在电池充电过程中，电流和功率为正值。
