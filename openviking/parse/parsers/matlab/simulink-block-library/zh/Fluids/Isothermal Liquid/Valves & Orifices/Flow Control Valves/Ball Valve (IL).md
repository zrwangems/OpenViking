---
type: simulink-block
title: 'Ball Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'ballvalveil'
documentation_source_path: 'ref/ballvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Ball Valve (IL)

## 端口

### 输入

### **S** — 阀门位置，rad 物理信号

与阀门位置关联的物理信号端口，单位为 rad。值 0 表示阀门完全关闭，值 π/2 表示阀门完全打开。

### 守恒

### **A** — 阀端口 A Isothermal liquid

与阀端口 A 关联的 Isothermal liquid 守恒端口。

### **B** — 阀端口 B Isothermal liquid

与阀端口 B 关联的 Isothermal liquid 守恒端口。

## 参数

### **Valve parameterization** — 用于参数化给定流量系数的选项 `Orifice area based on geometry`（默认） | `Cv flow coefficient` | `Kv flow coefficient`

是否使用 *Kv*、*Cv* 或 *Cd* 来参数化流量。模块使用以下系数定义：

- *Kv* 是在 15℃、压降为 1 bar 时，水通过完全打开阀门的流量容量，单位为
  m3/h。
- *Cv* 是在 60℉、压降为 1 psi 时，水通过完全打开阀门的流量容量，单位为 gpm。
- *Cd* 是无量纲排放系数，用于定义阀门的效率。

### **Opening characteristic** — 球阀参数化 `Area of overlapping circles`（默认） | `Tabulated`

用于使用重叠圆面积方法或表格数据来参数化模块的选项。

### **Maximum Cv flow coefficient** — 最大阀门流量系数 `32` `gpm`（默认） | 正标量

阀门流量系数的最大值。此值应对应于完全打开位置。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Area of overlapping circles`，并将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **Maximum Kv flow coefficient** — 最大阀门流量因子 `49` `m^3/hr`（默认） | 正标量

阀门流量因子的最大值。此值应对应于完全打开位置。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Area of overlapping circles`，并将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Discharge coefficient** — 排放系数 `0.64`（默认） | 正标量

阀门的排放系数。此值是一个修正因子，用于计入理论流量中的损失。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Cross-sectional area at ports A and B** — 阀端口横截面积 `pi * (25 ^ 2) / 4` `mm^2`（默认） | 正标量

阀端口的横截面积。阀端口是阀体中流体与球孔相交的路径。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Ball bore area** — 球孔面积 `pi * (20 ^ 2) / 4` `mm^2`（默认） | 正标量

阀门球体中孔口的横截面积。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Cv flow coefficient vector** — 给定球旋转角度下的流量系数 `[1e-06, .58, 1.15, 1.9, 2.8, 4.3, 7, 10.5, 17, 26, 32]` `gpm`（默认） | 向量

给定球旋转角度下的阀门流量系数。每个元素与 **Ball rotation vector** 参数一一对应。第一个元素对应于阀门泄漏，且必须非零。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`，并将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **Kv flow coefficient vector** — 给定球旋转角度下的流量因子 `[1e-06, .34, .76, 1.6, 2.45, 4.1, 5.75, 9.4, 13, 28, 50]` `m^3/hr`（默认） | 向量

给定球旋转角度下的阀门流量因子。每个元素与 **Ball rotation vector** 参数一一对应。第一个元素对应于阀门泄漏，且必须非零。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`，并将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Area vector** — 给定球旋转角度下的面积 `[1e-10, 62.5, 125, 187.5, 250, 312.5, 375, 437.5, 500, 562.5, 625]` `mm^2`（默认） | 向量

