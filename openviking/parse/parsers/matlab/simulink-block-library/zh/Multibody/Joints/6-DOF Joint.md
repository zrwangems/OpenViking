---
type: simulink-block
title: '6-DOF Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: '6dofjoint'
documentation_source_path: 'ref/6dofjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# 6-DOF Joint

## 端口
```yaml
ports:
- name: B
  summary: 基坐标系 frame
  direction: input
- name: F
  summary: 从坐标系 frame
  direction: input
- name: fx
  summary: 驱动力物理信号
  direction: input
- name: px
  summary: 运动轮廓物理信号
  direction: input
- name: fy
  summary: 驱动力物理信号
  direction: input
- name: py
  summary: 运动轮廓物理信号
  direction: input
- name: fz
  summary: 驱动力物理信号
  direction: input
- name: pz
  summary: 运动轮廓物理信号
  direction: input
- name: tx
  summary: 绕解算坐标系 x 轴的驱动力矩物理信号
  direction: input
- name: ty
  summary: 绕解算坐标系 y 轴的驱动力矩物理信号
  direction: input
- name: tz
  summary: 关于解算坐标系 z 轴的驱动力矩物理信号
  direction: input
- name: t
  summary: 驱动力矩矢量物理信号
  direction: input
- name: mode
  summary: 关节模式控制物理信号
  direction: input
- name: px
  summary: 基元位置物理信号
  direction: output
- name: vx
  summary: 基元速度物理信号
  direction: output
- name: ax
  summary: 原始物理信号加速度
  direction: output
- name: fx
  summary: 作用在关节原始上的执行器力物理信号
  direction: output
- name: fllx
  summary: 下限力物理信号
  direction: output
- name: fulx
  summary: 上限力物理信号
  direction: output
- name: py
  summary: 原始物理信号位置
  direction: output
- name: vy
  summary: 原始物理信号速度
  direction: output
- name: ay
  summary: 原始物理信号加速度
  direction: output
- name: fy
  summary: 作用在关节原始上的执行器力物理信号
  direction: output
- name: flly
  summary: 下限力物理信号
  direction: output
- name: fuly
  summary: 上限力物理信号
  direction: output
- name: pz
  summary: 关节原语位置的物理信号
  direction: output
- name: vz
  summary: 关节原语速度的物理信号
  direction: output
- name: az
  summary: 关节原语加速度的物理信号
  direction: output
- name: fz
  summary: 作用在关节原语上的致动器力的物理信号
  direction: output
- name: fllz
  summary: 作用在关节原语上的下限力的物理信号
  direction: output
- name: fulz
  summary: 作用在关节原语上的上限力的物理信号
  direction: output
- name: Q
  summary: 四元数参数化相对姿态的物理信号
  direction: output
- name: wx
  summary: 相对角速度的 *X* 坐标物理信号
  direction: output
- name: wy
  summary: 相对角速度的 *Y* 坐标物理信号
  direction: output
- name: wz
  summary: 相对角速度的 *Z* 坐标物理信号
  direction: output
- name: w
  summary: 角速度向量物理信号
  direction: output
- name: bx
  summary: 相对角加速度的 *X* 坐标物理信号
  direction: output
- name: by
  summary: 相对角加速度的 *Y* 坐标物理信号
  direction: output
- name: bz
  summary: 相对角加速度的 *Z* 坐标物理信号
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

### **B** — 基坐标系 frame

关节模块的基坐标系。

### **F** — 从坐标系 frame

关节模块的从坐标系。
### 输入

#### X 移动副基元 (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *x* 轴将力等大反向地施加到关节的基坐标系和从坐标系上。

#### 依赖

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从坐标系相对于基坐标系沿基坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Y 移动副基元 (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *y* 轴将此力等大反向地施加到关节的基坐标系和从坐标系上。

#### 依赖

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从坐标系相对于基坐标系沿基坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Z 移动副基元 (Pz)

### **fz** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基坐标系的 *z* 轴将此力等大反向地施加到关节的基坐标系和从坐标系上。

#### 依赖

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **pz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从坐标系相对于基坐标系沿基坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### 球面副基元 (S)

### **tx** — 绕解算坐标系 `x` 轴的驱动力矩物理信号

物理信号输入端口，接受球面副基元的驱动力矩。该信号为标量格式，表示绕解算坐标系 *x* 轴的力矩。

#### 依赖

要启用此端口，请在 **球面副基元 (S)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input` 并选择 **力矩 (X)**。

