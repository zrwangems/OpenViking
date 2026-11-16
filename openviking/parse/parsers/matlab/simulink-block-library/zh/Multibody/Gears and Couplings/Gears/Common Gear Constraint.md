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

### 坐标系

### **B** — 基座坐标系（Frame）

基座齿轮体上的连接坐标系。

### **F** — 随动坐标系（Frame）

随动齿轮体上的连接坐标系。

## 参数

### **Type** — 基座与随动齿轮体之间的啮合类型 `External`（默认） | `Internal`

基座与随动齿轮体之间的啮合类型。如果两个齿轮的齿都朝外，选择 `External`。如果一个齿轮的齿朝内，选择 `Internal`。这种齿轮称为内齿轮。节圆半径较大的齿轮用作内齿轮。

### **Center Distance** — 基座与随动齿轮中心之间的距离 `20` `cm`（默认） | 长度单位的正标量

基座与随动齿轮体中心之间的距离。该距离是基座与随动齿轮节圆半径之和。

#### 依赖项

当 **Specification Method** 参数设置为 `Center Distance and Ratio` 时，此参数启用。

### **Gear Ratio (Nf/Nb)** — 随动齿轮齿数与基座齿轮齿数之比 `1.0`（默认） | 无单位正标量

随动齿轮齿数除以基座齿轮齿数。该模块使用此比值确定基座与随动齿轮轴之间传输的速度和扭矩。

#### 依赖项

当 **Specification Method** 参数设置为 `Center Distance and Ratio` 时，此参数启用。

### **Base Gear Radius** — 基座齿轮体节圆的半径 `10` `cm`（默认） | 长度单位的正标量

基座齿轮体节圆的半径。节圆是一个假想圆，与齿轮体同心并与齿接触点相切。

#### 依赖项

当 **Specification Method** 参数设置为 `Pitch Circle Radii` 时，此参数启用。

### **Follower Gear Radius** — 随动齿轮体节圆的半径 `10` `cm`（默认） | 长度单位的正标量

随动齿轮体节圆的半径。节圆是一个假想圆，与齿轮体同心并与齿接触点相切。

#### 依赖项

当 **Specification Method** 参数设置为 `Pitch Circle Radii` 时，此参数启用。

## 所属库

Simscape / Multibody / Gears and Couplings / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有平行旋转轴的两个共面直齿轮体之间的运动学约束

Common Gear Constraint 模块表示具有平行旋转轴的两个共面直齿轮体之间的运动学约束。齿轮啮合可以在两个齿轮上均为外部啮合，也可以在其中一个齿轮上为内部啮合。基座和随动坐标系端口标识直齿轮体上的连接坐标系。齿轮旋转轴与坐标系 *z* 轴重合。

该模块仅表示直齿轮系统特有的运动学约束。齿轮惯量和几何是实体属性，必须使用实体模块指定。齿轮约束模型是理想模型。齿隙以及由齿间库仑摩擦和粘性摩擦导致的齿轮损耗均被忽略。但是，您可以通过在关节模块中指定阻尼系数来对关节处的粘性摩擦建模。

### 齿轮几何

公共齿轮约束根据齿轮节圆的尺寸进行参数化。节圆是一个假想圆，与齿轮体同心并与齿接触点相切。图中标记为 `RB` 和 `RF` 的节圆半径，是将齿轮简化为相互接触的摩擦圆柱时齿轮所具有的半径。

### 齿轮装配

齿轮约束出现在闭合运动学环中。该图显示了简单公共齿轮模型的闭环拓扑。关节模块将齿轮体连接到公共固定件或载体，定义它们之间的最大自由度。Common Gear Constraint 模块连接齿轮体，消除一个自由度并有效耦合两个齿轮运动。

### 装配要求

该模块对齿轮连接坐标系的相对位置和方向施加特殊限制。这些限制确保齿轮仅以适合啮合的距离和角度装配。该模块在模型装配期间（首次尝试将齿轮置于啮合状态时）强制实施这些限制，但依赖模型的其余部分在仿真期间保持齿轮啮合。

**位置限制**

- 基座和随动坐标系的 *z* 轴之间的距离（图中记为 *d*B-F）必须等于齿轮中心之间的距离。此约束确保齿轮的旋转轴处于适合啮合的适当距离。
- 随动坐标系原点必须位于基座坐标系的 *xy* 平面上。此约束确保一个齿轮的节圆与另一个齿轮的节圆共面。

**方向限制**

- 基座和随动坐标系的 *z* 轴必须指向相同方向。此约束确保齿轮旋转轴相互平行。图中显示基座和随动坐标系的 *z* 轴指向屏幕外。
