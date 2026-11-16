---
type: simulink-block
title: 'Positive-Displacement Compressor (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Turbomachinery'
documentation_page: 'positivedisplacementcompressorma'
documentation_source_path: 'ref/positivedisplacementcompressorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Positive-Displacement Compressor (MA)

## 端口

### 守恒

### **A** — 压缩机入口湿空气

与压缩机入口关联的湿空气守恒端口。

### **B** — 压缩机出口湿空气

与压缩机出口关联的湿空气守恒端口。

### **C** — 压缩机壳体机械旋转

与压缩机壳体关联的机械旋转守恒端口。

### **R** — 压缩机轴机械旋转

与压缩机轴关联的机械旋转守恒端口。

## 参数

### 排量

### **排量规格** — 用于按体积或标称条件指定排量的选项 `Volumetric displacement` (默认) | `Nominal mass flow rate and shaft speed`

是否根据每循环体积或标称条件值指定流体排量。

### **排量体积** — 排量体积 `130` `cm^3/rev` (默认) | 正标量

每循环排出的流体体积。该模块将一个循环定义为一次压缩冲程和一次膨胀冲程，它们发生在单次曲轴旋转期间。该体积是最大气缸体积与余隙容积之差，(*Va* — *Vc*)。通常，排量体积是压缩机在一转轴旋转中扫过的体积。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Volumetric displacement`。

### **标称质量流量** — 标称质量流量 `0.01` `kg/s` (默认) | 正标量

该模块用于求取排量体积的标称质量流量。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`。

### **标称轴转速** — 标称轴转速 `1000` `rpm` (默认) | 正标量

该模块用于求取排量体积的标称轴转速。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`。

### 效率

该表显示了 **热力学模型** 和 **效率规格** 参数的选项如何影响相关效率参数的可用性。

| **热力学模型** | | | |
| --- | --- | --- | --- |
| `Polytropic` | | `Isentropic` | |
| **效率规格** | | **效率规格** | |
| `Analytical` | `Tabulated` | `Analytical` | `Tabulated` |
| **多方指数** | **多方指数** | **等熵效率** | **等熵效率表, eta\_isen(pr,w)** |
| **标称容积效率** | **压力比向量, pr** | **标称容积效率** | **压力比向量, pr** |
| **轴转速向量, w** | **轴转速向量, w** |
| **容积效率表, eta\_vol(pr,w)** | **容积效率表, eta\_vol(pr,w)** |

### **效率规格** — 用于通过解析方式或表格参数化容积效率的选项 `Analytical` (默认) | `Tabulated`

是否通过解析方程或表格数据参数化排量容积效率。

### **热力学模型** — 热力学模型参数化选项 `Polytropic` (默认) | `Isentropic`

是否使用多方或等熵热力学模型。

### **多方指数** — 多方指数 `1.2` (默认) | 正标量

该模块在实现多方压力-体积关系时使用的指数。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Polytropic`。

### **等熵效率** — 等熵效率 `0.65` (默认) | 正标量

该模块在实现解析等熵压力-体积关系时使用的恒定效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic`，并将 **效率规格** 设置为 `Analytical`。

### **等熵效率表, eta\_isen(pr,w)** — 等熵效率表 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]` (默认) | 矩阵

该模块在实现表格化等熵压力-体积关系时使用的效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic`，并将 **效率规格** 设置为 `Tabulated`。

### **标称容积效率** — 标称容积效率 `0.95` (默认) | 正标量

用于计算余隙容积分数的标称容积效率。标称容积效率是压缩机在标称条件下运行时的容积效率。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Analytical`。

### **压力比向量, pr** — 压力比向量 `[2, 4, 6, 8]` (默认) | 向量

对应于压缩机容积效率的压力比向量。每个元素对应 **容积效率表, eta\_vol(pr,w)** 参数的一行。此参数必须为大小为 `N` 的向量，其中 `N` 是 **容积效率表, eta\_vol(pr,w)** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### **轴转速向量, w** — 轴转速向量 `[800, 1500, 2800, 3300, 4000]` `rpm` (默认) | 向量

