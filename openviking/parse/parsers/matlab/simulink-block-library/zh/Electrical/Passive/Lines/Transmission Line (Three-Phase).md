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

### 守恒

### **~1** — 三相端口 electrical

可扩展三相端口。

### **~2** — 三相端口 electrical

可扩展三相端口。

### **g1** — ~1 端处的接地连接 electrical

与传输线 `~1` 端处的接地连接对应的电气守恒端口。

### **g2** — ~2 端处的接地连接 electrical

与传输线 `~2` 端处的接地连接对应的电气守恒端口。

### **g1'** — 故障位置 1 处的接地连接 electrical

与故障位置 1 处的接地连接对应的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **区段接口处的可访问接地连接** 设置为 `Yes`

### **g2'** — 故障位置 2 处的接地连接 electrical

与故障位置 2 处的接地连接对应的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **区段接口处的可访问接地连接** 设置为 `Yes`

## 参数

### **建模选项** — 是建模复合三相端口还是扩展三相端口 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

是建模复合三相端口还是扩展三相端口。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### 主要

### **线路长度** — 传输线长度 `1` `km` (默认)

传输线的长度。

### **用于 rlcg 指定的频率** — 用于 rlcg 指定的频率 `60` `Hz` (默认) | 正标量

用于 R、L、C、G 指定的频率，其中：

- **R** 是单位长度的线路电阻。
- **L** 是单位长度的线路电感。
- **C** 是单位长度的线路电容。
- **G** 是单位长度的线路电导。

### **电阻** — 传输线电阻 `0.02` `Ohm/km` (默认)

每相单位长度的传输线电阻。

### **电感** — 传输线自感 `0.5` `mH/km` (默认)

每相单位长度的传输线自感。

### **互电感** — 线间互电感 `0.1` `mH/km` (默认)

单位长度的线间互电感。将其设置为 `0` 可移除互电感。

### **线间电容** — 线间电容 `0.3` `μF/km` (默认)

线间电容长度，按单位长度计。

### **线对地电容** — 线对地电容 `0.1` `μF/km` (默认)

线对地电容长度，按单位长度计。

### **互电阻** — 线间互电阻 `0` `Ohm/km` (默认)

单位长度的线间互电阻。默认值为 `0``Ohm/km`（无线路间互电阻）。

### **对两个线路区段建模** — 线间互电阻 `No` (默认) | `Yes`

将传输线建模为两个区段的选项。必须启用此参数，才能在 Transmission Line (Three-Phase) 模块中添加非侵入式故障。

### **区段数** — 区段数 `1` (默认)

pi 型线路模型中的区段数。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `No`。

### **区段接口位置** — 区段接口位置 `0.5` `Km` (默认)

pi 型线路模型中接口的位置。如果添加非侵入式故障，此参数表示 pi 型线路模型中故障的位置。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `Yes`。

### **第一个区段中的区段数** — 第一个区段中的区段数 `1` (默认)

pi 型线路模型第一个区段中的区段数。如果添加非侵入式故障，此参数表示故障发生前的区段数。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `Yes`。

### **第二个区段中的区段数** — 第二个区段中的区段数 `1` (默认)

pi 型线路模型第二个区段中的区段数。如果添加非侵入式故障，此参数表示故障发生后的区段数。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `Yes`。

### **区段接口处的可访问接地连接** — 访问故障位置接地连接的选项 `No` (默认) | `Yes`

访问故障位置接地连接的选项。如果将此参数设置为 `No`，模块会在内部将故障位置处的接地连接连接到电气参考。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `Yes`。

### 寄生

### **寄生串联电阻** — 寄生串联电阻 `1e-6` `Ohm` (默认)

电阻值，除以区段数，串联添加到模型中的每个电容器。

### **寄生并联电导** — 寄生并联电导 `1e-6` `1/Ohm` (默认)

电导值，除以区段数，并联添加到模型中的每个串联电阻和电感器。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **打开故障属性**。要打开故障，请在属性检查器中点击 **故障行为** 链接。

### **区段接口故障** — 向区段接口添加故障的选项 `Add fault`

