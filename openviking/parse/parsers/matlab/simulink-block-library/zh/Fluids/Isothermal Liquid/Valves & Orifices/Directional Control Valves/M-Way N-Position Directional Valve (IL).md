---
type: simulink-block
title: 'M-Way N-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'mwaynpositiondirectionalvalveil'
documentation_source_path: 'ref/mwaynpositiondirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# M-Way N-Position Directional Valve (IL)

## 端口

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号输入端口，单位为 m。

### 守恒

### **1** — 端口 1 等温液体

与端口 1 关联的等温液体守恒端口。

### **2,...,10** — 具有参数依赖关系的端口 等温液体

与端口 2 至 10 关联的等温液体守恒端口，其中端口数量等于 **Number of ports** 参数。

#### 依赖关系

要启用端口 2 至 10，请将 **Number of ports** 设置为所需的端口数量。

## 参数

### 阀配置

### **Number of ports** — 阀端口数量 `2`（默认）| `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

与阀关联的端口数量，*M*。最多可选择十个。

### **Number of spool positions** — 阀芯位置数量 `2`（默认）| `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

阀芯位置数量，*N*。最多可选择十个。

### **Spool travel at each spool position index** — 阀芯行程 `[-2, 0, 2, 4]` `mm`（默认）| 长度为 *N* 的向量

阀芯行程值。每个元素对应不同的阀芯位置索引。此向量的长度必须等于 **Number of spool positions** 参数的长度 *N*。值为 `0` 表示中位阀芯位置。

### **Number of orifices** — 节流口数量 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20`

节流口数量。最多可选择 20 个。

### **Area characteristics** — 面积特性参数化选项 `Identical for all flow paths`（默认）| `Different for each flow path`

是否为每个节流口应用相同或不同的参数化。

### **Orifice parameterization** — 节流口参数化 `Linear – Area vs. spool travel`（默认）| `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)` | `Tabulated data – Area vs. spool travel`

是否对每个节流口进行线性参数化、按面积使用表格数据参数化，或按压降使用表格体积流量数据参数化。

当 **Area characteristics** 为 `Identical for all flow paths` 时，可将此参数设置为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。要为此参数启用 `Tabulated data – Area vs. spool travel` 选项，请将 **Area characteristics** 设置为 `Different for each flow path`。

### **Inter-position spool travel fraction for which orifices remain fully open** — 阀芯位置之间节流口保持全开的行程比例 `0.5`（默认）| [0,1) 范围内的标量

相邻阀芯位置之间的分数距离，在此距离内每个节流口保持最大开度面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`。

### **Inter-position spool travel fraction for which orifices transition between open-closed** — 节流口在开-闭之间过渡的阀芯行程 `0.1`（默认）| 非负标量

相邻阀芯位置之间的分数距离，在此距离内节流口面积在最大面积和泄漏面积之间过渡。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`。

### **Maximum orifice area** — 最大节流口面积 `1e-4` `m^2`（默认）| 正标量

所有节流口的最大开度面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。

### **Leakage area fraction** — 泄漏面积比例 `0.01`（默认）| 正标量

泄漏面积占 **Maximum orifice area** 参数值的比例。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。

### **Cross-sectional area at ports** — 所有端口的横截面积 `inf` `m^2`（默认）| 正标量

所有端口的横截面积。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。
- **Area characteristics** 设置为 `Different for each path`，且 **Orifice parameterization** 设置为 `Tabulated data – Area vs. spool travel`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正系数。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。
- **Area characteristics** 设置为 `Different for each path`，且 **Orifice parameterization** 设置为 `Tabulated data – Area vs. spool travel`。

### **Critical Reynolds number** — 临界雷诺数 `150`（默认）| 正标量

通过节流孔的层流雷诺数上限。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。
- **Area characteristics** 设置为 `Different for each path`，且 **Orifice parameterization** 设置为 `Tabulated data – Area vs. spool travel`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。

### **Pressure recovery** — 考虑面积扩大时压力增加的选项 `Off`（默认）| `On`

是否考虑当流体从较小节流面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。
- **Area characteristics** 设置为 `Different for each path`，且 **Orifice parameterization** 设置为 `Tabulated data – Area vs. spool travel`。

