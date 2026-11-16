---
type: simulink-block
title: 'Spatial Contact Force'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'spatialcontactforce'
documentation_source_path: 'ref/spatialcontactforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Spatial Contact Force

## 端口

### 几何

### **B** — 基础几何体 geometry

与基础几何体关联的 geometry 端口。

### **F** — 从动几何体 geometry

与从动几何体关联的 geometry 端口。
### 输入

### **fnz** — 法向接触力大小，N physical signal

physical signal 输入端口，接受两个几何体之间的法向接触力大小。该模块将负值裁剪为零。

当对涉及点云的接触进行建模时，输入信号必须为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列指定其中一个点上的法向接触力。输入信号的大小和顺序必须与 Point Could block 中指定的点的大小和顺序匹配。力在点的接触坐标系中解析。

当对其他类型的几何体之间的接触进行建模时，输入信号必须为标量，用于指定法向接触力。

#### 依赖关系

要启用此端口，请在 **Normal Force** 部分中，将 **Method** 设置为 `Provided by Input`。

### **ffrxy** — 摩擦力，N physical signal

physical signal 输入端口，接受两个几何体之间的摩擦力。

当对涉及点云的接触进行建模时，输入信号必须为 2-by-*N* 矩阵，其中 *N* 等于点数。矩阵的每一列指定其中一个点上施加的摩擦力的 *x* 分量和 *y* 分量。输入信号的大小和顺序必须与 Point Could block 中指定的点的大小和顺序匹配。力在点的接触坐标系中解析。

当对其他类型的几何体之间的接触进行建模时，输入信号必须为 2-by-1 数组，用于指定在接触坐标系中解析的施加摩擦力的 *x* 分量和 *y* 分量。

#### 依赖关系

要启用此端口，请在 **Frictional Force** 部分中，将 **Method** 设置为 `Provided by Input`。
### 输出

### **con** — 接触信号，unitless physical signal

physical signal 输出端口，输出两个几何体的接触状态。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列指示对应点的状态。如果值为 1，则该点接触另一个几何体。否则，值为 0。

当对其他类型的几何体之间的接触进行建模时，输出为标量，指示几何体是否接触。如果输出为 1，则几何体接触；如果输出为 0，则分离。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Contact Signal**。

### **pen** — 穿透深度，m physical signal

physical signal 输出端口，输出两个几何体之间的穿透深度。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列指示对应点的状态。如果该点穿透另一个几何体，则值为正且等于穿透深度。否则，值为 0。

当对其他类型的几何体之间的接触进行建模时，输出为标量，指示几何体是否相互穿透。如果相互穿透，则输出为正。否则，输出为 0。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Penetration Depth**。

### **sep** — 分离距离，m physical signal

physical signal 输出端口，输出两个几何体之间的分离距离。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列指示对应点的状态。如果该点未穿透另一个几何体，则值为非负且等于该点与另一个几何体之间的最小距离。否则，输出为负，其绝对值等于穿透深度。

当对其他类型的几何体之间的接触进行建模时，输出为标量。如果它们未相互穿透，则输出为非负且等于两个几何体之间的最小距离。否则，输出为负，其绝对值等于穿透深度。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Separation Distance**。

### **vn** — 相对法向速度，m/s physical signal

physical signal 输出端口，提供基础几何体与从动几何体的接触点之间相对速度的 *z* 分量。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列等于对应点与另一个几何体上的接触点之间相对速度的 *z* 分量。相对速度在对应的接触坐标系中解析。

当对其他类型的几何体之间的接触进行建模时，输出为标量，等于两个几何体的接触点之间相对速度的 *z* 分量。输出在接触坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Relative Normal Velocity**。

### **vt** — 相对切向速度，m/s physical signal

physical signal 输出端口，输出基础几何体与从动几何体的接触点之间的相对切向速度。

当对涉及点云的接触进行建模时，输出为 2-by-*N* 矩阵，其中 *N* 等于点数。数组的每一列等于对应点与另一个几何体上的接触点之间相对速度的 *x* 分量和 *y* 分量。相对速度在对应的接触坐标系中解析。

当对其他类型的几何体之间的接触进行建模时，输出为 2-by-1 数组，等于两个几何体的接触点之间相对速度的 *x* 分量和 *y* 分量。输出在接触坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Sensing** 部分中，选择 **Relative Tangential Velocity**。

#### 力/力矩

### **fn** — 法向力，N physical signal

