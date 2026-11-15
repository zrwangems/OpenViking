---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'specificdissipationheatexchangerg'
documentation_source_path: 'ref/specificdissipationheatexchangerg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G)

## 端口

### 守恒

### **A1** — 气体端口 gas

气体进入和离开其热交换器一侧的开口。

### **B1** — 气体端口 gas

气体进入和离开其热交换器一侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。
### 输入

### **CP2** — 受控流体的等压比热 physical signal

受控流体的等压比热的瞬时值。

### **M2** — 受控流体的质量流量 physical signal

受控流体的质量流量的瞬时值。

## 参数

### 传热

### **Gas mass flow rate vector, mdot1** — 比耗散表查找表中每个断点处的气体质量流量，数值数组，单位为质量/时间

在比耗散表的查找表中每个断点处的气体质量流量。该模块对断点进行内插和外推，以获得热交换器在任何质量流量下的比耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但它们必须从左到右单调增加。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Controlled fluid mass flow rate vector, mdot2** — 比耗散表查找表中每个断点处的受控流体质量流量，数值数组，单位为质量/时间

在比耗散表的查找表中每个断点处的受控流体质量流量。该模块对断点进行内插和外推，以获得热交换器在任何质量流量下的比耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但它们必须从左到右单调增加。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 在气体和受控流体的质量流量上查找表中每个断点处的比耗散，数值数组，单位为功率/温度

在气体和受控流体的质量流量上，其查找表中每个断点处的比耗散。该模块对断点进行内插和外推，以获得任何气体和受控流体质量流量对下的效能。插值为 `linear`，外推为 `nearest`。

比耗散值不得为负。它们必须按照气体通道中质量流量增加的顺序从上到下对齐，并按照受控流体通道中质量流量增加的顺序从左到右对齐。行数必须等于 **Gas mass flow rate vector** 参数的大小，列数必须等于 **Controlled fluid mass flow rate vector** 参数的大小。

如果您的热交换器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比耗散。

### **Check if violating maximum specific dissipation** — 比耗散超过最小热容率时的警告条件 `Warning`（默认） | `None` | `Error`

比耗散超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是各流体中较低的值。该最小值给出了具有最大效能的热交换器的比耗散，并且不能超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 压力损失

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量，数值数组，单位为质量/时间

压降查找表中每个断点处的质量流量。该模块对断点进行内插和外推，以获得任何质量流量下的压降。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，并且可以跨越层流区、过渡区和湍流区。但是，它们必须从左到右单调增加。其数量必须等于 **Pressure drop vector** 参数的大小，它们将与该参数结合以构成完整的表格断点。

### **Pressure drop vector** — 质量流量查找表中每个断点处的压降，数值数组，单位为压力

在其关于质量流量的查找表中每个断点处的压降。该模块对断点进行内插和外推，以获得任何质量流量下的压降。插值为 `linear`，外推为 `nearest`。

压降可以为正、零或负，并且可以跨越层流区、过渡区和湍流区。但是，它们必须从左到右单调增加。其数量必须等于 **Mass flow rate vector** 参数的大小，它们将与该参数结合以构成完整的表格断点。

### **Reference inflow temperature** — 表格数据中假定的绝对入口温度 `293.15 K`（默认） | 标量，单位为温度

在采集表格压降时在入口处建立的绝对温度。参考入口温度和压力决定表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降，以获得实际压降。

### **Reference inflow pressure** — 表格数据中假定的绝对入口压力 `0.101325 MPa`（默认） | 标量，单位为压力

在采集表格压降时在入口处建立的绝对压力。参考入口温度和压力决定表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降，以获得实际压降。

### **Mass flow rate threshold for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s`（默认） | 标量，单位为质量/时间

低于此质量流量时，其值会进行数值平滑，以避免已知会在零流量时产生仿真错误的不连续性。有关热交换器气体侧计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (G) 模块。

### **Gas volume** — 气体流道中流体的体积 `0.01 m^3`（默认） | 标量，单位为长度立方

气体流道中流体的体积。

### **Cross-sectional area at ports A1 and B1** — 流道入口和出口处的流通面积 `0.01 m^2`（默认） | 标量，单位为长度平方

气体流道入口和出口处的流通面积。端口尺寸相同。

### 效应和初始条件

### **Enable Gas dynamic compressibility** — 用于对气体通道中的压力动态建模的选项 `On`（默认） | `Off`

用于对气体通道中的压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas nominal temperature** — 标称工作条件下的温度 `293.15 K`（默认） | 标量

标称工作条件下的气体温度。当动态可压缩性禁用时，该模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas nominal pressure** — 标称工作条件下的压力 `0.101325 MPa`（默认） | 标量

标称工作条件下的气体压力。当动态可压缩性禁用时，该模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas initial temperature** — 仿真开始时气体通道中的温度 `293.15 K`（默认） | 标量

仿真开始时气体通道中的温度。

### **Gas initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa`（默认） | 标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable Gas dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 可选地对动态可压缩性建模

Specific Dissipation Heat Exchanger (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。此前，此模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a: 对来自 Heat Exchanger (G) 模块的简单热交换器建模选项建模

此前，Heat Exchanger (G) 模块使用 **Modeling option** 参数对两个模块变体建模。此参数已被移除，这两个模块变体现在是两个单独的模块。Specific Dissipation Heat Exchanger (G) 模块使用先前在 **Modeling option** 为 `Simple model` 时使用的传热模型。要使用 **Modeling option** 为 `E-NTU Model` 时使用的模块模型，请参阅 Heat Exchanger (G) 模块。

## 描述

具有气体和受控流系统的、由比耗散数据参数化的热交换器

Specific Dissipation Heat Exchanger (G) 模块对在端口 **A1** 和 **B1** 之间流动的气体与外部*受控*流体之间通过物理信号进行的热交换进行建模。

### 传热模型

该模块的传热模型依赖于*比耗散*的概念，比耗散是当气体和受控流体入口温度相差一度时观察到的传热速率的度量。其与入口温差的乘积给出预期的传热速率：

Q=ξ(TIn,1−TIn,2),

其中 *ξ* 为比耗散，*T*In 为气体（下标 `1`）或受控流体（下标 `2`）的入口温度。比耗散是进入热交换器的气体和受控流体入口质量流量的表格函数：

ξ=f(m˙1,m˙2)

为适应反向流动，表格数据可以涵盖正流量和负流量，在这种情况下，入口也可以被视为出口。

比耗散是热交换器传热速率除以入口温度差

ξ=QTIn,1−TIn,2.

比耗散还等于基于入口温度定义的总传热系数乘以传热表面积，或热容率乘以效能系数（取热容率较小的流体）。

传热模型由于几乎完全依赖表格数据，并且该数据通常来自实验，因此几乎不需要有关热交换器的详细信息。如果与被建模的热交换器相关，流动布置、混合条件以及壳程或管程数假定完全体现在表格数据中。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 复合结构

该模块是一个复合组件。Specific Dissipation Heat Exchanger Interface (G) 模块对气体流建模。传热系数和质量流量的物理信号，以及用于温度的热端口，表示受控流。Specific Dissipation Heat Transfer 模块对流之间通过壁面交换的热量建模。
