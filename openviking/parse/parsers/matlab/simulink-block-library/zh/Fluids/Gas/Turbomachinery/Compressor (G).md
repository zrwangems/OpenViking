---
type: simulink-block
title: 'Compressor (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Turbomachinery'
documentation_page: 'compressorg'
documentation_source_path: 'ref/compressorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Compressor (G)

## 端口

### 守恒

### **A** — 气体入口 gas

与压缩机入口相关联的气体守恒端口。

### **B** — 气体出口 gas

与压缩机出口相关联的气体守恒端口。

### **C** — 压缩机机壳 机械平移

与压缩机机壳相关联的机械平移守恒端口。

### **R** — 压缩机轴 机械平移

与压缩机轴扭矩和角速度相关联的机械平移守恒端口。
### 输出

### **SM** — 喘振裕度 物理信号

与给定质量流量下的喘振裕度相关联的物理信号输出端口。模块计算喘振裕度如下：

SM(m˙corr)=pr,surge(m˙corr)pr(m˙corr)−1.

#### 依赖项

要启用此端口，将 **Parameterization** 设置为
`Tabulated`。

## 参数

### 压缩机特性图

### **Parameterization** — 压缩机性能参数化 `Analytical`（默认）| `Tabulated`

压缩机性能参数化。选择 `Analytical` 或 `Tabulated` 参数化：

- `Analytical`：压比–修正质量流量曲线定义峰值
  压缩机性能。您可以选择将等熵效率建模为常数或解析式。
- `Tabulated`：用户提供的
  压缩机特性图定义压缩机性能。模块
  使用线性插值在修正质量流量、压比
  和等熵效率表之间确定压缩机工作点，这些表基于
  用户提供的修正轴转速和 β 向量中的给定点。默
  认特性图来自 [3] 中报告的数据。

### **Corrected speed at design point** — 运行修正轴转速 `10000` `rpm`（默认）| 正标量

在目标压缩机压比和修正质量流量下的轴转速，
已对温度进行修正。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Pressure ratio at design point** — 运行出口至入口压比 `7.5`（默认）| 正标量

在目标压缩机修正质量流量下的出口至入口压比。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Corrected mass flow rate at design point** — 运行修正质量流量 `33` `kg/s`（默认）| 正标量

在目标压缩机压比下的质量流量，已对温度和压力进行修正。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Efficiency specification** — 等熵效率模型 `Analytical`（默认）| `Constant`

等熵效率模型类型。选择常数或解析式
模型。使用 `Analytical` 指定变量
值。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Maximum isentropic efficiency** — 最大压缩机效率 `0.887`（默认）| 范围 (0,1] 内的正标量

最大压缩机等熵效率。等熵效率是
等熵变化与实际变化之比。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Minimum isentropic efficiency** — 最小压缩机效率 `0.5`（默认）| 范围 (0,1] 内的正标量

最小压缩机等熵效率。等熵效率是
等熵变化与实际变化之比。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Corrected mass flow rate at maximum efficiency point** — 压缩机最大效率点的修正质量流量 `30` `kg/s`（默认）| 正标量

最大效率下的质量流量，已对温度和压力进行修正。最大效率点
不一定与压缩机
设计点重合。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Pressure ratio at maximum efficiency point** — 压缩机最大效率下的压比 `7`（默认）| 正标量

最大效率下的压比。最大效率点不一定
与压缩机设计点重合。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Constant isentropic efficiency** — 常数等熵效率值 `0.8`（默认）| 范围 (0,1] 内的正标量

