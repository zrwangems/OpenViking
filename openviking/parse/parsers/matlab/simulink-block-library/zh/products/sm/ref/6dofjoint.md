---
type: simulink-block
title: '6-DOF Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Joints / Joints with Multiple Primitives'
documentation_page: '6dofjoint'
documentation_source_path: 'ref/6dofjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# 6-DOF Joint

## 端口

### 坐标系

### **B** — 基坐标系 frame

关节模块的基坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。

### 输入

#### X Prismatic Primitive (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *x* 轴，对关节的基坐标系和从动坐标系等量且反向地施加该力。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对基坐标系沿基坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Y Prismatic Primitive (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *y* 轴，对关节的基坐标系和从动坐标系等量且反向地施加该力。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对基坐标系沿基坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Z Prismatic Primitive (Pz)

### **fz** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *z* 轴，对关节的基坐标系和从动坐标系等量且反向地施加该力。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **pz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对基坐标系沿基坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Spherical Primitive (S)

### **tx** — 关于解析坐标系 `x` 轴的驱动力矩物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解析坐标系 *x* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (X)**。

### **ty** — 关于解析坐标系 `y` 轴的驱动力矩物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解析坐标系 *y* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Y)**。

### **tz** — 关于解析坐标系 `z` 轴的驱动力矩物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解析坐标系 *z* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`，并选择 **Torque (Z)**。

### **t** — 驱动力矩向量物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为向量格式，表示关于在解析坐标系中指定的任意轴 [*x* *y* *z*] 的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`，并选择 **Torque (XYZ)**。

#### Mode Configuration

### **mode** — 关节模式控制物理信号

输入端口，控制关节的模式。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。可在仿真期间随时更改模式。

下表显示关节在模式之间转换期间位置和速度如何变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal to Locked | 关节位置保留当前值，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |
| Normal to Disengaged | 关节位置保留当前值，但转换后可沿任意方向变化。 | 关节速度保留当前值，但转换后可沿任意方向变化。 |
| Locked to Normal | 关节位置保留当前值，但转换后可沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但转换后可沿与关节自由度 (DOFs) 对齐的方向变化。 |
| Locked to Disengaged | 关节位置保留当前值，但转换后可沿任意方向变化。 | 关节速度保持为零，但转换后可沿任意方向变化。 |
| Disengaged to Normal | 对于与关节自由度 (DOFs) 对齐的方向，关节位置初始采用通过使用牛顿法计算的值，并可此后变化。在受约束方向上，关节位置变为零，并在转换后保持不变。 | 对于与关节自由度 (DOFs) 对齐的方向，关节速度初始采用通过使用牛顿法计算的值，并可此后变化。在受约束方向上，关节速度变为零，并在转换后保持不变。 |
| Disengaged to Locked | 对于与关节自由度 (DOFs) 对齐的方向，关节位置初始采用通过使用牛顿法计算的值，并在转换后保持不变。在受约束方向上，关节位置变为零，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。

### 输出

#### X Prismatic Primitive (Px)

### **px** — 基元位置物理信号

物理信号端口，输出关节基元的位置。该值是从动坐标系相对基坐标系在基坐标系 *x* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Position**。

### **vx** — 基元速度物理信号

物理信号端口，输出关节基元的速度。该值是端口 **px** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Velocity**。

### **ax** — 基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值是端口 **px** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Acceleration**。

### **fx** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Actuator Force**。

### **fllx** — 下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Y Prismatic Primitive (Py)

### **py** — 基元位置物理信号

物理信号端口，输出关节基元的位置。该值是从动坐标系相对基坐标系在基坐标系 *y* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Position**。

### **vy** — 基元速度物理信号

物理信号端口，输出关节基元的速度。该值是端口 **py** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Velocity**。

### **ay** — 基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值是端口 **py** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Acceleration**。

### **fy** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Actuator Force**。

### **flly** — 下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Z Prismatic Primitive (Pz)

### **pz** — 关节基元位置物理信号

物理信号端口，输出关节基元的位置。该值是从动坐标系相对基坐标系在基坐标系 *z* 轴上的位移。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **vz** — 关节基元速度物理信号