### **Pressure drop vector** — 表格化压降 `[-.1, .3, .5, .7]` `MPa`（默认）| 长度为 *X* 的向量

所有节流孔的表格化压降值。此向量的元素与 **Fully open volumetric flow rate vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Fully open volumetric flow rate vector** — 表格化体积流量 `[-.0009, .0016, .002, .0024]` `m^3/s`（默认）| 长度为 *X* 的向量

在给定压降下全开节流孔的体积流量。此向量的元素与 **Pressure drop vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Leakage flow rate fraction** — 泄漏流量分数 `0.01`（默认）| 正标量

泄漏量占 **Fully open volumetric flow rate vector** 参数的比例。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### Orifice 1

本节仅包含节流口 1 的参数。其余节流口参数与节流口 1 相同，只是编号不同，以及节流口 1 的参数说明中提到的情形不同。要了解更多信息，请参阅 Orifice Parameterization。

### **Ports connected by orifice 1** — 由节流口 1 连接的端口 `[3, 2]`（默认）| 长度为 2 的向量

由节流口 1 连接的两个流体端口。第一个元素是连接到节流口 A 端口的阀端口。第二个元素是连接到节流口 B 端口的阀端口。在 Simscape Results Explorer 应用中，变量 `mdot_A` 和 `mdot_B` 分别是流入 Orifice (IL) 模块 A 端口和 B 端口的质量流量。`p_diff` 是从节流口端口 A 到端口 B 的压降。在模块图标中，对于连接到单个节流口的端口，箭头指向由该参数第二个元素表示的端口。其他节流口的默认值为：

- 节流口 2：`[4, 5]`
- 节流口 3：`[2, 1]`
- 节流口 4：`[3, 4]`
- 节流口 5–节流口 20：`[1, 2]`

### **Spool position indices where orifice 1 is open** — 节流口 1 打开的阀芯位置 `[1, 4]`（默认）| 长度为 1 到 *N* 的向量

节流口 1 打开的阀芯位置。该向量必须严格单调递增，其值介于 1 和 **Number of spool positions** 参数的值之间。其他节流口的默认值为：

- 节流口 2：`[1, 4]`
- 节流口 3：`[3, 4]`
- 节流口 4：`[3, 4]`
- 节流口 5–节流口 20：`1`

如果 **Spool position indices where orifice 1 is open** 参数包含连续整数，则表示该节流口在多个相邻的离散阀芯位置中打开。在这种情况下，模块行为取决于 **Orifice parameterization** 参数：

- 如果 **Orifice parameterization** 为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`，则模块在该节流口打开的多个相邻离散阀芯位置中保持 **Maximum orifice area** 参数或 **Fully open volumetric flow rate vector** 参数的值。
- 如果 **Orifice parameterization** 为 `Tabulated data – Area vs. spool travel`，则 **Vector of spool travel relative to discrete spool position for orifice 1** 参数中等于 `0` 的元素对应于相邻位置中取值最小的离散阀芯位置。

### **Spool travel for which orifice 1 remains fully open** — 保持完全打开的阀芯行程 `1` `mm`（默认）| 非负标量

节流口保持最大开度面积的阀芯行程。该阀芯行程距离的中心位于 **Spool position with open orifice 1** 参数的值处。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Spool travel for which orifice 1 transitions between open-closed** — 节流口 1 在开-闭之间过渡的阀芯行程 `0.2` `mm`（默认）| 正标量

节流口从完全打开过渡到完全关闭所经过的阀芯行程。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Maximum area of orifice 1** — 完全打开时的节流口面积 `1e-4` `m^2`（默认）| 正标量

节流口 1 的开度面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel`。

### **Pressure drop vector of orifice 1** — 节流口 1 压降 `[-.1, .3, .5, .7]` `MPa`（默认）| 长度为 *X* 的向量

节流口 1 的压降值向量。这些值与 **Fully open volumetric flow rate vector of orifice 1** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Fully open volumetric flow rate vector of orifice 1** — 节流口 1 全开体积流量 `[-.0009, .0016, .002, .0024]` `m^3/s`（默认）| 长度为 *X* 的向量

