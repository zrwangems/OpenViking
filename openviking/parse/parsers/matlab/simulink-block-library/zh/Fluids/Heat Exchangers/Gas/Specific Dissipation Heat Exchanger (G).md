---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'specificdissipationheatexchangerg'
documentation_source_path: 'ref/specificdissipationheatexchangerg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G)

## 端口
```yaml
ports:
- name: A1
  summary: 气体端口 gas
  direction: conserving
- name: B1
  summary: 气体端口 gas
  direction: conserving
- name: H2
  summary: 受控流体 2 的入口温度 thermal
  direction: conserving
- name: CP2
  summary: 受控流体的等压比热 physical signal
  direction: input
- name: M2
  summary: 受控流体的质量流量 physical signal
  direction: input
```

### 守恒端口

### **A1** — 气体端口 gas

气体进入和离开热交换器其所在侧的开口。

### **B1** — 气体端口 gas

气体进入和离开热交换器其所在侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。
### 输入

### **CP2** — 受控流体的等压比热 physical signal

受控流体等压比热的瞬时值。

### **M2** — 受控流体的质量流量 physical signal

受控流体质量流量的瞬时值。
## 参数
```yaml
parameters:
- name: Gas mass flow rate vector, mdot1
  summary: 比热耗散表查找表中每个断点处的气体质量流量 numerical array with units of mass over time
  group: 传热
- name: Controlled fluid mass flow rate vector, mdot2
  summary: 比热耗散表查找表中每个断点处的受控流体质量流量 numerical array with units of mass over time
  group: 传热
- name: Specific heat dissipation table, SD(mdot1,mdot2)
  summary: 查找表中气体和受控流体质量流量各断点处的比热耗散 numerical array with units of power over temperature
  group: 传热
- name: Check if violating maximum specific dissipation
  summary: 比热耗散超过最小热容率时的警告条件 Warning (default) | None | Error
  group: 传热
- name: Mass flow rate vector
  summary: 压降查找表中每个断点处的质量流量 numerical array with units of mass per unit time
  group: 压力损失
- name: Pressure drop vector
  summary: 查找表中质量流量各断点处的压降 numerical array with units of pressure
  group: 压力损失
- name: Reference inflow temperature
  summary: 表格数据中假定的绝对入口温度 293.15 K (default) | scalar with units of temperature
  group: 压力损失
- name: Reference inflow pressure
  summary: 表格数据中假定的绝对入口压力 0.101325 MPa (default) | scalar with units of pressure
  group: 压力损失
- name: Mass flow rate threshold for flow reversal
  summary: 质量流量数值平滑区域的上界 1e-3 kg/s (default) | scalar with units of mass/time
  group: 压力损失
- name: Gas volume
  summary: 气体流道中的流体体积 0.01 m^3 (default) | scalar with units of length cubed
  group: 压力损失
- name: Cross-sectional area at ports A1 and B1
  summary: 流道入口和出口处的流通面积 0.01 m^2 (default) | scalar with units of length squared
  group: 压力损失
- name: Enable Gas dynamic compressibility
  summary: 对气体通道中的压力动态进行建模的选项 On (default) | Off
  group: 效应和初始条件
- name: Gas nominal temperature
  summary: 额定工况下的温度 293.15 K (default) | scalar
  group: 效应和初始条件
- name: Gas nominal pressure
  summary: 额定工况下的压力 0.101325 MPa (default) | scalar
  group: 效应和初始条件
- name: Gas initial temperature
  summary: 仿真开始时气体通道中的温度 293.15 K (default) | scalar
  group: 效应和初始条件
- name: Gas initial pressure
  summary: 仿真开始时气体通道中的压力 0.101325 MPa (default) | scalar
  group: 效应和初始条件
```

### 传热

### **Gas mass flow rate vector, mdot1** — 比热耗散表查找表中每个断点处的气体质量流量 numerical array with units of mass over time

比热耗散表查找表中每个断点处的气体质量流量。该模块对断点进行内插和外推，以获得热交换器在任意质量流量下的比热耗散。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量的长度必须为 *n* 个元素。

### **Controlled fluid mass flow rate vector, mdot2** — 比热耗散表查找表中每个断点处的受控流体质量流量 numerical array with units of mass over time

比热耗散表查找表中每个断点处的受控流体质量流量。该模块对断点进行内插和外推，以获得热交换器在任意质量流量下的比热耗散。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量的长度必须为 *n* 个元素。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 查找表中气体和受控流体质量流量各断点处的比热耗散 numerical array with units of power over temperature

查找表中气体和受控流体质量流量各断点处的比热耗散。该模块对断点进行内插和外推，以获得任意气体和受控流体质量流量对下的效能。插值方法为 `linear`，外推方法为 `nearest`。