### **ty** — 绕解算坐标系 `y` 轴的驱动力矩物理信号

物理信号输入端口，接受球面副基元的驱动力矩。该信号为标量格式，表示绕解算坐标系 *y* 轴的力矩。

#### 依赖

要启用此端口，请在 **球面副基元 (S)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input` 并选择 **力矩 (Y)**。

### **tz** — 关于解算坐标系 `z` 轴的驱动力矩物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为标量格式，表示关于解算坐标系 *z* 轴的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Torque** 设置为 `Provided by
Input` 并选择 **Torque (Z)**。

### **t** — 驱动力矩矢量物理信号

物理信号输入端口，接受球面基元的驱动力矩。该信号为矢量格式，表示关于在解算坐标系中指定的任意轴 [*x* *y* *z*] 的力矩。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Actuation** 下，将 **Motion** 设置为 `Provided by
Input` 并选择 **Torque (XYZ)**。

#### 模式配置

### **mode** — 关节模式控制物理信号

控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，为脱离；当输入信号为 `1` 时，为锁定。您可以在仿真过程中的任意时刻更改模式。

下表显示了关节的位置和速度在模式切换期间的变化方式。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保持当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| 正常到脱离 | 关节位置保持当前值，但切换后可在任意方向上变化。 | 关节速度保持当前值，但切换后可在任意方向上变化。 |
| 锁定到正常 | 关节位置保持当前值，但切换后可在与关节自由度（DOF）对齐的方向上变化。 | 关节速度保持为零，但切换后可在与关节自由度对齐的方向上变化。 |
| 锁定到脱离 | 关节位置保持当前值，但切换后可在任意方向上变化。 | 关节速度保持为零，但切换后可在任意方向上变化。 |
| 脱离到正常 | 对于与关节自由度对齐的方向，关节位置初始取通过牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节自由度对齐的方向，关节速度初始取通过牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在切换后保持不变。 |
| 脱离到锁定 | 对于与关节自由度对齐的方向，关节位置初始取通过牛顿法计算的值，并在切换后保持不变。在约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### X Prismatic Primitive (Px)

### **px** — 基元位置物理信号

输出关节基元位置的物理信号端口。该值为从动坐标系相对于基坐标系在基坐标系 *x* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Position**。

### **vx** — 基元速度物理信号

输出关节基元速度的物理信号端口。该值为端口 **px** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Velocity**。

### **ax** — 原始物理信号加速度

输出关节原始加速度的物理信号端口。该值为来自端口 **px** 的信号二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Acceleration**。

### **fx** — 作用在关节原始上的执行器力物理信号

输出作用在关节原始上的执行器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Actuator Force**。

### **fllx** — 下限力物理信号

输出下限力的物理信号端口。当关节原始位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节原始的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

输出上限力的物理信号端口。当关节原始位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节原始的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Y Prismatic Primitive (Py)

### **py** — 原始物理信号位置

输出关节原始位置的物理信号端口。该值为从动坐标系相对于基座坐标系在基座坐标系 *y* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Position**。

### **vy** — 原始物理信号速度

输出关节原始速度的物理信号端口。该值为来自端口 **py** 的信号一阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Velocity**。

### **ay** — 原始物理信号加速度

输出关节原始加速度的物理信号端口。该值为来自端口 **py** 的信号二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Acceleration**。

### **fy** — 作用在关节原始上的执行器力物理信号

输出作用在关节原始上的执行器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Actuator Force**。

### **flly** — 下限力物理信号

输出下限力的物理信号端口。当关节原始位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节原始的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

输出上限力的物理信号端口。当关节原始位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节原始的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Z Prismatic Primitive (Pz)

### **pz** — 关节原语位置的物理信号

输出关节原语位置的物理信号端口。该值为从动坐标系相对于基础坐标系在基础坐标系 *z* 轴方向上的位移。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **vz** — 关节原语速度的物理信号

输出关节原语速度的物理信号端口。该值为端口 **pz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **az** — 关节原语加速度的物理信号

输出关节原语加速度的物理信号端口。该值为端口 **pz** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **fz** — 作用在关节原语上的致动器力的物理信号

输出作用在关节原语上的致动器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节原语上的下限力的物理信号

输出下限力的物理信号端口。当关节原语位置小于自由区域的下界时，该模块施加此力。该模块将此外力施加到关节原语的基础坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节原语上的上限力的物理信号

输出上限力的物理信号端口。当关节原语位置超过自由区域的上界时，该模块施加此力。该模块将此外力施加到关节原语的基础坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Spherical Primitive (S)

### **Q** — 四元数参数化相对姿态的物理信号

从动坐标系相对于基础坐标系的姿态，以解析坐标系中的四元数参数化向量形式返回。有关更多信息，请参阅 Quaternion Measurements。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Position**。

### **wx** — 相对角速度的 *X* 坐标物理信号

相对角速度的 *X* 坐标，以标量形式返回。该值在解析坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (X)**。

### **wy** — 相对角速度的 *Y* 坐标物理信号

相对角速度的 *Y* 坐标，以标量形式返回。该值在解析坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Y)**。

### **wz** — 相对角速度的 *Z* 坐标物理信号

相对角速度的 *Z* 坐标，以标量形式返回。该值在解析坐标系中表示。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity (Z)**。

### **w** — 角速度向量物理信号

相对角速度，以解析坐标系中的 3-D 向量形式返回。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 相对角加速度的 *X* 坐标物理信号

相对角加速度的 *X* 坐标，以标量形式返回。该量等于从端口 **wx** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (X)**。

### **by** — 相对角加速度的 *Y* 坐标物理信号

相对角加速度的 *Y* 坐标，以标量形式返回。该量等于从端口 **wy** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Y)**。

### **bz** — 相对角加速度的 *Z* 坐标物理信号

相对角加速度的 *Z* 坐标，以标量形式返回。该量等于从端口 **wz** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration (Z)**。

### **b** — 角加速度矢量物理信号

相对角加速度，以在解析坐标系中表示的 3-D 矢量形式返回。该量等于从端口 **w** 导出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Acceleration**。

### **tll** — 下限力矩幅值物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，模块施加该力矩。该力矩施加到关节基元的基座坐标系和从动坐标系两者上，以将位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Signed Lower-Limit Torque Magnitude**。

### **tul** — 上限力矩幅值物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，模块施加该力矩。该力矩施加到关节基元的基座坐标系和从动坐标系两者上，以将位置加速回自由区域。

#### 依赖关系

要启用此端口，请在

要启用此端口，请在 **Spherical Primitive (S)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 矢量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 矢量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连坐标系之间传递的所有力的总和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，图中展示了一个使用棱柱副模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在相连坐标系之间传递的所有力矩的总和。力矩包括执行、内力、限位和约束力矩。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩传感。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力矩**。
## 参数
```yaml
parameters:
- name: 指定位置目标
  summary: 是否指定位置目标 off（默认）| on
  group: X 棱柱基元 (Px)
