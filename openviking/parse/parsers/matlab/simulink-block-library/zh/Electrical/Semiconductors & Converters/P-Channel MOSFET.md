---
type: simulink-block
title: 'P-Channel MOSFET'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pchannelmosfet'
documentation_source_path: 'ref/pchannelmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# P-Channel MOSFET

## 端口

### 守恒

### **G** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **B** — 体极端子电气

与晶体管体极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of terminals** 设置为
`Four`。

### **H** — 热端口 热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Threshold-based with thermal` 或
`Surface-potential-based with thermal`。

## 参数

### **Modeling Option** — MOSFET 表示形式 `Threshold-based`（默认） | `Threshold-based with thermal` | `Surface-potential-based` | `Surface-potential-based with thermal`

选择 MOSFET 表示形式：

- `Threshold-based` — 基本模型，它使用 Shichman-Hodges 方程（基于阈值电压）表示器件，并且不模拟热效应。这是默认值。
- `Threshold-based with thermal` — 基于阈值电压的模型，并暴露热端口。
- `Surface-potential-based` — 基于表面电势的模型。此模型不模拟热效应。
- `Surface-potential-based with thermal` — 基于表面电势模型的热建模选项。

### Main（基于阈值建模选项）

**Main** 设置的此配置对应于基于阈值的模块建模选项，这是默认设置。如果您使用的是模块的基于表面电势的建模选项，请参阅 Main（基于表面电势建模选项）。

### **Number of terminals** — 端子参数化 `Three`（默认） | `Four`

模块的端子数量。

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认） | `Specify using equation parameters directly` | `Lookup table (2-D, temperature independent)` | `Lookup table (3-D, temperature dependent)`

选择以下模块参数化方法之一：

- `Specify from a datasheet` — 提供漏源导通电阻以及对应的漏极电流和栅源电压。模块根据此信息计算 Shichman and Hodges 方程的晶体管增益。
- `Specify using equation parameters directly` — 提供晶体管增益。
- `Lookup table (2-D, temperature independent)` — 使用 2-D 查表获取作为栅源电压和漏源电压函数的漏源电流。
- `Lookup table (3-D, temperature dependent)` — 使用 3-D 查表获取作为栅源电压、漏源电压和温度函数的漏源电流。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.167` `Ohm`（默认）

对于指定的漏极电流和栅源电压值，漏源电压与漏极电流之比。*RDS(on)* 应为正值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Drain current, Ids, for R\_DS(on)** — 用于 R\_DS(on) 的漏极电流, Ids `-2.5` `A`（默认）

模块用于计算漏源电阻值的漏极电流。*IDS* 应为负值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gate-source voltage, Vgs, for R\_DS(on)** — 用于 R\_DS(on) 的栅源电压, Vgs `-4.5` `V`（默认）

模块用于计算漏源电阻值的栅源电压。*VGS* 应为负值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gain, K** — 增益, K `2` `A/V2`（默认）

Shichman and Hodges 方程的正恒定增益系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Gate-source threshold voltage, Vth** — 栅源阈值电压 `-1.4` `V`（默认）

Shichman and Hodges 方程中的栅源阈值电压 *Vth*。对于增强型器件，*Vth* 应为负值。对于耗尽型器件，*Vth* 应为正值。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Gate-source threshold voltage at zero bulk-source voltage, Vth0** — 零体源电压下的栅源阈值电压 `-1.4` `V`（默认）

Shichman and Hodges 方程中零体源电压下的栅源阈值电压 *Vth0*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Channel modulation, L** — 沟道调制 `0` `1/V`（默认）

沟道长度调制，通常用数学符号 λ 表示。在饱和区中，它是漏极电流随漏源电压变化率的负值。对漏极电流的影响通常很小，如果根据漏源导通电阻 *RDS(on)* 计算晶体管增益 *K*，则会忽略该效应。典型值为 0.02，但在大多数电路仿真中可以忽略该效应。然而，在某些电路中，小的非零值可能有助于数值收敛。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Gate-source threshold voltage at first non-zero bulk-source voltage, Vth1** — 第一个非零体源电压下的栅源阈值电压 `-1.6071` `V`（默认）

Shichman and Hodges 方程中第一个非零体源电压下的栅源阈值电压 *Vth1*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **First bulk-source voltage, Vbs1** — 第一个体源电压 `1` `V`（默认）

第一个体源电压，*Vbs1*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gate-source threshold voltage at second non-zero bulk-source voltage, Vth2** — 第二个非零体源电压下的栅源阈值电压 `-1.7660` `V`（默认）

Shichman and Hodges 方程中第二个非零体源电压下的栅源阈值电压 *Vth2*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Second bulk-source voltage, Vbs2** — 第二个体源电压 `2` `V`（默认）

第二个体源电压，*Vbs2*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Body factor** — 体因子 `0.5` `V^0.50000`（默认）

体因子，*γ*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Surface potential** — 表面电势 `0.5` `V`（默认）

表面电势。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量 **Drain-source on resistance, R\_DS(on)** 时的温度 *Tm1*。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Vector of source-gate voltages, Vsg** — 源栅电压向量 `[-.5, 2, 3, 4, 5]` `V`（默认）

源栅电压向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Vector of source-drain voltages, Vsd** — 源漏电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V`（默认）

源漏电压向量，用于查表。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Vector of source-bulk voltages, Vsb** — 源体电压向量 `[0, -4, -6, -12]` `V`（默认）

源体电压向量，用于查表。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents, Isd(Vsg,Vsd)** — 表格化源漏电流，温度无关 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

表格化源漏电流值，作为源栅电压和源漏电压的函数，用于 2-D 查表。矩阵中的每个值指定了特定源栅电压和源漏电压组合下的源漏电流。矩阵大小必须与由源栅电压和源漏电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Vector of temperatures, T** — 温度向量 `[25 125]` `degC`（默认）

温度向量，用于查表。向量值必须严格递增。这些值可以非均匀间隔。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents, Isd(Vsg,Vsd,T)** — 表格化源漏电流，温度相关 `zeros(5, 7, 2)` `A`（默认）

表格化源漏电流值，作为源栅电压、源漏电压和温度的函数，用于 3-D 查表。矩阵中的每个值指定了特定源栅电压、源漏电压和温度组合下的源漏电流。矩阵大小必须与由源栅电压、源漏电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated gate-source threshold voltage, Vth(Vsb)** — 栅源阈值电压向量，温度无关 `[.4, 1.2, 1.4, 1.45]` `V`（默认）

表格化栅源阈值电压值，作为源体电压的函数，用于 2-D 查表。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd)** — 零源体电压下的表格化源漏电流，温度无关 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

零源体电压下的表格化源漏电流值，作为源栅电压和源漏电压的函数，用于 2-D 查表。矩阵中的每个值指定了特定源栅电压和源漏电压组合下的源漏电流。矩阵大小必须与由源栅电压和源漏电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Tabulated gate-source threshold voltage, Vth(Vsb,T)** — 栅源阈值电压向量，温度相关 `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V`（默认）

表格化栅源阈值电压值，作为体源电压和温度的函数，用于 3-D 查表。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd,T)** — 零源体电压下的表格化源漏电流，温度相关 `zeros(5, 7, 2)` `A`（默认）

零源体电压下的表格化源漏电流值，作为源栅电压、源漏电压和温度的函数，用于 3-D 查表。矩阵中的每个值指定了特定源栅电压、源漏电压和温度组合下的源漏电流。矩阵大小必须与由源栅电压、源漏电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Isd-Vsd parameterization** — Isd-Vsd 表数据作为对称数据 `Provide negative and positive Vsd data`（默认） | `Provide positive Vsd data only`

是否将 Isd-Vsd 表数据作为对称数据提供。如果选择
`Provide negative and positive Vsd data`，则数据不对称。如果选择 `Provide positive Vsd data only`，
则模块会旋转并翻转正值数据以获得负值数据。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### Main（基于表面电势建模选项）

**Main** 设置的此配置对应于基于表面电势的模块建模选项。如果您使用的是模块的基于阈值建模选项（基于 Shichman and Hodges 方程），请参阅 Main（基于阈值建模选项）。

### **Number of terminals** — 端子参数化 `Three`（默认） | `Four`

模块的端子数量。

### **Gain** — 增益 `18` `A/V2`（默认）

MOSFET 增益，*β*。此参数主要定义 *ID*–*VDS* 特性上的线性工作区。

### **Flatband voltage** — 平带电压 `-1.1` `V`（默认）

平带电压 *VFB* 定义了为实现硅表面平带条件而必须施加的栅极偏置。您也可以使用此参数来任意移动阈值电压，以考虑材料功函数差异以及俘获的界面电荷或氧化层电荷。但在实践中，通常建议先使用 **Body factor** 和 **Surface potential at strong inversion** 参数修改阈值电压，仅使用此参数进行微调。

### **Body factor** — 体因子 `3.5` `V1/2`（默认）

表面电势方程中的体因子 *γ*。此参数主要影响阈值电压。

### **Surface potential at strong inversion** — 强反型时的表面电势 `1` `V`（默认）

表面电势方程中的 2*ϕB* 项。此参数还主要影响阈值电压。