解析式参数化中常数等熵效率的值。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Constant`。

### **Corrected speed index vector, N** — 修正轴转速向量 `[5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000]` `rpm`（默认）| 向量

修正轴转速向量。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### **Beta index vector, beta** — 修正转速线区间向量 `0 : 1 / 6 : 1`（默认）| 范围 [0,1] 内元素的向量

沿修正转速线的相对位置向量。当 β = 0 时发生阻塞
流，当 β = 1 时发生喘振流。β 线
垂直于压缩机轴等转速线
*N*。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### **Pressure ratio table, pr(N,beta)** — 压缩机特性图压比数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值下的压缩机出口至入口
压比的 *M*×*N* 矩阵。模块
在表元素之间采用线性插值。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N**
  参数中向量元素的数量。
- *N* 是 **Beta index vector, beta**
  参数中向量元素的数量。

默认值为：

`[1.369, 1.459, 1.587, 1.654, 1.734, 1.775, 1.82; 1.918,
2.075, 2.229, 2.318, 2.405, 2.456, 2.481; 2.706, 2.966, 3.168,
3.334, 3.404, 3.445, 3.435; 3.203, 3.533, 3.833, 4.021, 4.127,
4.135, 4.066; 3.782, 4.222, 4.565, 4.867, 5.065, 5.07, 4.934; 4.302,
4.861, 5.285, 5.821, 6.161, 6.334, 6.142; 4.841, 5.445, 5.988,
6.628, 7.222, 7.623, 7.573; 5.358, 5.997, 6.589, 7.334, 8.012,
8.668, 9; 5.851, 6.491, 7.124, 7.982, 8.754, 9.57, 9.814; 6.707,
7.321, 8.034, 9.047, 9.94, 10.834, 10.998]`

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### **Corrected mass flow rate table, mdot(N,beta)** — 压缩机特性图修正质量流量数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值下的修正质量流量的
*M*×*N* 矩阵。模块在表元素之间采用线性
插值。*M* 和
*N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N**
  参数中向量元素的数量。
- *N* 是 **Beta index vector, beta**
  参数中向量元素的数量。

默认值为：

`[10.45, 10.203, 9.784, 9.526, 9.144, 8.947, 8.615; 13.315,
13.018, 12.525, 11.984, 11.455, 11.086, 10.914; 17.601, 17.204,
16.502, 15.8, 14.903, 14.179, 13.184; 20.331, 19.983, 19.39, 18.492,
17.435, 16.293, 14.895; 23.466, 23.092, 22.572, 21.807, 20.687,
19.3, 17.682; 26.295, 26.091, 25.766, 25.28, 24.453, 23.26, 21.311;
29.013, 28.747, 28.641, 28.412, 28.06, 27.098, 25.306; 31.424,
31.379, 31.273, 31.103, 30.849, 30.484, 29.718; 33.688, 33.606,
33.561, 33.513, 33.392, 33.258, 33.059; 37.678, 37.621, 37.575,
37.598, 37.501, 37.415, 37.413] kg/s`

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### **Isentropic efficiency table, eta(N,beta)** — 压缩机特性图等熵效率数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值下的压缩机等熵
效率的 *M*×*N* 矩阵。模块
在表元素之间采用线性插值。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N**
  参数中向量元素的数量。
- *N* 是 **Beta index vector, beta**
  参数中向量元素的数量。

默认值为：

`[.68, .69, .695, .7, .701, .705, .704; .7, .725, .75, .755,
.745, .73, .725; .77, .795, .81, .805, .78, .765, .745; .795, .812,
.825, .82, .805, .78, .75; .82, .837, .848, .849, .835, .805, .78;
.83, .845, .856, .86, .855, .84, .8; .83, .848, .859, .869, .86,
.852, .83; .828, .845, .857, .869, .862, .855, .85; .806, .83, .85,
.86, .859, .857, .853; .79, .8, .82, .835, .845, .848,
.849]`

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### **Report when surge margin is negative** — 当压比超过喘振压比时是否通知 `None`（默认）| `Warning` | `Error`

当模块检测到负喘振裕度时，是执行无操作、生成警告还是生成
错误。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Tabulated`。

### 特性图系数

要启用 **特性图系数** 参数，将
**Parameterization** 设置为
`Analytical`。

### **Spine shape, a** — 脊线形状指数 `1.5`（默认）| 正标量

压缩机特性图解析式参数化中表征
脊线形状的指数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Speed line spread, b** — 等转速线间距指数 `5`（默认）| 正标量

压缩机特性图解析式参数化中表征
等转速线间距的指数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Speed line roundness, k** — 等转速线形状系数 `0.03`（默认）| 正标量

