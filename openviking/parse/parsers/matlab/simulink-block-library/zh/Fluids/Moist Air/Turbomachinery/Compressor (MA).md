---
type: simulink-block
title: 'Compressor (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'compressorma'
documentation_source_path: 'ref/compressorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Compressor (MA)

## 端口
```yaml
ports:
- name: A
  summary: 湿空气入口 湿空气
  direction: output
- name: B
  summary: 湿空气出口 湿空气
  direction: output
- name: C
  summary: 压缩机壳体 机械平移
  direction: output
- name: R
  summary: 压缩机轴 机械平移
  direction: output
- name: SM
  summary: 喘振裕度 物理信号
  direction: output
```

### 守恒

### **A** — 湿空气入口 湿空气

与压缩机入口相关联的湿空气守恒端口。

### **B** — 湿空气出口 湿空气

与压缩机出口相关联的湿空气守恒端口。

### **C** — 压缩机壳体 机械平移

与压缩机壳体相关联的机械平移守恒端口。

### **R** — 压缩机轴 机械平移

与压缩机轴扭矩和角速度相关联的机械平移守恒端口。
### 输出

### **SM** — 喘振裕度 物理信号

与给定质量流量下的喘振裕度相关联的物理信号输出端口。该模块按以下公式计算喘振裕度：

SM(m˙corr)=pr,surge(m˙corr)pr(m˙corr)−1。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为
`Tabulated`。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 压缩机性能参数化 Analytical（默认）| Tabulated
  group: 压缩机特性图
- name: Corrected speed at design point
  summary: 工作修正轴转速 10000 rpm（默认）| 正标量
  group: 压缩机特性图
- name: Pressure ratio at design point
  summary: 工作出口-入口压比 7.5（默认）| 正标量
  group: 压缩机特性图
- name: Corrected mass flow rate at design point
  summary: 工作修正质量流量 33 kg/s（默认）| 正标量
  group: 压缩机特性图
- name: Efficiency specification
  summary: 等熵效率模型 Analytical（默认）| Constant
  group: 压缩机特性图
- name: Maximum isentropic efficiency
  summary: 最大压缩机效率 0.887（默认）| (0,1] 范围内的正标量
  group: 压缩机特性图
- name: Minimum isentropic efficiency
  summary: 最小压缩机效率 0.5（默认）| (0,1] 范围内的正标量
  group: 压缩机特性图
- name: Corrected mass flow rate at maximum efficiency point
  summary: 压缩机最大效率点处的修正质量流量 30 kg/s（默认）| 正标量
  group: 压缩机特性图
- name: Pressure ratio at maximum efficiency point
  summary: 压缩机最大效率点处的压比 7（默认）| 正标量
  group: 压缩机特性图
- name: Constant isentropic efficiency
  summary: 常数等熵效率值 0.8（默认）| (0,1] 范围内的正标量
  group: 压缩机特性图
- name: Corrected speed index vector, N
  summary: 修正轴转速向量 [5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000] rpm（默认）| 向量
  group: 压缩机特性图
- name: Beta index vector, beta
  summary: '修正转速线间隔向量 0 : 1 / 6 : 1（默认）| [0,1] 范围内元素组成的向量'
  group: 压缩机特性图
- name: Pressure ratio table, pr(N,beta)
  summary: 压缩机特性图压比数据 *M*×*N* 矩阵（默认）
  group: 压缩机特性图
- name: Corrected mass flow rate table, mdot(N,beta)
  summary: 压缩机特性图修正质量流量数据 *M*×*N* 矩阵（默认）
  group: 压缩机特性图
- name: Isentropic efficiency table, eta(N,beta)
  summary: 压气机 map 等熵效率数据 *M*×*N* 矩阵（默认）
  group: 压缩机特性图
- name: Report when surge margin is negative
  summary: 当压比超过喘振压比时是否通知 None（默认）| Warning | Error
  group: 压缩机特性图
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
  summary: 表征解析等熵效率形状的指数 3（默认）| 正标量
  group: Map Coefficients
- name: Efficiency peak flatness along spine, d
  summary: 表征解析等熵效率形状的指数 4（默认）| 正标量
  group: Map Coefficients
- name: Efficiency contour gradient orthogonal to spine, C
  summary: 表征解析等熵效率形状的系数 15（默认）| 正标量
  group: Map Coefficients
- name: Efficiency contour gradient along spine, D
  summary: 表征解析等熵效率形状的系数 1（默认）| 范围 (0,1] 内的正标量
  group: Map Coefficients