### **Velocity saturation factor** — 速度饱和因子 `0.4` `1/V`（默认）

漏极电流方程中的速度饱和 *θsat*。在良好拟合线性工作会导致饱和电流过高的情况下，使用此参数。通过增大此参数值，可降低饱和电流。对于高压器件，经常会出现良好拟合线性工作导致饱和电流过低的情况。在这种情况下，要么同时增大增益和漏极欧姆电阻，要么改用 P-Channel LDMOS FET block。

### **Channel-length modulation factor** — 沟道长度调制因子 `0`（默认）

*GΔL* 方程中对数项相乘的因子 α。此参数描述沟道长度调制的起始。对于在饱和区表现出正电导的器件特性，增大此参数值以拟合此行为。默认值为 `0`，这意味着默认情况下沟道长度调制关闭。

### **Channel-length modulation voltage** — 沟道长度调制电压 `5e-2` `V`（默认）

*GΔL* 方程中的电压 *Vp*。此参数控制沟道长度调制开始生效时的漏极电压。

### **Surface roughness scattering factor** — 表面粗糙度散射因子 `0` `1/V`（默认）

指示迁移率降低的强度。迁移率为 *μ* = *μ*/*Gmob*，其中 *μ0* 是无表面散射效应时的低场迁移率。迁移率降低因子 *Gmob* 由 Gmob=1+(θsrVeff)20 给出，其中 *θsr* 是表面粗糙度散射因子，*Veff* 是表示沟道中有效垂直电场强度 *Eeff* 的电压。对于高垂直电场，空穴的迁移率大致与 *Eeff* 成正比。

### **Linear-to-saturation transition coefficient** — 线性到饱和过渡系数 `8`（默认）

此参数控制 MOSFET 从线性区过渡到饱和区的平滑程度，尤其是在启用速度饱和时。此参数通常可以保留为其默认值，但您可以用它微调 *ID*–*VDS* 特性的拐点。此参数值的预期范围在 2 到 8 之间。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量模块参数时的温度 *Tm1*。如果 **Device simulation temperature** 参数在 **Temperature Dependence** 设置上与此值不同，则器件参数将根据仿真温度和参考温度从其定义值进行缩放。有关详细信息，请参阅温度依赖性（基于表面电势的建模选项）。

### 欧姆电阻

如果将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`，要启用此设置，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **Source ohmic resistance** — 源极欧姆电阻 `1e-4` `Ohm`（默认） | 非负标量

晶体管源极电阻，即与源极接触相关的串联电阻。该值必须大于或等于 `0`。基于阈值变体的默认值为 `1e-4` Ohm。基于表面电势变体的默认值为 `2e-3` Ohm。

### **Drain ohmic resistance** — 漏极欧姆电阻 `0.01` `Ohm`（默认） | 非负标量

晶体管漏极电阻，即与漏极接触相关的串联电阻。该值必须大于或等于 `0`。基于阈值变体的默认值为 `0.01` Ohm。基于表面电势变体的默认值为 `0.17` Ohm。

### **Gate ohmic resistance** — 栅极欧姆电阻 `8.4` `Ohm`（默认） | 非负标量

晶体管栅极电阻，即与栅极接触相关的串联电阻。该值必须大于或等于 `0`。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### **Body ohmic resistance** — 晶体管体电阻 `0.001` `Ohm`（默认） | 非负标量

晶体管体电阻，即与体接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Bulk ohmic resistance** — 晶体管衬底电阻 `2e-3` `Ohm`（默认） | 非负标量

晶体管体电阻，即与衬底接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### 封装

### **Source lead resistance** — 晶体管源极引线电阻 `0` `Ohm`（默认） | 非负标量

*自 R2024b 起*

晶体管源极引线电阻，即与源极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Drain lead resistance** — 晶体管漏极引线电阻 `0` `Ohm`（默认） | 非负标量

*自 R2024b 起*

晶体管漏极引线电阻，即与漏极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Gate lead resistance** — 晶体管栅极引线电阻 `0` `Ohm`（默认） | 非负标量

*自 R2024b 起*

晶体管栅极引线电阻，即与栅极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Body lead resistance** — 晶体管体引线电阻 `0` `Ohm`（默认） | 非负标量

*自 R2024b 起*

晶体管体引线电阻，即与体接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Source lead inductance** — 晶体管源极引线电感 `0` `nH`（默认） | 非负标量

*自 R2024b 起*

晶体管源极引线电感，即与源极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Drain lead inductance** — 晶体管漏极引线电感 `0` `nH`（默认） | 非负标量

*自 R2024b 起*

晶体管漏极引线电感，即与漏极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Gate lead inductance** — 晶体管栅极引线电感 `0` `nH`（默认） | 非负标量

*自 R2024b 起*

晶体管栅极引线电感，即与栅极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Body lead inductance** — 晶体管体引线电感 `0` `nH`（默认） | 非负标量

*自 R2024b 起*

晶体管体引线电感，即与体接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### 电容

要启用此设置，将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Parameterization** — 电容参数化 `Specify fixed input, reverse transfer, and output capacitance`（默认） | `Specify fixed gate-source, gate-drain, and drain-source capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-source, gate-drain, and drain-source capacitance`

选择以下电容参数化方法之一：

- `Specify fixed input, reverse transfer, and output capacitance` — 提供数据手册中的固定参数值，并让模块将输入、输出和反向传输电容值转换为电容值，如基于阈值的建模选项的电荷模型中所述。这是默认方法。
- `Specify fixed gate-source, gate-drain, and drain-source capacitance` — 直接提供电容参数的固定值。
- `Specify tabulated input, reverse transfer, and output capacitance` — 基于数据手册图提供表格化的电容和源-漏电压值。模块将输入、输出和反向传输电容值转换为电容值，如基于阈值的建模选项的电荷模型中所述。
- `Specify tabulated gate-source, gate-drain, and drain-source capacitance` — 提供电容和源-漏电压的表格化值。

### **Input capacitance, Ciss** — 输入栅源电容 `182` `pF`（默认）

漏极短接到源极时的栅源电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Input capacitance, Ciss(Vsd)** — 表格化输入的输入栅源电容 `[225 210 200 185 175 170]` `pF`（默认）

漏极短接到源极时的栅源电容，按源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Reverse transfer capacitance, Crss** — 反向传输电容 `24` `pF`（默认）

源极连接到地时的漏栅电容，也称为米勒电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Reverse transfer capacitance, Crss(Vsd)** — 表格化输入的反向传输电容 `[75 60 50 35 25 20]` `pF`（默认）

源极连接到地时的漏栅电容，也称为米勒电容，按源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Output capacitance, Coss** — 输出电容 `0` `pF`（默认）

栅极和源极短接时的漏源电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Output capacitance, Coss(Vsd)** — 表格化输入的输出电容 `[180 160 125 80 60 45]` `pF`（默认）

栅极和源极短接时的漏源电容，按源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Gate-source capacitance, Cgs** — 栅源电容 `158` `pF`（默认）

放置在栅极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **Gate-source capacitance, Cgs(Vsg, Vsd)** — 表格化值的栅源电容 `[150 150 150 150 150 150]` `pF`（默认）

放置在栅极和源极之间的电容，按源-栅电压和源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Gate-drain capacitance, Cgd** — 栅漏电容 `24` `pF`（默认）

放置在栅极和漏极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **Gate-drain capacitance, Cgd(Vsg,Vsd)** — 表格化值的栅漏电容 `[75 60 50 35 25 20]` `pF`（默认）

放置在栅极和漏极之间的电容，按源-栅电压和源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Gate-bulk capacitance, Cgb** — 栅-衬底电容 `0` `pF`（默认）

放置在栅极和衬底之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`，并将 **Gate-bulk and gate-source charge-voltage linearity** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **Gate-bulk capacitance, Cgb(Vsg,Vsd)** — 表格化值的栅-衬底电容 `[450 400 300 190 95 55]` `pF`（默认）

放置在栅极和衬底之间的电容，按源-栅电压和源-漏电压表格化。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`，并将 **Gate-bulk and gate-source charge-voltage linearity** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **Corresponding source-gate voltages, Vsg** — 对应的源-栅电压 `0` `V`（默认）

与表格化电容值对应的源-栅电压。

如果此值为标量，则 **Gate-source capacitance, Cgs(Vsg,Vsd)** 和 **Gate-drain capacitance, Cgd(Vsg,Vsd)** 是标量向量。如果此值为向量，则 **Gate-source capacitance, Cgs(Vsg,Vsd)** 和 **Gate-drain capacitance, Cgd(Vsg,Vsd)** 是标量矩阵。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Drain-source capacitance, Cds** — 漏源电容 `0` `pF`（默认）

放置在漏极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **Drain-source capacitance, Cds(vsd)** — 具有表格值 `[105 100 75 45 35 25]` `pF` (默认) 的漏源电容

放置在漏极和源极之间的电容，按源漏电压制表。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Corresponding source-drain voltages, Vsd** — 对应的源漏电压 `[0.1 0.3 1 3 10 30]` `V` (默认)

与表格电容值对应的源漏电压。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Source-gate voltage, Vsg, for tabulated capacitances** — 用于表格电容的源栅电压，Vsg `0` `V` (默认)

对于表格电容模型，此参数控制 **Reverse transfer capacitance, Crss** 或 **Gate-drain capacitance, Cgd** 参数（取决于所选参数化选项）的电压依赖性。这些电容是漏栅电压的函数。模块通过从 **Corresponding source-drain voltages** 参数指定值的负值中减去此栅源电压值来计算漏栅电压（*Vdg* = –*Vsd* – *Vgs*）。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Gate-drain charge-voltage linearity** — 栅漏电荷-电压线性度 `Gate-drain capacitance is constant` (默认) | `Gate-drain charge function is nonlinear`

这两个固定电容选项允许您将栅极电容建模为固定的栅源电容 *CGS* 以及固定或非线性的栅漏电容 *CGD*。选择栅漏电容是固定还是非线性：

- `Gate-drain capacitance is constant` — 电容值是恒定的，并根据所选参数化选项定义，可以直接定义或从数据手册导出。这是默认方法。
- `Gate-drain charge function is nonlinear` — 栅漏电荷关系根据 Charge Model for Threshold-Based Modeling Option 中描述的分段非线性函数定义。将出现两个附加参数，用于定义栅漏电荷函数。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer and output capacitance` 或 `Specify fixed gate-source, gate-drain and drain-source capacitance`。

### **Gate-drain oxide capacitance** — 栅漏氧化层电容 `200` `pF` (默认)

当漏栅电压小于 **Drain-gate voltage at which oxide capacitance becomes active** 参数值时，为栅漏电容。

#### 依赖关系

要启用此参数，请将 **Gate-drain charge-voltage linearity** 设置为 `Gate-drain charge function is nonlinear`。

### **Drain-gate voltage at which oxide capacitance becomes active** — 氧化层电容开始生效时的漏栅电压 `0.5` `V` (默认)

漏栅电容在关态（*CGD*）和开态（*Cox*）电容值之间切换时的漏栅电压。

#### 依赖关系

要启用此参数，请将 **Gate-drain charge-voltage linearity** 设置为 `Gate-drain charge function is nonlinear`。

### **Gate-bulk and gate-source charge-voltage linearity** — 栅体及栅源电荷-电压线性度 `Gate-bulk and gate-source capacitance change instantly` (默认) | `Gate-bulk and gate-source capacitance change gradually` | `Separate gate-bulk and gate-source capacitance`

栅体及栅源电荷-电压线性度。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。

要启用 `Separate gate-bulk and gate-source capacitance` 选项，请在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`

### 沟道电容

要启用此设置，请将 **Modeling option** 设置为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### **Oxide capacitance** — 氧化层电容 `1500` `pF` (默认)

平行板栅极-沟道电容。

### **Gate-source overlap capacitance** — 栅源重叠电容 `100` `pF` (默认)

与栅电极和源阱重叠相关的固定线性电容。

### **Gate-drain overlap capacitance** — 栅漏重叠电容 `14` `pF` (默认)

与栅电极和漏阱重叠相关的固定线性电容。

### 体二极管

### **Model body diode** — 体二极管建模选项 `No` (默认) | `Exponential` | `Tabulated I-V curve`

是否对体二极管建模。

### **Table type** — 表格函数 `Table in If(Tj,Vf) form` (默认) | `Table in Vf(Tj,If) form`

是将电流制表为温度和电压的函数，还是将电压制表为温度和电流的函数。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Tabulated I-V curve`。

### **Reverse saturation current, Is** — 反向饱和电流 `0` `A` (默认)

体二极管方程中由 *Is* 符号表示的电流。基于阈值的建模选项的默认值为 `0` A。基于表面电势的建模选项的默认值为 `5.2e-13` A。

对于 MOSFET 电流在仿真期间改变符号的应用（例如 MOSFET 驱动感性负载时），要使体二极管导通，请将此参数设置为非零值。

对于 MOSFET 电流从不改变符号的应用（例如小信号放大器），请将此参数设置为 0，以提高仿真速度。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`。

### **Built-in voltage, Vbi** — 内置电压 `0.6` `V` (默认)

二极管的内置电压，在体二极管方程中由 *Vbi* 符号表示。内置电压仅影响结电容方程。它不影响传导电流。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`。

### **Ideality factor, n** — 理想因子 `1` (默认)

体二极管方程中由 *n* 符号表示的因子。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`。

### **Zero-bias junction capacitance, Cj0** — 零偏结电容 `0` `pF` (默认)

仅由体二极管引起的、零偏时漏极与体接触之间的电容。它在体二极管方程中由 *Cj0* 符号表示。基于阈值的建模选项的默认值为 `0` pF。基于表面电势的建模选项的默认值为 `480` pF。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`。

### **Transit time, TT** — 渡越时间 `50e-9` `s` (默认)

体二极管方程中由 *τ* 符号表示的时间。

当 **Reverse saturation current** 和 **Transit time** 参数均非零时，此模块会在体二极管模型中包含反向恢复。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`。

### **Measurement temperature** — 测量温度 `25` `°C` (默认)

测量模块参数时的温度。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Exponential`，并在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`

### **Diode forward voltages, Vf(If)** — 二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V` (默认)

使二极管变为正向偏置所需施加的最小电压的表格值。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet`、`Specify from equation parameters directly` 或 `Lookup table (2-D, temperature independent)`。
- 在 **Body diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。

    **Table type** 为 `Table in Vf(If) form`。

### **Diode forward currents, If** — 与温度无关的二极管正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (默认)

正向电流的表格值。

#### 依赖关系

要启用此参数，请在 **Body diode** 设置中，将 **Model body diode** 设置为 `Tabulated I-V curve`，并将 **Table type** 设置为 `Table in Vf(If) form` 或 `Table in Vf(Tj,If) form`。

### **Diode forward currents, If(Vf)** — 随正向电压制表的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A` (默认)

正向电流随正向电压变化的表格值。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet`、`Specify from equation parameters directly` 或 `Lookup table (2-D, temperature independent)`。
- 在 **Body diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。

    **Table type** 为 `Table in If(Vf) form`。

### **Diode forward voltages, Vf** — 与温度无关的二极管正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (默认)

正向电压的表格值。

#### 依赖关系

要启用此参数，请在 **Body diode** 设置中，将 **Model body diode** 设置为 `Tabulated I-V curve`，并将 **Table type** 设置为 `Table in If(Vf) form` 或 `Table in If(Tj,Vf) form`。

### **Diode junction temperatures, Tj** — 二极管结温 `[25, 125]` `degC` (默认)

结温向量。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Tabulated I-V curve`，并在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。

### **Diode forward currents, If(Tj,Vf)** — 与温度相关的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (默认)

正向电流随正向电压和结温变化的表格值。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 在 **Body diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。

    **Table type** 为 `Table in If(Tj,Vf) form`。

### **Diode forward voltages, If(Tj,Vf)** — 与温度相关的二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (默认)

正向电压随正向电流和结温变化的表格值。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 在 **Body diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。

    **Table type** 为 `Table in Vf(Tj,If) form`。

### **Diode off conductance** — 二极管反向偏置时的电导 `1e-12` `1/Ohm` (默认) | positive scalar

*自 R2024a 起*

二极管反向偏置时的电导。

#### 依赖关系

要启用此参数，请将 **Model body diode** 设置为 `Tabulated I-V curve`。

### 温度依赖性（基于阈值的建模选项）

此 **Temperature Dependence** 设置配置对应于基于阈值的模块建模选项，这也是默认选项。如果您使用的是该模块的基于表面电势的建模选项，请参阅温度依赖性（基于表面电势的建模选项）

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature` (默认) | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature` — 不对温度依赖性建模。这是默认方法。
- `Model temperature dependence` — 对温度相关效应建模。为仿真温度 *Ts* 提供一个值，为 *BEX* 提供一个值，并为测量温度 *Tm1* 提供一个值（使用 **Main** 设置中的 **Measurement temperature** 参数）。您还必须根据 **Main** 设置中 **Parameterization** 参数的值，使用两种方法之一为 *α* 提供一个值。如果您从数据手册对模块进行参数化，则必须在第二个测量温度下提供 *RDS(on)*，模块将据此计算 *α*。如果您通过指定方程参数进行参数化，则必须直接提供 *α* 的值。

### **Drain-source on resistance, R\_DS(on), at second measurement temperature** — 第二个测量温度下的漏源导通电阻 `0.25` `Ohm` (默认)

在第二个测量温度下，对于指定的漏极电流和栅源电压值，漏源电压与漏极电流之比。它必须在与 **Main** 设置中的 **Drain-source on resistance, R\_DS(on)** 参数相同的工作点（漏极电流和栅源电压）下给出。

#### 依赖关系

仅当您在 **Main** 设置中为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC` (默认)

测量 **Drain-source on resistance, R\_DS(on), at second measurement temperature** 时的第二温度 *Tm2*。

#### 依赖关系

仅当您在 **Main** 设置中为 **Parameterization** 参数选择 `Specify from a datasheet` 时，此参数才可见。

### **Gate threshold voltage temperature coefficient, dVth/dT** — 栅极阈值电压温度系数 `2` `mV/K` (默认)

栅极阈值电压随温度的变化率。

#### 依赖关系

仅当您在 **Main** 设置中为 **Parameterization** 参数选择 `Specify using equation parameters directly` 时，此参数才可见。

### **Mobility temperature exponent, BEX** — 迁移率温度指数 `-1.5` (默认)

迁移率温度系数值。对于大多数 MOSFET，您可以使用默认值。有关其他注意事项，请参阅“假设和限制”部分。

### **Body diode reverse saturation current temperature exponent** — 体二极管反向饱和电流温度指数 `3`（默认）

假定体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* =
*NC*
exp(–*EG*/2*kB**T*)。*NC* 是温度相关的
有效态密度，*EG* 是
半导体材料的温度相关带隙。为避免引入另一个
温度缩放参数，该模块忽略带隙的温度依赖性，
并对所有器件类型使用 300K 下硅的带隙 (1.12eV)。因此，
温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **Reverse
saturation current** 参数的值，该参数来自 **Body Diode**
设置，*kB* 是玻尔兹曼常数
(8.617x10-5eV/K)，*ηIs*
是 **Body diode reverse
saturation current temperature exponent**。默认值为
`3`，因为硅的 *NC*
大致与 T3/2 成正比。你可以通过务实地选择
*ηIs* 来弥补忽略带隙温度依赖性的影响。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

