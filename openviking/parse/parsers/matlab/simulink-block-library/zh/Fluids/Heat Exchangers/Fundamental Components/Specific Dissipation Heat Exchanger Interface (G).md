---
type: simulink-block
title: 'Specific Dissipation Heat Exchanger Interface (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheatexchangerinterfaceg'
documentation_source_path: 'ref/specificdissipationheatexchangerinterfaceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Exchanger Interface (G)

## 端口
```yaml
ports:
- name: CP
  summary: 气体的等压比热，kJ/(kg*K) 物理信号
  direction: output
- name: M
  summary: 热液体的质量流量，kg/s 物理信号
  direction: output
- name: A
  summary: 流体开口 气体
  direction: output
- name: B
  summary: 流体开口 气体
  direction: output
- name: H
  summary: 流体入口处的热条件 热
  direction: output
```

### 输出

### **CP** — 气体的等压比热，`kJ/(kg*K)` 物理信号

热接口内部流体体积中气体的等压比热。

### **M** — 热液体的质量流量，`kg/s` 物理信号

接口内部流体体积中气体的质量流量。当流量方向从端口 **A** 流向端口 **B** 时，输出信号为正，否则为负。

### 守恒

### **A** — 流体开口 气体

气体可以进入和退出热接口的开口。

### **B** — 流体开口 气体

气体可以进入和退出热接口的开口。

### **H** — 流体入口处的热条件 热

用于设置作为气体入口的气体端口处热条件的热端口。
## 参数
```yaml
parameters:
- name: 质量流量向量
  summary: 用于指定压降数据的质量流量 [.3, .5, 1, 1.5, 2, 2.5] kg/s（默认）| 单位为质量/时间的 *K* 元素数组
  group: ''
- name: 压降向量
  summary: 对应于指定质量流量的压降数据 [3, 5, 10, 25, 35, 50] * 1e-3 MPa（默认）| 单位为压力的 *K* 元素数组
  group: ''
- name: 参考流入温度
  summary: 指定压降数据时的温度 293.15 K（默认）| 单位为温度的标量
  group: ''
- name: 参考流入压力
  summary: 指定压降表格数据时的压力 0.101325 MPa（默认）| 单位为压力的标量
  group: ''
- name: 用于流动反向的质量流量阈值
  summary: 低于此值对数值数据进行平滑的质量流量 1e-6 kg/s（默认）| 单位为质量/时间的标量
  group: ''
- name: 气体体积
  summary: 热交换器内部的气体体积 0.01 m^3（默认）| 单位为体积的标量
  group: ''
- name: 端口 A1 和 B1 处的横截面积
  summary: 气体入口处的流通面积 0.01 m^2（默认）| 单位为面积的标量
  group: ''
- name: 启用动态可压缩性
  summary: 对气体通道中的压力动态进行建模的选项 On（默认）| Off
  group: ''
- name: 标称温度
  summary: 标称工况下的温度 293.15 K（默认）| 标量
  group: ''
- name: 标称压力
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: ''
- name: Initial pressure
  summary: 仿真开始时的压力 0.101325 MPa（默认）| 标量
  group: ''
- name: Initial pressure priority
  summary: 压力参数优先级 High（默认）| Low | None
  group: ''
- name: Initial temperature
  summary: 仿真开始时的温度 293.15 K（默认）| 标量
  group: ''
- name: Initial temperature priority
  summary: 温度参数优先级 High（默认）| Low | None
  group: ''
```

#### 压力损失

### **质量流量向量** — 用于指定压降数据的质量流量 `[.3, .5, 1, 1.5, 2, 2.5] kg/s`（默认）| 单位为质量/时间的 *K* 元素数组

用于指定压降表格数据的质量流量数组。

### **压降向量** — 对应于指定质量流量的压降数据 `[3, 5, 10, 25, 35, 50] * 1e-3 MPa`（默认）| 单位为压力的 *K* 元素数组

对应于表格质量流量数据的从入口到出口的压降数组。

### **参考流入温度** — 指定压降数据时的温度 `293.15 K`（默认）| 单位为温度的标量

指定表格压降数据时的温度。

### **参考流入压力** — 指定压降表格数据时的压力 `0.101325 MPa`（默认）| 单位为压力的标量

指定表格压降数据时的压力。该模块使用此参数计算第三个参考参数，即参考密度。它使用该参考值来缩放偏离参考条件的压力和温度下的表格压降数据。

### **用于流动反向的质量流量阈值** — 低于此值对数值数据进行平滑的质量流量 `1e-6 kg/s`（默认）| 单位为质量/时间的标量

低于此质量流量时启动平滑流动反向以防止仿真数据中出现不连续。

### **气体体积** — 热交换器内部的气体体积 `0.01 m^3`（默认）| 单位为体积的标量

在任何给定时间占据热交换器的气体体积。**效果和初始条件**选项卡中指定的初始条件适用于此体积。该体积在仿真期间保持恒定。

