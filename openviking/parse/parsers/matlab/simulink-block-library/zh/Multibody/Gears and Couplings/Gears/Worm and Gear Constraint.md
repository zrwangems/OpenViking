---
type: simulink-block
title: 'Worm and Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'wormandgearconstraint'
documentation_source_path: 'ref/wormandgearconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Worm and Gear Constraint

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

### 坐标系

### **B** — 基座坐标系 frame

蜗杆本体上的连接坐标系。

### **F** — 从动坐标系 frame

蜗轮本体上的连接坐标系。
## 参数
```yaml
parameters:
- name: Worm Direction
  summary: 蜗杆螺纹的旋绕方向 Right-Hand（默认）| Left-Hand
  group: ''
- name: Worm Lead Angle
  summary: 蜗杆螺纹与旋转平面之间的夹角 10 deg（默认）| 0 到 180 之间的正标量，单位为角度
  group: ''
- name: Specification Method
  summary: 蜗轮几何参数化方式 Center Distance and Ratio（默认）| Pitch Circle Radii
  group: ''
- name: Center Distance
  summary: 蜗杆与蜗轮中心之间的距离 20 cm（默认）| 单位为长度的正标量
  group: ''
- name: Ratio (Ng/Nw)
  summary: 蜗轮齿数与蜗杆螺纹数之比 1（默认）| 正的无量纲标量
  group: ''
- name: Worm Radius
  summary: 蜗杆分度圆半径 10 cm（默认）| 单位为长度的正标量
  group: ''
- name: Gear Radius
  summary: 蜗轮分度圆半径 10 cm（默认）| 单位为长度的正标量
  group: ''
```

### **Worm Direction** — 蜗杆螺纹的旋绕方向 `Right-Hand`（默认）| `Left-Hand`

蜗杆螺纹相对于基座坐标系 z 轴的旋绕方向。从基座坐标系原点观察，右旋螺纹沿基座坐标系 z 轴逆时针方向缠绕。左旋螺纹沿顺时针方向缠绕。该参数决定蜗杆与蜗轮本体的相对运动方向。

### **Worm Lead Angle** — 蜗杆螺纹与旋转平面之间的夹角 `10` `deg`（默认）| `0` 到 `180` 之间的正标量，单位为角度

蜗杆螺纹切线与垂直于基座坐标系 z 轴的平面之间的夹角。导程角影响蜗杆旋转一整圈时对应的蜗轮旋转量。

### **Specification Method** — 蜗轮几何参数化方式 `Center Distance and Ratio`（默认）| `Pitch Circle Radii`

用于指定蜗杆和蜗轮几何形状的参数化方式。您可以按蜗轮中心之间的距离或各蜗轮半径来指定蜗轮尺寸。

### **Center Distance** — 蜗杆与蜗轮中心之间的距离 `20` `cm`（默认）| 单位为长度的正标量

蜗杆与蜗轮中心之间的距离。该距离必须与蜗轮本体和公共载体本体之间的刚性变换、关节以及任何其他约束所施加的距离一致。

#### 依赖关系

当 **Specification Method** 参数设置为 `Center Distance and Ratio` 时，此参数启用。

### **Ratio (Ng/Nw)** — 蜗轮齿数与蜗杆螺纹数之比 `1`（默认）| 正的无量纲标量

蜗轮齿数与蜗杆螺纹数（或称*头数*）之比。该比值影响蜗杆与蜗轮之间传递的扭矩。

#### 依赖关系

当 **Specification Method** 参数设置为 `Center Distance and Ratio` 时，此参数启用。

### **Worm Radius** — 蜗杆分度圆半径 `10` `cm`（默认）| 单位为长度的正标量

蜗杆分度圆半径。即蜗杆旋转轴线与齿-螺纹接触点之间的距离。该参数影响蜗杆与蜗轮之间传递的扭矩。

#### 依赖关系

当 **Specification Method** 参数设置为 `Pitch Circle Radius` 时，此参数启用。

### **Gear Radius** — 蜗轮分度圆半径 `10` `cm`（默认）| 单位为长度的正标量

蜗轮分度圆半径。即蜗轮旋转轴线与齿-螺纹接触点之间的距离。该参数影响蜗杆与蜗轮之间传递的扭矩。

#### 依赖关系

当 **Specification Method** 参数设置为 `Pitch Circle Radius` 时，此参数启用。
## 所属库

Simscape / Multibody / Gears and Couplings / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

蜗轮与蜗杆刚体之间的运动学约束，具有垂直且不相交的旋转轴

Worm and Gear Constraint 模块表示以直角保持的蜗杆与蜗轮刚体之间的运动学约束。基座坐标系端口标识蜗杆上的连接坐标系，从动坐标系端口标识蜗轮上的连接坐标系。旋转轴与连接坐标系的 *z* 轴重合。蜗杆和蜗轮以由蜗轮节圆半径或齿-螺纹比确定的固定速度比旋转。

蜗杆螺纹方向可以遵循右旋或左旋约定。所使用的约定决定蜗杆和蜗轮旋转速度的相对方向。右旋约定使蜗杆和蜗轮绕各自的 z 轴沿相同方向旋转。左旋约定则使蜗杆和蜗轮沿相反方向旋转。

该模块仅表示蜗杆-蜗轮系统所特有的运动学约束特性。蜗轮惯量和几何形状是实体属性，必须使用实体模块指定。蜗轮约束模型是理想的。忽略齿间库仑摩擦和粘性摩擦导致的齿隙和蜗轮损耗。但是，可以通过在关节模块中指定阻尼系数来对关节处的粘性摩擦进行建模。

### 蜗轮几何

齿条-小齿轮约束根据蜗杆和蜗轮节圆的尺寸进行参数化。节圆是与蜗杆和蜗轮刚体同心并与螺纹接触点相切的假想圆。图中标记为 `RB` 和 `RF` 的节圆半径，是蜗杆和蜗轮在相互接触时若简化为摩擦圆柱体所应具有的半径。

### 蜗轮装配

蜗轮约束出现在闭式运动学回路中。该图显示了简单蜗杆-蜗轮模型的闭环拓扑。关节模块将蜗杆和蜗轮刚体连接到公共固定装置或载体，定义它们之间的最大自由度。Worm and Gear Constraint 模块连接蜗杆和蜗轮刚体，消除一个自由度并有效耦合蜗杆和蜗轮的运动。

### 装配要求

该模块对蜗轮连接坐标系的相对位置和方向施加特殊限制。这些限制确保蜗轮仅在适合啮合的距离和角度下装配。该模块在模型装配期间、首次尝试使蜗轮啮合时强制执行这些限制，但在仿真期间依赖模型的其余部分使蜗轮保持啮合。

**位置限制**

- 基座和从动坐标系 *z* 轴之间的距离，在图中记为 dB-F，必须等于蜗轮中心之间的距离。
- 基座和从动坐标系原点之间沿从动坐标系 *z* 轴的平移偏移，在图中记为 ΔZF，必须为零。

**方向限制**

- 基座和从动坐标系的 *z* 轴必须相互垂直。图中 *z* 轴以蓝色显示。
- 从动坐标系 *z* 轴与基座坐标系 *z* 轴的叉积必须是一个从从动坐标系原点指向基座坐标系 *z* 轴的向量。图中显示了 *z* 轴及其叉积向量。叉积定义为 z^F×z^B。
