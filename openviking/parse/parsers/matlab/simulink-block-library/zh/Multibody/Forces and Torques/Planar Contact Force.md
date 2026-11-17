---
type: simulink-block
title: 'Planar Contact Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'planarcontactforce'
documentation_source_path: 'ref/planarcontactforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Planar Contact Force

## 端口
```yaml
ports:
- name: B
  summary: 基础几何体 geometry
  direction: input
- name: F
  summary: 从动几何体 geometry
  direction: input
- name: fny
  summary: 法向接触力大小，N physical signal
  direction: input
- name: ffrx
  summary: 摩擦力，N physical signal
  direction: input
- name: con
  summary: 接触信号，unitless physical signal
  direction: output
- name: pen
  summary: 穿透深度，m physical signal
  direction: output
- name: vn
  summary: 相对法向速度，m/s 物理信号
  direction: output
- name: vt
  summary: 相对切向速度，m/s 物理信号
  direction: output
- name: fn
  summary: 法向力，N 物理信号
  direction: output
- name: fnm
  summary: 法向力大小，N 物理信号
  direction: output
- name: tn
  summary: 法向力产生的力矩，N\*m 物理信号
  direction: output
- name: ffr
  summary: 摩擦力，N 物理信号
  direction: output
- name: ffrm
  summary: 摩擦力大小，N 物理信号
  direction: output
- name: tfr
  summary: 由摩擦力产生的力矩，N\*m 物理信号
  direction: output
- name: ft
  summary: 总接触力，N 物理信号
  direction: output
- name: tt
  summary: 总接触力产生的力矩，N\*m 物理信号
  direction: output
- name: Rb
  summary: 基座旋转，无量纲物理信号
  direction: output
- name: pb
  summary: 基座平移，*m* 物理信号
  direction: output
- name: Rf
  summary: 从动件旋转，无量纲物理信号
  direction: output
- name: pf
  summary: 从动件平移，*m* 物理信号
  direction: output
```

### 几何

### **B** — 基础几何体 geometry

与基础几何体关联的几何端口。

### **F** — 从动几何体 geometry

与从动几何体关联的几何端口。
### 输入

### **fny** — 法向接触力大小，N physical signal

物理信号输入端口，接受两个几何体之间的法向接触力大小。该模块将负值截断为零。

当对涉及点云的联系进行建模时，输入信号必须为 1×*N* 数组，其中 *N* 等于点数。数组的每一列指定其中一个点上的法向接触力。输入信号的大小和顺序必须与 Point Could 模块中指定的点的大小和顺序匹配。力在点的接触坐标系中解析。

当对其他类型的几何体之间的联系进行建模时，输入信号必须为标量，指定法向接触力。

#### 依赖关系

要启用此端口，请在 **Normal Force** 部分中，将 **Method** 设置为 `Provided by Input`。

### **ffrx** — 摩擦力，N physical signal

物理信号输入端口，接受两个几何体之间的摩擦力。

当对涉及点云的联系进行建模时，输入信号必须为 1×*N* 数组，其中 *N* 等于点数。数组的每一列指定其中一个点上所施加摩擦力的 *x* 分量。输入信号的大小和顺序必须与 Point Could 模块中指定的点的大小和顺序匹配。力在点的接触坐标系中解析。

当对其他类型的几何体之间的联系进行建模时，输入信号必须为标量，指定在接触坐标系中解析的所施加摩擦力的 *x* 分量。

#### 依赖关系

要启用此端口，请在 **Frictional Force** 部分中，将 **Method** 设置为 `Provided by Input`。
### 输出

### **con** — 接触信号，unitless physical signal

物理信号输出端口，输出两个几何体的接触状态。

当对涉及点云的联系进行建模时，输出为 1×*N* 数组，其中 *N* 等于点数。数组的每一列指示对应点的状态。如果输出为 1，则该点与其他几何体接触。否则，输出为 0。

当对其他类型的几何体之间的联系进行建模时，输出为标量，指示几何体是否接触。如果输出为 1，则几何体接触；如果输出为 0，则几何体分离。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Contact Signal**。

### **pen** — 穿透深度，m physical signal

物理信号输出端口，输出两个几何体之间的穿透深度。

当对涉及点云的联系进行建模时，输出为 1×*N* 数组，其中 *N* 等于点数。数组的每一列指示对应点的状态。如果该点正在穿透其他几何体，则输出为正，且等于穿透深度。否则，输出为 0。

当对其他类型的几何体之间的联系进行建模时，输出为标量，指示几何体是否正在相互穿透。如果它们正在相互穿透，则输出为正，且等于穿透深度。否则，输出为 0。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Penetration Depth**。

### **vn** — 相对法向速度，m/s 物理信号

物理信号输出端口，输出基座几何体与从动几何体接触点之间的相对法向速度。

