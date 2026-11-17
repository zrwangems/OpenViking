---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'specificdissipationheatexchangergtl'
documentation_source_path: 'ref/specificdissipationheatexchangergtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger (G-TL)

## 端口
```yaml
ports:
- name: A1
  summary: 气体端口 gas
  direction: conserving
- name: B1
  summary: 气体端口 gas
  direction: conserving
- name: A2
  summary: 热液体端口 thermal liquid
  direction: conserving
- name: B2
  summary: 热液体端口 thermal liquid
  direction: conserving
```

### 守恒端口

### **A1** — 气体端口 gas

气体进入和退出换热器气体侧的开口。

### **B1** — 气体端口 gas

气体进入和退出换热器气体侧的开口。

### **A2** — 热液体端口 thermal liquid

热液体进入和退出换热器热液体侧的开口。

### **B2** — 热液体端口 thermal liquid

热液体进入和退出换热器热液体侧的开口。
## 参数
```yaml
parameters:
- name: Gas 1 mass flow rate vector, mdot1
  summary: 比散热查找表中每个断点处的气体质量流量，数值数组，单位为质量除以时间
  group: 传热
- name: Thermal Liquid 2 mass flow rate vector, mdot2
  summary: 比散热查找表中每个断点处的热液体质量流量，数值数组，单位为质量除以时间
  group: 传热
- name: Specific heat dissipation table, SD(mdot1, mdot2)
  summary: 查找表中每个断点处基于气体和热液体质量流量的比散热，数值数组，单位为功率除以温度
  group: 传热
- name: Check if violating maximum specific dissipation
  summary: 比散热超过最小热容率时的警告条件 Warning (default) | None | Error
  group: 传热
- name: Mass flow rate vector
  summary: 压降查找表中每个断点处的质量流量，数值数组，单位为质量每单位时间
  group: Gas 1
- name: Pressure drop vector
  summary: 查找表中每个断点处基于质量流量的压降，数值数组，单位为压力
  group: Gas 1
- name: Reference inflow temperature
  summary: 表格数据中假设的绝对入口温度 293.15 K (default) | 标量，单位为温度
  group: Gas 1
- name: Reference inflow pressure
  summary: 表格数据中假设的绝对入口压力 0.101325 MPa (default) | 标量，单位为压力
  group: Gas 1
- name: Mass flow rate threshold for flow reversal
  summary: 质量流量数值平滑区域的上界 1e-3 kg/s (default) | 标量，单位为质量/时间
  group: Gas 1
- name: Gas 1 volume
  summary: 气体流道中的流体体积 0.01 m^3 (default) | 标量，单位为长度的立方
  group: Gas 1
- name: Cross-sectional area at ports A1 and B1
  summary: 流道入口和出口处的流通面积 0.01 m^2 (default) | 标量，单位为长度的平方
  group: Gas 1
- name: Mass flow rate vector
  summary: 压降查找表中每个断点处的质量流量，数值数组，单位为质量每单位时间
  group: Thermal Liquid 2
- name: Pressure drop vector
  summary: 查找表中每个断点处基于质量流量的压降，数值数组，单位为压力
  group: Thermal Liquid 2
- name: Reference inflow temperature
  summary: 表格数据中假设的绝对入口温度 293.15 K (default) | 标量，单位为温度
  group: Thermal Liquid 2
- name: Reference inflow pressure
  summary: 表格数据中假设的绝对入口压力 0.101325 MPa (default) | 标量，单位为压力
  group: Thermal Liquid 2
- name: Mass flow rate threshold for flow reversal
  summary: 质量流量数值平滑区域的上界 1e-3 kg/s (default) | 标量，单位为质量/时间
  group: Thermal Liquid 2
- name: Thermal Liquid 2 volume
  summary: 热液体流道中的流体体积 0.01 m^3 (default) | 标量，单位为长度的立方
  group: Thermal Liquid 2
- name: Cross-sectional area at ports A2 and B2
  summary: 流道入口和出口处的流通面积 0.01 m^2 (default) | 标量，单位为长度的平方
  group: Thermal Liquid 2
- name: Enable Gas 1 dynamic compressibility
  summary: 对气体通道中的压力动态进行建模的选项 On (default) | Off
  group: 效应和初始条件
- name: Gas 1 nominal temperature
  summary: 额定工况下的温度 293.15 K (default) | 标量
  group: 效应和初始条件
- name: Gas 1 nominal pressure
  summary: 额定工况下的压力 0.101325 MPa (default) | 标量
  group: 效应和初始条件
- name: Gas 1 initial temperature
  summary: 仿真开始时气体通道中的温度 293.15 K (default) | 标量，单位为温度
  group: 效应和初始条件
- name: Gas 1 initial pressure
  summary: 仿真开始时气体通道中的压力 0.101325 MPa (default) | 标量，单位为压力
  group: 效应和初始条件
- name: Enable Thermal Liquid 2 dynamic compressibility
  summary: 对热液体通道中的压力动态进行建模的选项 On (default) | Off
  group: 效应和初始条件
- name: Thermal Liquid 2 initial temperature
  summary: 仿真开始时热液体通道中的温度 293.15 K (default) | 标量，单位为温度
  group: 效应和初始条件
- name: Enable Thermal Liquid 2 dynamic compressibility
  summary: 对热液体通道中的压力动态进行建模的选项 On (default) | Off
  group: 效应和初始条件
- name: Thermal Liquid 2 nominal temperature
  summary: 额定工况下的温度 293.15 K (default) | 标量
  group: 效应和初始条件
- name: Thermal Liquid 2 nominal pressure
  summary: 额定工况下的压力 0.101325 MPa (default) | 标量
  group: 效应和初始条件
- name: Thermal Liquid 2 initial temperature
  summary: 仿真开始时热液体通道中的温度 293.15 K (default) | 标量，单位为温度
  group: 效应和初始条件
- name: Thermal Liquid 2 initial pressure
  summary: 仿真开始时热液体通道中的压力 0.101325 MPa (default) | 标量，单位为压力
  group: 效应和初始条件
```

