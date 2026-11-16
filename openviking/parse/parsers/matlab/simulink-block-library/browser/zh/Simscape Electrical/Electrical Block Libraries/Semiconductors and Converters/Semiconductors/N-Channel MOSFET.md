---
type: simulink-block
title: 'N-Channel MOSFET'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'nchannelmosfet'
documentation_source_path: 'ref/nchannelmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Channel MOSFET

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

要启用此端口，请将 **参数化** 设置为 `Four`。

### **H** — 热端口 热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Threshold-based with thermal` 或 `Surface-potential-based with thermal`。

## 参数

### **建模选项** — MOSFET 表示形式 `Threshold-based`（默认） | `Threshold-based with thermal` | `Surface-potential-based` | `Surface-potential-based with thermal`

选择 MOSFET 表示形式：

- `Threshold-based` — 基本模型，使用 Shichman-Hodges 方程（基于阈值电压）表示器件，并且不仿真热效应。这是默认值。
- `Threshold-based with thermal` — 基于阈值电压且暴露热端口的模型。
- `Surface-potential-based` — 基于表面电势的模型。此模型不仿真热效应。
- `Surface-potential-based with thermal` — 基于表面电势模型的热建模选项。

### 主要（基于阈值的建模选项）

**主要**参数的此配置对应于基于阈值的模块建模选项，这是默认值。如果您使用的是该模块基于表面电势的建模选项，请参阅主要（基于表面电势的建模选项）。

### **端子数量** — 端子参数化 `Three`（默认） | `Four`

模块的端子数量。

### **参数化** — 模块参数化 `Specify from a datasheet`（默认） | `Specify using equation parameters directly` | `Lookup table (2-D, temperature independent)` | `Lookup table (3-D, temperature dependent)`

选择以下模块参数化方法之一：

- `Specify from a datasheet` — 提供漏源导通电阻以及对应的漏极电流和栅源电压。模块根据此信息计算 Shichman 和 Hodges 方程的晶体管增益。
- `Specify using equation parameters directly` — 提供晶体管增益。
- `Lookup table (2-D, temperature independent)` — 使用二维查表将漏源电流表示为栅源电压和漏源电压的函数。
- `Lookup table (3-D, temperature dependent)` — 使用三维查表将漏源电流表示为栅源电压、漏源电压和温度的函数。

### **漏源导通电阻，R\_DS(on)** — 漏源导通电阻 `0.025` `Ohm`（默认）

在指定的漏极电流和栅源电压值下，漏源电压与漏极电流之比。*RDS(on)* 应为正值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify from a datasheet`。

### **用于 R\_DS(on) 的漏极电流，Ids** — 漏极电流 `6``A`（默认）

模块用于计算漏源电阻值的漏极电流。*IDS* 应为正值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify from a datasheet`。

### **用于 R\_DS(on) 的栅源电压，Vgs** — 栅源电压，Vgs `10` `V`（默认）

模块用于计算漏源电阻值的栅源电压。*VGS* 应为正值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify from a datasheet`。

### **增益，K** — 正恒定增益系数 `5.0` `A/V2`（默认）

Shichman 和 Hodges 方程的正恒定增益系数。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify using equation parameters directly`。

### **栅源阈值电压，Vth** — 栅源阈值电压 `1.7` `V`（默认）

Shichman 和 Hodges 方程中的栅源阈值电压 *Vth*。对于增强型器件，*Vth* 应为正值。对于耗尽型器件，*Vth* 应为负值。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Three`，并将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **零体-源电压下的栅源阈值电压，Vth0** — 零体-源电压下的栅源阈值电压 `1.7` `V`（默认）

Shichman 和 Hodges 方程中零体-源电压下的栅源阈值电压 *Vth0*。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **沟道调制，L** — 沟道调制 `0` `1/V`（默认）

沟道长度调制，通常用数学符号 *λ* 表示。在饱和区，它是漏极电流随漏源电压的变化率。对漏极电流的影响通常很小，并且当根据漏源导通电阻 *RDS(on)* 计算晶体管增益 *K* 时会忽略该影响。典型值为 0.02，但在大多数电路仿真中可以忽略该影响。不过，在某些电路中，较小的非零值可能有助于数值收敛。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **第一个非零体-源电压下的栅源阈值电压，Vth1** — 第一个非零体-源电压下的栅源阈值电压 `1.9071` `V`（默认）

Shichman 和 Hodges 方程中第一个非零体-源电压下的栅源阈值电压 *Vth1*。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify from a datasheet`。

### **第一个体-源电压，Vbs1** — 第一个体-源电压 `-1` `V`（默认）

第一个体-源电压，*Vbs1*

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify from a datasheet`。

### **第二个非零体-源电压下的栅源阈值电压，Vth2** — 第二个非零体-源电压下的栅源阈值电压 `2.066` `V`（默认）

Shichman 和 Hodges 方程中第二个非零体-源电压下的栅源阈值电压 *Vth2*。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify from a datasheet`。

### **第二个体-源电压，Vbs2** — 第二个体-源电压 `-2` `V`（默认）

第二个体-源电压，*Vbs2*

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify from a datasheet`。

### **体因子** — 体因子 `0.5` `V^0.50000`（默认）

体因子，*γ*。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify using equation parameters directly`。

### **表面电势** — 表面电势 `0.5` `V`（默认）

表面电势。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Specify using equation parameters directly`。

### **测量温度** — 测量温度 `25` `°C`（默认）

测量 **漏源导通电阻，R\_DS(on)** 时的温度 *Tm1*。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **栅源电压向量，Vgs** — 栅源电压向量 `[-.5, 2, 3, 4, 5]` `V`（默认）

栅源电压向量。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。

### **漏源电压向量，Vds** — 漏源电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V`（默认）

用于查表的漏源电压向量。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。

### **体-源电压向量，Vbs** — 漏源电压向量 `[0, -4, -6, -12]` `V`（默认）

用于查表的体-源电压向量。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。

### **表格化漏源电流，Ids(Vgs,Vds)** — 与温度无关的表格化漏源电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

用于二维查表的漏源电流表格值，表示为栅源电压和漏源电压的函数。矩阵中的每个值指定特定栅源电压和漏源电压组合下的漏源电流。矩阵大小必须与栅源电压和漏源电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Three`，并将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。

### **温度向量，T** — 温度向量 `[25 125]` `degC`（默认）

用于查表的温度向量。向量值必须严格递增。这些值可以是非均匀间隔的。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。

### **表格化漏源电流，Ids(Vgs,Vds,T)** — 与温度相关的表格化漏源电流 `zeros(5, 7, 2)` `A`（默认）

用于三维查表的漏源电流表格值，表示为栅源电压、漏源电压和温度的函数。矩阵中的每个值指定特定栅源电压、漏源电压和温度组合下的漏源电流。矩阵大小必须与栅源电压、漏源电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Three`，并将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。

### **表格化栅源阈值电压，Vth(Vbs)** — 与温度无关的栅源阈值电压向量 `[.4, 1.2, 1.4, 1.45]` `V`（默认）

用于二维查表的栅源阈值电压表格值，表示为体-源电压的函数。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。

### **零体-源电压下的表格化漏源电流，Ids(Vgs,Vds)** — 零体-源电压下与温度无关的表格化漏源电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

用于二维查表的零体-源电压下的漏源电流表格值，表示为栅源电压和漏源电压的函数。矩阵中的每个值指定特定栅源电压和漏源电压组合下的漏源电流。矩阵大小必须与栅源电压和漏源电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。

### **表格化栅源阈值电压，Vth(Vbs,T)** — 与温度相关的栅源阈值电压向量 `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V`（默认）

用于三维查表的栅源阈值电压表格值，表示为体-源电压和温度的函数。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。

### **零体-源电压下的表格化漏源电流，Ids(Vgs,Vds,T)** — 零体-源电压下与温度相关的表格化漏源电流 `zeros(5, 7, 2)` `A`（默认）

用于三维查表的零体-源电压下的漏源电流表格值，表示为栅源电压、漏源电压和温度的函数。矩阵中的每个值指定特定栅源电压、漏源电压和温度组合下的漏源电流。矩阵大小必须与栅源电压、漏源电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **端子数量** 设置为 `Four`，并将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。

### **Ids-Vds 参数化** — Ids-Vds 表数据作为对称数据 `Provide negative and positive Vds data`（默认） | `Provide positive Vds data only`

是否将 Ids-Vds 表数据作为对称数据提供。如果选择 `Provide negative and positive Vds data`，则数据不对称。如果选择 `Provide positive Vds data only`，则模块会旋转并翻转正数据以获得负数据。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。

### 主要（基于表面电势的建模选项）

**主要**设置的此配置对应于基于表面电势的模块建模选项。如果您使用的是该模块基于阈值的建模选项（基于 Shichman-Hodges 方程），请参阅主要（基于阈值的建模选项）。

### **端子数量** — 端子参数化 `Three`（默认） | `Four`

模块的端子数量。

### **增益** — MOSFET 增益 `18` `A/V 2`（默认） | 正标量

MOSFET 增益，*β*。此参数主要定义 *ID*–*VDS* 特性上的线性工作区。

### **平带电压** — 平带电压 `-1.1` `V`（默认）

平带电压 *VFB* 定义必须在硅表面实现平带条件时所施加的栅极偏置。默认值为 `-1.1` V。您还可以使用此参数因材料功函数差异以及俘获界面电荷或氧化物电荷而任意移动阈值电压。不过，在实践中，通常建议先使用 **体因子** 和 **强反型表面电势** 参数修改阈值电压，仅将此参数用于微调。