向 pi 型线路模型的区段接口添加故障的选项。

要添加故障，请点击 **添加故障** 超链接。

#### 依赖关系

要启用此参数，请将 **对两个线路区段建模** 设置为 `Yes`。

### **故障类型** — 故障类型 `Single-phase to ground (a-g)` (默认) | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

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

要启用此参数，请通过点击 **区段接口故障** 参数旁边的 **添加故障** 超链接，向 Transmission Line (Three-Phase) 模块添加故障。

### **故障相-中性点电阻** — 故障相-中性点电阻 `1e-3` `Ohm` (默认)

故障激活时，相连接与中性点之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **区段接口故障** 参数旁边的 **添加故障** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **故障类型** 参数设置为：

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

### **故障中性点-接地电阻** — 故障中性点-接地电阻 `1e-3` `Ohm` (默认)

故障激活时，中性点与电气参考之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **区段接口故障** 参数旁边的 **添加故障** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **故障类型** 参数设置为：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **未故障相-中性点电导** — 未故障相-中性点电导 `1e-6` `1/Ohm` (默认)

故障未激活时，相连接与中性点之间的电导。

#### 依赖关系

要启用此参数，请通过点击 **区段接口故障** 参数旁边的 **添加故障** 超链接，向 Transmission Line (Three-Phase) 模块添加故障，并将 **故障类型** 参数设置为：

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

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

使用集中参数 pi 型线路模型的三相传输线

Transmission Line (Three-Phase) 模块使用集中参数 pi 型线路模型对三相传输线建模。该模型考虑相电阻、相自感、线间互感和电阻、线间电容以及线对地电容。

为简化模块定义方程，使用了 Clarke 变换。得到的方程为：

V1′−V2′=[R+2RmR−RmR−Rm]I1′+[L+2ML−ML−M]dI1′dt

I1′+I2′=[CgCg+3ClCg+3Cl]dV2′dt

I1′=T′I1

I2′=T′I2

V1′=T′V1

V2′=T′V2

T=13[1201−12321−12−32]

其中：

- *R* 是区段的线路电阻。
- *Rm* 是区段的互电阻。
- *L* 是区段的线路电感。
- *M* 是 **互电感** 参数的值。
- *Cg* 是区段的线对地电容。
- *Cl* 是区段的线间电容。
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

重新排列这些方程，可以得到用正序和零序参数表示的物理线路量：

R=2R1+R03

Rm=R0−R13

L=2L1+L03

M=L0−L13

Cl=C1−C03

Cg=C0

该图展示了使用 Clarke 变换的单区段 pi 型线路模型的等效电路。

为了提高保真度，可以使用 **区段数** 参数将 pi 区段重复 N 次，从而得到 N 区段传输线模型。更多区段会显著减慢仿真速度。

为了提高数值性能，可以添加寄生电阻和电导分量。为这些分量选择较大的值可以提高仿真速度，但会降低仿真精度。

### 传播速度

Transmission Line (Three-Phase) 使用以下方程计算正序传播速度：

- Z1=R1+jωL1 是串联阻抗，单位为 `Ω/Km`。
- Y1=jωC1 是并联导纳，单位为 `s/Km`。
- γ1=Z1Y1 是传播常数。
- ν1=ωImag(γ1) 是传播速度，单位为 `Km/s`，其中 ω=2πf。

对于零序传播速度，方程相同，但 *R1*、*L1*、*C1*、*Z1*、*Y1*、*γ1* 和 *ν1* 分别为 *R0*、*L0*、*C0*、*Z0*、*Y0*、*γ0* 和 *ν0*。

### 故障

要在 Transmission Line (Three-Phase) 模块中对故障建模，请在 **故障** 部分中，点击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

Transmission Line (Three-Phase) 模块允许您在传输线沿线的特定位置对以下类型的故障建模：

- 单相接地故障（a-g、b-g 或 c-g）
- 两相故障（a-b、b-c 或 c-a）
- 两相接地故障（a-b-g、b-c-g 或 c-a-g）
- 三相故障（a-b-c）
- 三相接地故障（a-b-c-g）
