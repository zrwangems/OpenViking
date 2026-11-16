---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'specificdissipationheatexchangertltl'
documentation_source_path: 'ref/specificdissipationheatexchangertltl.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (TL-TL)

## 端口

### 守恒

### **A1** — 热液体 1 端口 thermal liquid

用于热液体 1 进入和离开其换热器侧的开口。

### **B1** — 热液体 1 端口 thermal liquid

用于热液体 1 进入和离开其换热器侧的开口。

### **A2** — 热液体 2 端口 thermal liquid

用于热液体 2 进入和离开其换热器侧的开口。

### **B2** — 热液体 2 端口 thermal liquid

用于热液体 2 进入和离开其换热器侧的开口。

## 参数

### 传热

### **Thermal Liquid 1 mass flow rate vector, mdot1** — 在比热耗散表的查找表中每个断点处的热液体 1 质量流量，数值数组，单位为质量/时间

在比热耗散表的查找表中每个断点处的热液体 1 质量流量。该模块对断点进行内插和外推，以获得换热器在任意质量流量下的比热耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Thermal Liquid 2 mass flow rate vector, mdot2** — 在比热耗散表的查找表中每个断点处的热液体 2 质量流量，数值数组，单位为质量/时间

在比热耗散表的查找表中每个断点处的热液体 2 质量流量。该模块对断点进行内插和外推，以获得换热器在任意质量流量下的比热耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 在热液体 1 和热液体 2 质量流量上的查找表中每个断点处的比热耗散，数值数组，单位为功率/温度

在热液体 1 和热液体 2 的质量流量所对应的查找表中，每个断点处的比热耗散。该模块对断点进行内插和外推，以获得任意一对热液体 1 和热液体 2 质量流量下的效能。插值为 `linear`，外推为 `nearest`。

比热耗散值不得为负。它们必须按热液体 1 通道中质量流量递增的顺序从上到下排列，并按热液体 2 通道中质量流量递增的顺序从左到右排列。行数必须等于 **Thermal liquid 1 mass flow rate vector** 参数的大小，列数必须等于 **Thermal liquid 2 mass flow rate vector** 参数的大小。

如果您的换热器数据表提供传热系数，则将提供的传热系数乘以表面积，以计算比耗散。

### **Check if violating maximum specific dissipation** — 当比热耗散超过最小热容率时的警告条件 `Warning`（默认）| `None` | `Error`

当比热耗散超过最小热容率时的警告条件。热容率是质量流量与比热容的乘积，其最小值是两个流之间的较低值。该最小值给出了具有最大效能的换热器的比耗散，且不能超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Thermal Liquid 1|2 选项卡

### **Mass flow rate vector** — 在压力降查找表中每个断点处的质量流量，数值数组，单位为质量/时间

压力降查找表中每个断点处的质量流量。该模块对断点进行内插和外推，以获得任意质量流量下的压力降。插值为 `linear`，外推为 `nearest`。

质量流量可以为正、零或负，并且可以跨越层流、过渡流和湍流区。但是，它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，二者组合以构成完整的表格断点。

### **Pressure drop vector** — 在质量流量上的查找表中每个断点处的压力降，数值数组，单位为压力

压力降在其关于质量流量的查找表中每个断点处的值。该模块对断点进行内插和外推，以获得任意质量流量下的压力降。插值为 `linear`，外推为 `nearest`。

压力降可以为正、零或负，并且可以跨越层流、过渡流和湍流区。但是，它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，二者组合以构成完整的表格断点。

### **Reference inflow temperature** — 表格数据中假定的绝对入口温度 `293.15 K`（默认）| 具有温度单位的标量

在采集表格压力降数据时在入口处设定的绝对温度。参考入口温度和压力决定了表格数据中假定的流体密度。仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Reference inflow pressure** — 表格数据中假定的绝对入口压力 `0.101325 MPa`（默认）| 具有压力单位的标量

在采集表格压力降数据时在入口处设定的绝对压力。参考入口温度和压力决定了表格数据中假定的流体密度。仿真期间，参考流体密度与实际流体密度之比乘以表格压力降，以获得实际压力降。

### **Threshold mass flow rate for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s`（默认）| 具有质量/时间单位的标量

低于该质量流量时，其值经过数值平滑，以避免已知会在零流量下产生仿真错误的不连续。有关计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (TL) 模块。

### **Thermal liquid volume** — 热液体 1 或热液体 2 流道中的流体体积 `0.01 m^3`（默认）| 具有长度立方单位的标量

热液体 1 或热液体 2 流道中的流体体积。

### **Cross-sectional area at ports A and B** — 流道入口和出口处的流通面积 `0.01 m^2`（默认）| 具有长度平方单位的标量