### 传热

### **Gas 1 mass flow rate vector, mdot1** — 比散热查找表中每个断点处的气体质量流量，数值数组，单位为质量除以时间

比散热查找表中每个断点处的气体质量流量。该模块对断点进行内插和外推，以获得任意质量流量下的比散热。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation** 表参数的行数。如果表有 *m* 行和 *n* 列，则质量流量向量必须为 *m* 个元素。

### **Thermal Liquid 2 mass flow rate vector, mdot2** — 比散热查找表中每个断点处的热液体质量流量，数值数组，单位为质量除以时间

比散热查找表中每个断点处的热液体质量流量。该模块对断点进行内插和外推，以获得任意质量流量下换热器的比散热。插值方法为 `linear`，外推方法为 `nearest`。

质量流量可以为正值、零或负值，但必须从左到右单调递增。其数量必须等于 **Specific heat dissipation table** 参数的列数。如果表有 *m* 行和 *n* 列，则质量流量向量必须为 *n* 个元素。

### **Specific heat dissipation table, SD(mdot1, mdot2)** — 查找表中每个断点处基于气体和热液体质量流量的比散热，数值数组，单位为功率除以温度

查找表中每个断点处基于气体和热液体质量流量的比散热。该模块对断点进行内插和外推，以获得任意气体和热液体质量流量组合下的效能。插值方法为 `linear`，外推方法为 `nearest`。

比散热值必须为非负值。它们必须按照气体通道中质量流量递增的顺序从上到下排列，并按照热液体通道中质量流量递增的顺序从左到右排列。行数必须等于 **Gas 1 mass flow rate vector** 参数的大小，列数必须等于 **Thermal liquid 2 mass flow rate vector** 参数的大小。

如果您的换热器数据表提供了传热系数，请将提供的传热系数乘以表面积以计算比散热。

### **Check if violating maximum specific dissipation** — 比散热超过最小热容率时的警告条件 `Warning` (default) | `None` | `Error`