- name: 优先级
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: X 棱柱基元 (Px)
- name: 值
  summary: 位置目标 0 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: 指定速度目标
  summary: 是否指定线速度目标 off（默认）| on
  group: X 棱柱基元 (Px)
- name: 优先级
  summary: 线速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: X 棱柱基元 (Px)
- name: 值
  summary: 速度目标 0 m/s（默认）| 标量
  group: X 棱柱基元 (Px)
- name: 平衡位置
  summary: 内力为零的位置 0 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: 弹簧刚度
  summary: 力定律的刚度 0 N/m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: 阻尼系数
  summary: 力定律的阻尼系数 0 N(m/s)（默认）| 标量
  group: X 棱柱基元 (Px)
- name: 指定下限
  summary: 是否指定下限位置 off（默认）| on
  group: X 棱柱基元 (Px)
- name: Bound
  summary: 自由区域的下界 -1 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Spring Stiffness
  summary: 下界处的弹簧刚度 1e6 N/m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Specify Upper Limit
  summary: 是否指定上位置极限 off（默认）| on
  group: X 棱柱基元 (Px)
- name: Bound
  summary: 自由区域的上界 1 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e6 N/m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: X 棱柱基元 (Px)
- name: Force
  summary: 提供致动力的选项 None（默认）| Provided by Input | Automatically Computed
  group: X 棱柱基元 (Px)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: X 棱柱基元 (Px)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: Y Prismatic Primitive (Py)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: Y Prismatic Primitive (Py)
