---
type: simulink-block
title: 'Point on Surface Constraint'
family: 'constraints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Constraints'
documentation_page: 'pointonsurfaceconstraint'
documentation_source_path: 'ref/pointonsurfaceconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Point on Surface Constraint

## 端口

### 几何

### **B** — 基础坐标系 frame

与由 Infinite Plane 模块等模块指定的约束曲面关联的几何端口。
### 坐标系

### **F** — 随动坐标系 frame

随动坐标系，其原点被约束到连接到 Point on Surface Constraint 模块端口 **B** 的二维曲面上。随动坐标系的原点在二维曲面上移动，并具有五个自由度（三个旋转自由度和两个平移自由度）。
### 输出

### **f** — 约束力向量

作用在点与曲面之间的约束力，以向量形式返回。有关详细信息，请参阅测量关节约束力。如果将 **Resolution Frame** 参数设置为 `Base`，则检测到的力是相对于连接到端口 **B** 的曲面的参考坐标系。

#### 依赖关系

要启用此端口，请在 **Constraint Force/Torque Sensing** 下选择 **Force Vector**。

### **t** — 约束力矩向量

作用在点与曲面之间的约束力矩，以向量形式返回。有关详细信息，请参阅力和力矩检测。如果将 **Resolution Frame** 参数设置为 `Base`，则检测到的力矩是相对于连接到端口 **B** 的曲面的参考坐标系。

#### 依赖关系

要启用此端口，请在 **Constraint Force/Torque Sensing** 下选择 **Torque Vector**。

## 参数

### **Direction** — 测量方向 `Follower on Base`（默认） | `Base on Follower`

测量约束力和约束力矩的方向。反转此方向会改变测量值的符号。有关详细信息，请参阅力和力矩测量方向。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base`（默认） | `Follower`

用于解析所测量向量量的坐标系。有关详细信息，请参阅选择测量坐标系。

### **Force Vector** — 是否检测约束力 `off`（默认） | `on`

选择此参数可显示端口 **f**，该端口输出 **B** 和 **F** 坐标系之间的约束力向量。

### **Torque Vector** — 是否检测约束力矩 `off`（默认） | `on`

选择此参数可显示端口 **t**，该端口输出 **B** 和 **F** 坐标系之间的约束力矩向量。

## 所属库

Simscape / Multibody / Constraints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

坐标系原点与二维曲面之间的运动学约束

Point on Surface Constraint 模块将一个点约束到二维曲面上。附着到该点的坐标系具有五个自由度（三个旋转自由度和两个平移自由度）。此动画展示了使用 Point on Surface Constraint 模块将砖块的一个顶点约束到平面的示例。该顶点在平面上平移和旋转。注意，重力沿 -*Z* 方向，并且砖块与平面之间没有接触。

Point on Surface Constraint 示例

Point on Surface Constraint 模块有两个端口：**F** 和 **B**。端口 **F** 是一个 frame 端口，其原点对应该点。端口 **B** 是一个几何端口，可将其连接到二维曲面的几何。目前，Point on Surface Constraint 模块仅支持 Infinite Plane 模块。

您可以使用此模块检测点与二维曲面之间的约束力和约束力矩。根据 **Resolution Frame** 参数的设置，力和力矩在基础坐标系或随动坐标系中解析。