在对涉及点云的接触进行建模时，输出为 1×*N* 数组，其中 *N* 等于点数。数组的每一列等于对应点与另一几何体上接触点之间相对速度的 *y* 分量。相对速度在对应的接触坐标系中解析。

在对其他类型几何体之间的接触进行建模时，输出为标量，等于两个几何体接触点之间相对速度的 *y* 分量。输出在接触坐标系中解析。

#### 依赖关系

要启用此端口，请在**传感**部分中，选择**相对法向速度**。

### **vt** — 相对切向速度，m/s 物理信号

物理信号输出端口，输出基座几何体与从动几何体接触点之间的相对切向速度。

在对涉及点云的接触进行建模时，输出为 1×*N* 矩阵，其中 *N* 等于点数。数组的每一列等于对应点与另一几何体上接触点之间相对速度的 *x* 分量。相对速度在对应的接触坐标系中解析。

在对其他类型几何体之间的接触进行建模时，输出为标量，等于两个几何体接触点之间相对速度的 *x* 分量。输出在接触坐标系中解析。

#### 依赖关系

要启用此端口，请在**传感**部分中，选择**相对切向速度**。

#### 力/力矩

### **fn** — 法向力，N 物理信号

两个接触几何体之间法向力的物理信号输出端口。该模块在指定解析坐标系的坐标中解析测量值，并且**方向**参数的设置会影响测量值的符号。

在对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处的法向力。

在对其他类型几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示法向力。

#### 依赖关系

要启用此端口，请在**力/力矩**部分中，选择**法向力**。

### **fnm** — 法向力大小，N 物理信号

法向力大小的物理信号输出端口。**方向**和**解析坐标系**参数不影响测量值。

在对涉及点云的接触进行建模时，输出为 1×*N* 数组，其中 *N* 等于点数。数组的每一列是对应点处法向力的大小。

在对其他类型几何体之间的接触进行建模时，输出为法向力的大小。

#### 依赖关系

要启用此端口，请在**力/力矩**部分中，选择**法向力大小**。

### **tn** — 法向力产生的力矩，N\*m 物理信号

法向力产生的力矩的物理信号输出端口。测量值是法向力与接触点相对于指定解析坐标系的位置向量的叉积。**方向**参数会影响测量值的符号。

在对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处由法向力产生的力矩。

在对其他类型几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示由法向力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Normal Torque**。

### **ffr** — 摩擦力，N 物理信号

两个接触几何体之间摩擦力的物理信号输出端口。该模块在指定的解析坐标系中解析测量值，并且 **Direction** 参数的设置会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点的数量。数组的每一列表示一个 3-D 向量，指示对应点处的摩擦力。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示摩擦力。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Force**。

### **ffrm** — 摩擦力大小，N 物理信号

两个接触几何体之间摩擦力大小的物理信号输出端口。**Direction** 和 **Resolution Frame** 参数不影响测量值。

当对涉及点云的接触进行建模时，输出为 1×*N* 数组，其中 *N* 等于点的数量。数组的每一列是对应点处摩擦力的大小。

当对其他类型的几何体之间的接触进行建模时，输出是法向接触力的大小。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Force Magnitude**。

### **tfr** — 由摩擦力产生的力矩，N\*m 物理信号

由摩擦力产生的力矩的物理信号输出端口。测量值是摩擦力与接触点相对于指定解析坐标系的位置向量的叉积。**Direction** 参数会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点的数量。数组的每一列表示一个 3-D 向量，指示对应点处由摩擦力产生的力矩。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示由摩擦力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Torque**。

### **ft** — 总接触力，N 物理信号

两个接触几何体之间总接触力的物理信号输出端口。总接触力包括法向力和摩擦力。该模块在指定的解析坐标系中解析测量值，并且 **Direction** 参数的设置会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点的数量。数组的每一列表示一个 3-D 向量，指示对应点处的总接触力。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示总接触力。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Total Force**。

### **tt** — 总接触力产生的力矩，N\*m 物理信号

总接触力矩的物理信号输出端口，该力矩由接触力产生。测量值为接触力与接触点相对于指定解算坐标系的位置矢量的叉积。**Direction** 参数会影响测量值的符号。

在对涉及点云的接触进行建模时，输出为 3×*N* 数组，其中 *N* 表示点的数量。数组的每一列表示一个三维矢量，指示对应点处由总接触力产生的接触力矩。

在对其他类型几何体之间的接触进行建模时，输出表示一个三维矢量，指示由总接触力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Total Torque**。

#### 接触坐标系

### **Rb** — 基座旋转，无量纲物理信号

物理信号端口，输出一个 3×3 旋转矩阵，该矩阵将接触坐标系中的矢量映射到基座几何体参考坐标系中的矢量。输出信号在基座几何体关联的参考坐标系中解算。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Rotation**。

### **pb** — 基座平移，*m* 物理信号