器件仿真时的温度 *Ts*。

### 温度依赖性（基于表面电势的建模选项）

**Temperature Dependence** 设置的此配置对应于
基于表面电势的模块建模选项。如果你使用的是基于阈值的
模块建模选项，请参阅 温度依赖性（基于阈值的建模选项）

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认） | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement
  temperature` — 不对温度依赖性建模。这是
  默认方法。
- `Model temperature dependence` — 对
  温度相关效应建模。为器件仿真温度
  *Ts* 和其他模块参数的温度缩放系数
  提供值。

### **Gain temperature exponent** — 增益温度指数 `1.3`（默认）

假定 MOSFET 增益 *β* 随温度呈指数缩放，
*β* = *βm1*
(*Tm1*/*Ts*)^*ηβ*。*βm1* 是
**Main** 设置中 **Gain** 参数的值，
*ηβ* 是 **Gain temperature
exponent**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Flatband voltage temperature coefficient** — 平带电压温度系数 `5e-4` `V/K`（默认）

假定平带电压 *VFB* 随温度线性缩放，*VFB* =
*VFBm1* +
(*Ts* –
*Tm1*)*ST,VFB*。*VFBm1* 是
**Main** 设置中 **Flatband voltage** 参数的值，
*ST,VFB* 是
**Flatband voltage temperature coefficient**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Surface potential at strong inversion temperature coefficient** — 强反型表面电势温度系数 `-8.5e-4` `V/K`（默认）

假定强反型表面电势
2*ϕ*B 随温度线性缩放，*2ϕB* =
2*ϕBm1* +
(*Ts* –
*Tm1*)*ST,ϕB*。2*ϕBm1* 是
**Main** 设置中 **Surface potential at strong inversion** 参数的值，
*S*T,ϕB 是
**Surface potential at strong inversion temperature
coefficient**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Velocity saturation temperature exponent** — 速度饱和温度指数 `1.04`（默认）

假定速度饱和 *θsat* 随温度呈指数缩放，*θsat* =
*θsat,m1*
(*Tm1*/*Ts*)^*ηθ*。*θsat,m1* 是
**Main** 设置中 **Velocity saturation factor** 参数的值，
*ηθ* 是 **Velocity saturation temperature exponent**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Surface roughness scattering temperature exponent** — 表面粗糙度散射温度指数 `0.65`（默认）

此参数导致高栅极电压下 MOSFET 跨导随温度降低。假定表面粗糙度散射
*θsr* 随温度呈指数缩放，*θsr* =
*θsr,m1*
(*Tm1*/*Ts*)^*ηsr*。*θsr,m1* 是
**Main** 设置中 **Surface roughness scattering factor** 参数的值，
*ηsr* 是 **Surface roughness scattering temperature exponent**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Resistance temperature exponent** — 电阻温度指数 `0.95`（默认）

假定串联电阻对应于半导体电阻。
因此，它们随温度升高呈指数下降。*Ri* =
*Ri,m1*
(*Tm1*/*Ts*)^*ηR*，其中 *i* 为 S、D 或 G，分别对应
源极、漏极或栅极串联电阻。*Ri,m1*
是 **Ohmic Resistance** 设置中相应串联电阻参数的值，
*ηR* 是 **Resistance temperature exponent**。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Body diode reverse saturation current temperature exponent** — 体二极管反向饱和电流温度指数 `3`（默认）

假定体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* =
*NC*
exp(–*EG*/2*kB**T*)。*NC* 是温度相关的
有效态密度，*EG* 是
半导体材料的温度相关带隙。为避免引入另一个
温度缩放参数，该模块忽略带隙的温度依赖性，
并对所有器件类型使用 300K 下硅的带隙 (1.12eV)。因此，
温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **Reverse
saturation current** 参数的值，该参数来自 **Body Diode**
设置，*kB* 是玻尔兹曼常数
(8.617x10-5eV/K)，*ηIs*
是 **Body diode reverse
saturation current temperature exponent**。默认值为
`3`，因为硅的 *NC*
大致与 T3/2 成正比。你可以通过务实地选择
*ηIs* 来弥补忽略带隙温度依赖性的影响。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

器件仿真时的温度 *Ts*。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数可见。

### 故障

故障接口包括 **Fault Inspector** 窗口，以及对于支持故障的模块，还包括 **Blocks** 选项卡中的 **Faults** 部分。你定义触发故障的条件以及该触发发生时的故障行为。创建和编辑故障时，你会为故障行为设置参数。

要添加故障，请点击 **Add fault** 超链接。

创建故障后，可以在 **Fault Inspector** 窗口中更改属性。打开具有故障的模块时，会出现 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **PMOS fault** — 添加故障的选项 `Add fault`（默认）

在 P-Channel MOSFET 模块中添加故障的选项。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认） | nonnegative scalar

模块进入故障状态的仿真时间。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible source-gate voltage** — 故障转换的源栅电压阈值 `inf` `V`（默认） | positive scalar

最大允许源栅电压值，高于该值时可能触发故障。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible source-drain voltage** — 故障转换的源漏电压阈值 `inf` `V`（默认） | positive scalar

最大允许源漏电压值，高于该值时可能触发故障。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible bulk-drain voltage** — 故障转换的体漏电压阈值 `inf` `V`（默认） | positive scalar

最大允许体漏电压值，高于该值时可能触发故障。

#### 依赖项

要启用此参数：

- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。
- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Maximum permissible source-drain current** — 故障转换的电流阈值 `inf` `A`（默认） | positive scalar

最大允许源漏电流值。如果电流超过此值的持续时间长于
**Time to fail when exceeding drain-source
current** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **Time to fail when exceeding source-drain current** — 超过源漏电流时失效时间 `1` `s`（默认） | positive scalar

在触发行为故障之前，源漏电流必须连续超过最大
允许漏源电流的时间量。

#### 依赖项

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **Maximum permissible body diode current** — 故障转换的体二极管电流阈值 `inf` `A`（默认） | positive scalar

最大允许体二极管电流值。如果电流超过此值的持续时间长于
**Time to fail when exceeding body diode
current** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Time to fail when exceeding body diode current** — 超过体二极管电流时失效时间 `1` `s`（默认） | positive scalar

在触发行为故障之前，体二极管电流必须连续超过最大
允许体二极管电流的时间量。

#### 依赖项

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Maximum diode recovery, dV/dt** — 最大二极管恢复 `inf` `V/s`（默认） | positive scalar

每秒最大二极管恢复量。

#### 依赖项

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Maximum permissible temperature** — 故障转换的温度阈值 `inf` `K`（默认） | positive scalar

最大允许温度值。如果温度超过此值的持续时间长于
**Time to fail when exceeding
temperature** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based
  with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Time to fail when exceeding temperature** — 超过温度时失效时间 `1` `s`（默认） | positive scalar

在触发行为故障之前，温度必须连续超过最大
允许温度的时间量。

#### 依赖项

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based
  with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分。有关更多信息，请参阅 Set Fault Triggers。

### **Fault transition time constant, tau** — 故障转换时间常数 `1e-3` `s`（默认）

转换到故障状态的时间常数。

#### 依赖项

要启用此参数，请点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

### **Failure mode** — 失效类别 `Open circuit`（默认） | `Drain-source short` | `Drain-bulk short or source-bulk short` | `Gate oxide short` | `Parameter shift`

故障类型。你可以将此参数设置为：

- `Open circuit` — 由于
  金属化烧毁导致的失效。
- `Drain-source short` — 由于
  漏源沟道雪崩击穿导致的失效。
- `Drain-bulk short or source-bulk short` —
  由于漏体或源体沟道雪崩击穿导致的失效。
- `Gate oxide short` — 栅极
  氧化物介电层失效。
- `Parameter shift` — 由于
  老化导致的失效。

#### 依赖项

要启用此参数，请点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

要启用 `Drain-source short` 选项，请在
**Main** 设置中，将 **Number of terminals** 设置为
`Three`。

要启用 `Drain-bulk short or source-bulk short`
选项，请在 **Main** 设置中，将 **Number of
terminals** 设置为 `Four`。

### **Faulted series gate resistance, Rg** — 故障时串联栅极电阻 `1e6` `Ohm`（默认）

故障状态下的串联栅极电阻。

#### 依赖项

要启用此参数，请点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **Faulted series drain resistance, Rd** — 故障时串联漏极电阻 `1000` `Ohm`（默认）

故障状态下的串联漏极电阻。

#### 依赖项

要启用此参数，请点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **Faulted series source resistance, Rs** — 故障时串联源极电阻 `1000` `Ohm`（默认）

故障状态下的串联源极电阻。

#### 依赖项

要启用此参数，请点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **Faulted series bulk resistance, Rb** — 故障时串联源极电阻 `1000` `Ohm`（默认）

故障状态下的串联源极电阻。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Open
  circuit`。

