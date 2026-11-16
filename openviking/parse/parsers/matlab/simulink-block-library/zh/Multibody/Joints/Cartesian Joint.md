---
type: simulink-block
title: 'Cartesian Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'cartesianjoint'
documentation_source_path: 'ref/cartesianjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Cartesian Joint

## 端口

### 坐标系

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。

### 输入

#### X 平移基元 (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *x* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **驱动** 下，将 **Force** 设置为 `Provided by Input`。

### **px** — 运动配置文件物理信号

物理信号输入端口，接受关节基元的运动配置文件。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **驱动** 下，将 **Motion** 设置为 `Provided by Input`。

#### Y 平移基元 (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *y* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **驱动** 下，将 **Force** 设置为 `Provided by Input`。

### **py** — 运动配置文件物理信号

物理信号输入端口，接受关节基元的运动配置文件。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **驱动** 下，将 **Motion** 设置为 `Provided by Input`。

#### Z 平移基元 (Pz)

### **fz** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *z* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **驱动** 下，将 **Force** 设置为 `Provided by Input`。

### **pz** — 运动配置文件物理信号

物理信号输入端口，接受关节基元的运动配置文件。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **驱动** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

输入端口，控制关节的模式。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。您可以在仿真期间的任何时间更改模式。

下表显示了在模式之间转换期间关节的位置和速度如何变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal to Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal to Disengaged | 关节位置保留当前值，但在转换后可以在任意方向上变化。 | 关节速度保留当前值，但在转换后可以在任意方向上变化。 |
| Locked to Normal | 关节位置保留当前值，但在转换后可以在与关节自由度 (DOFs) 对齐的方向上变化。 | 关节速度保持为零，但在转换后可以在与关节 DOFs 对齐的方向上变化。 |
| Locked to Disengaged | 关节位置保留当前值，但在转换后可以在任意方向上变化。 | 关节速度保持为零，但在转换后可以在任意方向上变化。 |
| Disengaged to Normal | 对于与关节 DOFs 对齐的方向，关节位置最初采用通过牛顿法计算的值，此后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOFs 对齐的方向，关节速度最初采用通过牛顿法计算的值，此后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged to Locked | 对于与关节 DOFs 对齐的方向，关节位置最初采用通过牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖项

要启用此端口，请在 **模式配置** 下，将 **Mode** 设置为 `Provided by Input`。

### 输出

#### X 平移基元 (Px)

### **px** — 基元位置物理信号

物理信号端口，输出关节基元的位置。该值为从动坐标系相对于基础坐标系沿基础坐标系 *x* 方向的位移。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Position**。

### **vx** — 基元速度物理信号

物理信号端口，输出关节基元的速度。该值为端口 **px** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Velocity**。

### **ax** — 基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值为端口 **px** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Acceleration**。

### **fx** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Actuator Force**。

### **fllx** — 下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **X 平移基元 (Px)** > **感测** 下，选择 **Upper-Limit Force**。

#### Y 平移基元 (Py)

### **py** — 基元位置物理信号

物理信号端口，输出关节基元的位置。该值为从动坐标系相对于基础坐标系沿基础坐标系 *y* 方向的位移。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Position**。

### **vy** — 基元速度物理信号

物理信号端口，输出关节基元的速度。该值为端口 **py** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Velocity**。

### **ay** — 基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值为端口 **py** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Acceleration**。

### **fy** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Actuator Force**。

### **flly** — 下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Y 平移基元 (Py)** > **感测** 下，选择 **Upper-Limit Force**。

#### Z 平移基元 (Pz)

### **pz** — 关节基元位置物理信号

物理信号端口，输出关节基元的位置。该值为从动坐标系相对于基础坐标系沿基础坐标系 *z* 轴的位移。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Position**。

### **vz** — 关节基元速度物理信号

物理信号端口，输出关节基元的速度。该值为端口 **pz** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Velocity**。

### **az** — 关节基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值为端口 **pz** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Acceleration**。

### **fz** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节基元上的下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节基元上的上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Z 平移基元 (Pz)** > **感测** 下，选择 **Upper-Limit Force**。

#### 复合力/力矩感测

### **fc** — 约束力，N 物理信号

物理信号端口，输出跨关节作用的约束力。这些力维持关节的平移约束。输出采用 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

物理信号端口，输出跨关节作用的约束力矩。这些力矩维持关节的旋转约束。输出采用 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

物理信号端口，输出跨关节作用的总力。总力是通过关节在连接的坐标系之间传递的所有力之和。输出采用 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，下图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

物理信号端口，输出跨关节作用的总力矩。总力矩是通过关节在连接的坐标系之间传递的所有力矩之和。该力矩包括驱动、内力、极限和约束力矩。输出采用 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Total Torque**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### X 平移基元 (Px)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off` (默认) | `on`

