---
type: simulink-block
title: 'Partially Filled Pipe (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'partiallyfilledpipetl'
documentation_source_path: 'ref/partiallyfilledpipetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Partially Filled Pipe (TL)

## 端口

### 守恒

### **A** — 液体端口 thermal liquid

Thermal liquid 守恒端口。端口 **A** 始终高于端口 **B**。当端口 **A** 浸没时，m˙A=m˙B..。当端口 **A** 暴露时，m˙A=0。

### **B** — 液体端口 thermal liquid

Thermal liquid 守恒端口。端口 **A** 始终高于端口 **B**。当端口 **A** 浸没时，m˙A=m˙B。当端口 **A** 暴露时，流入或流出端口 **B** 的任何流动都会改变管道中的液位。干燥或部分干燥的管道只能通过端口 **B** 填充。

### 输入

### **AL** — 所连接模块的相对液位，m physical signal

所连接模块的相对液位，单位为 m，以 physical signal 形式指定。如果 **AL** 处的信号为正，则管道端部浸没。否则该端口暴露。

### 输出

### **L** — 管道液位，m physical signal

管道中的液位，单位为 m，以 physical signal 形式返回。

## 参数

### 几何

### **Pipe length** — 管道长度 `5 m` (默认) | positive scalar

管道长度。

### **Cross-sectional area** — 管道横截面积 `0.01 m^2` (默认) | positive scalar

管道的横截面积。

### **Hydraulic diameter** — 水力直径 `0.1128 m` (默认) | positive scalar

用于计算管道 Reynolds 数的水力直径。对于非圆形管道，水力直径是管道中流体的有效直径。对于圆形管道，水力直径与管道直径相同。

### **Elevation drop from port A to port B** — 从端口 A 到端口 B 的高程下降 `5 m` (默认) | positive scalar

管道的垂直高程变化。端口 **A** 始终高于端口 **B**。

### **Initial liquid level** — 起始液位 `5 m` (默认) | positive scalar

仿真开始时管道中的液位。

### **Liquid level below zero** — 当管道中没有液体时是否发出通知 `Error` (默认) | `None` | `Warning`

当管道中没有液体时是否发出通知。如果希望在仿真期间发生此情况时收到警告，请将此参数设置为 `Warning`。如果希望发生此情况时仿真停止，请将此参数设置为 `Error`。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2` (默认) | positive scalar

重力加速度常数。

### 摩擦

### **Aggregate equivalent length of local resistances** — 管道几何形状对液压损失的贡献 `1 m` (默认) | positive scalar

会产生与具有弯头、面积变化或其他非均匀属性的管道等效的液压损失的管道长度。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m` (默认) | positive scalar

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子会造成管道中的压力损失。

### **Laminar flow upper Reynolds number limit** — 层流上限阈值 `2000` (默认) | positive scalar

层流的 Reynolds 数上限。超过此数值，流体状态为过渡态，并接近湍流状态，且在 **Turbulent flow lower Reynolds number limit** 处变为完全湍流。

### **Turbulent flow lower Reynolds number limit** — 湍流下限阈值 `4000` (默认) | positive scalar

湍流的 Reynolds 数下限。低于此数值，流动状态为过渡态，并接近层流，且在 **Laminar flow upper Reynolds number limit** 处变为完全层流。

### **Laminar friction constant for Darcy friction factor** — 层流的管道摩擦常数 `64` (默认) | positive scalar

层流的管道摩擦常数。层流 Darcy 摩擦因子表示壁面摩擦在压力损失计算中的贡献。

### 初始条件

### **Initial liquid temperature** — 仿真开始时的液体温度 `293.15` `K` (默认)

仿真开始时的液体温度。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

thermal liquid 系统中具有可变液体体积的管道

Partially Filled Pipe (TL) 模块表示一种内部液位可变化的管道。该管道在仿真期间也可能完全变干。

除端口 **A** 和 **B** 处的液体连接外，端口 **AL** 还以 physical signal 形式接收来自所连接模块的入口液位。如果 **AL** 处的值大于零，则 **A** 浸没。如果 **AL** 处的值小于或等于零，则该端口暴露。管道液位以 physical signal 形式传输到端口 **L** 处的连接模块。

端口 **A** 始终高于端口 **B**。如果端口 **A** 暴露，则可通过端口 **B** 填充管道。当流体通过端口 **B** 进入管道时，通过端口 **A** 的质量流量为 0，直到管道完全充满；此时 m˙A=−m˙B。

### 何时使用 Partially Filled Pipe (TL) 模块

当预计液位会降至储罐入口以下时，此模块可与 Tank (TL) 模块一起使用。多个 Partially Filled Pipe (TL) 模块也可以串联或并联连接。但是，由于该模块只能在端口 **B** 处填充，因此在并联配置中，如果其中一个模块的端口 **A** 暴露，并且其在端口 **B** 处的连接无法重新填充该管道，则可能无法重新填充此管道。

### 管道上的压力损失

管道上的压差 *p*A – *p*B 由壁面摩擦造成的损失以及液面高度与端口 **A** 处液体高度之间的静水压差组成：

pA−pB=Δploss+Δpelev.

摩擦损失取决于管道中的流体状态。如果流动为层流，则摩擦损失为：

Δploss=−m˙BυfsL^2Dh2A2,

其中：

- *ν* 是流体运动黏度。
- *f*S 是 **Laminar friction constant for Darcy friction factor**。
- L^ 是管道长度与其 **Aggregate equivalent length of local resistances** 之和，并与管道填充液位成比例：L^=(L+Ladd)llmax。
- *l*、*lmax* 分别是液位和 **Elevation drop from port A to port B**。
- *D*h 是管道水力直径。如果管道横截面不是圆形，则水力直径是等效圆直径。

如果流动为湍流，则摩擦损失为：

Δploss=−m˙B|m˙B|fL^2ρDh2A2.

*f* 是湍流的 Darcy 摩擦因子，由经验 Haaland 关联式确定：

f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

其中 *ε* 是 **Internal surface absolute roughness** 参数。Reynolds 数基于端口 **B** 处的质量流量和管道水力直径。

静水压差为 Δpelev=ρgl。

### 质量流量

管道中的流动由内部液位和端口 **B** 处的条件决定。如果管道部分为空，则可在 **B** 处填充或排空管道。如果管道完全充满，则 m˙A=m˙B.，且质量守恒：

m˙A+m˙B=0.

该模块通过管道的相对填充液位确定管道中的流体质量：

M=ρALllmax.

### 能量平衡

该模块平衡能量流，使得当端口 **A** 浸没时，

McvdTdt=ϕA+ϕB−m˙Bgl.

当端口 **A** 暴露时，

McvdTdt=ϕA+ϕB−m˙Bh−m˙Bgl,

其中 *cv* 是定容比热，*T* 是流体温度，*h* 是比焓。

### 假设与限制

此模块不考虑动态可压缩性或流体惯性，也不对管道中的空气（或第二种液体）动力学建模。