两个接触几何体之间的法向力的 physical signal 输出端口。该模块在指定解析坐标系的坐标中解析测量值，并且 **Direction** 参数的设置会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处的法向力。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示法向力。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Normal Force**。

### **fnm** — 法向力大小，N physical signal

法向力大小的 physical signal 输出端口。**Direction** 和 **Resolution Frame** 参数不会影响测量值。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列是对应点处的法向力大小。

当对其他类型的几何体之间的接触进行建模时，输出为法向力大小。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Normal Force Magnitude**。

### **tn** — 由法向力产生的力矩，N\*m physical signal

由法向力产生的力矩的 physical signal 输出端口。测量值是法向力与接触点相对于指定解析坐标系的位置向量的叉积。**Direction** 参数会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处由法向力产生的力矩。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示由法向力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Normal Torque**。

### **ffr** — 摩擦力，N physical signal

两个接触几何体之间的摩擦力的 physical signal 输出端口。该模块在指定解析坐标系的坐标中解析测量值，并且 **Direction** 参数的设置会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处的摩擦力。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示摩擦力。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Force**。

### **ffrm** — 摩擦力大小，N physical signal

两个接触几何体之间的摩擦力大小的 physical signal 输出端口。**Direction** 和 **Resolution Frame** 参数不会影响测量值。

当对涉及点云的接触进行建模时，输出为 1-by-*N* 数组，其中 *N* 等于点数。数组的每一列是对应点处的摩擦力大小。

当对其他类型的几何体之间的接触进行建模时，输出为法向接触力大小。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Force Magnitude**。

### **tfr** — 由摩擦力产生的力矩，N\*m physical signal

由摩擦力产生的力矩的 physical signal 输出端口。测量值是摩擦力与接触点相对于指定解析坐标系的位置向量的叉积。**Direction** 参数会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处由摩擦力产生的力矩。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示由摩擦力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Frictional Torque**。

### **ft** — 总接触力，N physical signal

两个接触几何体之间的总接触力的 physical signal 输出端口。总接触力包括法向力和摩擦力。该模块在指定解析坐标系的坐标中解析测量值，并且 **Direction** 参数的设置会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处的总接触力。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示总接触力。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Total Force**。

### **tt** — 由总接触力产生的力矩，N\*m physical signal

由接触力产生的总接触力矩的 physical signal 输出端口。测量值是接触力与接触点相对于指定解析坐标系的位置向量的叉积。**Direction** 参数会影响测量值的符号。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 表示点数。数组的每一列表示一个 3-D 向量，指示对应点处由总接触力产生的接触力矩。

当对其他类型的几何体之间的接触进行建模时，输出表示一个 3-D 向量，指示由总接触力产生的力矩。

#### 依赖关系

要启用此端口，请在 **Force/Torque** 部分中，选择 **Total Torque**。

#### 接触坐标系

### **Rb** — 基础旋转，unitless physical signal

physical signal 端口，输出接触坐标系相对于基础几何体的参考坐标系的旋转矩阵。

当对涉及点云的接触进行建模时，输出为 3-D 数组，其中包含 *N* 个 3-by-3 矩阵，*N* 等于点云中的点数。每个 3-by-3 矩阵是一个旋转矩阵，将对应接触坐标系中的向量映射到基础几何体的参考坐标系中的向量。如果某个点未与另一个几何体接触，则对应矩阵为单位矩阵。

当对其他类型的几何体之间的接触进行建模时，输出为 3-by-3 旋转矩阵，将接触坐标系中的向量映射到基础几何体的参考坐标系中的向量。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Rotation**。

### **pb** — 基础平移，unitless physical signal

physical signal 端口，输出接触点相对于基础几何体的参考坐标系的位置。

当对涉及点云的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 等于点数。数组的每一列指示一个点相对于基础几何体的参考坐标系的坐标。如果某个点未与另一个几何体接触，则坐标为 `[0 0 0]`。

当对其他类型的几何体之间的接触进行建模时，输出为 3-by-1 数组，包含接触点相对于基础几何体的参考坐标系的坐标。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Translation**。

### **Rf** — 从动旋转，unitless physical signal

physical signal 端口，输出接触坐标系相对于从动几何体的参考坐标系的旋转矩阵。

