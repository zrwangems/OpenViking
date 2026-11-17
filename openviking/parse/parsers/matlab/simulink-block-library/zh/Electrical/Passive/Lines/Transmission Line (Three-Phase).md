---
type: simulink-block
title: 'Transmission Line (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'transmissionlinethreephase'
documentation_source_path: 'ref/transmissionlinethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission Line (Three-Phase)

## 端口

### 守恒端口

### **~1** — 三相端口 electrical

可扩展三相端口。

### **~2** — 三相端口 electrical

可扩展三相端口。

### **g1** — 端 ~1 处的接地连接 electrical

对应于传输线 `~1` 端接地连接的电气守恒端口。

### **g2** — 端 ~2 处的接地连接 electrical

对应于传输线 `~2` 端接地连接的电气守恒端口。

### **g1'** — 故障位置 1 处的接地连接 electrical

对应于故障位置 1 处接地连接的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Accessible ground connections at section interface** 设置为 `Yes`

### **g2'** — 故障位置 2 处的接地连接 electrical

对应于故障位置 2 处接地连接的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Accessible ground connections at section interface** 设置为 `Yes`

## 参数

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各相。

### 主

### **Line length** — 传输线的长度 `1` `km`（默认）

传输线的长度。

### **Frequency used for rlcg specification** — 用于 rlcg 规格的频率 `60` `Hz`（默认）| 正标量

用于 R、L、C、G 规格的频率，其中：

- **R** 是单位长度的线路电阻。
- **L** 是单位长度的线路电感。
- **C** 是单位长度的线路电容。
- **G** 是单位长度的线路电导。

### **Resistance** — 传输线的电阻 `0.02` `Ohm/km`（默认）

传输线每相单位长度的电阻。

### **Inductance** — 传输线的自感 `0.5` `mH/km`（默认）

传输线每相单位长度的自感。

### **Mutual inductance** — 线间互感 `0.1` `mH/km`（默认）

单位长度的线间互感。将此值设置为 `0` 可移除互感。

### **Line-line capacitance** — 线间电容 `0.3` `μF/km`（默认）

单位长度的线间电容。

### **Line-ground capacitance** — 线地电容 `0.1` `μF/km`（默认）

单位长度的线地电容。

### **Mutual resistance** — 线间互阻 `0` `Ohm/km`（默认）

单位长度的线间互阻。默认值为 `0``Ohm/km`（无线间互阻）。

### **Model two line sections** — 线间互阻 `No`（默认）| `Yes`

将传输线建模为两个区段的选项。您必须启用此参数才能在 Transmission Line (Three-Phase) 模块中添加非侵入式故障。

### **Number of segments** — 区段数 `1`（默认）

pi 线路模型中的区段数。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `No`。

### **Position of section interface** — 区段接口的位置 `0.5` `Km`（默认）

pi 线路模型中接口的位置。如果您添加非侵入式故障，此参数表示 pi 线路模型中故障的位置。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `Yes`。

### **Number of segments in first section** — 第一区段中的区段数 `1`（默认）

pi 线路模型第一区段中的区段数。如果您添加非侵入式故障，此参数表示故障发生前的区段数。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `Yes`。

### **Number of segments in second section** — 第二区段中的区段数 `1`（默认）

pi 线路模型第二区段中的区段数。如果您添加非侵入式故障，此参数表示故障发生后的区段数。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `Yes`。

### **Accessible ground connections at section interface** — 访问故障位置处接地连接的选项 `No`（默认）| `Yes`

访问故障位置处接地连接的选项。如果将此参数设置为 `No`，模块会在内部将故障位置处的接地连接连接到电气参考。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `Yes`。

### 寄生参数

### **Parasitic series resistance** — 寄生串联电阻 `1e-6` `Ohm`（默认）

电阻值除以区段数，该电阻与模型中的每个电容器串联添加。

### **Parasitic parallel conductance** — 寄生并联电导 `1e-6` `1/Ohm`（默认）

电导值除以区段数，该电导与模型中的每个串联电阻和电感并联添加。

### 故障

要修改故障，请创建一个故障，然后在模块对话框中点击 **Open fault properties**。要打开故障，请在 Property Inspector 中点击 **Fault behavior** 链接。

### **Section interface fault** — 向区段接口添加故障的选项 `Add fault`

