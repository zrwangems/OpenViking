---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'specificdissipationheatexchangergg'
documentation_source_path: 'ref/specificdissipationheatexchangergg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G-G)

## 端口

### 守恒

### **A1** — Gas 1 端口 gas

Gas 1 进入和离开换热器其侧的开口。

### **B1** — Gas 1 端口 gas

Gas 1 进入和离开换热器其侧的开口。

### **A2** — Gas 2 端口 gas

Gas 2 进入和离开换热器其侧的开口。

### **B2** — Gas 2 端口 gas

Gas 2 进入和离开换热器其侧的开口。

## 参数

### 传热

### **Gas 1 mass flow rate vector, mdot1** — Gas 1 在比热耗散表的查找表中每个断点处的质量流量，数值数组，单位为 mass over time

Gas 1 在比热耗散表的查找表中每个断点处的质量流量。模块对断点进行内插和外插，以获得换热器在任意质量流量下的比热耗散。插值为 `linear`，外插为 `nearest`。

质量流量可以为正、零或负，但它们必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Gas 2 mass flow rate vector, mdot2** — Gas 2 在比热耗散表的查找表中每个断点处的质量流量，数值数组，单位为 mass over time

Gas 2 在比热耗散表的查找表中每个断点处的质量流量。模块对断点进行内插和外插，以获得换热器在任意质量流量下的比热耗散。插值为 `linear`，外插为 `nearest`。

质量流量可以为正、零或负，但它们必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素长。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 在 Gas 1 和 Gas 2 质量流量上的查找表中每个断点处的比热耗散，数值数组，单位为 power over temperature

比热耗散在 Gas 1 和 Gas 2 质量流量上的查找表中每个断点处的值。模块对断点进行内插和外插，以获得任意 Gas 1 和 Gas 2 质量流量对下的效能。插值为 `linear`，外插为 `nearest`。

比热耗散值必须为非负。它们必须从上到下按 Gas 1 通道中质量流量递增的顺序排列，并且从左到右按 Gas 2 通道中质量流量递增的顺序排列。行数必须等于 **Gas 1 mass flow rate vector** 参数的大小，列数必须等于 **Gas 2 mass flow rate vector** 参数的大小。

如果您的换热器数据表提供了传热系数，请将提供的传热系数乘以其表面积，以计算比耗散。

### **Check if violating maximum specific dissipation** — 比热耗散超过最小热容量率时的警告条件 `Warning` (default) | `None` | `Error`

比热耗散超过最小热容量率时的警告条件。热容量率是质量流量与比热的乘积，其最小值是两个流之间的最低值。该最小值给出了具有最大效能的换热器的比耗散，且不能超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Gas 1|2

### **Mass flow rate vector** — 压力降查找表中每个断点处的质量流量，数值数组，单位为 mass per unit time

压力降查找表中每个断点处的质量流量。模块对断点进行内插和外插，以获得任意质量流量下的压力降。插值为 `linear`，外插为 `nearest`。

质量流量可以为正、零或负，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，它们将与之组合以完成制表的断点。

### **Pressure drop vector** — 质量流量上的查找表中每个断点处的压力降，数值数组，单位为 pressure

压力降在其关于质量流量的查找表中每个断点处的值。模块对断点进行内插和外插，以获得任意质量流量下的压力降。插值为 `linear`，外插为 `nearest`。

压力降可以为正、零或负，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，它们将与之组合以完成制表的断点。

### **Reference inflow temperature** — 制表数据中假设的绝对入口温度 `293.15 K` (default) | 标量，单位为温度

在收集制表压力降时在入口处建立的绝对温度。参考入口温度和压力决定了制表数据中假设的流体密度。在仿真过程中，参考流体密度与实际流体密度之比乘以制表压力降，以获得实际压力降。

### **Reference inflow pressure** — 制表数据中假设的绝对入口压力 `0.101325 MPa` (default) | 标量，单位为压力

在收集制表压力降时在入口处建立的绝对压力。参考入口温度和压力决定了制表数据中假设的流体密度。在仿真过程中，参考流体密度与实际流体密度之比乘以制表压力降，以获得实际压力降。

