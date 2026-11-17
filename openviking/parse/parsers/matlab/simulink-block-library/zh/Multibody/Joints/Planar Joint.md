---
type: simulink-block
title: 'Planar Joint'
family: 'joints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'planarjoint'
documentation_source_path: 'ref/planarjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Planar Joint

## 端口

### 坐标系

### **B** — 基座坐标系 frame

关节模块的基座坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。
### 输入

#### X Prismatic Primitive (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节原语的驱动力。模块沿基座坐标系的 *x* 轴将力等大反向地施加到关节的基座和从动坐标系。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节原语的运动轮廓。模块使用此信号确定从动坐标系相对于基座坐标系沿基座坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Y Prismatic Primitive (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节原语的驱动力。模块沿基座坐标系的 *y* 轴将力等大反向地施加到关节的基座和从动坐标系。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节原语的运动轮廓。模块使用此信号确定从动坐标系相对于基座坐标系沿基座坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Z Revolute Primitive (Rz)

### **tz** — 驱动力矩物理信号

物理信号输入端口，接受关节原语的驱动力矩。模块将力矩等大反向地施加到关节原语的基座和从动坐标系。力矩绕基座坐标系的 *z* 轴。在仿真期间，从动坐标系和基座坐标系的 *z* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`。

### **qz** — 运动轮廓物理信号

物理信号输入端口，接受关节原语的运动轮廓。模块使用此信号确定从动坐标系相对于基座坐标系绕基座坐标系 *z* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

控制关节模式的输入端口。信号必须是量纲一的标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，为分离；当输入信号为 `1` 时，为锁定。您可以在仿真期间的任何时间更改模式。

下表显示了在模式之间转换期间关节位置和速度的变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| 正常到分离 | 关节位置保留当前值，但转换后可以在任何方向上发生变化。 | 关节速度保留当前值，但转换后可以在任何方向上发生变化。 |
| 锁定到正常 | 关节位置保留当前值，但转换后可以在与关节自由度（DOF）对齐的方向上发生变化。 | 关节速度保持为零，但转换后可以在与关节自由度对齐的方向上发生变化。 |
| 锁定到分离 | 关节位置保留当前值，但转换后可以在任何方向上发生变化。 | 关节速度保持为零，但转换后可以在任何方向上发生变化。 |
| 分离到正常 | 对于与关节自由度对齐的方向，关节位置初始采用使用牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节自由度对齐的方向，关节速度初始采用使用牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在转换后保持恒定。 |
| 分离到锁定 | 对于与关节自由度对齐的方向，关节位置初始采用使用牛顿法计算的值，并在转换后保持恒定。在约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### X Prismatic Primitive (Px)

### **px** — 原语位置物理信号

物理信号端口，输出关节原语的位置。该值是沿基座坐标系 *x* 方向从动坐标系相对于基座坐标系的位移。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Position**。

### **vx** — 原语速度物理信号

物理信号端口，输出关节原语的速度。该值是端口 **px** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Velocity**。

### **ax** — 原语加速度物理信号

物理信号端口，输出关节原语的加速度。该值是端口 **px** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Acceleration**。

### **fx** — 作用在关节原语上的执行器力物理信号

物理信号端口，输出作用在关节原语上的执行器力。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Actuator Force**。

### **fllx** — 下限力物理信号

物理信号端口，输出下限力。当关节原语位置小于自由区域的下界时，模块施加此力。模块将力施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

物理信号端口，输出上限力。当关节原语位置超过自由区域的上界时，模块施加此力。模块将力施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选中 **Upper-Limit Force**。

#### Y Prismatic Primitive (Py)

### **py** — 原语位置物理信号

物理信号端口，输出关节原语的位置。该值是沿基座坐标系 *y* 方向从动坐标系相对于基座坐标系的位移。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Position**。

### **vy** — 原语速度物理信号

物理信号端口，输出关节原语的速度。该值是端口 **py** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Velocity**。

### **ay** — 原语加速度物理信号

物理信号端口，输出关节原语的加速度。该值是端口 **py** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Acceleration**。

### **fy** — 作用在关节原语上的执行器力物理信号

物理信号端口，输出作用在关节原语上的执行器力。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Actuator Force**。

### **flly** — 下限力物理信号

物理信号端口，输出下限力。当关节原语位置小于自由区域的下界时，模块施加此力。模块将力施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

物理信号端口，输出上限力。当关节原语位置超过自由区域的上界时，模块施加此力。模块将力施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选中 **Upper-Limit Force**。

#### Z Revolute Primitive (Rz)

### **qz** — 关节原语位置物理信号

物理信号端口，输出关节原语的位置。该值是绕基座坐标系 *z* 轴从动坐标系相对于基座坐标系的旋转角。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Position**。

### **wz** — 关节原语角速度物理信号

物理信号端口，输出关节原语的角速度。该值是端口 **qz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Velocity**。

### **bz** — 关节原语角加速度物理信号

物理信号端口，输出关节原语的角加速度。该值是端口 **qz** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Acceleration**。

### **tz** — 作用在关节原语上的执行器力矩物理信号

物理信号端口，输出作用在关节原语上的执行器力矩。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Actuator Torque**。

### **tllz** — 作用在关节原语上的下限力矩物理信号

物理信号端口，输出下限力矩。当关节原语位置小于自由区域的下界时，模块施加此力矩。模块将力矩施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Lower-Limit Torque**。

### **tulz** — 作用在关节原语上的上限力矩物理信号

物理信号端口，输出上限力矩。当关节原语位置超过自由区域的上界时，模块施加此力矩。模块将力矩施加到关节原语的基座和从动坐标系，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选中 **Upper-Limit Torque**。

#### 复合力/力矩传感

### **fc** — 约束力，N physical signal

物理信号端口，输出作用在关节上的约束力。这些力维持关节的平移约束。输出采用 3×1 向量格式，表示沿求解坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选中 **Constraint Force**。

### **tc** — 约束力矩，N\*m physical signal

物理信号端口，输出作用在关节上的约束力矩。这些力矩维持关节的旋转约束。输出采用 3×1 向量格式，表示绕求解坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选中 **Constraint Torque**。

### **ft** — 总力，N physical signal

物理信号端口，输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力之和。输出采用 3×1 向量格式，表示沿求解坐标系的 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，下图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选中 **Total Force**。

### **tt** — 总力矩，N\*m physical signal

物理信号端口，输出作用在关节上的总力矩。总力矩是通过关节在相连坐标系之间传递的所有力矩之和。力矩包括驱动力矩、内力矩、限位力矩和约束力矩。输出采用 3×1 向量格式，表示绕求解坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选中 **Total Torque**。

## 参数

### X Prismatic Primitive (Px)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选中此参数以指定 *x* 棱柱原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选中 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*x* 棱柱原语的位置目标，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选中 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级级别 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*x* 移动副基元的线速度目标，指定为以线速度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度单位表示的标量。

### **Spring Stiffness** — 力律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力律的刚度，指定为以线性刚度单位表示的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下位置限制 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*x* 移动副基元自由区域的下界，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e6 `N/m`（默认）| 标量

下界处弹簧的刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透达到过渡区域宽度时，模块施加下限力的完整值。区域越小，力的起始越陡峭，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限制 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| 标量

上界处弹簧的刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透达到过渡区域宽度时，模块施加上限力的完整值。区域越小，力的起始越陡峭，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

用于为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fx** 指定 *x* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

用于为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节基元的运动。 |

### Y Prismatic Primitive (Py)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级级别 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*y* 移动副基元的位置目标，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级级别 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*y* 移动副基元的线速度目标，指定为以线速度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度单位表示的标量。

### **Spring Stiffness** — 力律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力律的刚度，指定为以线性刚度单位表示的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下位置限制 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*y* 移动副基元自由区域的下界，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e6 `N/m`（默认）| 标量

下界处弹簧的刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透达到过渡区域宽度时，模块施加下限力的完整值。区域越小，力的起始越陡峭，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限制 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| 标量

上界处弹簧的刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透达到过渡区域宽度时，模块施加上限力的完整值。区域越小，力的起始越陡峭，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

用于为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fy** 指定 *y* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

用于为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **py** 指定关节基元的运动。 |

### Z Revolute Primitive (Rz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转副基元的位置目标。

### **Priority** — 位置目标的优先级级别 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*z* 旋转副基元的位置目标，指定为采用角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转副基元的角速度目标。

### **Priority** — 速度目标的优先级级别 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*z* 旋转副基元的角速度目标，指定为采用角速度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部转矩为零的位置 0 `deg`（默认）| 标量

弹簧转矩为零的位置，指定为采用角度单位的标量。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

*z* 旋转副基元的内部弹簧-阻尼力律的刚度，指定为采用扭转刚度单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*z* 旋转副基元的内部弹簧-阻尼力律的阻尼系数，指定为采用阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下位置限制 `off`（默认）| `on`

选择此参数以指定 *z* 旋转副基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*z* 旋转副基元自由区域的下界，指定为采用角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

下界处弹簧的刚度，指定为采用扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **阻尼系数** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **过渡区域宽度** — 用于平滑弹簧和阻尼扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼扭矩的区域，指定为具有角度单位的标量。

当穿透量达到过渡区域的宽度时，该模块会施加下限扭矩的完整值。该区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **指定上限** — 是否指定上限位置 `off`（默认）| `on`

选择此参数可指定 *z* 旋转基元的运动上限。

### **边界** — 自由区域的上界 90 `deg`（默认）| 标量

*z* 旋转基元的自由区域上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **弹簧刚度** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为具有扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **阻尼系数** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **过渡区域宽度** — 用于平滑弹簧和阻尼扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼扭矩的区域，指定为具有角度单位的标量。

当穿透量达到过渡区域的宽度时，该模块会施加上限扭矩的完整值。该区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

#### 驱动

### **扭矩** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| 扭矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **tz** 指定 *z* 旋转基元的执行器扭矩。 |
| `Automatically Computed` | 该模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **运动** 设置为 `Provided by Input`。自动计算的扭矩可能满足机构中其他位置的运动输入。 |

### **运动** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 该模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qz** 指定 *z* 旋转基元的运动。 |

### 模式配置

### **模式** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | Locked 模式约束关节的所有自由度 (DOFs)。在仿真过程中，锁定的关节以零速度保持其初始装配位置。关节模块可根据 **内部力学**、**限位** 和 **驱动** 参数的设置来感测力或扭矩。 |
| `Normal` | Normal 模式启用关节的 DOFs，并且关节的约束按预期在仿真过程中工作。 |
| `Disengaged` | Disengaged 模式在整个仿真过程中释放关节的所有约束。**内部力学**、**限位** 和 **驱动** 参数的设置不影响已分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您使用输入信号指定关节模式。有关详细信息，请参阅 **输入** 部分中的 **mode** 端口。 |

### 复合力/扭矩传感

### **方向** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 该模块感测从动坐标系施加在基础坐标系上的力和扭矩。
- `Base on Follower` — 该模块感测基础坐标系施加在从动坐标系上的力和扭矩。

此参数仅影响 **复合力/扭矩传感** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅力和扭矩测量方向。

### **解析坐标系** — 用于解析测量值的坐标系 `Base`（默认）| `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 该模块在基础坐标系的坐标中解析测量值。
- `Follower` — 该模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **复合力/扭矩传感** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：对模式故障建模