给定压降下节流口 1 全开时的体积流量。这些值与 **Pressure drop vector of orifice 1** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)`。

### **Vector of spool travel relative to discrete spool position for orifice 1** — 阀芯位移向量 `[-.7, -.4, -.35, -.3, -.25, 0]` `mm`（默认）| 向量

节流口 1 的阀芯位移向量，与 **Area vector for orifice 1** 参数中的元素相对应。此参数必须与 **Area vector for orifice 1** 参数长度相同，包含一个等于 `0` 的元素，并且必须严格单调递增。值为 `0` 的元素表示阀芯处于离散阀芯位置索引时。如果 **Spool position indices where orifice 1 is open** 参数包含多个相邻的离散阀芯位置，则 **Vector of spool travel relative to discrete spool position for orifice 1** 参数中值为 `0` 的元素对应于相邻位置序列中的最小值。例如，如果 **Spool position indices where orifice 1 is open** 参数为 `[1 2]`、`[1 3 4 7]` 或 `[2 3 4 8 9]`，则值为 0 的元素将分别对应于 `1`、`3` 或 `{2,8}`。

如果 **Spool position indices where orifice 1 is open** 参数对所有阀芯位置都打开，即值为 `[1:Number of spool positions]`，则 **Vector of spool travel relative to discrete spool position for orifice 1** 参数中值为 `0` 的元素对应于第一个离散阀芯位置。在这种情况下，您可以将 **Area vector for orifice 1** 参数设置为相同的重复值，以对恒定面积节流口建模。

该向量可以包含负值和正值元素，分别表示相对于节流口打开时所对应的离散阀芯位置，阀芯向任一方向移动的位移。如果该参数仅包含非负元素或仅包含非正元素，则节流口开度相对于离散位置分别对负向或正向阀芯位移表现为对称行为。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data – Area vs. spool travel`。

### **Area vector for orifice 1** — 节流口开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001, .0001]` `m^2`（默认）| 向量

节流口 1 的面积向量，与 **Vector of spool travel relative to discrete spool position for orifice 1** 参数中的元素相对应。此参数必须与 **Vector of spool travel relative to discrete spool position for orifice 1** 参数长度相同。如果节流口在第一个或最后一个离散阀芯位置打开，则当阀芯位移超过第一个或最后一个离散阀芯位置时，节流口保持以最大面积全开。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `每条流路不同`，并将 **节流孔参数化** 设置为 `表格数据 – 面积与阀芯行程`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2023b：使用关于面积和阀芯行程的表格数据对模块进行参数化

您现在可以使用面积与阀芯行程曲线的表格数据来参数化节流孔面积特性。当 **面积特性** 为 `每条流路不同` 时，将 **节流孔参数化** 参数设置为 `表格数据 – 面积与阀芯行程`，以使用新的参数化选项。使用 **相对于离散阀芯位置的阀芯行程向量** 和 **节流孔面积向量** 参数指定表格数据。

## 描述

等温液体网络中的 M 位 N 通阀

M-Way N-Position Directional Valve (IL) 模块表示一个滑阀操作的方向阀，具有任意配置的端口、阀芯位置和节流孔。该模块最多接受十个端口、十个阀芯位置和 20 个节流孔。具有多种配置的阀在建筑、农业以及某些车辆应用中最为常见。该模块允许您将相同的面积特性应用于所有流路，从而简化复杂的参数化过程。您也可以单独为每个流路指定面积特性。您可以通过使用表格数据或线性数据指定开口面积来参数化阀，也可以使用表示完全打开节流孔在不同压降下体积流量的表格数据来参数化阀。该模块使用可变节流孔来控制给定连接端口对之间的流量。端口 **S** 处的物理信号触发阀芯运动以打开或关闭阀。有关该模块如何计算通过可变节流孔的流量的更多详细信息，请参阅 Orifice (IL)。

您可以通过右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics** 来生成阀的特性曲线图。更改模块参数后要更新曲线图，请单击 **Reload Data** 按钮。您可以控制特性曲线图的形状。要选择哪些线可见，请单击图例上相应的节流孔。

默认阀特性曲线图为：

默认阀特性曲线图

该图指示了位置 A1、A2、B1 和 B2。

标有 A1、B1、B2 和 A2 点的阀特性曲线图。

