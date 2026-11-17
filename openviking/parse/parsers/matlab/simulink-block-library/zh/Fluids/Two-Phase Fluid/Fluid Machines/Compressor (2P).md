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
```yaml
ports:
- name: SM
  summary: 喘振裕度物理信号
  direction: output
- name: A
  summary: 压缩机入口两相流体
  direction: output
- name: B
  summary: 压缩机出口两相流体
  direction: output
- name: C
  summary: 压缩机壳体机械旋转
  direction: output
- name: R
  summary: 压缩机轴机械旋转
  direction: output
```

### 输出

### **SM** — 喘振裕度物理信号

与给定质量流量下的喘振裕度相关联的物理信号输出端口。该模块按以下公式计算喘振裕度

SM(m˙corr)=pr,surge(m˙corr)pr(m˙corr)−1。

#### 依赖

要启用此端口，请将 **Parameterization** 设置为
`Tabulated`。
### 守恒

### **A** — 压缩机入口两相流体

与压缩机入口相关联的两相流体守恒端口。

### **B** — 压缩机出口两相流体

与压缩机出口相关联的两相流体守恒端口。

### **C** — 压缩机壳体机械旋转

与压缩机壳体相关联的机械旋转守恒端口。

### **R** — 压缩机轴机械旋转

与压缩机轴相关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 压缩机性能参数化 Analytical（默认）| Tabulated
  group: 压缩机映射
- name: Corrected speed at design point
  summary: 运行修正轴转速 25000 rpm（默认）| 正标量
  group: 压缩机映射
- name: Pressure ratio at design point
  summary: 运行出口-入口压力比 2.2（默认）| 正标量
  group: 压缩机映射
- name: Corrected mass flow rate at design point
  summary: 运行修正质量流量 0.20 kg/s（默认）| 正标量
  group: 压缩机映射
- name: Efficiency specification
  summary: 等熵效率选项 Constant（默认）| Analytical
  group: 压缩机映射
- name: Maximum isentropic efficiency
  summary: 最大压缩机效率 0.887（默认）| 范围 (0,1] 内的正标量
  group: 压缩机映射
- name: Minimum isentropic efficiency
  summary: 最小压缩机效率 0.5（默认）| 范围 (0,1] 内的正标量
  group: 压缩机映射
- name: Corrected mass flow rate at maximum efficiency point
  summary: 压缩机最大效率点处的修正质量流量 0.19 kg/s（默认）| 正标量
  group: 压缩机映射
- name: Pressure ratio at maximum efficiency point
  summary: 压缩机最大效率点处的压力比 2.1（默认）| 正标量
  group: 压缩机映射
- name: Constant isentropic efficiency
  summary: 常数等熵效率值 0.8（默认）| 正标量
  group: 压缩机映射
- name: Corrected speed index vector, N
  summary: 修正轴转速向量 [12500, 17750, 21750, 25000] rpm（默认）| 向量
  group: 压缩机映射
- name: Beta index vector, beta
  summary: '修正转速线间隔向量 0 : 1 / 5 : 1（默认）| 范围 [0,1] 内元素组成的向量'
  group: 压缩机映射
- name: Pressure ratio table, pr(N, beta)
  summary: 压缩机映射压力比数据 *M*×*N* 矩阵（默认）
  group: 压缩机映射
- name: Corrected mass flow rate table, mdot(N,beta)
  summary: 压缩机映射修正质量流量数据 *M*×*N* 矩阵（默认）
  group: 压缩机映射
- name: Isentropic efficiency table, eta(N,beta)
  summary: 压缩机映射等熵效率数据 *M*×*N* 矩阵（默认）
  group: 压缩机映射
- name: Report when surge margin is negative
  summary: 负喘振裕度通知 None（默认）| Warning | Error
  group: 压缩机映射
- name: Spine shape, a
  summary: 脊线形状指数 1.5（默认）| 正标量
  group: Map Coefficients
- name: Speed line spread, b
  summary: 等转速线间距指数 5（默认）| 正标量
  group: Map Coefficients
