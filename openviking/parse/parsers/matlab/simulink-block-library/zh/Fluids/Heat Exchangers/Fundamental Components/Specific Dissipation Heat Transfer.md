---
type: simulink-block
title: 'Specific Dissipation Heat Transfer'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'specificdissipationheattransfer'
documentation_source_path: 'ref/specificdissipationheattransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# Specific Dissipation Heat Transfer

## 端口

### 输入

### **CP1** — 受控流体 1 的等压比热物理信号

受控流体 1 的等压比热。

### **CP2** — 受控流体 2 的等压比热物理信号

受控流体 2 的等压比热。

### **M1** — 受控流体 1 的入口质量流量物理信号

受控流体 1 的入口质量流量。正质量流量值对应于正常运行工况下的比耗散值。反向流动期间获得的比耗散值对应于负质量流量值。

### **M2** — 受控流体 2 的入口质量流量物理信号

受控流体 2 的入口质量流量。正质量流量值对应于正常运行工况下的比耗散值。反向流动期间获得的比耗散值对应于负质量流量值。
### 守恒

### **H1** — 受控流体 1 的入口温度热

受控流体 1 的入口温度。

### **H2** — 受控流体 2 的入口温度热

受控流体 2 的入口温度。

## 参数

### **Thermal Liquid mass flow rate vector, mdot1** — 用于指定比耗散数据的入口质量流量 `[.3, .5, .6, .7, 1, 1.4, 1.9, 2.3] kg/s`（默认）| 单位为质量/时间的 *M* 元素数组

受控流体 1 入口处的质量流量数组。每个值对应于比耗散查找表中的一行。正质量流量值对应于正常运行工况下的比耗散值。反向流动期间获得的比耗散值对应于负质量流量值。

### **Controlled fluid mass flow rate vector, mdot2** — 用于指定比耗散数据的入口质量流量 `[.3, .5, 1, 1.3, 1.7, 2, 2.6, 3.3] kg/s`（默认）| 单位为质量/时间的 *N* 元素数组

受控流体 2 入口处的质量流量数组。每个值对应于比耗散查找表中的一行。正质量流量值对应于正常运行工况下的比耗散值。反向流动期间获得的比耗散值对应于负质量流量值。

### **Specific dissipation table, SD(mdot1, mdot2)** — 与指定质量流量对应的比耗散值 单位为 `kW/K` 的 8×8 矩阵（默认）| 单位为功率/温度的 *M*×*N* 矩阵

与受控流体 1 和 2 的指定质量流量数组对应的比耗散值矩阵。该模块使用表格数据计算模拟工况下的传热。

如果您的换热器数据表基于入口温度提供传热系数，请将提供的传热系数乘以表面积以计算比耗散。

### **Mass flow rate threshold for flow reversal** — 用于平滑数值数据的质量流量下限 `1e-3 kg/s`（默认）| 单位为质量/时间的标量

低于该质量流量时启动平滑流动反转以防止仿真数据中出现不连续。

### **Check if violating maximum specific dissipation** — 用于在比耗散超过最大允许值时发出警告的选项 `Warning`（默认）| `None` | `Error`

用于在比耗散超过模块描述中所述最大值时发出警告的选项。

## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

两种通用流体之间的简单传热模型

Specific Dissipation Heat Transfer 模块在仅需极少组件参数知识的情况下对两种流体之间的传热进行建模。流体由物理信号控制，这些信号为每种流体提供入口质量流量和等压比热。热端口设置流体的入口温度。

传热速率根据比耗散计算，该参数以表格形式指定为入口质量流量的函数。比耗散量化了当入口温度相差一度时流体之间每单位时间交换的热量。

该模块不对压力损失和流动力学的其他方面进行建模。这些效应由换热器接口模块捕获。将此模块与 Specific Dissipation Heat Exchanger Interface (G) 或 Specific Dissipation Heat Exchanger Interface (TL) 模块结合使用以对换热器进行建模。

### 传热速率

热量从较热流体流向较冷流体，其速率与流体入口温度之差成正比。如果流体 1 的入口温度高于流体 2，并且因此热量从流体 1 流向流体 2，则热流率为正：

Q=ξ(TIn,1−TIn,2),

其中 *T*\*,in 是流体入口温度，由流体 1 的热端口 **H1** 和流体 2 的 **H2** 处的条件确定。*ξ* 是在给定质量流量下从指定表格数据获得的比耗散：

ξ=f(m˙1,m˙2)

其中 m˙ 是入口质量流量，通过流体 1 的物理信号端口 **M1** 和流体 2 的 **M2** 指定。

比耗散是换热器传热速率除以入口温度之差

ξ=QTIn,1−TIn,2。

比耗散还等于基于入口温度定义的总体传热系数乘以传热表面积，或热容率乘以效能因子，取两者中较小值的流体。

**最大传热速率**

传热速率受到约束，使得计算中使用的比耗散永远不会超过最大值：

ξmax=min(C1,C2),

其中 *C*\* 是受控流体的热容率，各自定义为：

C\*=m˙\*cp,\*,

其中 *c*p,\* 表示流体的等压比热，通过流体 1 的物理信号端口 **CP1** 和流体 2 的 **CP2** 指定。最大传热速率的约束以分段函数的形式实现：

Q={ξmax(T1,in−T2,in),if SD>SDmaxξ(T1,in−T2,in),otherwise,

如果 **Check if violating maximum specific dissipation** 参数为 `Warning`，则每当热流率超过最大值时，该模块会发出警告。