热液体 1 或热液体 2 流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### 效应和初始条件

### **Enable Thermal Liquid 1 dynamic compressibility** — 换热器中液体可压缩性的设置 `On`（默认）| `Off` | 标量

用于对换热器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。然后，换热器内部压力简化为两个端口压力的加权平均值。

### **Thermal Liquid 1 nominal temperature** — 标称工作条件下的温度 `293.15 K`（默认）| 标量

标称工作条件下的热液体温度。当动态可压缩性禁用时，该模块使用此值计算质量守恒和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 1 dynamic compressibility** 复选框。

### **Thermal Liquid 1 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa`（默认）| 标量

标称工作条件下的热液体压力。当动态可压缩性禁用时，该模块使用此值计算质量守恒和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 1 dynamic compressibility** 复选框。

### **Thermal Liquid 1 initial temperature** — 仿真开始时热液体 1 中的温度 `293.15 K`（默认）| 具有温度单位的标量

仿真开始时热液体 1 通道中的温度。

### **Thermal Liquid 1 initial pressure** — 仿真开始时热液体 1 通道中的压力 `0.101325 MPa`（默认）| 具有压力单位的标量

仿真开始时热液体 1 通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable Thermal Liquid 1 dynamic compressibility**。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体 2 通道中的压力动态进行建模的选项 `On`（默认）| `Off`

用于对热液体 2 通道中的压力动态进行建模的选项。如果清除此复选框，该模块会从组件能量和质量守恒方程中移除压力导数项。然后，换热器内部压力简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 标称工作条件下的温度 `293.15 K`（默认）| 标量

标称工作条件下的热液体温度。当动态可压缩性禁用时，该模块使用此值计算质量守恒和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa`（默认）| 标量

标称工作条件下的热液体压力。当动态可压缩性禁用时，该模块使用此值计算质量守恒和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体 1 中的温度 `293.15 K`（默认）| 具有温度单位的标量

仿真开始时热液体 2 通道中的温度。

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体 1 通道中的压力 `0.101325 MPa`（默认）| 具有压力单位的标量

仿真开始时热液体 1 通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable Thermal Liquid 2 dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024a: 对 Heat Exchanger (TL-TL) 模块中的简单换热器建模选项进行建模

以前，Heat Exchanger (TL-TL) 模块使用 **Modeling option** 参数对两个模块变体进行建模。此参数已被移除，这两个模块变体现已是两个单独的模块。Specific Dissipation Heat Exchanger (TL-TL) 模块使用以前在 **Modeling option** 为 `Simple model` 时使用的传热模型。若要使用在 **Modeling option** 为 `E-NTU Model` 时使用的模块模型，请参阅 Heat Exchanger (TL-TL) 模块。

## 描述

由比耗散数据参数化、用于具有两个热液体流的系统的换热器

Specific Dissipation Heat Exchanger (TL-TL) 模块对流体通过薄导热壁短暂热接触时的互补冷却和加热进行建模。该模块使用基于比耗散概念的简化模型，比耗散是传热速率的一种度量。

### 传热模型

该模块的传热模型取决于由比耗散定义的传热速率。比耗散是当热液体 1 和热液体 2 入口温度相差一度时观察到的传热速率的度量。其与入口温度差的乘积给出预期的传热速率

Q=ξ(TIn,1−TIn,2),

其中 *ξ* 是比耗散，*TIn* 是热液体 1（下标 `1`）或热液体 2（下标 `2`）的入口温度。比耗散是进入换热器的、流经热液体 1 和热液体 2 入口的质量流量的表格函数：

ξ=f(m˙1,m˙2)

为适应反向流动，表格数据可以涵盖正流量和负流量，在这种情况下，入口也可以视为出口。

比耗散是换热器传热速率除以入口温度差

ξ=QTIn,1−TIn,2.

比耗散还等于基于入口温度定义的总传热系数乘以传热表面积，或热容率乘以效能因子，取流体中值较小者。

该传热模型几乎完全依赖表格数据，并且这些数据通常来自实验，因此几乎不需要关于换热器的详细信息。如果与所建模的换热器相关，流动布置、混合条件以及壳程或管程数都假定完全体现在表格数据中。

该模块在传热计算中使用的流体属性是入口处值与流体体积中值的平均值。

有关传热计算的更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块是一个复合组件。一个 Specific Dissipation Heat Exchanger Interface (TL) 模块对换热器侧 1 上的热液体流进行建模。另一个模块对侧 2 上的热液体流进行建模。一个 Specific Dissipation Heat Transfer 模块捕获流体之间通过壁交换的热量。