- name: Speed line roundness, k
  summary: 等转速线形状系数 0.03（默认）| 正标量
  group: Map Coefficients
- name: Efficiency peak flatness orthogonal to spine, c
  summary: 垂直于脊线的平坦度指数 3（默认）| 正标量
  group: Map Coefficients
- name: Efficiency peak flatness along spine, d
  summary: 沿脊线的平坦度指数 4（默认）| 正标量
  group: Map Coefficients
- name: Efficiency contour gradient orthogonal to spine, C
  summary: 正交梯度系数 15（默认）| 正标量
  group: Map Coefficients
- name: Efficiency contour gradient along spine, D
  summary: 沿脊线梯度系数 1（默认）| 正标量
  group: Map Coefficients
- name: Reference pressure for corrected flow
  summary: 修正压力 0.101325 MPa（默认）| 正标量
  group: 参数
- name: Reference temperature for corrected flow
  summary: 修正温度 373.15 K（默认）| 正标量
  group: 参数
- name: Mechanical efficiency
  summary: 转换为扭矩的效率 0.9（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Inlet area at port A
  summary: 压气机入口面积 0.01 m^2（默认）| 正标量
  group: 参数
- name: Outlet area at port B
  summary: 压气机出口面积 0.01 m^2（默认）| 正标量
  group: 参数
- name: Report when fluid at inlet is not fully vapor
  summary: 流体未完全汽化通知 None（默认）| Warning | Error
  group: 参数
```

### 压缩机映射

### **Parameterization** — 压缩机性能参数化 `Analytical`（默认）| `Tabulated`

压缩机性能参数化。选择解析或表格参数化：

- `Analytical`：压力比–修正质量流量曲线定义峰值压缩机性能。您可以选择将等熵效率建模为常数或解析形式。
- `Tabulated`：用户提供的压缩机映射定义压缩机性能。该模块通过在用户提供的修正轴转速和 β 向量中给定点处的修正质量流量、压力比和等熵效率表之间使用线性插值来确定压缩机工作点。默认映射来自 [3] 中报告的数据。

### **Corrected speed at design point** — 运行修正轴转速 `25000` `rpm`（默认）| 正标量

在预期压缩机压力比和修正质量流量下的轴转速，已对温度进行修正。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Pressure ratio at design point** — 运行出口-入口压力比 `2.2`（默认）| 正标量

在预期压缩机修正质量流量下的出口-入口压力比。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Corrected mass flow rate at design point** — 运行修正质量流量 `0.20` `kg/s`（默认）| 正标量

在预期压缩机压力比下的质量流量，已对温度和压力进行修正。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Efficiency specification** — 等熵效率选项 `Constant`（默认）| `Analytical`

等熵效率模型类型。选择常数或解析模型。使用 `Analytical` 指定可变值。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Maximum isentropic efficiency** — 最大压缩机效率 `0.887`（默认）| 范围 (0,1] 内的正标量

最大压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Minimum isentropic efficiency** — 最小压缩机效率 `0.5`（默认）| 范围 (0,1] 内的正标量

最小压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Corrected mass flow rate at maximum efficiency point** — 压缩机最大效率点处的修正质量流量 `0.19` `kg/s`（默认）| 正标量

最大效率点处的质量流量，已对温度和压力进行修正。最大效率点不一定与压缩机设计点重合。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Pressure ratio at maximum efficiency point** — 压缩机最大效率点处的压力比 `2.1`（默认）| 正标量

最大效率点处的压力比。最大效率点不一定与压缩机设计点重合。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Constant isentropic efficiency** — 常数等熵效率值 `0.8`（默认）| 正标量

常数等熵效率的值。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Constant`。

### **Corrected speed index vector, N** — 修正轴转速向量 `[12500, 17750, 21750, 25000]` rpm（默认）| 向量

修正轴转速向量。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Beta index vector, beta** — 修正转速线间隔向量 `0 : 1 / 5 : 1`（默认）| 范围 [0,1] 内元素组成的向量