- name: Reference pressure for corrected flow
  summary: 修正压力 0.101325 MPa（默认）| 正标量
  group: 参数
- name: Reference temperature for corrected flow
  summary: 修正温度 288.15 K（默认）| 正标量
  group: 参数
- name: Reference relative humidity for corrected flow
  summary: 修正湿度 0（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Mechanical efficiency
  summary: 转换为扭矩的效率 0.9（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Model water droplets evaporation
  summary: 模拟水滴蒸发的选项 off（默认）| on
  group: 参数
- name: Relative humidity at saturation
  summary: 发生冷凝时的相对湿度阈值 1（默认）| 正标量
  group: 参数
- name: Inlet area at port A
  summary: 压气机入口面积 1 m^2（默认）| 正标量
  group: 参数
- name: Outlet area at port B
  summary: 压气机出口面积 1 m^2（默认）| 正标量
  group: 参数
```

### 压缩机特性图

### **Parameterization** — 压缩机性能参数化 `Analytical`（默认）| `Tabulated`

压缩机性能参数化。选择解析或表格参数化：

- `Analytical`：压比-修正质量流量曲线定义峰值压缩机性能。您可以选择将等熵效率建模为常数或解析形式。
- `Tabulated`：用户提供的压缩机特性图定义压缩机性能。该模块通过在用户提供的修正轴转速和 β 向量中给定点处的修正质量流量、压比和等熵效率表之间使用线性插值来确定压缩机工作点。默认特性图来自 [3] 中报告的数据。

### **Corrected speed at design point** — 工作修正轴转速 `10000` `rpm`（默认）| 正标量

在预期压缩机压比和修正质量流量下的轴转速，已对温度进行修正。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Pressure ratio at design point** — 工作出口-入口压比 `7.5`（默认）| 正标量

在预期压缩机修正质量流量下的出口-入口压比。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Corrected mass flow rate at design point** — 工作修正质量流量 `33` `kg/s`（默认）| 正标量

在预期压缩机压比下的质量流量，已对温度和压力进行修正。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Efficiency specification** — 等熵效率模型 `Analytical`（默认）| `Constant`

等熵效率模型类型。选择常数或解析模型。使用
`Analytical` 指定可变值。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`。

### **Maximum isentropic efficiency** — 最大压缩机效率 `0.887`（默认）| (0,1] 范围内的正标量

最大压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Minimum isentropic efficiency** — 最小压缩机效率 `0.5`（默认）| (0,1] 范围内的正标量

最小压缩机等熵效率。等熵效率是等熵变化与实际变化之比。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Corrected mass flow rate at maximum efficiency point** — 压缩机最大效率点处的修正质量流量 `30` `kg/s`（默认）| 正标量

最大效率处的质量流量，已对温度和压力进行修正。最大效率点不一定与压缩机设计点重合。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Pressure ratio at maximum efficiency point** — 压缩机最大效率点处的压比 `7`（默认）| 正标量

最大效率处的压比。最大效率点不一定与压缩机设计点重合。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Analytical`。

### **Constant isentropic efficiency** — 常数等熵效率值 `0.8`（默认）| (0,1] 范围内的正标量

解析参数化中常数等熵效率的值。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Analytical`，并将 **Efficiency
specification** 设置为
`Constant`。

### **Corrected speed index vector, N** — 修正轴转速向量 `[5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000]` `rpm`（默认）| 向量

修正轴转速向量。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Beta index vector, beta** — 修正转速线间隔向量 `0 : 1 / 6 : 1`（默认）| [0,1] 范围内元素组成的向量

沿修正转速线的相对位置向量。当 β = 0 时发生阻塞流，当 β = 1 时发生喘振流。β 线与压缩机轴等速线
*N* 垂直。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Pressure ratio table, pr(N,beta)** — 压缩机特性图压比数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值处的压缩机出口-入口压比的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N**
  参数中向量元素的个数。
- *N* 是 **Beta index vector, beta**
  参数中向量元素的个数。

默认值为：