### **体因子** — 体因子 `3.5` `V1/2`（默认）

表面电势方程中的体因子，*γ*。此参数主要影响阈值电压。

### **强反型表面电势** — 强反型表面电势 `1` `V` (默认)

表面电势方程中的 2*ϕB* 项。
此参数主要还会影响阈值电压。

### **速度饱和因子** — 速度饱和因子 `0.4` `1/V` (默认)

漏极电流方程中的速度饱和 *θsat*。在良好拟合线性工作会导致饱和电流过高的情况下，使用此参数。通过增大此参数值，可降低饱和电流。对于高压器件，通常会出现良好拟合线性工作导致饱和电流过低的情况。在这种情况下，要么增大增益和漏极欧姆电阻，要么改用 N-Channel LDMOS FET 模块。

### **沟道长度调制因子** — 沟道长度调制因子 `0` (默认)

*GΔL* 方程中对数项的乘数因子 α。此参数描述沟道长度调制的开始。对于在饱和区表现出正电导的器件特性，增大参数值以拟合此行为。默认值为 `0`，这意味着默认情况下沟道长度调制为 off。

### **沟道长度调制电压** — 沟道长度调制电压 `5e-2` `V` (默认)

*GΔL* 方程中的电压 *Vp*。此参数控制沟道长度调制开始生效时的漏极电压。

### **表面粗糙度散射因子** — 表面粗糙度散射因子 `0` `1/V` (默认)

