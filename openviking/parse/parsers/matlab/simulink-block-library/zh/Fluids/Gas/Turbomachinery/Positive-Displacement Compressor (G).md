---
type: simulink-block
title: 'Positive-Displacement Compressor (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Turbomachinery'
documentation_page: 'positivedisplacementcompressorg'
documentation_source_path: 'ref/positivedisplacementcompressorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Positive-Displacement Compressor (G)

## 端口

### 守恒

### **A** — 压缩机进口气体

与压缩机进口关联的气体守恒端口。

### **B** — 压缩机出口气体

与压缩机出口关联的气体守恒端口。

### **C** — 压缩机壳体机械旋转

与压缩机壳体关联的机械旋转守恒端口。

### **R** — 压缩机轴机械旋转

与压缩机轴关联的机械旋转守恒端口。

## 参数

### 排量

### **排量规格** — 按体积或标称条件指定排量的选项 `Volumetric displacement`（默认）| `Nominal mass flow rate and shaft speed`

是否根据每循环体积或标称条件值指定流体排量。

### **排量体积** — 排量体积 `130` `cm^3/rev`（默认）| positive scalar

每循环排出的流体体积。该模块将一个循环定义为一次压缩行程和一次膨胀行程，二者发生在单次曲轴旋转期间。此体积是最大气缸体积与余隙体积之差，(*Va* — *Vc*)。通常，排量体积是压缩机在单次轴旋转中扫过的体积。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Volumetric displacement`。

### **标称质量流量** — 标称质量流量 `0.01` `kg/s`（默认）| positive scalar

该模块用于求取排量体积的标称质量流量。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`。

### **标称轴转速** — 标称轴转速 `1000` `rpm`（默认）| positive scalar

该模块用于求取排量体积的标称轴转速。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`。

### 效率

该表显示 **热力学模型** 和 **效率规格** 参数的选项如何影响依赖的效率参数的可用性。

| **热力学模型** | | | |
| --- | --- | --- | --- |
| `Polytropic` | | `Isentropic` | |
| **效率规格** | | **效率规格** | |
| `Analytical` | `Tabulated` | `Analytical` | `Tabulated` |
| **多方指数** | **多方指数** | **等熵效率** | **等熵效率表, eta\_isen(pr,w)** |
| **标称容积效率** | **压比向量, pr** | **标称容积效率** | **压比向量, pr** |
| **轴转速向量, w** | **轴转速向量, w** |
| **容积效率表, eta\_vol(pr,w)** | **容积效率表, eta\_vol(pr,w)** |

### **效率规格** — 使用解析方式或表格参数化容积效率的选项 `Analytical`（默认）| `Tabulated`

是否使用解析方程或表格化数据参数化排量容积效率。

### **热力学模型** — 热力学模型参数化选项 `Polytropic`（默认）| `Isentropic`

是否使用多方或等熵热力学模型。

### **多方指数** — 多方指数 `1.2`（默认）| positive scalar

该模块在实现多方压力-体积关系时使用的指数。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Polytropic`。

### **等熵效率** — 等熵效率 `0.65`（默认）| positive scalar

该模块在实现解析等熵压力-体积关系时使用的恒定效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic` 并将 **效率规格** 设置为 `Analytical`。

### **等熵效率表, eta\_isen(pr,w)** — 等熵效率表 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认）| matrix

该模块在实现表格化等熵压力-体积关系时使用的效率。

#### 依赖关系

要启用此参数，请将 **热力学模型** 设置为 `Isentropic` 并将 **效率规格** 设置为 `Tabulated`。

### **标称容积效率** — 标称容积效率 `0.95`（默认）| positive scalar

用于计算余隙体积分数的标称容积效率。标称容积效率是压缩机在标称条件下运行时的容积效率。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Analytical`。

### **压比向量, pr** — 压比向量 `[2, 4, 6, 8]`（默认）| vector

与压缩机容积效率对应的压比向量。每个元素对应于 **容积效率表, eta\_vol(pr,w)** 参数的一行。此参数必须是大小为 `N` 的向量，其中 `N` 是 **容积效率表, eta\_vol(pr,w)** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### **轴转速向量, w** — 轴转速向量 `[800, 1500, 2800, 3300, 4000]` `rpm`（默认）| vector

