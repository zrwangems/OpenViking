---
type: simulink-block
title: 'Positive-Displacement Compressor (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Fluid Machines'
documentation_page: 'positivedisplacementcompressor2p'
documentation_source_path: 'ref/positivedisplacementcompressor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Positive-Displacement Compressor (2P)

## 端口

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

### 排量

### **排量指定** — 用于按体积或标称条件指定排量的选项 `Volumetric displacement`（默认） | `Nominal mass flow rate and shaft speed`

是否根据每循环体积或标称条件值指定流体排量。

### **排量体积** — 排量体积 `130` `cm^3/rev`（默认） | 正标量

每循环排出的流体体积。该模块将一个循环定义为一个压缩冲程和一个膨胀冲程，它们发生在单次曲轴旋转期间。此体积是最大气缸体积与余隙体积之差，(*Va* — *Vc*)。通常，排量体积是压缩机在一转轴旋转中扫出的体积。

#### 依赖关系

要启用此参数，请将 **排量指定** 设置为 `Volumetric displacement`。

### **标称质量流量** — 标称质量流量 `0.01` `kg/s`（默认） | 正标量

模块用来计算排量体积的标称质量流量。

#### 依赖关系

要启用此参数，请将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。

### **标称轴转速** — 标称轴转速 `1000` `rpm`（默认） | 正标量

模块用来计算排量体积的标称轴转速。

#### 依赖关系

要启用此参数，请将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。

### 效率

下表显示 **热力学模型** 和 **效率指定** 参数的选项如何影响依赖效率参数的可用性。

| **热力学模型** | | | |
| --- | --- | --- | --- |
| `Polytropic` | | `Isentropic` | |
| **效率指定** | | **效率指定** | |
| `Analytical` | `Tabulated` | `Analytical` | `Tabulated` |
| **多变指数** | **多变指数** | **等熵效率** | **等熵效率表, eta\_isen(pr,w)** |
| **标称容积效率** | **压力比向量, pr** | **标称容积效率** | **压力比向量, pr** |
| **轴转速向量, w** | **轴转速向量, w** |
| **容积效率表, eta\_vol(pr,w)** | **容积效率表, eta\_vol(pr,w)** |

### **效率指定** — 用于解析地或通过表格参数化容积效率的选项 `Analytical`（默认） | `Tabulated`

是否使用解析方程或表格数据来参数化排量容积效率。

### **热力学模型** — 热力学模型参数化选项 `Polytropic`（默认） | `Isentropic`

是否使用多变或等熵热力学模型。

### **多变指数** — 多变指数 `1.2`（默认） | 正标量

模块在实现多变压力-体积关系时使用的指数。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Polytropic`。

### **等熵效率** — 等熵效率 `0.65`（默认） | 正标量

模块在实现解析等熵压力-体积关系时使用的恒定效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic`，并将 **效率指定** 设置为 `Analytical`。

### **等熵效率表, eta\_isen(pr,w)** — 等熵效率表 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认） | 矩阵

