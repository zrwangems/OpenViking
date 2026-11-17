---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'specificdissipationheatexchangergg'
documentation_source_path: 'ref/specificdissipationheatexchangergg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G-G)

## 端口

### 守恒端口

### **A1** — 气体 1 端口 gas

气体 1 进入和离开热交换器其所在侧的开口。

### **B1** — 气体 1 端口 gas

气体 1 进入和离开热交换器其所在侧的开口。

### **A2** — 气体 2 端口 gas

气体 2 进入和离开热交换器其所在侧的开口。

### **B2** — 气体 2 端口 gas

气体 2 进入和离开热交换器其所在侧的开口。

## 参数

### Heat Transfer

### **Gas 1 mass flow rate vector, mdot1** — 比散热表查找表中每个断点处气体 1 的质量流量，数值数组，单位为质量除以时间

比散热表查找表中每个断点处气体 1 的质量流量。该模块对断点进行内插和外插，以获得热交换器在任何质量流量下的比散热。插值方法为 `linear`，外插方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素。

### **Gas 2 mass flow rate vector, mdot2** — 比散热表查找表中每个断点处气体 2 的质量流量，数值数组，单位为质量除以时间

比散热表查找表中每个断点处气体 2 的质量流量。该模块对断点进行内插和外插，以获得热交换器在任何质量流量下的比散热。插值方法为 `linear`，外插方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 查找表中气体 1 和气体 2 质量流量各断点处的比散热，数值数组，单位为功率除以温度

查找表中气体 1 和气体 2 质量流量各断点处的比散热。该模块对断点进行内插和外插，以获得任何一对气体 1 和气体 2 质量流量下的效能。插值方法为 `linear`，外插方法为 `nearest`。

比散热值不得为负。它们必须按照气体 1 通道中质量流量递增的顺序从上到下排列，并按照气体 2 通道中质量流量递增的顺序从左到右排列。行数必须等于 **Gas 1 mass flow rate vector** 参数的大小，列数必须等于 **Gas 2 mass flow rate vector** 参数的大小。

如果您的热交换器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比散热。

### **Check if violating maximum specific dissipation** — 比散热超过最小热容率时的警告条件 `Warning`（默认）| `None` | `Error`

比散热超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是两股流体中较低者。该最小值给出了具有最大效能的热交换器的比散热，且不可超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Gas 1|2

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量，数值数组，单位为质量除以单位时间

压降查找表中每个断点处的质量流量。该模块对断点进行内插和外插，以获得任何质量流量下的压降。插值方法为 `linear`，外插方法为 `nearest`。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，它们将与之组合以完成制表断点。

### **Pressure drop vector** — 质量流量查找表中每个断点处的压降，数值数组，单位为压力

质量流量查找表中每个断点处的压降。该模块对断点进行内插和外插，以获得任何质量流量下的压降。插值方法为 `linear`，外插方法为 `nearest`。

压降可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，它们将与之组合以完成制表断点。

### **Reference inflow temperature** — 制表数据中假设的绝对入口温度 `293.15 K`（默认）| 标量，单位为温度

在收集制表压降时在入口处建立的绝对温度。参考入口温度和压力决定了制表数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以制表压降以获得实际压降。

### **Reference inflow pressure** — 制表数据中假设的绝对入口压力 `0.101325 MPa`（默认）| 标量，单位为压力

在收集制表压降时在入口处建立的绝对压力。参考入口温度和压力决定了制表数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以制表压降以获得实际压降。

### **Threshold mass flow rate for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s`（默认）| 标量，单位为质量/时间

低于该质量流量时，其值经过数值平滑以避免在零流量下产生仿真误差的不连续性。有关计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (G) 模块。

### **Fluid volume** — 气体 1 或气体 2 流道中的流体体积 `0.01 m^3`（默认）| 标量，单位为长度的立方

气体 1 或气体 2 流道中的流体体积。

### **Cross-sectional area at ports A and B** — 流道入口和出口处的流通面积 `0.01 m^2`（默认）| 标量，单位为长度的平方

气体 1 或气体 2 流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### Effects and Initial Conditions

### **Enable Gas 1 dynamic compressibility** — 对气体通道中压力动态建模的选项 `On`（默认）| `Off`

对气体通道中压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K`（默认）| 标量，单位为温度

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa`（默认）| 标量，单位为压力

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas 1 dynamic compressibility**。

### **Enable Gas 2 dynamic compressibility** — 对气体通道中压力动态建模的选项 `On`（默认）| `Off`

对气体通道中压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 2 nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 2 dynamic compressibility** 复选框。

### **Gas 2 nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 2 dynamic compressibility** 复选框。

### **Gas 2 initial temperature** — 仿真开始时气体 2 通道中的温度 `293.15 K`（默认）| 标量，单位为温度

仿真开始时气体 2 通道中的温度。

### **Gas 2 initial pressure** — 仿真开始时气体 2 通道中的压力 `0.101325 MPa`（默认）| 标量，单位为压力

仿真开始时气体 2 通道中的压力。

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

Specific Dissipation Heat Exchanger (G-G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。此前，该模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：从 Heat Exchanger (G-G) 模块中建模简单热交换器建模选项

此前，Heat Exchanger (G-G) 模块使用 **Modeling option** 参数来建模两个模块变体。此参数已被移除，两个模块变体现在是两个独立的模块。Specific Dissipation Heat Exchanger (G-G) 模块使用此前当 **Modeling option** 为 `Simple model` 时使用的传热模型。要使用当 **Modeling option** 为 `E-NTU Model` 时使用的模块模型，请参阅 Heat Exchanger (G-G) 模块。

## 描述

基于比散热数据参数化的热交换器，适用于具有两股气流的系统

Specific Dissipation Heat Exchanger (G-G) 模块对气-气热交换器建模。流体为单相，且各为一种气体。两种流体均不能发生相变，因此，由于潜热永远不会释放，交换严格为显热交换。

### 传热模型

该模块的传热模型依赖于*比散热*的概念，即当气体 1 和气体 2 入口温度相差一度时观察到的传热速率的度量。其与入口温差的乘积给出预期的传热速率：

Q=ξ(TIn,1−TIn,2),

其中 *ξ* 为比散热，*T*In 为气体 1（下标 `1`）或气体 2（下标 `2`）的入口温度。比散热是进入交换器的气体 1 和气体 2 入口质量流量的制表函数：

ξ=f(m˙1,m˙2)

为适应反向流动，制表数据可以扩展到正值和负值流量范围，在这种情况下，入口也可以被视为出口。

比散热是热交换器传热速率除以入口温度差

ξ=QTIn,1−TIn,2。

比散热还等于基于入口温度定义的总体传热系数乘以传热表面积，或热容率乘以效能因子（取两种流体中较小值者）。

传热模型几乎完全依赖于制表数据，且该数据通常来自实验，因此对交换器的细节要求很少。流动布置、混合条件以及壳程或管程数（如果与被建模的热交换器相关）假定完全体现在制表数据中。

该模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

有关传热计算的更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块是一个复合组件。一个 Specific Dissipation Heat Exchanger Interface (G) 模块对热交换器侧 1 的气体流动建模。另一个对侧 2 的气体流动建模。一个 Specific Dissipation Heat Transfer 模块捕获两股流体之间通过壁面交换的热量。
