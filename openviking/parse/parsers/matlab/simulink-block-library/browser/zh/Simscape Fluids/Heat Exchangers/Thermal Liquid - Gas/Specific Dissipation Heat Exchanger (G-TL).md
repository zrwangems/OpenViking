---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'specificdissipationheatexchangergtl'
documentation_source_path: 'ref/specificdissipationheatexchangergtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G-TL)

## 端口

### 守恒

### **A1** — Gas 端口 gas

气体进入和离开热交换器其侧的开口。

### **B1** — Gas 端口 gas

气体进入和离开热交换器其侧的开口。

### **A2** — Thermal liquid 端口 thermal liquid

热液体进入和离开热交换器其侧的开口。

### **B2** — Thermal liquid 端口 thermal liquid

热液体进入和离开热交换器其侧的开口。

## 参数

### 传热

### **Gas 1 mass flow rate vector, mdot1** — 气体在比散热表查找表中每个断点处的质量流量 numerical array with units of mass over time

气体在比散热表查找表中每个断点处的质量流量。模块对这些断点进行内插和外推，以获得任意质量流量下的比散热。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation** 表参数中的行数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *m* 个元素长。

### **Thermal Liquid 2 mass flow rate vector, mdot2** — 热液体在比散热表查找表中每个断点处的质量流量 numerical array with units of mass over time

热液体在比散热表查找表中每个断点处的质量流量。模块对这些断点进行内插和外推，以获得任意质量流量下热交换器的比散热。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Specific heat dissipation table, SD(mdot1, mdot2)** — 在气体和热液体的质量流量上，比散热表查找表中每个断点处的比散热 numerical array with units of power over temperature

在气体和热液体的质量流量上，比散热表查找表中每个断点处的比散热。模块对这些断点进行内插和外推，以获得任意气体和热液体质量流量对下的效能。插值为 `linear`，外推为 `nearest`。

比散热值必须非负。它们必须从上到下按气体通道中质量流量递增的顺序排列，并且从左到右按热液体通道中质量流量递增的顺序排列。行数必须等于 **Gas 1 mass flow rate vector** 参数的大小，列数必须等于 **Thermal liquid 2 mass flow rate vector** 参数的大小。

如果您的热交换器数据表提供了传热系数，则将提供的传热系数乘以表面积，以计算比散热。

### **Check if violating maximum specific dissipation** — 比散热超过最小热容量率时的警告条件 `Warning` (default) | `None` | `Error`

比散热超过最小热容量率时的警告条件。热容量率是质量流量与比热的乘积，其最小值是各流之间的最低值。该最小值给出了具有最大效能的热交换器的比散热，且不能超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Gas 1

### **Mass flow rate vector** — 压力降查找表中每个断点处的质量流量 numerical array with units of mass per unit time

压力降查找表中每个断点处的质量流量。模块使用线性插值和最近邻外推来获得任意质量流量下的压力降。

质量流量可以为正、零或负，并且可以跨越层流、过渡流和湍流区域。该向量必须与 **Pressure drop vector** 参数具有相同数量的元素，并且这些元素必须从左到右单调递增。

### **Pressure drop vector** — 在质量流量上，压力降查找表中每个断点处的压力降 numerical array with units of pressure

在质量流量上，压力降查找表中每个断点处的压力降。模块使用线性插值和最近邻外推来获得任意质量流量下的压力降。

压力降可以为正、零或负，并且可以跨越层流、过渡流和湍流区域。该向量必须与 **Mass flow rate vector** 参数具有相同数量的元素，并且这些元素必须从左到右单调递增。

### **Reference inflow temperature** — 表格数据中假定的绝对入口温度 `293.15 K` (default) | scalar with units of temperature

在收集表格压力降时，在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Reference inflow pressure** — 表格数据中假定的绝对入口压力 `0.101325 MPa` (default) | scalar with units of pressure

在收集表格压力降时，在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Mass flow rate threshold for flow reversal** — 质量流量的数值平滑区域上界 `1e-3 kg/s` (default) | scalar with units of mass/time

低于该质量流量时，其值经过数值平滑以避免不连续性。有关计算的详细信息，请参阅 Simple Heat Exchanger Interface 模块。

### **Gas 1 volume** — 气体流动通道中的流体体积 `0.01 m^3` (default) | scalar with units of length cubed

气体流动通道中的流体体积。

### **Cross-sectional area at ports A1 and B1** — 流动通道入口和出口处的流通面积 `0.01 m^2` (default) | scalar with units of length squared

气体流动通道入口和出口处的流通面积。同一流动通道中的端口尺寸相同。

### Thermal Liquid 2

### **Mass flow rate vector** — 压力降查找表中每个断点处的质量流量 numerical array with units of mass per unit time

压力降查找表中每个断点处的质量流量。模块使用线性插值和最近邻外推来获得任意质量流量下的压力降。

质量流量可以为正、零或负，并且可以跨越层流、过渡流和湍流区域。该向量必须与 **Pressure drop vector** 参数具有相同数量的元素，并且这些元素必须从左到右单调递增。

### **Pressure drop vector** — 在质量流量上，压力降查找表中每个断点处的压力降 numerical array with units of pressure