当对涉及点云的接触进行建模时，输出为 3-D 数组，其中包含 *N* 个 3-by-3 矩阵，*N* 等于点云中的点数。每个 3-by-3 矩阵是一个旋转矩阵，将对应接触坐标系中的向量映射到从动几何体的参考坐标系中的向量。如果某个点未与另一个几何体接触，则对应矩阵为单位矩阵。

当对其他类型的几何体之间的接触进行建模时，输出为 3-by-3 旋转矩阵，将接触坐标系中的向量映射到从动几何体的参考坐标系中的向量。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Follower Rotation**。

### **pf** — Follower translation，无量纲物理信号

物理信号端口，输出接触点相对于 follower 几何体参考坐标系的位置。

当对涉及 point cloud 的接触进行建模时，输出为 3-by-*N* 数组，其中 *N* 等于点数。数组的每一列表示一个点相对于 follower 几何体参考坐标系的坐标。如果某个点未与另一几何体接触，则坐标为 `[0 0 0]`。

当对其它类型几何体之间的接触进行建模时，输出为 3-by-1 数组，其中包含接触点相对于 follower 几何体参考坐标系的坐标。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Follower Translation**。

## 参数

### 法向力

### **Method** — 用于指定法向接触力的方法 `Smooth Spring-Damper`（默认）| `Provided by Input`

用于指定法向接触力的方法，指定为 `Smooth Spring-Damper` 或 `Provided by Input`。

选择 `Smooth Spring-Damper` 以使用修改的 spring-damper 方法对法向接触力进行建模，或选择 `Provided by Input` 将自定义力输入为法向接触力。

### **Stiffness** — 接触弹簧对几何穿透的阻力 1e6 `N/m`（默认）| scalar

接触弹簧对几何穿透的阻力，指定为 scalar。spring stiffness 在接触期间为常量。spring stiffness 的值越大，几何体之间的接触越硬。

#### 依赖项

要启用此参数，请在 **法向力** 部分中将 **Method** 设置为 `Smooth Spring-Damper`。

### **Damping** — 几何体穿透期间接触阻尼器对运动的阻力 1e3 `N/(m/s)`（默认）| scalar

几何体穿透期间接触阻尼器对运动的阻力，指定为 scalar。damping coefficient 是一个常量值，表示碰撞几何体损失的能量。damping coefficient 的值越大，几何体碰撞时损失的能量越多，接触振动被阻尼的速度越快。使用值零可对完美弹性碰撞进行建模，这种碰撞守恒能量。

#### 依赖项

要启用此参数，请在 **法向力** 部分中将 **Method** 设置为 `Smooth Spring-Damper`。

### **Transition Region Width** — spring-damper 力升高到其完整值的区域 1e-4 `m`（默认）| scalar

spring-damper 力升高到其完整值的区域，指定为 scalar。区域越小，接触开始越尖锐，求解器所需的时间步长越小。减小 transition region 可提高模型精度，而扩大 transition region 可提高仿真速度。

#### 依赖项

要启用此参数，请在 **法向力** 部分中将 **Method** 设置为 `Smooth Spring-Damper`。

### 摩擦力

### **Method** — 用于指定摩擦力的方法 `Smooth Stick-Slip`（默认）| `None` | `Provided by Input`

用于指定摩擦力的方法，指定为 `Smooth Stick-Slip`、`None` 或 `Provided by Input`。

选择 `None` 可省略摩擦，选择 `Smooth Stick-Slip` 可使用修改的 stick-slip 方法计算摩擦力，或选择 `Provided by Input` 输入自定义摩擦力。

### **Coefficient of Static Friction** — 切向速度接近零时摩擦力大小与法向力大小的比值 0.5（默认）| 非负 scalar

切向速度接近零时摩擦力大小与法向力大小的比值，指定为正 scalar。

该值由接触几何体的材料属性决定。该参数的值通常小于一，尽管对于高摩擦材料，大于一的值也是可能的。在大多数情况下，该值应高于 dynamic friction 系数。

#### 依赖项

要启用此参数，请在 **摩擦力** 部分中将 **Method** 设置为 `Smooth Stick-Slip`。

### **Coefficient of Dynamic Friction** — 切向速度较大时摩擦力大小与法向力大小的比值 0.3（默认）| 非负 scalar

切向速度较大时摩擦力大小与法向力大小的比值，指定为非负 scalar。

该值由接触几何体的材料属性决定。该参数的值通常小于一，尽管对于高摩擦材料，大于一的值也是可能的。在大多数情况下，该值应小于 static friction 系数。

#### 依赖项