### **Threshold mass flow rate for flow reversal** — 质量流量的数值平滑区域上限 `1e-3 kg/s` (default) | 标量，单位为 mass/time

低于该质量流量时，其值会被数值平滑，以避免在零流量下已知会产生仿真错误的不连续性。有关计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (G) 模块。

### **Fluid volume** — Gas 1 或 Gas 2 流道中的流体体积 `0.01 m^3` (default) | 标量，单位为 length cubed

Gas 1 或 Gas 2 流道中的流体体积。

### **Cross-sectional area at ports A and B** — 流道入口和出口处的流通面积 `0.01 m^2` (default) | 标量，单位为 length squared

Gas 1 或 Gas 2 流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### 效应和初始条件

### **Enable Gas 1 dynamic compressibility** — 对气体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | 标量

标称工作条件下的气体温度。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | 标量

标称工作条件下的气体压力。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | 标量，单位为温度

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | 标量，单位为压力

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas 1 dynamic compressibility**。

### **Enable Gas 2 dynamic compressibility** — 对气体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 2 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | 标量

标称工作条件下的气体温度。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 2 dynamic compressibility** 复选框。

### **Gas 2 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | 标量

标称工作条件下的气体压力。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 2 dynamic compressibility** 复选框。

### **Gas 2 initial temperature** — 仿真开始时 Gas 2 通道中的温度 `293.15 K` (default) | 标量，单位为温度

仿真开始时 Gas 2 通道中的温度。

### **Gas 2 initial pressure** — 仿真开始时 Gas 2 通道中的压力 `0.101325 MPa` (default) | 标量，单位为压力

仿真开始时 Gas 2 通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas 2 dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：可选地对动态可压缩性建模

Specific Dissipation Heat Exchanger (G-G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性进行建模。以前，此模块始终对压力动态进行建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：从 Heat Exchanger (G-G) 模块对简单换热器建模选项进行建模

以前，Heat Exchanger (G-G) 模块使用 **Modeling option** 参数对两个模块变体进行建模。此参数已被移除，两个模块变体现在是两个单独的模块。Specific Dissipation Heat Exchanger (G-G) 模块使用以前在 **Modeling option** 为 `Simple model` 时使用的传热模型。要使用 **Modeling option** 为 `E-NTU Model` 时使用的模块模型，请参阅 Heat Exchanger (G-G) 模块。

## 描述

用于具有两个气体流的系统、由比耗散数据参数化的换热器

Specific Dissipation Heat Exchanger (G-G) 模块对气-气换热器进行建模。流体为单相，且均为气体。两种流体都不能发生相变，因此，由于潜热永远不会释放，交换严格为显热交换。

### 传热模型

模块传热模型依赖于 *比耗散* 的概念，它衡量当 Gas 1 和 Gas 2 入口温度相差一度时观察到的传热速率。其与入口温差的乘积给出预期的传热速率：

Q=ξ(TIn,1−TIn,2),

其中 *ξ* 是比耗散，*T*In 是 Gas 1（下标 `1`）或 Gas 2（下标 `2`）的入口温度。比耗散是通过 Gas 1 和 Gas 2 入口进入换热器的质量流量的制表函数：

ξ=f(m˙1,m˙2)

为了适应逆流，制表数据可以扩展到正流量和负流量，在这种情况下，入口也可以被视为出口。

比耗散是换热器传热速率除以入口温度差

ξ=QTIn,1−TIn,2.

比耗散还等于基于入口温度定义的总传热系数乘以传热表面积，或热容量率乘以效能因子，取两者中较小值的流体。

由于传热模型几乎完全依赖于制表数据，并且该数据通常来自实验，因此对换热器的细节要求很少。流动布置、混合条件以及壳程或管程数（如果与被建模的换热器相关）被假定完全体现在制表数据中。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值的平均值。

有关传热计算的更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块是一个复合组件。一个 Specific Dissipation Heat Exchanger Interface (G) 模块对换热器侧 1 的气体流进行建模。另一个模块对侧 2 的气体流进行建模。一个 Specific Dissipation Heat Transfer 模块捕获跨壁在流之间交换的热量。