### **故障状态下的并联漏-源电导，Gds** — 故障状态下的并联漏-源电导 `1000` `1/Ohm` (默认)

故障状态下的并联漏-源电导。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Three`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Drain-source
  short`。

### **故障状态下的并联漏-衬电导，Gdb** — 故障状态下的并联漏-衬电导 `1000` `1/Ohm` (默认)

故障状态下的并联漏-衬电导。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Drain-bulk short or
  source-bulk short`。

### **故障状态下的并联源-衬电导，Gsb** — 故障状态下的并联源-衬电导 `1000` `1/Ohm` (默认)

故障状态下的并联源-衬电导。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Drain-bulk short or
  source-bulk short`。

### **故障节点位置（距源极的总沟道长度百分比）** — 故障节点位置 `0` (默认)

故障节点的位置，以距源极的总沟道长度百分比表示。

#### 依赖项

要启用此参数，请在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **失效模式** 设为 `Gate oxide
short`。

### **栅氧化层短路电导，G** — 栅氧化层短路电导 `1000` `1/Ohm` (默认)

栅氧化层短路电导。

#### 依赖项

要启用此参数，请在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **失效模式** 设为 `Gate oxide
short`。

### **对栅氧化层短路二极管建模** — 栅氧化层短路二极管的建模选项 `No` (默认) | `Yes`