模块在实现表格化等熵压力-体积关系时使用的效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic`，并将 **效率指定** 设置为 `Tabulated`。

### **标称容积效率** — 标称容积效率 `0.95`（默认） | 正标量

用于计算余隙体积分数的标称容积效率。标称容积效率是压缩机在标称条件下运行时的容积效率。

#### 依赖关系

要启用此参数，请将 **效率指定** 设置为 `Analytical`。

### **压力比向量, pr** — 压力比向量 `[2, 4, 6, 8]`（默认） | 向量

与压缩机容积效率对应的压力比向量。每个元素对应于 **容积效率表, eta\_vol(pr,w)** 参数的一行。此参数必须为大小为 `N` 的向量，其中 `N` 是 **容积效率表, eta\_vol(pr,w)** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率指定** 设置为 `Tabulated`。

### **轴转速向量, w** — 轴转速向量 `[800, 1500, 2800, 3300, 4000]` `rpm`（默认） | 向量

与压缩机容积效率对应的轴转速向量。每个元素对应于 **容积效率表, eta\_vol(pr,w)** 参数的一列。此参数必须为大小为 `M` 的向量，其中 `M` 是 **容积效率表, eta\_vol(pr,w)** 参数的宽度。

#### 依赖关系

要启用此参数，请将 **效率指定** 设置为 `Tabulated`。

### **容积效率表, eta\_vol(pr,w)** — 容积效率 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认） | 矩阵

给定轴转速和压力比下的容积效率。此参数必须为大小 `N` 乘 `M` 的矩阵，其中 `N` 是 **压力比向量, pr** 参数的长度，`M` 是 **轴转速向量, w** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率指定** 设置为 `Tabulated`。

### 标称条件

这些表显示 **排量指定**、**热力学模型**、**效率指定** 和 **标称条件指定** 参数的选项如何影响依赖标称条件参数的可用性。

下表显示当您将 **排量指定** 参数设置为 `Volumetric displacement` 时的依赖参数：

| 当 **排量指定** 参数为 `Volumetric displacement` 时 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **效率指定** | | | | | | | |
| `Analytical` | | | | `Tabulated` | | | |
| **热力学模型** | | | | **热力学模型** | | | |
| `Polytropic` | | `Isentropic` | | `Polytropic` | | `Isentropic` | |
| **标称条件指定** | | **标称条件指定** | |  | | **标称条件指定** | |
| `Nominal pressure` | `Nominal saturation temperatures` | `Nominal pressure` | `Nominal saturation temperatures` | `Nominal pressure` | `Nominal saturation temperatures` |
| **标称压力比** | **标称蒸发温度** | **标称压力比** | **标称蒸发温度** | **标称压力比** | **标称蒸发温度** |
| **标称冷凝温度** | **标称入口压力** | **标称冷凝温度** | **标称入口压力** | **标称冷凝温度** |
| **标称入口温度** | **标称蒸发器过热度** | **标称入口温度** |

当您将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed` 时，**标称条件** 中的参数仅取决于 **标称条件指定** 参数：

| 当 **排量指定** 参数为 `Nominal mass flow rate and shaft speed` 时 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **标称条件指定** | | | | | | | |
| `Nominal pressure` | | | | `Nominal saturation temperatures` | | | |
| **标称压力比** | | | | **标称蒸发温度** | | | |
| **标称入口压力** | | | | **标称冷凝温度** | | | |
| **标称入口温度** | | | | **标称蒸发器过热度** | | | |

### **标称压力比** — 标称压力比 `5`（默认） | 正标量

用于计算余隙体积分数的标称压力比。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal pressure`，并且：

- 将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。
- 将 **排量指定** 设置为 `Volumetric displacement`，并将 **热力学模型** 设置为 `Isentropic`。
- 将 **排量指定** 设置为 `Volumetric displacement`，将 **热力学模型** 设置为 `Polytropic`，并将 **效率指定** 设置为 `Analytical`。

### **标称条件指定** — 用于指定压力比或制冷循环饱和温度的选项 `Nominal pressure`（默认） | `Nominal saturation temperatures`

是否使用标称出口-入口压力比或标称蒸发和冷凝温度来指定决定排量体积的标称条件。

#### 依赖关系

要启用此参数，请选择任何参数化，但以下情况除外：**排量指定** 为 `Volumetric displacement`、**热力学模型** 为 `Polytropic` 且 **效率指定** 为 `Tabulated`。

### **标称入口压力** — 标称入口压力 `0.101325` `MPa`（默认） | 正标量

模块用来计算排量体积的标称入口压力。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal pressure`，并且满足以下任一条件：

- 将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。
- 将 **排量指定** 设置为 `Volumetric displacement`，并将 **热力学模型** 设置为 `Isentropic`。

### **标称入口温度** — 标称入口温度 `373.15` `K`（默认） | 正标量

模块用来计算排量体积的标称入口温度。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal pressure`，并且满足以下任一条件：

- 将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。
- 将 **排量指定** 设置为 `Volumetric displacement`，并将 **热力学模型** 设置为 `Isentropic`。

### **标称蒸发温度** — 标称蒸发温度 `373.15` `K`（默认） | 正标量

模块用来计算排量体积的标称蒸发温度。此值是蒸发器中的饱和温度。模块假定标称压缩机入口压力是对应于此饱和温度的压力。

蒸发温度也称为饱和吸气温度 (SST)。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal saturation temperature`，并选择任何其他参数选项，但以下情况除外：**排量指定** 为 `Volumetric displacement`、**热力学模型** 为 `Polytropic` 且 **效率指定** 为 `Tabulated`。