`[1.369, 1.459, 1.587, 1.654, 1.734, 1.775, 1.82; 1.918,
2.075, 2.229, 2.318, 2.405, 2.456, 2.481; 2.706, 2.966, 3.168,
3.334, 3.404, 3.445, 3.435; 3.203, 3.533, 3.833, 4.021, 4.127,
4.135, 4.066; 3.782, 4.222, 4.565, 4.867, 5.065, 5.07, 4.934; 4.302,
4.861, 5.285, 5.821, 6.161, 6.334, 6.142; 4.841, 5.445, 5.988,
6.628, 7.222, 7.623, 7.573; 5.358, 5.997, 6.589, 7.334, 8.012,
8.668, 9; 5.851, 6.491, 7.124, 7.982, 8.754, 9.57, 9.814; 6.707,
7.321, 8.034, 9.047, 9.94, 10.834, 10.998]`

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Corrected mass flow rate table, mdot(N,beta)** — 压缩机特性图修正质量流量数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值处的修正质量流量的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N**
  参数中向量元素的个数。
- *N* 是 **Beta index vector, beta**
  参数中向量元素的个数。

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

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Tabulated`。

### **Isentropic efficiency table, eta(N,beta)** — 压气机 map 等熵效率数据 *M*×*N* 矩阵（默认）

在指定的修正轴转速和 β 值下的压气机等熵效率的 *M*×*N* 矩阵。该模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N** 参数中向量元素的数量。
- *N* 是 **Beta index vector, beta** 参数中向量元素的数量。

默认值为：

`[.68, .69, .695, .7, .701, .705, .704; .7, .725, .75, .755,
.745, .73, .725; .77, .795, .81, .805, .78, .765, .745; .795, .812,
.825, .82, .805, .78, .75; .82, .837, .848, .849, .835, .805, .78;
.83, .845, .856, .86, .855, .84, .8; .83, .848, .859, .869, .86,
.852, .83; .828, .845, .857, .869, .862, .855, .85; .806, .83, .85,
.86, .859, .857, .853; .79, .8, .82, .835, .845, .848,
.849]`

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### **Report when surge margin is negative** — 当压比超过喘振压比时是否通知 `None`（默认）| `Warning` | `Error`

当检测到负喘振裕度时，该模块是不执行任何操作、生成警告还是生成错误。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated`。

### Map Coefficients

要启用 **Map Coefficients** 参数，请将 **Parameterization** 设置为 `Analytical`。

### **Spine shape, a** — 脊线形状指数 `1.5`（默认）| 正标量

压气机 map 解析参数化中表征脊线形状的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line spread, b** — 等转速线间距指数 `5`（默认）| 正标量

压气机 map 解析参数化中表征等转速线间距的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Speed line roundness, k** — 等转速线形状系数 `0.03`（默认）| 正标量

压气机 map 解析参数化中表征等转速线形状的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`。

### **Efficiency peak flatness orthogonal to spine, c** — 表征解析等熵效率形状的指数 `3`（默认）| 正标量

与压气机 map 中垂直于脊线的峰值平坦度相关的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency peak flatness along spine, d** — 表征解析等熵效率形状的指数 `4`（默认）| 正标量

与沿脊线的效率 map 峰值平坦度相关的指数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient orthogonal to spine, C** — 表征解析等熵效率形状的系数 `15`（默认）| 正标量

与垂直于脊线的效率等值线梯度相关的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Efficiency contour gradient along spine, D** — 表征解析等熵效率形状的系数 `1`（默认）| 范围 (0,1] 内的正标量

与沿脊线的效率等值线梯度相关的系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Analytical`，并将 **Efficiency specification** 设置为 `Analytical`。

### 参数

### **Reference pressure for corrected flow** — 修正压力 `0.101325` `MPa`（默认）| 正标量

压气机 map 的参考入口压力。当将 **Parameterization** 设置为 `Tabulated` 时，数据提供方会针对表格化压气机数据指定此值。当将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口压力。

### **Reference temperature for corrected flow** — 修正温度 `288.15` `K`（默认）| 正标量

压气机 map 的参考入口温度。当将 **Parameterization** 设置为 `Tabulated` 时，数据提供方会针对表格化压气机数据指定此值。当将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口温度。

### **Reference relative humidity for corrected flow** — 修正湿度 `0`（默认）| 范围 [0,1] 内的正标量

压气机 map 的参考入口湿度。当将 **Parameterization** 设置为 `Tabulated` 时，数据提供方会针对表格化压气机数据指定此值。当将 **Parameterization** 设置为 `Analytical` 时，此值为设计工况下的入口湿度。

### **Mechanical efficiency** — 转换为扭矩的效率 `0.9`（默认）| 范围 [0,1] 内的正标量

传递给流体流的功率与驱动机械轴的功率之比。

### **Model water droplets evaporation** — 模拟水滴蒸发的选项 `off`（默认）| `on`

用于模拟压气机中因温度变化而导致的水滴蒸发的选项。