是否对栅氧化层短路二极管建模。

#### 依赖项

要启用此参数，请在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **失效模式** 设为 `Gate oxide
short`。

### **栅氧化层短路二极管反向饱和电流，Is** — 栅氧化层短路二极管的反向饱和电流 `0` `A` (默认)

栅氧化层短路二极管的反向饱和电流。

#### 依赖项

要启用此参数：

- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Gate oxide
  short`。
- 将 **对栅氧化层短路二极管建模** 设为 `Yes`。

### **栅氧化层短路二极管内建电压，Vbi** — 栅氧化层短路二极管的内建电压 `0.6` `V` (默认)

栅氧化层短路二极管的内建电压。

#### 依赖项

要启用此参数：

- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Gate oxide
  short`。
- 将 **对栅氧化层短路二极管建模** 设为 `Yes`。

### **栅氧化层短路二极管理想因子，n** — 栅氧化层短路二极管的理想因子 `1` (默认)

栅氧化层短路二极管的理想因子。

#### 依赖项

要启用此参数：

- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Gate oxide
  short`。
- 将 **对栅氧化层短路二极管建模** 设为 `Yes`。

### **栅氧化层短路二极管零偏结电容，Cj0** — 栅氧化层短路二极管的零偏结电容 `0` `pF` (默认)

栅氧化层短路二极管的零偏结电容。

#### 依赖项

要启用此参数：

- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Gate oxide
  short`。
- 将 **对栅氧化层短路二极管建模** 设为 `Yes`。

### **栅氧化层短路二极管渡越时间，TT** — 栅氧化层短路二极管的渡越时间 `50e-9` `s` (默认)

栅氧化层短路二极管的渡越时间。

#### 依赖项

要启用此参数：

- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Gate oxide
  short`。
- 将 **对栅氧化层短路二极管建模** 设为 `Yes`。

### **偏移后的增益占未偏移的百分比** — 偏移后的增益占未偏移的百分比 `100` (默认)

偏移后的增益占未偏移的百分比。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **阈值电压偏移值，dVth** — 阈值电压偏移值 `0` `V` (默认)

阈值电压的偏移值。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的沟道调制，L** — 故障状态下的沟道调制 `0` `1/V` (默认)

故障状态下的沟道调制。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **偏移后的体因子占未偏移的百分比** — 偏移后的体因子占未偏移的百分比 `100` (默认)

偏移后的体因子占未偏移的百分比。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **表面电位偏移值，dPhib** — 表面电位偏移值 `0` `V` (默认)

表面电位的偏移值。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的源极欧姆电阻，Rs** — 故障状态下的源极欧姆电阻 `0.0001` `Ohm` (默认)

故障状态下的晶体管源极电阻。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的漏极欧姆电阻，Rd** — 故障状态下的漏极欧姆电阻 `0.01` `Ohm` (默认)

故障状态下的晶体管漏极电阻。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的体欧姆电阻，Rb** — 故障状态下的体欧姆电阻 `0.001` `Ohm` (默认)

故障状态下的晶体管体电阻。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Specify from a
  datasheet` 或 `Specify using equation parameters
  directly`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的源-栅电压向量，Vsg** — 故障状态下的源-栅电压向量 `[-.5, 2, 3, 4, 5]` `V` (默认)

故障状态下的源-栅电压。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)` 或 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的源-漏电压向量，Vsd** — 故障状态下的源-漏电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V` (默认)

故障状态下的源-漏电压。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)` 或 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的源-衬电压向量，Vsb** — 故障状态下的源-衬电压向量 `[0, -4, -6, -12]` `V` (默认)

故障状态下的源-衬电压。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)` 或 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下表列的栅-源阈值电压，Vth(Vsb)** — 故障状态下表列的栅-源阈值电压 `[.4, 1.2, 1.4, 1.45]` `V` (默认)

故障状态下的表列栅-源阈值电压。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下表列的栅-源阈值电压，Vth(Vsb,T)** — 依赖温度的故障状态下表列的栅-源阈值电压 `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V` (默认)

故障状态下的栅-源阈值电压，按衬-源电压和温度表列。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下表列的源-漏电流，Isd(Vsg,Vsd)** — 故障状态下表列的源-漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (默认)

故障状态下的表列源-漏电流。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Three`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下表列的源-漏电流，Isd(Vsg,Vsd,T)** — 依赖温度的故障状态下表列的源-漏电流 `zeros(5, 7, 2)` `A` (默认)

故障状态下的源-漏电流，按源-栅电压、源-漏电压和温度表列。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Three`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **源-衬电压为零时故障状态下表列的源-漏电流，Isd(Vsg,Vsd)** — 源-衬电压为零时故障状态下表列的源-漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (默认)