对应于压缩机容积效率的轴转速向量。每个元素对应 **容积效率表, eta\_vol(pr,w)** 参数的一列。此参数必须为大小为 `M` 的向量，其中 `M` 是 **容积效率表, eta\_vol(pr,w)** 参数的宽度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### **容积效率表, eta\_vol(pr,w)** — 容积效率 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]` (默认) | 矩阵

给定轴转速和压力比下的容积效率。此参数必须为大小为 `N` 乘 `M` 的矩阵，其中 `N` 是 **压力比向量, pr** 参数的长度，`M` 是 **轴转速向量, w** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### 标称条件

该表显示了 **排量规格**、**热力学模型** 和 **效率规格** 参数的选项如何影响相关标称条件参数的可用性。

此表显示了当您将 **排量规格** 参数设置为 `Volumetric displacement` 时的相关参数：

| 当 **排量规格** 参数为 `Volumetric displacement` 时 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **效率规格** | | | | | | | |
| `Analytical` | | | | `Tabulated` | | | |
| **热力学模型** | | | | **热力学模型** | | | |
| `Polytropic` | | `Isentropic` | | `Polytropic` | | `Isentropic` | |
| **标称压力比** | | **标称压力比** | |  | | **标称压力比** | |
| **标称入口压力** | | **标称入口压力** | |
| **标称入口温度** | | **标称入口温度** | |
| 标称入口湿度、水滴和痕量气体参数 | | 标称入口湿度、水滴和痕量气体参数 | |

