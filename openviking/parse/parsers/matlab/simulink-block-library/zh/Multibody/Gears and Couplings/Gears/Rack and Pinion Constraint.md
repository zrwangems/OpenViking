---
type: simulink-block
title: 'Rack and Pinion Constraint'
family: 'gears-and-couplings'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'rackandpinionconstraint'
documentation_source_path: 'ref/rackandpinionconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Rack and Pinion Constraint

## 端口

### 坐标系

### **B** — 基座坐标系 frame

小齿轮体上的连接坐标系。

### **F** — 随动坐标系 frame

齿条体上的连接坐标系。

## 参数

### **Pinion Radius** — 小齿轮体节圆的半径 `10` `cm`（默认）| 长度单位下的正标量

小齿轮体节圆的半径。节圆是一个与小齿轮体同心且与轮齿接触点相切的假想圆。

## 所属库

Simscape / Multibody / Gears and Couplings / Gears

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

平移齿条体与旋转小齿轮体之间的运动学约束

Rack and Pinion Constraint 模块表示平移齿条体与旋转小齿轮体之间的运动学约束。基座坐标系端口标识小齿轮体上的连接坐标系，随动坐标系端口标识齿条体上的连接坐标系。小齿轮旋转轴和齿条平移轴与坐标系的 *z* 轴重合。

该模块仅表示齿条-小齿轮系统特有的运动学约束。齿轮惯量和几何形状是实体属性，必须使用实体模块指定。齿轮约束模型是理想的。齿间库仑摩擦和黏性摩擦导致的齿隙和齿轮损耗被忽略。但是，可以通过在关节模块中指定阻尼系数来对关节处的黏性摩擦建模。

### 齿轮几何

齿条-小齿轮约束根据小齿轮节圆的尺寸进行参数化。节圆是一个与小齿轮体同心且与轮齿接触点相切的假想圆。图中标记为 `RB` 的节圆半径是假设将小齿轮简化为与齿条的砖块近似接触的摩擦圆柱时，小齿轮所应具有的半径。

### 齿轮装配

齿轮约束出现在闭环运动学回路中。该图显示了简单齿条-小齿轮模型的闭环拓扑。关节模块将齿条体和小齿轮体连接到共同的固定件或载体，定义它们之间的最大自由度。Rack and Pinion Constraint 模块连接齿条体和小齿轮体。

### 装配要求

该模块对齿轮连接坐标系的相对位置和方向施加特殊限制。这些限制确保齿轮仅在适合啮合的距离和角度下装配。该模块在模型装配期间（即首次尝试将齿轮置于啮合状态时）强制执行这些限制，但依赖模型其余部分在仿真期间保持齿轮啮合。

**位置限制**

- 基座坐标系与随动坐标系原点之间沿随动坐标系 *y* 轴的距离必须等于小齿轮半径。此约束确保齿条的节点与小齿轮的旋转轴保持适当距离。
- 随动坐标系原点必须位于基座坐标系的 *xy* 平面上。此约束确保齿条的节点与小齿轮的节圆共面。

**方向限制**

- 随动坐标系的 *x* 轴必须垂直于基座坐标系的 *xy* 平面。此约束确保齿条和小齿轮共面，因此它们的运动轴相互垂直。