现在，您可以为所有关节模块对模式故障建模。使用这些故障，您可以在仿真过程中更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有一个旋转自由度和两个平移自由度的关节

Planar Joint 模块在两个坐标系之间提供一个旋转自由度和两个平移自由度。

沿基础坐标系的 x 轴和 y 轴的两个平移自由度，以及绕从动坐标系 z 轴的一个旋转自由度

该模块将从动坐标系的原点约束到基础坐标系的 *x-y* 平面，并且从动坐标系的相对变换遵循以下顺序：

变换顺序，显示 Px、Py 和 Rz 变换

首先，从动坐标系分别沿基础坐标系的 *x* 轴和 *y* 轴移动，然后绕平移后生成的从动坐标系的 *z* 轴旋转。

要为关节基元指定初始状态的目标，请使用 **状态目标** 下的参数。这些目标在基础坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将确定先满足哪些目标以及满足的接近程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元对阻尼和弹簧行为进行建模，请使用 **内部力学** 下的参数。使用 **阻尼系数** 参数对能量耗散进行建模，使用 **弹簧刚度** 参数对能量存储进行建模。关节弹簧尝试使关节基元偏离其平衡位置，而关节阻尼器充当能量耗散元件。弹簧和阻尼器严格线性。

要指定关节基元的限位，请使用 **限位** 下的参数。下界和上界定义自由区域的宽度。当位置超出边界时，该模块会施加力，使关节位置加速回到自由区域。该模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**驱动** 部分中的 **力**、**扭矩** 和 **运动** 参数控制仿真过程中关节基元的运动。有关详细信息，请参阅指定关节驱动输入。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅传感以及力和扭矩传感。

要指定关节模式配置，请使用 **模式** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **模式配置**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **模式** 参数设置为 `Locked`，并且 **故障行为** 参数设置为 `Disengaged`，则关节变为分离状态。

要向关节模块添加模式故障，请单击该关节模块，在 **Simscape Block** 选项卡和 **故障** 部分中，单击 **故障** > `Add Fault`。或者，您可以单击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后单击模块图标上的 Add a fault 按钮以添加故障。您可以将多个故障添加到一个关节模块，但该关节模块在仿真期间只能有一个活动故障。

添加故障时，在属性检查器中的 **故障** 部分下，指定故障的行为和触发类型。要定义故障行为，请单击 **故障行为** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅设置故障触发器。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用故障表。有关更多详细信息，请参阅访问故障表和故障仪表板。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **故障** 部分中，打开 **故障仿真** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真处于打开状态。仿真会记录触发状态数据。要查看数据，请使用仿真数据检查器。此外，您可以在故障仪表板中查看故障状态和已触发故障的摘要。要打开故障仪表板，请在 **Simscape Block** 选项卡中，单击 **故障** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
