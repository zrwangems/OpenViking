---
type: simulink-block
title: 'Telescoping Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'telescopingjoint'
documentation_source_path: 'ref/telescopingjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Telescoping Joint

## 端口
```yaml
ports:
- name: B
  summary: 基座坐标系 坐标系
  direction: input
- name: F
  summary: 从动坐标系 坐标系
  direction: input
- name: tx
  summary: 绕解算坐标系 *x* 轴的作用力矩 物理信号
  direction: input
- name: ty
  summary: 绕解算坐标系 *y* 轴的作用力矩 物理信号
  direction: input
- name: tz
  summary: 绕解算坐标系 *z* 轴的作用力矩 物理信号
  direction: input
- name: t
  summary: 作用力矩向量 物理信号
  direction: input
- name: fz
  summary: 作用力 物理信号
  direction: input
- name: pz
  summary: 运动轮廓 物理信号
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
- name: pz
  summary: 关节基元位置物理信号
  direction: output
- name: vz
  summary: 关节基元速度物理信号
  direction: output
- name: az
  summary: 关节基元加速度物理信号
  direction: output
- name: fz
  summary: 作用在关节基元上的执行器力物理信号
  direction: output
- name: fllz
  summary: 作用在关节基元上的下限力物理信号
  direction: output
- name: fulz
  summary: 作用在关节基元上的上限力物理信号
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

### **B** — 基座坐标系 坐标系

关节模块的基座坐标系。

### **F** — 从动坐标系 坐标系

关节模块的从动坐标系。
### 输入

#### 球面原语 (S)

### **tx** — 绕解算坐标系 *x* 轴的作用力矩 物理信号

物理信号输入端口，接受球面原语的作用力矩。该信号为标量格式，表示绕解算坐标系 *x* 轴的作用力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (X)**。

### **ty** — 绕解算坐标系 *y* 轴的作用力矩 物理信号

物理信号输入端口，接受球面原语的作用力矩。该信号为标量格式，表示绕解算坐标系 *y* 轴的作用力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (Y)**。

### **tz** — 绕解算坐标系 *z* 轴的作用力矩 物理信号

物理信号输入端口，接受球面原语的作用力矩。该信号为标量格式，表示绕解算坐标系 *z* 轴的作用力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input` 并选择 **Torque (Z)**。

### **t** — 作用力矩向量 物理信号

物理信号输入端口，接受球面原语的作用力矩。该向量表示在基座坐标系和从动坐标系之间施加的作用力矩，以解算坐标系表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input` 并选择 **Torque (XYZ)**。

#### Z 移动副原语 (Pz)

### **fz** — 作用力 物理信号

物理信号输入端口，接受关节原语的作用力。该模块沿基座坐标系的 *z* 轴将此外力等大反向地施加到关节的基座坐标系和从动坐标系上。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **pz** — 运动轮廓 物理信号

物理信号输入端口，接受关节原语的运动轮廓。该模块使用此信号确定从动坐标系相对于基座坐标系沿基座坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。你可以在仿真过程中的任意时刻更改模式。

下表显示了关节在模式之间转换时位置和速度的变化方式。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| 正常到分离 | 关节位置保留当前值，但在转换后可沿任意方向变化。 | 关节速度保留当前值，但在转换后可沿任意方向变化。 |
| 锁定到正常 | 关节位置保留当前值，但在转换后可沿与关节自由度（DOF）对齐的方向变化。 | 关节速度保持为零，但在转换后可沿与关节 DOF 对齐的方向变化。 |
| 锁定到分离 | 关节位置保留当前值，但在转换后可沿任意方向变化。 | 关节速度保持为零，但在转换后可沿任意方向变化。 |
| 分离到正常 | 对于与关节 DOF 对齐的方向，关节位置最初取通过使用 Newton 方法计算得到的值，此后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOF 对齐的方向，关节速度最初取通过使用 Newton 方法计算得到的值，此后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| 分离到锁定 | 对于与关节 DOF 对齐的方向，关节位置最初取通过使用 Newton 方法计算得到的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### Spherical Primitive (S)

### **Q** — 四元数参数化下的相对姿态物理信号

从动坐标系相对于基坐标系的姿态，返回为单位四元数。有关详细信息，请参阅 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 `x` 坐标物理信号

相对角速度的 *x* 坐标，返回为标量。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 `y` 坐标物理信号

相对角速度的 *y* 坐标，返回为标量。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 `z` 坐标物理信号

相对角速度的 *z* 坐标，返回为标量。该值在 resolution frame 中解析。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度向量物理信号

相对角速度，返回为在 resolution frame 中解析的 3-D 向量。

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

相对角加速度，以在解析坐标系中表示的 3-D 矢量形式返回。该量等于从端口 **w** 导出的信号的时间导数。

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

#### Z Prismatic Primitive (Pz)

### **pz** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值为从动坐标系相对于基础坐标系在基础坐标系 *z* 轴方向上的位移。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **vz** — 关节基元速度物理信号

输出关节基元速度的物理信号端口。该值为从端口 **pz** 导出的信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **az** — 关节基元加速度物理信号

输出关节基元加速度的物理信号端口。该值为从端口 **pz** 导出的信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **fz** — 作用在关节基元上的执行器力物理信号

输出作用在关节基元上的执行器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节基元上的下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置返回自由区域。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节基元上的上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置返回自由区域。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连坐标系之间传递的所有力之和。输出为 3×1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，该图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括驱动力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在相连坐标系之间传递的所有力矩之和。力矩包括驱动、内力、限位和约束力矩。输出为 3×1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。
## 参数
```yaml
parameters:
- name: Specify Position Target
  summary: 是否指定相对方向目标 off（默认）| on
  group: Spherical Primitive (S)