### **标称冷凝温度** — 标称冷凝温度 `398.15` `K`（默认） | 正标量

模块用来计算排量体积的标称冷凝温度。此值是冷凝器中的饱和温度。模块假定标称压缩机出口压力是对应于此饱和温度的压力。

冷凝温度也称为饱和排气温度 (SDT)。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal saturation temperature`，并选择任何其他参数选项，但以下情况除外：**排量指定** 为 `Volumetric displacement`、**热力学模型** 为 `Polytropic` 且 **效率指定** 为 `Tabulated`。

### **标称蒸发器过热度** — 标称饱和超额温度 `10` `deltaK`（默认） | 标量

蒸发器出口处超过饱和点的标称超额温度，模块假定该出口连接到压缩机入口。

#### 依赖关系

要启用此参数，请将 **标称条件指定** 设置为 `Nominal saturation temperature`，并且满足以下任一条件：

- 将 **排量指定** 设置为 `Nominal mass flow rate and shaft speed`。
- 将 **排量指定** 设置为 `Volumetric displacement`，将 **热力学模型** 设置为 `Isentropic`，并将 **效率指定** 设置为 `Analytical`。

### 参数

### **机械效率** — 压缩机机械效率 `0.9`（默认） | 正标量

流体功率与机械轴功率之比。

### **端口 A 处的入口面积** — 入口面积 `0.01` `m^2`（默认） | 正标量

与端口 **A** 关联的入口面积。

### **端口 B 处的出口面积** — 出口面积 `0.01` `m^2`（默认） | 正标量

与端口 **B** 关联的出口面积。

### **流体未完全汽化时报告** — 两相流体条件检查 `Warning`（默认） | `None` | `Error`

当端口 **A** 处的流体不满足蒸汽条件时要执行的操作。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b：对多变或等熵过程建模

现在，您可以使用 Positive-Displacement Compressor (2P) 模块将正排量过程建模为多变或等熵过程。以前，该模块假定为多变过程。使用新的 **热力学模型** 参数选择效率模型。

## 描述

两相流体网络中的正排量压缩机

Positive-Displacement Compressor (2P) 模块表示两相流体网络中的正排量压缩机，例如往复活塞式、旋转螺杆式、旋转叶片式或涡旋式压缩机。端口 **R** 和端口 **C** 分别是与压缩机轴和壳体关联的机械旋转守恒端口。当端口 **R** 相对于端口 **C** 存在正旋转时，两相流体从端口 **A** 流向端口 **B**。该模块对于反向流动可能不准确。

图示显示了正排量压缩机在 P-V 图上的步骤，其具有以下状态：

- *a* — 压缩机气缸在入口压力下充满。
- *b* — 压缩机内部压力超过出口压力，从而导致流体排出。
- *c* — 压缩机到达活塞冲程顶部，气缸中仅剩余余隙体积。
- *d* — 气缸内部压力降至入口压力以下，从而导致流体吸入。

  图示显示活塞压缩机过程，其中点 A 处于低压、高体积，点 B 处于高压、高体积，端口 C 处于高压、低体积，点 d 处于低压、低体积。

### 质量流量

该模块按以下公式计算质量流量

m˙=ηVωVdispvs,

其中：

- *ṁ* 是质量流量。
- *ω* 是端口 **R** 相对于端口 **C** 的角速度。
- *vs* 是入口处的比体积。该模块基于 **Nominal conditions specification** 参数和指定的标称入口条件计算此值。
- *Vdisp* 是该模块使用的排量。

### 排量

当您将 **Displacement specification** 设置为 `Volumetric displacement` 时，该模块使用 **Displacement volume** 参数作为 *Vdisp* 的值。

当您将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed` 时，该模块按以下公式计算排量

Vdisp=m˙nominalvs,nominalωnominalηVnominal,

其中：