迁移率降低的强度。迁移率为 *μ* = *μ0*/*Gmob*，其中 *μ0* 是不受表面散射效应影响的低场迁移率。迁移率降低因子 *Gmob* 由 Gmob=1+(θsrVeff)4 给出，其中 *θsr* 是表面粗糙度散射因子，*Veff* 是表示沟道中有效垂直电场强度 *Eeff* 的电压。对于高垂直电场，电子的迁移率大致与 *Eeff*^2 成正比。

### **线性到饱和过渡系数** — 线性到饱和过渡系数 `8` (默认)

MOSFET 从线性区过渡到饱和区的平滑度，特别是在启用速度饱和时。通常可将此参数保留为默认值，但可以使用它微调 *ID*–*VDS* 特性的拐点。此参数值的预期范围在 2 到 8 之间。

### **测量温度** — 测量温度 `25` `°C` (默认)

测量模块参数时的温度 *Tm1*。如果 **温度相关性** 设置上的 **器件仿真温度** 参数不同于此值，则器件参数将根据仿真温度和参考温度从其定义值进行缩放。有关详细信息，请参阅温度相关性（基于表面电势的建模选项）。

### 欧姆电阻

如果 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`，要启用此设置，请将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **源极欧姆电阻, Rs** — 晶体管源极电阻 `0.0001` `Ohm` (默认) | nonnegative scalar

晶体管源极电阻，即与源极接触相关的串联电阻。基于阈值变体的默认值为 `1e-4` Ohm。基于表面电势变体的默认值为 `2e-3` Ohm。

### **漏极欧姆电阻, Rd** — 晶体管漏极电阻 `0.01` `Ohm` (默认) | nonnegative scalar

晶体管漏极电阻，即与漏极接触相关的串联电阻。该值必须大于或等于 `0`。基于阈值变体的默认值为 `0.01` Ohm。基于表面电势变体的默认值为 `0.17` Ohm。

### **栅极欧姆电阻, Rg** — 晶体管栅极电阻 `8.4` `Ohm` (默认) | nonnegative scalar

晶体管栅极电阻，即与栅极接触相关的串联电阻。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### **体欧姆电阻, Rb** — 晶体管体电阻 `0.001` `Ohm` (默认) | nonnegative scalar

晶体管体电阻，即与体接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **端子数** 设置为 `Four`。
- **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **衬底欧姆电阻** — 晶体管体电阻 `2e-3` `Ohm` (默认) | nonnegative scalar

晶体管体电阻，即与衬底接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **端子数** 设置为 `Four`。
- **建模选项** 设置为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### 封装

### **源极引线电阻** — 晶体管源极引线电阻 `0` `Ohm` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的源极引线电阻，即与源极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **漏极引线电阻** — 晶体管漏极引线电阻 `0` `Ohm` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的漏极引线电阻，即与漏极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **栅极引线电阻** — 晶体管栅极引线电阻 `0` `Ohm` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的栅极引线电阻，即与栅极接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **体引线电阻** — 晶体管体引线电阻 `0` `Ohm` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的体引线电阻，即与体接触相关的串联引线电阻。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请设置：

- **端子数** 设置为 `Four`。
- **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **源极引线电感** — 晶体管源极引线电感 `0` `nH` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的源极引线电感，即与源极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **漏极引线电感** — 晶体管漏极引线电感 `0` `nH` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的漏极引线电感，即与漏极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **栅极引线电感** — 晶体管栅极引线电感 `0` `nH` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的栅极引线电感，即与栅极接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **体引线电感** — 晶体管体引线电感 `0` `nH` (默认) | nonnegative scalar

*自 R2024b 起*

晶体管的体引线电感，即与体接触相关的串联引线电感。使用此参数对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请设置：

- **端子数** 设置为 `Four`。
- **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### 电容

要启用此设置，请将 **建模选项** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **参数化** — 电容参数化 `Specify fixed input, reverse transfer, and output capacitance` (默认) | `Specify fixed gate-source, gate-drain, and drain-source capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-source, gate-drain, and drain-source capacitance`

选择以下方法之一进行电容参数化：

- `Specify fixed input, reverse transfer, and output capacitance` — 提供来自数据手册的固定参数值，并让模块将输入电容、输出电容和反向传输电容值转换为电容值，如基于阈值建模选项的电荷模型中所述。
- `Specify fixed gate-source, gate-drain, and drain-source capacitance` — 直接提供电容参数的固定值。
- `Specify tabulated input, reverse transfer, and output capacitance` — 提供基于数据手册曲线的表格化电容和漏源电压值。模块将输入电容、输出电容和反向传输电容值转换为电容值，如基于阈值建模选项的电荷模型中所述。
- `Specify tabulated gate-source, gate-drain, and drain-source capacitance` — 提供电容和漏源电压的表格化值。

### **输入电容, Ciss** — 输入栅源电容 `350` `pF` (默认)

当漏极短接到源极时的栅源电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **输入电容, Ciss(Vds)** — 具有表格化输入的输入栅源电容 `[720 700 590 470 390 310]` `pF` (默认)

当漏极短接到源极时的栅源电容，按漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **反向传输电容, Crss** — 反向传输电容 `80` `pF` (默认)

源极接地时的漏栅电容，也称为米勒电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **反向传输电容, Crss(Vds)** — 具有表格化输入的反向传输电容 `[450 400 300 190 95 55]` `pF` (默认)

源极接地时的漏栅电容，也称为米勒电容，按漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **输出电容, Coss** — 输出电容 `0` `pF` (默认)

栅极和源极短接时的漏源电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **输出电容, Coss(Vds)** — 具有表格化输入的输出电容 `[900 810 690 420 270 170]` `pF` (默认)

栅极和源极短接时的漏源电容，按漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **栅源电容, Cgs** — 栅源电容 `270` `pF` (默认)

放置在栅极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **栅源电容, Cgs(Vgs, Vds)** — 具有表格化值的栅源电容 `[270 300 290 280 295 255]` `pF` (默认)

放置在栅极和源极之间的电容，按栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **栅漏电容, Cgd** — 栅漏电容 `80` `pF` (默认)

放置在栅极和漏极之间的电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **栅漏电容, Cgd(Vgs,Vds)** — 具有表格化值的栅漏电容 `[450 400 300 190 95 55]` `pF` (默认)

放置在栅极和漏极之间的电容，按栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **栅极-衬底电容, Cgb** — 栅极-衬底电容 `0` `pF` (默认)

放置在栅极和衬底之间的电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`，并将 **栅极-衬底和栅极-源极电荷-电压线性度** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **栅极-衬底电容, Cgb(Vgs,Vds)** — 具有表格化值的栅极-衬底电容 `[450 400 300 190 95 55]` `pF` (默认)

放置在栅极和衬底之间的电容，按栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`，并将 **栅极-衬底和栅极-源极电荷-电压线性度** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **对应栅源电压, Vgs** — 对应栅源电压 `0` `V` (默认)

与表格化电容值对应的栅源电压。

如果此值为 scalar，则 **栅源电容, Cgs(Vgs,Vds)** 和 **栅漏电容, Cgd(Vgs,Vds)** 是 scalars 的向量。如果此值为 vector，则 **栅源电容, Cgs(Vgs,Vds)** 和 **栅漏电容, Cgd(Vgs,Vds)** 是 scalars 的矩阵。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **漏源电容, Cds** — 漏源电容 `0` `pF` (默认)

放置在漏极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **漏源电容, Cds(vds)** — 具有表格化值的漏源电容 `[450 410 390 230 175 115]` `pF` (默认)

放置在漏极和源极之间的电容，按漏源电压表格化。

#### 依赖项

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`。

### **对应的漏源电压, Vds** — 对应的漏源电压 `[.1, .3, 1, 3, 10, 30]` `V` (default)

与表格化电容值对应的漏源电压。

#### 依赖项

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse
transfer, and output capacitance` 或 `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`。

### **用于表格化电容的栅源电压, Vgs** — 用于表格化电容的栅源电压 `0` `V` (default)

对于表格化电容模型，此参数控制 **反向传输电容, Crss** 或 **栅漏电容, Cgd** 参数（取决于所选的参数化选项）的电压依赖性。这些电容是漏栅电压的函数。该模块通过从 **对应的漏源电压** 参数指定的值中减去此栅源电压值来计算漏栅电压。

#### 依赖项

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse
transfer, and output capacitance`。

### **栅漏电荷-电压线性度** — 电荷-电压线性度 `Gate-drain capacitance is constant` (default) | `Gate-drain charge function is nonlinear`

这两个固定电容选项允许您将栅极电容建模为固定的栅源电容 *CGS* 以及固定的或非线性的栅漏电容 *CGD*。选择栅漏电容是固定的还是非线性的：

- `Gate-drain capacitance is constant` — 电容值为常数，并根据所选的参数化选项定义，可以直接定义或从数据手册推导。
- `Gate-drain charge function is nonlinear` — 栅漏电荷关系根据基于阈值的建模选项的电荷模型中描述的分段非线性函数定义。将出现两个附加参数，供您定义栅漏电荷函数。

#### 依赖项

要启用此参数，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer
and output capacitance` 或 `Specify fixed gate-source,
gate-drain and drain-source capacitance`。

### **栅漏氧化层电容** — 栅漏氧化层电容 `200` `pF` (default)

当漏栅电压小于 **氧化层电容开始生效时的漏栅电压** 参数值时，为栅漏电容。

#### 依赖项

要启用此参数，请将 **栅漏电荷-电压线性度** 设置为 `Gate-drain charge function is nonlinear`。

### **氧化层电容开始生效时的漏栅电压** — 氧化层电容开始生效时的漏栅电压 `-0.5` `V` (default)

漏栅电容在关断状态 (*CGD*) 和导通状态 (*Cox*) 电容值之间切换时的漏栅电压。

#### 依赖项

要启用此参数，请将 **栅漏电荷-电压线性度** 设置为 `Gate-drain charge function is nonlinear`。

### **栅极-体极和栅源电荷-电压线性度** — 栅极-体极和栅源电荷-电压线性度 `Gate-bulk and gate-source capacitance change instantly` (default) | `Gate-bulk and gate-source capacitance change gradually` | `Separate gate-bulk and gate-source capacitance`

栅极-体极和栅源电荷-电压线性度。

#### 依赖项

要启用此参数，请在 **主** 设置中，将 **端子数量** 设置为 `Four`。

要启用 `Separate gate-bulk and gate-source capacitance`
选项，请在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed gate-source,
gate-drain, and drain-source capacitance` 或 `Specify tabulated
gate-source, gate-drain, and drain-source capacitance`

### 沟道电容

要启用此设置，请将 **建模选项** 设置为 `Surface-potential-based` 或 `Surface-potential-based with
thermal`。

### **氧化层电容** — 氧化层电容 `1500` `pF` (default)

平行板栅极-沟道电容。

### **栅源重叠电容** — 栅源重叠电容 `100` `pF` (default)

与栅电极和源极阱重叠相关的固定线性电容。

### **栅漏重叠电容** — 栅漏重叠电容 `14` `pF` (default)

与栅电极和漏极阱重叠相关的固定线性电容。

### 体二极管

### **体二极管建模** — 体二极管建模选项 `No` (default) | `Exponential` | `Tabulated I-V curve`

是否对体二极管建模。

### **表格类型** — 表格化函数 `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

是将电流表格化为温度和电压的函数，还是将电压表格化为温度和电流的函数。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Tabulated I-V curve`。

### **反向饱和电流, Is** — 反向饱和电流 `0` `A` (default)

体二极管方程中由 *Is* 符号表示的电流。基于阈值的建模选项的默认值为 `0` A。基于表面电势的建模选项的默认值为 `5.2e-13` A。

为使体二极管能够导通，对于 MOSFET 电流在仿真期间改变符号的应用（例如 MOSFET 驱动感性负载时），请将此参数设置为非零值。

对于 MOSFET 电流从不变号的应用（例如小信号放大器），请将此参数设置为 0 以提高仿真速度。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`。

### **内建电压, Vbi** — 内建电压 `0.6` `V` (default)

二极管的内建电压，在体二极管方程中由 *Vbi* 符号表示。内建电压仅影响结电容方程。它不影响传导电流。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`。

### **理想因子, n** — 理想因子 `1` (default)

体二极管方程中由 *n* 符号表示的因子。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`。

### **零偏结电容, Cj0** — 零偏结电容 `0` `pF` (default)

仅由体二极管引起的、零偏时漏极和体极接触之间的电容。在体二极管方程中由 *Cj0* 符号表示。基于阈值的建模选项的默认值为 `0` pF。基于表面电势的建模选项的默认值为 `480` pF。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`。

### **渡越时间, TT** — 渡越时间 `50e-9` `s` (default)

体二极管方程中由 *τ* 符号表示的时间。

当 **反向饱和电流** 和 **渡越时间** 参数均为非零时，此模块会在体二极管模型内部包含反向恢复。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`。

### **测量温度** — 测量温度 `25` `°C` (default)

测量模块参数时的温度。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Exponential`，并在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature
independent)` 或 `Lookup table (3-D, temperature
dependent)`

### **二极管正向电压, Vf(If)** — 二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V` (default)

使二极管变为正向偏置所需施加的最小电压的表格化值。

#### 依赖项

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet`、`Specify from
  equation parameters directly` 或 `Lookup table (2-D,
  temperature independent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。

    **表格类型** 为 `Table in Vf(If)
    form`。

### **二极管正向电流, If** — 与温度无关的二极管正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

正向电流的表格化值。

#### 依赖项

要启用此参数，请在 **体二极管** 设置中，将 **体二极管建模** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in Vf(If) form` 或
`Table in Vf(Tj,If) form`。

### **二极管正向电流, If(Vf)** — 随正向电压表格化的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A` (default)

作为正向电压函数的正向电流的表格化值。

#### 依赖项

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet`、`Specify from
  equation parameters directly` 或 `Lookup table (2-D,
  temperature independent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。

    **表格类型** 为 `Table in If(Vf)
    form`。

### **二极管正向电压, Vf** — 与温度无关的二极管正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

正向电压的表格化值。

#### 依赖项

要启用此参数，请在 **体二极管** 设置中，将 **体二极管建模** 设置为 `Tabulated I-V curve`，并将 **表格类型** 设置为 `Table in If(Vf) form` 或
`Table in If(Tj,Vf) form`。

### **二极管结温, Tj** — 二极管结温 `[25, 125]` `degC` (default)

结温向量。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Tabulated I-V curve`，并在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D,
temperature dependent)`。

### **二极管正向电流, If(Tj,Vf)** — 与温度相关的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default)

作为正向电压和结温函数的正向电流的表格化值。

#### 依赖项

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。

    **表格类型** 为 `Table in If(Tj,Vf)
    form`。

### **二极管正向电压, If(Tj,Vf)** — 与温度相关的二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default)

作为正向电流和结温函数的正向电压的表格化值。

#### 依赖项

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。
- 在 **体二极管** 设置中，设置：

  - **体二极管建模** 为 `Tabulated I-V
    curve`。

    **表格类型** 为 `Table in Vf(Tj,If)
    form`。

### **二极管关断电导** — 二极管反向偏置时的电导 `1e-12` `1/Ohm` (default) | positive scalar

*自 R2024a 起*

二极管反向偏置时的电导。

#### 依赖项

要启用此参数，请将 **体二极管建模** 设置为 `Tabulated I-V curve`。

### 温度依赖性（基于阈值的建模选项）

**温度依赖性** 设置的此配置对应于基于阈值的模块建模选项，这是默认选项。如果您使用的是该模块的基于表面电势的建模选项，请参阅温度依赖性（基于表面电势的建模选项）

### **参数化** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature` — 不建模温度依赖性。这是默认方法。
- `Model temperature dependence` — 建模温度相关效应。提供仿真温度 *Ts* 的值、*BEX* 的值以及测量温度 *Tm1* 的值（使用 **主** 设置中的 **测量温度** 参数）。您还必须根据 **主** 设置中 **参数化** 参数的值，使用两种方法之一提供 *α* 的值。如果从数据手册对模块进行参数化，则必须在第二测量温度下提供 *RDS(on)*，模块将据此计算 *α*。如果通过指定方程参数进行参数化，则必须直接提供 *α* 的值。

### **第二测量温度下的漏源导通电阻, R\_DS(on)** — 第二测量温度下的漏源导通电阻 `0.037` `Ohm` (default)

在第二测量温度下，对于指定的漏极电流和栅源电压值，漏源电压与漏极电流的比值。它必须与 **主** 设置中的 **漏源导通电阻, R\_DS(on)** 参数针对相同工作点（漏极电流和栅源电压）引用。

#### 依赖项

仅当您在 **主** 设置中为 **参数化** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **第二测量温度** — 第二温度 `125` `°C` (default)

测量 **第二测量温度下的漏源导通电阻, R\_DS(on)** 时的第二温度 *Tm2*。

#### 依赖项

仅当您在 **主** 设置中为 **参数化** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **栅极阈值电压温度系数, dVth/dT** — 栅源电压, Vgs `-6` `mV/K` (default)

栅极阈值电压随温度的变化率。

#### 依赖项

仅当您在 **主** 设置中为 **参数化** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **迁移率温度指数, BEX** — 迁移率温度指数 `-1.5` (default)

迁移率温度系数值。大多数 MOSFET 可以使用默认值。有关其他注意事项，请参阅假设和限制部分。

### **体二极管反向饱和电流温度指数** — 体二极管反向饱和电流温度指数 `3` (default)

假设体二极管的反向饱和电流与固有载流子浓度的平方成正比，*ni* =
*NC*
exp(–*EG*/2*kB**T*)。*NC* 是随温度变化的有效态密度，*EG* 是半导体材料随温度变化的带隙。为避免引入另一个温度缩放参数，该模块忽略带隙的温度依赖性，并对所有器件类型使用硅在 300K 时的带隙 (1.12eV)。因此，经过温度缩放的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **体二极管** 设置中 **反向饱和电流** 参数的值，*kB* 是玻尔兹曼常数
(8.617x10-5eV/K)，*ηIs* 是 **体二极管反向饱和电流温度指数**。默认值为 `3`，因为硅的 *NC* 大致与 *T3/2* 成正比。您可以通过对 *ηIs* 进行实用选择来弥补忽略带隙温度依赖性的影响。

