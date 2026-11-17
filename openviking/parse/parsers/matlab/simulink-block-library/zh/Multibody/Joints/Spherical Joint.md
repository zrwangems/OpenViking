---
type: simulink-block
title: 'Spherical Joint'
family: 'joints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'sphericaljoint'
documentation_source_path: 'ref/sphericaljoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Spherical Joint

## 端口

### 坐标系

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。
### 输入

#### Spherical Primitive (S)

### **tx** — 绕解析坐标系的 *x* 轴的驱动力矩 physical signal

physical signal 输入端口，用于接受球面基元的驱动力矩。该信号具有 scalar 格式，表示绕解析坐标系的 *x* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (X)**。

### **ty** — 绕解析坐标系的 *y* 轴的驱动力矩 physical signal

physical signal 输入端口，用于接受球面基元的驱动力矩。该信号具有 scalar 格式，表示绕解析坐标系的 *y* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Y)**。

### **tz** — 绕解析坐标系的 *z* 轴的驱动力矩 physical signal

physical signal 输入端口，用于接受球面基元的驱动力矩。该信号具有 scalar 格式，表示绕解析坐标系的 *z* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Z)**。

### **t** — 驱动力矩 vector physical signal

physical signal 输入端口，用于接受球面基元的驱动力矩。该 vector 表示要在基础坐标系和从动坐标系之间施加的驱动力矩，以解析坐标系表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`，并选择 **Torque (XYZ)**。

#### 模式配置

### **mode** — 关节模式控制 physical signal

输入端口，用于控制关节的模式。该信号必须是 unitless scalar。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，关节模式为 disengaged；当输入信号为 `1` 时，关节模式为 locked。您可以在仿真过程中的任意时间更改模式。

该表显示了在模式之间转换期间关节的位置和速度如何变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal 到 Locked | 关节位置保持当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal 到 Disengaged | 关节位置保持当前值，但在转换后可以沿任意方向变化。 | 关节速度保持当前值，但在转换后可以沿任意方向变化。 |
| Locked 到 Normal | 关节位置保持当前值，但在转换后可以沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但在转换后可以沿与关节 DOFs 对齐的方向变化。 |
| Locked 到 Disengaged | 关节位置保持当前值，但在转换后可以沿任意方向变化。 | 关节速度保持为零，但在转换后可以沿任意方向变化。 |
| Disengaged 到 Normal | 对于与关节 DOFs 对齐的方向，关节位置最初采用通过牛顿法计算的值，此后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOFs 对齐的方向，关节速度最初采用通过牛顿法计算的值，此后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged 到 Locked | 对于与关节 DOFs 对齐的方向，关节位置最初采用通过牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### Spherical Primitive (S)

### **Q** — 四元数参数化中的相对方位 physical signal

从动坐标系相对于基础坐标系的方位，以单位四元数返回。有关详细信息，请参阅 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 `x` 坐标 physical signal

相对角速度的 *x* 坐标，以 scalar 返回。该值在解析坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 `y` 坐标 physical signal

相对角速度的 *y* 坐标，以 scalar 返回。该值在解析坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 `z` 坐标 physical signal

相对角速度的 *z* 坐标，以 scalar 返回。该值在解析坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度 vector physical signal

相对角速度，以在解析坐标系中解析的 3-D vector 返回。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 相对角加速度的 `x` 坐标 physical signal

相对角加速度的 *x* 坐标，以 scalar 返回。此量等于从端口 **wx** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (X)**。

### **by** — 相对角加速度的 `y` 坐标 physical signal

相对角加速度的 *y* 坐标，以 scalar 返回。此量等于从端口 **wy** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Y)**。

### **bz** — 相对角加速度的 `z` 坐标 physical signal

相对角加速度的 *z* 坐标，以 scalar 返回。此量等于从端口 **wz** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Z)**。

### **b** — 角加速度 vector physical signal

相对角加速度，以在解析坐标系中解析的 3-D vector 返回。此量等于从端口 **w** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration**。

### **tll** — 下限力矩幅值 physical signal

physical signal 端口，用于输出下限力矩的幅值。当两个坐标系的 *z* 轴之间的角度小于下限边界时，该模块施加下限力矩。该力矩施加到球面基元的基础坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Signed Lower-Limit Torque Magnitude**。

### **tul** — 上限力矩幅值 physical signal

physical signal 端口，用于输出上限力矩的幅值。当两个坐标系的 *z* 轴之间的角度超过上限边界时，该模块施加上限力矩。该力矩施加到球面基元的基础坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/力矩感测

### **fc** — 约束力，N physical signal

physical signal 端口，用于输出作用在关节上的约束力。这些力维持关节的平移约束。输出采用 3-by-1 vector 格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m physical signal

physical signal 端口，用于输出作用在关节上的约束力矩。这些力矩维持关节的旋转约束。输出采用 3-by-1 vector 格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N physical signal

physical signal 端口，用于输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力的总和。输出采用 3-by-1 vector 格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力图示

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m physical signal

physical signal 端口，用于输出作用在关节上的总力矩。总力矩是通过关节在相连坐标系之间传递的所有力矩的总和。该力矩包括驱动力矩、内力矩、限值力矩和约束力矩。输出采用 3-by-1 vector 格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

### Spherical Primitive (S)

#### 状态目标

### **Specify Position Target** — 是否指定相对方位目标 `off` (默认) | `on`

选择此参数以指定基础坐标系和从动坐标系之间相对方位的目标。

### **Priority** — 相对方位目标的优先级 `High (desired)` (默认) | `Low (approximate)`

相对方位目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value > Method** — 指定相对方位目标的方法 `None` (默认) | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基础坐标系和从动坐标系之间相对方位目标的方法。当您将该参数设置为 `None` 时，方位目标会使基础坐标系和从动坐标系对齐。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Pair 1: Follower** — 用于与指定基础坐标系轴对齐的从动坐标系轴 `+X` (默认) | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Base** 参数设置的基础坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基础坐标系旋转，以实现基础坐标系和从动坐标系的所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基础坐标系轴 `+Y` (默认) | `+X` | `-X` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Follower** 指定的从动坐标系对齐的基础坐标系轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基础坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

基础坐标系轴，用于与 **Pair 2: Follower** 指定的从动坐标系对齐，指定为从动坐标系的正交轴。从动坐标系相对于基础坐标系旋转，以实现基础坐标系和从动坐标系的所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基础坐标系轴 `+Z` (默认) | `+X` | `-X` | `+Y` | `-Y` | `-Z`

基础坐标系轴，用于让 **Pair2: Follower** 参数中设置的从动坐标系轴与之对齐，指定为基础坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z` (默认) | `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg` (默认) | scalar