- name: Priority
  summary: 相对方向目标的优先级 High (desired)（默认）| Low (approximate)
  group: Spherical Primitive (S)
- name: Value > Method
  summary: 指定相对方向目标的方法 None（默认）| Aligned Axes | Standard Axis | Arbitrary Axis | Rotation Sequence | Rotation Matrix | Quaternion
  group: Spherical Primitive (S)
- name: 'Pair 1: Follower'
  summary: 用于与指定基座坐标系轴对齐的从动坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 1: Base'
  summary: 基座坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 2: Follower'
  summary: 用于与指定基座坐标系轴对齐的从动坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair2: Base'
  summary: 基座坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: Spherical Primitive (S)
- name: Axis
  summary: 相对旋转的标准轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: Spherical Primitive (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Axis
  summary: 相对旋转的轴 [0 0 1]（默认）| 3×1 向量
  group: Spherical Primitive (S)
- name: Angle
  summary: 相对旋转角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Rotation About
  summary: 从动坐标系绕其轴旋转的坐标系 Follower Axes（默认）| Base Axes
  group: Spherical Primitive (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: Spherical Primitive (S)
- name: Angles
  summary: 旋转序列参数化的角度 [0 0 0] deg（默认）| 1×3 向量
  group: Spherical Primitive (S)
- name: Rotation Matrix
  summary: 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: Spherical Primitive (S)
- name: Quaternion
  summary: 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
  group: Spherical Primitive (S)
- name: Specify Velocity Target
  summary: 是否指定角速度目标 off（默认）| on
  group: Spherical Primitive (S)
- name: Priority
  summary: 角速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Spherical Primitive (S)
- name: Value
  summary: 球面基元的角速度目标 [0 0 0] deg/s（默认）| 1×3 向量
  group: Spherical Primitive (S)
- name: Resolution Frame
  summary: 用于解析指定角速度目标的坐标系 Base（默认）| Follower
  group: Spherical Primitive (S)
- name: Equilibrium Position > Method
  summary: 用于指定平衡坐标系的方法 None（默认）| Aligned Axes | Standard Axis | Arbitrary Axis | Rotation Sequence | Rotation Matrix | Quaternion
  group: Spherical Primitive (S)
- name: 'Pair 1: Follower'
  summary: 用于与指定基座坐标系轴对齐的平衡坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 1: Base'
  summary: 基座坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 2: Follower'
  summary: 用于与指定基座坐标系轴对齐的平衡坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair2: Base'
  summary: 基座坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: Spherical Primitive (S)
- name: Axis
  summary: 相对旋转的标准轴 +Z（默认）| +X | -X | +Y | -Y | -Z
  group: Spherical Primitive (S)
- name: Angle
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Axis
  summary: 相对旋转的轴 [0 0 1]（默认）| 3×1 向量
  group: Spherical Primitive (S)
- name: Angle
  summary: 相对旋转角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Rotation About
  summary: 平衡坐标系绕其轴旋转的坐标系 Follower Axes（默认）| Base Axes
  group: Spherical Primitive (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: Spherical Primitive (S)
- name: Angles
  summary: 基本旋转的角度 [0 0 0] deg（默认）| 1×3 向量
  group: Spherical Primitive (S)
- name: Matrix
  summary: 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: Spherical Primitive (S)
- name: Quaternion
  summary: 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
  group: Spherical Primitive (S)
- name: Spring Stiffness
  summary: 力律的刚度 0 N*m/deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N*m/(deg/s)（默认）| 标量
  group: Spherical Primitive (S)
- name: Specify Lower Limit
  summary: 是否指定下限位置限制 off（默认）| on
  group: Spherical Primitive (S)
- name: Bound
  summary: 自由区域的下界 15 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Spring Stiffness
  summary: 下界处弹簧的刚度 1e4 N*m/deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Spherical Primitive (S)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Specify Upper Limit
  summary: 是否指定上位置限位 off（默认）| on
  group: Spherical Primitive (S)
- name: Bound
  summary: 自由区域的上界 45 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Spherical Primitive (S)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Torque
  summary: 提供驱动力矩的选项 None（默认）| Provided by Input
  group: Spherical Primitive (S)
- name: Resolution Frame
  summary: 用于解析驱动力矩的坐标系 Base（默认）| Follower
  group: Spherical Primitive (S)
- name: Resolution Frame
  summary: 用于解析传感输出的坐标系 Base（默认）| Follower
  group: Spherical Primitive (S)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: Value
  summary: 位置目标 0 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Specify Velocity Target
  summary: 是否指定线速度目标 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Priority
  summary: 线速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: Value
  summary: 速度目标 0 m/s（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Equilibrium Position
  summary: 内力为零时的位置 0 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 力律的刚度 0 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Specify Lower Limit
  summary: 是否指定下限位置 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: 自由区域的下界 -1 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 下限处弹簧的刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 下限处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: 用于平滑弹簧力和阻尼力的区域 1e-4 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Specify Upper Limit
  summary: 是否指定位置上限 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: 自由区域的上界 1 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 上界处弹簧的刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Force
  summary: 提供驱动力力的选项 None（默认）| Provided by Input | Automatically Computed
  group: Z Prismatic Primitive (Pz)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Z Prismatic Primitive (Pz)
- name: Mode
  summary: 关节模式 Normal（默认）| Locked | Disengaged | Provided by Input
  group: 模式配置
- name: Direction
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: Composite Force/Torque Sensing
- name: Resolution Frame
  summary: 用于解析测量的坐标系 Base（默认）| Follower
  group: Composite Force/Torque Sensing
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### Spherical Primitive (S)

#### 状态目标

### **Specify Position Target** — 是否指定相对方向目标 `off`（默认）| `on`

选择此参数以指定基座坐标系和从动坐标系之间相对方向的目标。

### **Priority** — 相对方向目标的优先级 `High (desired)`（默认）| `Low (approximate)`

相对方向目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value > Method** — 指定相对方向目标的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基座坐标系与从动坐标系之间相对方向目标的方法。
当您将该参数设置为 `None` 时，方向目标将使基座坐标系与从动坐标系对齐。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基座坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座坐标系与从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 2: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座坐标系与从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于使 **Pair2: Follower** 参数中设置的从动坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系相对于基座坐标系绕指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基座坐标系中表示的旋转轴。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系相对于基础坐标系绕 **Axis** 参数所指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 从动坐标系绕其轴旋转的坐标系 `Follower Axes`（默认）| `Base Axes`

从动坐标系绕其轴旋转所围绕的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则从动坐标系绕其自身轴旋转，并且从动坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则从动坐标系绕固定的基础坐标系轴旋转。有关更多信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关更多信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 旋转序列参数化的角度 [0 0 0] `deg`（默认）| 1×3 向量

旋转序列参数化的角度，指定为 1×3 向量。有关更多信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Rotation Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为将向量从从动坐标系映射到基础坐标系的 3×3 矩阵。该矩阵必须正交且行列式为 1。有关更多信息，请参阅 Rotational Measurements。

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

### **Resolution Frame** — 用于解析指定角速度目标的坐标系 `Base`（默认）| `Follower`

用于解析指定角速度目标的坐标系，指定为以下选项之一：

- `Base` — 关节模块在基座坐标系中解析角速度目标。
- `Follower` — 关节模块在从动坐标系中解析角速度目标。

#### 内部机制

### **Equilibrium Position > Method** — 用于指定平衡坐标系的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基座坐标系方向的方法。平衡坐标系在整个仿真过程中相对于基座坐标系保持固定。当您将该参数设置为 `None` 时，平衡坐标系与基座坐标系对齐。

当从动坐标系和平衡坐标系对齐时，球面基元的弹簧力矩为零。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Base** 参数设置的基座坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

用于与 **Pair 2: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

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

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基座坐标系中解析的旋转轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系相对于基础坐标系绕 **Axis** 参数所指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 平衡坐标系绕其轴旋转的坐标系 `Follower Axes`（默认）| `Base Axes`

平衡坐标系绕其轴旋转的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则平衡坐标系绕其自身轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则平衡坐标系绕固定的基础坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

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

弹簧试图拉动从动坐标系，使从动坐标系与指定的平衡坐标系对齐。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

球面基元内部弹簧-阻尼力律的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置限制 `off`（默认）| `on`

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

当穿透量达到过渡区域的宽度时，模块施加下界扭矩的完整值。该区域越小，扭矩的出现越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限位 `off`（默认）| `on`

选择此参数以指定球面基元的上限。关节限位使用弹簧-阻尼器来抵抗超出范围边界的运动。

### **Bound** — 自由区域的上界 45 `deg`（默认）| 标量

球面基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

上界处的弹簧刚度，指定为具有刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加上界扭矩的完整值。该区域越小，扭矩的出现越急剧，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input`

为球面基元提供驱动力矩的选项，指定为以下值之一。

| 驱动力矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动力矩。 |
| `Provided by Input` | 基于物理信号施加驱动力矩。该信号指定作用在从坐标系上相对于基坐标系的力矩。该信号提供的力矩值等值且反向地施加到基坐标系和从坐标系上。选择此选项会显示可用于启用输入端的附加参数。有关详细信息，请参阅 **Input** 部分。 |

### **Resolution Frame** — 用于解析驱动力矩的坐标系 `Base`（默认）| `Follower`

用于解析输入驱动力矩的坐标系，指定为 `Base` 或 `Follower`。

#### 传感

### **Resolution Frame** — 用于解析传感输出的坐标系 `Base`（默认）| `Follower`

用于解析传感输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的详细信息，请参阅 **Output** 部分。

### Z Prismatic Primitive (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。
有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 一节。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*z* 移动副基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 一节。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*z* 移动副基元的线速度目标，指定为以线速度单位为单位的标量。

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

选择此参数以指定 *z* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*z* 移动副基元自由区域的下界，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处弹簧的刚度 1e6 `N/m`（默认）| 标量

下限处弹簧的刚度，指定为以线性刚度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下限处的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，模块施加完整的下限力值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，指定为以长度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| 标量

上界处弹簧的刚度，指定为以线性刚度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度为单位的标量。

当穿透深度达到过渡区域的宽度时，模块施加完整的上限力值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供驱动力力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供驱动力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无驱动力。 |
| `Provided by Input` | 输入端口 **fz** 指定 *z* 移动副基元的驱动力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **pz** 指定关节基元的运动。 |

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### Composite Force/Torque Sensing

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块检测从动坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块检测基坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基坐标系的坐标中解析测量值。
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

### R2025a：模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

具有一个球面副和一个移动副的关节

伸缩关节模块在两个坐标系之间提供三个旋转自由度和一个平移自由度，如下图所示。

伸缩关节的关节变换序列

从动坐标系可以通过相对于基础坐标系进行三维旋转，然后沿从动坐标系的 *z* 轴平移来进行变换。图中显示了在给定仿真时间步中关节变换发生的顺序。

伸缩关节的关节变换序列

三维旋转不存在运动学奇异性，因为旋转以四元数编码。

要指定关节原语初始状态的目标，请使用 **状态目标** 下的参数。目标在基础坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定首先满足哪些目标以及满足的程度。有关示例，请参阅多体装配工作原理的引导装配部分。

要对关节原语进行阻尼和弹簧行为建模，请使用 **内部力学** 下的参数。使用 **阻尼系数** 参数来建模能量耗散，使用 **弹簧刚度** 参数来建模能量存储。关节弹簧试图将关节原语从其平衡位置移开，关节阻尼器充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节原语的限制，请使用 **限制** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，模块施加力将关节位置加速回自由区域。模块使用平滑弹簧-阻尼方法计算力。有关平滑弹簧-阻尼方法的更多信息，请参阅空间接触力模块的描述部分。

**驱动** 部分中的 **力**、**力矩** 和 **运动** 参数控制仿真期间关节原语的运动。有关更多信息，请参阅指定关节驱动输入。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关更多信息，请参阅传感以及力和力矩传感。

要指定关节模式配置，请使用 **模式** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **模式配置**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡中的 **Faults** 部分，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