压缩机特性图解析式参数化中表征
等转速线形状的系数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`。

### **Efficiency peak flatness orthogonal to spine, c** — 表征解析式等熵效率形状的指数 `3`（默认）| 正标量

与压缩机特性图垂直于脊线的峰值平坦度
相关的指数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Efficiency peak flatness along spine, d** — 表征解析式等熵效率形状的指数 `4`（默认）| 正标量

与沿脊线的效率特性图峰值平坦度
相关的指数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Efficiency contour gradient orthogonal to spine, C** — 表征解析式等熵效率形状的系数 `15`（默认）| 正标量

与垂直于脊线的效率等值线梯度
相关的系数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Efficiency contour gradient along spine, D** — 表征解析式等熵效率形状的系数 `1`（默认）| 范围 (0,1] 内的正标量

与沿脊线的效率等值线梯度相关的
系数。

#### 依赖项

要启用此参数，将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### 参数

### **Reference pressure for corrected flow** — 修正压力 `0.101325` `MPa`（默认）| 正标量

压缩机特性图的参考入口压力。当您将
**Parameterization** 设置为
`Tabulated` 时，数据提供者相对于
表格化压缩机数据指定此值。当您将
**Parameterization** 设置为
`Analytical` 时，此值是设计
工况下的入口压力。

### **Reference temperature for corrected flow** — 修正温度 `288.15` `K`（默认）| 正标量

压缩机特性图的参考入口温度。当您将
**Parameterization** 设置为
`Tabulated` 时，数据提供者相对于
表格化压缩机数据指定此值。当您将
**Parameterization** 设置为
`Analytical` 时，此值是设计
工况下的入口温度。

### **Mechanical efficiency** — 转换为扭矩的效率 `0.9`（默认）| 范围 [0,1] 内的正标量

传递给流体流的功率与驱动
机械轴的功率之比。

### **Inlet area at port A** — 压缩机入口面积 `1` `m^2`（默认）| 正标量

压缩机入口横截面积。

### **Outlet area at port B** — 压缩机出口面积 `1` `m^2`（默认）| 正标量

压缩机出口横截面积。

## 所属库

Simscape / Fluids / Gas / Turbomachinery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

热力学循环中的气体压缩机

Compressor (G) 模块表示气体网络中的动态压缩机，
例如离心式或轴流式压缩机。您可以使用
**Parameterization** 参数基于设计点以解析方式
参数化该模块，或通过表格化压缩机特性图进行参数化。端口 **R**
相对于端口 **C** 的正旋转
会使流体从端口 **A** 流向端口 **B**。
端口 **R** 和端口 **C** 是分别
与压缩机轴和机壳相关联的机械旋转
守恒端口。

喘振裕度是沿等转速线的喘振压比与工作点
压比之比减一。当您将
**Parameterization** 设置为 `Tabulated` 时，
模块在端口 **SM** 输出喘振裕度。

设计点是仿真期间压缩机的设计运行压比和
通过压缩机的质量流量。压缩机工作点和最大效率点
不需要重合。

### Compressor Map

Compressor Map 绘制压缩机的等熵效率，以及介于堵塞流和喘振流两个极端之间的恒定修正轴转速线。要可视化该模块图谱，请右键点击该模块并选择 **Fluids** > **Plot Compressor Map**。每次修改模块设置后，请在图窗上点击 **Reload Data**。

压缩机图谱

每条修正转速线显示当轴以相应修正转速旋转时，压比如何随修正质量流量变化。变量 *β* 表示沿修正转速线在两个极端之间的相对位置。堵塞流对应 *β* = 0，喘振流对应 *β* = 1。该图谱还绘制等熵效率等值线，作为压比和修正质量流量的函数，这相对指示了压缩机在各种压比和修正质量流量组合下运行所需的功率。

**修正质量流量**

由于压缩机内部压力和温度变化很大，压缩机图谱以修正质量流量表示性能。该图谱使用参考压力和参考温度，从入口质量流量调整得到修正质量流量，

m˙corr=m˙A(TATref/pApref),

其中：

- *ṁA* 是端口 **A** 处的质量流量。
- *TA* 是端口 **A** 处的温度。
- *Tref* 是 **Reference temperature for corrected flow** 参数的值。当您将 **Parameterization** 设置为 `Analytical` 时，这是设计工况下的入口温度。
- m˙*corr* 是修正质量流量。

  当您将 **Parameterization** 设置为 `Analytical` 时，该模块使用 **Corrected mass flow rate at design point** 参数。

  当您将 **Parameterization** 设置为 `Tabulated` 时，该模块使用 **Corrected mass flow rate table, mdot(N,beta)** 参数。
- *pA* 是端口 **A** 处的压力。
- *pref* 是 **Reference pressure for corrected flow** 参数。使用解析参数化时，这是设计工况下的入口压力。

该模块根据比内能 *uA* 和压力 *pA* 推导 *TA*。

**修正转速**

该模块还根据参考温度调整轴转速 *ω*，使得修正轴转速为

ωcorr=ωTATref。

### 轴转矩

该模块按如下方式计算轴转矩 *τ*：

τ=m˙AΔhtotalηmω,

其中：

- *Δhtotal* 是比总焓的变化。
- *ηm* 是压缩机 **Mechanical efficiency**。
- *ω* 是相对轴角速度，*ωR - ωC*。

该模块将压缩机图谱中的效率关联为

Δhtotal=Δhisenηisen,

其中：

- *Δhisen* 是比总焓的等熵变化。
- *ηisen* 是等熵效率。

当流量趋近于零时的阈值区域确保当流量接近零或反向时，压缩机不产生转矩。

### 解析参数化

您可以通过将 **Parameterization** 设置为 `Analytical` 来解析生成压缩机图谱。该模块基于 [1] 的压缩机图谱模型，将其拟合到 **Corrected speed at design point**、**Pressure ratio at design point** 和 **Corrected mass flow rate at design point** 参数的指定值。此方法不使用 *β* 线，并且该模块不报告喘振裕度。

**压比**

该模块将给定轴转速和质量流量下的压比计算为

π=1+(πD−1)[N˜ab+2N˜kln(1−m˜−N˜bk)],

其中：

- *πD* 是 **Pressure ratio at design point** 参数。
- N˜ 是归一化修正轴转速，

  NND,

  其中 *ND* 是 **Corrected speed at design point** 参数。
- m˜ 是归一化修正质量流量，

  m˙corrm˙D,

  其中 m˙*D* 是 **Corrected mass flow rate at design point**。
- *a* 是 **Spine shape, a** 参数。
- *b* 是 **Speed line spread, b** 参数。
- *k* 是 **Speed line roundness, k** 参数。

*脊线* 指的是等熵效率等值线开始弯曲的黑线。图谱 *转速线* 是与脊线垂直相交的轴恒速线。

压缩机解析图谱

**等熵效率参数化**

当您将 **Efficiency specification** 设置为 `Analytical` 时，该模块将可变压缩机效率建模为

η=η0(1−C|p˜m˜a+Δa−1−m˜|c−D|m˜m˜0−1|d),

其中：

- *η0* 是 **Maximum isentropic efficiency** 参数的值。
- *C* 是 **Efficiency contour gradient orthogonal to spine, C** 参数的值。
- *D* 是 **Efficiency contour gradient along spine, D** 参数的值。
- *c* 是 **Efficiency peak flatness orthogonal to spine, c** 参数的值。
- *d* 是 **Efficiency peak flatness along spine, d** 参数的值。
- p˜ 是归一化修正压比，

  π−1πD−1,

  其中 *πD* 是 **Corrected pressure ratio at design point** 参数。
- m˜*0* 是压缩机达到 **Maximum isentropic efficiency** 参数值时的归一化修正质量流量。

您可以为不同的性能特性调整效率变量。或者，您可以使用 **Constant isentropic efficiency** 参数选择恒定效率值。

### 表格数据参数化

当您将 **Parameterization** 设置为 `Tabulated` 时，压缩机的等熵效率、压比和修正质量流量是修正转速 *N* 和图谱索引 *β* 的函数。该模块对效率、压比和修正质量流量使用数据点之间的线性插值。

如果 *β* 超过 1，则发生压缩机喘振，该模块假设压比保持在 *β* = 1，同时质量流量继续变化。如果仿真条件低于 *β* = 0，该模块对堵塞流的影响进行建模，其中质量流量保持在其 *β* = 0 时的值，同时压比继续变化。为了将压缩机性能约束在图谱边界内，该模块将等熵效率外推到最近点。

您可以选择在工况点压比超过喘振压比时收到通知。将 **Report when surge margin is negative** 设置为 `Warning` 以接收警告，或设置为 `Error` 以在此情况发生时停止仿真。

### 连续性方程

该模块守恒质量，使得

m˙A+m˙B=0,

其中 m˙*B* 是端口 **B** 处的质量流量。

该模块计算能量平衡方程为

ΦA+ΦB+Pfluid=0,

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。
- *Pfluid* 是传递给流体的流体功率，该模块根据比焓变化 Pfluid=m˙AΔhtotal 确定该功率。

### 假设和限制

- 该模块假设过热流体在 **A** 处进入。
- 该模块仅定义从端口 **A** 到端口 **B** 的压缩机图谱流动。反向流动结果可能不准确。
- 该模块仅表示动力式压缩机。