位置 1 位于阀芯行程 -1 mm 处。位置 2 位于阀芯行程 0 mm 处，位置 3 位于阀芯行程 1 mm 处。位置 *A1* 和 *A2* 分别表示节流孔开口面积的左侧和右侧过渡区域。位置 *B1* 和 *B2* 分别表示节流孔开口面积的左侧和右侧完全打开区域。当前阀芯位置是 *B1* 和 *B2* 之间的间隔。当您将 **Area characteristics** 设置为 `Identical for all flow paths` 时。

- *A1* = （阀芯位置 1 和 2 之间的距离）\*（**Inter-position spool travel fraction for which orifices transition between open-closed** 参数的值）
- *A2* = （阀芯位置 2 和 3 之间的距离）\*（**Inter-position spool travel fraction for which orifices transition between open-closed** 参数的值）
- *B1* = （阀芯位置 1 和 2 之间的距离）\*（**Inter-position spool travel fraction for which orifices remain fully open** 参数的值）
- *B2* = （阀芯位置 2 和 3 之间的距离）\*（**Inter-position spool travel fraction for which orifices remain fully open** 参数的值）

当您将 **Area characteristics** 设置为 `Different for each flow path` 并将 **Orifice parameterization** 设置为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)` 时：

- *A1* = *A2* = **Spool travel for which orifice 2 transitions between open-closed** 参数的值。
- *B1* = *B2* = **Spool travel for which orifice 2 remains fully open** 参数的值。

### 节流孔参数化

当您将 **面积参数化** 设置为 `Different
for each flow path` 时，您可以使用 **Orifice 1,…,20** 部分中的参数来参数化每个节流孔。例如，如果您将 **节流孔数量** 设置为 3，则该模块包含 **Orifice 1**、**Orifice 2** 和 **Orifice 3** 的部分。每个部分具有相同的参数名称，后跟该部分的编号。

模块图标会自动更新以指示节流孔配置，您可以通过相应的 **Ports connected by orifice...** 参数进行控制。如果您将一个奇数编号的端口连接到一个偶数编号的端口，模块图标会显示一个指向第二个列出端口的箭头。当参数化无效时，模块图标会进行指示。

如果您启用日志记录，每个节流孔的 `Orifice.S` 信号根据下表描述阀芯位置：

|  | **面积特性** 参数 | |
| --- | --- | --- |
|  | `Identical for all flow paths` | `Different for each flow path` |
| 如果 **节流孔参数化** 为 `Linear – Area vs. spool travel` 或 `Tabulated data – Volumetric flow rate vs. pressure drop (linear with spool travel)` | 当节流孔完全打开时，`Orifice.S` = `0 m`。`Orifice.S` 信号中的单位 m 对应于位置间阀芯行程分数。当节流孔完全关闭时，`Orifice.S = - Stravel`，其中 *Stravel* 是 **Inter-position spool travel fraction for which orifices transition between open-closed** 参数的值。 | 当节流孔完全打开时，`Orifice.S` = `0 m`。当节流孔完全关闭时，`Orifice.S = - Stravel`，其中 *Stravel* 是 **Spool travel for which orifice transitions between open-closed** 参数的值。 |
| 如果 **节流孔参数化** 为 `Tabulated data – Area vs. spool travel` | 不是参数化选项 | 当节流孔完全打开时，`Orifice.S` = `0 m`。在所有其他位置，当节流孔完全关闭时，`Orifice.S` = **Vector of spool travel relative to discrete spool position for Orifice** 参数扩展版本的第一个或最后一个元素。如果 **Vector of spool travel relative to discrete spool position for Orifice** 参数不包含正区域或负区域，则参数的扩展版本将阀芯行程向量和面积向量扩展到对称的正区域和负区域。节流孔泄漏面积对应于扩展阀芯行程向量的第一个和最后一个元素。如果 **Vector of spool travel relative to discrete spool position for Orifice** 参数同时具有负区域和正区域，则节流孔可以具有不同的泄漏面积。 |

### 假设和限制

- 当您将 **面积特性** 设置为 `Different for each flow
  path` 时，该模块假设每个节流孔围绕阀芯位置具有对称的打开和关闭。
- 当您将 **面积特性** 设置为 `Identical for all flow
  paths` 时，该模块假设每个节流孔具有对称的打开和关闭，并按 **Spool travel at each spool position
  index** 参数的间距进行缩放。
