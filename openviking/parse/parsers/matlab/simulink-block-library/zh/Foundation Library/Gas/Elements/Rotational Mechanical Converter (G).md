---
type: simulink-block
title: 'Rotational Mechanical Converter (G)'
family: 'gas'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'rotationalmechanicalconverterg'
documentation_source_path: 'ref/rotationalmechanicalconverterg.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Mechanical Converter (G)

## 端口

### 输入

### **q** — 端口 R 相对于端口 C 的旋转，rad 物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到该关节的位置传感端口 **q**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

#### 依赖关系

要启用此端口，请将 **接口旋转** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口气体

与转换器入口关联的气体守恒端口。

### **H** — 转换器内部温度

与转换器内部气体温度关联的热守恒端口。

### **R** — 杆机械旋转

与运动接口关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与转换器壳体关联的机械旋转守恒端口。

## 参数

### **机械方向** — 选择转换器方向 `Pressure at A causes positive rotation of R relative to C`（默认）| `Pressure at A causes negative rotation of R relative to C`

选择运动接口相对于转换器气体体积的对齐方式：

- `Pressure at A causes positive rotation of R relative to C` — 气体体积增加会导致端口 **R** 相对于端口 **C** 正向旋转。
- `Pressure at A causes negative rotation of R relative to C` — 气体体积增加会导致端口 **R** 相对于端口 **C** 负向旋转。

### **接口旋转** — 选择确定相对端口位置的方法 `Calculate from angular velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 旋转的方法：

- `Calculate from angular velocity of port R relative to port C` — 根据模块方程，从相对端口角速度计算旋转。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

### **初始接口旋转** — 仿真开始时端口 R 相对于端口 C 的旋转偏移 `0 rad`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移。值 0 对应于初始气体体积等于 **死区体积**。

#### 依赖关系

当 **接口旋转** 参数设置为 `Calculate from angular velocity of port R relative to port C` 时启用。

- 如果 **机械方向** 为 `Pressure at A causes positive rotation of R relative to C`，则参数值必须大于或等于 0。
- 如果 **机械方向** 为 `Pressure at A causes negative rotation of R relative to C`，则参数值必须小于或等于 0。

### **接口体积排量** — 单位旋转所排开的气体体积 `0.01 m^3/rad`（默认）

运动接口每单位旋转所排开的气体体积。

### **死区体积** — 接口旋转为 0 时的气体体积 `1e-5 m^3`（默认）

接口旋转为 0 时的气体体积。

### **端口 A 处的横截面积** — 转换器入口处垂直于流动路径的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于气体流动路径。

### **环境压力规格** — 选择环境压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择环境压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路中的 Gas Properties (G) 模块指定的大气压。
- `Specified pressure` — 使用 **环境压力** 参数指定一个值。

### **环境压力** — 转换器外部的压力 `0.101325 MPa`（默认）

转换器外部压力，对抗转换器气体体积的压力。值 0 表示转换器向真空膨胀。

#### 依赖关系

当 **环境压力规格** 参数设置为 `Specified pressure` 时启用。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体网络与机械旋转网络之间的接口

Rotational Mechanical Converter (G) 模块对气体网络与机械旋转网络之间的接口进行建模。该模块将气体压力转换为机械扭矩，反之亦然。它可用作旋转执行器的构建块。

该转换器包含可变体积的气体。压力和温度基于该气体体积的可压缩性和热容量演变。**机械方向** 参数允许您指定气体体积增加是否导致端口 **R** 相对于端口 **C** 正向或负向旋转。

端口 **A** 是与转换器入口关联的气体守恒端口。端口 **H** 是与转换器内部气体温度关联的热守恒端口。端口 **R** 和 **C** 分别是与运动接口和转换器壳体关联的机械旋转守恒端口。

### 质量平衡

质量守恒方程与 Constant Volume Chamber (G) 模块的方程类似，但增加了一个与气体体积变化相关的项：

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt+ρIdVdt=m˙A

其中：

- ∂M∂p 是气体体积的质量在恒定温度和体积下对压力的偏导数。
- ∂M∂T 是气体体积的质量在恒定压力和体积下对温度的偏导数。
- *p*I 是气体体积的压力。假设端口 A 处的压力等于该压力，*p*A = *p*I。
- *T*I 是气体体积的温度。假设端口 H 处的温度等于该温度，*T*H = *T*I。
- *ρ*I 是气体体积的密度。
- *V* 是气体体积。
- *t* 是时间。
- m˙A 是端口 **A** 处的质量流量。与端口关联的流量在流入模块时为正。

### 能量平衡

能量守恒方程也与 Constant Volume Chamber (G) 模块的方程类似。附加项考虑了气体体积的变化，以及气体对运动接口所做的压力-体积功：

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
- *c*pI 是气体体积的定压比热容。

### 真实气体模型的偏导数

对于真实气体模型，气体体积的质量 *M* 和内能 *U* 在恒定体积下对压力和温度的偏导数为：

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

其中：

- *β* 是气体体积的等温体积模量。
- *α* 是气体体积的等压热膨胀系数。

### 气体体积

气体体积取决于运动接口的旋转：

V=Vdead+Dintθintεint

其中：

- *V*dead 是死区体积。
- *D*int 是接口体积排量。
- *θ*int 是接口旋转。
- *ε*int 是机械方向系数。如果 **机械方向** 为 `Pressure at A causes positive rotation of R relative to C`，则 *ε*int = 1。如果 **机械方向** 为 `Pressure at A causes negative rotation of R relative to C`，则 *ε*int = –1。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **q** 指定端口 **R** 相对于端口 **C** 的旋转。否则，模块根据相对端口角速度计算接口旋转。当气体体积等于死区体积时，接口旋转为零。然后，根据 **机械方向** 参数的值：

- 如果为 `Pressure at A causes positive rotation of R relative to C`，则当气体体积从死区体积增加时，接口旋转增加。
- 如果为 `Pressure at A causes negative rotation of R relative to C`，则当气体体积从死区体积增加时，接口旋转减小。

### 扭矩平衡

作用在气体体积上的运动接口的扭矩平衡为

τint=(penv−pI)Dintεint

其中：

- *τ*int 是从端口 **R** 到端口 **C** 的扭矩。
- *p*env 是环境压力。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标以及具有有限气体体积的模块的初始条件。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

### 假设和限制

- 转换器壳体完全刚性。
- 端口 **A** 与转换器内部之间没有流动阻力。
- 端口 **H** 与转换器内部之间没有热阻。
- 运动接口完全密封。
- 该模块不对运动接口的机械效应建模，例如硬限位、摩擦和惯性。
