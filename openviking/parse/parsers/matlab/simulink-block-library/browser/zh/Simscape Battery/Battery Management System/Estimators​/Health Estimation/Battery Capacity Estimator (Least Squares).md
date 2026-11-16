---
type: simulink-block
title: 'Battery Capacity Estimator (Least Squares)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / Health Estimation'
documentation_page: 'batterycapacityestimatorleastsquares'
documentation_source_path: 'ref/batterycapacityestimatorleastsquares.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Capacity Estimator (Least Squares)

## 端口

### 输入

### **Current** — 电池电流，A scalar | vector

电池电流，以安培为单位，指定为单个电池单元的 scalar 或用于多个电池单元的 vector。要将此输入指定为电池单元电流的 vector，请选择 **Specify Current input as cell current(s)** 参数。如果选择此参数，此输入端口的大小必须等于其他输入端口的大小。

### **CellSOC** — 电池单元荷电状态，unitless scalar | vector

一个或多个电池单元的荷电状态，指定为范围 [0, 1] 内的 scalar 或 vector 项。此输入端口的大小必须等于 **InitialCellAH** 输入端口的大小。

### **InitialCellAH** — 初始电池单元容量，A\*Hr scalar | vector

电池的初始电池单元容量，以安培小时为单位，指定为单个电池单元的 scalar 或用于多个电池单元的 vector。此输入端口的大小必须等于 **CellSOC** 输入端口的大小。
### 输出

### **CellAH** — 估计的电池单元容量，A\*Hr scalar | vector

电池的估计电池单元容量，以安培小时为单位，返回为 scalar 或 vector。此输出端口的大小等于 **InitialCellAH** 输入端口的大小。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Specify Current input as cell current(s)** — 用于将 current 输入端口指定为 vector 的选项 `off` (default) | `on`

用于将 **Current** 输入端口的值指定为电池单元电流 vector 的选项。如果选择此参数，则 **Current** 输入端口处的值可以是 scalar，也可以是大小等于模块输入大小的 vector。

### **Least square algorithm** — 最小二乘算法 `Ordinary least squares` (default) | `Recursive total least squares` | `Approximate total least squares`

模块用于估计电池单元容量的最小二乘算法。

### **SOC change detection threshold** — 用于检测 SOC 变化的阈值 `0.03` (default) | scalar in the range (0,1)

用于检测 SOC 变化的阈值。典型值为 0.05 或 0.03，分别表示 5% 或 3% 的变化。

### **Forgetting factor, gamma** — 遗忘因子 `0.9` (default) | scalar in the range (0,1]

遗忘因子。

### **Variance of SOC, VarianceX** — SOC 的方差 `2e-4` (default) | positive scalar

电池 SOC 的方差。

#### 依赖关系

要启用此参数，请将 **Least squares algorithm** 设置为 `Approximate total least squares`。

### **Variance of current measurement, VarianceY** — 电流测量的方差 `5e-7` (default) | positive scalar

电流测量的方差。

### **Scaling factor k in VarianceX=k^2\*VarianceY** — 缩放因子 *k* `10` (default) | positive scalar

缩放因子 *k*。

#### 依赖关系

要启用此参数，请将 **Least squares algorithm** 设置为 `Recursive total least squares` 或 `Approximate total least squares`。