相对旋转的角度，指定为 scalar。该角度表示从动坐标系绕指定轴相对于基础坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1] (默认) | 3-by1 vector

相对旋转的轴，指定为 3-by-1 unit vector。该 vector 是无量纲的，表示在基础坐标系中解析的旋转轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg` (默认) | scalar

相对旋转的角度，指定为 scalar。该角度表示从动坐标系绕 **Axis** 参数指定的轴相对于基础坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 从动坐标系要绕其轴旋转的坐标系 `Follower Axes` (默认) | `Base Axes`

从动坐标系要绕其轴旋转的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果您将该参数设置为 `Follower Axes`，从动坐标系绕其自身轴旋转，并且从动坐标系在每次连续旋转时更改方位。如果您将该参数设置为 `Base Axes`，从动坐标系绕固定基础坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认） | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 旋转序列参数化的角度 [0 0 0] `deg`（默认） | 1-by-3 向量

旋转序列参数化的角度，指定为 1-by-3 向量。有关详细信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Rotation Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认） | 3-by-3 矩阵

相对旋转，指定为将向量从 follower frame 映射到 base frame 的 3-by-3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认） | 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Quaternion`。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认） | `on`

选择此参数以指定球形基元的角速度目标。

### **Priority** — 角速度目标的优先级 `High (desired)`（默认） | `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参见 Guiding Assembly。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 球形基元的角速度目标 [0 0 0] `deg/s`（默认） | 1-by-3 向量

