---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'specificdissipationheatexchangertltl'
documentation_source_path: 'ref/specificdissipationheatexchangertltl.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (TL-TL)

## 端口
```yaml
ports:
- name: A1
  summary: 热液体 1 端口 thermal liquid
  direction: conserving
- name: B1
  summary: 热液体 1 端口 thermal liquid
  direction: conserving
- name: A2
  summary: 热液体 2 端口 thermal liquid
  direction: conserving
- name: B2
  summary: 热液体 2 端口 thermal liquid
  direction: conserving
```

### 守恒端口

### **A1** — 热液体 1 端口 thermal liquid

热液体 1 进入和离开其换热器侧的开口。

### **B1** — 热液体 1 端口 thermal liquid

热液体 1 进入和离开其换热器侧的开口。

### **A2** — 热液体 2 端口 thermal liquid

热液体 2 进入和离开其换热器侧的开口。

### **B2** — 热液体 2 端口 thermal liquid

热液体 2 进入和离开其换热器侧的开口。
## 参数
```yaml
parameters:
- name: Thermal Liquid 1 mass flow rate vector, mdot1
  summary: 比散热查找表中每个断点处热液体 1 的质量流量，数值数组，单位为质量/时间
  group: 传热
- name: Thermal Liquid 2 mass flow rate vector, mdot2
  summary: 比散热查找表中每个断点处热液体 2 的质量流量，数值数组，单位为质量/时间
  group: 传热
- name: Specific heat dissipation table, SD(mdot1,mdot2)
  summary: 查找表中热液体 1 和热液体 2 质量流量各断点处的比散热，数值数组，单位为功率/温度
  group: 传热
- name: Check if violating maximum specific dissipation
  summary: 比散热超过最小热容率时的警告条件 Warning（默认）| None | Error
  group: 传热
- name: Mass flow rate vector
  summary: 压降查找表中每个断点处的质量流量，数值数组，单位为质量/时间
  group: Thermal Liquid 1|2 选项卡
- name: Pressure drop vector
  summary: 质量流量查找表中每个断点处的压降，数值数组，单位为压力
  group: Thermal Liquid 1|2 选项卡
- name: Reference inflow temperature
  summary: 表格数据中假设的绝对入口温度 293.15 K（默认）| 标量，单位为温度
  group: Thermal Liquid 1|2 选项卡
- name: Reference inflow pressure
  summary: 表格数据中假设的绝对入口压力 0.101325 MPa（默认）| 标量，单位为压力
  group: Thermal Liquid 1|2 选项卡
- name: Threshold mass flow rate for flow reversal
  summary: 质量流量数值平滑区域的上限 1e-3 kg/s（默认）| 标量，单位为质量/时间
  group: Thermal Liquid 1|2 选项卡
- name: Thermal liquid volume
  summary: 热液体 1 或热液体 2 流道中的流体体积 0.01 m^3（默认）| 标量，单位为长度立方
  group: Thermal Liquid 1|2 选项卡
- name: Cross-sectional area at ports A and B
  summary: 流道入口和出口处的流通面积 0.01 m^2（默认）| 标量，单位为长度平方
  group: Thermal Liquid 1|2 选项卡
- name: Enable Thermal Liquid 1 dynamic compressibility
  summary: 换热器中液体可压缩性的设置 On（默认）| Off | 标量
  group: 效应和初始条件
- name: Thermal Liquid 1 nominal temperature
  summary: 标称工况下的温度 293.15 K（默认）| 标量
  group: 效应和初始条件
- name: Thermal Liquid 1 nominal pressure
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 效应和初始条件
- name: Thermal Liquid 1 initial temperature
  summary: 仿真开始时热液体 1 中的温度 293.15 K（默认）| 标量，单位为温度
  group: 效应和初始条件
- name: Thermal Liquid 1 initial pressure
  summary: 仿真开始时热液体 1 通道中的压力 0.101325 MPa（默认）| 标量，单位为压力
  group: 效应和初始条件
- name: Enable Thermal Liquid 2 dynamic compressibility
  summary: 对热液体 2 通道中压力动态进行建模的选项 On（默认）| Off
  group: 效应和初始条件
- name: Thermal Liquid 2 nominal temperature
  summary: 标称工况下的温度 293.15 K（默认）| 标量
  group: 效应和初始条件
- name: Thermal Liquid 2 nominal pressure
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 效应和初始条件
- name: Thermal Liquid 2 initial temperature
  summary: 仿真开始时热液体 1 中的温度 293.15 K（默认）| 标量，单位为温度
  group: 效应和初始条件
- name: Thermal Liquid 2 initial pressure
  summary: 仿真开始时热液体 1 通道中的压力 0.101325 MPa（默认）| 标量，单位为压力
  group: 效应和初始条件
```

