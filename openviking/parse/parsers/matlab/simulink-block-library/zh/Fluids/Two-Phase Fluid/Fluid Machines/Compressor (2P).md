---
type: simulink-block
title: 'Compressor (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'compressor2p'
documentation_source_path: 'ref/compressor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Compressor (2P)

## 端口

### 输出

### **SM** — 喘振裕度物理信号

与给定质量流量下的喘振裕度关联的物理信号输出端口。该模块按以下方式计算喘振裕度

SM(m˙corr)=pr,surge(m˙corr)pr(m˙corr)−1.

#### 依赖项

要启用此端口，请将 **Parameterization** 设置为 `Tabulated`。

### 守恒

### **A** — 压缩机入口两相流体

与压缩机入口关联的两相流体守恒端口。

### **B** — 压缩机出口两相流体

与压缩机出口关联的两相流体守恒端口。

### **C** — 压缩机壳体机械旋转

与压缩机壳体关联的机械旋转守恒端口。

### **R** — 压缩机轴机械旋转

与压缩机轴关联的机械旋转守恒端口。

## 参数

### 压缩机特性图

### **Parameterization** — Compressor performance parameterization `Analytical` (默认) | `Tabulated`

压缩机性能参数化。选择 `Analytical` 或 `Tabulated` 参数化：

- `Analytical`：压力比–校正质量流量曲线定义压缩机峰值性能。您可以选择将等熵效率建模为常量或按解析方式建模。
- `Tabulated`：用户提供的压缩机特性图定义压缩机性能。该模块通过在用户提供的校正轴转速和 β 向量中的给定点处，对校正质量流量、压力比和等熵效率表进行线性插值，确定压缩机工作点。默认特性图来自 [3] 中报告的数据。

### **Corrected speed at design point** — Operational corrected shaft speed `25000` `rpm` (默认) | positive scalar

在预期压缩机压力比和校正质量流量下的轴转速，并针对温度进行校正。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Pressure ratio at design point** — Operational outlet-to-inlet pressure ratio `2.2` (默认) | positive scalar

在预期压缩机校正质量流量下的出口-入口压力比。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Corrected mass flow rate at design point** — Operational corrected mass flow rate `0.20` `kg/s` (默认) | positive scalar

在预期压缩机压力比下的质量流量，并针对温度和压力进行校正。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Efficiency specification** — Isentropic efficiency option `Constant` (默认) | `Analytical`

等熵效率模型类型。选择常量模型或解析模型。使用 `Analytical` 可指定可变值。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Maximum isentropic efficiency** — Maximum compressor efficiency `0.887` (默认) | positive scalar in the range (0,1]

最大压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Minimum isentropic efficiency** — Minimum compressor efficiency `0.5` (默认) | positive scalar in the range (0,1]

最小压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Corrected mass flow rate at maximum efficiency point** — Corrected mass flow rate at compressor maximum efficiency `0.19` `kg/s` (默认) | positive scalar

最大效率处的质量流量，并针对温度和压力进行校正。最大效率点不一定与压缩机设计点重合。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Pressure ratio at maximum efficiency point** — Pressure ratio at compressor maximum efficiency `2.1` (默认) | positive scalar

最大效率处的压力比。最大效率点不一定与压缩机设计点重合。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Constant isentropic efficiency** — Constant isentropic efficiency value `0.8` (默认) | positive scalar

