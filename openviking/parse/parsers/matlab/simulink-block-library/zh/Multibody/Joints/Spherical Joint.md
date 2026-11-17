---
type: simulink-block
title: 'Spherical Joint'
family: 'sm'
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
```yaml
ports:
- name: B
  summary: 基础坐标系 坐标系
  direction: input
- name: F
  summary: 从动坐标系 坐标系
  direction: input
- name: tx
  summary: 关于解算坐标系 *x* 轴的驱动力矩 物理信号
  direction: input
- name: ty
  summary: 关于解算坐标系 *y* 轴的驱动力矩 物理信号
  direction: input
- name: tz
  summary: 关于解算坐标系 *z* 轴的驱动力矩 物理信号
  direction: input
- name: t
  summary: 驱动力矩向量 物理信号
  direction: input
- name: mode
  summary: 关节模式控制物理信号
  direction: input
- name: Q
  summary: 四元数参数化下的相对姿态物理信号
  direction: output
- name: wx
  summary: 相对角速度的 x 坐标物理信号
  direction: output
- name: wy
  summary: 相对角速度的 y 坐标物理信号
  direction: output
- name: wz
  summary: 相对角速度的 z 坐标物理信号
  direction: output
- name: w
  summary: 角速度向量物理信号
  direction: output
- name: bx
  summary: 相对角加速度的 x 坐标物理信号
  direction: output
- name: by
  summary: 相对角加速度的 y 坐标物理信号
  direction: output
- name: bz
  summary: 相对角加速度的 z 坐标物理信号
  direction: output
- name: b
  summary: 角加速度矢量物理信号
  direction: output
- name: tll
  summary: 下限力矩幅值物理信号
  direction: output
- name: tul
  summary: 上限力矩幅值物理信号
  direction: output
- name: fc
  summary: 约束力，N 物理信号
  direction: output
- name: tc
  summary: 约束力矩，N\*m 物理信号
  direction: output
- name: ft
  summary: 总力，N 物理信号
  direction: output
- name: tt
  summary: 总力矩，N\*m 物理信号
  direction: output
```

### 坐标系

### **B** — 基础坐标系 坐标系

关节模块的基础坐标系。

### **F** — 从动坐标系 坐标系

关节模块的从动坐标系。
### 输入

#### 球面基元 (S)

### **tx** — 关于解算坐标系 *x* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解算坐标系 *x* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (X)**。

### **ty** — 关于解算坐标系 *y* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解算坐标系 *y* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (Y)**。

### **tz** — 关于解算坐标系 *z* 轴的驱动力矩 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解算坐标系 *z* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (Z)**。

### **t** — 驱动力矩向量 物理信号

