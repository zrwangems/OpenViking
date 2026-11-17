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

### **Thr** — 归一化发动机节气门开度，无量纲物理信号

发动机扭矩需求，表示为最大可能扭矩的分数。此信号必须在 [0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Normalized throttle`。

### **Trq** — 扭矩指令，N\*m 物理信号

发动机扭矩需求，表示为最大可能扭矩的分数，单位为 Nm。此信号必须在 0 与 **Maximum torque** 参数的值之间。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Torque command`。
### 输出

### **P** — 瞬时发动机功率，W 物理信号

发动机产生的功率，单位为 W。

### **FC** — 燃油消耗率，kg/s 物理信号

发动机消耗的燃油，单位为 kg/s。
### 守恒

### **B** — 发动机缸体机械旋转

与发动机缸体关联的机械旋转守恒端口。这是基础端口。发动机缸体是包含活塞气缸的物理本体。

### **F** — 发动机曲轴机械旋转

与发动机曲轴关联的机械旋转守恒端口。这是发动机的从动端口。曲轴传递燃烧过程产生的功率。通常，您将离合器和变速器连接到此端口。

## 参数

### 发动机规格

### **Input type** — 通过归一化节气门或扭矩驱动的选项 `Normalized throttle`（默认）| `Torque command`

模块接收归一化节气门指令还是扭矩指令。这些设置控制端口：

- `Normalized throttle` — 启用物理信号端口 **Thr**，该端口接收介于零和一之间的无量纲节气门指令。
- `Torque command` — 启用物理信号端口 **Trq**，该端口接收介于零和最大扭矩之间的扭矩指令。

### **Model parameterization** — 发动机模型 `Normalized 3rd-order polynomial matched to peak power`（默认）| `Tabulated torque data` | `Tabulated power data`

发动机模型。根据可用数据在以下选项之间选择：

- `Normalized 3rd-order polynomial` — 使用由功率和转速特性定义的功率曲线查找表来参数化发动机。
- `Tabulated torque data` — 使用转速-扭矩表来参数化发动机。
- `Tabulated power data` — 使用转速-功率表来参数化发动机。

### **Engine type** — 要建模的燃烧过程 `Spark-ignition`（默认）| `Diesel` | `Generic`

要建模的内燃过程。您可以基于最大扭矩、最大扭矩时的转速和最大转速来参数化火花点火发动机、柴油发动机或通用发动机。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Maximum torque** — 发动机扭矩输出的物理极限 `380` `N*m`（默认）| 正标量

发动机可输出的峰值扭矩 *TP*。此值设置转速-扭矩曲线的峰值。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Generic`。

### **Speed at maximum torque** — 发动机达到最大功率输出时的曲轴角速度 `4300` `rpm`（默认）| 正标量

发动机产生峰值扭矩时的发动机转速 *ɷPT*。此值设置扭矩曲线上峰值出现的位置。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Generic`。

### **Maximum power** — 发动机功率输出的物理极限 `230` `kW`（默认）| 正标量

发动机可输出的最大功率 *PP*。此值设置转速-功率曲线的峰值。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Spark-ignited` 或 `Diesel`。

### **Speed at maximum power** — 发动机达到最大扭矩输出时的曲轴角速度 `6858` `rpm`（默认）| 正标量

发动机以最大功率运行时的发动机转速 *ɷPP*。此值设置功率曲线上峰值出现的位置。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`，并将 **Engine type** 设置为 `Spark-ignited` 或 `Diesel`。

### **Maximum speed** — 最大曲轴角速度 `7000` `rpm`（默认）| 正标量

发动机可产生扭矩的最大转速 *ɷmax*。此值设置功率曲线的上限。

在仿真期间，如果 *ɷ* 超过此值，仿真将停止并报错。发动机最大转速 *ɷmax* 不能超过发动机功率变为负值时的发动机转速。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Stall speed** — 发动机切断转速 `500` `rpm`（默认）| 正标量

发动机可产生扭矩的最低转速 *ɷmin*。此值设置功率曲线的下限。

在仿真期间，如果 *ɷ* 降至该值以下，发动机扭矩将混合为零。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Stall speed threshold** — 发动机切断阈值 `100` `rpm`（默认）| 正标量

在转速降至 *ɷmin* 以下后，发动机转速过渡到零的阈值转速。使用此参数来调整熄火期间的仿真性能。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial`。

### **Speed vector** — 表列发动机转速数据 `[500, 1000, 2000, 3000, 4300, 5000, 6000, 7000]` `rpm`（默认）| 向量

为模型参数化查找表提供信息的发动机转速向量。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data` 或 `Tabulated power data`。

### **Torque vector** — 表列发动机扭矩数据 `[250, 280, 330, 360, 380, 370, 350, 310]` `N*m`（默认）| 向量

给定转速下的扭矩值向量。此向量的大小必须与 **Speed vector** 参数匹配。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data`。

### **Power vector** — 表列发动机功率数据 `[10, 30, 70, 110, 165, 190, 220, 230]` `kW`（默认）| 向量

给定转速下的功率值向量。此向量的大小必须与 **Speed vector** 参数匹配。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated power data`。

### **Interpolation method** — 中间点计算方法 `Linear`（默认）| `Smooth`

计算中间转速-扭矩值处燃油消耗的方法。超出数据范围时，燃油消耗保持为查找表的最终值不变。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `Tabulated torque data` 或 `Tabulated power data`。

### 动力学

### **Inertia** — 启用惯性建模参数 `No inertia`（默认）| `Specify inertia and initial velocity`

用于参数化惯性和初始速度的选项。您可以选择对惯性建模以提高保真度或数值稳定性。

### **Engine inertia** — 发动机曲轴转动惯量 `1` `kg*m^2`（默认）| 正标量

初始转动惯量。此参数初始化发动机惯性计算。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Initial velocity** — 发动机曲轴角速度 `800` `rpm`（默认）| 正标量

初始角速度。此参数初始化发动机惯性计算。

### **Time constant** — 启用发动机滞后建模参数 `No lag - Suitable for HIL simulation`（默认）| `Specify time constant and initial value`

用于参数化时间常数和初始归一化发动机节气门的选项。

### **Engine time constant** — 发动机滞后值 `0.2` `s`（默认）| 正标量

发动机响应的时间延迟。此参数指定节气门信号与发动机响应之间的滞后。

#### 依赖关系

要启用此参数，请将 **Time constant** 设置为 `Specify time constant and initial value`。

### **Initial normalized throttle** — 发动机初始节气门值 `0`（默认）| [0,1] 范围内的标量

初始归一化发动机节气门。此值必须在 [0,1] 范围内。为此参数指定正值以包含滞后。

#### 依赖关系

要启用此参数，请将 **Time constant** 设置为 `Specify time constant and initial value`。

### 燃油消耗

下表显示了 **Fuel consumption model** 参数的选项如何影响依赖参数的可用性。

**燃油消耗参数依赖关系**

| **Fuel Consumption** | | | | |
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

如果将 **Fuel consumption model** 设置为 `No fuel consumption`，即使将 **FC** 端口连接到另一个模块，模块也不会计算燃油消耗。选择此选项可提高仿真速度。

### **Fuel consumption per revolution** — 常数 `25` `mg/rev`（默认）| 正标量

作为曲轴转数函数的恒定燃油消耗率。输入一个曲轴转数中消耗的燃油体积。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Constant per revolution`。

### **Speed vector** — 发动机转速数据 `[1000, 2000, 3000, 4000, 5000, 6000]`（默认）| 向量

与燃油消耗查找表的 *M* 行对应的发动机扭矩向量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为以下之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

### **Torque vector** — 发动机扭矩数据 `[0, 80, 160, 200, 240, 320, 360, 400]`（默认）| 向量

与燃油消耗查找表的 *N* 列对应的发动机扭矩向量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and torque`。

### **Fuel consumption table** — 发动机燃油消耗数据 *M*×*N* 矩阵（默认）| 矩阵

与发动机转速和扭矩向量对应的燃油消耗值矩阵。行数必须等于 **Speed vector** 参数中的元素数。列数必须等于 **Torque vector** 参数中的元素数。默认值为 `[.5, .9, 1.4, 1.6, 1.9, 2.7, 3.4, 4.4; 1, 1.7, 2.7, 3.1, 3.6, 5, 6, 7.4; 1.4, 2.7, 4, 4.8, 5.6, 7.5, 8.5, 10.5; 2, 3.6, 5.8, 6.7, 8, 10.4, 11.7, 13.3; 2.5, 4.8, 7.9, 9.4, 10.8, 14, 16.2, 18.6; 3.1, 6, 10.3, 11.9, 13.8, 18.4, 22, 26.5]` `g/s`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque`。

### **Brake mean effective pressure vector** — 活塞压力数据 `[0, 250, 500, 625, 750, 1000, 1150, 1250]`（默认）| 向量

制动平均有效压力 (BMEP) 值向量。BMEP 值满足以下表达式：

BMEP=T⋅(2π⋅ncVd)，

其中：

- *T* 是输出扭矩。
- *nc* 是每转的循环数。
- *Vd* 是气缸排量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Brake specific fuel consumption table** — 制动比油耗数据 *M*×*N* 矩阵（默认）| 矩阵

当您将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and torque` 时，此参数是与发动机转速和扭矩向量对应的制动比油耗 (BSFC) 率矩阵。BSFC 是燃油消耗率与输出功率之比。

当您将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure` 时，此参数是与发动机转速和制动平均有效压力 (BMEP) 向量对应的制动比油耗 (BSFC) 率矩阵。BSFC 是燃油消耗率与输出功率之比。

对于这两种燃油消耗模型，行数必须等于 **Speed vector** 参数中的元素数。列数必须等于 **Torque vector** 参数或 **Brake mean effective pressure vector** 参数中的元素数。默认值为 `[410, 380, 300, 280, 270, 290, 320, 380; 410, 370, 290, 270, 260, 270, 285, 320; 415, 380, 290, 275, 265, 270, 270, 300; 420, 390, 310, 290, 285, 280, 280, 285; 430, 410, 340, 320, 310, 300, 310, 320; 450, 430, 370, 340, 330, 330, 350, 380]` `g/(hr*kW)`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Displaced volume** — 单个活塞冲程排出的燃油体积 `400` `cm^3`（默认）| 正标量

活塞冲程燃油排量。这等于圆形活塞气缸横截面积乘以活塞行程距离。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Interpolation method** — 中间步骤行为 `Linear`（默认）| `Smooth`

用于计算中间转速和扭矩值处燃油消耗的插值方法。超出查找表范围时，燃油消耗保持不变。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为以下之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

### **Revolutions per cycle** — 燃烧循环转数 `2`（默认）| `1`

一个燃烧循环中的曲轴转数。对于四冲程发动机输入 `2`，对于二冲程发动机输入 `1`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### 转速控制

### **Idle speed control** — 启用速度控制参数 `Off`（默认）| `On`

启用速度控制的选项。速度控制使发动机在给定设定点怠速运转。
当施加的节气门不足以使发动机转动时，发动机怠速可防止熄火。启用速度控制后，模块会施加足够的节气门以至少维持 **Idle speed reference** 参数值。有关详细信息，请参阅 Idle Speed Controller Model。

### **Idle speed reference** — 稳态怠速 `1000` `rpm`（默认）| 正标量

曲轴的参考角速度。怠速控制器至少维持此速度。

#### 依赖关系

要启用此参数，请选择 **Idle speed control**。

### **Controller time constant** — 怠速控制器响应延迟 `1` `s`（默认）| 正标量

对偏离 **Idle speed reference** 参数值的响应时间。

#### 依赖关系

要启用此参数，请将 **Idle speed control** 设置为 `On`。

### **Controller threshold speed** — 控制器响应平滑度 `1` `rpm`（默认）| 正标量

控制器平滑参数。当发动机转速越过怠速参考值时，**Controller threshold speed** 会平滑受控节气门值。有关详细信息，请参阅 Idle Speed Controller Model。较大的值会降低控制器响应性。较小的值会增加计算成本。此参数必须为正。

#### 依赖关系

要启用此参数，请选择 **Idle speed control**。

### **Redline control** — 启用红线控制参数 `Off`（默认）| `On`

启用发动机曲轴最大角速度限制器的选项。当您将 **Redline control** 设置为 `On` 时，模块会阻止发动机速度超过最大设定点。

### **Redline speed** — 曲轴速度控制峰值阈值 `5000` `rpm`（默认）| 正标量

红线控制发动机速度设定点。输入红线控制激活所依据的速度参考值。

#### 依赖关系

要启用此参数，请选择 **Redline control**。

### **Redline time constant** — 红线控制器响应延迟 `1` `s`（默认）| 正标量

对超过 **Redline speed** 参数值的发动机速度的响应时间。输入与受控节气门增加或减少相关的时间常数值。

#### 依赖关系

要启用此参数，请选择 **Redline control**。

### **Redline threshold speed** — 红线控制器响应平滑度 `1` `rpm`（默认）| 正标量

红线过渡的角速度范围。指定红线速度周围区域的角速度范围，在该区域内控制器从完全启用过渡到未启用。当发动机转速越过红线速度参考值时，模块使用此参数平滑受控节气门值。较大的值会降低控制器响应性。较小的值会增加计算成本。

#### 依赖关系

要启用此参数，请选择 **Redline control**。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

Generic internal combustion engine

Generic Engine 模块表示可配置的内燃机，适用于火花点火和柴油应用。您可以使用扭矩或归一化节气门物理信号来控制该模块。您可以使用三阶多项式，或使用表格化扭矩或功率数据来参数化该模块。可选动态参数包括曲轴惯量和响应时间滞后。物理信号端口 **FC** 根据您选择的燃料消耗模型输出发动机燃料消耗率。可选的速度和红线控制器可防止发动机熄火并启用巡航控制。该图显示了端口与发动机配置的关系。

### Engine Speed, Throttle, Power, and Torque

默认情况下，Generic Engine 模块使用扭矩与速度之间的编程关系，并由节气门信号或扭矩命令信号进行调制。

模块将发动机功率需求评估为发动机速度的函数，*g(ɷ)*。该函数提供给定发动机速度 *ɷ* 下可用的最大功率。模块参数 **Maximum power**、**Speed at maximum power** 和 **Maximum speed** 将该函数归一化为物理最大扭矩和速度值。

归一化节气门信号 *Thr* 控制发动机功率，使得 *P(**ɷ**,Thr)* = *Thr*·*g(**ɷ**)*。当您将 **Model parameterization** 设置为 `Normalized throttle` 时，物理输入信号 **Thr** 控制发动机功率。当您选择 `Torque command` 时，模块会在内部计算归一化节气门。模块以固定发动机速度下稳态可能最大功率的分数形式提供功率。该图显示了默认设置下的扭矩和功率曲线。

发动机扭矩曲线为实线蓝色。发动机功率曲线为虚线橙色。

请注意，瞬态期间端口 **F** 处可用的扭矩可能与记录变量 `trq` 的值不同。记录变量跟踪产生的扭矩，并且不考虑因系统惯量损失的扭矩。

### Polynomial Engine Control

当您将 **Model parameterization** 设置为 `Normalized 3rd-order polynomial` 时，模块使用归一化发动机速度 *ɷN* 来计算速度和扭矩。模块将归一化发动机速度定义为

ωN(ω)≡ωωPP

其中：

- *ɷ* 是当前发动机速度。
- *ɷPP* 是峰值功率处的发动机速度。

模块将归一化、无量纲发动机功率视为三阶多项式，使得

P(ω(ωN))=PP⋅pN(ωN)pN(ωN)=s1ωN+s2ωN2+s3ωN3

其中 *s1*、*s2* 和 *s3* 是常数多项式系数，*Pp* 是峰值功率。在典型发动机中，*si* 系数为正。

模块使用多项式系数计算节气门全开条件下的发动机扭矩，使得

T(ω(ωN))=p1+p2ωN+p3ωN2p1≡s1Pp/ωppp2≡s2Pp/ωppp3≡s3Pp/ωpp

模块将峰值功率处的归一化发动机速度设置为

ωNPP=ωN(ωNPP)=1.

将此等式代入 *pN* 的公式可得

s1+s2+s3=1.

此条件将功率归一化到峰值功率处的发动机速度。模块将 *pN(ɷPP)* 的斜率设置为零，使得

s1+2s2+3s3=0.

模块将峰值扭矩处的归一化发动机速度定义为

ωNPT=ωN(ωPT)=ωPTωPP<1

其中峰值功率速度大于峰值扭矩速度。模块使用多项式公式求无量纲、归一化扭矩 *τN*，并将斜率设置为零，使得

dτN(ωNPT)dω=s2+2s3ωNPT=0.

使用这些方程求解 *si* 可得

s1=3−4ωNPT2(1−ωNPT)s2=−ωNPTωNPT−1s3=12(ωNPT−1)

模块计算发动机扭矩为

T(ω(ωN))=2TP3−ωNPT(s1+s2ωN+s3ωN2),

其中 *TP* 是峰值扭矩。代入 *ɷNPT* 的方程可得约束

2TPωPP2−3PPωPP+PPωPT=0.

模块使用 *TP*、*PP* 和 *ɷPT* 计算峰值功率处的发动机速度，使得

ωPP=3PP+PP(9PP−8TPωPT)4TP>ωPT.

其中 *TPɷPT* 等效于峰值扭矩处的功率 *PPT*，其始终小于峰值功率 *PP*。

**Engine Power Forms for Different Engine Types**

模块使用与 **Engine type** 参数设置对应的系数来计算多项式。当您将 **Engine type** 设置为 `Spark-ignition` 或 `Diesel` 时，模块会从表中选择适当的系数。当您选择 `Generic` 时，模块会在内部计算这些系数。

| Power Demand Coefficient | Engine Type | |
| --- | --- | --- |
| Spark-Ignition | Diesel |
| *s1* | 1 | 0.6526 |
| *s2* | 1 | 1.6948 |
| *s 3* | -1 | -1.3474 |

### Fuel Consumption

模块可以选择性地对燃料消耗建模，并将结果作为物理信号在端口 **FC** 输出。要在仿真中包含燃料消耗，请将 **Fuel consumption model** 设置为以下设置之一：

- `Constant per revolution`
- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

您可以创建燃料消耗的可视化表示。当您将 **Fuel consumption model** 设置为 `Fuel consumption by speed and torque`，并单击模块描述中的 **engine properties** 超链接时，实时脚本会生成给定扭矩和速度下燃料消耗的热图。

给定扭矩和速度下燃料消耗的热图。

此图是对发动机速度、节气门、功率和扭矩图的补充。当您将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure` 时，实时脚本会生成燃料消耗热图以及单独的制动比燃料消耗图。

给定扭矩和速度下燃料消耗的热图，以及给定扭矩和速度下制动比燃料消耗的热图。

### Idle Speed Controller Model

怠速控制器调整节气门信号，以根据以下公式在低于参考速度时增加发动机转速：

Π=max(Πi,Πc)

以及

d(Πc)dt=0.5⋅(1−tanh(4⋅ω−ωrωt))−Πcτ

其中：

- *Π* 是发动机节气门。
- *Πi* 是输入节气门端口 **Thr**。
- *Πc* 是控制器节气门。
- *ω* 是发动机速度或曲轴角速度。
- *ωr* 是怠速速度参考。
- *ωt* 是控制器速度阈值。
- *τ* 是控制器时间常数。

当发动机速度低于参考速度时，受控节气门以一阶滞后从 0 增加到 1。当发动机速度高于参考速度时，受控节气门从 1 减少到 0。当发动机速度与参考速度之差小于控制器速度阈值时，方程中的 *tanh* 部分会平滑受控节气门的时间导数。平滑函数将受控节气门限制在范围 [0,1] 内。发动机使用输入节气门值和受控节气门值中的较大者。如果您包含发动机时间滞后，控制器会在计算滞后之前更改输入。

### Redline Controller Model

怠速控制器确定用于维持发动机速度的最小节气门值，红线控制器基于最大节气门输入防止速度过高。为了确定最大节气门值，红线控制器使用怠速控制器模型方程。但是，对于红线控制器：

- *ωr* 是红线速度参考。
- *ωt* 是红线速度阈值。
- *τ* 是红线时间常数。

### Performance

要提高仿真速度，请将 **Fuel consumption model** 设置为 `No fuel consumption`。使用此设置时，无论端口 **FC** 如何，模块都不会计算燃料消耗。

如果您为 **Fuel consumption model** 选择任何其他选项，模块必须执行非线性计算。即使报告燃料消耗率的 **FC** 端口未连接到另一个模块，模块也会求解该方程。

### Predefined Parameterization

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的“<click to select>”超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件，并在 **Compare selected part with block** 部分查看数据，将当前参数设置与特定供应商组件进行比较。

**Note**

预定义模块参数化使用可用数据源提供参数值。模块会用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

### 假设和限制

发动机对速度和节气门变化的响应存在滞后。模块仅支持由节气门变化引起的滞后。

### 硬件在环仿真

要提高 HIL 仿真的性能，请将 **Dynamics** > **Time Constant** 参数设置为 `No time constant - Suitable for HIL simulation`。