物理信号端口，输出关节基元的速度。该值是端口 **pz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **az** — 关节基元加速度物理信号

物理信号端口，输出关节基元的加速度。该值是端口 **pz** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **fz** — 作用在关节基元上的执行器力物理信号

物理信号端口，输出作用在关节基元上的执行器力。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节基元上的下限力物理信号

物理信号端口，输出下限力。当关节基元位置小于自由区域的下边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节基元上的上限力物理信号

物理信号端口，输出上限力。当关节基元位置超过自由区域的上边界时，该模块施加此力。该模块将力施加到关节基元的基坐标系和从动坐标系两者，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Spherical Primitive (S)

### **Q** — 四元数参数化中的相对姿态物理信号

从动坐标系相对基坐标系的姿态，以解析坐标系中的四元数参数化向量形式返回。有关更多信息，请参见 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 *X* 坐标物理信号

相对角速度的 *X* 坐标，以标量形式返回。该值在解析坐标系中分解。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 *Y* 坐标物理信号

相对角速度的 *Y* 坐标，以标量形式返回。该值在解析坐标系中分解。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 *Z* 坐标物理信号

相对角速度的 *Z* 坐标，以标量形式返回。该值在解析坐标系中分解。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度向量物理信号

相对角速度，以在解析坐标系中分解的 3-D 向量形式返回。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 相对角加速度的 *X* 坐标物理信号

相对角加速度的 *X* 坐标，返回为标量。该量等于从端口 **wx** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **加速度 (X)**。

### **by** — 相对角加速度的 *Y* 坐标物理信号

相对角加速度的 *Y* 坐标，返回为标量。该量等于从端口 **wy** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **加速度 (Y)**。

### **bz** — 相对角加速度的 *Z* 坐标物理信号

相对角加速度的 *Z* 坐标，返回为标量。该量等于从端口 **wz** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **加速度 (Z)**。

### **b** — 角加速度向量物理信号

相对角加速度，返回为在解析坐标系中解析的 3-D 向量。该量等于从端口 **w** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **加速度**。

### **tll** — 下限力矩幅值物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下限时，该模块施加此力矩。该力矩作用于关节基元的基础坐标系和从动坐标系，以使位置加速回到自由区域。

#### 依赖关系

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **带符号下限力矩幅值**。

### **tul** — 上限力矩幅值物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上限时，该模块施加此力矩。该力矩作用于关节基元的基础坐标系和从动坐标系，以使位置加速回到自由区域。

#### 依赖关系

要启用此端口，在

要启用此端口，在 **球面副基元 (S)** > **传感** 下，选择 **上限力矩**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出采用 3-by-1 向量格式，并表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，在 **复合力/力矩传感** 下，选择 **约束力**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出采用 3-by-1 向量格式，并表示围绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，在 **复合力/力矩传感** 下，选择 **约束力矩**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在连接的坐标系之间传递的所有力之和。输出采用 3-by-1 向量格式，并表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，在 **复合力/力矩传感** 下，选择 **总力**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在连接的坐标系之间传递的所有力矩之和。该力矩包括驱动、内力、限位和约束力矩。输出采用 3-by-1 向量格式，并表示围绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，在 **复合力/力矩传感** 下，选择 **总力矩**。

## 参数

### X 移动副基元 (Px)

#### 状态目标

### **指定位置目标** — 是否指定位置目标 `off` (默认) | `on`

选择此参数可指定 *x* 移动副基元的位置目标。

### **优先级** — 位置目标的优先级 `High (desired)` (默认) | `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅《多体装配的工作原理》中的“引导装配”部分。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **值** — 位置目标 0 `m` (默认) | 标量

*x* 移动副基元的位置目标，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **指定速度目标** — 是否指定线性速度目标 `off` (默认) | `on`

选择此参数可指定 *x* 移动副基元的线性速度目标。

### **优先级** — 线性速度目标的优先级 `High (desired)` (默认) | `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅《多体装配的工作原理》中的“引导装配”部分。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

### **值** — 速度目标 0 `m/s` (默认) | 标量

*x* 移动副基元的线性速度目标，指定为以线性速度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