当您将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed` 时，**标称条件** 中的参数不依赖于 **效率规格** 或 **热力学模型** 参数。

### **标称压力比** — 标称压力比 `5` (默认) | 正标量

该模块用于计算余隙容积分数的标称压力比。

#### 依赖关系

要启用此参数，请选择任意参数化，但 **排量规格** 为 `Volumetric displacement`、**热力学模型** 为 `Polytropic` 且 **效率规格** 为 `Tabulated` 时除外。

### **标称入口压力** — 标称入口压力 `0.101325` `MPa` (默认) | 正标量

该模块用于求取排量体积的标称入口压力。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **标称入口温度** — 标称入口温度 `293.15` `K` (默认) | 正标量

该模块用于求取排量体积的标称入口温度。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **入口湿度规格** — 用于描述入口湿度水平的量 `Relative humidity` (默认) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述入口湿空气湿度水平。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **标称入口相对湿度** — 入口相对湿度 `0.5` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处的湿空气相对湿度。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口湿度规格** 为 `Relative humidity`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口湿度规格** 为 `Relative humidity`。

### **标称入口比湿度** — 入口比湿度 `0.01` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处的湿空气比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口湿度规格** 为 `Specific humidity`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口湿度规格** 为 `Specific humidity`。

### **标称入口水蒸气摩尔分数** — 入口水蒸气摩尔分数 `0.01` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口湿度规格** 为 `Mole fraction`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口湿度规格** 为 `Mole fraction`。

### **标称入口湿度比** — 入口湿度比 `0.01` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处的湿空气湿度比，定义为水蒸气与干空气和痕量气体的质量比。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口湿度规格** 为 `Humidity ratio`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口湿度规格** 为 `Humidity ratio`。

### **标称入口湿球温度** — 入口湿球温度 `287` `K` (默认) | 正标量

标称运行条件下入口处湿空气混合物的湿球温度。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口湿度规格** 为 `Wet-bulb temperature`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口湿度规格** 为 `Wet-bulb temperature`。

### **入口痕量气体规格** — 用于描述入口痕量气体水平的量 `Mass fraction` (默认) | `Mole fraction`

是否使用质量分数或摩尔分数描述入口处的痕量气体水平。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **标称入口痕量气体质量分数** — 入口痕量气体质量分数 `0.001` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处湿空气混合物中痕量气体的质量分数。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口痕量气体规格** 为 `Mass fraction`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口痕量气体规格** 为 `Mass fraction`。

### **标称入口痕量气体摩尔分数** — 仿真开始时痕量气体的摩尔分数 `0.001` (默认) | 范围 [0,1] 内的标量

标称运行条件下入口处湿空气混合物中痕量气体的摩尔分数。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **排量规格** 为 `Nominal mass flow rate and shaft speed`，并且 **入口痕量气体规格** 为 `Mole fraction`。
- **排量规格** 为 `Volumetric displacement`，**热力学模型** 为 `Isentropic`，并且 **入口痕量气体规格** 为 `Mole fraction`。

### **标称入口水滴与湿空气的质量比** — 水滴与湿空气的比 `0` (默认) | 正标量

标称运行条件下入口处水滴与湿空气的质量比。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **饱和时的相对湿度** — 发生冷凝时高于该值的相对湿度 `1` (默认) | 正标量

压缩机中发生冷凝时高于该值的相对湿度。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或者将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### 参数

### **机械效率** — 压缩机机械效率 `0.9` (默认) | 正标量

流体功率与机械轴功率之比。

### **模拟水滴蒸发** — 用于模拟水滴蒸发的选项 `off` (默认) | `on`

用于模拟由于压缩机中温度变化而引起的水滴蒸发的选项。

### **饱和时的相对湿度** — 发生冷凝时高于该值的相对湿度 `1` (默认) | 正标量

压缩机中发生冷凝时高于该值的相对湿度。

### **端口 A 处的入口面积** — 入口面积 `0.01` `m^2` (默认) | 正标量

与端口 **A** 关联的入口面积。

### **Outlet area at port B** — Outlet area `0.01` `m^2` (默认) | 正标量

与端口 **B** 关联的出口面积。

## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：对水滴蒸发建模

通过使用 **Model water droplets evaporation** 参数，对由温度变化引起的水滴蒸发建模。

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的容积式压缩机

Positive-Displacement Compressor (MA) 模块表示湿空气网络中的容积式压缩机，例如往复活塞式、旋转螺杆式、旋转叶片式或涡旋式。端口 **R** 和端口 **C** 分别是与压缩机轴和壳体关联的机械旋转守恒端口。当端口 **R** 相对于端口 **C** 存在正向旋转时，湿空气从端口 **A** 流向端口 **B**。对于反向流动，该模块可能不准确。

该图显示活塞压缩机在 P-V 图上的步骤，其具有以下状态：

- *a* — 压缩机气缸在入口压力下充满。
- *b* — 压缩机内部压力超过出口压力，从而导致流体排出。
- *c* — 压缩机达到活塞行程顶部，气缸中仅剩余隙容积。
- *d* — 气缸内压力降至入口压力以下，从而导致流体吸入。

图示活塞压缩机过程，其中点 A 处于低压、高容积，点 B 处于高压、高容积，端口 C 处于高压、低容积，点 d 处于低压、低容积。

### 质量流量

该模块按如下公式计算质量流量：

m˙=ηVωVdispvs,

其中：

- *ṁ* 是质量流量。
- *ω* 是端口 **R** 相对于端口 **C** 的角速度。
- *vs* 是入口处的比容。该模块根据标称入口条件计算此值。
- *Vdisp* 是该模块使用的排量体积。

### 排量体积

当您将 **Displacement specification** 设置为 `Volumetric displacement` 时，该模块使用 **Displacement volume** 参数作为 *Vdisp* 的值。

当您将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed` 时，该模块按如下公式计算排量体积：

Vdisp=m˙nominalvs,nominalωnominalηVnominal,

其中：

- *ṁnominal* 是 **Nominal mass flow rate** 参数的值。
- *ωnominal* 是 **Nominal shaft speed** 参数的值。
- 当 **Efficiency specification** 参数为 `Analytical` 时，*ηVnominal* 是 **Nominal volumetric efficiency** 参数的值。当 **Volumetric efficiency** 参数为 `Tabulated` 时，该模块使用 `tablelookup` 函数将 *ηVnominal* 插值为轴转速和压力比的函数。

### 容积效率

您可以使用解析值或查找表来参数化容积效率。

**解析容积效率**

当您将 **Efficiency specification** 设置为 `Analytical` 时，该模块使用解析值计算容积效率。当 **Thermodynamic model** 参数为 `Polytropic` 时，容积效率为

ηV=1+C−C(poutpin)1n,

其中 *pin* 和 *pout* 分别是入口压力和出口压力，*n* 是 **Polytropic exponent** 参数的值。该模块按如下公式计算余隙容积分数 *C*：