物理信号端口，输出一个 3×1 矢量，其中包含接触坐标系原点在基座几何体参考坐标系中解算的坐标。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Translation**。

### **Rf** — 从动件旋转，无量纲物理信号

物理信号端口，输出一个 3×3 旋转矩阵，该矩阵将接触坐标系中的矢量映射到从动件几何体参考坐标系中的矢量。输出信号在从动件几何体关联的参考坐标系中解算。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Follower Rotation**。

### **pf** — 从动件平移，*m* 物理信号

物理信号端口，输出一个 3×1 矢量，其中包含接触坐标系原点在从动件几何体参考坐标系中解算的坐标。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Follower Translation**。
## 参数
```yaml
parameters:
- name: Method
  summary: 指定法向接触力的方法 Smooth Spring-Damper（默认）| Provided by Input
  group: 法向力
- name: Stiffness
  summary: 接触弹簧对几何穿透的阻力 1e6 N/m（默认）| 标量
  group: 法向力
- name: Damping
  summary: 几何体穿透期间接触阻尼器对运动的阻力 1e3 N/(m/s)（默认）| 标量
  group: 法向力
- name: Transition Region Width
  summary: 弹簧-阻尼力上升至其完整值的区域 1e-4 m（默认）| 标量
  group: 法向力
- name: Method
  summary: 指定摩擦力的方法 Smooth Stick-Slip（默认）| None | Provided by Input
  group: 摩擦力
- name: Coefficient of Static Friction
  summary: 切向速度接近零时摩擦力大小与法向力大小之比 0.5（默认）| 非负标量
  group: 摩擦力
- name: Coefficient of Dynamic Friction
  summary: 切向速度较大时摩擦力大小与法向力大小之比 0.3（默认）| 非负标量
  group: 摩擦力
- name: Critical Velocity
  summary: 确定静摩擦系数与动摩擦系数之间混合的临界速度 1e-3 m/s（默认）| 标量
  group: 摩擦力
- name: Direction
  summary: 测量方向 Base on Follower（默认）| Follower on Base
  group: 传感
- name: Resolution Frame
  summary: 用于解析测量的坐标系 Contact（默认）| Base | Follower
  group: 传感
- name: Detect Contact Start and End
  summary: 将接触的开始和结束检测为零交叉事件 off（默认）| on
  group: Zero-Crossings
```

### 法向力

### **Method** — 指定法向接触力的方法 `Smooth Spring-Damper`（默认）| `Provided by Input`

指定法向接触力的方法，指定为 `Smooth Spring-Damper` 或 `Provided by Input`。

选择 `Smooth Spring-Damper` 以使用改进的弹簧-阻尼器方法对法向接触力进行建模，或选择 `Provided by Input` 以输入自定义力作为法向接触力。

### **Stiffness** — 接触弹簧对几何穿透的阻力 1e6 `N/m`（默认）| 标量

接触弹簧对几何穿透的阻力，指定为标量。弹簧刚度在接触期间为常数。弹簧刚度值越大，几何体之间的接触越硬。

#### 依赖关系

要启用此参数，请在 **Normal Force** 部分中，将 **Method** 设置为 `Smooth Spring-Damper`。

### **Damping** — 几何体穿透期间接触阻尼器对运动的阻力 1e3 `N/(m/s)`（默认）| 标量

几何体穿透期间接触阻尼器对运动的阻力，指定为标量。阻尼系数是一个常数值，表示碰撞几何体损失的能量。阻尼系数值越大，几何体碰撞时损失的能量越多，接触振动衰减得越快。使用零值来建模完美弹性碰撞，即能量守恒。

#### 依赖关系

要启用此参数，请在 **Normal Force** 部分中，将 **Method** 设置为 `Smooth
Spring-Damper`。

### **Transition Region Width** — 弹簧-阻尼力上升至其完整值的区域 1e-4 `m`（默认）| 标量

弹簧-阻尼力上升至其完整值的区域，指定为标量。该区域越小，接触开始越急剧，求解器所需的时间步长越小。减小过渡区域可提高模型精度，而扩大过渡区域可提高仿真速度。

#### 依赖关系

要启用此参数，请在 **Normal Force** 部分中，将 **Method** 设置为 `Smooth
Spring-Damper`。

### 摩擦力

### **Method** — 指定摩擦力的方法 `Smooth Stick-Slip`（默认）| `None` | `Provided by Input`

指定摩擦力的方法，指定为 `Smooth
Stick-Slip`、`None` 或 `Provided
by Input`。

选择 `None` 可忽略摩擦，选择 `Smooth
Stick-Slip` 可使用改进的粘滑方法计算摩擦力，或选择 `Provided by Input` 以输入自定义摩擦力。

### **Coefficient of Static Friction** — 切向速度接近零时摩擦力大小与法向力大小之比 0.5（默认）| 非负标量