#### 内部力学

### **平衡位置** — 内力为零时的位置 0 `m` (默认) | 标量

弹簧力为零时的位置，指定为以长度单位表示的标量。

### **弹簧刚度** — 力定律的刚度 0 `N/m` (默认) | 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度单位表示的标量。

### **阻尼系数** — 力定律的阻尼系数 0 `N(m/s)` (默认) | 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 限位

### **指定下限** — 是否指定下限位置 `off` (默认) | `on`

选择此参数可指定 *x* 移动副基元的下限。

### **边界** — 自由区域的下限 -1 `m` (默认) | 标量

*x* 移动副基元自由区域的下限，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **弹簧刚度** — 下限处的弹簧刚度 1e6 `N/m` (默认) | 标量

下限处的弹簧刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **阻尼系数** — 下限处的阻尼系数 1e3 `N/(m/s)` (默认) | 标量

下限处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **过渡区域宽度** — 平滑弹簧力和阻尼力的区域 1e-4 `m` (默认) | 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **指定上限** — 是否指定上限位置 `off` (默认) | `on`

选择此参数可指定 *x* 移动副基元的上限。

### **边界** — 自由区域的上限 1 `m` (默认) | 标量

关节基元自由区域的上限，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **弹簧刚度** — 上限处的弹簧刚度 1e6 `N/m` (默认) | 标量

上限处的弹簧刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **阻尼系数** — 上限处的阻尼系数 1e3 `N/(m/s)` (默认) | 标量

上限处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

### **过渡区域宽度** — 平滑弹簧力和阻尼力的区域 1e-4 `m` (默认) | 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透量达到过渡区域的宽度时，该模块施加上限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **指定上限**。

#### 驱动

### **力** — 提供执行器力的选项 `None` (默认) | `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fx** 指定 *x* 移动副基元的执行器力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **运动** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **运动** — 提供运动的选项 `Automatically Computed` (默认) | `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节基元运动。 |

### Y 移动副基元 (Py)

#### 状态目标

### **指定位置目标** — 是否指定位置目标 `off` (默认) | `on`

选择此参数可指定 *y* 移动副基元的位置目标。

### **优先级** — 位置目标的优先级 `High (desired)` (默认) | `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅《多体装配的工作原理》中的“引导装配”部分。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **值** — 位置目标 0 `m` (默认) | 标量

*y* 移动副基元的位置目标，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定位置目标**。

### **指定速度目标** — 是否指定线性速度目标 `off` (默认) | `on`

选择此参数可指定 *y* 移动副基元的线性速度目标。

### **优先级** — 线性速度目标的优先级 `High (desired)` (默认) | `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅《多体装配的工作原理》中的“引导装配”部分。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

### **值** — 速度目标 0 `m/s` (默认) | 标量

*y* 移动副基元的线性速度目标，指定为以线性速度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定速度目标**。

#### 内部力学

### **平衡位置** — 内力为零时的位置 0 `m` (默认) | 标量

弹簧力为零时的位置，指定为以长度单位表示的标量。

### **弹簧刚度** — 力定律的刚度 0 `N/m` (默认) | 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度单位表示的标量。

### **阻尼系数** — 力定律的阻尼系数 0 `N(m/s)` (默认) | 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 限位

### **指定下限** — 是否指定下限位置 `off` (默认) | `on`

选择此参数可指定 *y* 移动副基元的下限。

### **边界** — 自由区域的下限 -1 `m` (默认) | 标量

*y* 移动副基元自由区域的下限，指定为以长度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **弹簧刚度** — 下限处的弹簧刚度 1e6 `N/m` (默认) | 标量

下限处的弹簧刚度，指定为以线性刚度单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **阻尼系数** — 下限处的阻尼系数 1e3 `N/(m/s)` (默认) | 标量

下限处的阻尼系数，指定为以线性阻尼系数单位表示的标量。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **过渡区域宽度** — 平滑弹簧力和阻尼力的区域 1e-4 `m` (默认) | 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度单位表示的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **指定下限**。

### **指定上限** — 是否指定上限位置 `off` (默认) | `on`

