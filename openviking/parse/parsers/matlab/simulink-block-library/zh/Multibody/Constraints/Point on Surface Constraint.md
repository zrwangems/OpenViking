---
type: simulink-block
title: 'Point on Surface Constraint'
family: 'sm'
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
```yaml
ports:
- name: B
  summary: 基础坐标系 frame
  direction: output
- name: F
  summary: 从动坐标系 frame
  direction: output
- name: f
  summary: 约束力向量
  direction: output
- name: t
  summary: 约束力矩向量
  direction: output
```

### Geometry

### **B** — 基础坐标系 frame

与约束曲面关联的 Geometry 端口，该曲面由
Infinite
Plane 模块等模块指定。
### Frame

### **F** — 从动坐标系 frame

从动坐标系，其原点被限制在连接到 Point on Surface
Constraint 模块端口 **B** 的二维曲面上。从动坐标系的原点
在二维曲面上运动，具有五个自由度（三个
旋转和两个平移）。
### 输出

### **f** — 约束力向量

作用在点与曲面之间的约束力，以向量形式返回。有关
更多信息，请参阅 Measure Joint Constraint Forces。如果将
 **Resolution Frame** 参数设置为
`Base`，则感测到的力是相对于
连接到端口 **B** 的曲面的参考坐标系。

#### 依赖关系

要启用此端口，请在 **Constraint Force/Torque Sensing** 下选择
**Force Vector**。

### **t** — 约束力矩向量

作用在点与曲面之间的约束力矩，以向量形式返回。有关
更多信息，请参阅 Force and Torque Sensing。如果将
 **Resolution Frame** 参数设置为
`Base`，则感测到的力矩是相对于
连接到端口 **B** 的曲面的参考坐标系。

#### 依赖关系

要启用此端口，请在 **Constraint Force/Torque Sensing** 下选择
**Torque Vector**。
## 参数
```yaml
parameters:
- name: Direction
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: ''
- name: Resolution Frame
  summary: 解析测量值的坐标系 Base（默认）| Follower
  group: ''
- name: Force Vector
  summary: 是否感测约束力 off（默认）| on
  group: ''
- name: Torque Vector
  summary: 是否感测约束力矩 off（默认）| on
  group: ''
```

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量约束力和力矩的方向。反转此方向
会改变测量值的符号。有关更多信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 解析测量值的坐标系 `Base`（默认）| `Follower`

用于解析测量向量量的坐标系。有关更多信息，请参阅 Selecting a Measurement Frame。

### **Force Vector** — 是否感测约束力 `off`（默认）| `on`

选择此参数以显示端口 **f**，该端口
输出 **B** 和
**F** 坐标系之间的约束力向量。

### **Torque Vector** — 是否感测约束力矩 `off`（默认）| `on`

选择此参数以显示端口 **t**，该端口
输出 **B** 和
**F** 坐标系之间的约束力矩向量。
## 所属库

Simscape / Multibody / Constraints

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

坐标系原点与二维曲面之间的运动学约束

Point on Surface Constraint 模块将点限制在
二维曲面上。附着在点上的坐标系具有五个自由度（三个
旋转和两个平移）。此动画展示了使用
Point on Surface Constraint 模块将一个
砖块的顶点约束到平面的示例。该顶点在平面上平移和旋转。请注意，
重力方向为 -*Z* 方向，且砖块与平面之间没有接触。

Point on Surface Constraint 示例

Point on Surface Constraint 模块有两个端口：
**F** 和 **B**。端口 **F** 是一个
坐标系端口，其原点对应于该点。端口 **B** 是一个
Geometry 端口，您将其连接到二维曲面的几何。目前，
Point on Surface Constraint 模块仅支持
Infinite
Plane 模块。

您可以使用此模块感测点与二维
曲面之间的约束力和力矩。力和力矩在基础坐标系或从动坐标系中解析，具体
取决于 **Resolution Frame** 参数的设置。