- *ṁnominal* 是 **Nominal mass flow rate** 参数的值。
- *ωnominal* 是 **Nominal shaft speed** 参数的值。
- *ηVnominal* 是当 **Efficiency specification** 参数为 `Analytical` 时 **Nominal volumetric efficiency** 参数的值。当 **Efficiency specification** 参数为 `Tabulated` 时，该模块使用 `tablelookup` 函数将 *ηVnominal* 插值为轴转速和压力比的函数。

### 容积效率

您可使用解析值或查找表来参数化容积效率。

**解析容积效率**

当您将 **Efficiency specification** 设置为 `Analytical` 时，该模块使用解析值计算容积效率。当 **Thermodynamic model** 参数为 `Polytropic` 时，容积效率为

ηV=1+C−C(poutpin)1n,

其中 *pin* 和 *pout* 分别是入口压力和出口压力，*n* 是 **Polytropic exponent** 参数的值。该模块按以下公式计算余隙容积分数 *C*：

C=1−ηVnominalpratio1/n−1,

其中 *ηVnominal* 是 **Nominal volumetric efficiency** 参数的值，*pratio* 是 **Nominal pressure ratio** 参数的值。

当 **Thermodynamic model** 参数为 `Isentropic` 时，容积效率为

ηV=1+C−C(vinvout),

其中 *vin* 和 *vout* 分别是入口和出口比体积。该模块按以下公式计算余隙容积分数 *C*：

C=1-ηVnominalvrnominal-1

其中 vrnominal=vinnominal/voutnominal 是标称比体积比。该模块根据 **Nominal conditions specification** 参数的选择，从标称入口条件和等熵效率计算此值。

**表格化容积效率**

当您将 **Efficiency specification** 设置为 `Tabulated` 时，该模块通过将 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的值插值为轴转速和压力比的函数来计算容积效率。

### 连续性方程

该模块按如下方式守恒质量

m˙A+m˙B=0,

其中 *ṁA* 和 *ṁB* 分别是端口 **A** 和 **B** 处的质量流量。该模块按如下方式守恒能量

ϕA+ϕB+m˙AΔht=0,

其中 *Δht* 是比总焓的变化，*ṁAΔht* 是流体功率，其等于机械功率，*torque\*ω*。

当 **Thermodynamic model** 参数为 `Polytropic` 时，流体功率为

W˙c=ωnn−1ηVpinVdisp[(pinpout)n−1n−1],

其中该模块使用多变关系 pvn=constant 来关联 *pin*、*pout*、*vin* 和 *vout*。

当 **Thermodynamic model** 参数为 `Isentropic` 时，流体功率为

W˙C=m˙AΔht.

该模块根据等熵效率 *ηisen* 计算 *Δht*。当 **Efficiency specification** 为 `Analytical` 时，*ηisen* 等于 **Isentropic efficiency** 参数的值。当 **Efficiency specification** 为 `Tabulated` 时，该模块通过将 **Isentropic efficiency table, eta\_isen(pr,w)** 参数的值插值为压力比和轴转速的函数来计算 *ηisen*。

### 可视化容积效率

要可视化模块容积效率，请右键单击该模块并选择 **Fluids** > **Plot Volumetric Efficiency**。

每次修改模块设置后，请在图形窗口中点击 **Reload Data**。

当您将 **Efficiency specification** 设置为 `Analytical` 且将 **Thermodynamic model** 设置为 `Polytropic` 时，该模块绘制压缩机容积效率随压力比变化的曲线。

容积效率

当您将 **Efficiency specification** 设置为 `Analytical` 且将 **Thermodynamic model** 设置为 `Isentropic` 时，该模块绘制压缩机在模块标称条件下的容积效率随压力比变化的曲线。

容积效率

当您将 **Efficiency specification** 设置为 `Tabulated` 时，该模块针对 **Shaft speed vector, w** 参数中的每个元素绘制压缩机容积效率随压力比变化的曲线。

容积效率

### 假设和限制

- 该模块对于从端口 **B** 流向端口 **A** 的流动可能不准确。
- 该模块假设流动为准稳态。压缩机不累积质量。
- 该模块设计用于在过热蒸气中运行。该模块在两相混合物或过冷液体中可能不准确。
