---
type: simulink-block
title: 'Bevel Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'bevelgearconstraint'
documentation_source_path: 'ref/bevelgearconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Bevel Gear Constraint

## 端口

### 坐标系

### **B** — 基座坐标系 坐标系

基座锥齿轮上的连接坐标系。

### **F** — 从动坐标系 坐标系

从动锥齿轮上的连接坐标系。

## 参数

### **Base Gear Radius** — 基座齿轮节圆半径 `10` `cm`（默认）| 带长度单位的正标量

基座齿轮节圆的半径。节圆与齿轮同心并与齿接触点相切。齿轮半径影响基座齿轮体和从动齿轮体之间的扭矩传递。

### **Follower Gear Radius** — 从动齿轮节圆半径 `10` `cm`（默认）| 带长度单位的正标量

从动齿轮节圆的半径。节圆与齿轮同心并与齿接触点相切。齿轮半径影响基座齿轮体和从动齿轮体之间的扭矩传递。

### **Shaft Axes** — 齿轮轴角的参数化方式 `Perpendicular`（默认）| `Arbitrarily Oriented`

锥齿轮轴之间相交角的参数化方式。选择 `Perpendicular` 使齿轮轴对齐成直角。选择 `Arbitrarily Oriented` 使齿轮轴对齐成从 `0` 到 `180` `deg` 的任意角度。

### **Angle Between Shafts** — 基座轴与从动轴之间的角度 `90` `deg`（默认）| 正标量

从基座和从动坐标系 z 轴延伸的假想线之间的角度。该角度必须在 `0`–`180` `deg` 范围内。基座齿轮和从动齿轮之间的实际角度（通常通过刚性变换、关节以及偶尔其他约束设定）必须与此处指定的角度相同。

#### 依赖关系

当 **Shaft Axes** 参数设置为 `Arbitrarily Oriented` 时，此参数启用。

## 所属库

Simscape / Multibody / Gears and Couplings / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

具有成角度相交旋转轴的两个锥齿轮体之间的运动学约束

Bevel Gear Constraint 模块表示两个齿轮体之间的运动学约束，这两个齿轮体具有以指定角度相交的旋转轴。基座和从动坐标系端口标识齿轮体上的连接坐标系。齿轮旋转轴与连接坐标系的 *z* 轴重合。齿轮以由齿轮节圆半径确定的固定速度比旋转。

该模块仅表示锥齿轮系统特有的运动学约束特性。齿轮惯量和几何形状是实体属性，必须使用实体模块指定。齿轮约束模型是理想的。齿间库仑摩擦和粘性摩擦导致的齿隙和齿轮损耗被忽略。但是，您可以通过在关节模块中指定阻尼系数来建模关节处的粘性摩擦。

### 齿轮几何

锥齿轮约束根据齿轮节圆的尺寸进行参数化。节圆是与齿轮体同心并与齿接触点相切的假想圆。图中标记为 `RB` 和 `RF` 的节圆半径是齿轮若简化为相互接触的摩擦锥时所具有的外半径。

### 齿轮装配

齿轮约束出现在闭运动链中。该图显示了简单锥齿轮模型的闭环拓扑结构。关节模块将齿轮体连接到公共固定装置或载体，定义它们之间的最大自由度。Bevel Gear Constraint 模块连接齿轮体，消除一个自由度并有效耦合齿轮运动。

### 装配要求

该模块对齿轮连接坐标系的相对位置和方向施加特殊限制。这些限制确保齿轮仅在适合啮合的距离和角度下装配。该模块在模型装配期间、首次尝试将齿轮置于啮合状态时强制执行这些限制，但在仿真期间依赖模型的其余部分使齿轮保持啮合。

**位置限制**

- 基座坐标系与从动坐标系原点之间的距离必须使得，在给定轴角和节圆半径下，齿轮节圆彼此相切。该距离记为
  *d*B-F，由余弦定理得出：

  dB−F=RB2+RF2−2RBRFcos(π−θ),

  其中 *R*B 是基座齿轮的节圆半径，
  *R*F 是从动齿轮的节圆半径，*θ*Shaft
  是旋转轴之间的相交角。
- 基座坐标系与从动坐标系原点沿基座坐标系
  *z* 轴的距离，记为
  *Δz*B，必须等于：

  ΔzB=RF·sin(θShaft)
- 基座坐标系与从动坐标系原点沿从动坐标系
  *z* 轴的距离，记为
  *Δz*F，必须等于：

  ΔzF=RB·sin(θShaft)

**方向限制**

- 从基座和从动 z 轴延伸出的假想线必须在模块对话框中设置的轴角处相交。该角度在图中记为 θB-F。如果
  **Shaft Axes** 参数设置为
  `Perpendicular`，则该角度为
  90°。