与压缩机容积效率对应的轴转速向量。每个元素对应于 **容积效率表, eta\_vol(pr,w)** 参数的一列。此参数必须是大小为 `M` 的向量，其中 `M` 是 **容积效率表, eta\_vol(pr,w)** 参数的宽度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### **容积效率表, eta\_vol(pr,w)** — 容积效率 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认）| matrix

给定轴转速和压比下的容积效率。此参数必须是大小为 `N` × `M` 的矩阵，其中 `N` 是 **压比向量, pr** 参数的长度，`M` 是 **轴转速向量, w** 参数的长度。

#### 依赖关系

要启用此参数，请将 **效率规格** 设置为 `Tabulated`。

### 标称条件

该表显示 **排量规格**、**热力学模型** 和 **效率规格** 参数的选项如何影响依赖的标称条件参数的可用性。

此表显示当将 **排量规格** 参数设置为 `Volumetric displacement` 时的依赖参数：

| 当 **排量规格** 参数为 `Volumetric displacement` 时 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **效率规格** | | | | | | | |
| `Analytical` | | | | `Tabulated` | | | |
| **热力学模型** | | | | **热力学模型** | | | |
| `Polytropic` | | `Isentropic` | | `Polytropic` | | `Isentropic` | |
| **标称压比** | | **标称压比** | |  | | **标称压比** | |
| **标称进口压力** | | **标称进口压力** | |
| **标称进口温度** | | **标称进口温度** | |

当将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed` 时，**标称条件** 中的参数不依赖于 **效率规格** 或 **热力学模型** 参数。

### **标称压比** — 标称压比 `5`（默认）| positive scalar

该模块用于计算余隙体积分数的标称压比。

#### 依赖关系

要启用此参数，请选择任何参数化，但 **排量规格** 为 `Volumetric displacement`、**热力学模型** 为 `Polytropic` 且 **效率规格** 为 `Tabulated` 时除外。

### **标称进口压力** — 标称进口压力 `0.101325` `MPa`（默认）| positive scalar

该模块用于求取排量体积的标称进口压力。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### **标称进口温度** — 标称进口温度 `293.15` `K`（默认）| positive scalar

该模块用于求取排量体积的标称进口温度。

#### 依赖关系

要启用此参数，请将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed`，或将 **排量规格** 设置为 `Volumetric displacement` 并将 **热力学模型** 设置为 `Isentropic`。

### 参数

### **机械效率** — 压缩机机械效率 `0.9`（默认）| positive scalar

流体功率与机械轴功率之比。

### **端口 A 处的进口面积** — 进口面积 `0.01` `m^2`（默认）| positive scalar

与端口 **A** 关联的进口面积。

### **端口 B 处的出口面积** — 出口面积 `0.01` `m^2`（默认）| positive scalar

与端口 **B** 关联的出口面积。

## 所属库

Simscape / Fluids / Gas / Turbomachinery

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b: 对多方或等熵过程建模

现在可以使用 Positive-Displacement Compressor (G) 模块将容积式过程建模为多方过程或等熵过程。以前，该模块假设为多方过程。使用新的 **热力学模型** 参数选择效率模型。

## 描述

气体网络中的容积式压缩机

Positive-Displacement Compressor (G) 模块表示气体网络中的容积式压缩机，例如往复活塞式、螺杆式、旋片式或涡旋式。端口 **R** 和端口 **C** 分别是与压缩机轴和壳体关联的机械旋转守恒端口。当端口 **R** 相对于端口 **C** 存在正旋转时，气体从端口 **A** 流向端口 **B**。该模块对于反向流动可能不准确。

该图在 P-V 图上显示了活塞压缩机的各个步骤，这些状态包括：

- *a* — 压缩机气缸在进口压力下充满。
- *b* — 压缩机内部压力超过出口压力，从而导致流体排出。
- *c* — 压缩机到达活塞行程顶部，气缸内仅剩余余隙体积。
- *d* — 气缸内部压力降至进口压力以下，从而导致流体吸入。

显示活塞压缩机过程的图，其中点 A 处于低压、高体积，点 B 处于高压、高体积，端口 C 处于高压、低体积，点 d 处于低压、低体积。

### 质量流量

该模块按如下公式计算质量流量

m˙=ηVωVdispvs,

其中：

- *ṁ* 是质量流量。
- *ω* 是端口 **R** 相对于端口 **C** 的角速度。
- *vs* 是进口处的比容。该模块根据标称进口条件计算此值。
- *Vdisp* 是该模块使用的排量体积。

