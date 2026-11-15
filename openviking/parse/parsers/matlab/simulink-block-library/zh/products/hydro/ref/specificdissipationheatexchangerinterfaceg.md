---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger Interface (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheatexchangerinterfaceg'
documentation_source_path: 'ref/specificdissipationheatexchangerinterfaceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger Interface (G)

## 端口

### 输出

### **CP** — 气体的等压比热，`kJ/(kg*K)` physical signal

热接口内部流体体积中气体的等压比热。

### **M** — 热液体的质量流量，`kg/s` physical signal

接口内部流体体积中气体的质量流量。当流量方向从端口 **A** 到端口 **B** 时，输出信号为正，否则为负。

### 守恒

### **A** — 气体流体开口

气体可以进入和离开热接口的开口。

### **B** — 气体流体开口

气体可以进入和离开热接口的开口。

### **H** — 流体入口处的热状态 热

用于设置作为气体入口的气体端口处热状态的热端口。

## 参数

#### 压力损失

### **Mass flow rate vector** — 用于指定压降数据的质量流量 `[.3, .5, 1, 1.5, 2, 2.5] kg/s`（默认） | *K*-element array，单位 mass/time

用于指定压降表格数据的质量流量数组。

### **Pressure drop vector** — 对应于指定质量流量的压降数据 `[3, 5, 10, 25, 35, 50] * 1e-3 MPa`（默认） | *K*-element array，单位 pressure

对应于表格质量流量数据的从入口到出口的压降数组。

### **Reference inflow temperature** — 指定压降数据时的温度 `293.15 K`（默认） | scalar，单位 temperature

指定表格压降数据时的温度。

### **Reference inflow pressure** — 指定压降表格数据时的压力 `0.101325 MPa`（默认） | scalar，单位 pressure

指定表格压降数据时的压力。模块使用此参数计算第三个参考参数，即参考密度。它使用该参考值对偏离参考条件的压力和温度下的表格压降数据进行缩放。

### **Mass flow rate threshold for flow reversal** — 低于该值对数值数据进行平滑的质量流量 `1e-6 kg/s`（默认） | scalar，单位 mass/time

低于该质量流量时启动平滑流动反向，以防止仿真数据中出现不连续。

### **Gas volume** — 换热器内气体的体积 `0.01 m^3`（默认） | scalar，单位 volume

在任何给定时间占据换热器的气体体积。**Effects and Initial Conditions** 选项卡中指定的初始条件应用于此体积。该体积在仿真期间保持恒定。

### **Cross-sectional area at ports A1 and B1** — 气体入口处的流通面积 `0.01 m^2`（默认） | scalar，单位 area

气体入口处的流通面积。入口 **A1** 和 **B1** 假设尺寸相同。

#### 效应和初始条件

### **Enable dynamic compressibility** — 对气体通道中的压力动态建模的选项 `On`（默认） | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。

### **Nominal temperature** — 标称工况下的温度 `293.15 K`（默认） | scalar

标称工况下的气体温度。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal pressure** — 标称工况下的压力 `0.101325 MPa`（默认） | scalar

标称工况下的气体压力。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial pressure** — 仿真开始时的压力 `0.101325 MPa`（默认） | scalar

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial pressure priority** — 压力参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认） | scalar

仿真开始时气体通道中的温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：可选地对动态可压缩性建模

Specific Dissipation Heat Exchanger Interface (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。以前，此模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：新模块名

该模块现在名为 Specific Dissipation Heat Exchanger Interface (G)。以前名为 Simple Heat Exchanger Interface (G)。

## 描述

气体与其周围环境之间的热接口

Specific Dissipation Heat Exchanger Interface (G) 模块对气体在热接口（例如换热器提供的热接口）长度方向上的压降和温度变化进行建模。热接口上的传热被忽略。有关如何组合这两个模块的示例，请参见 Heat Exchanger (G-G) 模块的复合框图。

压降根据在某些参考压力和温度下指定的表格数据计算为质量流率的函数。如果质量流率在表格数据的边界内，则计算基于线性插值；否则基于最近邻外推。换句话说，相邻数据点通过直线段连接，位于质量流率边界处的数据点则水平向外延伸。

**线性插值（左）和最近邻外推（右）**

模块计算依赖于热接口入口处流体温度、密度和比内能的状态和属性。在流动反向期间，入口会从一个端口突然切换到另一个端口，从而在这些变量的值中引入不连续。为消除这些不连续，模块会在低于指定阈值的质量流量下平滑受影响的变量。

**低于质量流量阈值的入口温度平滑**

### 质量平衡

质量可以通过端口 **A** 和 **B** 进入和离开热接口。当选择 **Enable dynamic compressibility** 时，质量平衡为

∂M∂pdpdt+∂M∂TdTdt=m˙A+m˙B,

其中：

- *M* 是热接口内部流体体积的质量。
- *p* 是内部流体压力。
- *T* 是内部流体温度。
- *m˙\** 是通过气体端口流入的质量流量。

当清除 **Enable dynamic compressibility** 复选框时，质量平衡为

m˙A+m˙B=0.

### 能量平衡

能量可以通过两种方式进入和离开热接口：通过端口 **A** 和 **B** 的流体流动，以及通过端口 **H** 的热流。当选择 **Enable dynamic compressibility** 时，能量平衡为

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH,

其中：

- *E* 是热接口内部流体体积中的总能量。
- *ϕ*\* 是通过气体端口流入的能量流率。
- *Q* 是通过热端口流入的热流率。

如果清除 **Enable dynamic compressibility** 复选框，能量平衡为

dEdt=ϕA+ϕB+QH,

其中总内部能量为

E=ρ0uV.

模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算常数 *ρ0*。

### 动量平衡

压降计算完全基于您指定的表格数据。压降的原因被忽略，除非它们可能对指定数据产生影响。从一个气体端口到另一个气体端口的总压降由从每个气体端口到内部流体体积的各个压降计算得到：

pA−pB=ΔpA−ΔpB,

其中：

- *p*\* 是气体端口处的流体压力。
- *Δp*\* 是从气体端口到内部流体体积的压降：

  Δp\*=p\*−p,

  其中 *p* 是内部流体体积中的压力。

表格数据在参考压力和温度下指定，并据此计算第三个参考参数，即 *参考密度*。参考密度与实际端口密度的比值用作各个压降方程中的修正因子，每个方程定义为：

Δp\*=Δp(m˙\*)ρRρ\*,

其中：

- *Δp(m˙)* 是表格压降函数。
- *ρ*\* 是气体端口处的流体密度。

星号表示定义参数或变量的气体端口（**A** 或 **B**）。下标 R 表示参考值。界面入口处的密度通过在质量流量阈值以下引入双曲项 *ɑ* 来平滑：

ρ\*,smooth=ρ\*(1+α2)+ρ(1−α2),

其中 *ρ*smooth 是入口端口的平滑密度，*ρ*\* 是同一端口的未平滑密度，*ρ* 是内部流体体积中的密度。双曲平滑项定义为：

α=tanh(4m˙avgm˙th),

其中 *m˙avg* 是通过气体端口的质量流率的平均值，*m˙th* 是模块对话框中指定的质量流率阈值。此阈值确定用于平滑流体密度的质量流率区域宽度。平均质量流率定义为：

m˙avg=m˙A+m˙B2
