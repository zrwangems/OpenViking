---
type: simulink-block
title: 'Planar Joint'
family: 'sm'
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

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 随动坐标系 frame

关节模块的随动坐标系。
### 输入

#### X 移动副基元 (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *x* 轴将力等大反向地施加到关节的基础坐标系和随动坐标系上。

#### 依赖

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定随动坐标系相对于基础坐标系沿基础坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Y 移动副基元 (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *y* 轴将力等大反向地施加到关节的基础坐标系和随动坐标系上。

#### 依赖

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定随动坐标系相对于基础坐标系沿基础坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Z 转动副基元 (Rz)

### **tz** — 驱动力矩物理信号

物理信号输入端口，接受关节基元的驱动力矩。该模块将力矩等大反向地施加到关节基元的基础坐标系和随动坐标系上。力矩绕基础坐标系的 *z* 轴。随动坐标系和基础坐标系的 *z* 轴在仿真期间彼此对齐。

#### 依赖

要启用此端口，请在 **Z 转动副基元 (Rz)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input`。

### **qz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定随动坐标系相对于基础坐标系绕基础坐标系 *z* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **Z 转动副基元 (Rz)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。你可以在仿真过程中的任意时刻更改模式。

下表显示了在模式之间切换时，关节的位置和速度如何变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保留当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| 正常到分离 | 关节位置保留当前值，但在切换后可以沿任意方向变化。 | 关节速度保留当前值，但在切换后可以沿任意方向变化。 |
| 锁定到正常 | 关节位置保留当前值，但在切换后可以沿与关节自由度（DOF）对齐的方向变化。 | 关节速度保持为零，但在切换后可以沿与关节自由度对齐的方向变化。 |
| 锁定到分离 | 关节位置保留当前值，但在切换后可以沿任意方向变化。 | 关节速度保持为零，但在切换后可以沿任意方向变化。 |
| 分离到正常 | 对于与关节自由度对齐的方向，关节位置最初取通过牛顿法计算得到的值，此后可以变化。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节自由度对齐的方向，关节速度最初取通过牛顿法计算得到的值，此后可以变化。在受约束方向上，关节速度变为零，并在切换后保持不变。 |
| 分离到锁定 | 对于与关节自由度对齐的方向，关节位置最初取通过牛顿法计算得到的值，并在切换后保持不变。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### X Prismatic Primitive (Px)

### **px** — 基元物理信号的位置

输出关节基元位置的物理信号端口。该值是跟随坐标系相对于基础坐标系沿基础坐标系 *x* 方向的位移。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Position**。

### **vx** — 基元物理信号的速度

输出关节基元速度的物理信号端口。该值是端口 **px** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Velocity**。

### **ax** — 基元物理信号的加速度

输出关节基元加速度的物理信号端口。该值是端口 **px** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Acceleration**。

### **fx** — 作用在关节基元上的执行器力物理信号

输出作用在关节基元上的执行器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Actuator Force**。

### **fllx** — 下限力物理信号

输出下限力的物理信号端口。当关节原始位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节原始的基础坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖项

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

输出上限力的物理信号端口。当关节原始位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节原始的基础坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖项

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Y Prismatic Primitive (Py)

### **py** — 原始位置物理信号

输出关节原始位置的物理信号端口。该值是从动坐标系相对于基础坐标系在基础坐标系 *y* 方向上的位移。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Position**。

### **vy** — 原始速度物理信号

输出关节原始速度的物理信号端口。该值是端口 **py** 信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Velocity**。

### **ay** — 原始加速度物理信号

输出关节原始加速度的物理信号端口。该值是端口 **py** 信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Acceleration**。

### **fy** — 作用在关节原始上的执行器力物理信号

输出作用在关节原始上的执行器力的物理信号端口。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Actuator Force**。

### **flly** — 下限力物理信号

输出下限力的物理信号端口。当关节原始位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节原始的基础坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

输出上限力的物理信号端口。当关节原始位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节原始的基础坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖项

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Z Revolute Primitive (Rz)

### **qz** — 关节原始位置物理信号

输出关节原始位置的物理信号端口。该值是从动坐标系相对于基础坐标系绕基础坐标系 *z* 轴的旋转角度。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Position**。

### **wz** — 关节原始角速度物理信号

输出关节原始角速度的物理信号端口。该值是端口 **qz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Velocity**。

### **bz** — 关节基元的角加速度物理信号

输出关节基元角加速度的物理信号端口。
该值是来自端口 **qz** 的信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Acceleration**。

### **tz** — 作用在关节基元上的执行器扭矩物理信号

输出作用在关节基元上的执行器扭矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Actuator Torque**。

### **tllz** — 作用在关节基元上的下限扭矩物理信号

输出下限扭矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块会施加此扭矩。该模块将此扭矩施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Lower-Limit Torque**。

### **tulz** — 作用在关节基元上的上限扭矩物理信号

输出上限扭矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块会施加此扭矩。该模块将此扭矩施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/扭矩感测

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出采用 3×1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束扭矩，N\*m 物理信号

输出作用在关节上的约束扭矩的物理信号端口。这些扭矩维持关节的旋转约束。输出采用 3×1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连坐标系之间传递的所有力的总和。输出采用 3×1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总扭矩，N\*m 物理信号

输出作用在关节上的总扭矩的物理信号端口。总扭矩是通过关节在相连坐标系之间传递的所有扭矩之和。该扭矩包括驱动扭矩、内部扭矩、限位扭矩和约束扭矩。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅力与扭矩传感。

#### 依赖关系

要启用此端口，请在 **复合力/扭矩传感** 下选择 **总扭矩**。

## 参数

### X 移动副基元 (Px)

#### 状态目标

### **指定位置目标** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的位置目标。

### **优先级** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅多体装配工作原理中的引导装配部分。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **值** — 位置目标 0 `m`（默认）| 标量

*x* 移动副基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **指定速度目标** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的线速度目标。

### **优先级** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅多体装配工作原理中的引导装配部分。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

### **值** — 速度目标 0 `m/s`（默认）| 标量

*x* 移动副基元的线速度目标，指定为以线速度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

#### 内部力学

### **平衡位置** — 内部力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度单位为单位的标量。

### **弹簧刚度** — 力律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力律的刚度，指定为以线性刚度单位为单位的标量。

### **阻尼系数** — 力律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 限位

### **指定下限** — 是否指定下限位置限位 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的下限。

### **边界** — 自由区域的下界 -1 `m`（默认）| 标量

*x* 移动副基元的自由区域的下界，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **弹簧刚度** — 下限处弹簧的刚度 1e6 `N/m`（默认）| 标量

下限处弹簧的刚度，指定为以线性刚度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **阻尼系数** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下限处的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *x* 移动副原语的上限。

### **Bound** — 自由区域的上限 1 `m`（默认）| 标量

关节原语自由区域的上限，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处的弹簧刚度 1e6 `N/m`（默认）| 标量

上限处的弹簧刚度，指定为以线性刚度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上限处的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加上限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### Actuation

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节原语提供致动力的选项，指定为以下值之一：

| Force Setting | Description |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fx** 指定 *x* 移动副原语的致动力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节原语提供运动的选项，指定为以下值之一：

| Motion Setting | Description |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节原语运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节原语的运动。 |

### Y Prismatic Primitive (Py)

#### State Targets

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*y* 移动副基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*y* 移动副基元的线速度目标，指定为以线速度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内力为零时的位置 0 `m`（默认）| 标量

弹簧力为零时的位置，指定为以长度单位为单位的标量。

### **Spring Stiffness** — 力律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力律的刚度，指定为以线性刚度单位为单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 限位

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*y* 移动副基元自由区域的下界，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处的弹簧刚度 1e6 `N/m`（默认）| 标量

下限处的弹簧刚度，指定为以线性刚度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下限处的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透深度达到过渡区域的宽度时，模块施加下限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节原语的自由区域上界，以长度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| 标量

上界处的弹簧刚度，以线性刚度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，以线性阻尼系数单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，以长度单位指定为标量。

当穿透深度达到过渡区域的宽度时，模块施加完整的上限力值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节原语提供致动力的选项，指定为以下值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fy** 为 *y* 移动原语指定致动力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节原语提供运动的选项，指定为以下值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节原语运动。 |
| `Provided by Input` | 输入端口 **py** 为关节原语指定运动。 |

### Z Revolute Primitive (Rz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*z* 旋转原语的位置目标，以角度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转原语的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High
(desired)` 或 `Low (approximate)`。有关
更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity
Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*z* 转动基元的角度速度目标，
指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity
Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| 标量

弹簧力矩为零的位置，指定为具有角度单位的标量。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

*z* 转动基元的内部弹簧-阻尼力律的
刚度，指定为具有扭转刚度单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*z* 转动基元的内部弹簧-阻尼力律的
阻尼系数，指定为具有阻尼
系数单位的标量。

#### 限值

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的
下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*z* 转动基元的自由区域的
下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower
Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

下界处的弹簧刚度，指定为具有扭转刚度单位的
标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower
Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有阻尼系数单位的
标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower
Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为具有
角度单位的标量。

当穿透达到过渡区域的宽度时，该模块施加下限力矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower
Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的
上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| 标量

*z* 转动基元的自由区域的
上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper
Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为具有扭转刚度单位的
标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper
Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为具有阻尼系数单位的
标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper
Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为带角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加完整的上限力矩值。区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力矩的选项，指定为以下值之一：

| 力矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器力矩。 |
| `Provided by Input` | 输入端口 **tz** 指定 *z* 旋转基元的执行器力矩。 |
| `Automatically Computed` | 模块自动计算力矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力矩可能满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qz** 指定 *z* 旋转基元的运动。 |

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参见 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩感测

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块感测基坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参见 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 该模块在基座坐标系的坐标中解析测量值。
- `Follower` — 该模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a: 模式故障建模

现在您可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

具有一个旋转和两个平移自由度的关节

Planar Joint 模块在两个坐标系之间提供一个旋转和两个平移自由度。

沿基座坐标系的 x 轴和 y 轴的两个平移自由度，以及绕从动坐标系 z 轴的一个旋转自由度

该模块将从动坐标系的原点约束到基座坐标系的 *x-y* 平面，从动坐标系的相对变换遵循以下顺序：

变换顺序，显示 Px、Py 和 Rz 变换

首先，从动坐标系分别沿基座坐标系的 *x* 轴和 *y* 轴移动，然后绕平移后生成的从动坐标系的 *z* 轴旋转。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。目标在基座坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定先满足哪些目标以及满足的程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数建模能量耗散，使用 **Spring Stiffness** 参数建模能量存储。关节弹簧试图将关节基元从其平衡位置移开，关节阻尼器充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限位，请使用 **Limits** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing 和 Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击用于添加故障的“Add a fault on the block”图标按钮。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在属性检查器的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡的 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
