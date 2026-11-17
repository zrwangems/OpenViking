---
type: simulink-block
title: 'Universal Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'universaljoint'
documentation_source_path: 'ref/universaljoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Universal Joint

## 端口

### 坐标系

### **B** — 基础坐标系 坐标系

关节模块的基础坐标系。

### **F** — 从动坐标系 坐标系

关节模块的从动坐标系。
### 输入

#### X 旋转基元 (Rx)

### **tx** — 驱动力矩 物理信号

物理信号输入端口，接受关节基元的驱动力矩。该模块将此力矩等值反向地施加到关节基元的基础坐标系和从动坐标系上。该力矩绕基础坐标系的 *x* 轴。在仿真过程中，从动坐标系和基础坐标系的 *x* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **X 旋转基元 (Rx)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input`。

### **qx** — 运动轮廓 物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号来确定从动坐标系相对于基础坐标系绕基础坐标系 *x* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **X 旋转基元 (Rx)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Y 旋转基元 (Ry)

### **ty** — 驱动力矩 物理信号

物理信号输入端口，接受关节基元的驱动力矩。该模块将此力矩等值反向地施加到关节基元的基础坐标系和从动坐标系上。该力矩绕基础坐标系的 *y* 轴。在仿真过程中，从动坐标系和基础坐标系的 *y* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **Y 旋转基元 (Ry)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input`。

### **qy** — 运动轮廓 物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号来确定从动坐标系相对于基础坐标系绕基础坐标系 *y* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Y 旋转基元 (Ry)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。你可以在仿真过程中的任意时刻更改模式。

下表显示了在模式之间切换时，关节的位置和速度如何变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保留当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| 正常到分离 | 关节位置保留当前值，但切换后可以沿任意方向变化。 | 关节速度保留当前值，但切换后可以沿任意方向变化。 |
| 锁定到正常 | 关节位置保留当前值，但切换后可以沿与关节自由度（DOF）对齐的方向变化。 | 关节速度保持为零，但切换后可以沿与关节 DOF 对齐的方向变化。 |
| 锁定到分离 | 关节位置保留当前值，但切换后可以沿任意方向变化。 | 关节速度保持为零，但切换后可以沿任意方向变化。 |
| 分离到正常 | 对于与关节 DOF 对齐的方向，关节位置最初取通过使用牛顿法计算得到的值，此后可以变化。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节 DOF 对齐的方向，关节速度最初取通过使用牛顿法计算得到的值，此后可以变化。在受约束方向上，关节速度变为零，并在切换后保持不变。 |
| 分离到锁定 | 对于与关节 DOF 对齐的方向，关节位置最初取通过使用牛顿法计算得到的值，并在切换后保持不变。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### X Revolute Primitive (Rx)

### **qx** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是跟随坐标系相对于基础坐标系绕基础坐标系 *x* 轴的旋转角度。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Position**。

### **wx** — 关节基元角速度物理信号

输出关节基元角速度的物理信号端口。该值是端口 **qx** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 关节基元角加速度物理信号

输出关节基元角加速度的物理信号端口。该值是端口 **qx** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Acceleration**。

### **tx** — 作用在关节基元上的执行器扭矩物理信号

输出作用在关节基元上的执行器扭矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Actuator Torque**。

### **tllx** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X 转动基元 (Rx)** > **传感** 下，选择 **下限力矩**。

### **tulx** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X 转动基元 (Rx)** > **传感** 下，选择 **上限力矩**。

#### Y 转动基元 (Ry)

### **qy** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基座坐标系绕基座坐标系 *y* 轴的旋转角度。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **位置**。

### **wy** — 关节基元角速度物理信号

输出关节基元角速度的物理信号端口。该值是端口 **qy** 输出信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **速度**。

### **by** — 关节基元角加速度物理信号

输出关节基元角加速度的物理信号端口。该值是端口 **qy** 输出信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **加速度**。

### **ty** — 作用在关节基元上的执行器力矩物理信号

输出作用在关节基元上的执行器力矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **执行器力矩**。

### **tlly** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **下限力矩**。

### **tuly** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **上限力矩**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。
这些力维持关节的平移约束。输出为
3×1 向量格式，表示沿
解算坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅力与力矩传感。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的约束力矩。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

物理信号端口，输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力的总和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，下图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的总力矩。总力矩是通过关节在相连坐标系之间传递的所有力矩的总和。力矩包括驱动力矩、内力矩、极限力矩和约束力矩。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下选择 **Total Torque**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### X Revolute Primitive (Rx)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 旋转基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*x* 旋转基元的位置目标，指定为带角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 旋转基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*x* 旋转基元的角速度目标，指定为带角速度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| 标量

弹簧力矩为零的位置，指定为带角度单位的标量。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

*x* 转动基元内部弹簧-阻尼力律的刚度，指定为带扭转刚度单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*x* 转动基元内部弹簧-阻尼力律的阻尼系数，指定为带阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*x* 转动基元自由区域的下界，指定为带角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

下界处的弹簧刚度，指定为带扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为带阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为带角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加下限力矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| 标量

*x* 转动基元自由区域的上界，指定为带角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为带扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为带阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为带角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加上限力矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| 扭矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **tx** 为 *x* 旋转基元指定执行器扭矩。 |
| `Automatically Computed` | 模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的扭矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **qx** 为 *x* 旋转基元指定运动。 |

### Y Revolute Primitive (Ry)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 旋转基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*y* 旋转基元的位置目标，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 旋转基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*y* 旋转基元的角速度目标，指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部扭矩为零的位置 0 `deg`（默认）| 标量

弹簧扭矩为零的位置，指定为具有角度单位的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认）| 标量

*y* 旋转基元的内部弹簧-阻尼力定律的刚度，指定为具有扭转刚度单位的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*y* 旋转基元的内部弹簧-阻尼力定律的阻尼系数，指定为具有阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *y* 旋转基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*y* 旋转基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

下界处的弹簧刚度，指定为具有扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当侵入量达到过渡区域的宽度时，该模块施加下极限扭矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置极限 `off`（默认）| `on`

选择此参数以指定 *y* 旋转基元的上极限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| 标量

*y* 旋转基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为具有扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当侵入量达到过渡区域的宽度时，该模块施加上极限扭矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| 扭矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **ty** 为 *y* 旋转基元指定执行器扭矩。 |
| `Automatically Computed` | 该模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的扭矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qy** 为 *y* 旋转基元指定运动。 |

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | 正常模式启用自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您使用输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩感测

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base`（默认）| `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模型模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

允许在不共轴轴之间传递旋转运动的关节

万向节模块对两个旋转轴之间的联轴器进行建模。这两个轴与基座坐标系和从动坐标系的 *z* 轴对齐，并以相同的平均角速度旋转。但是，如果两轴不共轴，则两轴的相对速度会波动。波动随弯曲角的增大而增大。该关节约束两个坐标系的原点使其重合。

该关节具有两个旋转基元，表示两次连续旋转。这些旋转指定了从动坐标系相对于基座坐标系的姿态。第一次旋转绕从动坐标系的 *x* 轴进行，第二次旋转绕第一次旋转后生成的从动坐标系的 *y* 轴进行，如下图所示。

变换序列示意图

要指定关节基元初始状态的目标，请使用 **State Targets** 下的参数。目标在基座坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定首先满足哪些目标以及满足的程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要对关节基元的阻尼和弹簧行为进行建模，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数对能量耗散进行建模，使用 **Spring Stiffness** 参数对能量存储进行建模。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器则充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限值，请使用 **Limits** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡中的 **Faults** 部分，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