当源-衬电压为零时，故障状态下的表列源-漏电流。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (2-D,
  temperature independent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **源-衬电压为零时故障状态下表列的源-漏电流，Isd(Vsg,Vsd,T)** — 源-衬电压为零时依赖温度的故障状态下表列的源-漏电流 `zeros(5, 7, 2)` `A` (默认)

当源-衬电压为零时，故障状态下的表列源-漏电流，按源-栅电压、源-漏电压和温度表列。

#### 依赖项

要启用此参数：

- 在 **Main** 设置中，将 **端子数量** 设为 `Four`。
- 在 **Main** 设置中，将 **参数化** 设为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **PMOS 故障** 参数中点击 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设为 `Parameter
  shift`。

### **故障状态下的栅-源电容占未故障时的百分比** — 故障状态下的栅-源电容占未故障时的百分比 `100` (默认)

故障状态下的栅-源电容占未故障时的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify fixed input,
  reverse transfer, and output capacitance` 或
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance` 或
  `Specify tabulated gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open
  circuit`、`Drain-source short`、
  `Drain-bulk short or source-bulk short` 或
  `Gate oxide short`。

### **Faulted gate-drain capacitance as percentage of unfaulted** — 故障状态下的栅-漏电容占未故障状态的百分比 `100`（默认）

故障状态下的栅-漏电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify fixed input,
  reverse transfer, and output capacitance` 或
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance` 或
  `Specify tabulated gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open
  circuit`、`Drain-source short`、
  `Drain-bulk short or source-bulk short` 或
  `Gate oxide short`。

### **Faulted gate-bulk capacitance as percentage of unfaulted** — 故障状态下的栅-体电容占未故障状态的百分比 `100`（默认）

故障状态下的栅-体电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify fixed
    gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-bulk and gate-source charge-voltage
    linearity** 设置为 `Separate gate-bulk and
    gate-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify
    tabulated gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-bulk and gate-source charge-voltage
    linearity** 设置为 `Separate gate-bulk and
    gate-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open
  circuit`、`Drain-bulk short or source-bulk
  short` 或 `Gate oxide short`。

### **Faulted drain-source capacitance as percentage of unfaulted** — 故障状态下的漏-源电容占未故障状态的百分比 `100`（默认）

故障状态下的漏-源电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify fixed input,
  reverse transfer, and output capacitance` 或
  `Specify fixed gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance` 或
  `Specify tabulated gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open
  circuit`、`Drain-source short`、
  `Drain-bulk short or source-bulk short` 或
  `Gate oxide short`。

### **Faulted gate-drain oxide capacitance as percentage of unfaulted** — 故障状态下的栅-漏氧化层电容占未故障状态的百分比 `100`（默认）

故障状态下的栅-漏氧化层电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify fixed
    input, reverse transfer, and output capacitance` 或
    `Specify fixed gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-drain charge-voltage linearity** 设置为
    `Gate-drain charge function is non
    linear`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted drain-gate voltage at which oxide capacitance becomes active** — 氧化层电容开始激活时的故障漏-栅电压 `-0.5` `V`（默认）

故障状态下氧化层电容开始激活时的漏-栅电压。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify fixed
    input, reverse transfer, and output capacitance` 或
    `Specify fixed gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-drain charge-voltage linearity** 设置为
    `Gate-drain charge function is non
    linear`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted input capacitance, Ciss(Vds)** — 故障输入电容 `[720, 700, 590, 470, 390, 310]` `pF`（默认）

故障状态下的输入电容。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted reverse transfer capacitance, Crss(Vds)** — 故障反向传输电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认）

故障状态下的反向传输电容。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted output capacitance, Coss(Vds)** — 故障输出电容 `[900, 810, 690, 420, 270, 170]` `pF`（默认）

故障状态下的输出电容。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted corresponding source-drain voltages, Vsd** — 故障对应的源-漏电压 `[.1, .3, 1, 3, 10, 30]` `V`（默认）

故障状态下的对应漏-源电压。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance` 或
  `Specify tabulated gate-source, gate-drain, and drain-source
  capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted source-gate voltages, Vsg, for tabulated capacitances** — 表格化电容对应的故障源-栅电压 `0` `V`（默认）

故障状态下表格化电容对应的源-栅电压。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  input, reverse transfer, and output capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

**条件组二**

- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify
    tabulated gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-bulk and gate-source charge-voltage
    linearity** 设置为 `Gate-bulk and gate-source
    capacitance change instantly` 或 `Gate-bulk
    and gate-source capacitance change gradually`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted gate-source capacitance, Cgs(Vgs,Vds)** — 故障栅-源电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认）

故障状态下的栅-源电容，随栅-源电压和漏-源电压表格化。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted gate-drain capacitance, Cgd(Vgs,Vds)** — 故障栅-漏电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认）

故障状态下的栅-漏电容，随栅-源电压和漏-源电压表格化。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，将
  **Parameterization** 设置为 `Specify tabulated
  gate-source, gate-drain, and drain-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted gate-bulk capacitance, Cgb(Vgs,Vds)** — 故障栅-体电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认）

故障状态下的栅-体电容，随栅-源电压和漏-源电压表格化。

#### 依赖关系

要启用此参数，请：

- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify
    tabulated gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-bulk and gate-source charge-voltage
    linearity** 设置为 `Separate gate-bulk and
    gate-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted corresponding source-gate voltages, Vsg** — 故障对应的源-栅电压 `0` `V`（默认）

故障状态下的对应源-栅电压。

#### 依赖关系

要启用此参数，请：

- 在 **Capacitance** 设置中，设置：

  - 将 **Parameterization** 设置为 `Specify
    tabulated gate-source, gate-drain, and drain-source
    capacitance`。
  - 将 **Gate-bulk and gate-source charge-voltage
    linearity** 设置为 `Separate gate-bulk and
    gate-source capacitance`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode reverse saturation current, Is** — 故障二极管反向饱和电流 `0` `A`（默认）

故障状态下二极管的反向饱和电流。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Exponential`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode built-in voltage, Vbi** — 故障二极管内建电压 `0.6` `V`（默认）

故障状态下二极管的内建电压。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Exponential`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode ideality factor, n** — 故障二极管理想因子 `1`（默认）

故障状态下二极管的理想因子。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Exponential`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode zero-bias junction capacitance as percentage of unfaulted** — 故障二极管零偏结电容占未故障状态的百分比 `100`（默认）

故障二极管零偏结电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Exponential`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode transit time, TT** — 故障二极管渡越时间 `50e-9` `s`（默认）

故障状态下二极管的渡越时间。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Exponential`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode forward currents, If(Vf)** — 故障二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A`（默认）

故障状态下二极管的正向电流，随正向电压表格化。

#### 依赖关系

要启用此参数，请：

- 在 **Main** 设置中，将
  **Parameterization** 设置为 `Specify from a
  datasheet`、`Specify using equation parameters
  directly` 或 `Lookup table (2-D, temperature
  independent)`。
- 在 **Body Diode** 设置中，设置：

  - 将 **Model body diode** 设置为 `Tabulated I-V
    curve`。
  - 将 **Table type** 设置为 `Table in If(Vf)
    form`。
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode forward voltages, Vf** — 故障二极管正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

故障状态下二极管的正向电压。

#### 依赖关系

要启用此参数，请：

- 在 **Body Diode** 设置中，设置：

  - 将 **Model body diode** 设置为 `Tabulated I-V
    curve`。
  - 将 **Table type** 设置为 `Table in If(Vf)
    form` 或 `Table in If(Tj,Vf)
    form`
- 在 **PMOS fault**
  参数中单击 **添加故障**
  超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **故障二极管正向电压, Vf(If)** — 故障二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V`（默认）

故障状态下二极管的正向电压，与正向电流一起列表。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a
  datasheet`、`Specify using equation parameters
  directly` 或 `Lookup table (2-D, temperature
  independent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。
  - **表类型** 为 `Table in Vf(If)
    form`。
- 通过点击 **PMOS 故障** 参数中的 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设置为 `Parameter
  shift`。

### **故障二极管正向电流, If** — 故障二极管正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

故障状态下二极管的正向电流。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。
  - **表类型** 为 `Table in Vf(If)
    form` 和 `Table in Vf(Tj,If)
    form`。
- 通过点击 **PMOS 故障** 参数中的 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设置为 `Parameter
  shift`。

### **故障二极管正向电流, If(Tj,Vf)** — 带表格输入的故障二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）

故障状态下二极管的正向电流，与正向电压和结温一起列表。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。
  - **表类型** 为 `Table in If(Tj,Vf)
    form`。
- 通过点击 **PMOS 故障** 参数中的 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设置为 `Parameter
  shift`。

### **故障二极管正向电压, Vf(Tj,If)** — 带表格输入的故障二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）

故障状态下二极管的正向电压，与正向电流和结温一起列表。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。
  - **表类型** 为 `Table in Vf(Tj,If)
    form`。
- 通过点击 **PMOS 故障** 参数中的 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设置为 `Parameter
  shift`。

### **故障二极管关断电导** — 故障二极管关断电导 `1e-12` `1/Ohm`（默认）

*自 R2024a 起*

故障状态下二极管的关断电导。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **体二极管建模** 设置为 `Tabulated I-V curve`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设置为 `Parameter
  shift`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2008a 中引入**

### R2024b: 对每个晶体管端子的寄生引线电阻和电感建模

现在，您可以通过使用以下参数指定引线电阻和电感，对 P-Channel MOSFET 模块每个端子中的寄生效应建模：

- **源极引线电阻**
- **漏极引线电阻**
- **栅极引线电阻**
- **体引线电阻**
- **源极引线电感**
- **漏极引线电感**
- **栅极引线电感**
- **体引线电感**

### R2024a: 指定表格化二极管的关断电导值

现在，您可以使用 **二极管关断电导** 参数指定表格化二极管的关断电导值。

在 R2024a 之前，要指定表格化二极管的关断电导，您必须将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数，设置 P-Channel MOSFET 模块和其他 SPICE 兼容模块的最小电导。

## 描述

P-Channel 金属氧化物半导体场效应晶体管，使用 Shichman-Hodges 方程或基于表面势的模型

P-Channel MOSFET 模块提供两种主要建模选项：

- 基于阈值电压 — 使用 Shichman-Hodges 方程表示器件。这种基于阈值电压的建模方法的优点在于参数化简单且电流-电压表达式简单。然而，这些模型难以准确捕捉跨阈值电压的过渡，并且缺少一些重要效应，例如速度饱和。有关详细信息，请参阅基于阈值的模型。

  此建模选项提供四种参数化 P-Channel MOSFET 的方式：

  - 通过从数据表指定参数。
  - 通过直接指定方程参数。
  - 通过 I-V（电流-电压）曲线的 2-D 查找表近似。有关详细信息，请参阅通过 2-D 查找表表示。
  - 通过包含温度数据的 I-V（电流-电压）曲线的 3-D 查找表近似。有关详细信息，请参阅通过 3-D 查找表表示。
- 基于表面势 — 使用表面势方程表示器件。这种建模方法比简单的平方律（基于阈值电压）模型提供更高水平的模型保真度。代价是需要提取更多参数。有关详细信息，请参阅基于表面势的模型。

结合热端口变体（请参阅热端口），该模块因此为您提供四种选择。要选择所需的建模选项，请将 **建模选项** 参数设置为以下之一：

- **Threshold-based** — 基本模型，使用 Shichman-Hodges 方程（基于阈值电压）表示器件，并且不仿真热效应。这是默认值。
- **Threshold-based with thermal** — 基于阈值电压的模型，并带有暴露的热端口。
- **Surface-potential-based** — 基于表面势的模型。此模型不仿真热效应。
- **Surface-potential-based with thermal** — 基于表面势的模型的热建模选项。

### 基于阈值的模型

该模块的基于阈值的建模选项使用绝缘栅场效应晶体管的 Shichman and Hodges 方程 [1] 来表示 P-Channel MOSFET。

漏源电流 *IDS* 取决于工作区：

- 在截止区（–*VGS* < –*Vth*）中，漏源电流为：

  IDS=0
- 在线性区（0 < –*VDS* < –*VGS* +*Vth*）中，漏源电流为：

  IDS=−K((VGS−Vth)VDS−VDS2/2)(1+λ|VDS|)
- 在饱和区（0 < –*VGS* +*Vth* < –*VDS*）中，漏源电流为：

  IDS=−(K/2)(VGS−Vth)2(1+λ|VDS|)

在上述方程中：

- *K* 是晶体管增益。
- *VDS* 是负漏源电压。
- *VGS* 是栅源电压。
- *Vth* 是阈值电压。对于四端子参数化，*Vth* 使用以下方程获得：

  | *VBS* 范围 | *Vth* 方程 |
  | --- | --- |
  | VBS≤0 | Vth=VT0+γ(2ϕB)−γ(2ϕB+VBS) |
  | 0<VBS≤4ϕB | Vth=VT0−γVBS2ϕB |
  | VBS>4ϕB | Vth=VT0+γ(2ϕB) |
- *λ* 是沟道调制。

要指定沟道的并联电导，请将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数，设置 P-Channel MOSFET 模块以及其他 SPICE 兼容模块的最小电导。

### 基于阈值建模选项的电荷模型

该模块通过固定电容值或作为漏源电压函数的表格值来对电容建模。无论哪种情况，您都可以直接指定栅源和栅漏电容值，或者让该模块从输入电容和反向传输电容值推导它们。因此，**电容** 设置上电荷模型的 **参数化** 选项包括：

- `Specify fixed input, reverse transfer and output
  capacitance` — 提供来自数据表的固定参数值，并让该模块按照下文所述将输入电容和反向传输电容值转换为电容值。这是默认方法。
- `Specify fixed gate-source, gate-drain and drain-source
  capacitance` — 直接提供电容参数的固定值。
- `Specify tabulated input, reverse transfer and output
  capacitance` — 基于数据表图提供表格化电容和漏源电压值。该模块按照下文所述将输入电容和反向传输电容值转换为电容值。
- `Specify tabulated gate-source, gate-drain and drain-source
  capacitance` — 提供电容和漏源电压的表格化值。

当数据表提供电容作为漏源电压函数的图时，请使用其中一个表格化电容选项（`Specify tabulated input, reverse transfer and output capacitance` 或 `Specify tabulated gate-source, gate-drain and drain-source capacitance`）。使用表格化电容值可获得更准确的动态特性，并避免为拟合动态特性而迭代调整参数。

如果您使用 `Specify fixed gate-source, gate-drain and drain-source capacitance` 或 `Specify tabulated gate-source, gate-drain and drain-source capacitance` 选项，则 **电容** 设置允许您直接指定 **栅漏电容, Cgd**、**栅源电容, Cgs** 和 **漏源电容, Cds** 参数值（固定或表格化）。否则，该模块从 **输入电容, Ciss**、**反向传输电容, Crss** 和 **输出电容, Coss** 参数值推导它们。这两种参数化方法的关系如下：

- *CGD* = *Crss*
- *CGS* = *Ciss* – *Crss*
- *CDS* = *Coss* – *Crss*

对于四端子参数化，**输入电容, Ciss**、**反向传输电容, Crss** 和 **输出电容, Coss** 使用以下方程获得：

- *CGD* = *Crss*
- *CGS* + *CGB* = *Ciss* – *Crss*
- *CDB* = *Coss* – *Crss*

使用简化的 Meyer 电容模型来描述栅源电容 *CGS*、栅体电容 *CGB* 和栅漏电容 *CGD*。这些图显示栅体电容和栅源电容如何瞬时变化，而

栅体电容和栅源电容瞬时变化。

两种固定电容选项（`Specify fixed input, reverse transfer and output capacitance` 或 `Specify fixed gate-source, gate-drain and drain-source capacitance`）允许您将栅极电容建模为固定栅源电容 *CGS* 以及固定或非线性栅漏电容 *CGD*。如果您为 **栅漏电荷-电压线性度** 参数选择 `Gate-drain charge function is nonlinear` 选项，则栅漏电荷关系由下图中所示的分段线性函数定义。

有关如何将时间响应映射到器件电容值的说明，请参阅 N-Channel IGBT 模块参考页。然而，这种映射只是近似的，因为 Miller 电压通常比 IGBT 情况下更偏离阈值电压。

**注意**

因为此模块实现包含电荷模型，所以您必须对驱动栅极的电路阻抗建模，以获得具有代表性的开通和关断动态特性。因此，如果您通过将栅极驱动电路表示为受控电压源来简化它，则必须在电压源和栅极之间包含合适的串联电阻。

### 通过 2-D 查找表表示

对于详细模块建模选项的查找表表示，您提供源漏电流作为源栅电压和源栅电压函数的表格值。使用此选项的主要优点是仿真速度。它还允许您从测量数据或从另一仿真环境获得的数据来参数化器件。

此图显示当您将 **Isd-Vsd 参数化** 设置为 `Provide negative and positive Vsd data` 时，2-D 查找表选项的实现：

此图显示当您将 **Isd-Vsd 参数化** 设置为 `Provide positive Vsd data only` 时，2-D 查找表选项的实现：

对于四端子 MOSFET，表面势和体因子值基于最近的阈值电压计算，如此图所示：

**注意**

为确保源漏电流和源漏电压的符号一致：

- 如果源漏电压等于 `0`，则 **表格化源漏电流, Isd(Vsg,Vsd)** 参数的值必须等于 `0`。
- 表格化功率（即 **表格化源漏电流, Isd(Vsg,Vsd)** 参数与源漏电压的乘积）必须大于或等于 `0`。
- 表格化电导（即 **表格化源漏电流, Isd(Vsg,Vsd)** 参数相对于源漏电压 *Vsd* 的梯度）必须大于或等于 `0`。
- **表格化源漏电流, Isd(Vsg,Vsd)** 参数相对于源栅电压 *Vsg* 的一阶梯度必须等于 `0`。

### 通过 3-D 查找表表示

对于详细模块建模选项的温度相关查找表表示，您提供源漏电流作为源栅电压、源栅电压和温度函数的表格值。

**注意**

为确保源漏电流和源漏电压的符号一致：

- 如果源漏电压等于 `0`，则 **表格化源漏电流, Isd(Vsg,Vsd,T)** 参数的值必须等于 `0`。
- 表格化功率（即 **表格化源漏电流, Isd(Vsg,Vsd,T)** 参数与源漏电压的乘积）必须大于或等于 `0`。
- 表格化电导（即 **表格化源漏电流, Isd(Vsg,Vsd,T)** 参数相对于源漏电压 *Vsd* 的梯度）必须大于或等于 `0`。
- **表格化源漏电流, Isd(Vsg,Vsd,T)** 参数相对于源栅电压 *Vsg* 的一阶梯度必须等于 `0`。

### 基于表面电势的模型

该模块的基于表面电势的建模选项比简单的平方律（基于阈值电压）模型提供更高水平的模型保真度。基于表面电势的模块建模选项包括以下效应：

- 完全非线性电容模型（包括非线性 Miller 电容）
- 模型内部电荷守恒，因此可将该模型用于电荷敏感仿真
- 速度饱和与沟道长度调制
- 本征体二极管
- 体二极管模型中的反向恢复
- 物理参数的温度缩放
- 对于热建模选项，动态自热（即，可以仿真自热对器件电气特性的影响）

该模型是世界标准 PSP 模型的最小版本（参见 https://briefs.techconnect.org/papers/introduction-to-psp-mosfet-model/），仅包含 PSP 模型中的某些效应，以在模型保真度与复杂度之间取得平衡。有关该模型中包含现象的物理背景详细信息，请参见 [2]。

表面电势方程的推导方式与 N-Channel MOSFET 模块参考页中描述的方式类似，所有电压、电荷和电流均乘以 -1。

整体模型由通过表面电势公式定义的本征 MOSFET、体二极管、串联电阻和固定重叠电容组成，如示意图所示。

### 体二极管建模

该模块将体二极管建模为理想指数二极管或表格化二极管。

**指数二极管**

该模块将体二极管建模为理想指数二极管或表格化二极管。

当将 **Model body diode** 设置为 `Exponential` 时，结电容和扩散电容为：

Idio=Is[exp(−VBDnϕT)−1]

Cj=Cj01+VBDVbi

Cdiff=τIsnϕTexp(−VBDnϕT)

其中：

- *Idio* 是流过二极管的电流。
- *Is* 是反向饱和电流。
- *VBD* 是体漏电压。
- *n* 是理想因子。
- *ϕT* 是热电压。
- *Cj* 是二极管的结电容。
- *Cj0* 是零偏结电容。
- *Vbi* 是内建电压。
- *Cdiff* 是二极管的扩散电容。
- *τ* 是渡越时间。

这些电容通过显式计算电荷来定义，然后对电荷求导以得到上述电容表达式。该模块将电容性二极管电流计算为相关电荷的时间导数，类似于基于表面电势的 MOSFET 模型中的计算。

**表格化二极管**

要建模表格化二极管，将 **Model body diode** 参数设置为 `Tabulated I-V curve`。下图显示了表格化二极管选项的实现：

选择此参数化时，必须仅提供正向偏置的数据。

该模块使用平滑插值选项实现二极管。如果二极管超出所提供的表格化数据范围，则该模块在最后一个电压-电流数据点处使用线性外推技术。

要指定表格化二极管的关断电导，请设置 **Diode off conductance** 参数。*（自 R2024a 起）*

**注意**

表格化二极管不对反向击穿建模。

### 温度依赖性建模

默认行为是不对温度依赖性进行建模，器件在提供模块参数时的温度下进行仿真。要在仿真期间对温度依赖性建模，请在 **Temperature Dependence** 设置的 **Parameterization** 参数中选择 `Model temperature dependence`。

**基于阈值的模型**

对于基于阈值的建模选项，您可以包括在仿真期间对晶体管静态行为温度依赖性的建模。不对结电容的温度依赖性建模，因为其影响要小得多。

当包括温度依赖性时，晶体管定义方程保持不变。增益 *K* 和阈值电压 *Vth* 根据以下方程成为温度的函数：

KTs=KTm1(TsTm1)BEX

*V*ths =
*Vth1* + *α* (
*Ts* – *Tm1*)

其中：

- *Tm1* 是指定晶体管参数时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *KTm1* 是测量温度下的晶体管增益。
- *KTs* 是仿真温度下的晶体管增益。当对温度依赖性建模时，这是 MOSFET 方程中使用的晶体管增益值。
- *Vth1* 是测量温度下的阈值电压。
- *Vths* 是仿真温度下的阈值电压。当对温度依赖性建模时，这是 MOSFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**Vth*/*d**T*。

对于四端子参数化，*Vth* 使用以下方程获得：

| *VBS* 范围 | *Vth* 方程 |
| --- | --- |
| VBS≤0 | dVthdT=dVT0dT−γ22ϕBd2ϕBdT+γ22ϕB−VBSd2ϕBdT |
| 0<VBS≤4ϕB | dVthdT=dVT0dT−γVBS4(2ϕB)−32d2ϕBdT |
| VBS>4ϕB | dVthdT=dVT0dT−γ22ϕBd2ϕBdT |

其中：

- ϕB=kTqln(NBni) 是表面电势，且 d2ϕBdT=−1T[2ϕB−(Eg(0)q+3kTq)]。
- *Eg(0)* 是外推的零度带隙，对于硅等于 `1.16` `eV`。
- *VBS* 是体源电压。

对于大多数 MOSFETS，可以使用 `-1.5` 作为 *BEX* 的默认值。一些数据表给出了 *α* 的值，但最典型的是提供漏源导通电阻 *RDS(on)* 的温度依赖性。根据模块参数化方法，有两种指定 *α* 的方式：

- 如果从数据表对模块进行参数化，则必须提供第二个测量温度下的 *RDS(on)*。然后该模块基于此数据计算 *α* 的值。
- 如果通过指定方程参数进行参数化，则必须直接提供 *α* 的值。

如果您有更多数据，包括多个温度下漏极电流作为栅源电压函数的数据，那么您还可以使用 Simulink® Design Optimization™ 软件来帮助调整 *α* 和 *BEX* 的值。

**基于表面电势的模型**

基于表面电势的模型包括温度对电容特性的影响，以及在仿真期间对晶体管静态行为温度依赖性的建模。

**Main** 设置上的 **Measurement temperature** 参数指定提取其他器件参数时的温度 *Tm1*。**Temperature Dependence** 设置提供仿真温度 *Ts* 以及其他器件参数的温度缩放系数。有关更多信息，请参见温度依赖性（基于表面电势的建模选项）。

### 故障

要对 P-Channel MOSFET 模块中的故障建模，请在 **Faults** 部分中，单击要建模故障旁边的 **Add fault**。有关故障建模的更多信息，请参见故障行为建模和故障触发。

P-Channel MOSFET 模块对五种类型的故障建模：

- `Open circuit` — 由金属化烧毁导致的故障
- `Drain-source short` — 由漏源沟道雪崩击穿导致的故障
- `Drain-bulk short or source-bulk short` — 由漏体或源体沟道雪崩击穿导致的故障
- `Gate oxide short` — 栅氧化层介质层故障
- `Parameter shift` — 由老化导致的故障

该模块可以在特定时间触发故障事件，或者当电流或电压超过限值的时间长于特定时间间隔时触发故障事件。

**参数偏移故障**

如果在 **Faults** 设置中将 **Failure mode** 参数设置为 `Parameter shift`，则 MOSFET 因其组件老化而失效。以下方程定义了偏移参数的值：

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

其中 *tth* 是触发故障的时间阈值，*τ* 是 **Fault transition time constant, tau** 参数的值。

**栅氧化层短路故障**

如果在 **Faults** 设置中将 **Failure mode** 参数设置为 `Gate oxide short`，则栅氧化层介质层失效。这些图显示了未故障和故障状态下三端子 MOSFET 的等效电路：

这些图显示了未故障和故障状态下四端子 MOSFET 的等效电路：

### 热端口

该模块有一个可选热端口，默认隐藏。要显示热端口，请将 **Modeling option** 参数设置为：

- `Threshold-based with thermal` — 基于阈值电压并显示热端口的模型
- `Surface-potential-based with thermal` — 基于表面电势并显示热端口的模型

此操作会在模块图标上显示热端口 **H**，并显示 **Thermal Port** 参数。

使用热端口可仿真产生的热量和器件温度的影响。有关使用热端口以及 **Thermal Port** 参数的更多信息，请参见仿真半导体中的热效应。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参见设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参见按标称值进行系统缩放。

下表显示了模块的电容与初始目标之间的关系：

| 定义的电容 | 初始目标 |
| --- | --- |
| 栅射电容，*Cge* | 仅设置栅射电容电压的初始目标。将集射电容电压的初始目标设置为 `0` 或将其优先级设置为 `None`。 |
| 集射电容，*Cce* | 仅设置集射电容电压的初始目标。将栅射电容电压的初始目标设置为 `0` 或将其优先级设置为 `None`。 |
| 栅集电容，*Cgc* | 通过对栅射和集射电压施加约束来设置栅集电压的初始目标。栅集电容电压的初始条件等于栅射与集射之间的电压。 |
| 栅射电容，*Cge* 和栅集电容，*Cgc* | 通过对栅射和集射电压施加约束来设置栅射和栅集电压的初始目标。栅集电容电压的初始条件等于栅射与集射之间的电压。 |
| 栅射电容，*Cge* 和集射电容，*Cce* | 设置栅射和集射电容的初始目标。 |
| 栅集电容，*Cgc* 和集射电容，*Cce* | 通过对栅射和集射电压施加约束来设置栅集和集射电压的初始目标。栅集电容电压的初始条件等于栅射与集射之间的电压。 |
| 栅射电容，*Cge*、栅集电容，*Cgc* 和集射电容，*Cce* | 通过对栅射和集射电压施加约束来设置栅射、栅集和集射电容的初始目标。栅集电容电压的初始条件等于栅射与集射之间的电压。 |

**注意**

在您的模型内部，**Priority** 等于 `Low` 或 `High` 的初始目标数量必须与微分变量数量匹配。微分变量来自模型中的电感和电容。

### 绘制器件特性

无需构建完整模型，即可绘制 P-Channel MOSFET 模块的基本 I-V 特性。使用这些图来探究参数选择对器件特性的影响。如果从数据表对模块进行参数化，则可以将图与数据表进行比较，以检查是否正确地参数化了模块。如果您有一个完整的工作模型但不知道使用哪个制造部件，则可以将图与数据表进行比较，以帮助您决定。

要启用此选项，请将 P-Channel MOSFET 模块的 **Modeling option** 参数设置为 `Threshold Based` 或 `Surface potential based`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参见绘制半导体模块的基本 I-V 特性。

P-Channel MOSFET 模块还支持 **Explore characteristics** 选项。使用此选项可深入研究模块特性，并使模块行为与一组目标特性匹配。要启用此选项，请将该模块的 **Modeling option** 参数设置为 `Surface potential based`。然后，右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Explore characteristics**。有关此选项的更多信息，请参见 MOSFET Characteristics Viewer。
