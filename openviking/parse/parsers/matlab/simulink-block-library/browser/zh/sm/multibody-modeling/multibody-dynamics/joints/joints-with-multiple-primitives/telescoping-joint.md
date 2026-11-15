---
type: simulink-block
title: 'Telescoping Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Joints / Joints with Multiple Primitives'
documentation_page: 'telescopingjoint'
documentation_source_path: 'ref/telescopingjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Telescoping Joint

## 端口

### 坐标系

### **B** — 基座坐标系 frame

关节模块的基座坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。
### 输入

#### Spherical Primitive (S)

### **tx** — 绕解算坐标系 *x* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示绕解算坐标系 *x* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (X)**。

### **ty** — 绕解算坐标系 *y* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示绕解算坐标系 *y* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Y)**。

### **tz** — 绕解算坐标系 *z* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示绕解算坐标系 *z* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Z)**。

### **t** — 驱动力矩向量 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该向量表示要在基座坐标系和从动坐标系之间施加的、以解算坐标系表示的驱动力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`，并选择 **Torque (XYZ)**。

#### Z Prismatic Primitive (Pz)

### **fz** — 驱动力 物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基座坐标系的 *z* 轴将此力等大反向地施加到关节的基座坐标系和从动坐标系。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **pz** — 运动配置文件 物理信号

物理信号输入端口，接受关节基元的运动配置文件。该模块使用此信号确定从动坐标系相对于基座坐标系沿基座坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制 物理信号

用于控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。您可以在仿真期间随时更改模式。

下表显示了模式转换期间关节位置和速度的变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal to Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal to Disengaged | 关节位置保留当前值，但转换后可以向任意方向变化。 | 关节速度保留当前值，但转换后可以向任意方向变化。 |
| Locked to Normal | 关节位置保留当前值，但转换后可以沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但转换后可以沿与关节自由度 (DOFs) 对齐的方向变化。 |
| Locked to Disengaged | 关节位置保留当前值，但转换后可以向任意方向变化。 | 关节速度保持为零，但转换后可以向任意方向变化。 |
| Disengaged to Normal | 对于与关节自由度 (DOFs) 对齐的方向，关节位置最初采用由牛顿法计算的值，此后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节自由度 (DOFs) 对齐的方向，关节速度最初采用由牛顿法计算的值，此后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged to Locked | 对于与关节自由度 (DOFs) 对齐的方向，关节位置最初采用由牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### Spherical Primitive (S)

### **Q** — 四元数参数化中的相对方向 物理信号

从动坐标系相对于基座坐标系的方向，以单位四元数返回。有关详细信息，请参阅 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 `x` 坐标 物理信号

相对角速度的 *x* 坐标，以标量返回。该值在解算坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 `y` 坐标 物理信号

相对角速度的 *y* 坐标，以标量返回。该值在解算坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 `z` 坐标 物理信号

相对角速度的 *z* 坐标，以标量返回。该值在解算坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度向量 物理信号

相对角速度，以在解算坐标系中表示的 3 维向量返回。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 相对角加速度的 `x` 坐标 物理信号

相对角加速度的 *x* 坐标，以标量返回。该量等于从端口 **wx** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (X)**。

### **by** — 相对角加速度的 `y` 坐标 物理信号

相对角加速度的 *y* 坐标，以标量返回。该量等于从端口 **wy** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Y)**。

### **bz** — 相对角加速度的 `z` 坐标 物理信号

相对角加速度的 *z* 坐标，以标量返回。该量等于从端口 **wz** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Z)**。

### **b** — 角加速度向量 物理信号

相对角加速度，以在解算坐标系中表示的 3 维向量返回。该量等于从端口 **w** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration**。

### **tll** — 下限力矩大小 物理信号

物理信号端口，输出下限力矩的大小。当两个坐标系的 *z* 轴之间的夹角小于下限边界时，模块施加下限力矩。该力矩施加到球面基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Signed Lower-Limit Torque Magnitude**。

### **tul** — 上限力矩大小 物理信号

物理信号端口，输出上限力矩的大小。当两个坐标系的 *z* 轴之间的夹角超过上限边界时，模块施加上限力矩。该力矩施加到球面基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### Z Prismatic Primitive (Pz)

### **pz** — 关节基元位置 物理信号

物理信号端口，输出关节基元的位置。该值为从动坐标系相对于基座坐标系在基座坐标系 *z* 轴中的位移。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **vz** — 关节基元速度 物理信号

物理信号端口，输出关节基元的速度。该值为从端口 **pz** 导出的信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **az** — 关节基元加速度 物理信号

物理信号端口，输出关节基元的加速度。该值为从端口 **pz** 导出的信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **fz** — 作用在关节基元上的执行器力 物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节基元上的下限力 物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下限时，模块施加此力。模块将此力施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节基元上的上限力 物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上限时，模块施加此力。模块将此力施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