### 传热

### **Thermal Liquid 1 mass flow rate vector, mdot1** — 比散热查找表中每个断点处热液体 1 的质量流量，数值数组，单位为质量/时间

比散热查找表中每个断点处热液体 1 的质量流量。该模块对断点进行内插和外推，以获得换热器在任意质量流量下的比散热。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素。

### **Thermal Liquid 2 mass flow rate vector, mdot2** — 比散热查找表中每个断点处热液体 2 的质量流量，数值数组，单位为质量/时间

比散热查找表中每个断点处热液体 2 的质量流量。该模块对断点进行内插和外推，以获得换热器在任意质量流量下的比散热。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素。

### **Specific heat dissipation table, SD(mdot1,mdot2)** — 查找表中热液体 1 和热液体 2 质量流量各断点处的比散热，数值数组，单位为功率/温度

查找表中热液体 1 和热液体 2 质量流量各断点处的比散热。该模块对断点进行内插和外推，以获得任意一对热液体 1 和热液体 2 质量流量下的效能。插值方法为 `linear`，外推方法为 `nearest`。

比散热值必须为非负。它们必须按照热液体 1 通道中质量流量递增的顺序从上到下排列，并按照热液体 2 通道中质量流量递增的顺序从左到右排列。行数必须等于 **Thermal liquid 1 mass flow rate vector** 参数的大小，列数必须等于 **Thermal liquid 2 mass flow rate vector** 参数的大小。

如果您的换热器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比散热。

### **Check if violating maximum specific dissipation** — 比散热超过最小热容率时的警告条件 `Warning`（默认）| `None` | `Error`

比散热超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是两股流体中较低者。该最小值给出了具有最大效能的换热器的比散热，且不可超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Thermal Liquid 1|2 选项卡

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量，数值数组，单位为质量/时间

压降查找表中每个断点处的质量流量。该模块对断点进行内插和外推，以获得任意质量流量下的压降。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡流和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Pressure drop vector** 参数的大小，它们将与之组合以完成表格化的断点。

### **Pressure drop vector** — 质量流量查找表中每个断点处的压降，数值数组，单位为压力

质量流量查找表中每个断点处的压降。该模块对断点进行内插和外推，以获得任意质量流量下的压降。插值方法为 `linear`，外推方法为 `nearest`。

压降可以为正值、零或负值，并且可以跨越层流、过渡流和湍流区域。但是，它们必须从左到右单调递增。其数量必须等于 **Mass flow rate vector** 参数的大小，它们将与之组合以完成表格化的断点。

### **Reference inflow temperature** — 表格数据中假设的绝对入口温度 `293.15 K`（默认）| 标量，单位为温度

在收集表格化压降数据时在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考密度与实际流体密度之比乘以表格化压降以获得实际压降。

### **Reference inflow pressure** — 表格数据中假设的绝对入口压力 `0.101325 MPa`（默认）| 标量，单位为压力

在收集表格化压降数据时在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考密度与实际流体密度之比乘以表格化压降以获得实际压降。

### **Threshold mass flow rate for flow reversal** — 质量流量数值平滑区域的上限 `1e-3 kg/s`（默认）| 标量，单位为质量/时间

低于该质量流量时，其值经过数值平滑处理，以避免在零流量下产生仿真误差的已知不连续性。有关计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (TL) 模块。