物理信号输入端口，接受球面基元的驱动力矩。该向量表示在基础坐标系和从动坐标系之间施加的驱动力矩，以解算坐标系表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input` 并选择 **Torque (XYZ)**。

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，关节模式为 disengaged；当输入信号为 `1` 时，关节模式为 locked。你可以在仿真过程中的任意时刻更改模式。

下表显示了在模式之间切换时，关节的位置和速度如何变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| Normal 到 Locked | 关节位置保留当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| Normal 到 Disengaged | 关节位置保留当前值，但在切换后可以沿任意方向变化。 | 关节速度保留当前值，但在切换后可以沿任意方向变化。 |
| Locked 到 Normal | 关节位置保留当前值，但在切换后可以沿与关节自由度（DOFs）对齐的方向变化。 | 关节速度保持为零，但在切换后可以沿与关节 DOFs 对齐的方向变化。 |
| Locked 到 Disengaged | 关节位置保留当前值，但在切换后可以沿任意方向变化。 | 关节速度保持为零，但在切换后可以沿任意方向变化。 |
| Disengaged 到 Normal | 对于与关节 DOFs 对齐的方向，关节位置最初取通过使用 Newton 方法计算得到的值，此后可以变化。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节 DOFs 对齐的方向，关节速度最初取通过使用 Newton 方法计算得到的值，此后可以变化。在受约束方向上，关节速度变为零，并在切换后保持不变。 |
| Disengaged 到 Locked | 对于与关节 DOFs 对齐的方向，关节位置最初取通过使用 Newton 方法计算得到的值，并在切换后保持不变。在受约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### Spherical Primitive (S)

### **Q** — 四元数参数化下的相对姿态物理信号

从动坐标系相对于基坐标系的姿态，以单位四元数返回。有关更多信息，请参见 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 `x` 坐标物理信号

相对角速度的 *x* 坐标，以标量返回。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 `y` 坐标物理信号

相对角速度的 *y* 坐标，以标量返回。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 `z` 坐标物理信号

相对角速度的 *z* 坐标，以标量返回。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度向量物理信号

相对角速度，以在 resolution frame 中解析的 3-D 向量返回。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 相对角加速度的 `x` 坐标物理信号

相对角加速度的 *x* 坐标，以标量形式返回。该量等于从端口 **wx** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (X)**。

### **by** — 相对角加速度的 `y` 坐标物理信号

相对角加速度的 *y* 坐标，以标量形式返回。该量等于从端口 **wy** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Y)**。

### **bz** — 相对角加速度的 `z` 坐标物理信号

相对角加速度的 *z* 坐标，以标量形式返回。该量等于从端口 **wz** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Z)**。

### **b** — 角加速度矢量物理信号

相对角加速度，以在解析坐标系中表示的 3 维矢量形式返回。该量等于从端口 **w** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration**。

### **tll** — 下限力矩幅值物理信号

输出下限力矩幅值的物理信号端口。当两个坐标系的 *z* 轴之间的角度小于下限边界时，该模块施加下限力矩。该力矩施加于球面基元的基础坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Signed Lower-Limit Torque Magnitude**。

### **tul** — 上限力矩幅值物理信号

输出上限力矩幅值的物理信号端口。当两个坐标系的 *z* 轴之间的角度超过上限边界时，该模块施加上限力矩。该力矩施加于球面基元的基础坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 矢量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅力与力矩传感。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 矢量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力与力矩传感。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连坐标系之间传递的所有力的总和。输出为 3×1 向量格式，表示沿解析坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，图中展示了一个使用棱柱关节模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在相连坐标系之间传递的所有力矩的总和。力矩包括执行、内力、限位和约束力矩。输出为 3×1 向量格式，表示绕解析坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力矩**。
## 参数
```yaml
parameters:
- name: 指定位置目标
  summary: 是否指定相对方向目标 off（默认）| on
  group: 球形基元 (S)
- name: 优先级
  summary: 相对方向目标的优先级 High (desired)（默认）| Low (approximate)
  group: 球形基元 (S)
- name: 值 > 方法
  summary: 指定相对方向目标的方法 None（默认）| Aligned Axes | Standard Axis | Arbitrary Axis | Rotation Sequence | Rotation Matrix | Quaternion
  group: 球形基元 (S)
- name: 配对 1：从动
  summary: 用于与指定基座坐标系轴对齐的从动坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 配对 1：基座
  summary: 基座坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 配对 2：从动
  summary: 用于与指定基座坐标系轴对齐的从动坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 'Pair2: Base'
  summary: 基座坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: 球形基元 (S)