物理信号端口，输出作用在关节上的约束力。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的约束力矩。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

物理信号端口，输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力之和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的总力矩。总力矩是通过关节在相连坐标系之间传递的所有力矩之和。该力矩包括驱动力矩、内力矩、限位力矩和约束力矩。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### Spherical Primitive (S)

#### 状态目标

### **Specify Position Target** — 是否指定相对方向目标 `off` (默认) | `on`

选择此参数以指定基座坐标系和从动坐标系之间相对方向的目标。

### **Priority** — 相对方向目标的优先级 `High (desired)` (默认) | `Low (approximate)`

相对方向目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value > Method** — 指定相对方向目标的方法 `None` (默认) | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基座坐标系和从动坐标系之间相对方向目标的方法。当您将此参数设置为 `None` 时，方向目标会使基座坐标系和从动坐标系对齐。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+X` (默认) | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基座坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座坐标系和从动坐标系的所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以使基座坐标系和从动坐标系的所选轴之间能够对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的从动坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系绕指定轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转轴 [0 0 1]（默认）| 3-by1 向量

相对旋转的轴，指定为 3-by-1 单位向量。该向量无量纲，表示在基座坐标系中解析的旋转轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系绕由 **Axis** 参数指定的轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 用于绕其轴旋转从动坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

用于绕其轴旋转从动坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将参数设置为 `Follower Axes`，则从动坐标系绕其自身的轴旋转，并且从动坐标系在每次连续旋转时改变方向。如果将参数设置为 `Base Axes`，则从动坐标系绕固定的基座坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 旋转序列参数化的角度 [0 0 0] `deg`（默认）| 1-by-3 向量

旋转序列参数化的角度，指定为 1-by-3 向量。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Rotation Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3-by-3 矩阵

相对旋转，指定为将向量从从动坐标系映射到基座坐标系的 3-by-3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Quaternion`。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数可指定球面基元的角速度目标。

### **Priority** — 角速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 球面基元的角速度目标 [0 0 0] `deg/s`（默认）| 1-by-3 向量

球面基元的角速度目标，指定为在解析坐标系中解析的 1-by-3 向量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Resolution Frame** — 用于解析指定角速度目标的坐标系 `Base`（默认）| `Follower`

用于解析指定角速度目标的坐标系，指定为以下之一：

- `Base` — 关节模块在基座坐标系的坐标中解析角速度目标。
- `Follower` — 关节模块在从动坐标系的坐标中解析角速度目标。

#### 内部机制

### **Equilibrium Position > Method** — 用于指定平衡坐标系的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基座坐标系的方向的方法。在整个仿真过程中，平衡坐标系保持相对于基座坐标系固定。当您将参数设置为 `None` 时，平衡坐标系与基座坐标系对齐。

当从动坐标系和平衡坐标系对齐时，球面基元的弹簧力矩为零。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基座坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以使基座坐标系和平衡坐标系的所选轴之间能够对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以使基座坐标系和平衡坐标系的所选轴之间能够对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的平衡坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系绕指定轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转轴 [0 0 1]（默认）| 3-by1 向量

相对旋转的轴，指定为 3-by-1 单位向量。该向量无量纲，表示在基座坐标系中解析的旋转轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系绕由 **Axis** 参数指定的轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 用于绕其轴旋转平衡坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

用于绕其轴旋转平衡坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将参数设置为 `Follower Axes`，则平衡坐标系绕其自身的轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将参数设置为 `Base Axes`，则平衡坐标系绕固定的基座坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 基本旋转的角度 [0 0 0] `deg`（默认）| 1-by-3 向量

基本旋转的角度，指定为 1-by-3 向量。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3-by-3 矩阵

相对旋转，指定为 3-by-3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Quaternion`。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

球面基元的内部弹簧-阻尼器力律的刚度，指定为具有旋转刚度单位的标量。

弹簧尝试拉动从动坐标系，以使从动坐标系与指定的平衡坐标系对齐。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

球面基元的内部弹簧-阻尼器力律的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置限制 `off`（默认）| `on`

选择此参数可指定球面基元的下限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的移动。

### **Bound** — 自由区域的下界 15 `deg`（默认）| 标量

球面基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

下界处的弹簧刚度，指定为具有旋转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器力矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块应用下限力矩的完整值。该区域越小，力矩开始得越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置限制 `off`（默认）| `on`

选择此参数可指定球面基元的上限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的移动。

### **Bound** — 自由区域的上界 45 `deg`（默认）| 标量

球面基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为具有刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

上界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼器力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域的宽度时，模块施加完整的上限力矩值。区域越小，力矩出现得越尖锐，求解器所需的时间步越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input`

