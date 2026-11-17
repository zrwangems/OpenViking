---
type: simulink-block
title: 'Universal Joint'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'universaljoint'
documentation_source_path: 'ref/universaljoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Universal Joint

## 端口
```yaml
ports:
- name: B
  summary: 基轴机械旋转
  direction: input
- name: F
  summary: 从动轴机械旋转
  direction: input
- name: A
  summary: 交叉角物理信号
  direction: input
```

### 守恒

### **B** — 基轴机械旋转

与基轴关联的守恒旋转端口。

### **F** — 从动轴机械旋转

与从动轴关联的守恒旋转端口。
### 输入

### **A** — 交叉角物理信号

交叉角的物理信号输入端口。
## 参数
```yaml
parameters:
- name: Maximum joint angle
  summary: 最大关节交叉角，*A* pi/4 rad（默认）| 0 ≤ *A* < pi/2 | 标量
  group: ''
- name: Joint compliance
  summary: 柔顺性模型 off（默认）| on
  group: ''
- name: Joint stiffness
  summary: 刚度系数，k 1e6 N*m/rad（默认）| 标量
  group: ''
- name: Joint damping
  summary: 阻尼系数，b 1e3 N*m/(rad/s)（默认）| 标量
  group: ''
- name: Initial base shaft angle
  summary: 基轴初始角度 0 rad（默认）| 标量
  group: ''
- name: Initial torque from base to follower shaft
  summary: 初始扭矩 0 N*m（默认）| 标量
  group: ''
```

j

### **Maximum joint angle** — 最大关节交叉角，*A* `pi/4` `rad`（默认）| 0 ≤ *A* < pi/2 | 标量

关节允许的最大交叉角。该角度衡量基轴与从动轴绕基轴销的旋转。该角度的值必须落在 0≤A<pi/2 rad 范围内。

### **Joint compliance** — 柔顺性模型 `off`（默认）| `on`

模块的柔顺性模型：

- `off` — 不对刚度和阻尼建模。
- `on` — 对刚度和阻尼建模。

### **Joint stiffness** — 刚度系数，k `1e6` `N*m/rad`（默认）| 标量

关节的线性弹簧刚度，以角速度比的从动轴分量表示。弹簧刚度考虑了由于材料柔顺性而在关节中存储的弹性能量。

#### 依赖关系

要启用此参数，请选中 **Joint compliance**。

### **Joint damping** — 阻尼系数，b `1e3` `N*m/(rad/s)`（默认）| 标量

关节的线性阻尼系数，以角速度比的从动轴分量表示。阻尼系数考虑了由于材料柔顺性而在关节中耗散的能量。

#### 依赖关系

要启用此参数，请选中 **Joint compliance**。

### **Initial base shaft angle** — 基轴初始角度 `0` `rad`（默认）| 标量

仿真开始时基轴绕其长度轴的旋转角度。

### **Initial torque from base to follower shaft** — 初始扭矩 `0` `N*m`（默认）| 标量

仿真开始时基轴传递给从动轴的扭矩。该扭矩决定了关节处材料柔顺性的初始状态。将此值设置为大于零可为轴施加扭矩预载。更改此值会改变由于材料柔顺性引起的初始瞬态响应。

#### 依赖关系

要启用此参数，请选中 **Joint compliance**。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2025a：枚举更新

**Joint compliance** 参数现在使用复选框。在之前的版本中，此参数使用下拉菜单。

## 描述

两个传动系轴之间的旋转联轴器

Universal Joint 模块表示两个传动系轴之间的旋转联轴器。该联轴器在轴之间传递扭矩，使它们在施加负载下作为一个整体旋转。联轴器内部的两个旋转自由度允许轴以一定角度连接。该交叉角根据端口 **A** 的物理信号输入而变化。可选的柔顺性（建模为并联的弹簧-阻尼器组）允许联轴器在负载下变形。

您可以将 Universal Joint 模块用作两个旋转传动系组件之间的连接，例如，汽车传动系中主动轴与从动轴之间的连接。

轴的角速度之比取决于两个参数：两轴之间的交叉角和基轴的旋转角度。物理信号输入提供交叉角，而属性检查器参数提供基轴初始角度。这两个角度根据以下非线性方程确定两轴角速度之比：

ωF=cos(A)1−sin2(A)⋅cos2(θB)ωB，

其中：

- *ωF* 和 *tF* 分别是从动轴绕其长度轴的角速度和扭矩。
- *ωB* 和 *tB* 分别是基轴绕其长度轴的角速度和扭矩。
- *θB* 是基轴绕其长度轴的旋转角度。
- *A* 是基轴与从动轴绕基轴销的交叉角。

图中的两个示意图说明了方程参数。在每个示意图中，左侧轴表示基轴，而右侧轴表示从动轴。右侧示意图显示了左侧示意图中的联轴器在轴绕其长度轴旋转 90° 后的情况（虚线线段）。

在图中，交叉角是两轴绕基轴销的角度。该角度的绝对值必须落在 `0 ≤ A < Maximum intersection angle` 范围内。基轴角度是基轴绕其长度轴的角度。基轴角度也是基轴角速度 *ωB* 的时间积分。

### 柔顺性

您可以在万向节扭矩传递中纳入柔顺性的影响。当您清除 **Joint compliance** 时，

ωF=cos(A)1−sin2(A)⋅cos2(θB)ωBtB=−cos(A)1−sin2(A)⋅cos2(θB)tF

当您选中 **Joint compliance** 时，

θC=θF−cos(A)1−sin2(A)⋅cos2(θB)θBtB=−cos(A)1−sin2(A)⋅cos2(θB)tFtF=bωC+kθC

其中：

- *k* 是 **Joint stiffness** 参数的值。
- *b* 是 **Joint damping** 参数的值。
- *θC* 是扭转柔顺角。
- *ωC* 是扭转柔顺角速度。