选择此参数可指定 *y* 移动副基元的上限。

### **边界** — 自由区域的上限 1 `m` (默认) | 标量

关节基元自由区域的上限，指定为以长度单位表示的标量。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认） | scalar

上界处的弹簧刚度，指定为以线性刚度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认） | scalar

上界处的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认） | scalar

用于平滑弹簧和阻尼力的区域，指定为以长度为单位的 scalar。

当穿透量达到过渡区域宽度时，模块应用上限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认） | `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fy** 指定 *y* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认） | `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **py** 指定关节基元的运动。 |

### Z 移动副基元 (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认） | `on`

选择此参数以指定 *z* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认） | `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参见 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认） | scalar

*z* 移动副基元的位置目标，指定为以长度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线性速度目标 `off`（默认） | `on`

选择此参数以指定 *z* 移动副基元的线性速度目标。

### **Priority** — 线性速度目标的优先级 `High (desired)`（默认） | `Low (approximate)`

线性速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参见 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认） | scalar

*z* 移动副基元的线性速度目标，指定为以线性速度单位为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认） | scalar

弹簧力为零的位置，指定为以长度为单位的 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认） | scalar

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度为单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认） | scalar

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 限值

### **Specify Lower Limit** — 是否指定下位置限值 `off`（默认） | `on`

选择此参数以指定 *z* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认） | scalar

*z* 移动副基元自由区域的下界，指定为以长度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认） | scalar

下界处的弹簧刚度，指定为以线性刚度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认） | scalar

下界处的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认） | scalar

用于平滑弹簧和阻尼力的区域，指定为以长度为单位的 scalar。

当穿透量达到过渡区域宽度时，模块应用下限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置限值 `off`（默认） | `on`

选择此参数以指定 *z* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认） | scalar

关节基元自由区域的上界，指定为以长度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认） | scalar

上界处的弹簧刚度，指定为以线性刚度为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认） | scalar

上界处的阻尼系数，指定为以线性阻尼系数为单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认） | scalar

用于平滑弹簧和阻尼力的区域，指定为以长度为单位的 scalar。

当穿透量达到过渡区域宽度时，模块应用上限力的完整值。区域越小，力的开始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认） | `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fz** 指定 *z* 移动副基元的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认） | `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **pz** 指定关节基元的运动。 |

### 球面基元 (S)

#### 状态目标

### **Specify Position Target** — 是否指定相对方向目标 `off`（默认） | `on`

选择此参数以指定基座和从动坐标系之间相对方向的目标。

### **Priority** — 相对方向目标的优先级 `High (desired)`（默认） | `Low (approximate)`

相对方向目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参见 Guiding Assembly。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value > Method** — 指定相对方向目标的方法 `None`（默认） | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基座和从动坐标系之间相对方向目标的方法。当将此参数设置为 `None` 时，方向目标使基座和从动坐标系对齐。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+X`（默认） | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Base** 参数设置的基座坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座和从动坐标系所选轴之间的对齐。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认） | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与 **Pair 1: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与 **Pair 2: Follower** 指定的从动坐标系对齐的基座坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基座坐标系旋转，以实现基座和从动坐标系所选轴之间的对齐。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的从动坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | scalar

相对旋转的角度，指定为 scalar。该角度表示从动坐标系相对于基座坐标系绕指定轴的旋转。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认） | 3-by1 vector

相对旋转的轴，指定为 3-by-1 单位 vector。该 vector 是无量纲的，表示在基座坐标系中分解的旋转轴。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | scalar

相对旋转的角度，指定为 scalar。该角度表示从动坐标系相对于基座坐标系绕 **Axis** 参数指定的轴的旋转。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 从动坐标系绕其轴旋转所围绕的坐标系 `Follower Axes`（默认） | `Base Axes`

从动坐标系绕其轴旋转所围绕的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，从动坐标系绕自身轴旋转，并且从动坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，从动坐标系绕固定基座坐标系轴旋转。有关更多信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴顺序 `X-Y-X`（默认） | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴顺序。有关更多信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 旋转序列参数化的角度 [0 0 0] `deg`（默认） | 1-by-3 vector