给定球旋转角度下的流动面积。每个元素与 **Ball rotation vector** 参数一一对应。第一个元素对应于阀门泄漏，且必须非零。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`，并将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Ball rotation vector** — 球旋转角度 `pi / 2 .* [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]` `rad`（默认） | 向量

给定流量系数或面积下的球旋转角度。此向量中的元素必须与 **Cv flow coefficient vector** 参数、**Kv flow coefficient vector** 参数或 **Area vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Leakage area** — 处于完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认） | 正标量

当阀门处于完全关闭位置时所有间隙的总和。模块将任何小于此值的面积饱和到指定的泄漏面积。此值通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | 正标量

通过阀门的层流的上限雷诺数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024b：更新了参数和参数设置名称

Ball Valve (IL) 模块中参数和参数设置的名称已更新，以与其他阀门模块保持一致。模块的行为没有变化。下表总结了新的参数和参数设置名称。

| 以前的参数或设置名称 | 更新后的参数或设置名称 |
| --- | --- |
| **Ball valve parameterization** | **Opening characteristic** |
| **Flow coefficient parameterization** | **Valve parameterization** |
| `Kv coefficient (SI)` | `Kv flow coefficient` |
| `Cv coefficient (USCS)` | `Cv flow coefficient` |
| `Cd coefficient and area` | `Orifice area based on geometry` |
| **Discharge coefficient (Cd)** | **Discharge coefficient** |
| **Maximum valve flow coefficient (Cv)** | **Maximum Cv flow coefficient** |
| **Maximum valve flow factor (Kv)** | **Maximum Kv flow coefficient** |
| **Valve flow coefficient (Cv) vector** | **Cv flow coefficient vector** |
| **Valve flow factor (Kv) vector** | **Kv flow coefficient vector** |

## 描述

等温液体网络中的球阀

Ball Valve (IL) 模块表示等温液体网络中的球阀。球阀由球体和阀体组成，球体带有一个可在阀体内转动的孔。当阀门打开时，孔与阀体端口完全重叠。当阀门关闭时，球体旋转并减少重叠量，从而减小孔口的有效面积。球阀通常用于流量隔离，因为它们可以在许多循环中可靠地切断流量。在需要精确节流的应用中，球阀不太常见。

您可以通过解析方法或使用表格数据来参数化该模块。当您将 **Opening characteristic** 设置为 `Area of overlapping circles` 时，模块将阀端口与球孔之间的重叠面积视为开启面积，使得

Aopen=sin(φ)Rbore2[cos−1(λbore)−λbore1−λ2bore]+Rport2[cos−1(λport)−λport1−λ2port]λbore=Rbore2−Rport2+l22Rborelλport=Rport2−Rbore2+l22Rportl

其中：

- *Rport* 和
  *Rbore* 分别是阀端口和球孔的半径。
- *l* 是孔中心相对于阀端口中心的位移。
- *φ* 是物理信号 **S** 给出的球阀旋转角度。阀门在 0 rad 时完全关闭，在 π/2 rad 时完全打开。

### 质量流量

模块使用孔口的压力-面积关系计算通过阀门的流量，使得

m˙=CdA2ρ¯Δp(Δp2+Δpcrit2)14,

其中：

- *Cd* 是排放系数。
- ρ¯ 是平均流体密度。
- *A* 是开口流动面积，其中 *A* =
  *Aopen* +
  *Aleak*，而 *Aleak*
  是 **Leakage area** 参数。
- *Δpcrit* 是与临界雷诺数 *Recrit* 关联的临界压差。

模块按如下方式计算 *Δpcrit*：

Δpcrit=πρ¯8A(vRecritCd)2.

当您将 **Valve parameterization** 设置为
`Orifice area based on geometry` 时，您可以使用 **Discharge
coefficient** 参数指定 *Cd*。当您将 **Valve
parameterization** 设置为 `Cv flow coefficient` 时，
模块按如下方式计算 *Cd*：

Cd=CvAρwater,60°F2ΔpCv,

其中 *Cv* 是
**Maximum Cv flow coefficient** 参数。当您将
**Valve parameterization** 设置为 `Kv flow
coefficient` 时，模块使用

Cd=KvAρwater,15°C2ΔpKv,

其中 *Kv* 是
**Maximum Kv flow coefficient** 参数。在任一方程中，
*ΔpCv* 为
1 psi，*ΔpKv* 为 1
bar。