比散热超过最小热容率时的警告条件。热容率是质量流量与比热的乘积，其最小值是两种流体中较低的值。该最小值给出了具有最大效能的换热器的比散热，且不能被超过。有关更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### Gas 1

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量，数值数组，单位为质量每单位时间

压降查找表中每个断点处的质量流量。该模块使用线性插值和最近邻外推来获得任意质量流量下的压降。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。该向量的元素数量必须与 **Pressure drop vector** 参数相同，且这些元素必须从左到右单调递增。

### **Pressure drop vector** — 查找表中每个断点处基于质量流量的压降，数值数组，单位为压力

查找表中每个断点处基于质量流量的压降。该模块使用线性插值和最近邻外推来获得任意质量流量下的压降。

压降可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。该向量的元素数量必须与 **Mass flow rate vector** 参数相同，且这些元素必须从左到右单调递增。

### **Reference inflow temperature** — 表格数据中假设的绝对入口温度 `293.15 K` (default) | 标量，单位为温度

在收集表格压降数据时在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降以获得实际压降。

### **Reference inflow pressure** — 表格数据中假设的绝对入口压力 `0.101325 MPa` (default) | 标量，单位为压力

在收集表格压降数据时在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降以获得实际压降。

### **Mass flow rate threshold for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s` (default) | 标量，单位为质量/时间

低于该质量流量时，其值经过数值平滑以避免不连续。有关计算的详细信息，请参阅 Simple Heat Exchanger Interface 模块。

### **Gas 1 volume** — 气体流道中的流体体积 `0.01 m^3` (default) | 标量，单位为长度的立方

气体流道中的流体体积。

### **Cross-sectional area at ports A1 and B1** — 流道入口和出口处的流通面积 `0.01 m^2` (default) | 标量，单位为长度的平方

气体流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### Thermal Liquid 2

### **Mass flow rate vector** — 压降查找表中每个断点处的质量流量，数值数组，单位为质量每单位时间

压降查找表中每个断点处的质量流量。该模块使用线性插值和最近邻外推来获得任意质量流量下的压降。

质量流量可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。该向量的元素数量必须与 **Pressure drop vector** 参数相同，且这些元素必须从左到右单调递增。

### **Pressure drop vector** — 查找表中每个断点处基于质量流量的压降，数值数组，单位为压力

查找表中每个断点处基于质量流量的压降。该模块使用线性插值和最近邻外推来获得任意质量流量下的压降。

压降可以为正值、零或负值，并且可以跨越层流、过渡和湍流区域。该向量的元素数量必须与 **Mass flow rate vector** 参数相同，且这些元素必须从左到右单调递增。

### **Reference inflow temperature** — 表格数据中假设的绝对入口温度 `293.15 K` (default) | 标量，单位为温度

在收集表格压降数据时在入口处建立的绝对温度。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降以获得实际压降。

### **Reference inflow pressure** — 表格数据中假设的绝对入口压力 `0.101325 MPa` (default) | 标量，单位为压力

在收集表格压降数据时在入口处建立的绝对压力。参考入口温度和压力决定了表格数据中假设的流体密度。在仿真期间，参考流体密度与实际流体密度之比乘以表格压降以获得实际压降。

### **Mass flow rate threshold for flow reversal** — 质量流量数值平滑区域的上界 `1e-3 kg/s` (default) | 标量，单位为质量/时间

低于该质量流量时，其值经过数值平滑以避免不连续。有关计算的详细信息，请参阅 Simple Heat Exchanger Interface 模块。

### **Thermal Liquid 2 volume** — 热液体流道中的流体体积 `0.01 m^3` (default) | 标量，单位为长度的立方

热液体流道中的流体体积。

### **Cross-sectional area at ports A2 and B2** — 流道入口和出口处的流通面积 `0.01 m^2` (default) | 标量，单位为长度的平方

热液体流道入口和出口处的流通面积。同一流道中的端口尺寸相同。

### 效应和初始条件