要启用此参数，请在 **摩擦力** 部分中将 **Method** 设置为 `Smooth Stick-Slip`。

### **Critical Velocity** — 确定静摩擦系数和动摩擦系数之间混合的速度 1e-3 `m/s`（默认）| scalar

确定静摩擦系数和动摩擦系数之间混合的速度，指定为 scalar。

当 critical velocity 等于切向速度的大小时，有效摩擦系数等于 **Coefficient of Static Friction** 参数的值。当切向速度的大小增加到超过指定的 critical velocity 时，有效摩擦系数渐近地接近 **Coefficient of Dynamic Friction** 参数的值。

#### 依赖项

要启用此参数，请在 **摩擦力** 部分中将 **Method** 设置为 `Smooth Stick-Slip`。

### 感测

#### 力/力矩

### **Direction** — 测量方向 `Base on Follower`（默认）| `Follower on Base`

测量方向，指定为以下值之一：

- `Base on Follower` — 该模块感测 base 几何体施加在 follower 几何体上的力和力矩。
- `Follower on Base` — 该模块感测 follower 几何体施加在 base 几何体上的力和力矩。

该参数仅影响 **力/力矩** 部分下的向量输出。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Contact`（默认）| `Base` | `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Contact` — 该模块在 contact frame 的坐标中解析测量值。
- `Base` — 该模块在 base frame 的坐标中解析测量值。
- `Follower` — 该模块在 follower frame 的坐标中解析测量值。

该参数仅影响 **力/力矩** 部分下的向量输出。

### 过零

### **Detect Contact Start and End** — 将接触的开始和结束检测为过零事件 off（默认）| on

选择此项可将每个接触的开始和结束检测为过零事件。当 separation distance 从正或零变为负，以及从负变为正或零时，会发生过零事件。

## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2025a: 将接触力和力矩作为向量测量，并使用 base、follower 或 contact frame 解析测量值

现在可以将法向、摩擦和总接触力与力矩输出为 3-D 向量。通过使用 **Direction** 参数，可以指定输出表示 base 几何体施加在 follower 几何体上的力和力矩，还是相反。还可以在 base、follower 或 contact frame 的坐标中解析这些向量输出。

### R2023b: 对 point cloud 和 grid surface 使用输入力并测量接触量

现在可以使用输入力对涉及 point cloud 或 grid surface 的接触进行建模，并测量相应的接触量。当其中一个几何体是 point cloud 时，输入力的信号必须是数组，用于指定 cloud 中每个点的力，并且测得的接触量是包含 cloud 中每个点信息的数组。

对于 point cloud 和 grid surface 接触对，Spatial Contact Force 模块支持过零检测。仅当 separation distance 从正或零变为负，以及从负变为正或零时，才会发生过零事件。

### R2023b: 测量两个几何体之间的 penetration depth

测量两个接触几何体之间的 penetration depth。当两个几何体碰撞时，该值等于重叠距离；当几何体未接触时，该值等于零。

### R2023b: **Separation Distance** 参数将被移除

**Separation Distance** 参数将在未来版本中移除。请改用 **Penetration Depth** 参数。

### R2023b: 行为变更 non-scalar 输出

如果编译一个模型，该模型具有一个 Spatial Contact Force 模块，该模块将 non-scalar 信号直接输出到除 PS-Simulink Converter 模块之外的任何 Simscape 模块，则会出现 inconsistent dimensions 错误。

为避免该错误，请使用 PS Signal Specification 模块将 Spatial Contact Force 模块的每个 non-scalar 输出信号与对应的 Simscape 模块连接，并明确指定输出信号的维度。

## 描述

对两个几何体之间的空间接触进行建模

Spatial Contact Force 模块对 3-D 空间中的一对几何体之间的接触进行建模。可以使用内置的 penalty 方法，或提供自定义法向力和摩擦力定律来对接触进行建模。

### 支持的几何体

Spatial Contact Force 模块可以对多种几何体对之间的接触进行建模。可以使用从 Body Elements 子库中的 solid 模块导出的几何体，或 Curves and Surfaces 子库中的 point 和 surface 模块的几何体。

所有导出的几何体都是对应 solid 的凸包表示，即使某些 solid 可能具有凹形。该图显示了 L-shape solid 的真实几何体和凸包表示。

L-shape solid 的真实几何体和凸包表示。

请注意，在计算惯性属性时，solid 模块使用真实几何体。

Spatial Contact Force 模块不会对某些几何体对之间的接触进行建模。此表列出了支持的几何体对。

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Convex Hull of Solid** | **Disk** | **Grid Surface** | **Infinite Plane** | **Point** | **Point Cloud** |
| **Convex Hull of Solid** | Yes | Yes | No | Yes | Yes | Yes |
| **Disk** | Yes | No | No | Yes | No | No |
| **Grid Surface** | No | No | No | No | Yes | Yes |
| **Infinite Plane** | Yes | Yes | No | No | Yes | Yes |
| **Point** | Yes | No | Yes | Yes | No | No |
| **Point Cloud** | Yes | No | Yes | Yes | No | No |

### 接触力

该图显示了 Spatial Contact Force 模块如何对两个 3-D 几何体之间的空间接触问题进行建模。在此情况下，接触发生在蓝色 base 几何体和红色 follower 几何体之间，并且有一个接触点。

在接触期间，每个几何体都有一个 contact frame。这些 contact frame 始终重合，并位于接触点处。contact frame 的 *xy* 平面定义接触平面。contact frame 的 *z* 方向对于 base 几何体是向外的法向量，但对于 follower 几何体是向内的法向量。在连续接触期间，随着接触点移动，contact frame 会围绕几何体移动。

该模块根据牛顿第三定律，在 contact frame 的原点处对几何体施加接触力：

1. 法向力 fn，它与 contact frame 的 *z* 轴对齐。该力将几何体推开，以减少穿透。
2. 摩擦力 ff，它位于接触平面内。该力抵抗几何体之间的相对切向速度。

要指定法向接触力，请在 **Normal Force** 部分中，将 **Method** 参数设置为 `Smooth Spring-Damper` 或 `Provided by Input`。如果选择 `Smooth Spring-Damper`，则法向力为：

fn=s(d,w)⋅(k⋅d+b⋅d'),

其中：

- fn 是以等大反向方式施加到每个接触几何体上的法向力。
- d 是两个接触几何体之间的 penetration depth。
- w 是模块中指定的 transition region width。
- d' 是 penetration depth 的一阶时间导数。
- k 是模块中指定的 normal-force stiffness。
- b 是模块中指定的 normal-force damping。
- s(d,w) 是平滑函数。

力定律在穿透开始时附近被平滑。当 *d* < *w* 时，平滑函数在区间 [0, *w*] 上连续且单调增加。当 *d* = 0 时函数为 0，当 *d* = *w* 时函数为 1，并且该函数在区间端点处对 *d* 的导数为零。

为了更好地检测接触（当 **Transition Region Width** 参数的值很小时），Spatial Contact Force 模块支持可选的过零检测。仅当 separation distance 从正或零变为负，以及从负变为正或零时，才会发生过零事件。

**注意**

Spatial Contact Force 模块的过零检测与其它 Simulink® 模块（例如 From File 和 Integrator）的过零检测不同，因为 Spatial Contact Force 的力方程是连续的。有关 Simulink 模块中过零检测的详细信息，请参阅 Zero-Crossing Detection。

要指定摩擦力，请在 **Frictional Force** 部分中，将 **Method** 参数设置为 `Smooth Stick-Slip`、`Provided by Input` 或 `None`。如果选择 `Smooth Stick-Slip`，则摩擦力始终直接抵抗接触点处相对速度的方向，并通过取决于相对速度大小的摩擦系数与法向力相关：

|ff|=μ⋅|fn|,

其中：

- ff 是摩擦力。
- fn 是法向力。
- μ 是有效摩擦系数。

有效摩擦系数是 **Coefficient of Static Friction**、**Coefficient of Dynamic Friction** 和 **Critical Velocity** 参数的值以及相对切向速度大小的函数。在高相对速度下，有效摩擦系数的值接近 dynamic friction 系数。在 critical velocity 下，有效摩擦系数达到最大值，该值等于 static friction 系数。该图显示了典型情况下 μstatic > μdynamic 的基本关系。在此情况下，模型能够通过在小切向速度附近使用更高的有效摩擦系数来近似 stiction。

有效摩擦系数图

当对涉及 point cloud 的接触进行建模时，Spatial Contact Force 模块计算每个点的接触量，并且输出信号的顺序与 Point Could 模块中指定的点的顺序相同。对于未与另一几何体接触的点，测量值为零。使用输入力时，输入信号的大小和顺序必须与 Point Could 模块中指定的点的大小和顺序匹配。