球形基元的角速度目标，指定为在 resolution frame 中解算的 1-by-3 向量。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Resolution Frame** — 用于解算指定角速度目标的坐标系 `Base`（默认） | `Follower`

用于解算指定角速度目标的坐标系，指定为以下值之一：

- `Base` — 关节模块在基坐标系的坐标中解算角速度目标。
- `Follower` — 关节模块在从动坐标系的坐标中解算角速度目标。

#### 内部力学

### **Equilibrium Position > Method** — 指定平衡坐标系的方法 `None`（默认） | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基坐标系方向的方法。平衡坐标系在整个仿真过程中保持相对于基坐标系固定。当您将该参数设置为 `None` 时，平衡坐标系与基坐标系对齐。

当从动坐标系和平衡坐标系对齐时，球形基元的弹簧扭矩为零。

### **Pair 1: Follower** — 用于与指定基坐标系轴对齐的平衡坐标系轴 `+X`（默认） | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基坐标系旋转，以使基坐标系和平衡坐标系的选定轴之间能够对齐。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基坐标系轴 `+Y`（默认） | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的平衡坐标系对齐的基坐标系轴，指定为基坐标系的正交轴。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的平衡坐标系对齐的基坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基坐标系旋转，以使基坐标系和平衡坐标系的选定轴之间能够对齐。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基坐标系轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的平衡坐标系轴对齐的基坐标系轴，指定为基坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基坐标系的正交轴。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系绕指定轴相对于基坐标系旋转的角度。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认） | 3-by1 向量

相对旋转的轴，指定为 3-by1 单位向量。该向量无量纲，表示在基坐标系中解算的旋转轴。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系绕由 **Axis** 参数指定的轴相对于基坐标系旋转的角度。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 要绕其轴旋转平衡坐标系的坐标系 `Follower Axes`（默认） | `Base Axes`

要绕其轴旋转平衡坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则平衡坐标系绕其自身轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则平衡坐标系绕固定的基坐标系轴旋转。有关详细信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认） | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 基本旋转的角度 [0 0 0] `deg`（默认） | 1-by-3 向量

基本旋转的角度，指定为 1-by-3 向量。有关详细信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认） | 3-by-3 矩阵

相对旋转，指定为 3-by-3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认） | 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Quaternion`。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认） | 标量

球形基元的内部弹簧-阻尼力定律的刚度，指定为具有旋转刚度单位的标量。

弹簧尝试拉动从动坐标系，以使从动坐标系与指定的平衡坐标系对齐。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N*m/(deg/s)`（默认） | 标量

球形基元的内部弹簧-阻尼力定律的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认） | `on`

选择此参数以指定球形基元的下限。关节限制使用弹簧-阻尼器来阻止越过范围边界的移动。

### **Bound** — 自由区域的下界 15 `deg`（默认） | 标量

球形基元的自由区域的下界，指定为具有角度单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处的弹簧刚度 1e4 `N*m/deg`（默认） | 标量

下限处的弹簧刚度，指定为具有旋转刚度单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 10 `N*m/(deg/s)`（默认） | 标量

下限处的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认） | 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块施加下限扭矩的完整值。该区域越小，扭矩的出现越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认） | `on`

选择此参数以指定球形基元的上限。关节限制使用弹簧-阻尼器来阻止越过范围边界的移动。

### **Bound** — 自由区域的上界 45 `deg`（默认） | 标量

球形基元的自由区域的上界，指定为具有角度单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处的弹簧刚度 1e4 `N*m/deg`（默认） | 标量

上限处的弹簧刚度，指定为具有刚度单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 10 `N*m/(deg/s)`（默认） | 标量

上限处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认） | 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块施加上限扭矩的完整值。该区域越小，扭矩的出现越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供驱动扭矩的选项 `None`（默认） | `Provided by Input`