比热耗散值必须为非负值。它们必须按照气体通道中质量流量递增的顺序从上到下排列，并按照受控流体通道中质量流量递增的顺序从左到右排列。行数必须等于 **Gas mass flow rate vector** 参数的大小，列数必须等于 **Controlled fluid mass flow rate vector** 参数的大小。

如果您的热交换器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比耗散。

### **Check if violating maximum specific dissipation** — 比热耗散超过最小热容率时的警告条件 `Warning` (default) | `None` | `Error`

比热耗散超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是两股流体中较低者。该最小值给出了具有最大效能的热交换器的比耗散，且不可超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 压力损失

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量 numerical array with units of mass per unit time

压降查找表中每个断点处的质量流量。该模块对断点进行内插和外推，以获得任意质量流量下的压降。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，并与该参数结合以完成表格化的断点。

### **Pressure drop vector** — 查找表中质量流量各断点处的压降 numerical array with units of pressure

查找表中质量流量各断点处的压降。该模块对断点进行内插和外推，以获得任意质量流量下的压降。插值方法为 `linear`，外推方法为 `nearest`。

压降可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，并与该参数结合以完成表格化的断点。

### **Reference inflow temperature** — 表格数据中假定的绝对入口温度 `293.15 K` (default) | scalar with units of temperature

在收集表格化压降数据时在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格化压降，以获得实际压降。

### **Reference inflow pressure** — 表格数据中假定的绝对入口压力 `0.101325 MPa` (default) | scalar with units of pressure

在收集表格化压降数据时在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假定的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格化压降，以获得实际压降。

### **Mass flow rate threshold for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s` (default) | scalar with units of mass/time

低于该质量流量时，其值经过数值平滑处理，以避免在零流量下产生仿真误差的已知不连续性。有关交换器气体侧计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (G) 模块。

### **Gas volume** — 气体流道中的流体体积 `0.01 m^3` (default) | scalar with units of length cubed

气体流道中的流体体积。

### **Cross-sectional area at ports A1 and B1** — 流道入口和出口处的流通面积 `0.01 m^2` (default) | scalar with units of length squared

气体流道入口和出口处的流通面积。端口尺寸相同。

### 效应和初始条件

### **Enable Gas dynamic compressibility** — 对气体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas nominal temperature** — 额定工况下的温度 `293.15 K` (default) | scalar

额定工况下的气体温度。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas nominal pressure** — 额定工况下的压力 `0.101325 MPa` (default) | scalar

额定工况下的气体压力。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | scalar

仿真开始时气体通道中的温度。

### **Gas initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | scalar

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas dynamic compressibility**。
## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：可选地对动态可压缩性进行建模

Specific Dissipation Heat Exchanger (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性进行建模。此前，该模块始终对压力动态进行建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以阻止动态可压缩性建模。

### R2024a：从 Heat Exchanger (G) 模块对简单热交换器建模选项进行建模

此前，Heat Exchanger (G) 模块使用 **Modeling option** 参数对两个模块变体进行建模。该参数已被移除，这两个模块变体现在是两个独立的模块。Specific Dissipation Heat Exchanger (G) 模块使用此前当 **Modeling option** 为 `Simple model` 时所使用的传热模型。要使用当 **Modeling option** 为 `E-NTU Model` 时所使用的模块模型，请参阅 Heat Exchanger (G) 模块。

## 描述

基于比耗散数据参数化的热交换器，用于具有气体和受控流的系统

Specific Dissipation Heat Exchanger (G) 模块通过物理信号对在端口 **A1** 和 **B1** 之间流动的气体与外部*受控*流体之间的热交换进行建模。

### 传热模型

该模块的传热模型依赖于*比耗散*的概念，即当气体和受控流体入口温度相差一度时所观察到的传热速率的度量。其与入口温差的乘积给出预期的传热速率：

Q=ξ(TIn,1−TIn,2)，

其中 *ξ* 为比耗散，*T*In 为气体（下标 `1`）或受控流体（下标 `2`）的入口温度。比耗散是进入交换器的气体和受控流体入口质量流量的表格化函数：

ξ=f(m˙1,m˙2)

为适应反向流动，表格数据可以扩展到正值和负值流量范围，在这种情况下，入口也可以被视为出口。

比耗散是热交换器传热速率除以入口温差

ξ=QTIn,1−TIn,2。

比耗散也等于基于入口温度定义的总体传热系数乘以传热表面积，或热容率乘以效能因子，取两者中流体具有较小值的那个。

该传热模型几乎完全依赖于表格数据，并且由于该数据通常来自实验，因此对交换器的细节要求很少。流动布置、混合条件以及壳程或管程数量（如果与被建模的热交换器相关）假定完全体现在表格数据中。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 复合结构

该模块是一个复合组件。Specific Dissipation Heat Exchanger Interface (G) 模块对气体流动进行建模。传热系数和质量流量的物理信号，以及用于温度的热端口，捕获受控流动。Specific Dissipation Heat Transfer 模块对两股流体之间通过壁面交换的热量进行建模。