沿修正转速线的相对位置向量。当 β = 0 时发生阻塞流，当 β = 1 时发生喘振流。β 线垂直于压缩机轴等速线 *N*。

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Pressure ratio table, pr(N, beta)** — 压缩机映射压力比数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值处的压缩机出口-入口压力比的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N** 参数中向量元素的数量。
- *N* 是 **Beta index vector, beta** 参数中向量元素的数量。

默认值为：

`[1.1814, 1.2385, 1.2792, 1.3017, 1.3057, 1.3057; 1.3648,
1.5157, 1.6298, 1.691, 1.7011, 1.7032; 1.587, 1.8357, 2.011, 2.0925,
2.1006, 2.1006; 1.8255, 2.28, 2.4777, 2.5225, 2.5633,
2.5389]`

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Corrected mass flow rate table, mdot(N,beta)** — 压缩机映射修正质量流量数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值处的修正质量流量的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N** 参数中向量元素的数量。
- *N* 是 **Beta index vector, beta** 参数中向量元素的数量。

默认值为：

`[.1503, .1313, .11, .0887, .0668, .0502; .2265, .1999, .1649,
.1322, .0992, .0639; .2869, .2545, .216, .1798, .1424, .108; .3275,
.2846, .2466, .2285, .209, .1661] kg/s`

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Isentropic efficiency table, eta(N,beta)** — 压缩机映射等熵效率数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值处的压缩机等熵效率的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N** 参数中向量元素的数量。
- *N* 是 **Beta index vector, beta** 参数中向量元素的数量。

默认值为：

`[.56, .66, .71, .695, .659, .635; .558, .682, .755, .743,
.697, .638; .57, .705, .765, .752, .712, .652; .552, .718, .755,
.752, .736, .67]`

#### 依赖

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Report when surge margin is negative** — 负喘振裕度通知 `None`（默认）| `Warning` | `Error`

当模块检测到负喘振裕度时，是执行无操作、生成警告还是生成错误。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### Map Coefficients

要启用 **Map Coefficients** 参数，请将 **Parameterization** 设置为 `Analytical`。

### **Spine shape, a** — 脊线形状指数 `1.5`（默认）| 正标量

压气机映射解析参数化中表征脊线形状的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line spread, b** — 等转速线间距指数 `5`（默认）| 正标量

压气机映射解析参数化中表征等转速线间距的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line roundness, k** — 等转速线形状系数 `0.03`（默认）| 正标量

压气机映射解析参数化中表征等转速线形状的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Efficiency peak flatness orthogonal to spine, c** — 垂直于脊线的平坦度指数 `3`（默认）| 正标量

与压气机映射中垂直于脊线的峰值平坦度相关的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency peak flatness along spine, d** — 沿脊线的平坦度指数 `4`（默认）| 正标量

与效率映射中沿脊线的峰值平坦度相关的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient orthogonal to spine, C** — 正交梯度系数 `15`（默认）| 正标量

与效率等值线中垂直于脊线的梯度相关的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient along spine, D** — 沿脊线梯度系数 `1`（默认）| 正标量

与效率等值线中沿脊线的梯度相关的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### 参数

### **Reference pressure for corrected flow** — 修正压力 `0.101325` `MPa`（默认）| 正标量

压气机映射的参考入口压力。当您将 **Parameterization** 设置为 `Tabulated` 时，数据提供方针对表格化压气机数据指定此值。当您将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口压力。

### **Reference temperature for corrected flow** — 修正温度 `373.15` `K`（默认）| 正标量

压气机映射的参考入口温度。当您将 **Parameterization** 设置为 `Tabulated` 时，数据提供方针对表格化压气机数据指定此值。当您将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口温度。

### **Mechanical efficiency** — 转换为扭矩的效率 `0.9`（默认）| 范围 [0,1] 内的正标量

传递给流体流的功率与驱动机械轴的功率之比。