C=1−ηVnominalpratio1/n−1,

其中 *ηVnominal* 是 **Nominal volumetric efficiency** 参数的值，*pratio* 是 **Nominal pressure ratio** 参数的值。

当 **Thermodynamic model** 参数为 `Isentropic` 时，容积效率为

ηV=1+C−C(vinvout),

其中 *vin* 和 *vout* 分别是入口比容和出口比容。该模块按如下公式计算余隙容积分数 *C*：

C=1-ηVnominalvrnominal-1

其中 vrnominal=vinnominal/voutnominal 是标称比容比。该模块根据标称入口条件和等熵效率计算此值。

**表格化容积效率**

当您将 **Efficiency specification** 设置为 `Tabulated` 时，该模块通过将 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的值插值为轴转速和压力比的函数，来计算容积效率。

### 质量守恒

当您清除 **Model water droplets evaporation** 参数时，该模块按如下方式守恒质量：

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中：

- m˙*B* 是端口 **B** 处的混合物质量流量。
- m˙*wA* 和 m˙*wB* 分别是端口 **A** 和 **B** 处的水蒸气质量流量。
- m˙*gA* 和 m˙*gB* 分别是端口 **A** 和 **B** 处的痕量气体质量流量。
- m˙*dA* 和 m˙*dB* 分别是端口 **A** 和 **B** 处的水滴质量流量。

如果您选择 **Model water droplets evaporation**，质量平衡方程为

m˙A+m˙B+m˙devap=0m˙wA+m˙wB−m˙devap=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙devap=0

蒸发水滴的质量流量 m˙*devap* 为

m˙devap=max{m˙A,0}rdevap.

*rdevap* 是可以蒸发的水滴质量比，

rdevap=min{rdA,xwcapacity},

其取决于 *rdA*，即端口 **A** 处水滴与湿空气的质量比。

湿空气容纳更多水蒸气的能力为

xwcapacity=max{xwsB−xwA,0},

其中 *xwsB* 是饱和比湿，*xwA* 是比湿。

### 能量守恒

该模块按如下方式守恒能量：

ϕA+ϕB+m˙AΔht=0,

其中 *Δht* 是比总焓变化，*ṁAΔht* 是流体功率，其等于机械功率 *torque\*ω*。

当 **Thermodynamic model** 参数为 `Polytropic` 时，流体功率为

W˙c=ωnn−1ηVpinVdisp[(pinpout)n−1n−1],

其中该模块使用多变关系 pvn=constant 来关联 *pin*、*pout*、*vin* 和 *vout*。

当 **Thermodynamic model** 参数为 `Isentropic` 时，流体功率为

W˙C=m˙AΔht.

该模块根据等熵效率 *ηisen* 计算 *Δht*。当 **Efficiency specification** 参数为 `Analytical` 时，*ηisen* 等于 **Isentropic efficiency** 参数的值。当 **Efficiency specification** 参数为 `Tabulated` 时，该模块通过将 **Isentropic efficiency table, eta\_isen(pr,w)** 参数的值插值为压力比和轴转速的函数，来计算 *ηisen*。

### 可视化容积效率

要可视化模块容积效率，请右键单击该模块，然后选择 **Fluids** > **Plot Volumetric Efficiency**。

每次修改模块设置后，请在图形窗口中点击 **Reload Data**。

当您将 **Efficiency specification** 设置为 `Analytical`，并将 **Thermodynamic model** 设置为 `Polytropic` 时，该模块绘制压缩机容积效率随压力比变化的曲线。

容积效率

当您将 **Efficiency specification** 设置为 `Analytical`，并将 **Thermodynamic model** 设置为 `Isentropic` 时，该模块绘制在 *Tout nom*（标称出口温度）下压缩机容积效率随压力比变化的曲线。

容积效率

当您将 **Efficiency specification** 设置为 `Tabulated` 时，该模块针对 **Shaft speed vector, w** 参数中的每个元素，绘制压缩机容积效率随压力比变化的曲线。

容积效率

### 假设和限制

- 对于从端口 **B** 到端口 **A** 的流动，该模块可能不准确。
- 该模块假设流动为准稳态。压缩机不累积质量。