- name: Value
  summary: 位置目标 0 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Specify Velocity Target
  summary: 是否指定线速度目标 off（默认）| on
  group: Y Prismatic Primitive (Py)
- name: Priority
  summary: 线速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Y Prismatic Primitive (Py)
- name: Value
  summary: 速度目标 0 m/s（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Equilibrium Position
  summary: 内力为零的位置 0 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Spring Stiffness
  summary: 力定律的刚度 0 N/m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Damping Coefficient
  summary: 力定律的阻尼系数 0 N(m/s)（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Specify Lower Limit
  summary: 是否指定下限位置 off（默认）| on
  group: Y Prismatic Primitive (Py)
- name: Bound
  summary: 自由区域的下界 -1 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Spring Stiffness
  summary: 下限处的弹簧刚度 1e6 N/m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Damping Coefficient
  summary: 下限处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Specify Upper Limit
  summary: 是否指定上限位置限制 off（默认）| on
  group: Y Prismatic Primitive (Py)
- name: Bound
  summary: 自由区域的上界 1 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e6 N/m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Force
  summary: 提供致动力的选项 None（默认）| Provided by Input | Automatically Computed
  group: Y Prismatic Primitive (Py)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Y Prismatic Primitive (Py)
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
  summary: 内力为零的位置 0 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 力定律的刚度 0 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 力定律的阻尼系数 0 N(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Specify Lower Limit
  summary: 是否指定下限位置 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: 自由区域的下界 -1 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 下限处的弹簧刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 下限处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Specify Upper Limit
  summary: 是否指定上限位置 off（默认）| on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: 自由区域的上界 1 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: 用于平滑弹簧力和阻尼力的区域 1e-4 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Force
  summary: 提供致动力的选项 None（默认）| Provided by Input | Automatically Computed
  group: Z Prismatic Primitive (Pz)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Z Prismatic Primitive (Pz)
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
  summary: 用于与指定基础坐标系轴对齐的从坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 1: Base'
  summary: 基础坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 2: Follower'
  summary: 用于与指定基础坐标系轴对齐的从坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair2: Base'
  summary: 基础坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
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
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Rotation About
  summary: 绕其轴旋转从坐标系的坐标系 Follower Axes（默认）| Base Axes
  group: Spherical Primitive (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: Spherical Primitive (S)
- name: Angles
  summary: 旋转序列参数化的角度 [0 0 0] deg（默认）| 1×3 向量
  group: Spherical Primitive (S)
- name: Rotation Matrix
  summary: 使用旋转矩阵表示的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: Spherical Primitive (S)
- name: Quaternion
  summary: 使用四元数表示的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
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
  summary: 用于解算指定角速度目标的坐标系 Base（默认）| Follower
  group: Spherical Primitive (S)
- name: Equilibrium Position > Method
  summary: 指定平衡坐标系的方法 None（默认）| Aligned Axes | Standard Axis | Arbitrary Axis | Rotation Sequence | Rotation Matrix | Quaternion
  group: Spherical Primitive (S)
- name: 'Pair 1: Follower'
  summary: 用于与指定基础坐标系轴对齐的平衡坐标系轴 +X（默认）| -X | +Y | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 1: Base'
  summary: 基础坐标系轴 +Y（默认）| +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair 2: Follower'
  summary: 用于与指定基础坐标系轴对齐的平衡坐标系轴 +Y | +X | -X | -Y | +Z | -Z
  group: Spherical Primitive (S)
- name: 'Pair2: Base'
  summary: 基础坐标系轴 +Z（默认）| +X | -X | +Y | -Y | -Z
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
  summary: 相对旋转的角度 0.0 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Rotation About
  summary: 绕其轴旋转平衡坐标系的坐标系 Follower Axes（默认）| Base Axes
  group: Spherical Primitive (S)
- name: Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: Spherical Primitive (S)
- name: Angles
  summary: 基本旋转的角度 [0 0 0] deg（默认）| 1×3 向量
  group: Spherical Primitive (S)
- name: Matrix
  summary: 使用旋转矩阵表示的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: Spherical Primitive (S)
- name: Quaternion
  summary: 使用四元数表示的相对旋转 [1 0 0 0]（默认）| 单位四元数向量
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
  summary: 下限处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Damping Coefficient
  summary: 下限处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Spherical Primitive (S)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Specify Upper Limit
  summary: 是否指定位置上限 off（默认）| on
  group: Spherical Primitive (S)
- name: Bound
  summary: 自由区域的上界 45 deg（默认）| 标量
  group: Spherical Primitive (S)
- name: Spring Stiffness
  summary: 上界处弹簧的刚度 1e4 N*m/deg（默认）| 标量
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

### X 棱柱基元 (Px)

#### 状态目标

### **指定位置目标** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 棱柱基元的位置目标。

### **优先级** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅多体装配工作原理中的引导装配部分。

#### 依赖关系

要启用此参数，请选择**指定位置目标**。

### **值** — 位置目标 0 `m`（默认）| 标量

*x* 棱柱基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择**指定位置目标**。

### **指定速度目标** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 棱柱基元的线速度目标。

### **优先级** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅多体装配工作原理中的引导装配部分。

#### 依赖关系

要启用此参数，请选择**指定速度目标**。

### **值** — 速度目标 0 `m/s`（默认）| 标量

*x* 棱柱基元的线速度目标，指定为以线速度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择**指定速度目标**。

#### 内部力学

### **平衡位置** — 内力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度单位为单位的标量。

### **弹簧刚度** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度单位为单位的标量。

### **阻尼系数** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 限位

### **指定下限** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *x* 棱柱基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*x* 移动副基元的自由区域下界，以长度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认）| 标量

下界处的弹簧刚度，以线性刚度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，以线性阻尼系数单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，以长度单位指定为标量。

当穿透量达到过渡区域的宽度时，模块施加下极限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上位置极限 `off`（默认）| `on`

选择此参数以指定 *x* 移动副基元的上极限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，以长度单位指定为标量。

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

当穿透量达到过渡区域的宽度时，模块施加上极限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供致动力的选项，指定为以下值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fx** 为 *x* 移动副基元指定致动力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| Motion Setting | Description |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节基元的运动。 |

### Y Prismatic Primitive (Py)

#### State Targets

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*y* 移动副基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*y* 移动副基元的线速度目标，指定为以线速度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### Internal Mechanics

### **Equilibrium Position** — 内力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度单位为单位的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度单位为单位的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### Limits

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

当穿透量达到过渡区域的宽度时，该模块施加下限力的完整值。该区域越小，力的出现越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置限制 `off`（默认）| `on`

选择此参数以指定 *y* 棱柱图元的运动上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节图元自由区域的上界，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| 标量

上界处的弹簧刚度，指定为以线性刚度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为以线性阻尼系数单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加上限力的完整值。该区域越小，力的出现越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### Actuation

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节图元提供致动力的选项，指定为以下值之一：

| Force Setting | Description |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fy** 为 *y* 棱柱图元指定致动力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节图元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节图元提供运动的选项，指定为以下值之一：

| Motion Setting | Description |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节图元运动。 |
| `Provided by Input` | 输入端口 **py** 为关节图元指定运动。 |

### Z Prismatic Primitive (Pz)

#### State Targets

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 棱柱图元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。
有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*z* 移动副基元的位置目标，指定为以长度为单位的标量。

#### 依赖

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*z* 移动副基元的线速度目标，指定为以线速度单位为单位的标量。

#### 依赖

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，指定为以长度为单位的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的刚度，指定为以线性刚度为单位的标量。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 限位

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*z* 移动副基元自由区域的下界，指定为以长度为单位的标量。

#### 依赖

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处的弹簧刚度 1e6 `N/m`（默认）| 标量

下限处的弹簧刚度，指定为以线性刚度为单位的标量。

#### 依赖

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下限处的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 依赖

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度为单位的标量。

当穿透深度达到过渡区域的宽度时，模块施加下限力的完整值。该区域越小，力的出现越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *z* 移动副基元的上限。

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

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，以长度单位指定为标量。

当穿透量达到过渡区域的宽度时，该模块施加完整的上限力值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节原语提供致动力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fz** 为 *z* 移动原语指定致动力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节原语提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节原语运动。 |
| `Provided by Input` | 输入端口 **pz** 为关节原语指定运动。 |

### Spherical Primitive (S)

#### 状态目标

### **Specify Position Target** — 是否指定相对方向目标 `off`（默认）| `on`

选择此参数以指定基座坐标系与从动坐标系之间相对方向的目标。

### **Priority** — 相对方向目标的优先级 `High (desired)`（默认）| `Low (approximate)`

相对方向目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value > Method** — 指定相对方向目标的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基座坐标系与从动坐标系之间相对方向目标的方法。当将此参数设置为 `None` 时，方向目标使基座坐标系与从动坐标系对齐。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Pair 1: Follower** — 用于与指定基础坐标系轴对齐的从坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基础坐标系轴对齐的从坐标系轴，指定为从坐标系的正交轴。从坐标系相对于基础坐标系旋转，以实现基础坐标系和从坐标系所选轴之间的对齐。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基础坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的从坐标系对齐的基础坐标系轴，指定为基础坐标系的正交轴。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基础坐标系轴对齐的从坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的从坐标系对齐的基础坐标系轴，指定为从坐标系的正交轴。从坐标系相对于基础坐标系旋转，以实现基础坐标系和从坐标系所选轴之间的对齐。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基础坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的从坐标系轴与之对齐的基础坐标系轴，指定为基础坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基础坐标系的正交轴。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从坐标系相对于基础坐标系绕指定轴的旋转。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基础坐标系中分解的旋转轴。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从坐标系相对于基础坐标系绕由 **Axis** 参数指定的轴的旋转。

#### 依赖

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 绕其轴旋转从坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

绕其轴旋转从坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则从坐标系绕其自身轴旋转，并且从坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则从坐标系绕固定的基础坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

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

### **Rotation Matrix** — 使用旋转矩阵表示的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为将向量从从动坐标系映射到基础坐标系的 3×3 矩阵。该矩阵必须为正交矩阵且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数表示的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为单位四元数向量。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Specify Position Target** > **Value** 下，将 **Method** 参数设置为 `Quaternion`。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定球面基元的角速度目标。

### **Priority** — 角速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 球面基元的角速度目标 [0 0 0] `deg/s`（默认）| 1×3 向量

球面基元的角速度目标，指定为在解算坐标系中解算的 1×3 向量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Resolution Frame** — 用于解算指定角速度目标的坐标系 `Base`（默认）| `Follower`

用于解算指定角速度目标的坐标系，指定为以下之一：

- `Base` — 关节模块在基础坐标系的坐标中解算角速度目标。
- `Follower` — 关节模块在从动坐标系的坐标中解算角速度目标。

#### 内部机制

### **Equilibrium Position > Method** — 指定平衡坐标系的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定平衡坐标系相对于基础坐标系方向的方法。平衡坐标系在整个仿真过程中相对于基础坐标系保持固定。当您将该参数设置为 `None` 时，平衡坐标系与基础坐标系对齐。

当从动坐标系和平衡坐标系对齐时，球面基元的弹簧力矩为零。

### **Pair 1: Follower** — 用于与指定基础坐标系轴对齐的平衡坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基础坐标系轴对齐的平衡坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基础坐标系旋转，以实现基础坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基础坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的平衡坐标系对齐的基础坐标系轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基础坐标系轴对齐的平衡坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的平衡坐标系对齐的基础坐标系轴，指定为平衡坐标系的正交轴。平衡坐标系相对于基础坐标系旋转，以实现基础坐标系和平衡坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基础坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于使 **Pair2: Follower** 参数中设置的平衡坐标系轴与之对齐的基础坐标系轴，指定为基础坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系相对于基础坐标系绕指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基础坐标系中分解的旋转轴。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示平衡坐标系相对于基础坐标系绕由 **Axis** 参数指定的轴的旋转。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 绕其轴旋转平衡坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

绕其轴旋转平衡坐标系的坐标系，指定为 `Follower Axes` 或 `Base Axes`。如果将该参数设置为 `Follower Axes`，则平衡坐标系绕其自身轴旋转，并且平衡坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base Axes`，则平衡坐标系绕固定的基础坐标系轴旋转。有关更多信息，请参阅 Rotational Measurements。

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

### **Matrix** — 使用旋转矩阵表示的相对旋转 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为 3×3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Equilibrium Position** 下将 **Method** 参数设置为 `Rotation Matrix`。

### **Quaternion** — 使用四元数表示的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

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

### **Spring Stiffness** — 下限处的弹簧刚度 1e4 `N*m/deg`（默认）| 标量

下限处的弹簧刚度，指定为具有旋转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下限处的阻尼系数，指定为具有旋转阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为具有角度单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限扭矩的完整值。区域越小，扭矩的出现越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定球面基元的上限。关节限制使用弹簧-阻尼器来抵抗超出范围边界的运动。

### **Bound** — 自由区域的上界 45 `deg`（默认）| 标量

球面基元自由区域的上界，指定为带角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

上界处弹簧的刚度，指定为带刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上界处的阻尼系数，指定为带阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为带角度单位的标量。

当穿透深度达到过渡区域的宽度时，该模块施加完整的上限扭矩值。该区域越小，扭矩的起始越急剧，求解器所需的时间步长也越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input`

为球面基元提供驱动力矩的选项，指定为以下值之一。

| 驱动力矩设置 | 描述 |
| --- | --- |
| `None` | 不施加驱动力矩。 |
| `Provided by Input` | 基于物理信号施加驱动力矩。该信号指定作用在从坐标系上相对于基坐标系的力矩。该信号提供的力矩值等值反向地施加于基坐标系和从坐标系。选择此选项将显示可用于启用输入端的附加参数。有关详细信息，请参阅 **Input** 部分。 |

### **Resolution Frame** — 用于解析驱动力矩的坐标系 `Base`（默认）| `Follower`

用于解析输入驱动力矩的坐标系，指定为 `Base` 或 `Follower`。

#### 传感

### **Resolution Frame** — 用于解析传感输出的坐标系 `Base`（默认）| `Follower`

用于解析传感输出信号的坐标系，指定为 `Base` 或 `Follower`。有关输出信号的详细信息，请参阅 **Output** 部分。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置来感测力或力矩。 |
| `Normal` | 正常模式启用自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中将关节从所有约束中释放。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端输出零。 |
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

六自由度且无运动学奇异的关节

6-DOF Joint 模块提供三个平移自由度和三个旋转自由度。从动坐标系可以相对于基坐标系具有三维变换。该变换包含三个顺序平移以及以四元数编码的三维旋转。四元数不存在运动学奇异。

沿基坐标系 x、y 和 z 轴的三个平移自由度，以及绕平移后形成的从动坐标系 x、y 和 z 轴的三个旋转自由度

平移分别沿基坐标系的 *x*、*y* 和 *z* 轴进行。在旋转之前，从动坐标系的轴与基坐标系的对应轴平行。三维旋转相对于平移后形成的从动坐标系。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。目标在基坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定先满足哪些目标以及满足的程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数来建模能量耗散，使用 **Spring Stiffness** 参数来建模能量存储。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器则充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限制，请使用 **Limits** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼方法计算力。有关平滑弹簧-阻尼方法的更多信息，请参阅 Spatial Contact Force 模块的 Description 部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关更多信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关更多信息，请参阅 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡中的 **Faults** 部分，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