### **Sample time (-1 for inherited)** — 模块采样时间 `1` (default) | `0` | `-1` | positive integer

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的 masked subsystem 或 variant subsystem 中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Algorithm data type** — 用于选择模块算法数据类型的选项 `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 可以在 `single` 和 `double` 精度下仿真该模块。必须显式将输入和参数提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2024a 中引入**

### R2025a: 使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **Algorithm data type** 参数，轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

使用最小二乘算法的电池容量估计器

Battery Capacity Estimator (Least Squares) 模块使用最小二乘算法计算电池的电池单元容量。

对于离散时间仿真，请将 **Sample time** 参数设置为正值。要继承采样时间，请将 **Sample time** 设置为 `-1`。对于连续时间仿真，请将 **Sample time** 设置为 `0`。

下图显示了该模块的结构：

### 方程

最小二乘估计通过最小化残差平方和，为一组数据点找到最佳拟合线。残差平方是模型的观测响应与预测响应之间的差。此最佳拟合线用于预测因变量。

此方程定义时间 *t*n2 处的电池荷电状态 (SOC)，

SOC(tn2)=SOC(tn1)+1Q∫tn1tn2i(τ)dτ,

其中：

- *SOC*(*t*n1) 是时间 *t*n1 处的 SOC，其中 *n*={1,…,N}。
- *Q* 是以安培小时为单位的容量。
- *i* 是电池单元电流，以安培为单位。
- ∫tn1tn2i(τ)dτ 表示在时间区间 *t*n2 - *t*n1 上积分的电池单元电流。为了使单位一致，时间 *t*n1 和 *t*n2 必须以小时为单位。

定义 xn=SOC(tn2)−SOC(tn1) 和 yn=∫tn1tn2i(τ)dτ，并重写 SOC 方程：

yn=Qxn.

该模块使用此线性方程，通过最小二乘估计来确定电池单元容量的估计值，

(yn−Δyn)=Q^(xn−Δxn),

其中：

- *Δx*n 是与 SOC 估计相关的误差。
- *Δy*n 是与电流传感器相关的误差。
- Q^ 是在有噪声测量下真实电池单元容量的估计值。

**Ordinary Least Squares**

加权普通最小二乘 (OLS) 方法通过最小化评价函数的加权平方误差 *Δy*n 来估计电池单元容量

xWLS2=∑n=1N(yn−Yn)2σyn2=∑n=1N(yn−Q^xn)2σyn2,

其中 *σ*2yn 表示电流测量的方差，*Y*n 是直线 Yn=Q^xn 上与测量数据点 {*x*n,*y*n} 对应的点。该模块假设 *y*n 有噪声，而 *x*n 无噪声。

为求解加权 OLS 问题，该模块对评价函数关于 Q^ 求导，并通过将偏导数设置为零来求解 Q^ [1]：

∂xWLS2∂Q^=−2∑n=1Nxn(yn−Q^xn)σyn2=0Q^∑n=1Nxn2σyn2=∑n=1Nxnynσyn2Q^=∑n=1Nxnynσyn2∑n=1Nxn2σyn2

此方法可以递归计算，并且易于调整以允许过去测量淡出。

如果将遗忘因子定义为 0≪γ≤1，则该模块通过以下方程获得估计容量

Q^=k2,nk1,n,

其中：

k1,n=γk1,n−1+xn2σyn2k2,n=γk2,n−1+xnynσyn2

**Total Least Squares**

加权总体最小二乘 (TLS) 方法通过最小化评价函数的两个加权平方误差 *Δx*n 和 *Δy*n 之和来估计电池单元容量 [1],[2]，

χWLTS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2,

其中 *σ*2yn 表示电流测量的方差，*σ*2xn 表示 SOC 估计误差的方差，*X*n 和 *Y*n 是直线 Yn=Q^Xn 上与含噪声测量数据点 {*x*n,*y*n} 对应的点。

为强制满足 Yn=Q^Xn，该模块使用 Lagrange 乘子 *λi* 增广评价函数：

χWLTS,a2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2−λi(Yn−Q^Xn).

该模块将 χWLTS,a2 关于 *λi*、*Y*n 和 *X*n 的偏导数设置为零：

∂χWLTS,a2∂λi=−(Yn−Q^Xn)=0→Yn=Q^Xn∂χWLTS,a2∂Yn=−2(yn−Yn)σyn2−λi=0→λi=−2(yn−Yn)σyn2∂χWLTS,a2∂Xn=−2(xn−Xn)σxn2+λiQ^=0→Xn=xnσyn2+Q^ynσxn2σyn2+Q^2σxn2

然后，该模块将评价函数重写为 [1]：

χWLTS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2=∑n=1N(yn−Q^xn)2σyn2+Q^2σxn2.

最后，该模块将 χWLTS2 关于 Q^ 的偏导数设置为零：

∂χWLTS2∂Q^=∑n=1N2(Q^xn−yn)(Q^ynσxn2+xnσyn2)(Q^2σxn2+σyn2)2=0.

在此方程中：

- 一般情况下没有闭式解。为找到闭式解，请对 Q^ 执行 Newton-Raphson 搜索。
- 一般情况下没有递归更新。
- 该解不适用于在嵌入式系统中实现。

**Recursive Approximation of Total Least Squares (RTLS)**

该模块在 χWLTS2 的方程中代入 σxn=kσyn：

χRTLS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2kσyn2=∑n=1N(yn−Q^xn)2(Q^2k2+1)σyn2.

WTLS 评价函数的偏导数简化为：

∂χRTLS2∂Q^=2∑n=1N(Q^xn−yn)(Q^k2yn+xn)(Q^2k2+1)2σyn2=0Q^2∑n=1Nk2xnynσyn2︸a+∑n=1Nk2xn2−k2yn2σyn2︸b+∑n=1N−xnynσyn2︸c=0Q^=−b±b2−4ac2a

该模块通过以下方程引入衰减记忆

Q^=−k1,n+k2k3,n+(k1,n−k2k3,n)2+4k2k2,n22k2k2,n,

其中：

k1,n=γk1,n−1+xn2σyn2k2,n=γk2,n−1+xnynσyn2k3,n=γk3,n−1+yn2σyn2

**Approximate Total Least Squares (ATLS)**

ATLS 方法是递归的，并允许 *σ*2yn 和 *σ*2xn 不成比例。

下图显示了该模块用于推导近似加权总体最小二乘的定义：

该模块将 *Δx*n 和 *Δy*n 分别定义为数据点 *n* 与直线之间的 *x* 距离和 *y* 距离。对于所有 *n*，直线的斜率为 Q^=ΔynΔxn。直线的角度为 θ=tan−1Q^。

此方程定义直线与给定数据点之间的最短距离：

Rn=Δyncosθ=Δyn1+Q^2.

如果 δxi=Risinθ 且 δyi=Ricosθ，则该模块定义数据点 *n* 与拟合直线之间垂直距离的 *x* 和 *y* 分量。然后，该模块可以使用以下方程定义 AWTLS 评价函数：

χAWTLS2=∑n=1Nδxn2σxn2+δyn2σyn2=∑n=1N(yn−Q^xn)2(Q^2+1)2(Q^2σxn2+1σyn2).

此方程定义 AWTLS 评价函数的 Jacobian：

∂χAWTLS2∂Q^=2(Q^2+1)3∑n=1NQ^4xnynσxn2+Q^3(2xn2σxn2−xn2σyn2−yn2σxn2)+Q^2(3xnynσyn2−3xnynσxn2)+Q^(xn2−2yn2σyn2+yn2σxn2)+−xnynσyn2.

四次方程的根是 Q^ 的候选解。该模块将四次方程重写为

c5,nQ^4+(2c4,n−c1,n−c6,n)Q^3+(3c2,n−3c5,n)Q^2+(c1,n−2c3,n+c6,n)Q^−c2,n=0,

其中：

c1,n=γc1,n−1+xn2k2σyn2c2,n=γc2,n−1+kxnynk2σyn2c3,n=γc3,n−1+yn2σyn2c4,n=γc4,n−1+xn2σxn2c5,n=γc5,n−1+kxnynσxn2c6,n=γc6,n−1+k2yn2σxn2

当 σxn=kσyn 时，ATLS 评价函数不等于加权 TLS 评价函数。

当 σxn=kσyn 时，该模块使用以下方程估计真实电池单元容量：

Q^corrected=Q^k.

### 实现

下图显示了该模块如何使用不同的最小二乘算法估计电池容量：

在 Data Acquisition 阶段，该模块循环运行，直到算法找到有效数据点。该模块遵循以下步骤：

1. 该模块使用 SOC 估计器在时间 *t*n1 接收一个 SOC 估计值。
2. 该模块在时间 *t*n2 接收第二个 SOC 估计值。
3. 当 SOC(tn1)−SOC(tn2)<SOCmin\_change 时，该模块：

   - 持续接收 SOC 估计值。
   - 对电池单元电流积分，yn=∫tn1tn2i(τ)dτ。
   - 用新时间戳覆盖时间 *t*n2。
   - 如果电池正在充电，则该模块丢弃该测量值并返回步骤 1。

### 假设和限制

- 该模块假设随机误差 *Δx*n 和 *Δy*n 遵循零均值正态分布。
- 该模块假设权重 *σ*2xn 和 *σ*2yn 是已知的。
- 在 RTLS 算法中，缩放因子 *k* 必须使权重 *σ*2xn 和 *σ*2yn 成比例关系，使得 σxn=kσyn
