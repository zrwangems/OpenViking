---
type: simulink-block
title: 'Common Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'commongearconstraint'
documentation_source_path: 'ref/commongearconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Common Gear Constraint

## 端口
```yaml
ports:
- name: B
  summary: 基座坐标系 frame
  direction: unspecified
- name: F
  summary: 从动坐标系 frame
  direction: unspecified
```

### Frame

### **B** — 基座坐标系 frame

基座齿轮体上的连接坐标系。

### **F** — 从动坐标系 frame

从动齿轮体上的连接坐标系。
## 参数
```yaml
parameters:
- name: Type
  summary: 基座齿轮体与从动齿轮体之间的啮合类型 External（默认）| Internal
  group: ''
- name: Center Distance
  summary: 基座齿轮与从动齿轮中心之间的距离 20 cm（默认）| 以长度单位为单位的正标量
  group: ''
- name: Gear Ratio (Nf/Nb)
  summary: 从动齿轮齿数与基座齿轮齿数之比 1.0（默认）| 无量纲正标量
  group: ''
- name: Base Gear Radius
  summary: 基座齿轮体节圆的半径 10 cm（默认）| 以长度单位为单位的正标量
  group: ''
- name: Follower Gear Radius
  summary: 从动齿轮体节圆的半径 10 cm（默认）| 以长度单位为单位的正标量
  group: ''
```

### **Type** — 基座齿轮体与从动齿轮体之间的啮合类型 `External`（默认）| `Internal`

基座齿轮体与从动齿轮体之间的啮合类型。如果两个齿轮的轮齿均朝外，请选择
`External`。如果一个齿轮的轮齿朝内，请选择 `Internal`。这种齿轮称为内齿圈。节圆半径较大的齿轮作为内齿圈。

### **Center Distance** — 基座齿轮与从动齿轮中心之间的距离 `20` `cm`（默认）| 以长度单位为单位的正标量

基座齿轮体与从动齿轮体中心之间的距离。该距离为基座齿轮与从动齿轮节圆半径之和。

#### 依赖关系

当 **Specification
Method** 参数设置为 `Center Distance
and Ratio` 时，此参数启用。

### **Gear Ratio (Nf/Nb)** — 从动齿轮齿数与基座齿轮齿数之比 `1.0`（默认）| 无量纲正标量

从动齿轮齿数除以基座齿轮齿数。该模块使用此比值来确定基座齿轮轴与从动齿轮轴之间传递的速度和扭矩。

#### 依赖关系

当 **Specification
Method** 参数设置为 `Center Distance
and Ratio` 时，此参数启用。

### **Base Gear Radius** — 基座齿轮体节圆的半径 `10` `cm`（默认）| 以长度单位为单位的正标量

基座齿轮体节圆的半径。节圆是一个假想的圆，与齿轮体同心并与轮齿接触点相切。

#### 依赖关系

当 **Specification
Method** 参数设置为 `Pitch Circle
Radii` 时，此参数启用。

### **Follower Gear Radius** — 从动齿轮体节圆的半径 `10` `cm`（默认）| 以长度单位为单位的正标量

从动齿轮体节圆的半径。节圆是一个假想的圆，与齿轮体同心并与轮齿接触点相切。

#### 依赖关系

当 **Specification
Method** 参数设置为 `Pitch Circle
Radii` 时，此参数启用。
## 所属库

Simscape / Multibody / Gears and Couplings / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

两个共面直齿轮体之间具有平行旋转轴的运动学约束

Common Gear Constraint 模块表示两个共面直齿轮体之间具有平行旋转轴的运动学约束。齿轮啮合可以是两个齿轮的外啮合，也可以是其中一个齿轮的内啮合。基座和从动坐标系端口标识直齿轮体上的连接坐标系。齿轮旋转轴与坐标系的 *z* 轴重合。

该模块仅表示直齿轮系统特有的运动学约束。齿轮惯量和几何形状是实体属性，必须使用实体模块指定。齿轮约束模型是理想的。忽略轮齿之间的侧隙以及由于库仑摩擦和粘性摩擦引起的齿轮损耗。但是，您可以通过在关节模块中指定阻尼系数来对关节处的粘性摩擦进行建模。

### 齿轮几何形状

Common gear constraint 根据齿轮节圆的尺寸进行参数化。节圆是一个假想的圆，与齿轮体同心并与轮齿接触点相切。图中标记为
`RB` 和
`RF` 的节圆半径，是齿轮在简化为相互接触的摩擦圆柱时所具有的半径。

### Gear Assembly

齿轮约束出现在闭运动环路中。该图展示了一个简单常见齿轮模型的闭环拓扑结构。关节模块将齿轮体连接到共同的固定件或载体，定义它们之间的最大自由度。Common Gear Constraint 模块连接齿轮体，消除一个自由度并有效地耦合两个齿轮运动。

### Assembly Requirements

该模块对齿轮连接坐标系的相对位置和方向施加特殊限制。这些限制确保齿轮仅在适合啮合的距离和角度下装配。该模块在模型装配期间、首次尝试将齿轮置于啮合状态时强制执行这些限制，但在仿真期间依赖模型的其余部分使齿轮保持啮合。

**Position Restrictions**

- 基座坐标系与从动坐标系 *z* 轴之间的距离，在图中记为 *d*B-F，必须等于齿轮中心之间的距离。此约束确保齿轮的旋转轴处于适合啮合的适当距离。
- 从动坐标系原点必须位于基座坐标系的 *xy* 平面上。此约束确保一个齿轮的节圆与另一个齿轮的节圆共面。

**Orientation Restrictions**

- 基座坐标系与从动坐标系的 *z* 轴必须指向相同方向。此约束确保齿轮旋转轴彼此平行。图中显示基座坐标系与从动坐标系的 *z* 轴指向屏幕外。
