---
type: simulink-block
title: 'Cylinder Friction (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylinderfrictiontl'
documentation_source_path: 'ref/cylinderfrictiontl.html'
language: zh-CN
chinese_source: worker-translation
---

# Cylinder Friction (TL)

## 端口

### 守恒

### **A** — 液体端口（热液体）

与孔口的液体入口或出口点关联的热液体守恒端口。

### **B** — 液体端口（热液体）

与孔口的液体入口或出口点关联的热液体守恒端口。

### **C** — 机械端口（速度，机械平移）

与气缸壳体运动关联的机械平移守恒端口。

### **R** — 机械端口（速度，机械平移）

与气缸杆运动关联的机械平移守恒端口。

## 参数

### **两侧流体相同** — 对模块两侧相同流体建模的选项 `on`（默认） | `off`

是否对模块两侧的相同流体进行建模。如果选中此参数，模块会将流体属性传播通过该模块。清除此参数可将每个腔室建模为不同流体，其中每个腔室连接到隔离的流体网络。

### **启动力与库仑摩擦力之比** — 启动力与库仑摩擦力之比 `1.2`（默认） | 正标量

启动力与库仑摩擦力之比，RBreak,Coulomb=FbreakFCoulomb。

### **启动摩擦速度** — 抵抗摩擦力运动的阈值 `0.1 m/s`（默认） | 正标量

气缸抵抗摩擦力运动时的阈值。

### **预紧力** — 由密封组件引起的气缸初始力 `20 N`（默认） | 标量

由密封组件引起的气缸初始力。该模块使用此参数计算库仑摩擦力。

### **库仑摩擦力系数** — 库仑摩擦力系数 `1e-6 N/Pa`（默认） | 正标量

库仑摩擦力系数。该模块使用此参数计算库仑摩擦力。

### **粘性摩擦系数** — 粘性摩擦系数 `100 N*s/m`（默认） | 正标量

粘性摩擦系数。该模块使用此参数计算粘性摩擦力。

### **环境压力指定** — 压力参考源 `Atmospheric pressure`（默认） | `Specified pressure`

用于库仑摩擦计算的压力参考。

### **环境压力** — 用户定义的压力参考 `0.101325 MPa`（默认） | 正标量

用于库仑摩擦计算的用户定义压力参考。

#### 依赖关系

要启用此参数，请将 **环境压力指定** 设置为 `Specified pressure`。

## 所属库

Simscape / Fluids / Thermal Liquid / Actuators / Auxiliary Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2024a: 在模块两侧对不同流体建模

清除新的 **两侧流体相同** 参数，以阻止流体属性传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

## 描述

热液体网络中的气缸摩擦

Cylinder Friction (TL) 模块对热液体网络中运动气缸的摩擦进行建模。总摩擦力是 Stribeck、库仑和粘性效应的组合。库仑摩擦分量包括密封件施加的任何初始力以及气缸中压力的影响。

该模块使用与 Simscape Foundational Library Translational Friction 模块相同的方法计算 Stribeck 力和粘性力。

### 库仑摩擦力

库仑摩擦力是垂直于摩擦表面作用的力。气缸运动在固定气缸壳体内产生径向应力，该应力随气缸压缩内部流体而增大。径向应力垂直于气缸运动，并产生阻碍气缸运动的库仑摩擦力。

库仑摩擦力为

FCoulomb=Fctanh(υυCoulomb,th),

其中 *ν* 是端口 **R** 和 **C** 之间的相对速度，*νR* – *νC*。*νCoulomb,th* 是库仑力的阈值速度，

υCoulomb,th=vbreak10.

库仑力的阈值速度与静摩擦力的阈值速度是不同的量，模块使用后者计算 Stribeck 摩擦力，尽管二者都充当阈值区域，以确保库仑力和 Stribeck 力的平滑建模。

*FC* 是由密封预紧和气缸压力产生的力贡献，

FC=Fpreload+fCoulomb(PA+PB),

其中：

- *Fpreload* 是 **预紧力** 参数的值。
- *fCoulomb* 是 **库仑摩擦力系数** 参数的值。
- *PA* 和 *PB* 分别是气缸端口 **A** 和 **B** 处的压力。这些值是关于环境压力的表压。你可以通过 **环境压力指定** 参数将这些值指定为大气压或另一个用户定义值。

### Stribeck 摩擦力和粘性摩擦力

Stribeck 摩擦力 *FStribeck* 是低速下占主导的摩擦分量。该模块使用以下方程

FStribeck=2e(Rbreak,Coulomb−1)⋅FC(υυstatic,th)e−(υυstatic,th)2,

其中：

- *Rbreak,Coulomb* 是 **启动力与库仑摩擦力之比** 参数的值，RBreak,Coulomb=FbreakFCoulomb。
- *ν* 是气缸速度，υ=υR−υC。
- *νstatic,th* 是静力矩的阈值速度

  υstatic,th=2vbreak,

  其中 *vbreak* 是 **启动摩擦速度** 参数的值。模块在 0 和静力矩的阈值速度之间建立过渡范围，以确保摩擦力的平滑建模。
- *FC* 是由密封预紧和气缸压力产生的力贡献。

粘性摩擦力基于工作流体的 **粘性摩擦系数** 参数值 *fviscous*，并与气缸速度成正比

Fviscous=fviscousυ.