- name: Axis
  summary: 相对旋转的标准轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: 球形基元 (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: 球形基元 (S)
- name: Axis
  summary: 相对旋转的轴 [0 0 1]（默认）| 3×1 向量
  group: 球形基元 (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: 球形基元 (S)
- name: Rotation About
  summary: 绕其轴旋转跟随坐标系的坐标系 Follower Axes（默认）| Base Axes
  group: 球形基元 (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: 球形基元 (S)
- name: Angles
  summary: 旋转序列参数化的角度 [0 0 0] deg（默认）| 1×3 向量
  group: 球形基元 (S)
- name: Rotation Matrix
  summary: 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: 球形基元 (S)
- name: Quaternion
  summary: 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
  group: 球形基元 (S)
- name: Specify Velocity Target
  summary: 是否指定角速度目标 off（默认）| on
  group: 球形基元 (S)
- name: Priority
  summary: 角速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: 球形基元 (S)
- name: Value
  summary: 球面基元的角速度目标 [0 0 0] deg/s（默认）| 1×3 向量
  group: 球形基元 (S)
- name: Resolution Frame
  summary: 用于解算指定角速度目标的坐标系 Base（默认）| Follower
  group: 球形基元 (S)
- name: Equilibrium Position > Method
  summary: 指定平衡坐标系的方法 None（默认）| Aligned Axes | Standard Axis | Arbitrary Axis | Rotation Sequence | Rotation Matrix | Quaternion
  group: 球形基元 (S)
- name: 'Pair 1: Follower'
  summary: 用于与指定基座坐标系轴对齐的平衡坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 'Pair 1: Base'
  summary: 基座坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 'Pair 2: Follower'
  summary: 用于与指定基座坐标系轴对齐的平衡坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: 球形基元 (S)
- name: 'Pair2: Base'
  summary: 基座坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: 球形基元 (S)
- name: Axis
  summary: 相对旋转的标准轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: 球形基元 (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: 球形基元 (S)
- name: Axis
  summary: 相对旋转的轴 [0 0 1]（默认）| 3×1 向量
  group: 球形基元 (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: 球形基元 (S)
- name: Rotation About
  summary: 绕其轴旋转平衡坐标系的坐标系 Follower Axes（默认）| Base Axes
  group: 球形基元 (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: 球形基元 (S)
- name: Angles
  summary: 基本旋转的角度 [0 0 0] deg（默认）| 1×3 向量
  group: 球形基元 (S)
- name: Matrix
  summary: 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: 球形基元 (S)
- name: Quaternion
  summary: 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
  group: 球形基元 (S)
- name: Spring Stiffness
  summary: 力律的刚度 0 N*m/deg（默认）| 标量
  group: 球形基元 (S)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N*m/(deg/s)（默认）| 标量
  group: 球形基元 (S)
- name: Specify Lower Limit
  summary: 是否指定下位置限制 off（默认）| on
  group: 球形基元 (S)
- name: Bound
  summary: 自由区域的下界 15 deg（默认）| 标量
  group: 球形基元 (S)
- name: Spring Stiffness
  summary: 下界处弹簧的刚度 1e4 N*m/deg（默认）| 标量
  group: 球形基元 (S)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: 球形基元 (S)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: 球形基元 (S)
- name: Specify Upper Limit
  summary: 是否指定上位置限制 off（默认）| on
  group: 球形基元 (S)
- name: Bound
  summary: 自由区域的上界 45 deg（默认）| 标量
  group: 球形基元 (S)
- name: Spring Stiffness
  summary: 上界处弹簧的刚度 1e4 N*m/deg（默认）| 标量
  group: 球形基元 (S)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: 球形基元 (S)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力矩的区域 0.1 deg（默认）| 标量
  group: 球形基元 (S)
- name: Torque
  summary: 提供驱动力矩的选项 None（默认）| Provided by Input
  group: 球形基元 (S)
- name: Resolution Frame
  summary: 用于分解驱动力矩的坐标系 Base（默认）| Follower
  group: 球形基元 (S)
- name: Resolution Frame
  summary: 用于分解传感输出的坐标系 Base（默认）| Follower
  group: 球形基元 (S)
- name: Mode
  summary: 关节模式 Normal（默认）| Locked | Disengaged | Provided by Input
  group: 模式配置
- name: Direction
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: 复合力/力矩传感
- name: Resolution Frame
  summary: 用于解析测量的坐标系 Base（默认）| Follower
  group: 复合力/力矩传感
```

### 球形基元 (S)

#### 状态目标

### **指定位置目标** — 是否指定相对方向目标 `off`（默认）| `on`

选择此参数以指定基座坐标系和从动坐标系之间相对方向的目标。

### **优先级** — 相对方向目标的优先级 `High (desired)`（默认）| `Low (approximate)`

相对方向目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅引导装配。

#### 依赖关系

要启用此参数，请选择**指定位置目标**。

### **值 > 方法** — 指定相对方向目标的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基座坐标系和从动坐标系之间相对方向目标的方法。当您将该参数设置为 `None` 时，方向目标将使基座坐标系和从动坐标系对齐。

#### 依赖关系

要启用此参数，请选择**指定位置目标**。

### **配对 1：从动** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由**配对 1：基座**参数设置的基座坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座坐标系和从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在**指定位置目标** > **值**下，将**方法**参数设置为 `Aligned Axis`。

### **配对 1：基座** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由**配对 1：从动**指定的从动坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在**指定位置目标** > **值**下，将**方法**参数设置为 `Aligned Axis`。

### **配对 2：从动** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由**配对 2：从动**指定的从动坐标系对齐的基座坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座坐标系和从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在**指定位置目标** > **值**下，将**方法**参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让在 **Pair2: Follower** 参数中设置的跟随坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示跟随坐标系相对于基座坐标系绕指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基座坐标系中分解的旋转轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示跟随坐标系相对于基座坐标系绕由 **Axis** 参数指定的轴的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 绕其轴旋转跟随坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

绕其轴旋转跟随坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则跟随坐标系绕其自身轴旋转，并且跟随坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则跟随坐标系绕固定的基座坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 旋转序列参数化的角度 [0 0 0] `deg`（默认）| 1×3 向量

旋转序列参数化的角度，指定为 1×3 向量。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Rotation Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为将向量从跟随坐标系映射到基座坐标系的 3×3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的更多信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Quaternion`。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定球面基元的角速度目标。

### **Priority** — 角速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 球面基元的角速度目标 [0 0 0] `deg/s`（默认）| 1×3 向量

球面基元的角速度目标，指定为在解算坐标系中表示的 1×3 向量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Resolution Frame** — 用于解算指定角速度目标的坐标系 `Base`（默认）| `Follower`

用于解算指定角速度目标的坐标系，指定为以下之一：

- `Base` — 关节模块在基座坐标系的坐标中解算角速度目标。
- `Follower` — 关节模块在从动坐标系的坐标中解算角速度目标。

#### 内部机制

### **Equilibrium Position > Method** — 指定平衡坐标系的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基座坐标系的方向的方法。平衡坐标系在整个仿真过程中相对于基座坐标系保持固定。当您将该参数设置为 `None` 时，平衡坐标系与基座坐标系对齐。

当从动坐标系和平衡坐标系对齐时，球面基元的弹簧扭矩为零。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基座坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于使 **Pair2: Follower** 参数中设置的平衡坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系相对于基座坐标系绕指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基座坐标系中分解的旋转轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系相对于基座坐标系绕 **Axis** 参数指定的轴的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 绕其轴旋转平衡坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

绕其轴旋转平衡坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则平衡坐标系绕其自身轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则平衡坐标系绕固定的基座坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 基本旋转的角度 [0 0 0] `deg`（默认）| 1×3 向量

基本旋转的角度，指定为 1×3 向量。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Rotation Sequence`。

### **Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为 3×3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Quaternion`。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

球面基元内部弹簧-阻尼力律的刚度，指定为具有旋转刚度单位的标量。

弹簧尝试拉动从动坐标系，使从动坐标系与指定的平衡坐标系对齐。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

球面基元内部弹簧-阻尼力律的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下位置限制 `off`（默认）| `on`

选择此参数以指定球面基元的下限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的运动。

### **Bound** — 自由区域的下界 15 `deg`（默认）| 标量

球面基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

下界处弹簧的刚度，指定为具有旋转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块施加下限扭矩的完整值。区域越小，扭矩的起始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限制 `off`（默认）| `on`

选择此参数以指定球面基元的上限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的运动。

### **Bound** — 自由区域的上界 45 `deg`（默认）| 标量

球面基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

上界处弹簧的刚度，指定为具有刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为带角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加完整的上限力矩值。该区域越小，力矩的出现越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input`

为球面基元提供驱动力矩的选项，指定为以下值之一。

| 驱动力矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动力矩。 |
| `Provided by Input` | 基于物理信号施加驱动力矩。该信号指定作用在从坐标系上相对于基坐标系的力矩。该信号提供的力矩值等值反向地施加于基坐标系和从坐标系。选择此选项将显示附加参数，可用于启用输入端口。有关详细信息，请参阅 **Input** 部分。 |

### **Resolution Frame** — 用于分解驱动力矩的坐标系 `Base`（默认）| `Follower`

用于分解输入驱动力矩的坐标系，指定为 `Base` 或 `Follower`。

#### 传感

### **Resolution Frame** — 用于分解传感输出的坐标系 `Base`（默认）| `Follower`

用于分解传感输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的更多信息，请参阅 **Output** 部分。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置来感测力或力矩。 |
| `Normal` | 正常模式启用自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关更多信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩传感

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块感测基坐标系施加在从坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关更多信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 该模块在基座坐标系的坐标中解析测量值。
- `Follower` — 该模块在从动坐标系的坐标中解析测量值。

该参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。
## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障

您现在可以为所有关节模块建模模式故障。使用这些故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

Joint allows 3-D rotations

Spherical Joint 模块在两个坐标系之间提供三个旋转自由度。从动坐标系可以相对于基座坐标系具有任意 3-D 旋转。在仿真期间，基座坐标系和从动坐标系的原点保持重合，如图所示。

Joint Transformation Sequence of Spherical joint

与万向节不同，Spherical Joint 不具有运动学奇异。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。目标在基座坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定先满足哪些目标以及满足的程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数来建模能量耗散，使用 **Spring Stiffness** 参数来建模能量存储。关节弹簧试图将关节基元从其平衡位置移开，而关节阻尼器则充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限制，请使用 **Limits** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击该关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击“在模块图标上添加故障”按钮以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在属性检查器的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅设置故障触发器。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用故障表。有关更多详细信息，请参阅访问故障表和故障仪表板。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用仿真数据检查器。此外，您可以在故障仪表板中查看故障状态和已触发故障的摘要。要打开故障仪表板，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink 故障控制和 Simscape 故障接口的函数部分。