### **器件仿真温度** — 器件仿真温度 `25` `°C` (default)

仿真器件时的温度 *Ts*。

### Temperature Dependence (Surface-Potential-Based Modeling Option)

**Temperature Dependence** 设置的此配置对应于基于表面电势的模块建模选项。如果您使用的是该模块的基于阈值的建模选项，请参见 Temperature Dependence (Threshold-Based Modeling Option)

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement
  temperature` — 不对温度依赖性建模。
- `Model temperature dependence` — 对温度相关效应建模。为器件仿真温度 *Ts* 以及其他模块参数的温度缩放系数提供值。

### **Gain temperature exponent** — 增益温度指数 `1.3` (default)

假设 MOSFET 增益 *β* 随温度按指数规律缩放，*β* = *β*m1(*Tm1*/*Ts*)^*ηβ*。*βm1* 是 **Main** 设置中 **Gain** 参数的值，*ηβ* 是 **Gain temperature exponent**。

### **Flatband voltage temperature coefficient** — 平带电压温度系数 `5e-4` `V/K` (default)

假设平带电压 *V*FB 随温度线性缩放，*V*FB = *VFBm1* + (*Ts* – *Tm1*)*ST,VFB*。*VFBm1* 是 **Main** 设置中 **Flatband voltage** 参数的值，*ST,VFB* 是 **Flatband voltage temperature coefficient**。

### **Surface potential at strong inversion temperature coefficient** — 强反型表面电势温度系数 `-8.5e-4` `V/K` (default)

假设强反型表面电势 2*ϕB* 随温度线性缩放，*2ϕB* = 2*ϕBm1* + (*Ts* – *Tm1*)*ST,ϕB*。2*ϕBm1* 是 **Main** 设置中 **Surface potential at strong inversion** 参数的值，*ST,ϕB* 是 **Surface potential at strong inversion temperature coefficient**。

### **Velocity saturation temperature exponent** — 速度饱和温度指数 `1.04` (default)

假设速度饱和 *θsat* 随温度按指数规律缩放，*θsat* = *θsat,m1* (*Tm1*/*Ts*)^*ηθ*。*θsat,m1* 是 **Main** 设置中 **Velocity saturation factor** 参数的值，*ηθ* 是 **Velocity saturation temperature exponent**。

### **Surface roughness scattering temperature exponent** — 表面粗糙度散射温度指数 `0.65` (default)

此参数导致高栅极电压下 MOSFET 跨导随温度降低。假设表面粗糙度散射 *θsr* 随温度按指数规律缩放，*θsr* = *θsr,m1* (*Tm1*/*Ts*)^*ηsr*。*θsr,m1* 是 **Main** 设置中 **Surface roughness scattering factor** 参数的值，*ηsr* 是 **Surface roughness scattering temperature exponent**。

### **Resistance temperature exponent** — 电阻温度指数 `0.95` (default)

假设串联电阻对应于半导体电阻。因此，它们随温度升高按指数规律减小。*Ri* = *Ri,m1* (*Tm1*/*Ts*)^*ηR*，其中 *i* 分别为 S、D 或 G，对应源极、漏极或栅极串联电阻。*Ri,m1* 是 **Ohmic Resistance** 设置中相应串联电阻参数的值，*ηR* 是 **Resistance temperature exponent**。

### **Body diode reverse saturation current temperature exponent** — 体二极管反向饱和电流温度指数 `3` (default)

假设体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* = *NC* exp(–*EG*/2*kB**T*)。*NC* 是随温度变化的有效状态密度，*EG* 是半导体材料随温度变化的带隙。为避免引入另一个温度缩放参数，模块忽略带隙的温度依赖性，并对所有器件类型使用硅在 300K 时的带隙 (1.12eV)。因此，温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **Body Diode** 设置中 **Reverse saturation current** 参数的值，*kB* 是玻尔兹曼常数 (8.617x10-5eV/K)，*ηIs* 是 **Body diode reverse saturation current temperature exponent**。默认值为 `3`，因为硅的 *N*C 大致与 *T3/2* 成正比。您可以通过对 *ηIs* 进行实用选择来弥补忽略带隙温度依赖性的影响。

### **Device simulation temperature** — 器件仿真温度 `25` `°C` (default)

器件仿真的温度 *Ts*。

### Faults

故障界面包括 **Fault Inspector** 窗口和支持故障的模块的 **Blocks** 选项卡中的 **Faults** 部分。您定义触发故障的条件以及触发发生时故障的行为。创建和编辑故障时，您需要参数化故障行为。

要添加故障，请点击 **Add fault** 超链接。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接而不是 **Add fault** 超链接。有关如何包含故障的示例，请参见 Analyze a DC Armature Winding Fault。

### **NMOS fault** — 添加故障的选项 `Add fault` (default)

在 N-Channel MOSFET 模块中添加故障的选项。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s` (default) | nonnegative scalar

模块进入故障状态的仿真时间。

#### Dependencies

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible gate-source voltage** — 故障转换的栅源电压阈值 `inf` `V` (default) | positive scalar

最大允许栅源电压值，超过该值可能触发故障。

#### Dependencies

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible drain-source voltage** — 故障转换的漏源电压阈值 `inf` `V` (default) | positive scalar

最大允许漏源电压值，超过该值可能触发故障。

#### Dependencies

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible drain-bulk voltage** — 故障转换的漏体电压阈值 `inf` `V` (default) | positive scalar

最大允许漏体电压值，超过该值可能触发故障。

#### Dependencies

要启用此参数：

- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。
- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Maximum permissible drain-source current** — 故障转换的电流阈值 `inf` `A` (default) | positive scalar

最大允许漏源电流值。如果电流超过该值的时间长于 **Time to fail when exceeding drain-source current** 参数的值，则模块进入故障状态。

#### Dependencies

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding drain-source current** — 超过漏源电流时失效的时间 `1` `s` (default) | positive scalar

在触发行失效故障之前，漏源电流必须持续超过最大允许漏源电流的时间量。

#### Dependencies

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible body diode current** — 故障转换的体二极管电流阈值 `inf` `A` (default) | positive scalar

最大允许体二极管电流值。如果电流超过该值的时间长于 **Time to fail when exceeding body diode current** 参数的值，则模块进入故障状态。

#### Dependencies

要启用此参数：

- 将 **Model body diode** 设置为 `Exponential` 或 `Tabulated I-V curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Time to fail when exceeding body diode current** — 超过体二极管电流时失效的时间 `1` `s` (default) | positive scalar

在触发行失效故障之前，体二极管电流必须持续超过最大允许体二极管电流的时间量。

#### Dependencies

要启用此参数：

- 将 **Model body diode** 设置为 `Exponential` 或 `Tabulated I-V curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Maximum diode recovery, dV/dt** — 最大二极管恢复 `inf` `V/s` (default) | positive scalar

每秒的最大二极管恢复量。

#### Dependencies

要启用此参数：

- 将 **Model body diode** 设置为 `Exponential` 或 `Tabulated I-V curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Maximum permissible temperature** — 故障转换的温度阈值 `inf` `K` (default) | positive scalar

最大允许温度值。如果温度超过该值的时间长于 **Time to fail when exceeding temperature** 参数的值，则模块进入故障状态。

#### Dependencies

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Time to fail when exceeding temperature** — 超过温度时失效的时间 `1` `s` (default) | positive scalar

在触发行失效故障之前，温度必须持续超过最大允许温度的时间量。

#### Dependencies

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为 `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger** 部分中。有关更多信息，请参见 Set Fault Triggers。

### **Fault transition time constant, tau** — 故障转换时间常数 `1e-3` `s` (default)

转换到故障状态的时间常数。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。

### **Failure mode** — 故障类别 `Open circuit` (default) | `Drain-source short` | `Drain-bulk short or source-bulk short` | `Gate oxide short` | `Parameter shift`

故障类型。您可以将此参数设置为：

- `Open circuit` — 由于金属化烧毁导致的故障。
- `Drain-source short` — 由于漏源沟道雪崩击穿导致的故障。
- `Drain-bulk short or source-bulk short` — 由于漏体或源体沟道雪崩击穿导致的故障。
- `Gate oxide short` — 栅氧化层介电层故障。
- `Parameter shift` — 由于老化导致的故障。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。

要启用 `Drain-source short` 选项，请在 **Main** 设置中将 **Number of terminals** 设置为 `Three`。

要启用 `Drain-bulk short or source-bulk short` 选项，请在 **Main** 设置中将 **Number of terminals** 设置为 `Four`。

### **Faulted series gate resistance, Rg** — 故障态串联栅极电阻 `1e6` `Ohm` (default)

