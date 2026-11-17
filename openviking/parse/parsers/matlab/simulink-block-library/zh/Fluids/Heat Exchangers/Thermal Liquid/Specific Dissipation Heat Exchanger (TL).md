---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'specificdissipationheatexchangertl'
documentation_source_path: 'ref/specificdissipationheatexchangertl.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (TL)

## 端口

### 守恒端口

### **A1** — 热液体端口 thermal liquid

热液体进入和离开换热器其侧的开孔。

### **B1** — 热液体端口 thermal liquid

热液体进入和离开换热器其侧的开孔。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。
### 输入

### **CP2** — 受控流体的等压比热 physical signal

受控流体的等压比热的瞬时值。

### **M2** — 受控流体的质量流量 physical signal

受控流体的质量流量的瞬时值。

## 参数

### 传热

### **Thermal liquid mass flow rate vector, mdot1** — 比热耗散表查找表中每个断点处的热液体质量流量 numerical array with units of mass over time

比热耗散表查找表中每个断点处的热液体质量流量。该模块对断点进行内插和外推，以获得换热器在任何质量流量下的比热耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量的长度必须为 *n* 个元素。

### **Controlled fluid mass flow rate vector, mdot2** — 比热耗散表查找表中每个断点处的受控流体质量流量 numerical array with units of mass over time

比热耗散表查找表中每个断点处的受控流体质量流量。该模块对断点进行内插和外推，以获得换热器在任何质量流量下的比热耗散。插值为 `linear`，外推为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量的长度必须为 *n* 个元素。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 热液体和受控流体质量流量查找表中每个断点处的比热耗散 numerical array with units of power over temperature

热液体和受控流体质量流量查找表中每个断点处的比热耗散。该模块对断点进行内插和外推，以获得任何一对热液体和受控流体质量流量下的效能。插值为 `linear`，外推为 `nearest`。

比热耗散值不得为负。它们必须按照热液体通道中质量流量递增的顺序从上到下排列，并按照受控流体通道中质量流量递增的顺序从左到右排列。行数必须等于 **Thermal liquid mass flow rate vector** 参数的大小，列数必须等于 **Controlled fluid mass flow rate vector** 参数的大小。

如果您的换热器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比耗散。

### **Check if violating maximum specific dissipation** — 比热耗散超过最小热容率时的警告条件 `Warning` (default) | `None` | `Error`

比热耗散超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是两股流体中较低者。该最小值给出了具有最大效能的换热器的比耗散，且不能被超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 压降

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量 numerical array with units of mass per unit time

压降查找表中每个断点处的质量流量。该模块对断点进行内插和外推，以获得任何质量流量下的压降。插值为 `linear`，外推为 `nearest`。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，它们将与之组合以完成表格化的断点。

### **Pressure drop vector** — 质量流量查找表中每个断点处的压降 numerical array with units of pressure

质量流量查找表中每个断点处的压降。该模块对断点进行内插和外推，以获得任何质量流量下的压降。插值为 `linear`，外推为 `nearest`。

压降可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，它们将与之组合以完成表格化的断点。

### **Reference inflow temperature** — 表格数据中假设的绝对入口温度 `293.15 K` (default) | scalar with units of temperature

在收集表格化压降时在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考密度与实际流体密度之比乘以表格化压降以获得实际压降。

### **Reference inflow pressure** — 表格数据中假设的绝对入口压力 `0.101325 MPa` (default) | scalar with units of pressure

在收集表格化压降时在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考密度与实际流体密度之比乘以表格化压降以获得实际压降。

### **Mass flow rate threshold for flow reversal** — 质量流量数值平滑区域的上限 `1e-3 kg/s` (default) | scalar with units of mass/time

低于该质量流量时，其值经过数值平滑以避免在零流量下产生仿真误差的不连续性。有关换热器热液体侧计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (TL) 模块（`Simple Model` 变体所基于的模块）。

### **Thermal liquid volume** — 热液体流道中的流体体积 `0.01 m^3` (default) | scalar with units of length cubed

热液体流道中的流体体积。

### **Cross-sectional area at ports A1 and B1** — 流道入口和出口处的流通面积 `0.01 m^2` (default) | scalar with units of length squared

热液体流道入口和出口处的流通面积。端口尺寸相同。

### 效应和初始条件

### **Enable Thermal Liquid dynamic compressibility** — 换热器中液体压缩性的设置 `On` (default) | `Off` | scalar

对换热器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid nominal temperature** — 标称工况下的温度 `293.15 K` (default) | scalar

标称工况下的热液体温度。当动态压缩性被禁用时，该模块使用此值来计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid dynamic compressibility** 复选框。

### **Thermal Liquid nominal pressure** — 标称工况下的压力 `0.101325 MPa` (default) | scalar

标称工况下的热液体压力。当动态压缩性被禁用时，该模块使用此值来计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid dynamic compressibility** 复选框。

### **Thermal Liquid initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时热液体通道中的温度

### **Thermal Liquid initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa` (default) | scalar with units of pressure

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024a: 从 Heat Exchanger (TL) 模块对简单换热器建模选项进行建模

以前，Heat Exchanger (TL) 模块使用 **Modeling option** 参数来对两个模块变体进行建模。此参数已被移除，这两个模块变体现在是两个独立的模块。Specific Dissipation Heat Exchanger (TL) 模块使用以前在 **Modeling option** 为 `Simple model` 时使用的传热模型。要使用 **Modeling option** 为 `E-NTU Model` 时使用的模块模型，请参阅 Heat Exchanger (TL) 模块。

## 描述

由比耗散数据参数化的换热器，用于具有热液体和受控流的系统

Specific Dissipation Heat Exchanger (TL) 模块通过薄壁上的传导对流体进行冷却和加热建模。单相热液体的属性在 **Thermal Liquid** 选项卡上定义。第二种流体是受控流体，仅由 **Controlled Fluid** 选项卡上的用户定义参数指定。它不从域流体网络接收任何属性。流体之间的热交换基于热液体显热。

### 传热模型

简单模型的传热基于比耗散：

Q=ξ(TIn,Th−TIn,C)，

其中：

- *ξ* 是比耗散，它是热液体和受控液体质量流量的函数。
- *TIn,Th* 是热液体入口温度。
- *TIn,C* 是受控液体入口温度。

简单模型基于用户提供的表格数据的线性插值，不捕捉换热器的个别特征。

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

### 复合结构

Heat Exchanger (TL) 模块是 Specific Dissipation Heat Exchanger Interface (TL) 和 Specific Dissipation Heat Transfer 模块的复合：