### **Enable Gas 1 dynamic compressibility** — 对气体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 额定工况下的温度 `293.15 K` (default) | 标量

额定工况下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 额定工况下的压力 `0.101325 MPa` (default) | 标量

额定工况下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | 标量，单位为温度

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | 标量，单位为压力

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas 1 dynamic compressibility**。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对热液体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | 标量，单位为温度

仿真开始时热液体通道中的温度。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体通道中的压力动态进行建模的选项 `On` (default) | `Off`

对热液体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 额定工况下的温度 `293.15 K` (default) | 标量

额定工况下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 额定工况下的压力 `0.101325 MPa` (default) | 标量

额定工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | 标量，单位为温度

仿真开始时热液体通道中的温度

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa` (default) | 标量，单位为压力

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid 2 dynamic compressibility**。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：可选地对动态可压缩性进行建模

Specific Dissipation Heat Exchanger (G-TL) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性进行建模。此前，该模块始终对压力动态进行建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：从 Heat Exchanger (G-TL) 模块中建模简单换热器建模选项

此前，Heat Exchanger (G-TL) 模块使用 **Modeling option** 参数来建模两种模块变体。该参数已被移除，两种模块变体现在是两个独立的模块。Specific Dissipation Heat Exchanger (G-TL) 模块使用此前当 **Modeling option** 为 `Simple model` 时所使用的传热模型。要使用当 **Modeling option** 为 `E-NTU Model` 时所使用的模块模型，请参阅 Heat Exchanger (G-TL) 模块。

## 描述

基于比耗散数据参数化的热交换器，适用于具有气体和热液体流动的系统

Specific Dissipation Heat Exchanger (G-TL) 模块对短暂处于热接触状态、通过薄导热壁隔开的流体进行互补冷却和加热建模。流体为单相，一侧为纯气体，另一侧为纯液体。两种流体均不能发生相变，因此由于潜热永远不会释放，交换严格意义上仅为显热交换。

显热交换器在机械中随处可见。在某些喷气式飞机中，防止冰在燃油管路中析出并堵塞燃油滤网的燃油加热器，其工作原理是将来自压缩机的仍然炽热的引气吹过燃油管路。在某些摩托车中，防止润滑油过热工作的机油冷却器同样通过将环境温度的冲压空气快速吹过油路来工作。引气和冲压空气为气体流，燃油和机油为热液体流。

### 传热模型

模块传热模型取决于比耗散，比耗散是当气体和热液体入口温度相差一度时观察到的传热速率的度量。其与入口温差的乘积给出预期的传热速率

Q=ξ(TIn,G−TIn,TL)，

其中 *ξ* 为比耗散，*TIn* 为气体（下标 `G`）或热液体（下标 `TL`）的入口温度。比耗散是通过气体和热液体入口进入交换器的质量流量的表格函数：

ξ=f(m˙In,G,m˙In,TL)，

为适应反向流动，表格数据可以覆盖正流量和负流量，在这种情况下，入口也可以被视为出口。

比耗散是热交换器传热速率除以入口温度差

ξ=QTIn,1−TIn,2。

比耗散也等于基于入口温度定义的总传热系数乘以传热表面积，或热容率乘以效能因子，取两者中值较小的流体。

传热模型几乎完全依赖于表格数据，且该数据通常来自实验，因此对交换器的细节要求很少。流动布置、混合条件以及壳程或管程数（如果与被建模的热交换器相关）假定完全体现在表格数据中。

模块在传热计算中使用的流体属性为入口值与流体体积内值的平均值。

有关传热计算的更多详细信息，请参阅 Specific Dissipation Heat Transfer 模块。

### 复合结构

该模块为复合组件。Specific Dissipation Heat Exchanger Interface (G) 模块对气体流动建模，Specific Dissipation Heat Exchanger Interface (TL) 模块对热液体流动建模。流动通道中的质量、动量和能量守恒来自相应的接口模块。Specific Dissipation Heat Transfer 模块捕获两种流动之间通过壁面交换的热量。