故障状态下的串联栅极电阻。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open circuit`。

### **Faulted series drain resistance, Rd** — 故障态串联漏极电阻 `1000` `Ohm` (default)

故障状态下的串联漏极电阻。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open circuit`。

### **Faulted series source resistance, Rs** — 故障态串联源极电阻 `1000` `Ohm` (default)

故障状态下的串联源极电阻。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open circuit`。

### **Faulted series bulk resistance, Rb** — 故障态串联源极电阻 `1000` `Ohm` (default)

故障状态下的串联源极电阻。

#### Dependencies

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`。

### **Faulted parallel drain-source conductance, Gds** — 故障态并联漏源电导 `1000` `1/Ohm` (default)

故障状态下的并联漏源电导。

#### Dependencies

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Three`。
- 点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-source short`。

### **Faulted parallel drain-bulk conductance, Gdb** — 故障态并联漏体电导 `1000` `1/Ohm` (default)

故障状态下的并联漏体电导。

#### Dependencies

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-bulk short or source-bulk short`。

### **Faulted parallel source-bulk conductance, Gsb** — 故障态并联源体电导 `1000` `1/Ohm` (default)

故障状态下的并联源体电导。

#### Dependencies

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-bulk short or source-bulk short`。

### **Location of fault node (percentage of total channel length from source)** — 故障节点位置 `0` (default)

故障节点的位置，以距源极的总沟道长度百分比表示。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Gate oxide short`。

### **Gate oxide short conductance, G** — 栅氧化层短路电导 `1000` `1/Ohm` (default)

栅氧化层短路电导。

#### Dependencies

要启用此参数，请点击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Gate oxide short`。

### **对栅氧化层短路二极管建模** — 对栅氧化层短路二极管建模的选项 `No` (默认) | `Yes`

是否对栅氧化层短路二极管建模。

#### 依赖关系

要启用此参数，请通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障，并将 **失效模式** 设置为 `Gate oxide short`。

### **栅氧化层短路二极管反向饱和电流，Is** — 栅氧化层短路二极管的反向饱和电流 `0` `A` (默认)

栅氧化层短路二极管的反向饱和电流。

#### 依赖关系

要启用此参数：

- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Gate oxide short`。
- 将 **对栅氧化层短路二极管建模** 设置为 `Yes`。

### **栅氧化层短路二极管内建电压，Vbi** — 栅氧化层短路二极管的内建电压 `0.6` `V` (默认)

栅氧化层短路二极管的内建电压。

#### 依赖关系

要启用此参数：

- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Gate oxide short`。
- 将 **对栅氧化层短路二极管建模** 设置为 `Yes`。

### **栅氧化层短路二极管理想因子，n** — 栅氧化层短路二极管的理想因子 `1` (默认)

栅氧化层短路二极管的理想因子。

#### 依赖关系

要启用此参数：

- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Gate oxide short`。
- 将 **对栅氧化层短路二极管建模** 设置为 `Yes`。

### **栅氧化层短路二极管零偏结电容，Cj0** — 栅氧化层短路二极管的零偏结电容 `0` `pF` (默认)

栅氧化层短路二极管的零偏结电容。

#### 依赖关系

要启用此参数：

- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Gate oxide short`。
- 将 **对栅氧化层短路二极管建模** 设置为 `Yes`。

### **栅氧化层短路二极管渡越时间，TT** — 栅氧化层短路二极管的渡越时间 `50e-9` `s` (默认)

栅氧化层短路二极管的渡越时间。

#### 依赖关系

要启用此参数：

- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Gate oxide short`。
- 将 **对栅氧化层短路二极管建模** 设置为 `Yes`。

### **偏移后的增益占未偏移增益的百分比** — 偏移后的增益占未偏移增益的百分比 `100` (默认)

偏移后的增益占未偏移增益的百分比。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **阈值电压偏移值，dVth** — 阈值电压偏移值 `0` `V` (默认)

阈值电压的偏移值。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的沟道调制，L** — 故障状态下的沟道调制 `0` `1/V` (默认)

故障状态下的沟道调制。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **偏移后的体因子占未偏移体因子的百分比** — 偏移后的体因子占未偏移体因子的百分比 `100` (默认)

偏移后的体因子占未偏移体因子的百分比。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **表面电势偏移值，dPhib** — 表面电势偏移值 `0` `V` (默认)

表面电势的偏移值。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的源极欧姆电阻，Rs** — 故障状态下的源极欧姆电阻 `0.0001` `Ohm` (默认)

故障状态下的晶体管源极电阻。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的漏极欧姆电阻，Rd** — 故障状态下的漏极欧姆电阻 `0.01` `Ohm` (默认)

故障状态下的晶体管漏极电阻。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的体极欧姆电阻，Rb** — 故障状态下的体极欧姆电阻 `0.001` `Ohm` (默认)

故障状态下的晶体管体极电阻。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的栅源电压向量，Vgs** — 故障状态下的栅源电压向量 `[-.5, 2, 3, 4, 5]` `V` (默认)

故障状态下的栅源电压。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的漏源电压向量，Vds** — 故障状态下的漏源电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V` (默认)

故障状态下的漏源电压。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的衬底-源电压向量，Vbs** — 故障状态下的衬底-源电压向量 `[0, -4, -6, -12]` `V` (默认)

故障状态下的衬底-源电压。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下表格化的栅源阈值电压，Vth(Vbs)** — 故障状态下表格化的栅源阈值电压 `[.4, 1.2, 1.4, 1.45]` `V` (默认)

故障状态下的表格化栅源阈值电压。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下表格化的栅源阈值电压，Vth(Vbs,T)** — 故障状态下依赖于温度的表格化栅源阈值电压 `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V` (默认)

故障状态下的栅源阈值电压，按衬底-源电压和温度制表。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下表格化的漏源电流，Ids(Vgs,Vds)** — 故障状态下表格化的漏源电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (默认)

故障状态下的表格化漏源电流。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Three`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下表格化的漏源电流，Ids(Vgs,Vds,T)** — 故障状态下依赖于温度的表格化漏源电流 `zeros(5, 7, 2)` `A` (默认)

故障状态下的漏源电流，按栅源电压、漏源电压和温度制表。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Three`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **零衬底-源电压下故障状态表格化的漏源电流，Ids(Vgs,Vds)** — 零衬底-源电压下故障状态表格化的漏源电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A` (默认)

故障状态下的表格化漏源电流，当衬底-源电压为零时。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **零衬底-源电压下故障状态表格化的漏源电流，Ids(Vgs,Vds,T)** — 零衬底-源电压下故障状态依赖于温度的表格化漏源电流 `zeros(5, 7, 2)` `A` (默认)

故障状态下的表格化漏源电流，当衬底-源电压为零时，按栅源电压、漏源电压和温度制表。

#### 依赖关系

要启用此参数：

- 在 **主** 设置中，将 **端子数量** 设置为 `Four`。
- 在 **主** 设置中，将 **参数化** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Parameter shift`。

### **故障状态下的栅源电容占未故障电容的百分比** — 故障状态下的栅源电容占未故障电容的百分比 `100` (默认)

故障状态下的栅源电容占未故障电容的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **故障状态下的栅漏电容占未故障电容的百分比** — 故障状态下的栅漏电容占未故障电容的百分比 `100` (默认)

故障状态下的栅漏电容占未故障电容的百分比。

#### 依赖关系

要启用此参数，请满足以下条件组之一：

**条件组一**

- 在 **电容** 设置中，将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。

**条件组二**

- 在 **电容** 设置中，将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **失效模式** 设置为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **故障状态下的栅体电容占未故障电容的百分比** — 故障状态下的栅体电容占未故障电容的百分比 `100` (默认)

故障状态下的栅体电容占未故障电容的百分比。

#### 依赖关系

要启用此参数，请满足以下条件集之一：

**条件集一**

- 在 **主** 设置中，将 **端子数量**
  设为 `Four`。
- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **栅-体与栅-源电荷-电压线性** 为 `Separate gate-bulk and gate-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **主** 设置中，将 **端子数量**
  设为 `Four`。
- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **栅-体与栅-源电荷-电压线性** 为 `Separate gate-bulk and gate-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Open circuit`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **故障状态下的漏源电容占未故障状态的百分比** — 故障状态下的漏源电容占未故障状态的百分比 `100`（默认）

故障状态下的漏源电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件集之一：

**条件集一**

- 在 **电容** 设置中，将 **参数化** 设为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **故障状态下的栅漏氧化层电容占未故障状态的百分比** — 故障状态下的栅漏氧化层电容占未故障状态的百分比 `100`（默认）

故障状态下的栅漏氧化层电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **栅漏电荷-电压线性** 为 `Gate-drain charge function is non linear`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的漏栅电压，在该电压下氧化层电容变为有效** — 故障状态下的漏栅电压，在该电压下氧化层电容变为有效 `-0.5` `V`（默认）

故障状态下的漏栅电压，在该电压下氧化层电容变为有效。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **栅漏电荷-电压线性** 为 `Gate-drain charge function is non linear`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的输入电容，Ciss(Vds)** — 故障状态下的输入电容 `[720, 700, 590, 470, 390, 310]` `pF`（默认）

故障状态下的输入电容。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的反向传输电容，Crss(Vds)** — 故障状态下的反向传输电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认）

故障状态下的反向传输电容。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的输出电容，Coss(Vds)** — 故障状态下的输出电容 `[900, 810, 690, 420, 270, 170]` `pF`（默认）

故障状态下的输出电容。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的对应漏源电压，Vds** — 故障状态下的对应漏源电压 `[.1, .3, 1, 3, 10, 30]` `V`（默认）

故障状态下的对应漏源电压。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **用于表格化电容的故障状态栅源电压，Vgs** — 用于表格化电容的故障状态栅源电压 `0` `V`（默认）

用于表格化电容的栅源电压，处于故障状态。

#### 依赖关系

要启用此参数，请满足以下条件集之一：

**条件集一**

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

**条件集二**

- 在 **主** 设置中，将 **端子数量** 设为 `Four`。
- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **栅-体与栅-源电荷-电压线性** 为 `Gate-bulk and gate-source capacitance change instantly` 或 `Gate-bulk and gate-source capacitance change gradually`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的栅源电容，Cgs(Vgs,Vds)** — 故障状态下的栅源电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认）

故障状态下的栅源电容，以栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的栅漏电容，Cgd(Vgs,Vds)** — 故障状态下的栅漏电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认）

故障状态下的栅漏电容，以栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，将 **参数化** 设为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的栅体电容，Cgb(Vgs,Vds)** — 故障状态下的栅体电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认）

故障状态下的栅体电容，以栅源电压和漏源电压表格化。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **端子数量** 设为 `Four`。
- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **栅-体与栅-源电荷-电压线性** 为 `Separate gate-bulk and gate-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的对应栅源电压，Vgs** — 故障状态下的对应栅源电压 `0` `V`（默认）