切向速度接近零时摩擦力大小与法向力大小之比，指定为正标量。

该值由接触几何体的材料属性决定。该参数的值通常小于一，尽管对于高摩擦材料，大于一的值也是可能的。在大多数情况下，该值应高于动摩擦系数。

#### 依赖关系

要启用此参数，请在 **Frictional Force** 部分中，将 **Method** 设置为 `Smooth
Stick-Slip`。

### **Coefficient of Dynamic Friction** — 切向速度较大时摩擦力大小与法向力大小之比 0.3（默认）| 非负标量

切向速度较大时摩擦力大小与法向力大小之比，指定为非负标量。

该值由接触几何体的材料属性决定。该参数的值通常小于一，尽管对于高摩擦材料，大于一的值也是可能的。在大多数情况下，该值应小于静摩擦系数。

#### 依赖关系

要启用此参数，请在 **Frictional Force** 部分中，将 **Method** 设置为 `Smooth
Stick-Slip`。

### **Critical Velocity** — 确定静摩擦系数与动摩擦系数之间混合的临界速度 1e-3 `m/s`（默认）| 标量

确定静摩擦系数与动摩擦系数之间混合的临界速度，指定为标量。

当临界速度等于切向速度的大小时，有效摩擦系数等于 **Coefficient of Static Friction** 参数的值。当切向速度的大小超过指定的临界速度时，有效摩擦系数渐近地趋近于 **Coefficient of Dynamic Friction** 参数的值。

#### 依赖关系

要启用此参数，请在 **Frictional Force** 部分中，将 **Method** 设置为 `Smooth
Stick-Slip`。

### 传感

#### Force/Torque

### **Direction** — 测量方向 `Base on Follower`（默认）| `Follower on Base`

测量方向，指定为以下值之一：

- `Base on Follower` — 模块感测基础几何体施加在从动几何体上的力和力矩。
- `Follower on Base` — 模块感测从动几何体施加在基础几何体上的力和力矩。

此参数仅影响 **Force/Torque** 部分下的矢量输出。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Contact`（默认）| `Base` | `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Contact` — 模块在接触坐标系的坐标中解析测量值。
- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Force/Torque** 部分下的矢量输出。

### Zero-Crossings

### **Detect Contact Start and End** — 将接触的开始和结束检测为零交叉事件 off（默认）| on

选择此项可将每次接触的开始和结束检测为零交叉事件。当间隔距离从正值或零变为负值，以及从负值变为正值或零时，会发生零交叉事件。
## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2025a：将接触力和力矩作为矢量测量，并使用基础、从动或接触坐标系解析测量值

现在，您可以将法向、摩擦和总接触力及力矩输出为三维矢量。通过使用 **Direction** 参数，您可以指定输出表示的是基础几何体施加在从动几何体上的力和力矩，还是相反情况。您还可以在基础、从动或接触坐标系的坐标中解析这些矢量输出。

## 描述

对两个几何体之间的平面接触进行建模

Planar Contact Force 模块对以下几何体对之间的平面接触进行建模：

- 圆盘与圆盘
- 圆盘与线段
- 圆盘与点
- 圆盘与二维点云

在对平面接触进行建模时，两个几何体必须共面，并且基础几何体和从动几何体的 *z* 轴必须对齐并指向同一方向。

### 接触

您可以使用内置的罚函数方法，或提供自定义的法向力和摩擦力定律来对接触进行建模。平面接触力模块使用与空间接触力模块相同的罚函数方法，但法向力沿接触坐标系的 *y* 轴，摩擦力沿接触坐标系的 *x* 轴。有关罚函数模型的更多信息，请参阅接触力。

在对两个圆盘之间或圆盘与线段之间的接触进行建模时，存在一个位于穿透深度中心的单个接触点。每个几何体都有一个接触坐标系。这两个坐标系始终重合，并位于接触点处。接触坐标系的正 *y* 轴与从基础几何体指向从动几何体的接触法向方向对齐，*z* 轴与基础坐标系的 *z* 轴对齐。该图显示了两个圆盘之间的接触。**B**、**F** 和 **C** 坐标系分别是基础坐标系、从动坐标系和接触坐标系。

圆盘与圆盘接触示意图

该图显示了圆盘与线段之间接触的两种场景。

圆盘与线段示意图

在对圆盘与点之间的接触进行建模时，存在一个与点重合的单个接触点。

圆盘与点示意图

在对圆盘与二维点云之间的接触进行建模时，对于与圆盘接触的每个点都有一个接触点。平面接触力模块计算每个点的接触量，输出信号的顺序与点云模块中指定的点的顺序相同。对于未与圆盘接触的点，测量值为零。使用输入力时，输入信号的大小和顺序必须与点云模块中指定的点的大小和顺序匹配。

圆盘与点云示意图