向 pi 线路模型的区段接口添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Model two line sections** 设置为 `Yes`。

### **Fault type** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

要建模的故障类型。相关参数的可见性取决于故障模型。选项包括：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

#### 依赖关系

要启用此参数，请通过点击 **Section interface fault** 参数旁边的 **Add fault** 超链接，向 Transmission Line (Three-Phase) 模块添加故障。

### **Faulted phase-neutral resistance** — 故障相-中性点电阻 `1e-3` `Ohm`（默认）

故障激活时，相连接与中性点之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **Section interface fault** 参数旁边的 **Add fault** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **Fault type** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **Faulted neutral-ground resistance** — 故障中性点-地电阻 `1e-3` `Ohm`（默认）

故障激活时，中性点与电气参考之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **Section interface fault** 参数旁边的 **Add fault** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **Fault type** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **Unfaulted phase-neutral conductance** — 未故障相-中性点电导 `1e-6` `1/Ohm`（默认）

故障未激活时，相连接与中性点之间的电导。

#### 依赖关系

要启用此参数，请通过点击 **Section interface fault** 参数旁边的 **Add fault** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **Fault type** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

使用集中参数 pi 型线路模型的三相传输线

Transmission Line (Three-Phase) 模块使用集中参数 pi 型线路模型对三相传输线进行建模。该模型考虑了相电阻、相自感、线间互感和互阻、线间电容以及线地电容。

为简化模块定义方程，使用了 Clarke 变换。所得方程为：

V1′−V2′=[R+2RmR−RmR−Rm]I1′+[L+2ML−ML−M]dI1′dt

I1′+I2′=[CgCg+3ClCg+3Cl]dV2′dt

I1′=T′I1

I2′=T′I2

V1′=T′V1

V2′=T′V2

T=13[1201−12321−12−32]

其中：

- *R* 是该区段的线路电阻。
- *Rm* 是该区段的互阻。
- *L* 是该区段的线路电感。
- *M* 是 **Mutual inductance** 参数的值。
- *Cg* 是该区段的线地电容。
- *Cl* 是该区段的线间电容。
- *T* 是 Clarke 变换矩阵。
- *I1* 是流入 `~1` 端口的三相电流。
- *I2* 是流入 `~2` 端口的三相电流。
- *V1* 是 `~1` 端口处的三相电压。
- *V2* 是 `~2` 端口处的三相电压。

正序和零序参数由变换方程中的对角项定义：

R0=R+2Rm

R1=R−Rm

L0=L+2M

L1=L−M

C0=Cg

C1=Cg+3Cl

重新整理这些方程，可用正序和零序参数表示物理线路量：

R=2R1+R03

Rm=R0−R13

L=2L1+L03

M=L0−L13

Cl=C1−C03

Cg=C0

该图显示了使用 Clarke 变换的单区段 pi 型线路模型的等效电路。

为提高保真度，您可以使用 **Number of segments** 参数将 pi 区段重复 N 次，从而得到 N 区段传输线模型。更多的区段会显著降低仿真速度。

为提高数值性能，您可以添加寄生电阻和电导分量。为这些分量选择较大的值可提高仿真速度，但会降低仿真精度。

### 传播速度

Transmission Line (Three-Phase) 使用以下方程计算正序传播速度：

- Z1=R1+jωL1 是串联阻抗，单位为 `Ω/Km`。
- Y1=jωC1 是并联导纳，单位为 `s/Km`。
- γ1=Z1Y1 是传播常数。
- ν1=ωImag(γ1) 是传播速度，单位为 `Km/s`，其中 ω=2πf。

对于零序传播速度，方程相同，但 *R1*、*L1*、*C1*、*Z1*、*Y1*、*γ1* 和 *ν1* 分别替换为 *R0*、*L0*、*C0*、*Z0*、*Y0*、*γ0* 和 *ν0*。

### 故障

要在 Transmission Line (Three-Phase) 模块中对故障进行建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

Transmission Line (Three-Phase) 模块允许您对传输线上特定位置处的以下故障类型进行建模：

- 单相接地故障（a-g、b-g 或 c-g）
- 两相故障（a-b、b-c 或 c-a）
- 两相接地故障（a-b-g、b-c-g 或 c-a-g）
- 三相故障（a-b-c）
- 三相接地故障（a-b-c-g）
