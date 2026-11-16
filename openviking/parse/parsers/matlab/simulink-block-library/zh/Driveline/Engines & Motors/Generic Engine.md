---
type: simulink-block
title: 'Generic Engine'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'genericengine'
documentation_source_path: 'ref/genericengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Generic Engine

## 端口

### 输入

### **Thr** — 归一化发动机节气门水平，无量纲物理信号

发动机扭矩需求，表示为最大可能扭矩的分数。该信号必须在 [0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Input type** 设置为 `Normalized throttle`。

### **Trq** — 扭矩命令，N\*m 物理信号

发动机扭矩需求，以 Nm 为单位，表示为最大可能扭矩的分数。该信号必须介于 0 和 **Maximum torque** 参数的值之间。

#### 依赖项

要启用此参数，请将 **Input type** 设置为 `Torque command`。

### 输出

### **P** — 瞬时发动机功率，W 物理信号

发动机产生的功率，单位为 W。

### **FC** — 燃油消耗率，kg/s 物理信号

发动机消耗的燃油，单位为 kg/s。

### 守恒

### **B** — 发动机缸体机械旋转

与发动机缸体关联的机械旋转守恒端口。这是基础端口。发动机缸体是包含活塞气缸的物理体。

### **F** — 发动机曲轴机械旋转

与发动机曲轴关联的机械旋转守恒端口。这是发动机的从动端口。曲轴传递燃烧过程产生的功率。通常，将离合器和变速器连接到此端口。

## 参数

### 发动机规格

### **Input type** — 通过归一化节气门或扭矩驱动的选项 `Normalized throttle`（默认）| `Torque command`

模块接收归一化节气门命令还是扭矩命令。这些设置控制端口：

- `Normalized throttle` — 启用
  物理信号端口 **Thr**，该端口
  接受介于 0 和 1 之间的无量纲节气门命令。
- `Torque command` — 启用
  物理信号端口 **Trq**，该端口接受
  介于 0 和最大扭矩之间的扭矩命令。

### **Model parameterization** — 发动机模型 `Normalized 3rd-order polynomial matched to peak power`（默认）| `Tabulated torque data` | `Tabulated power data`

发动机模型。根据可用数据在这些选项之间选择：

- `Normalized 3rd-order polynomial`
  — 使用由功率和速度特性定义的功率曲线查找表来参数化发动机。
- `Tabulated torque data` —
  使用速度-扭矩表来参数化发动机。
- `Tabulated power data` —
  使用速度-功率表来参数化发动机。

### **Engine type** — 要建模的燃烧过程 `Spark-ignition`（默认）| `Diesel` | `Generic`

要建模的内燃过程。您可以基于最大扭矩、最大扭矩转速和最大速度来参数化火花点火发动机、柴油发动机或通用发动机。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Maximum torque** — 发动机扭矩输出的物理极限 `380` `N*m`（默认）| 正标量

发动机可输出的峰值扭矩 *TP*。该值设置速度-扭矩曲线的峰值。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Generic`。

### **Speed at maximum torque** — 发动机达到最大功率输出时的曲轴角速度 `4300` `rpm`（默认）| 正标量

发动机产生峰值扭矩 *ɷPT* 时的发动机转速。该值设置扭矩曲线上峰值出现的位置。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Generic`。

### **Maximum power** — 发动机功率输出的物理极限 `230` `kW`（默认）| 正标量

发动机可输出的最大功率 *PP*。该值设置速度-功率曲线的峰值。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Spark-ignited` 或 `Diesel`。

### **Speed at maximum power** — 发动机达到最大扭矩输出时的曲轴角速度 `6858` `rpm`（默认）| 正标量

发动机以最大功率运行时的发动机转速 *ɷPP*。该值设置功率曲线上峰值出现的位置。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Spark-ignited` 或 `Diesel`。

### **Maximum speed** — 最大曲轴角速度 `7000` `rpm`（默认）| 正标量

发动机可产生扭矩的最大速度 *ɷmax*。该值设置功率曲线的上限。

在仿真期间，如果 *ɷ* 超过该值，仿真将停止并报错。发动机最大速度 *ɷmax* 不能超过发动机功率变为负值时的发动机转速。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Stall speed** — 发动机截止速度 `500` `rpm`（默认）| 正标量

发动机可产生扭矩的最小速度 *ɷmin*。该值设置功率曲线的下限。

在仿真期间，如果 *ɷ* 低于该值，发动机扭矩将混合到零。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Stall speed threshold** — 发动机截止阈值 `100` `rpm`（默认）| 正标量

在速度低于 *ɷmin* 后，发动机速度过渡到零的阈值速度。使用此参数可在熄火期间调整仿真性能。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Speed vector** — 表格化发动机速度数据 `[500, 1000, 2000, 3000, 4300, 5000, 6000, 7000]` `rpm`（默认）| 向量

发动机速度向量，用于为模型参数化查找表提供信息。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data` 或 `Tabulated power data`。

### **Torque vector** — 表格化发动机扭矩数据 `[250, 280, 330, 360, 380, 370, 350, 310]` `N*m`（默认）| 向量

给定速度下的扭矩值向量。此向量的大小必须与 **Speed vector** 参数匹配。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data`。

### **Power vector** — 表格化发动机功率数据 `[10, 30, 70, 110, 165, 190, 220, 230]` `kW`（默认）| 向量

给定速度下的功率值向量。此向量的大小必须与 **Speed vector** 参数匹配。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated power data`。

### **Interpolation method** — 中间点计算方法 `Linear`（默认）| `Smooth`

用于计算中间速度-扭矩值处燃油消耗的方法。超出数据范围后，燃油消耗保持为查找表的最终值。

#### 依赖项

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data` 或 `Tabulated power data`。

### 动力学

### **Inertia** — 启用惯性建模参数 `No inertia`（默认）| `Specify inertia and initial velocity`

用于参数化惯性和初始速度的选项。您可以选择对惯性建模，以提高保真度或数值稳定性。

### **Engine inertia** — 发动机曲轴旋转惯性 `1` `kg*m^2`（默认）| 正标量

初始旋转惯性。此参数初始化发动机惯性计算。

#### 依赖项

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Initial velocity** — 发动机曲轴角速度 `800` `rpm`（默认）| 正标量

初始角速度。此参数初始化发动机惯性计算。

### **Time constant** — 启用发动机滞后建模参数 `No lag - Suitable for HIL simulation`（默认）| `Specify time constant and initial value`

用于参数化时间常数和初始归一化发动机节气门的选项。

### **Engine time constant** — 发动机滞后值 `0.2` `s`（默认）| 正标量

发动机响应的时间延迟。此参数指定节气门信号与发动机响应之间的滞后。

#### 依赖项

要启用此参数，请将 **Time constant** 设置为 `Specify time constant and initial value`。

### **Initial normalized throttle** — 发动机初始节气门值 `0`（默认）| [0,1] 范围内的标量

初始归一化发动机节气门。此值必须在 [0,1] 范围内。为此参数指定正值以包含滞后。

#### 依赖项

要启用此参数，请将 **Time constant** 设置为 `Specify time constant and initial value`。

### 燃油消耗

该表显示了 **Fuel consumption model** 参数的选项如何影响依赖参数的可用性。

**燃油消耗参数依赖关系**

| **燃油消耗** | | | | |
| --- | --- | --- | --- | --- |
| **Fuel consumption model** | | | | |
| `No fuel consumption` | `Constant per revolution` | `Fuel consumption by speed and torque` | `Brake specific fuel consumption by speed and torque` | `Brake specific fuel consumption by speed and brake mean effective pressure` |
| **Fuel consumption per revolution** | **Displaced volume** |
| **Revolutions per cycle** |
| **Speed vector** | | |
| **Torque vector** | | **Brake mean effective pressure vector** |
| **Fuel consumption table** | **Brake specific fuel consumption table** | |
| **Interpolation method** | | |

### **Fuel consumption model** — 启用燃油消耗建模参数 `No fuel consumption`（默认）| `Constant per revolution` | `Fuel consumption by speed and torque` | ...

基于可用数据的燃油消耗方法。这些方法启用与典型工业数据一致的参数。从以下选项中选择：

- `No fuel consumption`
- `Constant per revolution`
- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

如果将 **Fuel consumption model** 设置为 `No fuel consumption`，即使 **FC** 端口连接到另一个模块，该模块也不会计算燃油消耗。选择此选项可提高仿真速度。

### **Fuel consumption per revolution** — 常数 `25` `mg/rev`（默认）| 正标量

作为曲轴转数函数的恒定燃油消耗率。输入一个曲轴转数内消耗的燃油体积。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Constant per revolution`。

### **Speed vector** — 发动机速度数据 `[1000, 2000, 3000, 4000, 5000, 6000]`（默认）| 向量

对应于燃油消耗查找表 *M* 行的发动机扭矩向量。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为以下设置之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

### **Torque vector** — 发动机扭矩数据 `[0, 80, 160, 200, 240, 320, 360, 400]`（默认）| 向量

对应于燃油消耗查找表 *N* 列的发动机扭矩向量。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and torque`。

### **Fuel consumption table** — 发动机燃油消耗数据 *M*×*N* 矩阵（默认）| 矩阵

对应于发动机速度和扭矩向量的燃油消耗值矩阵。行数必须等于 **Speed vector** 参数中的元素数。列数必须等于 **Torque vector** 参数中的元素数。默认值为 `[.5, .9, 1.4, 1.6, 1.9, 2.7, 3.4, 4.4; 1, 1.7, 2.7, 3.1, 3.6, 5, 6, 7.4; 1.4, 2.7, 4, 4.8, 5.6, 7.5, 8.5, 10.5; 2, 3.6, 5.8, 6.7, 8, 10.4, 11.7, 13.3; 2.5, 4.8, 7.9, 9.4, 10.8, 14, 16.2, 18.6; 3.1, 6, 10.3, 11.9, 13.8, 18.4, 22, 26.5]` `g/s`。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque`。

### **Brake mean effective pressure vector** — 活塞压力数据 `[0, 250, 500, 625, 750, 1000, 1150, 1250]`（默认）| 向量

制动平均有效压力 (BMEP) 值向量。BMEP 值满足表达式：

BMEP=T⋅(2π⋅ncVd),

其中：

- *T* 是输出扭矩。
- *nc* 是每转的循环数。
- *Vd* 是气缸排量。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Brake specific fuel consumption table** — 制动比燃油消耗数据 *M*×*N* 矩阵（默认）| 矩阵

当您将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and torque` 时，此参数是制动比燃油消耗 (BSFC) 率矩阵，对应于发动机速度和扭矩向量。BSFC 是燃油消耗率与输出功率之比。

当您将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure` 时，此参数是制动比燃油消耗 (BSFC) 率矩阵，对应于发动机速度和制动平均有效压力 (BMEP) 向量。BSFC 是燃油消耗率与输出功率之比。

对于这两种燃油消耗模型，行数必须等于 **Speed vector** 参数中的元素数。列数必须等于 **Torque vector** 参数或 **Brake mean effective pressure vector** 参数中的元素数。默认值为 `[410, 380, 300, 280, 270, 290, 320, 380; 410, 370, 290, 270, 260, 270, 285, 320; 415, 380, 290, 275, 265, 270, 270, 300; 420, 390, 310, 290, 285, 280, 280, 285; 430, 410, 340, 320, 310, 300, 310, 320; 450, 430, 370, 340, 330, 330, 350, 380]` `g/(hr*kW)`。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Displaced volume** — 单个活塞冲程排出的燃油体积 `400` `cm^3`（默认）| 正标量

活塞冲程燃油排量。这等于圆形活塞气缸横截面积乘以活塞行程距离。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Interpolation method** — 中间步骤行为 `Linear`（默认）| `Smooth`

用于计算中间速度和扭矩值处燃油消耗的插值方法。超出查找表范围后，燃油消耗保持恒定。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为以下设置之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

### **Revolutions per cycle** — 燃烧循环转数 `2`（默认）| `1`

一个燃烧循环中的曲轴转数。对于四冲程发动机输入 `2`，对于二冲程发动机输入 `1`。

#### 依赖项

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### 速度控制

### **怠速速度控制** — 启用速度控制参数 `Off`（默认）| `On`

启用速度控制的选项。速度控制使发动机在给定设定值下怠速。
当所施加的节气门不足以转动时，发动机怠速可防止熄火。当您启用速度控制时，该模块会施加足够的节气门，以至少维持 **怠速速度参考值** 参数值。有关详细信息，请参阅怠速速度控制器模型。

### **怠速速度参考值** — 稳态怠速速度 `1000` `rpm`（默认）| 正标量

曲轴的参考角速度。怠速速度控制器至少维持此速度。

#### 依赖关系

要启用此参数，请选择 **怠速速度控制**。

### **控制器时间常数** — 怠速控制器响应延迟 `1` `s`（默认）| 正标量

对偏离 **怠速速度参考值** 参数值的响应时间。

#### 依赖关系

要启用此参数，请将 **怠速速度控制** 设置为 `On`。

### **控制器阈值速度** — 控制器响应平滑度 `1` `rpm`（默认）| 正标量

控制器平滑参数。当发动机转速越过怠速速度参考值时，**控制器阈值速度** 会平滑受控节气门值。有关详细信息，请参阅怠速速度控制器模型。较大的值会降低控制器响应性。较小的值会增加计算成本。此参数必须为正。

#### 依赖关系

要启用此参数，请选择 **怠速速度控制**。

### **红线控制** — 启用红线控制参数 `Off`（默认）| `On`

用于启用发动机曲轴最大角速度限制器的选项。当您将 **红线控制** 设置为 `On` 时，该模块会阻止发动机速度超过最大设定值。

### **红线速度** — 曲轴速度控制峰值阈值 `5000` `rpm`（默认）| 正标量

红线控制发动机速度设定值。输入使红线控制激活的速度参考值。

#### 依赖关系

要启用此参数，请选择 **红线控制**。

### **红线时间常数** — 红线控制器响应延迟 `1` `s`（默认）| 正标量

对超过 **红线速度** 参数值的发动机速度的响应时间。输入与受控节气门增加或减少相关联的时间常数值。

#### 依赖关系

要启用此参数，请选择 **红线控制**。

### **红线阈值速度** — 红线控制器响应平滑度 `1` `rpm`（默认）| 正标量

红线过渡的角速度范围。指定红线速度周围区域的范围，其中控制器从完全启用过渡到未启用。当发动机转速越过红线速度参考值时，该模块使用此参数平滑受控节气门值。较大的值会降低控制器响应性。较小的值会增加计算成本。

#### 依赖关系

要启用此参数，请选择 **红线控制**。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

通用内燃机

Generic Engine 模块表示可配置的内燃机，适用于 spark-ignition 和 diesel 应用。您可以使用扭矩或归一化节气门物理信号来控制该模块。您可以使用三阶多项式，或使用表格化的扭矩或功率数据来参数化该模块。可选的动态参数包括曲轴惯量和响应时间滞后。物理信号端口 **FC** 会根据您选择的燃油消耗模型输出发动机燃油消耗率。可选的速度和红线控制器可防止发动机熄火并启用巡航控制。该图显示了端口与发动机配置的关系。

### 发动机速度、节气门、功率和扭矩

默认情况下，Generic Engine 模块使用扭矩和速度之间的编程关系，该关系由节气门信号或扭矩命令信号调制。

该模块将发动机功率需求评估为发动机速度的函数 *g(ɷ)*。该函数提供给定发动机速度 *ɷ* 下可用的最大功率。模块参数 **最大功率**、**最大功率时的速度** 和 **最大速度** 可将此函数归一化为物理最大扭矩和速度值。

归一化节气门信号 *Thr* 控制发动机功率，使得 *P(**ɷ**,Thr)* = *Thr*·*g(**ɷ**)*。当您将 **模型参数化** 设置为 `Normalized throttle` 时，物理输入信号 **Thr** 控制发动机功率。当您选择 `Torque command` 时，该模块在内部计算归一化节气门。该模块以在固定发动机速度下稳态可能的最大功率的分数形式提供功率。该图显示了默认设置下的扭矩和功率曲线。

发动机扭矩曲线为蓝色实线。发动机功率曲线为橙色虚线。

请注意，瞬态期间端口 **F** 处可用的扭矩可能与记录变量 `trq` 的值不同。记录变量跟踪产生的扭矩，不考虑因系统惯量损失的扭矩。

### 多项式发动机控制

当您将 **模型参数化** 设置为 `Normalized 3rd-order polynomial` 时，该模块使用归一化发动机速度 *ɷN* 来计算速度和扭矩。该模块将归一化发动机速度定义为

ωN(ω)≡ωωPP

其中：

- *ɷ* 是当前发动机速度。
- *ɷPP* 是峰值功率时的发动机速度。

该模块将归一化、无量纲的发动机功率视为三阶多项式，使得

P(ω(ωN))=PP⋅pN(ωN)pN(ωN)=s1ωN+s2ωN2+s3ωN3

其中 *s1*、*s2* 和 *s3* 是常数多项式系数，*Pp* 是峰值功率。在典型发动机中，*si* 系数为正。

该模块使用多项式系数计算节气门全开条件下的发动机扭矩，使得

T(ω(ωN))=p1+p2ωN+p3ωN2p1≡s1Pp/ωppp2≡s2Pp/ωppp3≡s3Pp/ωpp

该模块将峰值功率处的归一化发动机速度设置为

ωNPP=ωN(ωNPP)=1.

将此等式代入 *pN* 的公式，得到

s1+s2+s3=1.

此条件将功率归一化到峰值功率处的发动机速度。该模块将 *pN(ɷPP)* 的斜率设置为零，使得

s1+2s2+3s3=0.

该模块将峰值扭矩的归一化发动机速度定义为

ωNPT=ωN(ωPT)=ωPTωPP<1

其中峰值功率的速度大于峰值扭矩的速度。该模块使用多项式公式来求无量纲的归一化扭矩 *τN*，并将斜率设置为零，使得

dτN(ωNPT)dω=s2+2s3ωNPT=0.

使用这些方程求解 *si*，得到

s1=3−4ωNPT2(1−ωNPT)s2=−ωNPTωNPT−1s3=12(ωNPT−1)

该模块计算发动机扭矩为

T(ω(ωN))=2TP3−ωNPT(s1+s2ωN+s3ωN2),

其中 *TP* 是峰值扭矩。代入 *ɷNPT* 的方程，得到约束

2TPωPP2−3PPωPP+PPωPT=0.

该模块使用 *TP*、*PP* 和 *ɷPT* 来计算峰值功率处的发动机速度，使得

ωPP=3PP+PP(9PP−8TPωPT)4TP>ωPT.

其中 *TPɷPT* 等效于峰值扭矩处的功率 *PPT*，其始终小于峰值功率 *PP*。

**不同发动机类型的发动机功率形式**

该模块使用 **发动机类型** 参数设置对应的系数来计算多项式。当您将 **发动机类型** 设置为 `Spark-ignition` 或 `Diesel` 时，该模块从表中选择相应的系数。当您选择 `Generic` 时，该模块在内部计算这些系数。

| 功率需求系数 | 发动机类型 | |
| --- | --- | --- |
| Spark-Ignition | Diesel |
| *s1* | 1 | 0.6526 |
| *s2* | 1 | 1.6948 |
| *s 3* | -1 | -1.3474 |

### 燃油消耗

该模块可以选择性地对燃油消耗建模，并将结果作为物理信号在端口 **FC** 输出。要在仿真中包含燃油消耗，请将 **燃油消耗模型** 设置为以下设置之一：

- `Constant per revolution`
- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

您可以创建燃油消耗的可视化表示。当您将 **燃油消耗模型** 设置为 `Fuel consumption by speed and torque` 并单击模块描述中的 **发动机属性** 超链接时，实时脚本会为给定扭矩和速度生成燃油消耗热图。

给定扭矩和速度的燃油消耗热图。

此图是发动机速度、节气门、功率和扭矩图之外的附加图。当您将 **燃油消耗模型** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure` 时，实时脚本会生成燃油消耗热图以及制动比燃油消耗的单独图。

给定扭矩和速度的燃油消耗热图，以及给定扭矩和速度的制动比燃油消耗热图。

### 怠速速度控制器模型

怠速速度控制器调整节气门信号，以根据以下公式在低于参考速度时增加发动机转速：

Π=max(Πi,Πc)

并且

d(Πc)dt=0.5⋅(1−tanh(4⋅ω−ωrωt))−Πcτ

其中：

- *Π* 是发动机节气门。
- *Πi* 是输入节气门端口 **Thr**。
- *Πc* 是控制器节气门。
- *ω* 是发动机速度或曲轴角速度。
- *ωr* 是怠速速度参考值。
- *ωt* 是控制器速度阈值。
- *τ* 是控制器时间常数。

当发动机速度降至参考速度以下时，受控节气门以一阶滞后从 0 增加到 1。当发动机速度升至参考速度以上时，受控节气门从 1 减少到 0。当发动机速度与参考速度之差小于控制器速度阈值时，方程中的 *tanh* 部分会平滑受控节气门的时间导数。平滑函数将受控节气门限制在范围 [0,1] 内。发动机使用输入节气门值和受控节气门值中的较大者。如果您包含发动机时间滞后，控制器会在计算滞后之前更改输入。

### 红线控制器模型

怠速速度控制器确定用于维持发动机速度的最小节气门值，红线控制器基于最大节气门输入防止速度过高。为了确定最大节气门值，红线控制器使用怠速速度控制器模型方程。但是，对于红线控制器：

- *ωr* 是红线速度参考值。
- *ωt* 是红线速度阈值。
- *τ* 是红线时间常数。

### 性能

要提高仿真速度，请将 **燃油消耗模型** 设置为 `No fuel consumption`。使用此设置时，无论端口 **FC** 如何，该模块都不会计算燃油消耗。

如果您为 **燃油消耗模型** 选择任何其他选项，则该模块必须执行非线性计算。即使报告燃油消耗率的 **FC** 端口未连接到另一个模块，该模块也会求解方程。

### 预定义参数化

您可以使用预参数化的制造数据填充该模块，从而允许您对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **选定部件** 旁边，单击模块对话框设置中 **选定部件** 旁边的 "<单击以选择>" 超链接。
2. 模块参数化管理器窗口打开。从菜单中选择一个部件，然后单击 **全部应用**。您可以使用 **制造商** 下拉菜单缩小选择范围。
3. 您可以关闭 **模块参数化管理器** 菜单。该模块现在具有您指定的参数化。
4. 您可以在模块参数化管理器窗口中选择一个部件，并在 **将选定部件与模块比较** 部分查看数据，从而将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源来提供参数值。该模块对缺失数据使用工程判断和简化假设进行替代。因此，预计仿真行为与实际物理行为之间会存在一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

### 假设和限制

发动机对速度和节气门变化的响应存在滞后。该模块仅支持因节气门变化引起的滞后。

### 硬件在环仿真

为提高 HIL 仿真的性能，请将 **动力学** > **时间常数** 参数设置为 `No time constant - Suitable for HIL simulation`。