故障状态下的对应栅源电压。

#### 依赖关系

要启用此参数，

- 在 **电容** 设置中，设置：

  - **参数化** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **栅-体与栅-源电荷-电压线性** 为 `Separate gate-bulk and gate-source capacitance`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管反向饱和电流，Is** — 故障状态下的二极管反向饱和电流 `0` `A`（默认）

故障状态下二极管的反向饱和电流。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **对体二极管建模** 设为 `Exponential`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管内建电压，Vbi** — 故障状态下的二极管内建电压 `0.6` `V`（默认）

故障状态下二极管的内建电压。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **对体二极管建模** 设为 `Exponential`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管理想因子，n** — 故障状态下的二极管理想因子 `1`（默认）

故障状态下二极管的理想因子。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **对体二极管建模** 设为 `Exponential`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管零偏结电容占未故障状态的百分比** — 故障状态下的二极管零偏结电容占未故障状态的百分比 `100`（默认）

故障状态下的二极管零偏结电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **对体二极管建模** 设为 `Exponential`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管渡越时间，TT** — 故障状态下的二极管渡越时间 `50e-9` `s`（默认）

故障状态下二极管的渡越时间。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，将 **对体二极管建模** 设为 `Exponential`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电流，If(Vf)** — 故障状态下的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A`（默认）

故障状态下二极管的正向电流，以正向电压表格化。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设为 `Specify from a datasheet`、`Specify using equation parameters directly` 或 `Lookup table (2-D, temperature independent)`。
- 在 **体二极管** 设置中，设置：

  - **对体二极管建模** 为 `Tabulated I-V curve`。
  - **表类型** 为 `Table in If(Vf) form`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电压，Vf** — 故障状态下的二极管正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

故障状态下二极管的正向电压。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，设置：

  - **对体二极管建模** 为 `Tabulated I-V curve`。
  - **表类型** 为 `Table in If(Vf) form` 或 `Table in If(Tj,Vf) form`
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电压，Vf(If)** — 故障状态下的二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V`（默认）

故障状态下二极管的正向电压，以正向电流表格化。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设为 `Specify from a datasheet`、`Specify using equation parameters directly` 或 `Lookup table (2-D, temperature independent)`。
- 在 **体二极管** 设置中，设置：

  - **对体二极管建模** 为 `Tabulated I-V curve`。
  - **表类型** 为 `Table in Vf(If) form`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电流，If** — 故障状态下的二极管正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

故障状态下二极管的正向电流。

#### 依赖关系

要启用此参数，

- 在 **体二极管** 设置中，设置：

  - **对体二极管建模** 为 `Tabulated I-V curve`。
  - **表类型** 为 `Table in Vf(If) form` 和 `Table in Vf(Tj,If) form`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电流，If(Tj,Vf)** — 具有表格化输入的故障状态二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）

故障状态下二极管的正向电流，以正向电压和结温表格化。

#### 依赖关系

要启用此参数，

- 在 **主** 设置中，将 **参数化** 设为 `Lookup table (3-D, temperature dependent)`。
- 在 **体二极管** 设置中，设置：

  - **对体二极管建模** 为 `Tabulated I-V curve`。
  - **表类型** 为 `Table in If(Tj,Vf) form`。
- 单击 **NMOS 故障** 参数中的 **添加故障** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **故障模式** 设为 `Parameter shift`。

### **故障状态下的二极管正向电压，Vf(Tj,If)** — 具有表格化输入的故障状态二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）

故障状态下二极管的正向电压，以正向电流和结温表格化。

#### 依赖项

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 在 **Body Diode** 设置中，设置：

  - 将 **Model body diode** 设置为 `Tabulated I-V curve`。
  - 将 **Table type** 设置为 `Table in Vf(Tj,If) form`。
- 通过单击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode off conductance** — Faulted diode off conductance `1e-12` `1/Ohm`（默认）

*自 R2024a 起*

故障状态下二极管的关断电导。