在质量流量上，压力降查找表中每个断点处的压力降。模块使用线性插值和最近邻外推来获得任意质量流量下的压力降。

压力降可以为正、零或负，并且可以跨越层流、过渡流和湍流区域。该向量必须与 **Mass flow rate vector** 参数具有相同数量的元素，并且这些元素必须从左到右单调递增。

### **Reference inflow temperature** — 表格数据中假定的绝对入口温度 `293.15 K` (default) | scalar with units of temperature

在收集表格压力降时，在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Reference inflow pressure** — 表格数据中假定的绝对入口压力 `0.101325 MPa` (default) | scalar with units of pressure

在收集表格压力降时，在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Mass flow rate threshold for flow reversal** — 质量流量的数值平滑区域上界 `1e-3 kg/s` (default) | scalar with units of mass/time

低于该质量流量时，其值经过数值平滑以避免不连续性。有关计算的详细信息，请参阅 Simple Heat Exchanger Interface 模块。

### **Thermal Liquid 2 volume** — 热液体流动通道中的流体体积 `0.01 m^3` (default) | scalar with units of length cubed

热液体流动通道中的流体体积。

### **Cross-sectional area at ports A2 and B2** — 流动通道入口和出口处的流通面积 `0.01 m^2` (default) | scalar with units of length squared

热液体流动通道入口和出口处的流通面积。同一流动通道中的端口尺寸相同。

### 效应与初始条件

### **Enable Gas 1 dynamic compressibility** — 对气体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | scalar

标称工作条件下的气体温度。当动态压缩性禁用时，模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | scalar

标称工作条件下的气体压力。当动态压缩性禁用时，模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | scalar with units of pressure

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable Gas 1 dynamic compressibility**。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对热液体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。热交换器内部的压力则降低为两个端口压力的加权平均值。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时热液体通道中的温度。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对热液体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。热交换器内部的压力则降低为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | scalar

标称工作条件下的热液体温度。当动态压缩性禁用时，模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | scalar

标称工作条件下的热液体压力。当动态压缩性禁用时，模块使用此值计算质量与能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时热液体通道中的温度

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa` (default) | scalar with units of pressure

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable Thermal Liquid 2 dynamic compressibility** 。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 可选地建模动态压缩性

Specific Dissipation Heat Exchanger (G-TL) 模块现在可以通过使用 **Enable dynamic compressibility** 参数可选地建模动态压缩性。以前，此模块始终建模压力动态，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态压缩性建模。

### R2024a: 为 Heat Exchanger (G-TL) 模块建模简单的热交换器建模选项

以前，Heat Exchanger (G-TL) 模块使用 **Modeling option** 参数来建模两种模块变体。此参数已被移除，两种模块变体现为两个独立的模块。Specific Dissipation Heat Exchanger (G-TL) 模块使用以前当 **Modeling option** 为 `Simple model` 时所用的传热模型。要使用以前当 **Modeling option** 为 `E-NTU Model` 时所用的模块模型，请参阅 Heat Exchanger (G-TL) 模块。

## 描述

基于比耗散数据参数化的、用于具有气体和热液体流的系统的热交换器

Specific Dissipation Heat Exchanger (G-TL) 模块对短暂地通过薄导热壁保持热接触的流体进行互补冷却和加热建模。流体为单相，一侧为纯气体，另一侧为纯液体。两种流体都不能发生相变，因此由于始终不释放潜热，交换严格为显热交换。

显热交换器在机械中随处可见。某些喷气式飞机中的燃油加热器通过将仍来自压气机的热引气吹过燃油管路，防止冰在燃油管路中析出并堵塞燃油滤网。某些摩托车中的油冷却器同样通过将环境温度的冲压空气快速吹过油路，防止润滑油过热。引气和冲压空气是气体流，燃油和油是热液体流。

### 传热模型

该模块的传热模型取决于比耗散，比耗散是当气体和热液体入口温度相差一度时观察到的传热速率的一种度量。其与入口温差的乘积给出预期的传热速率

Q=ξ(TIn,G−TIn,TL),

其中 *ξ* 是比耗散，*TIn* 是气体（下标 `G`）或热液体（下标 `TL`）的入口温度。比耗散是流经气体入口和热液体入口进入交换器的质量流率的表格函数：

ξ=f(m˙In,G,m˙In,TL),

为了适应反向流，表格数据可以扩展到正流量和负流量，在这种情况下，入口也可以被视为出口。

比耗散是热交换器传热速率除以入口温度差

ξ=QTIn,1−TIn,2.

比耗散还等于基于入口温度定义的总传热系数乘以传热表面积，或等于值较小的流体的热容量率乘以效能因子。

由于传热模型几乎完全依赖表格数据，且该数据通常来自实验，因此它几乎不需要有关交换器的细节。流动布置、混合条件以及壳程或管程数（如果与被建模的热交换器相关）被假定完全体现在表格数据中。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

有关传热计算的更多详细信息，请参见 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块是一个复合组件。Specific Dissipation Heat Exchanger Interface (G) 模块对气体流建模，Specific Dissipation Heat Exchanger Interface (TL) 模块对热液体流建模。流道中的质量、动量和能量守恒来自相应的接口模块。Specific Dissipation Heat Transfer 模块捕获流之间通过壁交换的热量。
