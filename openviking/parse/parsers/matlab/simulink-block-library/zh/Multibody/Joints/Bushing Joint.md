---
type: simulink-block
title: 'Bushing Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'bushingjoint'
documentation_source_path: 'ref/bushingjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Bushing Joint

## 端口
```yaml
ports:
- name: B
  summary: 基础坐标系 坐标系
  direction: input
- name: F
  summary: 从动坐标系 坐标系
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
  summary: 驱动力矩物理信号
  direction: input
- name: qx
  summary: 运动轮廓物理信号
  direction: input
- name: ty
  summary: 驱动力矩物理信号
  direction: input
- name: qy
  summary: 运动轮廓物理信号
  direction: input
- name: tz
  summary: 驱动力矩物理信号
  direction: input
- name: qz
  summary: 运动轮廓物理信号
  direction: input
- name: mode
  summary: 关节模式控制物理信号
  direction: input
- name: px
  summary: 基元物理信号的位置
  direction: output
- name: vx
  summary: 基元物理信号的速度
  direction: output
- name: ax
  summary: 基元物理信号的加速度
  direction: output
- name: fx
  summary: 作用在关节基元上的执行器力物理信号
  direction: output
- name: fllx
  summary: 下限力物理信号
  direction: output
- name: fulx
  summary: 上限力物理信号
  direction: output
- name: py
  summary: 基元位置物理信号
  direction: output
- name: vy
  summary: 基元速度物理信号
  direction: output
- name: ay
  summary: 基元加速度物理信号
  direction: output
- name: fy
  summary: 作用在关节基元上的致动力物理信号
  direction: output
- name: flly
  summary: 下限力物理信号
  direction: output
- name: fuly
  summary: 上限力物理信号
  direction: output
- name: pz
  summary: 关节基元位置物理信号
  direction: output
- name: vz
  summary: 关节基元速度物理信号
  direction: output
- name: az
  summary: 关节原语加速度物理信号
  direction: output
- name: fz
  summary: 作用在关节原语上的执行器力物理信号
  direction: output
- name: fllz
  summary: 作用在关节原语上的下限力物理信号
  direction: output
- name: fulz
  summary: 作用在关节原语上的上限力物理信号
  direction: output
- name: qx
  summary: 关节原语位置物理信号
  direction: output
- name: wx
  summary: 关节原语角速度物理信号
  direction: output
- name: bx
  summary: 关节原语角加速度物理信号
  direction: output
- name: tx
  summary: 作用在关节原语上的执行器力矩物理信号
  direction: output
- name: tllx
  summary: 作用在关节原语上的下限力矩物理信号
  direction: output
- name: tulx
  summary: 作用在关节基元上的上限力矩物理信号
  direction: output
- name: qy
  summary: 关节基元位置物理信号
  direction: output
- name: wy
  summary: 关节基元角速度物理信号
  direction: output
- name: by
  summary: 关节基元角加速度物理信号
  direction: output
- name: ty
  summary: 作用在关节基元上的致动力矩物理信号
  direction: output
- name: tlly
  summary: 作用在关节基元上的下限力矩物理信号
  direction: output
- name: tuly
  summary: 作用在关节基元上的上限力矩物理信号
  direction: output
- name: qz
  summary: 关节基元位置物理信号
  direction: output
- name: wz
  summary: 关节基元角速度物理信号
  direction: output
- name: bz
  summary: 关节基元角加速度物理信号
  direction: output
- name: tz
  summary: 作用在关节基元上的执行器扭矩物理信号
  direction: output
- name: tllz
  summary: 作用在关节基元上的下限扭矩物理信号
  direction: output
- name: tulz
  summary: 作用在关节基元上的上限扭矩物理信号
  direction: output
- name: fc
  summary: 约束力，N 物理信号
  direction: output
- name: tc
  summary: 约束扭矩，N\*m 物理信号
  direction: output
- name: ft
  summary: 总力，N 物理信号
  direction: output
- name: tt
  summary: 总扭矩，N\*m 物理信号
  direction: output
```

### 坐标系

### **B** — 基础坐标系 坐标系

关节模块的基础坐标系。