#### 依赖项

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Tabulated I-V curve`。
- 通过单击 **NMOS fault** 参数中的 **Add fault** 超链接，向 N-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024b：对每个晶体管端子的寄生引线电阻和电感建模

现在，您可以通过使用以下参数指定引线电阻和电感，对 N-Channel MOSFET 模块每个端子中的寄生效应建模：

- **Source lead resistance**
- **Drain lead resistance**
- **Gate lead resistance**
- **Body lead resistance**
- **Source lead inductance**
- **Drain lead inductance**
- **Gate lead inductance**
- **Body lead inductance**

### R2024a：指定表格化二极管的关断电导值

现在，您可以使用 **Diode off conductance** 参数指定表格化二极管的关断电导值。

在 R2024a 之前，要指定表格化二极管的关断电导，必须将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数，设置 N-Channel MOSFET 模块和其他 SPICE 兼容模块的最小电导。

## 描述

N-Channel 金属氧化物半导体场效应晶体管，使用 Shichman-Hodges 方程或基于表面势的模型

N-Channel MOSFET 模块提供两种主要建模选项：

- 基于阈值电压 — 使用 Shichman-Hodges 方程表示器件。这种基于阈值电压的建模方法具有参数化简单和电流-电压表达式简单的优点。但是，这些模型难以准确捕获跨阈值电压的过渡，并且缺少一些重要效应，例如速度饱和。有关详细信息，请参阅基于阈值的模型。

  此建模选项提供四种参数化 N-Channel MOSFET 的方式：

  - 通过从数据手册指定参数。
  - 通过直接指定方程参数。
  - 通过对 I-V（电流-电压）曲线的 2-D 查找表近似。有关详细信息，请参阅通过 2-D 查找表表示。
  - 通过包含温度数据的对 I-V（电流-电压）曲线的 3-D 查找表近似。有关详细信息，请参阅通过 3-D 查找表表示。
- 基于表面势 — 使用表面势方程表示器件。这种建模方法比简单平方律（基于阈值电压）模型提供更高水平的模型保真度。代价是需要提取更多参数。有关详细信息，请参阅基于表面势的模型。

结合热端口选项（请参阅 Thermal Port），该模块因此为您提供四种选择。要选择所需选项，请将 **Modeling option** 参数设置为以下之一：

- **Threshold-based** — 基本模型，使用 Shichman-Hodges 方程（基于阈值电压）表示器件，并且不仿真热效应。这是默认值。
- **Threshold-based with thermal** — 基于阈值电压且具有暴露热端口的模型。
- **Surface-potential-based** — 基于表面势的模型。此模型不仿真热效应。
- **Surface-potential-based with thermal** — 基于表面势的模型的热建模选项。

### 基于阈值的模型

该模块的基于阈值选项使用绝缘栅场效应晶体管的 Shichman 和 Hodges 方程 [1] 来表示 N-Channel MOSFET。

漏源电流 *IDS* 取决于工作区域：

- 在关断区域（*VGS* < *Vth*）中，漏源电流为：

  IDS=0
- 在线性区域（0 < *VDS* < *VGS* –*Vth*）中，漏源电流为：

  IDS=K((VGS−Vth)VDS−VDS2/2)(1+λ|VDS|)
- 在饱和区域（0 < *VGS* –*Vth* < *VDS*）中，漏源电流为：

  IDS=(K/2)(VGS−Vth)2(1+λ|VDS|)

在上述方程中：

- *K* 是晶体管增益。
- *VDS* 是正的漏源电压。
- *VGS* 是栅源电压。
- *Vth* 是阈值电压。对于四端子参数化，*Vth* 使用以下方程获得：

  | *VBS* 范围 | *Vth* 方程 |
  | --- | --- |
  | VBS≤0 | Vth=VT0+γ(−2ϕB)+γ(2ϕB−VBS) |
  | 0<VBS≤4ϕB | Vth=VT0−γVBS2ϕB |
  | VBS>4ϕB | Vth=VT0+γ(−2ϕB) |
- *λ* 是沟道调制。

要指定沟道的并联电导，请将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数，设置 N-Channel MOSFET 模块和其他 SPICE 兼容模块的最小电导。

### 基于阈值建模选项的电荷模型

该模块通过固定电容值或作为漏源电压函数的表格化值来对电容建模。无论哪种情况，您都可以直接指定栅源和栅漏电容值，或者让该模块从输入电容和反向传输电容值推导它们。因此，**Capacitance** 设置上电荷模型的 **Parameterization** 选项为：

- `Specify fixed input, reverse transfer and output capacitance` — 提供来自数据手册的固定参数值，并让该模块将输入电容和反向传输电容值转换为电容值，如下所述。这是默认方法。
- `Specify fixed gate-source, gate-drain and drain-source capacitance` — 直接为电容参数提供固定值。
- `Specify tabulated input, reverse transfer and output capacitance` — 基于数据手册图提供表格化电容和漏源电压值。该模块将输入电容和反向传输电容值转换为电容值，如下所述。
- `Specify tabulated gate-source, gate-drain and drain-source capacitance` — 提供电容和漏源电压的表格化值。

当数据手册提供电容随漏源电压变化的图时，请使用其中一个表格化电容选项（`Specify tabulated input, reverse transfer and output capacitance` 或 `Specify tabulated gate-source, gate-drain and drain-source capacitance`）。使用表格化电容值可获得更准确的动态特性，并避免为了拟合动态特性而交互调参。

如果使用 `Specify fixed gate-source, gate-drain and drain-source capacitance` 或 `Specify tabulated gate-source, gate-drain and drain-source capacitance` 选项，**Capacitance** 设置允许您直接指定 **Gate-drain capacitance, Cgd**、**Gate-source capacitance, Cgs** 和 **Drain-source capacitance, Cds** 参数值（固定或表格化）。否则，该模块从 **Input capacitance, Ciss**、**Reverse transfer capacitance, Crss** 和 **Output capacitance, Coss** 参数值推导它们。这两种参数化方法的关系如下：

- *CGD* = *Crss*
- *CGS* = *Ciss* – *Crss*
- *CDS* = *Coss* – *Crss*

对于四端子参数化，**Input capacitance, Ciss**、**Reverse transfer capacitance, Crss** 和 **Output capacitance, Coss** 使用以下方程获得：

- *CGD* = *Crss*
- *CGS* + *CGB* = *Ciss* – *Crss*
- *CDB* = *Coss* – *Crss*

简化的 Meyer 电容模型描述栅源电容 *CGS*、栅体电容 *CGB* 和栅漏电容 *CGD*。

如果您将 **Gate-bulk and gate-source charge-voltage linearity** 参数设置为 `Gate-bulk and gate-source capacitance change instantly`，此图显示当栅源电压 *Vgs* 达到阈值电压 *Vth* 时 *CGB* 和 *CGS* 如何变化。

如果您将 **Gate-bulk and gate-source charge-voltage linearity** 参数设置为 `Gate-bulk and gate-source capacitance change gradually`，此图显示当 *Vgs* 介于 *Vth* –2*ΦB* 和 *Vth* 之间时 *CGB* 和 *CGS* 如何变化。

两个固定电容选项（`Specify fixed input, reverse transfer and output capacitance` 或 `Specify fixed gate-source, gate-drain and drain-source capacitance`）允许您将栅极电容建模为固定栅源电容 *CGS* 以及固定或非线性栅漏电容 *CGD*。如果您为 **Gate-drain charge-voltage linearity** 参数选择 `Gate-drain charge function is nonlinear` 选项，则栅漏电荷关系由下图所示的分段线性函数定义。

有关如何将时间响应映射到器件电容值的说明，请参阅 N-Channel IGBT 模块参考页。但是，这种映射只是近似的，因为 Miller 电压通常比 IGBT 的情况更偏离阈值电压。

**注意**

由于此模块实现包含电荷模型，您必须对驱动栅极的电路阻抗建模，以获得具有代表性的开通和关断动态特性。因此，如果您通过将栅极驱动电路表示为受控电压源来简化它，则必须在电压源和栅极之间包含合适的串联电阻。

### 通过 2-D 查找表表示

对于详细模块建模选项的查找表表示，您提供漏源电流作为栅源电压和漏源电压函数的表格化值。使用此选项的主要优点是仿真速度。它还允许您根据测量数据或从另一个仿真环境获得的数据对器件进行参数化。

此图显示当您将 **Ids-Vds parameterization** 设置为 `Provide negative and positive Vds data` 时 2-D 查找表选项的实现：

此图显示当您将 **Ids-Vds parameterization** 设置为 `Provide positive Vds data only` 时 2-D 查找表选项的实现：

对于四端子 MOSFET，表面势和体因子值基于最近的阈值电压计算，如下图所示：

**注意**

为确保漏源电流和漏源电压的符号一致：

- 如果漏源电压等于 `0`，则 **Tabulated drain-source currents, Ids(Vgs,Vds)** 参数的值必须等于 `0`。
- 表格化功率，即 **Tabulated drain-source currents, Ids(Vgs,Vds)** 参数与漏源电压的乘积，必须大于或等于 `0`。
- 表格化电导，即 **Tabulated drain-source currents, Ids(Vgs,Vds)** 参数关于漏源电压 *Vds* 的梯度，必须大于或等于 `0`。
- **Tabulated drain-source currents, Ids(Vgs,Vds)** 参数关于栅源电压 *Vgs* 的一阶梯度必须等于 `0`。

### 通过 3-D 查找表表示

对于详细模块建模选项的温度相关查找表表示，您提供漏源电流作为栅源电压、漏源电压和温度函数的表格化值。

**注意**

为确保漏源电流和漏源电压的符号一致：

- 如果漏源电压等于 `0`，则 **Tabulated drain-source currents, Ids(Vgs,Vds,T)** 参数的值必须等于 `0`。
- 表格化功率，即 **Tabulated drain-source currents, Ids(Vgs,Vds,T)** 参数与漏源电压的乘积，必须大于或等于 `0`。
- 表格化电导，即 **Tabulated drain-source currents, Ids(Vgs,Vds,T)** 参数关于漏源电压 *Vds* 的梯度，必须大于或等于 `0`。
- **Tabulated drain-source currents, Ids(Vgs,Vds,T)** 参数关于栅源电压 *Vgs* 的一阶梯度必须等于 `0`。

### Surface-Potential-Based Model

该模块的基于表面电势的建模选项比简单的平方律（基于阈值电压的）模型提供更高水平的模型保真度。该模块的基于表面电势的建模选项包括以下效应：

- 完全非线性电容模型（包括非线性 Miller 电容）
- 模型内部电荷守恒，因此您可以将该模型用于对电荷敏感的仿真
- 速度饱和与沟道长度调制
- 本征体二极管
- 体二极管模型中的反向恢复
- 物理参数的温度缩放
- 对于热建模选项，动态自热（即，您可以仿真自热对器件电气特性的影响）

该模型是世界标准 PSP 模型的最小版本（参见 https://briefs.techconnect.org/papers/introduction-to-psp-mosfet-model/），仅包括 PSP 模型中的某些效应，以便在模型保真度和复杂度之间取得平衡。有关此模型中包含现象的物理背景的详细信息，请参阅 [2]。

该模型的基础是泊松方程：

∂2ψ∂x2+∂2ψ∂y2=qNAεSi[1−exp(−ψϕT)+exp(ψ−2ϕB−VCBϕT)]

ϕT=kBTq

其中：

- *ψ* 是静电势。
- *q* 是电子电荷量。
- *NA* 是衬底中的受主密度。
- *ɛSi* 是半导体材料（例如硅）的介电常数。
- *ϕB* 是本征费米能级与体硅中费米能级之间的差值。
- *VCB* 是表面层相对于体区的准费米势。
- *ϕT* 是热电压。
- *kB* 是玻尔兹曼常数。
- *T* 是温度。

泊松方程用于推导表面电势方程：

(VGB−VFB−ψs)2=γ2[ψs+ϕT(exp(−ψsϕT)−1)+ϕTexp(−2ϕB+VCBϕT)(exp(ψsϕT)−1)]

其中：

- *VGB* 是施加的栅极-体区电压。
- *VFB* 是平带电压。
- *ψs* 是表面电势。
- *γ* 是体因子，

γ=2qεSiNACox

- *Cox* 是单位面积电容。

该模块使用表面电势方程的显式近似，以避免需要对该隐式方程进行数值求解。

一旦表面电势已知，漏极电流 *ID* 由下式给出

ID=Wμ0LGΔLGmob1+(θsatΔψ)2[−Q¯invΔψ+ϕT(QinvL−Qinv0)]

其中：

- *W* 是器件宽度。
- *L* 是沟道长度。
- *μ0* 是低场迁移率。
- *θsat* 是速度饱和。
- *Δψ* 是漏极与源极之间的表面电势差。
- *Qinv0* 和 *QinvL* 分别是源极和漏极处的反型电荷密度。
- Q¯inv 是沟道上的平均反型电荷密度。
- *Gmob* 是迁移率降低因子。有关更多信息，请参阅 Main (Surface-Potential-Based Modeling Option) 部分中的 **Surface roughness scattering factor** 参数描述。
- *GΔL* 是沟道长度调制。

GΔL=1−ΔLL=1−αln[VDB−VDB,eff+(VDB−VDB,eff)2+Vp2Vp]

其中：

- *α* 是沟道长度调制因子。
- *VDB* 是漏极-体区电压。
- *VDB,eff* 是漏极-体区电压，限幅到对应于速度饱和或夹断（以先发生者为准）的最大值。
- *Vp* 是沟道长度调制电压。

该模块直接从表面电势计算反型电荷密度。

该模块还根据表面电势计算非线性电容。源极和漏极电荷贡献通过依赖于偏置的 Ward-Dutton 电荷分配方案分配，如 [3] 所述。这些电荷是显式计算得到的，因此该模型是电荷守恒的。容性电流通过计算相关电荷的时间导数得到。在实践中，仿真中的电荷会归一化到氧化层电容，并以伏特为单位计算。

MOSFET 增益 β 由下式给出

β=Wμ0CoxL

源极-体区短接连接的阈值电压近似由下式给出

VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

其中：

- 2*ϕB* 是强反型时的表面电势。

总体三端和四端模型由基于表面电势公式定义的本征 MOSFET、一个体二极管、串联电阻和固定重叠电容组成，如示意图所示。

### 对体二极管建模

该模块将体二极管建模为理想指数二极管或表格化二极管。

**指数二极管**

当您将 **Model body diode** 设置为 `Exponential` 时，结电容和扩散电容为：

Idio=Is[exp(−VDBnϕT)−1]

Cj=Cj01+VDBVbi

Cdiff=τIsnϕTexp(−VDBnϕT)

其中：

- *Idio* 是流经二极管的电流。
- *Is* 是反向饱和电流。
- *VDB* 是漏极-体区电压。
- *n* 是理想因子。
- *ϕT* 是热电压。
- *Cj* 是二极管的结电容。
- *Cj0* 是零偏结电容。
- *Vbi* 是内建电压。
- *Cdiff* 是二极管的扩散电容。
- *τ* 是渡越时间。

这些电容通过显式计算电荷来定义，然后对这些电荷求导以得到上述容性表达式。该模块将容性二极管电流计算为相关电荷的时间导数，类似于基于表面电势的 MOSFET 模型中的计算。

**表格化二极管**

要对表格化二极管建模，请将 **Model body diode** 参数设置为 `Tabulated I-V curve`。下图显示了表格化二极管选项的实现：

选择此参数化时，您必须仅提供正向偏置的数据。

该模块使用平滑插值选项实现二极管。如果二极管超出所提供的表格化数据范围，该模块会在最后一个电压-电流数据点处使用线性外推技术。

要指定表格化二极管的关断电导，请设置 **Diode off conductance** 参数。*(since R2024a)*

**注意**

表格化二极管不对反向击穿进行建模。

### 对温度依赖性建模

默认行为是不对温度依赖性进行建模，并且器件在您提供模块参数所用的温度下进行仿真。要在仿真期间对温度依赖性进行建模，请在 **Temperature Dependence** 设置的 **Parameterization** 参数中选择 `Model temperature dependence`。

**基于阈值的模型**

对于基于阈值的建模选项，您可以包括在仿真期间对晶体管静态行为的温度依赖性进行建模。电容的温度依赖性不建模，因为这是一个小得多的效应。

当包括温度依赖性时，定义晶体管的方程保持不变。增益 *K* 和阈值电压 *Vth* 根据以下方程变为温度的函数：

KTs=KTm1(TsTm1)BEX

*Vths* =
*Vth1* + *α*
(*Ts* –
*Tm1*)

其中：

- *Tm1* 是指定晶体管参数时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *KTm1* 是测量温度下的晶体管增益。
- *KTs* 是仿真温度下的晶体管增益。当对温度依赖性建模时，这是 MOSFET 方程中使用的晶体管增益值。
- *Vth1* 是测量温度下的阈值电压。
- *Vths* 是仿真温度下的阈值电压。当对温度依赖性建模时，这是 MOSFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**Vth*/*d**T*。

对于四端参数化，*Vth* 使用以下方程获得：

| *VBS* 范围 | *Vth* 方程 |
| --- | --- |
| VBS≤0 | dVthdT=dVT0dT−γ22ϕBd2ϕBdT+γ22ϕB−VBSd2ϕBdT |
| 0<VBS≤4ϕB | dVthdT=dVT0dT−γVBS4(2ϕB)−32d2ϕBdT |
| VBS>4ϕB | dVthdT=dVT0dT−γ22ϕBd2ϕBdT |

其中：

- ϕB=kTqln(NBni) 是表面电势，且 d2ϕBdT=1T[2ϕB−(Eg(0)q+3kTq)]。
- *Eg(0)* 是外推的零度带隙，对于硅等于 `1.16` `eV`。
- *VBS* 是体区-源极电压。

对于大多数 MOSFETS，您可以使用 `-1.5` 作为 *BEX* 的默认值。一些数据手册会给出 *α* 的值，但最典型的是它们提供漏源导通电阻 *RDS(on)* 的温度依赖性。根据模块参数化方法，您有两种指定 *α* 的方式：

- 如果您根据数据手册对模块进行参数化，则必须提供在第二个测量温度下的 *RDS(on)*。然后模块基于此数据计算 *α* 的值。
- 如果您通过指定方程参数进行参数化，则必须直接提供 *α* 的值。

如果您有更多数据，包括超过一个温度下漏极电流作为栅源电压函数的数据，那么您还可以使用 Simulink® Design Optimization™ 软件来帮助调整 *α* 和 *BEX* 的值。

**Surface-Potential-Based Model**

基于表面电势的模型包括对电容特性的温度效应，以及在仿真期间对晶体管静态行为的温度依赖性进行建模。

**Main** 设置上的 **Measurement temperature** 参数指定提取其他器件参数时的温度 *T*m1。**Temperature Dependence** 设置提供仿真温度 *T*s，以及其他器件参数的温度缩放系数。有关更多信息，请参阅 Temperature Dependence (Surface-Potential-Based Modeling Option)。

### 故障

要对 N-Channel MOSFET 模块中的故障进行建模，请在 **Faults** 部分中，单击您要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

N-Channel MOSFET 模块对五类故障进行建模：

- `Open circuit` — 由于金属化烧毁导致的故障
- `Drain-source short` — 由于漏-源沟道上的雪崩击穿导致的故障
- `Drain-bulk short or source-bulk short` — 由于漏-体或源-体沟道上的雪崩击穿导致的故障
- `Gate oxide short` — 栅氧化层介电层故障
- `Parameter shift` — 由于老化导致的故障

该模块可以在特定时间触发故障事件，或者当电流或电压超过限值的时间长于特定时间间隔时触发故障事件。

**Parameter shift 故障**

如果在 **Faults** 设置中，您将 **Failure mode** 参数设置为 `Parameter shift`，则 MOSFET 由于其组件老化而发生故障。以下方程定义了漂移参数的值：

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

其中 *tth* 是触发故障的时间阈值，*τ* 是 **Fault transition time constant, tau** 参数的值。

**Gate oxide short 故障**

如果在 **Faults** 设置中，您将 **Failure mode** 参数设置为 `Gate oxide short`，则栅氧化层介电层发生故障。这些图显示了未故障和故障状态下三端 MOSFET 的等效电路：

这些图显示了未故障和故障状态下四端 MOSFET 的等效电路：

### 热端口

该模块具有可选热端口，默认隐藏。要显示热端口，请将 **Modeling option** 参数设置为：

- `Threshold-based with thermal` — 基于阈值电压并显示热端口的模型
- `Surface-potential-based with thermal` — 基于表面电势并显示热端口的模型

此操作会在模块图标上显示热端口 **H**，并显示 **Thermal Port** 参数。

使用热端口来仿真产生的热量和器件温度的影响。有关使用热端口和 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。

此表显示了模块的电容与 initial targets 之间的关系：

| 定义的电容 | Initial Targets |
| --- | --- |
| 栅极-发射极电容，*Cge* | 仅设置栅极-发射极电容电压的初始目标。将集电极-发射极电容电压的初始目标设置为 `0`，或将其优先级设置为 `None`。 |
| 集电极-发射极电容，*Cce* | 仅设置集电极-发射极电容电压的初始目标。将栅极-发射极电容电压的初始目标设置为 `0`，或将其优先级设置为 `None`。 |
| 栅极-集电极电容，*Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| 栅极-发射极电容，*Cge*，和栅极-集电极电容，*Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-发射极和栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| 栅极-发射极电容，*Cge*，和集电极-发射极电容，*Cce* | 设置栅极-发射极和集电极-发射极电容的初始目标。 |
| 栅极-集电极电容，*Cgc*，和集电极-发射极电容，*Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-集电极和集电极-发射极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| 栅极-发射极电容，*Cge*，栅极-集电极电容，*Cgc*，和集电极-发射极电容，*Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-发射极、栅极-集电极和集电极-发射极电容的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |

**注意**

在您的模型中，**Priority** 等于 `Low` 或 `High` 的 initial targets 数量必须与微分变量数量匹配。微分变量来自模型中的电感和电容。

### 绘制器件特性

您可以绘制 N-Channel MOSFET 模块的基本 I-V 特性，而无需构建完整模型。使用这些图来探索参数选择对器件特性的影响。如果根据数据手册对模块进行参数化，则可以将您的图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型，但不知道要使用哪个制造器件，则可以将您的图与数据手册进行比较，以帮助您做出决定。

要启用此选项，请将 N-Channel MOSFET 模块的 **Modeling option** 参数设置为 `Threshold Based` 或 `Surface potential based`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅绘制半导体模块的基本 I-V 特性。

N-Channel MOSFET 模块还支持 **Explore characteristics** 选项。使用此选项可深入研究模块特性，并将模块行为与一组目标特性进行匹配。要启用此选项，请将该模块的 **Modeling option** 参数设置为 `Surface potential based`。然后，右键单击该模块，并从上下文菜单中选择 **Electrical** > **Explore characteristics**。有关此选项的详细信息，请参阅 MOSFET 特性查看器。