### **Relative humidity at saturation** — 发生冷凝时的相对湿度阈值 `1`（默认）| 正标量

压气机中发生冷凝时的相对湿度阈值。

#### 依赖关系

要启用此参数，请选择 **Model water droplets evaporation**。

### **Inlet area at port A** — 压气机入口面积 `1` `m^2`（默认）| 正标量

压气机入口横截面积。

### **Outlet area at port B** — 压气机出口面积 `1` `m^2`（默认）| 正标量

压气机出口横截面积。
## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 模拟水滴蒸发

使用 **Model water droplets evaporation** 参数模拟因温度变化而导致的水滴蒸发。

### R2024b: 模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要模拟水滴，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的压气机

Compressor (MA) 模块表示湿空气网络中的动态压气机，例如离心式或轴流式压气机。您可以使用 **Parameterization** 参数，基于设计点或使用表格化压气机 map 对该模块进行解析参数化。端口 **R** 相对于端口 **C** 的正旋转会使流体从端口 **A** 流向端口 **B**。端口 **R** 和端口 **C** 分别是与压气机轴和壳体相关的机械旋转守恒端口。

喘振裕度是沿等转速线的喘振压比与工作点压比之比减一。当将 **Parameterization** 设置为 `Tabulated` 时，该模块会在端口 **SM** 输出喘振裕度。

设计点是仿真期间压气机上的设计工作压比和质量流量。压气机工作点和最大效率点不需要重合。

### Compressor Map

Compressor map 绘制了压缩机的等熵效率，以及介于堵塞流动和喘振流动两个极端之间的等校正轴转速线。要可视化该模块 map，请右键单击该模块并选择 **Fluids** > **Plot Compressor Map**。每次修改模块设置后，请单击图窗上的 **Reload Data**。

Compressor map

每条校正转速线显示了当轴以相应的校正转速旋转时，压比如何随校正质量流量变化。变量 *β* 表示在两条极端线之间沿校正转速线的相对位置。堵塞流动对应于 *β* = 0，喘振流动对应于 *β* = 1。该 map 还绘制了等熵效率等值线，作为压比和校正质量流量的函数，这提供了压缩机在各种压比和校正质量流量组合下运行所需功率的相对指示。

**Corrected Mass Flow Rate**

由于压缩机内部压力和温度变化很大，compressor map 以校正质量流量来表示性能。该 map 使用参考压力和参考温度，根据入口质量流量调整校正质量流量，

m˙corr=m˙A(TARA/γATrefRref/γref/pApref),

其中：

- *ṁA* 是端口 **A** 处的质量流量。
- *TA* 是端口 **A** 处的温度。
- *Tref* 是 **Reference temperature for corrected flow** 参数的值。当您将 **Parameterization** 设置为 `Analytical` 时，该值为设计工况下的入口温度。
- *RA* 是端口 **A** 处的混合物比气体常数。
- *Rref* 是根据 **Reference pressure for corrected flow**、**Reference temperature for corrected flow** 和 **Reference relative humidity for corrected flow** 参数的值计算得到的混合物比气体常数。
- m˙*corr* 是校正质量流量。当您将 **Parameterization** 设置为 `Analytical` 时，该模块使用 **Corrected mass flow rate at design point** 参数。当您将 **Parameterization** 设置为 `Tabulated` 时，该模块使用 **Corrected mass flow rate table, mdot(N,beta)** 参数。
- *γA* 是端口 **A** 处的比热比。
- *γref* 是根据 **Reference pressure for corrected flow**、**Reference temperature for corrected flow** 和 **Reference relative humidity for corrected flow** 参数的值得到的比热比。
- *pA* 是端口 **A** 处的压力。
- *pref* 是 **Reference pressure for corrected flow** 参数的值。使用 analytical parameterization 时，该值为设计工况下的入口压力。

该模块根据比内能 *uA* 和比压力 *pA* 推导 *TA*。

**Corrected Speed**

该模块还根据参考温度调整轴转速 *ω*，使得校正轴转速为

ωcorr=ωTARA/γATrefRref/γref。

### Shaft Torque

该模块将轴扭矩 *τ* 计算为

τ=m˙AΔhtotalηmω,

其中：

- *Δhtotal* 是比总焓的变化。
- *ηm* 是 **Mechanical efficiency** 参数的值。
- *ω* 是相对轴角速度，*ωR - ωC*。

该模块将 compressor map 中的效率关联为

Δhtotal=Δhisenηisen,

其中：

- *Δhisen* 是比总焓的等熵变化。
- *ηisen* 是等熵效率。