### **F** — 从动坐标系 坐标系

关节模块的从动坐标系。
### 输入

#### X 移动副基元 (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *x* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系上。

#### 依赖关系

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Y 移动副基元 (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *y* 轴将此力等大反向地施加到关节的基础坐标系和从动坐标系上。

#### 依赖关系

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### Z 移动副基元 (Pz)

### **fz** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。该模块沿基础坐标系的 *z* 轴将此力等大反向地施加到关节的基础坐标系和从动坐标系上。

#### 依赖关系

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **力** 设置为 `Provided by Input`。

### **pz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **运动** 设置为 `Provided by Input`。

#### X 转动副基元 (Rx)

### **tx** — 驱动力矩物理信号

物理信号输入端口，接受关节基元的驱动力矩。该模块将此外力矩等大反向地施加到关节基元的基础坐标系和从动坐标系上。该力矩绕基础坐标系的 *x* 轴作用。在仿真过程中，从动坐标系和基础坐标系的 *x* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **X 转动副基元 (Rx)** > **驱动** 下，将 **力矩** 设置为 `Provided by Input`。

### **qx** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。该模块使用此信号确定从动坐标系相对于基础坐标系绕基础坐标系 *x* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Y Revolute Primitive (Ry)

### **ty** — 驱动力矩物理信号

物理信号输入端口，用于接受关节原语的驱动力矩。该模块将此力矩等值且反向地施加到关节原语的基座坐标系和从动坐标系上。该力矩是围绕基座坐标系的 *y* 轴的。在仿真过程中，从动坐标系和基座坐标系的 *y* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **Y Revolute Primitive (Ry)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`。

### **qy** — 运动轮廓物理信号

物理信号输入端口，用于接受关节原语的运动轮廓。该模块使用此信号来确定从动坐标系相对于基座坐标系围绕基座坐标系 *y* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Revolute Primitive (Ry)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### Z Revolute Primitive (Rz)

### **tz** — 驱动力矩物理信号

物理信号输入端口，用于接受关节原语的驱动力矩。该模块将此力矩等值且反向地施加到关节原语的基座坐标系和从动坐标系上。该力矩是围绕基座坐标系的 *z* 轴的。在仿真过程中，从动坐标系和基座坐标系的 *z* 轴彼此对齐。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`。

### **qz** — 运动轮廓物理信号

物理信号输入端口，用于接受关节原语的运动轮廓。该模块使用此信号来确定从动坐标系相对于基座坐标系围绕基座坐标系 *z* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。你可以在仿真过程中的任意时刻更改模式。

下表显示了在模式之间切换时，关节的位置和速度如何变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保留当前值，并在切换后保持恒定。 | 关节速度变为零，并在切换后保持恒定。 |
| 正常到分离 | 关节位置保留当前值，但在切换后可沿任意方向变化。 | 关节速度保留当前值，但在切换后可沿任意方向变化。 |
| 锁定到正常 | 关节位置保留当前值，但在切换后可沿与关节自由度（DOF）对齐的方向变化。 | 关节速度保持为零，但在切换后可沿与关节 DOF 对齐的方向变化。 |
| 锁定到分离 | 关节位置保留当前值，但在切换后可沿任意方向变化。 | 关节速度保持为零，但在切换后可沿任意方向变化。 |
| 分离到正常 | 对于与关节 DOF 对齐的方向，关节位置最初取通过牛顿法计算得到的值，此后可以变化。在受约束方向上，关节位置变为零，并在切换后保持恒定。 | 对于与关节 DOF 对齐的方向，关节速度最初取通过牛顿法计算得到的值，此后可以变化。在受约束方向上，关节速度变为零，并在切换后保持恒定。 |
| 分离到锁定 | 对于与关节 DOF 对齐的方向，关节位置最初取通过牛顿法计算得到的值，并在切换后保持恒定。在受约束方向上，关节位置变为零，并在切换后保持恒定。 | 关节速度变为零，并在切换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### X Prismatic Primitive (Px)

### **px** — 基元物理信号的位置

物理信号端口，用于输出关节基元的位置。该值是跟随坐标系相对于基坐标系在基坐标系 *x* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Position**。

### **vx** — 基元物理信号的速度

物理信号端口，用于输出关节基元的速度。该值是端口 **px** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Velocity**。

### **ax** — 基元物理信号的加速度

物理信号端口，用于输出关节基元的加速度。该值是端口 **px** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Acceleration**。

### **fx** — 作用在关节基元上的执行器力物理信号

物理信号端口，用于输出作用在关节基元上的执行器力。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Actuator Force**。

### **fllx** — 下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulx** — 上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **X Prismatic Primitive (Px)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Y Prismatic Primitive (Py)

### **py** — 基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基座坐标系在基座坐标系 *y* 方向上的位移。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Position**。

### **vy** — 基元速度物理信号

输出关节基元速度的物理信号端口。该值是端口 **py** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Velocity**。

### **ay** — 基元加速度物理信号

输出关节基元加速度的物理信号端口。该值是端口 **py** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Acceleration**。

### **fy** — 作用在关节基元上的致动力物理信号

输出作用在关节基元上的致动力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Actuator Force**。

### **flly** — 下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fuly** — 上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节基元的基座坐标系和从动坐标系上，以加速相对位置回到自由区域。

#### 依赖关系

要启用此端口，请在 **Y Prismatic Primitive (Py)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### Z Prismatic Primitive (Pz)

### **pz** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基座坐标系在基座坐标系 *z* 轴上的位移。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **vz** — 关节基元速度物理信号

输出关节基元速度的物理信号端口。该值是端口 **pz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **az** — 关节原语加速度物理信号

输出关节原语加速度的物理信号端口。该值为端口 **pz** 输出信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **fz** — 作用在关节原语上的执行器力物理信号

输出作用在关节原语上的执行器力的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fllz** — 作用在关节原语上的下限力物理信号

输出下限力的物理信号端口。当关节原语位置小于自由区域的下界时，该模块施加此力。该模块将此力施加到关节原语的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **fulz** — 作用在关节原语上的上限力物理信号

输出上限力的物理信号端口。当关节原语位置超过自由区域的上界时，该模块施加此力。该模块将此力施加到关节原语的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### X Revolute Primitive (Rx)

### **qx** — 关节原语位置物理信号

输出关节原语位置的物理信号端口。该值为从动坐标系相对于基座坐标系绕基座坐标系 *x* 轴的旋转角度。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Position**。

### **wx** — 关节原语角速度物理信号

输出关节原语角速度的物理信号端口。该值为端口 **qx** 输出信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Velocity**。

### **bx** — 关节原语角加速度物理信号

输出关节原语角加速度的物理信号端口。该值为端口 **qx** 输出信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Acceleration**。

### **tx** — 作用在关节原语上的执行器力矩物理信号

输出作用在关节原语上的执行器力矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Actuator Torque**。

### **tllx** — 作用在关节原语上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节原语位置小于自由区域的下界时，该模块施加此力矩。该模块将此力矩施加到关节原语的基座坐标系和从动坐标系上，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X Revolute Primitive (Rx)** > **Sensing** 下，选择 **Lower-Limit Torque**。

### **tulx** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **X 转动基元 (Rx)** > **传感** 下，选择 **上限力矩**。

#### Y 转动基元 (Ry)

### **qy** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值为从动坐标系相对于基座坐标系绕基座坐标系 *y* 轴的旋转角度。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **位置**。

### **wy** — 关节基元角速度物理信号

输出关节基元角速度的物理信号端口。该值为端口 **qy** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **速度**。

### **by** — 关节基元角加速度物理信号

输出关节基元角加速度的物理信号端口。该值为端口 **qy** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **加速度**。

### **ty** — 作用在关节基元上的致动力矩物理信号

输出作用在关节基元上的致动力矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **致动力矩**。

### **tlly** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **下限力矩**。

### **tuly** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此力矩施加到关节基元的基座坐标系和从动坐标系，以将相对位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Y 转动基元 (Ry)** > **传感** 下，选择 **上限力矩**。

#### Z 转动基元 (Rz)

### **qz** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值为从动坐标系相对于基座坐标系绕基座坐标系 *z* 轴的旋转角度。

#### 依赖关系

要启用此端口，请在 **Z 转动基元 (Rz)** > **传感** 下，选择 **位置**。

### **wz** — 关节基元角速度物理信号

输出关节基元角速度的物理信号端口。该值为端口 **qz** 信号的一阶导数。

#### 依赖关系

要启用此端口，请在 **Z 转动基元 (Rz)** > **传感** 下，选择 **速度**。

### **bz** — 关节基元角加速度物理信号

输出关节基元角加速度的物理信号端口。该值为端口 **qz** 信号的二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Acceleration**。

### **tz** — 作用在关节基元上的执行器扭矩物理信号

输出作用在关节基元上的执行器扭矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Actuator Torque**。

### **tllz** — 作用在关节基元上的下限扭矩物理信号

输出下限扭矩的物理信号端口。当关节基元位置小于自由区域的下界时，模块施加此扭矩。模块将此扭矩施加到关节基元的基座和从动框架上，以加速相对位置返回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Lower-Limit Torque**。

### **tulz** — 作用在关节基元上的上限扭矩物理信号

输出上限扭矩的物理信号端口。当关节基元位置超过自由区域的上界时，模块施加此扭矩。模块将此扭矩施加到关节基元的基座和从动框架上，以加速相对位置返回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/扭矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束扭矩，N\*m 物理信号

输出作用在关节上的约束扭矩的物理信号端口。这些扭矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在连接框架之间传递的所有力之和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，该图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总扭矩，N\*m 物理信号

输出作用在关节上的总扭矩的物理信号端口。总扭矩是通过关节在连接框架之间传递的所有扭矩之和。扭矩包括执行、内部、限位和约束扭矩。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。
## 参数
```yaml
parameters:
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: X Prismatic Primitive (Px)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: X Prismatic Primitive (Px)
- name: Value
  summary: 位置目标 0 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Specify Velocity Target
  summary: 是否指定线速度目标 off（默认）| on
  group: X Prismatic Primitive (Px)
- name: Priority
  summary: 线速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: X Prismatic Primitive (Px)
- name: Value
  summary: 速度目标 0 m/s（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Equilibrium Position
  summary: 内力为零的位置 0 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Spring Stiffness
  summary: 力定律的刚度 0 N/m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Damping Coefficient
  summary: 力定律的阻尼系数 0 N(m/s)（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Specify Lower Limit
  summary: 是否指定下限位置 off（默认）| on
  group: X Prismatic Primitive (Px)
- name: Bound
  summary: 自由区域的下界 -1 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Spring Stiffness
  summary: 下限处弹簧的刚度 1e6 N/m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Damping Coefficient
  summary: 下限处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Specify Upper Limit
  summary: 是否指定上限位置 off（默认）| on
  group: X Prismatic Primitive (Px)
- name: Bound
  summary: 自由区域的上限 1 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Spring Stiffness
  summary: 上限处的弹簧刚度 1e6 N/m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Damping Coefficient
  summary: 上限处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力的区域 1e-4 m（默认）| 标量
  group: X Prismatic Primitive (Px)
- name: Force
  summary: 提供致动力的选项 None（默认）| Provided by Input | Automatically Computed
  group: X Prismatic Primitive (Px)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: X Prismatic Primitive (Px)
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
  summary: 内力为零时的位置 0 m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Spring Stiffness
  summary: 力律的刚度 0 N/m（默认）| 标量
  group: Y Prismatic Primitive (Py)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N(m/s)（默认）| 标量
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
  summary: 是否指定上限位置 off（默认）| on
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
  summary: 用于平滑弹簧力和阻尼力的区域 1e-4 m（默认）| 标量
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
  summary: 线性速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: Value
  summary: 速度目标 0 m/s（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Equilibrium Position
  summary: 内部力为零的位置 0 m（默认）| 标量
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
  summary: 下界处弹簧的刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
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
  summary: 上界处弹簧的刚度 1e6 N/m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 1e3 N/(m/s)（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: 用于平滑弹簧力和阻尼力的区域 1e-4 m（默认）| 标量
  group: Z Prismatic Primitive (Pz)
- name: Force
  summary: 提供执行器力的选项 None（默认）| Provided by Input | Automatically Computed
  group: Z Prismatic Primitive (Pz)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Z Prismatic Primitive (Pz)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: X 转动基元 (Rx)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: X 转动基元 (Rx)
- name: Value
  summary: 位置目标 0 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Specify Velocity Target
  summary: 是否指定角速度目标 off（默认）| on
  group: X 转动基元 (Rx)
- name: Priority
  summary: 速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: X 转动基元 (Rx)
- name: Value
  summary: 速度目标 0 deg/s（默认）| 标量
  group: X 转动基元 (Rx)
- name: Equilibrium Position
  summary: 内部力矩为零的位置 0 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Spring Stiffness
  summary: 力定律的刚度 0 N*m/deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N*m/(deg/s)（默认）| 标量
  group: X 转动基元 (Rx)
- name: Specify Lower Limit
  summary: 是否指定下限位置限制 off（默认）| on
  group: X 转动基元 (Rx)
- name: Bound
  summary: 自由区域的下界 -90 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Spring Stiffness
  summary: 下界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: X 转动基元 (Rx)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力矩的区域 0.1 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Specify Upper Limit
  summary: 是否指定上限位置限制 off（默认）| on
  group: X 转动基元 (Rx)
- name: Bound
  summary: 自由区域的上界 90 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: X 转动基元 (Rx)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力矩的区域 0.1 deg（默认）| 标量
  group: X 转动基元 (Rx)
- name: Torque
  summary: 提供执行器扭矩的选项 None（默认）| Provided by Input | Automatically Computed
  group: X 转动基元 (Rx)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: X 转动基元 (Rx)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: Y 旋转基元 (Ry)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: Y 旋转基元 (Ry)
- name: Value
  summary: 位置目标 0 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Specify Velocity Target
  summary: 是否指定角速度目标 off（默认）| on
  group: Y 旋转基元 (Ry)
- name: Priority
  summary: 速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Y 旋转基元 (Ry)
- name: Value
  summary: 速度目标 0 deg/s（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Equilibrium Position
  summary: 内部扭矩为零的位置 0 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Spring Stiffness
  summary: 力定律的刚度 0 N*m/deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Damping Coefficient
  summary: 力定律的阻尼系数 0 N*m/(deg/s)（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Specify Lower Limit
  summary: 是否指定下限位置限制 off（默认）| on
  group: Y 旋转基元 (Ry)
- name: Bound
  summary: 自由区域的下界 -90 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Spring Stiffness
  summary: 下界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Specify Upper Limit
  summary: 是否指定上位置极限 off（默认）| on
  group: Y 旋转基元 (Ry)
- name: Bound
  summary: 自由区域的上界 90 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼器扭矩的区域 0.1 deg（默认）| 标量
  group: Y 旋转基元 (Ry)
- name: Torque
  summary: 提供执行器扭矩的选项 None（默认）| Provided by Input | Automatically Computed
  group: Y 旋转基元 (Ry)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Y 旋转基元 (Ry)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: Z Revolute Primitive (Rz)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Revolute Primitive (Rz)
- name: Value
  summary: 位置目标 0 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Specify Velocity Target
  summary: 是否指定角速度目标 off（默认）| on
  group: Z Revolute Primitive (Rz)
- name: Priority
  summary: 速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Revolute Primitive (Rz)
- name: Value
  summary: 速度目标 0 deg/s（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Equilibrium Position
  summary: 内部力矩为零的位置 0 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: 力律的刚度 0 N*m/deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: 力律的阻尼系数 0 N*m/(deg/s)（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Specify Lower Limit
  summary: 是否指定下限位置 off（默认）| on
  group: Z Revolute Primitive (Rz)
- name: Bound
  summary: 自由区域的下界 -90 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: 下界处弹簧的刚度 1e4 N*m/deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: 下界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力矩的区域 0.1 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Specify Upper Limit
  summary: 是否指定上限位置 off（默认）| on
  group: Z Revolute Primitive (Rz)
- name: Bound
  summary: 自由区域的上界 90 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: 上界处的弹簧刚度 1e4 N*m/deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: 上界处的阻尼系数 10 N*m/(deg/s)（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Transition Region Width
  summary: 用于平滑弹簧和阻尼力矩的区域 0.1 deg（默认）| 标量
  group: Z Revolute Primitive (Rz)
- name: Torque
  summary: 提供执行器力矩的选项 None（默认）| Provided by Input | Automatically Computed
  group: Z Revolute Primitive (Rz)
- name: Motion
  summary: 提供运动的选项 Automatically Computed（默认）| Provided by Input
  group: Z Revolute Primitive (Rz)
- name: Mode
  summary: 关节模式 Normal（默认）| Locked | Disengaged | Provided by Input
  group: Mode Configuration
- name: Direction
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: Composite Force/Torque Sensing
- name: Resolution Frame
  summary: 用于解析测量的坐标系 Base（默认）| Follower
  group: Composite Force/Torque Sensing
```

要交互式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### X Prismatic Primitive (Px)

#### State Targets

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 棱柱基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*x* 棱柱基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 棱柱基元的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*x* 棱柱基元的线速度目标，指定为以线速度单位为单位的标量。

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

选择此参数以指定 *x* 棱柱基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*x* 棱柱基元自由区域的下界，指定为以长度单位为单位的标量。

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

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

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

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加上限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节原语提供致动力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fx** 指定 *x* 移动副原语的致动力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节原语提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 该模块根据模型动力学计算并施加关节原语运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节原语的运动。 |

### Y Prismatic Primitive (Py)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的位置目标。

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

当穿透深度达到过渡区域的宽度时，模块施加下限力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *y* 移动副基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节原语的自由区域上界，指定为以长度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认）| 标量

上界处的弹簧刚度，指定为以线性刚度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度为单位的标量。

当穿透量达到过渡区域的宽度时，模块施加完整的上限力值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节原语提供致动力的选项，指定为以下值之一：

| Force 设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **fy** 指定 *y* 移动副原语的致动力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节原语提供运动的选项，指定为以下值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节原语运动。 |
| `Provided by Input` | 输入端口 **py** 指定关节原语的运动。 |

### Z Prismatic Primitive (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| 标量

*z* 移动副原语的位置目标，指定为以长度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的线速度目标。

### **Priority** — 线性速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线性速度目标的优先级，指定为 `High
(desired)` 或 `Low
(approximate)`。有关详细信息，
请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| 标量

*z* 移动副基元的
线性速度目标，
以线性
速度单位指定为标量。

#### 依赖关系

要启用此参数，请选择
**Specify Velocity
Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认）| 标量

弹簧力为零的位置，以长度单位指定为标量。

### **Spring Stiffness** — 力律的刚度 0 `N/m`（默认）| 标量

关节基元的内部弹簧-阻尼力律的刚度，以线性刚度单位指定为标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N(m/s)`（默认）| 标量

关节基元的内部弹簧-阻尼力律的阻尼系数，以线性阻尼系数单位指定为标量。

#### 限值

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *z* 移动副
基元的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| 标量

*z* 移动副基元自由区域的下界，以
长度单位指定为
标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e6 `N/m`（默认）| 标量

下界处弹簧的刚度，以线性刚度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

下界处的阻尼系数，以线性阻尼系数单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧和阻尼力的区域，以长度单位指定为标量。

当穿透达到过渡区域的宽度时，模块施加下限力的完整值。该
区域越小，力的起始越尖锐，求解器所需的时间步长
越小。在仿真精度与
仿真速度之间的权衡中，减小过渡区域
可提高精度，增大过渡区域
可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *z* 移动副
基元的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| 标量

关节基元自由区域的上界，以长度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| 标量

上界处弹簧的刚度，以线性刚度单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 标量

上界处的阻尼系数，以线性阻尼系数单位指定为标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| 标量

用于平滑弹簧力和阻尼力的区域，指定为以长度为单位的标量。

当穿透深度达到过渡区域的宽度时，模块施加完整的上限力值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fz** 为 *z* 移动基元指定执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可能满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **pz** 为关节基元指定运动。 |

### X 转动基元 (Rx)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*x* 转动基元的位置目标，指定为以角度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 中的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*x* 转动基元的角速度目标，指定为以角速度为单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| 标量

弹簧力矩为零的位置，指定为以角度为单位的标量。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认）| 标量

*x* 转动基元的内部弹簧-阻尼力定律的刚度，指定为以扭转刚度为单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*x* 转动基元内部弹簧-阻尼力律的阻尼系数，指定为具有阻尼系数单位的标量。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置限制 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*x* 转动基元自由区域的下界，指定为具有角度单位的标量。

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

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块施加下限力矩的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置限制 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| 标量

*x* 转动基元自由区域的上界，指定为具有角度单位的标量。

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

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的标量。

当穿透达到过渡区域的宽度时，模块施加上限力矩的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| 扭矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **tx** 指定 *x* 旋转基元的执行器扭矩。 |
| `Automatically Computed` | 模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的扭矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **qx** 指定 *x* 旋转基元的运动。 |

### Y 旋转基元 (Ry)

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

### **Specify Lower Limit** — 是否指定下限位置限制 `off`（默认）| `on`

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

当侵入量达到过渡区域的宽度时，该模块施加下极限扭矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

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

当侵入量达到过渡区域的宽度时，该模块施加上极限扭矩的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| 扭矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **ty** 为 *y* 旋转基元指定执行器扭矩。 |
| `Automatically Computed` | 该模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的扭矩可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

用于指定关节基元运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 该模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qy** 指定 *y* 旋转基元的运动。 |

### Z Revolute Primitive (Rz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| 标量

*z* 旋转基元的位置目标，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 旋转基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| 标量

*z* 旋转基元的角速度目标，指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| 标量

弹簧力矩为零的位置，指定为具有角度单位的标量。

### **Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 标量

*z* 旋转基元的内部弹簧-阻尼力律的刚度，指定为具有扭转刚度单位的标量。

### **Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 标量

*z* 旋转基元的内部弹簧-阻尼力律的阻尼系数，指定为具有阻尼系数单位的标量。

#### 限位

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以指定 *z* 旋转基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| 标量

*z* 旋转基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

下界处弹簧的刚度，指定为具有扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

下界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼力矩的区域，指定为带角度单位的标量。

当穿透量达到过渡区域的宽度时，该模块施加下限力矩的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| 标量

*z* 转动基元自由区域的上界，指定为带角度单位的标量。

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

当穿透量达到过渡区域的宽度时，该模块施加上限力矩的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### Actuation

### **Torque** — 提供执行器力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力矩的选项，指定为以下值之一：

| 力矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器力矩。 |
| `Provided by Input` | 输入端口 **tz** 指定 *z* 转动基元的执行器力矩。 |
| `Automatically Computed` | 该模块自动计算力矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 该模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qz** 指定 *z* 转动基元的运动。 |

### Mode Configuration

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，并且关节的约束按预期在仿真期间工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不会影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过使用输入信号来指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### Composite Force/Torque Sensing

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块感测基坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。
## 所属库

Simscape / Multibody / Joints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模型模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

具有三个移动副和三个转动副的关节

Bushing Joint 模块对具有三个平移和三个旋转自由度的关节进行建模。该关节使从动坐标系能够通过三个正交平移及随后的三个旋转序列，相对于基坐标系执行空间变换。图中显示了在给定仿真时间步中关节变换发生的顺序。

变换序列示意图

每次变换得到的坐标系作为下一次变换的基坐标系。由于三维旋转是按序列发生的，因此两个轴可能会对齐，从而导致失去一个旋转自由度。这种现象称为万向节锁。

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。目标在基坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定先满足哪些目标以及满足的程度。有关示例，请参见 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数来建模能量耗散，使用 **Spring Stiffness** 参数来建模能量存储。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器则充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限制，请使用 **Limits** 下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼方法计算力。有关平滑弹簧-阻尼方法的更多信息，请参见 Spatial Contact Force 模块的 Description 部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关更多信息，请参见 Specifying Joint Actuation Inputs。此外，该关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关更多信息，请参见 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参见 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以用于添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
