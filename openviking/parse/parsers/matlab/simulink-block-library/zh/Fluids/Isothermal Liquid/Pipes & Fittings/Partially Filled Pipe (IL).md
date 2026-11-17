---
type: simulink-block
title: 'Partially Filled Pipe (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'partiallyfilledpipeil'
documentation_source_path: 'ref/partiallyfilledpipeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Partially Filled Pipe (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

管道中流体的入口或出口。端口 **A** 始终高于端口 **B**。当端口 **A** 浸没时，m˙A=m˙B。当端口 **A** 暴露时，m˙A=0。

### **B** — 液体端口，等温液体

管道中流体的入口或出口。端口 **A** 始终高于端口 **B**。当端口 **A** 浸没时，m˙A=m˙B。当端口 **A** 暴露时，任何流入或流出端口 **B** 的流量都会改变管道中的液位。干燥或部分干燥的管道只能通过端口 **B** 填充。

### 输入

### **AL** — 所连接模块的相对液位，m，物理信号

所连接模块的相对液位，单位为 m，指定为物理信号。如果 **AL** 处的信号为正，则管道末端浸没。否则该端口暴露。

### 输出

### **L** — 管道液位，m，物理信号

管道中的液位，单位为 m，以物理信号形式返回。

## 参数

### 几何

### **Pipe length** — 管道长度 `5 m`（默认）| 正标量

管道长度。

### **Cross-sectional area** — 管道横截面积 `0.01 m^2`（默认）| 正标量

管道的横截面积。

### **Hydraulic diameter** — 水力直径 `0.1128 m`（默认）| 正标量

用于计算管道雷诺数的水力直径。对于非圆形管道，水力直径为管道中流体的有效直径。对于圆形管道，水力直径与管道直径相同。

### **Elevation drop from port A to port B** — A 与 B 之间的垂直距离 `5 m`（默认）| 正标量

管道的垂直高程变化。端口 **A** 始终高于端口 **B**。

### **Initial liquid level** — 初始液位 `5 m`（默认）| 正标量

仿真开始时管道中的液位。

### **Liquid level below zero** — 管道中无液体时是否通知 `Error`（默认）| `None` | `Warning`

管道中无液体时是否通知。如果您希望在仿真期间发生此情况时收到警告，请将此参数设置为 `Warning`。如果您希望在发生此情况时停止仿真，请将此参数设置为 `Error`。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2`（默认）| 正标量

重力加速度常数。

### 摩擦

### **Aggregate equivalent length of local resistances** — 管道几何形状对水力损失的贡献 `1 m`（默认）| 正标量

产生与具有弯头、面积变化或其他非均匀属性的管道相同水力损失的等效管道长度。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m`（默认）| 正标量

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子影响管道中的压力损失。

### **Laminar flow upper Reynolds number limit** — 层流上限阈值 `2000`（默认）| 正标量

层流的上限雷诺数。超过此数值后，流体流态为过渡态并趋近于湍流态，并在 **Turbulent flow lower Reynolds number limit** 处变为完全湍流。

### **Turbulent flow lower Reynolds number limit** — 湍流下限阈值 `4000`（默认）| 正标量

湍流的下限雷诺数。低于此数值时，流态为过渡态并趋近于层流，并在 **Laminar flow upper Reynolds number limit** 处变为完全层流。

### **Laminar friction constant for Darcy friction factor** — 层流的管道摩擦常数 `64`（默认）| 正标量

层流的管道摩擦常数。层流 Darcy 摩擦因子用于在压力损失计算中体现壁面摩擦的贡献。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中具有可变液体体积的管道

Partially Filled Pipe (IL) 模块对具有可变内部液位能力的管道进行建模。该管道在仿真过程中也可能完全排空。

除了端口 **A** 和 **B** 处的液体连接外，端口 **AL** 从连接的模块接收入口液位作为物理信号。如果 **AL** 处的值大于零，则 **A** 被淹没。如果 **AL** 处的值小于或等于零，则该端口暴露。管道液位作为物理信号传输到端口 **L** 处的连接模块。

端口 **A** 始终高于端口 **B**。如果端口 **A** 暴露，则可以通过端口 **B** 填充管道。当流体通过端口 **B** 进入管道时，通过端口 **A** 的质量流量为 0，直到管道完全充满，此时 m˙A=−m˙B。

### 何时使用 Partially Filled Pipe (IL) 模块

当预计液位会降至储罐入口以下时，此模块可与 Tank (IL) 模块配合使用。多个 Partially Filled Pipe (IL) 模块也可以串联或并联连接。然而，由于部分填充的管道只能在端口 **B** 处填充，如果并联配置中某个模块的端口 **A** 暴露，并且其在端口 **B** 处的连接无法重新填充该管道，则可能无法重新填充此管道。

### 管道上的压力损失

管道上的压差，
*p*A –
*p*B，包括由于壁面摩擦和液面高度与端口 **A** 处液体高度之间的静水压差引起的损失：

pA−pB=Δploss+Δpelev。

摩擦损失取决于管道中的流体流态。如果流动为层流，则摩擦损失为：

Δploss=−m˙BυfsL^2Dh2A2，

其中：

- *ν* 是流体运动黏度。
- *f*S 是 **Laminar friction constant for Darcy friction factor**。
- L^ 是管道长度与其 **Aggregate equivalent length of local resistances** 之和，与管道填充液位成比例：L^=(L+Ladd)llmax。
- *l*、*lmax* 分别是液位和 **Elevation drop from port A to port B**。
- *D*h 是管道水力直径。如果管道横截面不是圆形，则水力直径为等效圆直径。

如果流动为湍流，则摩擦损失为：

Δploss=−m˙B|m˙B|fL^2ρDh2A2。

*f* 是湍流的 Darcy 摩擦因子，由经验 Haaland 关联式确定：

f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2，

其中 *ε* 是 **Internal surface absolute roughness**。Reynolds 数基于端口 **B** 处的质量流量和管道水力直径。

静水压差为 Δpelev=ρgl。

### 质量流量

管道中的流动由内部液位和端口 **B** 处的条件决定。如果管道部分为空，则可以在 **B** 处填充或排空管道。如果管道完全充满，则 m˙A=m˙B，并且质量守恒：

m˙A+m˙B=0。

管道中的流体质量由管道的相对填充液位确定：

M=ρALllmax。

### 假设和限制

此模块不考虑动态可压缩性或流体惯性，也不对管道中空气（或第二种液体）的动力学进行建模。