旋转序列参数化的角度，指定为 1-by-3 vector。有关更多信息，请参见 Rotation Sequence Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Rotation Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认） | 3-by-3 matrix

相对旋转，指定为将 vector 从从动坐标系映射到基座坐标系的 3-by-3 matrix。该 matrix 必须正交且行列式为 1。有关更多信息，请参见 Rotational Measurements。

#### 依赖项

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认） | unit quaternion vector

相对旋转，指定为 unit quaternion vector。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Quaternion`。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认） | `on`

选择此参数以指定球面基元的角速度目标。

### **Priority** — 角速度目标的优先级 `High (desired)`（默认） | `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 球面基元的角速度目标 [0 0 0] `deg/s`（默认） | 1-by-3 vector

球面基元的角速度目标，指定为在 resolution frame 中解析的 1-by-3 vector。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Resolution Frame** — 用于解析指定角速度目标的坐标系 `Base`（默认） | `Follower`

用于解析指定角速度目标的坐标系，指定为以下之一：

- `Base` — 关节模块在基座坐标系的坐标中解析角速度目标。
- `Follower` — 关节模块在从动坐标系的坐标中解析角速度目标。

#### 内部力学

### **Equilibrium Position > Method** — 指定平衡坐标系的方法 `None`（默认） | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基座坐标系的方向的方法。在整个仿真过程中，平衡坐标系保持相对于基座坐标系固定。当您将该参数设置为 `None` 时，平衡坐标系与基座坐标系对齐。

当从动坐标系与平衡坐标系对齐时，球面基元的弹簧扭矩为零。

### **Pair 1: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+X`（默认） | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与 **Pair 1: Base** 参数设置的基座坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系与平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基座坐标系轴 `+Y`（默认） | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与 **Pair 1: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基座坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与 **Pair 2: Follower** 指定的平衡坐标系对齐的基座坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基座坐标系旋转，以实现基座坐标系与平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基座坐标系轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的平衡坐标系轴与之对齐的基座坐标系轴，指定为基座坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认） | `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基座坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | scalar

相对旋转的角度，指定为 scalar。该角度表示平衡坐标系绕指定轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认） | 3-by1 vector

相对旋转的轴，指定为 3-by-1 unit vector。该向量无量纲，并指示在基座坐标系中解析的旋转轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认） | scalar

相对旋转的角度，指定为 scalar。该角度表示平衡坐标系绕 **Axis** 参数指定的轴相对于基座坐标系的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 绕其轴旋转平衡坐标系的坐标系 `Follower Axes`（默认） | `Base Axes`

用于绕其轴旋转平衡坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则平衡坐标系绕其自身轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则平衡坐标系绕固定的基座坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认） | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Angles** — 基本旋转的角度 [0 0 0] `deg`（默认） | 1-by-3 vector