当流量接近零时的阈值区域确保当流量接近零或反向时，压缩机不产生扭矩。

### Analytical Parameterization

您可以通过将 **Parameterization** 设置为 `Analytical` 来解析生成 compressor map。该模块根据 **Corrected speed at design point**、**Pressure ratio at design point** 和 **Corrected mass flow rate at design point** 参数的指定值，拟合基于 [1] 的 compressor map 模型。此方法不使用 *β* 线，并且该模块不报告喘振裕度。

**Pressure Ratio**

该模块根据给定轴转速和质量流量求取压比，公式为

π=1+(πD−1)[N˜ab+2N˜kln(1−m˜−N˜bk)],

其中：

- *πD* 是 **Pressure ratio at design point** 参数的值。
- N˜ 是归一化校正轴转速，

  NND,

  其中 *ND* 是 **Corrected speed at design point** 参数的值。
- m˜ 是归一化校正质量流量，

  m˙corrm˙D,

  其中 m˙*D* 是 **Corrected mass flow rate at design point** 参数的值。
- *a* 是 **Spine shape, a** 参数的值。
- *b* 是 **Speed line spread, b** 参数的值。
- *k* 是 **Speed line roundness, k** 参数的值。

*spine* 指的是等熵效率等值线开始弯曲处的黑线。该 map 的 *speed lines* 是与 spine 垂直相交的轴恒转速线。

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

  π−1πD−1,

  其中 *πD* 是 **Corrected pressure ratio at design point** 参数的值。
- m˜*0* 是压缩机达到 **Maximum isentropic efficiency** 参数值时的归一化校正质量流量。

您可以根据不同的性能特性调整效率变量。或者，您可以使用 **Constant isentropic efficiency** 参数选择恒定效率值。

### Tabulated Data Parameterization

当您将 **Parameterization** 设置为 `Tabulated` 时，压缩机的等熵效率、压比和校正质量流量是校正转速 *N* 和 map 索引 *β* 的函数。该模块对效率、压比和校正质量流量使用数据点之间的线性插值。

如果 *β* 超过 1，则发生压缩机喘振，该模块假定压比保持在 *β* = 1，而质量流量继续变化。如果仿真条件低于 *β* = 0，该模块将对堵塞流动的影响进行建模，其中质量流量保持在其 *β* = 0 时的值，而压比继续变化。为了将压缩机性能限制在 map 边界内，该模块将等熵效率外推到最近点。

您可以选择在工作点压比超过喘振压比时收到通知。将 **Report when surge margin is negative** 设置为 `Warning` 以接收警告，或设置为 `Error` 以在发生此情况时停止仿真。

### 质量守恒

当清除 **Model water droplets evaporation** 参数时，该模块保持质量守恒，使得

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中：

- m˙*B* 是端口 **B** 处的混合物质量流量。
- m˙*wA* 和 m˙*wB* 分别是端口 **A** 和 **B** 处的水蒸气质量流量。
- m˙*gA* 和 m˙*gB* 分别是端口 **A** 和 **B** 处的示踪气体质量流量。
- m˙*dA* 和 m˙*dB* 分别是端口 **A** 和 **B** 处的水滴质量流量。

如果选择 **Model water droplets evaporation**，则质量平衡方程为

m˙A+m˙B+m˙devap=0m˙wA+m˙wB−m˙devap=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙devap=0

蒸发水滴的质量流量 m˙*devap* 为

m˙devap=max{m˙A,0}rdevap.

*rdevap* 是可蒸发水滴的质量比，

rdevap=min{rdA,xwcapacity},

其取决于 *rdA*，即端口 **A** 处水滴与湿空气的质量比。

湿空气容纳更多水蒸气的能力为

xwcapacity=max{xwsB−xwA,0},

其中 *xwsB* 是饱和比湿度，*xwA* 是比湿度。

### 能量守恒

该模块按如下方式计算能量平衡方程

ΦA+ΦB+Pfluid=0,

其中：

- *ΦA* 是端口 **A** 处的能量流量。
- *ΦB* 是端口 **B** 处的能量流量。
- *Pfluid* 是传递给流体的液压功率，该模块根据比焓变化 *Δh* 确定该值，Pfluid=m˙AΔhtotal。

### 假设和限制

- 该模块假设过热流体从 **A** 进入。
- 该模块仅定义从端口 **A** 到端口 **B** 的压缩机映射流量。反向流动的结果可能不准确。
- 该模块仅表示动态压缩机。