### 排量体积

当将 **排量规格** 设置为 `Volumetric displacement` 时，该模块使用 **排量体积** 参数作为 *Vdisp* 的值。

当将 **排量规格** 设置为 `Nominal mass flow rate and shaft speed` 时，该模块按如下公式计算排量体积

Vdisp=m˙nominalvs,nominalωnominalηVnominal,

其中：

- *ṁnominal* 是 **标称质量流量** 参数的值。
- *ωnominal* 是 **标称轴转速** 参数的值。
- *ηVnominal* 是当 **效率规格** 参数为 `Analytical` 时 **标称容积效率** 参数的值。当 **容积效率** 参数为 `Tabulated` 时，该模块使用 `tablelookup` 函数将 *ηVnominal* 插值为轴转速和压比的函数。

### 容积效率

可以使用解析值或查找表来参数化容积效率。

**解析容积效率**

当将 **效率规格** 设置为 `Analytical` 时，该模块使用解析值计算容积效率。当 **热力学模型** 参数为 `Polytropic` 时，容积效率为

ηV=1+C−C(poutpin)1n,

其中 *pin* 和 *pout* 分别是进口压力和出口压力，*n* 是 **多方指数** 参数的值。该模块按如下公式计算余隙体积分数 *C*：

C=1−ηVnominalpratio1/n−1,

其中 *ηVnominal* 是 **标称容积效率** 参数的值，*pratio* 是 **标称压比** 参数的值。

当 **热力学模型** 参数为 `Isentropic` 时，容积效率为

ηV=1+C−C(vinvout),

其中 *vin* 和 *vout* 分别是进口比容和出口比容。该模块按如下公式计算余隙体积分数 *C*：

C=1-ηVnominalvrnominal-1

其中 vrnominal=vinnominal/voutnominal 是标称比容比。该模块根据标称进口条件和等熵效率计算此值。

**表格化容积效率**

当将 **效率规格** 设置为 `Tabulated` 时，该模块通过将 **容积效率表, eta\_vol(pr,w)** 参数的值插值为轴转速和压比的函数来计算容积效率。

### 连续性方程

该模块按如下方式守恒质量

m˙A+m˙B=0,

其中 *ṁA* 和 *ṁB* 分别是端口 **A** 和 **B** 处的质量流量。该模块按如下方式守恒能量

ϕA+ϕB+m˙AΔht=0,

其中 *Δht* 是比总焓变化，*ṁAΔht* 是流体功率，它等于机械功率 *torque\*ω*。

当 **热力学模型** 参数为 `Polytropic` 时，流体功率为

W˙c=ωnn−1ηVpinVdisp[(pinpout)n−1n−1],

其中该模块使用多方关系 pvn=constant 来关联 *pin*、*pout*、*vin* 和 *vout*。

当 **热力学模型** 参数为 `Isentropic` 时，流体功率为

W˙C=m˙AΔht.

该模块根据等熵效率 *ηisen* 计算 *Δht*。当 **效率规格** 参数为 `Analytical` 时，*ηisen* 等于 **等熵效率** 参数的值。当 **效率规格** 参数为 `Tabulated` 时，该模块通过将 **等熵效率表, eta\_isen(pr,w)** 参数的值插值为压比和轴转速的函数来计算 *ηisen*。

### 可视化容积效率

要可视化模块容积效率，请右键单击该模块并选择 **Fluids** > **Plot Volumetric Efficiency**。

每次修改模块设置时，请在图窗中点击 **Reload Data**。

当将 **效率规格** 设置为 `Analytical` 并将 **热力学模型** 设置为 `Polytropic` 时，该模块绘制压缩机容积效率随压比变化的曲线。

容积效率

当将 **效率规格** 设置为 `Analytical` 并将 **热力学模型** 设置为 `Isentropic` 时，该模块绘制在 *Tout nom*（计算得到的标称出口温度）下压缩机容积效率随压比变化的曲线。

容积效率

当将 **效率规格** 设置为 `Tabulated` 时，该模块针对 **轴转速向量, w** 参数中的每个元素绘制压缩机容积效率随压比变化的曲线。

容积效率

### 假设和限制

- 对于从端口 **B** 流向端口 **A** 的流动，该模块可能不准确。
- 该模块假设流动是准稳态的。压缩机不积累质量。
