---
type: simulink-block
title: 'Cylinder Friction (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'cylinderfrictionil'
documentation_source_path: 'ref/cylinderfrictionil.html'
language: zh-CN
chinese_source: worker-translation
---

# Cylinder Friction (IL)

## 端口

### 守恒端口

### **A** — 液体端口 等温液体

与节流孔液体进入或离开点相关联的等温液体守恒端口。

### **B** — 液体端口 等温液体

与节流孔液体进入或离开点相关联的等温液体守恒端口。

### **C** — 机械端口 速度 机械平移

与缸体运动相关联的机械平移守恒端口。

### **R** — 机械端口 速度 机械平移

与缸杆运动相关联的机械平移守恒端口。

## 参数

### **Same fluid on both sides** — 用于对模块两侧流体进行相同建模的选项 `on`（默认）| `off`

是否对模块两侧的流体进行相同建模。如果选择此参数，模块将通过模块传播流体属性。清除此参数可将每个腔室建模为不同的流体，其中每个腔室连接到隔离的流体网络。

### **Breakaway to Coulomb friction force ratio** — 启动力与库仑摩擦力之比 `1.2`（默认）| 正标量

启动力与库仑摩擦力之比，RBreak,Coulomb=FbreakFCoulomb。

### **Breakaway friction velocity** — 克服摩擦力运动的阈值 `0.1 m/s`（默认）| 正标量

克服摩擦力运动的阈值。

### **Preload force** — 由于密封组件在缸中产生的初始力 `20 N`（默认）| 标量

由于密封组件在缸中产生的初始力。模块使用此参数计算库仑摩擦力。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6 N/Pa`（默认）| 正标量

库仑摩擦力系数。模块使用此参数计算库仑摩擦力。

### **Viscous friction coefficient** — 粘性摩擦系数 `100 N*s/m`（默认）| 正标量

粘性摩擦系数。此参数用于计算粘性摩擦力。

### **Environment pressure specification** — 压力参考源 `Atmospheric pressure`（默认）| `Specified pressure`

用于库仑摩擦计算的压力参考。

### **Environment pressure** — 用户定义的压力参考 `0.101325 MPa`（默认）| 正标量

用于库仑摩擦计算的用户定义压力参考。

#### 依赖关系

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：对模块两侧的不同流体进行建模

清除新的 **Same fluid on both sides** 参数，以阻止流体属性的传播，并将每个腔室建模为连接到其自身隔离流体网络的不同流体。

## 描述

为具有运动部件的缸添加摩擦

Cylinder Friction (IL) 模块对等温液体网络中运动缸上的摩擦进行建模。总摩擦是 Stribeck、库仑和粘性效应的组合。库仑摩擦分量包括密封件施加的任何初始力以及缸中压力的影响。

Stribeck 力和粘性力的计算方式与 Simscape 基础库 Translational Friction 模块相同。

### 库仑摩擦力

库仑摩擦力是垂直于摩擦表面作用的力。缸的运动在固定缸套内产生径向应力，该应力随着缸压缩内部流体而增大。径向应力垂直于缸的运动方向，并产生阻碍缸运动的库仑摩擦力。

库仑摩擦力为

FCoulomb=Fctanh(υυCoulomb,th),

其中 *ν* 是端口 **R** 和 **C** 之间的相对速度，*νR* – *νC*。*νCoulomb,th* 是库仑力的阈值速度，

υCoulomb,th=vbreak10.

库仑力的阈值速度与静态力的阈值速度是不同的量，模块使用后者计算 Stribeck 摩擦力，尽管它们都用作阈值区域以确保库仑力和 Stribeck 力的平滑建模。

*FC* 是来自密封预紧力和缸中压力的力贡献，

FC=Fpreload+fCoulomb(PA+PB),

其中：

- *Fpreload* 是 **Preload force** 参数的值。
- *fCoulomb* 是 **Coulomb friction force coefficient** 参数的值。
- *PA* 和 *PB* 分别是缸端口 **A** 和 **B** 处的压力。这些值是相对于环境压力的表压。您可以使用 **Environment pressure specification** 参数将这些值指定为大气压或另一个用户定义值。

### Stribeck 摩擦力和粘性摩擦力

Stribeck 摩擦力 *FStribeck* 是在低速下占主导地位的摩擦分量。模块使用以下方程

FStribeck=2e(Rbreak,Coulomb−1)⋅FC(υυstatic,th)e−(υυstatic,th)2,

其中：

- *Rbreak,Coulomb* 是 **Breakaway to Coulomb friction force ratio** 参数的值，RBreak,Coulomb=FbreakFCoulomb。
- *ν* 是缸的速度，υ=υR−υC。
- *νstatic,th* 是静态扭矩的阈值速度

  υstatic,th=2vbreak,

  其中 *vbreak* 是 **Breakaway friction velocity** 参数的值。模块在 0 和静态扭矩的阈值速度之间建立过渡范围，以确保摩擦力的平滑建模。
- *FC* 是来自密封预紧力和缸中压力的力贡献。

粘性摩擦力基于工作流体的 **Viscous friction coefficient** 参数值 *fviscous*，并与缸的速度成正比

Fviscous=fviscousυ。