选择此参数可指定 *x* 平移基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)` (默认) | `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m` (默认) | 标量

*x* 平移基元的位置目标，指定为采用长度单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线性速度目标 `off`（默认）| `on`

选择此参数可指定 *x* 移动副基元的线性速度目标。

### **Priority** — 线性速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

用于 *x* 移动副基元的线性速度目标，指定为线性速度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内力为零时的位置 0 `m`（默认）| 标量

弹簧力为零时的位置，指定为长度单位下的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为线性刚度单位下的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数可指定 *x* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*x* 移动副基元自由区域的下界，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认）| 标量

下界处的弹簧刚度，指定为线性刚度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的标量。

当穿透量达到过渡区域宽度时，模块会施加下限力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数可指定 *x* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| 标量

上界处的弹簧刚度，指定为线性刚度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的标量。

当穿透量达到过渡区域宽度时，模块会施加上限力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为下列值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fx** 指定 *x* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为下列值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块基于模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节基元的运动。 |

### Y 移动副基元 (Py)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数可指定 *y* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*y* 移动副基元的位置目标，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线性速度目标 `off`（默认）| `on`

选择此参数可指定 *y* 移动副基元的线性速度目标。

### **Priority** — 线性速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

用于 *y* 移动副基元的线性速度目标，指定为线性速度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内力为零时的位置 0 `m`（默认）| 标量

弹簧力为零时的位置，指定为长度单位下的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为线性刚度单位下的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数可指定 *y* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*y* 移动副基元自由区域的下界，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认）| 标量

下界处的弹簧刚度，指定为线性刚度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的标量。

当穿透量达到过渡区域宽度时，模块会施加下限力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数可指定 *y* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| 标量

上界处的弹簧刚度，指定为线性刚度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的标量。

当穿透量达到过渡区域宽度时，模块会施加上限力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为下列值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fy** 指定 *y* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为下列值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块基于模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **py** 指定关节基元的运动。 |

### Z 移动副基元 (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数可指定 *z* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*z* 移动副基元的位置目标，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线性速度目标 `off`（默认）| `on`

选择此参数可指定 *z* 移动副基元的线性速度目标。

### **Priority** — 线性速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

用于 *z* 移动副基元的线性速度目标，指定为线性速度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内力为零时的位置 0 `m`（默认）| 标量

弹簧力为零时的位置，指定为长度单位下的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为线性刚度单位下的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为线性阻尼系数单位下的标量。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数可指定 *z* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*z* 移动副基元自由区域的下界，指定为长度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认）| 标量

下界处的弹簧刚度，指定为线性刚度单位下的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

下界处的阻尼系数，指定为线性阻尼系数单位下的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的 scalar。

当穿透达到过渡区域的宽度时，模块应用下限力的完整值。区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数可指定 *z* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| scalar

关节基元的自由区域的上界，指定为长度单位下的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| scalar

上界处的弹簧刚度，指定为线性刚度单位下的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

上界处的阻尼系数，指定为线性阻尼系数单位下的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，指定为长度单位下的 scalar。

当穿透达到过渡区域的宽度时，模块应用上限力的完整值。区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### Actuation

### **Force** — 提供致动器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

提供关节基元的致动器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无致动器力。 |
| `Provided by Input` | 输入端口 **fz** 指定 *z* 移动副基元的致动器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节基元运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块基于模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **pz** 指定关节基元的运动。 |

### Mode Configuration

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度 (DOFs)。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | 正常模式启用自由度，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 分离模式在整个仿真期间释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不会影响分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您使用输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### Composite Force/Torque Sensing

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测 follower 坐标系施加在 base 坐标系上的力和力矩。
- `Base on Follower` — 模块感测 base 坐标系施加在 follower 坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在 base 坐标系的坐标中解析测量值。
- `Follower` — 模块在 follower 坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障建模

现在，您可以为所有关节模块对模式故障进行建模。使用这些故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

带三个移动副基元的关节

Cartesian Joint 模块对具有三个平移自由度的关节进行建模。该关节使 follower 坐标系能够通过三个正交平移的序列相对于 base 坐标系执行空间变换。图中显示了在给定仿真时间步长下关节变换发生的顺序。

Cartesian Joint 的关节变换序列

follower 坐标系的轴与 base 坐标系的对应轴平行。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。目标在 base 坐标系中指定。您还可以为目标设置优先级。如果关节无法满足所有状态目标，优先级将确定先满足哪些目标以及满足的程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元对阻尼和弹簧行为进行建模，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数对能量耗散进行建模，使用 **Spring Stiffness** 参数对能量存储进行建模。关节弹簧尝试使关节基元从其平衡位置位移，关节阻尼器用作能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限值，请使用 **Limits** 下的参数。下界和上界定义自由区域的宽度。当位置超出边界时，模块施加力以将关节位置加速回自由区域。模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出感测数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing 和 Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **Mode Configuration**。

### Faults

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要为关节模块添加模式故障，请单击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，单击 **Fault** > `Add Fault`。或者，您可以单击关节模块，悬停在省略号上以打开操作栏，然后单击 Add a fault on the block icon 按钮以添加故障。您可以为关节模块添加多个故障，但关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中，在 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请单击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，单击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls and Simscape Faults Interface 的函数部分。
