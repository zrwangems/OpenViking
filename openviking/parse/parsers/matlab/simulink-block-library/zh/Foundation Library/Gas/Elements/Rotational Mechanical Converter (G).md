---
type: simulink-block
title: 'Rotational Mechanical Converter (G)'
family: 'simscape'
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
```yaml
ports:
- name: q
  summary: 端口 R 相对于端口 C 的旋转，rad，物理信号
  direction: input
- name: A
  summary: 转换器入口气体
  direction: input
- name: H
  summary: 转换器内部温度，热
  direction: input
- name: R
  summary: 杆，机械旋转
  direction: input
- name: C
  summary: 壳体，机械旋转
  direction: input
```

### 输入

### **q** — 端口 R 相对于端口 C 的旋转，rad，物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **q**。有关详细信息，请参阅 Connecting Simscape Networks to Simscape Multibody Joints。

#### 依赖关系

要启用此端口，请将 **Interface rotation** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口气体

与转换器入口相关联的气体守恒端口。

### **H** — 转换器内部温度，热

与转换器内部气体温度相关联的热守恒端口。

### **R** — 杆，机械旋转

与运动界面相关联的机械旋转守恒端口。

### **C** — 壳体，机械旋转

与转换器壳体相关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Mechanical orientation
  summary: 选择转换器方向 Pressure at A causes positive rotation of R relative to C（默认）| Pressure at A causes negative rotation of
    R relative to C
  group: ''
- name: Interface rotation
  summary: 选择确定相对端口位置的方法 Calculate from angular velocity of port R relative to port C（默认）| Provide input signal from Multibody
    joint
  group: ''
- name: Initial interface rotation
  summary: 仿真开始时端口 R 相对于端口 C 的旋转偏移 0 rad（默认）
  group: ''
- name: Interface volume displacement
  summary: 每单位旋转所排开的气体体积 0.01 m^3/rad（默认）
  group: ''
- name: Dead volume
  summary: 界面旋转为 0 时的气体体积 1e-5 m^3（默认）
  group: ''
- name: Cross-sectional area at port A
  summary: 转换器入口处垂直于流动路径的面积 0.01 m^2（默认）
  group: ''
- name: 环境压力设定
  summary: 选择环境压力 Atmospheric pressure（默认）| Specified pressure 的设定方法
  group: ''
- name: 环境压力
  summary: 转换器外部压力 0.101325 MPa（默认）
  group: ''
```

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive rotation of R relative to C`（默认）| `Pressure at A causes negative rotation of R relative to C`

选择运动界面相对于转换器气体体积的对齐方式：

- `Pressure at A causes positive rotation of R relative to C` — 气体体积增加导致端口 **R** 相对于端口 **C** 产生正旋转。
- `Pressure at A causes negative rotation of R relative to C` — 气体体积增加导致端口 **R** 相对于端口 **C** 产生负旋转。

### **Interface rotation** — 选择确定相对端口位置的方法 `Calculate from angular velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 旋转的方法：

- `Calculate from angular velocity of port R relative to port C` — 基于模块方程，从相对端口角速度计算旋转。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅 How to Pass Position Information。

### **Initial interface rotation** — 仿真开始时端口 R 相对于端口 C 的旋转偏移 `0 rad`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移。值为 0 对应于初始气体体积等于 **Dead volume**。

#### 依赖关系

当 **Interface rotation** 参数设置为 `Calculate from angular velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive rotation of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative rotation of R relative to C`，则参数值必须小于或等于 0。

### **Interface volume displacement** — 每单位旋转所排开的气体体积 `0.01 m^3/rad`（默认）

运动界面每单位旋转所排开的气体体积。

### **Dead volume** — 界面旋转为 0 时的气体体积 `1e-5 m^3`（默认）

界面旋转为 0 时的气体体积。

### **Cross-sectional area at port A** — 转换器入口处垂直于流动路径的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于气体流动路径。

### **环境压力设定** — 选择环境压力 `Atmospheric pressure`（默认）| `Specified pressure` 的设定方法

选择环境压力的设定方法：

- `Atmospheric pressure` —
  使用由连接到回路的气体属性（G）模块指定的大气压。
- `Specified pressure` —
  使用 **Environment pressure** 参数指定一个值。

### **环境压力** — 转换器外部压力 `0.101325 MPa`（默认）

转换器外部作用于转换器气体体积压力的压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。
## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体与机械旋转网络之间的接口

Rotational Mechanical Converter (G) 模块对气体网络与机械旋转网络之间的接口进行建模。该模块将气体压力转换为机械扭矩，反之亦然。它可用作旋转执行器的构建模块。

该转换器包含可变体积的气体。压力和温度基于该气体体积的可压缩性和热容量演化。**Mechanical orientation** 参数允许您指定气体体积的增加是否导致端口 **R** 相对于端口 **C** 的正旋转或负旋转。

端口 **A** 是与转换器入口关联的气体守恒端口。端口 **H** 是与转换器内部气体温度关联的热守恒端口。端口 **R** 和 **C** 分别是与运动界面和转换器外壳关联的机械旋转守恒端口。

### 质量平衡

质量守恒方程与 Constant Volume Chamber (G) 模块的方程类似，并增加了一个与气体体积变化相关的项：

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt+ρIdVdt=m˙A

其中：

- ∂M∂p 是气体体积的质量在恒定温度和体积下对压力的偏导数。
- ∂M∂T 是气体体积的质量在恒定压力和体积下对温度的偏导数。
- *p*I 是气体体积的压力。假设端口 A 处的压力等于该压力，*p*A = *p*I。
- *T*I 是气体体积的温度。假设端口 H 处的温度等于该温度，*T*H = *T*I。
- *ρ*I 是气体体积的密度。
- *V* 是气体体积。
- *t* 是时间。
- m˙A 是端口 **A** 处的质量流量。当流量流入模块时，与端口关联的流量为正。

### 能量平衡

能量守恒方程也与 Constant Volume Chamber (G) 模块的方程类似。附加项考虑了气体体积的变化，以及气体对运动界面所做的压力-体积功：

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

气体体积取决于运动界面的旋转：

V=Vdead+Dintθintεint

其中：

- *V*dead 是死体积。
- *D*int 是界面体积排量。
- *θ*int 是界面旋转。
- *ε*int 是机械方向系数。如果 **Mechanical orientation** 为 `Pressure at A causes positive rotation of R relative to C`，则 *ε*int = 1。如果 **Mechanical orientation** 为 `Pressure at A causes negative rotation of R relative to C`，则 *ε*int = –1。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **q** 来指定端口 **R** 相对于端口 **C** 的旋转。否则，模块根据相对端口角速度计算界面旋转。当气体体积等于死体积时，界面旋转为零。然后，根据 **Mechanical orientation** 参数值：

- 如果为 `Pressure at A causes positive rotation of R relative to C`，则当气体体积从死体积增加时，界面旋转增加。
- 如果为 `Pressure at A causes negative rotation of R relative to C`，则当气体体积从死体积增加时，界面旋转减小。

### 扭矩平衡

气体体积上运动界面的扭矩平衡为

τint=(penv−pI)Dintεint

其中：

- *τ*int 是从端口 **R** 到端口 **C** 的扭矩。
- *p*env 是环境压力。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Gas Volume。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- 转换器外壳完全刚性。
- 端口 **A** 和转换器内部之间没有流动阻力。
- 端口 **H** 和转换器内部之间没有热阻。
- 运动界面完全密封。
- 模块不建模运动界面的机械效应，例如硬限位、摩擦和惯性。