常量等熵效率的值。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Constant`。

### **Corrected speed index vector, N** — Vector of corrected shaft speeds `[12500, 17750, 21750, 25000]` rpm (默认) | vector

校正轴转速向量。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Beta index vector, beta** — Vector of corrected speed line intervals `0 : 1 / 5 : 1` (默认) | vector of elements in the range [0,1]

沿校正转速线的相对位置向量。当 β = 0 时发生阻塞流动，当 β = 1 时发生喘振流动。β 线垂直于压缩机轴恒定转速线 *N*。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Pressure ratio table, pr(N, beta)** — Compressor map pressure ratio data *M*-by-*N* matrix (默认)

*M*-by-*N* matrix，包含在指定校正轴转速和 β 值下的压缩机出口-入口压力比。该模块在表元素之间采用线性插值。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Corrected speed index vector, N** 参数中的向量元素数。
- *N* 是 **Beta index vector, beta** 参数中的向量元素数。

默认值为：

`[1.1814, 1.2385, 1.2792, 1.3017, 1.3057, 1.3057; 1.3648,
1.5157, 1.6298, 1.691, 1.7011, 1.7032; 1.587, 1.8357, 2.011, 2.0925,
2.1006, 2.1006; 1.8255, 2.28, 2.4777, 2.5225, 2.5633,
2.5389]`

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Corrected mass flow rate table, mdot(N,beta)** — Compressor map corrected mass flow rate data *M*-by-*N* matrix (默认)

*M*-by-*N* matrix，包含在指定校正轴转速和 β 值下的校正质量流量。该模块在表元素之间采用线性插值。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Corrected speed index vector, N** 参数中的向量元素数。
- *N* 是 **Beta index vector, beta** 参数中的向量元素数。

默认值为：

`[.1503, .1313, .11, .0887, .0668, .0502; .2265, .1999, .1649,
.1322, .0992, .0639; .2869, .2545, .216, .1798, .1424, .108; .3275,
.2846, .2466, .2285, .209, .1661] kg/s`

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Isentropic efficiency table, eta(N,beta)** — Compressor map isentropic efficiency data *M*-by-*N* matrix (默认)

*M*-by-*N* matrix，包含在指定校正轴转速和 β 值下的压缩机等熵效率。该模块在表元素之间采用线性插值。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Corrected speed index vector, N** 参数中的向量元素数。
- *N* 是 **Beta index vector, beta** 参数中的向量元素数。

默认值为：

`[.56, .66, .71, .695, .659, .635; .558, .682, .755, .743,
.697, .638; .57, .705, .765, .752, .712, .652; .552, .718, .755,
.752, .736, .67]`

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Report when surge margin is negative** — Negative surge margin notification `None` (默认) | `Warning` | `Error`

当检测到负喘振裕度时，该模块是不执行任何操作、生成警告，还是生成错误。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### 特性图系数

要启用 **Map Coefficients** 参数，请将 **Parameterization** 设置为 `Analytical`。

### **Spine shape, a** — Spine shape exponent `1.5` (默认) | positive scalar

压缩机特性图解析参数化中表征脊线形状的指数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line spread, b** — Constant speed line spacing exponent `5` (默认) | positive scalar

压缩机特性图解析参数化中表征恒定转速线间距的指数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line roundness, k** — Constant speed line shape coefficient `0.03` (默认) | positive scalar

压缩机特性图解析参数化中表征恒定转速线形状的系数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Efficiency peak flatness orthogonal to spine, c** — Flatness orthogonal to spine exponent `3` (默认) | positive scalar

与压缩机特性图峰值垂直于脊线的平坦度相关的指数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency peak flatness along spine, d** — Along spine flatness exponent `4` (默认) | positive scalar

与效率图峰值沿脊线的平坦度相关的指数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient orthogonal to spine, C** — Orthogonal gradient coefficient `15` (默认) | positive scalar

与效率等值线垂直于脊线的梯度相关的系数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient along spine, D** — Along spine gradient coefficient `1` (默认) | positive scalar

与效率等值线沿脊线的梯度相关的系数。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### 参数

### **Reference pressure for corrected flow** — Correcting pressure `0.101325` `MPa` (默认) | positive scalar

压缩机特性图的参考入口压力。当您将 **Parameterization** 设置为 `Tabulated` 时，数据提供方会针对表格化压缩机数据指定此值。当您将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口压力。

### **Reference temperature for corrected flow** — Correcting temperature `373.15` `K` (默认) | positive scalar

压缩机特性图的参考入口温度。当您将 **Parameterization** 设置为 `Tabulated` 时，数据提供方会针对表格化压缩机数据指定此值。当您将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口温度。

### **Mechanical efficiency** — Efficiency of conversion to torque `0.9` (默认) | positive scalar in the range [0,1]

传递给流体流的功率与驱动机械轴的功率之比。

### **Inlet area at port A** — Compressor inlet area `0.01` `m^2` (默认) | positive scalar

压缩机入口横截面积。

### **Outlet area at port B** — Compressor outlet area `0.01` `m^2` (默认) | positive scalar

压缩机出口横截面积。

### **Report when fluid at inlet is not fully vapor** — Fluid not fully vapor notification `None` (默认) | `Warning` | `Error`

当检测到流体未完全汽化时，该模块是不执行任何操作、生成警告，还是生成错误。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

热力学循环中的两相流体压缩机

Compressor (2P) 模块表示两相流体网络中的动态压缩机，例如离心式或轴流式压缩机。您可以使用 **Parameterization** 参数，基于设计点以解析方式或使用表格化压缩机特性图来参数化该模块。端口 **R** 相对于端口 **C** 的正旋转会使流体从端口 **A** 流向端口 **B**。端口 **R** 和端口 **C** 分别是与压缩机轴和壳体关联的机械旋转守恒端口。

喘振裕度是沿恒定转速线的喘振压力比与工作点压力比之比减一。当您将 **Parameterization** 设置为 `Tabulated` 时，该模块在端口 **SM** 输出喘振裕度。

设计点是仿真期间压缩机两侧的设计运行压力比和通过压缩机的质量流量。压缩机工作点与最大效率点不需要重合。

Compressor (2P) 模块假设过热流体进入入口。您可以使用 **Report when fluid is not fully vapor** 参数来选择当流体不满足过热条件时该模块的行为。

### Compressor Map

压缩机特性图绘制压缩机的等熵效率，以及位于阻塞流和喘振流两个极端之间的恒定修正轴转速线。要可视化模块特性图，请右键单击该模块并选择 **Fluids** > **Plot Compressor Map**。每次修改模块设置后，单击图窗上的 **Reload Data**。

压缩机特性图

每个修正转速线显示当轴以对应的修正转速旋转时，压比如何随修正质量流量变化。变量 *β* 表示沿修正转速线在两个极端之间的相对位置。阻塞流对应 *β* = 0，喘振流对应 *β* = 1。特性图还绘制等熵效率等值线，作为压比和修正质量流量的函数，这相对指示了压缩机在各种压比和修正质量流量组合下运行所需功率。

**修正质量流量**

由于压缩机内部压力和温度变化很大，压缩机特性图以修正质量流量表示性能。特性图使用参考压力和参考温度，从入口质量流量调整得到修正质量流量，

m˙corr=m˙A(TATref/pApref),

其中：

- *ṁA* 是端口 **A** 处的质量流量。
- *TA* 是端口 **A** 处的温度。
- *Tref* 是 **Reference temperature for corrected flow** 参数的值。当将 **Parameterization** 设置为 `Analytical` 时，这是设计工况下的入口温度。
- m˙*corr* 是修正质量流量。当将 **Parameterization** 设置为 `Analytical` 时，模块使用 **Corrected mass flow rate at design point** 参数。当将 **Parameterization** 设置为 `Tabulated` 时，模块使用 **Corrected mass flow rate table, mdot(N,beta)** 参数。
- *pA* 是端口 **A** 处的压力。
- *pref* 是 **Reference pressure for corrected flow** 参数。使用解析参数化时，这是设计工况下的入口压力。

模块根据比内能 *uA* 和比压力 *pA* 推导 *TA*。

**修正转速**

模块还根据参考温度调整轴转速 *ω*，使得修正轴转速为

ωcorr=ωTATref.

### 轴转矩

模块按下式计算轴转矩 *τ*：

τ=m˙AΔhtotalηmω,

其中：

- *Δhtotal* 是比总焓变化。
- *ηm* 是压缩机的 **Mechanical efficiency**。
- *ω* 是相对轴角速度，*ωR - ωC*。

模块将特性图中的效率关联为

Δhtotal=Δhisenηisen,

其中：

- *Δhisen* 是比总焓的等熵变化。
- *ηisen* 是等熵效率。

当流量趋近于零时，阈值区域确保当流量接近零或反向时，压缩机不产生转矩。

### 解析参数化

您可以通过将 **Parameterization** 设置为 `Analytical` 来解析生成压缩机特性图。模块基于 [1] 拟合压缩机特性图模型，使其匹配 **Corrected speed at design point**、**Pressure ratio at design point** 和 **Corrected mass flow rate at design point** 参数的指定值。此方法不使用 *β* 线，并且模块不报告喘振裕度。

**压比**

模块按下式求给定轴转速和质量流量下的压比：

π=1+(πD−1)[N˜ab+2N˜kln(1−m˜−N˜bk)],

其中：

- *πD* 是 **Pressure ratio at design point** 参数。
- N˜ 是归一化修正轴转速，

  NND,

  其中 *ND* 是 **Corrected speed at design point** 参数。
- m˜ 是归一化修正质量流量，

  m˙corrm˙D,

  其中 m˙*D* 是 **Corrected mass flow rate at design point** 参数。
- *a* 是 **Spine shape, a** 参数。
- *b* 是 **Speed line spread, b** 参数。
- *k* 是 **Speed line roundness, k** 参数。

*脊线* 指的是等熵效率等值线开始弯曲处的黑线。特性图 *转速线* 是与脊线垂直相交的轴恒转速线。

压缩机解析特性图

**等熵效率参数化**

当将 **Efficiency specification** 设置为 `Analytical` 时，模块将可变压缩机效率建模为

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

您可以针对不同性能特性调整效率变量。或者，您可以通过 **Constant isentropic efficiency** 参数选择恒定效率值。

### 表格数据参数化

当将 **Parameterization** 设置为 `Tabulated` 时，压缩机的等熵效率、压比和修正质量流量是修正转速 *N* 和特性图索引 *β* 的函数。模块对效率、压比和修正质量流量使用数据点之间的线性插值。

如果 *β* 超过 1，则发生压缩机喘振，模块假设压比保持在 *β* = 1，而质量流量继续变化。如果仿真条件低于 *β* = 0，模块对阻塞流效应建模，其中质量流量保持其在 *β* = 0 时的值，而压比继续变化。为了将压缩机性能限制在特性图边界内，模块将等熵效率外推到最近点。

您可以选择在工作点压比超过喘振压比时收到通知。将 **Report when surge margin is negative** 设置为 `Warning` 以收到警告，或设置为 `Error` 以在此情况发生时停止仿真。

### 连续性方程

模块按如下方式守恒质量

m˙A+m˙B=0,

其中 m˙*B* 是端口 **B** 处的质量流量。

模块计算能量平衡方程为

ΦA+ΦB+Pfluid=0,

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。
- *Pfluid* 是传递给流体的液压功率，模块根据比焓变化 Pfluid=m˙AΔhtotal 确定该功率。

### 假设与限制

- 模块假设过热流体在 **A** 处进入。
- 模块仅定义从端口 **A** 到端口 **B** 的压缩机特性图流动。反向流结果可能不准确。
- 模块仅表示动力式压缩机。