基本旋转的角度，指定为 1-by-3 vector。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Sequence`。

### **Matrix** — 使用旋转矩阵的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认） | 3-by-3 matrix

相对旋转，指定为 3-by-3 matrix。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认） | unit quaternion vector

相对旋转，指定为 unit quaternion vector。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下，将 **Method** 参数设置为 `Quaternion`。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认） | scalar

球面基元的内部弹簧-阻尼力律的刚度，指定为具有旋转刚度单位的 scalar。

弹簧尝试拉动从动坐标系，使从动坐标系与指定的平衡坐标系对齐。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认） | scalar

球面基元的内部弹簧-阻尼力律的阻尼系数，指定为具有旋转阻尼系数单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认） | `on`

选择此参数以指定球面基元的下限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的移动。

### **Bound** — 自由区域的下界 15 `deg`（默认） | scalar

球面基元自由区域的下界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处的弹簧刚度 1e4 `N*m/deg`（默认） | scalar

下限处的弹簧刚度，指定为具有旋转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 10 `N*m/(deg/s)`（默认） | scalar

下限处的阻尼系数，指定为具有旋转阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认） | scalar

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的 scalar。

当穿透达到过渡区域的宽度时，模块施加下限扭矩的完整值。该区域越小，扭矩的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认） | `on`

选择此参数以指定球面基元的上限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的移动。

### **Bound** — 自由区域的上界 45 `deg`（默认） | scalar

球面基元自由区域的上界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处的弹簧刚度 1e4 `N*m/deg`（默认） | scalar

上限处的弹簧刚度，指定为具有刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 10 `N*m/(deg/s)`（默认） | scalar

上限处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认） | scalar

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的 scalar。

当穿透达到过渡区域的宽度时，模块施加上限扭矩的完整值。该区域越小，扭矩的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 用于提供驱动扭矩的选项 `None`（默认） | `Provided by Input`

用于为球面基元提供驱动扭矩的选项，指定为以下值之一。

| 驱动扭矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动扭矩。 |
| `Provided by Input` | 基于物理信号施加驱动扭矩。该信号指定作用在从动坐标系上相对于基座坐标系的扭矩。该信号提供的扭矩值以大小相等、方向相反的方式施加到基座坐标系和从动坐标系。选择此选项会显示可用于启用输入端口的附加参数。有关详细信息，请参阅 **输入** 部分。 |

### **Resolution Frame** — 用于解析驱动扭矩的坐标系 `Base`（默认） | `Follower`

用于解析输入驱动扭矩的坐标系，指定为 `Base` 或 `Follower`。

#### 感测

### **Resolution Frame** — 用于解析感测输出的坐标系 `Base`（默认） | `Follower`

用于解析感测输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的详细信息，请参阅 **输出** 部分。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认） | `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| Mode | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度 (DOFs)。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **内部力学**、**限制** 和 **驱动** 参数的设置感测力或扭矩。 |
| `Normal` | 正常模式在仿真期间按预期启用关节的自由度和约束。 |
| `Disengaged` | 脱离模式在仿真期间释放关节的所有约束。**内部力学**、**限制** 和 **驱动** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **输入** 部分中的端口 **mode**。 |

### 复合力/力矩感测

### **Direction** — 测量方向 `Follower on Base`（默认） | `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基座坐标系上的力和扭矩。
- `Base on Follower` — 模块感测基座坐标系施加在从动坐标系上的力和扭矩。

此参数仅影响 **复合力/力矩感测** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base`（默认） | `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 模块在基座坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **复合力/力矩感测** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障建模

现在，您可以为所有关节模块对模式故障建模。使用这些故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有六个自由度且无运动学奇异性的关节

6-DOF Joint block 提供三个平移和三个转动自由度。follower frame 可以相对于 base frame 具有 3-D 变换。该变换包含三个顺序平移和编码为四元数的 3-D 旋转。四元数不具有运动学奇异性。

沿 base 的 x、y 和 z 轴有三个平移自由度 DOF，围绕平移后形成的 follower 的 x、y 和 z 轴有三个转动自由度 DOF

这些平移分别沿基础坐标系的 *x*、*y* 和 *z* 轴。在旋转之前，从动坐标系的轴与基础坐标系的对应轴平行。3-D 旋转是相对于平移后形成的从动坐标系进行的。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。这些目标在基础坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将确定首先满足哪些目标以及满足它们的接近程度。有关示例，请参见 How Multibody Assembly Works 的 Guiding Assembly 部分。

要对关节基元的阻尼和弹簧行为建模，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数对能量耗散建模，使用 **Spring Stiffness** 参数对能量存储建模。关节弹簧试图使关节基元偏离其平衡位置，而关节阻尼器充当能量耗散元件。弹簧和阻尼器是严格线性的。

要指定关节基元的限值，请使用 **Limits** 下的参数。下限和上限定义自由区域的宽度。当位置超出边界时，该模块施加力以使关节位置加速回到自由区域。该模块使用平滑弹簧-阻尼器方法计算该力。有关平滑弹簧-阻尼器方法的详细信息，请参见 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参见 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如 position、velocity、acceleration、force 和 torque，您可以使用这些数据对模型执行分析任务。有关详细信息，请参见 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参见 **端口** 和 **参数** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入将覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为脱开状态。

要向关节模块添加模式故障，请点击该关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 来添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

添加故障时，在 Property Inspector 中，在 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参见 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参见 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真处于开启状态。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参见 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
