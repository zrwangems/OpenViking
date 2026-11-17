---
type: simulink-block
title: 'Translational Mechanical Converter (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'translationalmechanicalconverterg'
documentation_source_path: 'ref/translationalmechanicalconverterg.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Mechanical Converter (G)

## 端口

### 输入

### **p** — 端口 R 相对于端口 C 的位移，m 物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **p**。有关详细信息，请参阅 Connecting Simscape Networks to Simscape Multibody Joints。

#### 依赖关系

要启用此端口，请将 **Interface displacement** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口气体

与转换器入口关联的气体守恒端口。

### **H** — 转换器内部温度热

与转换器内部气体温度关联的热守恒端口。

### **R** — 杆机械平移

与运动界面关联的机械平移守恒端口。

### **C** — 壳体机械平移

与转换器壳体关联的机械平移守恒端口。

## 参数

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

选择转换器相对于转换器气体体积的相对方向：

- `Pressure at A causes positive displacement of R relative to C` — 气体体积增加导致端口 **R** 相对于端口 **C** 产生正位移。
- `Pressure at A causes negative displacement of R relative to C` — 气体体积增加导致端口 **R** 相对于端口 **C** 产生负位移。

### **Interface displacement** — 选择确定相对端口位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 位移的方法：

- `Calculate from velocity of port R relative to port C` — 基于模块方程，从相对端口速度计算位移。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **p**，以传递来自 Multibody 关节的位移信息。仅当使用 Translational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅 How to Pass Position Information。

### **Initial interface displacement** — 仿真开始时端口 R 相对于端口 C 的平移偏移量 `0 m`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的平移偏移量。值为 0 对应于初始气体体积等于 **Dead volume**。

#### 依赖关系

当 **Interface displacement** 参数设置为 `Calculate from velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive displacement of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative displacement of R relative to C`，则参数值必须小于或等于 0。

### **Interface cross-sectional area** — 气体施加压力以产生平移力的面积 `0.01 m^2`（默认）

气体施加压力以产生平移力的面积。

### **Dead volume** — 界面位移为 0 时的气体体积 `1e-5 m^3`（默认）

界面位移为 0 时的气体体积。

### **Cross-sectional area at port A** — 转换器入口处垂直于流动路径的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于气体流动路径。

### **Environment pressure specification** — 选择环境压力 `Atmospheric pressure`（默认）| `Specified pressure` 的指定方法

选择环境压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的气体属性（G）模块指定的大气压。
- `Specified pressure` — 使用 **Environment pressure** 参数指定一个值。

### **Environment pressure** — 转换器外部压力 `0.101325 MPa`（默认）

转换器外部作用于转换器气体体积压力的压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体与机械平移网络之间的接口

Translational Mechanical Converter (G) 模块对气体网络与机械平移网络之间的接口进行建模。该模块将气体压力转换为机械力，反之亦然。它可用作线性执行器的构建模块。

该转换器包含可变体积的气体。压力和温度基于该气体体积的可压缩性和热容量演化。**Mechanical orientation** 参数允许您指定气体体积的增加是否导致端口 **R** 相对于端口 **C** 的正位移或负位移。

端口 **A** 是与转换器入口关联的气体守恒端口。端口 **H** 是与转换器内部气体温度关联的热守恒端口。端口 **R** 和 **C** 分别是与移动接口和转换器外壳关联的机械平移守恒端口。

### 质量平衡

质量守恒方程与 Constant Volume Chamber (G) 模块的方程类似，并增加了一个与气体体积变化相关的项：

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt+ρIdVdt=m˙A

其中：

- ∂M∂p 是气体体积的质量在恒定温度和体积下对压力的偏导数。
- ∂M∂T 是气体体积的质量在恒定压力和体积下对温度的偏导数。
- *p*I 是气体体积的压力。端口 **A** 处的压力假定等于该压力，*p*A = *p*I。
- *T*I 是气体体积的温度。端口 **H** 处的温度假定等于该温度，*T*H = *T*I。
- *ρ*I 是气体体积的密度。
- *V* 是气体体积。
- *t* 是时间。
- m˙A 是端口 **A** 处的质量流量。当流量流入模块时，与端口关联的流量为正。

### 能量平衡

能量守恒方程也与 Constant Volume Chamber (G) 模块的方程类似。附加项考虑了气体体积的变化，以及气体对移动接口所做的压力-体积功：

∂U∂p⋅dpIdt+∂U∂T⋅dTIdt+ρIhIdVdt=ΦA+QH

其中：

- ∂U∂p 是气体体积的内能在恒定温度和体积下对压力的偏导数。
- ∂U∂T 是气体体积的内能在恒定压力和体积下对温度的偏导数。
- ФA 是端口 **A** 处的能量流量。
- *Q*H 是端口 **H** 处的热流量。
- *h*I 是气体体积的比焓。

### 理想气体和半理想气体模型的偏导数

气体体积的质量 *M* 和内能 *U* 在恒定体积下对压力和温度的偏导数取决于气体属性模型。对于理想气体和半理想气体模型，方程为：

∂M∂p=VρIpI∂M∂T=−VρITI∂U∂p=V(hIZRTI−1)∂U∂T=VρI(cpI−hITI)

其中：

- *ρ*I 是气体体积的密度。
- *V* 是气体体积。
- *h*I 是气体体积的比焓。
- *Z* 是压缩因子。
- *R* 是比气体常数。
- *c*pI 是气体体积的定压比热。

### 真实气体模型的偏导数

对于真实气体模型，气体体积的质量 *M* 和内能 *U* 在恒定体积下对压力和温度的偏导数为：

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

其中：

- *β* 是气体体积的等温体积模量。
- *α* 是气体体积的等压热膨胀系数。

### 气体体积

气体体积取决于运动界面的位移：

V=Vdead+Sintxintεint

其中：

- *V*dead 是死体积。
- *S*int 是界面横截面积。
- *x*int 是界面位移。
- *ε*int 是机械方向系数。如果 **Mechanical orientation** 为 `Pressure at A causes positive displacement of R relative to C`，则 *ε*int = 1。如果 **Mechanical orientation** 为 `Pressure at A causes negative displacement of R relative to C`，则 *ε*int = –1。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **p** 来指定端口 **R** 相对于端口 **C** 的位移。否则，模块根据相对端口速度计算界面位移。当气体体积等于死体积时，界面位移为零。然后，根据 **Mechanical orientation** 参数值：

- 如果为 `Pressure at A causes positive displacement of R relative to C`，则当气体体积从死体积增加时，界面位移增加。
- 如果为 `Pressure at A causes negative displacement of R relative to C`，则当气体体积从死体积增加时，界面位移减小。

### 力平衡

气体体积上运动界面的力平衡为

Fint=(penv−pI)Sintεint

其中：

- *F*int 是从端口 **R** 到端口 **C** 的力。
- *p*env 是环境压力。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Gas Volume。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- 转换器外壳是完全刚性的。
- 端口 **A** 和转换器内部之间没有流动阻力。
- 端口 **H** 和转换器内部之间没有热阻。
- 运动界面是完全密封的。
- 模块不建模运动界面的机械效应，例如硬限位、摩擦和惯性。