### **Inlet area at port A** — 压气机入口面积 `0.01` `m^2`（默认）| 正标量

压气机入口横截面积。

### **Outlet area at port B** — 压气机出口面积 `0.01` `m^2`（默认）| 正标量

压气机出口横截面积。

### **Report when fluid at inlet is not fully vapor** — 流体未完全汽化通知 `None`（默认）| `Warning` | `Error`

当模块检测到流体未完全汽化时，是执行无操作、生成警告还是生成错误。
## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

热力学循环中的两相流体压气机

Compressor (2P) 模块表示两相流体网络中的动态压气机，例如离心式或轴流式压气机。您可以使用 **Parameterization** 参数，基于设计点或使用表格化压气机映射对模块进行解析参数化。端口 **R** 相对于端口 **C** 的正旋转会导致流体从端口 **A** 流向端口 **B**。端口 **R** 和端口 **C** 分别是与压气机轴和壳体相关联的机械旋转守恒端口。

喘振裕度是沿等转速线的喘振压力比与工作点压力比之间的比值减一。当您将 **Parameterization** 设置为 `Tabulated` 时，模块在端口 **SM** 输出喘振裕度。

设计点是仿真期间压气机的设计操作压力比和通过压气机的质量流量。压气机工作点和最大效率点不需要重合。

Compressor (2P) 模块假定过热流体进入入口。您可以使用 **Report when fluid is not fully vapor** 参数来选择当流体不满足过热条件时模块的行为。

### Compressor Map

Compressor Map 绘制压缩机的等熵效率，以及在堵塞流动和喘振流动两个极端之间的等校正转速线。要可视化该模块映射，请右键单击该模块并选择 **Fluids** > **Plot Compressor Map**。每次修改模块设置后，请在图窗上单击 **Reload Data**。

Compressor map

每条校正转速线显示当轴以相应的校正转速旋转时，压比如何随校正质量流量变化。变量 *β* 表示在两种极端之间沿校正转速线的相对位置。堵塞流动对应于 *β* = 0，喘振流动对应于 *β* = 1。该映射还绘制等熵效率随压比和校正质量流量变化的等值线，这提供了压缩机在各种压比和校正质量流量组合下运行所需功率的相对指示。

**Corrected Mass Flow Rate**

由于压缩机内部压力和温度变化很大，Compressor Map 以校正质量流量来表示性能。该映射使用参考压力和参考温度，从入口质量流量调整校正质量流量，

m˙corr=m˙A(TATref/pApref),

其中：

- *ṁA* 是端口 **A** 处的质量流量。
- *TA* 是端口 **A** 处的温度。
- *Tref* 是 **Reference temperature for corrected flow** 参数的值。当您将 **Parameterization** 设置为 `Analytical` 时，这是设计工况下的入口温度。
- m˙*corr* 是校正质量流量。当您将 **Parameterization** 设置为 `Analytical` 时，该模块使用 **Corrected mass flow rate at design point** 参数。当您将 **Parameterization** 设置为 `Tabulated` 时，该模块使用 **Corrected mass flow rate table, mdot(N,beta)** 参数。
- *pA* 是端口 **A** 处的压力。
- *pref* 是 **Reference pressure for corrected flow** 参数。当使用 analytical parameterization 时，这是设计工况下的入口压力。

该模块根据比内能 *uA* 和比压力 *pA* 推导 *TA*。

**Corrected Speed**

该模块还根据参考温度调整轴转速 *ω*，使得校正轴转速为

ωcorr=ωTATref。

### Shaft Torque

该模块将轴扭矩 *τ* 计算为

τ=m˙AΔhtotalηmω,

其中：

- *Δhtotal* 是比总焓的变化。
- *ηm* 是压缩机 **Mechanical efficiency**。
- *ω* 是相对轴角速度，*ωR - ωC*。

该模块将压缩机映射中的效率关联为

Δhtotal=Δhisenηisen,

其中：

- *Δhisen* 是比总焓的等熵变化。
- *ηisen* 是等熵效率。

