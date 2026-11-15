---
type: simulink-block
title: 'Point on Curve Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Other Constraints'
documentation_page: 'pointoncurveconstraint'
documentation_source_path: 'ref/pointoncurveconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Point on Curve Constraint

## 端口

### 几何

### **B** — 基座坐标系 frame

与由 Spline 模块定义的曲线关联的几何端口。
### 坐标系

### **F** — 从动坐标系 frame

从动坐标系，其原点被限制在连接到端口 **B** 的曲线上。
### 输出

### **f** — 约束力向量

作用在点与曲线之间的约束力，以向量形式返回。有关详细信息，请参阅测量关节约束力。如果将 **Resolution Frame** 参数设置为 `Base`，则感测到的力是相对于连接到端口 **B** 的曲线的参考坐标系。

#### 依赖项

要启用此端口，请在 **Constraint Force/Torque Sensing** 下，选择 **Force Vector**。

### **t** — 约束力矩向量

作用在点与曲线之间的约束力矩，以向量形式返回。有关详细信息，请参阅力和力矩感测。如果将 **Resolution Frame** 参数设置为 `Base`，则感测到的力矩是相对于连接到端口 **B** 的曲线的参考坐标系。

#### 依赖项

要启用此端口，请在 **Constraint Force/Torque Sensing** 下，选择 **Torque Vector**。

## 参数

### **Direction** — 测量方向 `Follower on Base`（默认） | `Base on Follower`

测量约束力和力矩的方向。反转此方向会改变测量值的符号。有关详细信息，请参阅力和力矩测量方向。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认） | `Follower`

用于解析所测量向量量的坐标系。有关详细信息，请参阅选择测量坐标系。

### **Force Vector** — 是否感测约束力 `off`（默认） | `on`

选择此参数将显示端口 **f**，该端口输出 **B** 和 **F** 坐标系之间的约束力向量。

### **Torque Vector** — 是否感测约束力矩 `off`（默认） | `on`

选择此参数将显示端口 **t**，该端口输出 **B** 和 **F** 坐标系之间的约束力矩向量。

## 所属库

Simscape / Multibody / Constraints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

坐标系原点与曲线路径之间的运动学约束

Point on Curve Constraint 模块将点限制在曲线上。连接到该点的坐标系可根据模型中的其他约束自由旋转。使用 Point on Curve Constraint 模块对点到曲线约束进行建模，例如过山车与轨道之间或凸轮从动件与凸轮之间的约束。

点到曲线约束示例

Point on Curve Constraint 模块有两个端口：
**F** 和 **B**。端口 **F** 是坐标系端口，其原点对应于该点。端口 **B** 是几何端口，您将其连接到曲线。避免斜率急剧变化的曲线，因为这可能导致仿真问题。

您可以使用此模块感测点与曲线之间的约束力和力矩。根据 **Resolution Frame** 参数的设置，该模块在基座坐标系或从动坐标系中解析这些力和力矩。