### **Thermal liquid volume** — 热液体 1 或热液体 2 流道中的流体体积 `0.01 m^3`（默认）| 标量，单位为长度立方

热液体 1 或热液体 2 流道中的流体体积。

### **Cross-sectional area at ports A and B** — 流道入口和出口处的流通面积 `0.01 m^2`（默认）| 标量，单位为长度平方

热液体 1 或热液体 2 流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### 效应和初始条件

### **Enable Thermal Liquid 1 dynamic compressibility** — 换热器中液体可压缩性的设置 `On`（默认）| `Off` | 标量

对换热器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后简化为两个端口压力的加权平均值。

### **Thermal Liquid 1 nominal temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 1 dynamic compressibility** 复选框。

### **Thermal Liquid 1 nominal pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 1 dynamic compressibility** 复选框。

### **Thermal Liquid 1 initial temperature** — 仿真开始时热液体 1 中的温度 `293.15 K`（默认）| 标量，单位为温度

仿真开始时热液体 1 通道中的温度。

### **Thermal Liquid 1 initial pressure** — 仿真开始时热液体 1 通道中的压力 `0.101325 MPa`（默认）| 标量，单位为压力

仿真开始时热液体 1 通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid 1 dynamic compressibility**。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体 2 通道中压力动态进行建模的选项 `On`（默认）| `Off`

对热液体 2 通道中压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体 1 中的温度 `293.15 K`（默认）| 标量，单位为温度

仿真开始时热液体 2 通道中的温度。

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体 1 通道中的压力 `0.101325 MPa`（默认）| 标量，单位为压力

仿真开始时热液体 2 通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid 2 dynamic compressibility**。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024a：从 Heat Exchanger (TL-TL) 模块中建模简单换热器建模选项

此前，Heat Exchanger (TL-TL) 模块使用 **Modeling option** 参数来建模两个模块变体。此参数已被移除，两个模块变体现在是两个独立的模块。Specific Dissipation Heat Exchanger (TL-TL) 模块使用此前当 **Modeling option** 为 `Simple model` 时所使用的传热模型。要使用当 **Modeling option** 为 `E-NTU Model` 时所使用的模块模型，请参阅 Heat Exchanger (TL-TL) 模块。

## 描述

基于比散热数据参数化的换热器，适用于具有两股热液体流的系统

Specific Dissipation Heat Exchanger (TL-TL) 模块对短暂保持在薄导热壁两侧热接触的流体的互补冷却和加热进行建模。该模块使用基于比散热概念的简化模型，比散热是传热速率的一种度量。

### 传热模型

该模块的传热模型取决于由比散热定义的传热速率。比散热是当热液体 1 和热液体 2 入口温度相差一度时观察到的传热速率的度量。其与入口温差的乘积给出预期的传热速率

Q=ξ(TIn,1−TIn,2)，

其中 *ξ* 为比散热，*TIn* 为热液体 1（下标 `1`）或热液体 2（下标 `2`）的入口温度。比散热是经由热液体 1 和热液体 2 入口进入换热器的质量流量的表格化函数：

ξ=f(m˙1,m˙2)

为适应反向流动，表格数据可以覆盖正质量流量和负质量流量，在这种情况下，入口也可以被视为出口。

比散热是换热器传热速率除以入口温度差

ξ=QTIn,1−TIn,2。

比散热还等于基于入口温度定义的总传热系数乘以传热表面积，或者热容率乘以效能因子，取两者中具有较小值的流体。

传热模型几乎完全依赖于表格数据，并且由于该数据通常来自实验，因此对换热器的细节要求很少。流动布置、混合条件以及壳程或管程数（如果与被建模的换热器相关）假定完全体现在表格数据中。

该模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

有关传热计算的更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块是一个复合组件。一个 Specific Dissipation Heat Exchanger Interface (TL) 模块对换热器侧 1 的热液体流动进行建模。另一个模块对侧 2 的热液体流动进行建模。一个 Specific Dissipation Heat Transfer 模块捕获两股流体之间穿过壁面的热交换。