为球面基元提供驱动力矩的选项，指定为以下值之一。

| 驱动扭矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动力矩。 |
| `Provided by Input` | 基于物理信号施加驱动力矩。该信号指定作用在从动坐标系上相对于基坐标系的力矩。该信号提供对基坐标系和从动坐标系等大反向施加的力矩值。选择此选项会显示附加参数，可用于启用输入端口。有关详细信息，请参阅 **输入** 部分。 |

### **Resolution Frame** — 用于解析驱动力矩的坐标系 `Base`（默认）| `Follower`

用于解析输入驱动力矩的坐标系，指定为 `Base` 或 `Follower`。

#### 传感

### **Resolution Frame** — 用于解析传感输出的坐标系 `Base`（默认）| `Follower`

用于解析传感输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的详细信息，请参阅 **输出** 部分。

### Z Prismatic Primitive (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| scalar

*z* 移动副基元的位置目标，指定为以长度单位为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| scalar

*z* 移动副基元的线速度目标，指定为以线速度单位为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认）| scalar

弹簧力为零的位置，指定为以长度单位为单位的 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| scalar

关节基元的内部弹簧-阻尼器力定律的刚度，指定为以线性刚度为单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| scalar

关节基元的内部弹簧-阻尼器力定律的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定下位置限制 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| scalar

*z* 移动副基元的自由区域的下界，指定为以长度单位为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e6 `N/m`（默认）| scalar

下界处弹簧的刚度，指定为以线性刚度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

下界处的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧和阻尼器力的区域，指定为以长度单位为单位的 scalar。

当穿透量达到过渡区域的宽度时，模块施加完整的下限力值。区域越小，力出现得越尖锐，求解器所需的时间步越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限制 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| scalar

关节基元的自由区域的上界，指定为以长度单位为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| scalar

上界处弹簧的刚度，指定为以线性刚度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

上界处的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧和阻尼器力的区域，指定为以长度单位为单位的 scalar。

当穿透量达到过渡区域的宽度时，模块施加完整的上限力值。区域越小，力出现得越尖锐，求解器所需的时间步越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fz** 指定 *z* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块基于模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **pz** 指定关节基元的运动。 |

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | `Locked` 模式约束关节的所有自由度 (DOF)。锁定关节在仿真期间以零速度保持其初始装配位置。关节模块可以根据 **内部力学**、**限制** 和 **驱动** 参数的设置感测力或力矩。 |
| `Normal` | `Normal` 模式启用自由度，关节约束在仿真期间按预期工作。 |
| `Disengaged` | `Disengaged` 模式在整个仿真期间将关节从所有约束中释放。**内部力学**、**限制** 和 **驱动** 参数的设置不影响分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许使用输入信号指定关节模式。有关详细信息，请参阅 **输入** 部分中的端口 **mode**。 |

### 复合力/力矩传感

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块感测基坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **复合力/力矩传感** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **复合力/力矩传感** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障

现在可以为所有关节模块建模模式故障。使用这些故障，可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有一个球面和一个移动副关节基元的关节

Telescoping Joint 模块在两个坐标系之间提供三个旋转和一个平移自由度，如图所示。

伸缩关节的关节变换序列

从动坐标系可以相对于基坐标系通过先进行 3-D 旋转，然后沿从动坐标系的 *z* 轴平移来进行变换。该图显示了在给定仿真时间步中关节变换发生的顺序。

伸缩关节的关节变换序列

由于旋转编码为四元数，3-D 旋转没有运动学奇异性。

要为关节基元指定初始状态的目标，请使用 **状态目标** 下的参数。这些目标在基坐标系中指定。还可以为这些目标设置优先级。如果关节无法满足所有状态目标，优先级将确定先满足哪些目标以及满足的接近程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **内部力学** 下的参数。使用 **Damping Coefficient** 参数建模能量耗散，使用 **Spring Stiffness** 参数建模能量存储。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器则作为能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限制，请使用 **限制** 下的参数。下限和上限定义自由区域的宽度。当位置超出边界时，模块施加力以将关节位置加速回到自由区域。模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**驱动** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，可用于对模型执行分析任务。有关详细信息，请参阅 Sensing 和 Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **模式配置**。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为脱开状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡的 **Faults** 部分中，点击 **Fault** > `Add Fault`。
或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击“Add a fault on the block icon”按钮以添加故障。您可以将多个故障添加到关节模块，但在一次仿真期间，关节模块只能有一个活动故障。

添加故障时，在属性检查器中，**Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅设置故障触发器。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用故障表。有关更多详细信息，请参阅访问故障表和故障仪表板。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真处于打开状态。仿真会记录触发状态数据。要查看数据，请使用仿真数据检查器。此外，您可以在故障仪表板中查看故障状态和已触发故障的摘要。要打开故障仪表板，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