用于为球形基元提供驱动扭矩的选项，指定为以下值之一。

| 驱动扭矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动扭矩。 |
| `Provided by Input` | 基于物理信号施加驱动扭矩。该信号指定作用在从动坐标系上相对于基坐标系的扭矩。该信号提供等大反向作用于基坐标系和从动坐标系的扭矩值。选择此选项会显示附加参数，您可以使用这些参数来启用输入端口。有关详细信息，请参见 **Input** 部分。 |

### **Resolution Frame** — 用于解算驱动扭矩的坐标系 `Base`（默认） | `Follower`

用于解算输入驱动扭矩的坐标系，指定为 `Base` 或 `Follower`。

#### 传感

### **Resolution Frame** — 用于解算传感输出的坐标系 `Base`（默认） | `Follower`

用于解算传感输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的详细信息，请参见 **Output** 部分。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认） | `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | `Locked` 模式约束关节的所有自由度 (DOFs)。锁定关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或扭矩。 |
| `Normal` | `Normal` 模式启用关节的自由度，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | `Disengaged` 模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响分离的关节。所有输出端口均输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您使用输入信号指定关节模式。有关详细信息，请参见 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩传感

### **Direction** — 测量方向 `Follower on Base` (默认) | `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加到基座坐标系上的力和扭矩。
- `Base on Follower` — 模块感测基座坐标系施加到从动坐标系上的力和扭矩。

此参数仅影响 **复合力/扭矩传感** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅力和扭矩测量方向。

### **Resolution Frame** — 用于解析测量的坐标系 `Base` (默认) | `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基座坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **复合力/扭矩传感** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a: 模型模式故障

您现在可以为所有关节模块建模模式故障。使用这些故障，您可以在仿真期间更改关节模式，而不更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

关节允许 3-D 旋转

Spherical Joint 模块在两个坐标系之间提供三个旋转自由度。从动坐标系可以相对于基座坐标系具有任意 3-D 旋转。在仿真期间，基座坐标系和从动坐标系的原点保持重合，如图所示。

Spherical joint 的关节变换序列

与万向关节不同，Spherical Joint 没有运动学奇异。

要为关节基元指定初始状态的目标，请使用 **状态目标** 下的参数。目标在基座坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级确定首先满足哪些目标以及满足的程度。有关示例，请参阅多体装配如何工作的引导装配部分。

要为关节基元建模阻尼和弹簧行为，请使用 **内部力学** 下的参数。使用 **Damping Coefficient** 参数来建模能量耗散，使用 **Spring Stiffness** 参数来建模能量存储。关节弹簧试图使关节基元偏离其平衡位置，而关节阻尼器充当能量耗散元件。弹簧和阻尼器严格线性。

要指定关节基元的限制，请使用 **限制** 下的参数。下限和上限定义了自由区域的宽度。当位置超过边界时，模块施加力以将关节位置加速回自由区域。模块使用平滑弹簧阻尼器方法计算该力。有关平滑弹簧阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**驱动** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅指定关节驱动输入。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅传感以及力和扭矩传感。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **模式配置**。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则关节变为 disengaged。

要向关节模块添加模式故障，请单击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，单击 **Fault** > `Add Fault`。或者，您可以单击关节模块，悬停以打开操作栏的省略号，然后单击 Add a fault on the block icon Button 来添加故障。您可以向关节模块添加多个故障，但关节模块在仿真期间只能有一个活动故障。

添加故障时，在属性检查器中，在 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请单击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅设置故障触发器。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要设置模块的活动故障，请使用故障表。有关更多详细信息，请参阅访问故障表和故障仪表板。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真开启。仿真会记录触发状态数据。要查看数据，请使用仿真数据检查器。此外，您可以在故障仪表板中查看故障状态和已触发故障的摘要。要打开故障仪表板，请在 **Simscape Block** 选项卡中，单击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink 故障控制和 Simscape 故障接口的函数部分。