当流量趋近于零时的阈值区域确保当流量接近零或反向时，压缩机不产生扭矩。

### Analytical Parameterization

您可以通过将 **Parameterization** 设置为 `Analytical` 来解析生成压缩机映射。该模块基于 [1] 中的压缩机映射模型，将其拟合到 **Corrected speed at design point**、**Pressure ratio at design point** 和 **Corrected mass flow rate at design point** 参数的指定值。此方法不使用 *β* 线，并且该模块不报告喘振裕度。

**Pressure Ratio**

该模块在给定轴转速和质量流量下按如下方式求取压比

π=1+(πD−1)[N˜ab+2N˜kln(1−m˜−N˜bk)],

其中：

- *πD* 是 **Pressure ratio at design point** 参数。
- N˜ 是归一化校正轴转速，

  NND，

  其中 *ND* 是 **Corrected speed at design point** 参数。
- m˜ 是归一化校正质量流量，

  m˙corrm˙D，

  其中 m˙*D* 是 **Corrected mass flow rate at design point** 参数。
- *a* 是 **Spine shape, a** 参数。
- *b* 是 **Speed line spread, b** 参数。
- *k* 是 **Speed line roundness, k** 参数。

*spine* 是指等熵效率等值线开始弯曲处的黑线。映射 *speed lines* 是与 spine 垂直相交的轴恒速线。

Compressor analytical map

**Isentropic Efficiency Parameterization**

当您将 **Efficiency specification** 设置为 `Analytical` 时，该模块将可变压缩机效率建模为

η=η0(1−C|p˜m˜a+Δa−1−m˜|c−D|m˜m˜0−1|d),

其中：

- *η0* 是 **Maximum isentropic efficiency** 参数的值。
- *C* 是 **Efficiency contour gradient orthogonal to spine, C** 参数的值。
- *D* 是 **Efficiency contour gradient along spine, D** 参数的值。
- *c* 是 **Efficiency peak flatness orthogonal to spine, c** 参数的值。
- *d* 是 **Efficiency peak flatness along spine, d** 参数的值。
- p˜ 是归一化校正压比，

  π−1πD−1，

  其中 *πD* 是 **Corrected pressure ratio at design point** 参数。
- m˜*0* 是压缩机达到 **Maximum isentropic efficiency** 参数值时的归一化校正质量流量。

您可以针对不同的性能特性调整效率变量。或者，您可以通过 **Constant isentropic efficiency** 参数选择恒定效率值。

### Tabulated Data Parameterization

当您将 **Parameterization** 设置为 `Tabulated` 时，压缩机的等熵效率、压比和校正质量流量是校正转速 *N* 和映射索引 *β* 的函数。该模块对效率、压比和校正质量流量使用数据点之间的线性插值。

如果 *β* 超过 1，则发生压缩机喘振，该模块假定压比保持在 *β* = 1，而质量流量继续变化。如果仿真条件低于 *β* = 0，则该模块对堵塞流动的影响进行建模，其中质量流量保持在其 *β* = 0 时的值，而压比继续变化。为了将压缩机性能约束在映射边界内，该模块将等熵效率外推到最近点。

您可以选择在工作点压比超过喘振压比时收到通知。将 **Report when surge margin is negative** 设置为 `Warning` 以接收警告，或设置为 `Error` 以在此情况发生时停止仿真。

### Continuity Equations

该模块按如下方式守恒质量

m˙A+m˙B=0,

其中 m˙*B* 是端口 **B** 处的质量流量。

该模块按如下方式计算能量平衡方程

ΦA+ΦB+Pfluid=0,

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。
- *Pfluid* 是传递给流体的液压功率，该模块根据比焓变化确定该功率 Pfluid=m˙AΔhtotal。

### 假设和限制

- 该模块假定过热流体在 **A** 处进入。
- 该模块仅定义从端口 **A** 到端口 **B** 的压缩机映射流动。反向流动结果可能不准确。
- 该模块仅表示动态压缩机。