### **端口 A1 和 B1 处的横截面积** — 气体入口处的流通面积 `0.01 m^2`（默认）| 单位为面积的标量

气体入口处的流通面积。假设入口 **A1** 和 **B1** 的尺寸相同。

#### 效果和初始条件

### **启用动态可压缩性** — 对气体通道中的压力动态进行建模的选项 `On`（默认）| `Off`

对气体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **标称温度** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的气体温度。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除**启用动态可压缩性**复选框。

### **标称压力** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的气体压力。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial pressure** — 仿真开始时的压力 `0.101325 MPa`（默认）| 标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| 标量

仿真开始时气体通道中的温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。
## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：可选地建模动态可压缩性

Specific Dissipation Heat Exchanger Interface (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地建模动态可压缩性。此前，该模块始终建模压力动态特性，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以阻止动态可压缩性建模。

### R2024a：新模块名称

该模块现在名为 Specific Dissipation Heat Exchanger Interface (G)。此前名为 Simple Heat Exchanger Interface (G)。

## 描述

气体与其周围环境之间的热接口

Specific Dissipation Heat Exchanger Interface (G) 模块对气体在流经热接口（例如由热交换器提供的热接口）长度时的压降和温度变化进行建模。跨热接口的传热被忽略。有关如何组合这两个模块的示例，请参见 Heat Exchanger (G-G) 模块的复合框图。

压降根据在某个参考压力和温度下指定的表格数据计算为质量流量的函数。如果质量流量在表格数据的边界内，则计算基于线性插值；否则基于最近邻外推。换句话说，相邻数据点通过直线段连接，而在质量流量边界处的数据点则水平向外延伸。

**线性插值（左）和最近邻外推（右）**

模块计算依赖于热接口入口处流体温度、密度和比内能的状态和属性。在流动反转期间，入口会从一个端口突然变为另一个端口，从而在这些变量的值中引入不连续性。为消除这些不连续性，模块在质量流量低于指定阈值时对受影响的变量进行平滑处理。

**质量流量阈值以下的入口温度平滑**

### 质量平衡

质量可以通过端口 **A** 和 **B** 进入和离开热接口。当您选中 **Enable dynamic compressibility** 时，质量平衡为

∂M∂pdpdt+∂M∂TdTdt=m˙A+m˙B，

其中：

- *M* 是热接口内部流体体积的质量。
- *p* 是内部流体压力。
- *T* 是内部流体温度。
- *m˙\** 是通过气体端口进入的质量流量。

当您清除 **Enable dynamic compressibility** 复选框时，质量平衡为

m˙A+m˙B=0。

### 能量平衡

能量可以通过两种方式进入和离开热接口：通过端口 **A** 和 **B** 的流体流动，以及通过端口 **H** 的热流。当您选中 **Enable dynamic compressibility** 时，能量平衡为

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH，

其中：

- *E* 是热接口内部流体体积中的总能量。
- *ϕ*\* 是通过气体端口进入的能量流量。
- *Q* 是通过热端口进入的热流量。

如果您清除 **Enable dynamic compressibility** 复选框，能量平衡为

dEdt=ϕA+ϕB+QH，

其中总内能为

E=ρ0uV。

该模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算常数 *ρ0*。

### 动量平衡

压降计算完全基于您指定的表格数据。除这些因素可能对指定数据产生影响外，压降的原因会被忽略。从一个气体端口到另一个气体端口的总压降由从每个气体端口到内部流体体积的各个压降计算得出：

pA−pB=ΔpA−ΔpB，

其中：

- *p*\* 是气体端口处的流体压力。
- *Δp*\* 是从气体端口到内部流体体积的压降：

  Δp\*=p\*−p，

  其中 *p* 是内部流体体积中的压力。

表格数据是在参考压力和温度下指定的，并根据这些数据计算第三个参考参数，即*参考密度*。参考密度与实际端口密度的比值用作各个压降方程中的修正因子，每个方程定义为：

Δp\*=Δp(m˙\*)ρRρ\*，

其中：

- *Δp(m˙)* 是表格压降函数。
- *ρ*\* 是气体端口处的流体密度。

星号表示定义参数或变量的气体端口（**A** 或 **B**）。下标 R 表示参考值。接口入口处的密度在质量流量阈值以下通过引入双曲项 *ɑ* 进行平滑处理：

ρ\*,smooth=ρ\*(1+α2)+ρ(1−α2)，

其中 *ρ*smooth 是入口端口处的平滑密度，*ρ*\* 是同一端口处的未平滑密度，*ρ* 是内部流体体积中的密度。双曲平滑项定义为：

α=tanh(4m˙avgm˙th)，

其中 *m˙avg* 是通过气体端口的质量流量的平均值，*m˙th* 是在模块对话框中指定的质量流量阈值。该阈值决定了用于平滑流体密度的质量流量区域的宽度。平均质量流量定义为：

m˙avg=m˙A+m˙B2
