---
type: simulink-block
title: 'Unbalanced Load'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'unbalancedload'
documentation_source_path: 'ref/unbalancedload.html'
language: zh-CN
chinese_source: worker-translation
---

# Unbalanced Load

## 端口

### 守恒端口

### **LConn 1** — 轴连接机械旋转

与不平衡负载的轴连接相关联的机械旋转守恒端口。

## 参数

### **Parameterization** — 用于对转动惯量建模的选项 `Circular rotation`（默认）| `Elliptical rotation` | `By table lookup`

用于对不平衡负载的转动惯量建模的参数化选项。选择 `Circular rotation` 或 `Elliptical rotation`，以根据负载的旋转路径来参数化负载惯量。选择 `By table lookup`，以直接沿其旋转路径提供负载惯量。

### **Moment of inertia about own axis** — 转动惯量 `1` `kg*m^2`（默认）| 正标量

不平衡负载绕其固有旋转轴的恒定转动惯量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Circular rotation`。

### **Mass** — 负载质量 `1` `kg`（默认）| 正标量

不平衡负载的质量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Circular rotation`。

### **Distance from axis to center of rotation** — 偏移半径 `.01` `m`（默认）| 正标量

主旋转轴与旋转路径中心之间的距离。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Circular rotation`。

### **Radius of rotation** — 旋转半径 `.01` `m`（默认）| 正标量

不平衡负载所经过的圆形旋转路径的半径。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Circular rotation`。

### **Radius of rotation inline with distance from axis** — 半长轴半径 `.01` `m`（默认）| 正标量

不平衡负载所经过的椭圆旋转路径的半长轴长度。该半长轴与连接主旋转轴和椭圆旋转中心的线段共线。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Elliptical rotation`。

### **Radius of rotation perpendicular to distance from axis** — 半短轴半径 `.005` `m`（默认）| 正标量

不平衡负载所经过的椭圆旋转路径的半短轴长度。该半短轴垂直于连接主旋转轴和椭圆旋转中心的线段。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Elliptical rotation`。

### **Angle vector** — 角度 `[0, pi, 3 * pi / 2]` `rad`（默认）| 向量

用于指定负载惯量的角度位置数组。该模块使用线性插值计算所指定角度之间的负载惯量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Inertia vector** — 惯量 `[1, 10, 1]` `kg*m^2`（默认）| 向量

负载绕其固有旋转轴的惯量数组。每个惯量对应于 **Angle vector** 参数中指定的一个角度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

## 所属库

Simscape / Driveline / Inertias & Loads

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

具有角度相关转动惯量的负载

Unbalanced Load 模块表示转动惯量随旋转角度变化的负载所产生的效应。示例包括旋转轴的摆动以及偏心旋转机器的振动。您可以按负载的旋转路径指定负载惯量，也可以将其指定为角度-惯量查找表。

该模块提供两种旋转路径参数化方式。一种假设不平衡负载做圆周运动。另一种假设其做椭圆运动。在每种情况下，不平衡负载与主旋转轴之间的距离都会随旋转角度变化。该变化的距离会使转动惯量（由平行轴定理给出）在旋转过程中发生变化：

I(θ)=I0+Mr2(θ)，

其中：

- *I* 是绕主旋转轴的转动惯量。
- *I*0 是不平衡负载绕其固有旋转轴的转动惯量。
- *M* 是不平衡负载的总质量。
- *r* 是不平衡负载与主旋转轴之间的距离。

转动惯量对角度的依赖性会导致作用在不平衡负载上的惯性力矩也具有角度依赖性：

TI(θ)=I(θ)ω˙，

其中：

- *T*I 是惯性力矩。
- *ω* 是负载的角速度。

如果负载沿圆形路径运动，则其到主旋转轴的距离由下式给出

r(θ)=(rCcos(θ)+rA)2+(rCsin(θ))2，

其中：

- *r*A 是主旋转轴与偏移旋转轴之间的距离。
- *r*C 是圆形路径的半径。

**圆形旋转路径**

如果负载沿椭圆路径运动，则其到主旋转轴的距离由下式给出

r(θ)=(r∥cos(θ)+rA)2+(r⊥sin(θ))2，

其中：

- *r*∥ 是与到主旋转轴距离共线的椭圆路径半径。
- *r*⊥ 是垂直于到主旋转轴距离的椭圆路径半径。

**椭圆旋转路径**
