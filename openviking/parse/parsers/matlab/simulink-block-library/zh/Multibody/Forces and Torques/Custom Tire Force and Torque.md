---
type: simulink-block
title: 'Custom Tire Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'customtireforceandtorque'
documentation_source_path: 'ref/customtireforceandtorque.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Tire Force and Torque

## 端口

### 几何

### **B** — 基础几何 geometry

表示轮胎所接触表面的基础几何。必须将此端口连接到 Infinite Plane 或 Grid Surface 模块。

### 坐标系

### **F** — 从动坐标系 frame

表示轮胎的从动坐标系。坐标系原点位于轮胎中心。

### 输入

### **ft** — 轮胎力，*N* physical signal

physical signal 输入端口，接收计算得到的自定义轮胎力。使用 Custom Tire Force and Torque 模块的输出计算轮胎力。必须相对于轮胎的接触坐标系计算轮胎力。

输入包含三个部分：

- Fx 是切向于接触平面的纵向力，并与接触坐标系的 *x* 轴对齐。
- Fy 是侧向力，与由 Fx 和 Fz 定义的平面正交。
- Fz 是法向力，在接触点处垂直于接触平面。

力必须为非负。如果模块接收到负力，模块会将该值裁剪为零。此外，必须确保仿真期间单位一致。

### **tt** — 轮胎力矩，*N\*m* physical signal

physical signal 输入端口，接收计算得到的自定义轮胎力矩。使用 Custom Tire Force and Torque 模块的输出计算轮胎力矩。必须相对于轮胎的接触坐标系计算轮胎力矩。

输入包含三个部分：

- Mx 是翻转力矩。
- My 是滚动阻力矩。
- Mz 是回正力矩。

必须确保仿真期间单位一致。

### 输出

### **con** — 接触信号，unitless physical signal

physical signal 输出端口，指示轮胎与接触表面是否具有有效接触。当它们接触且接触有效时，信号等于 `1`，否则信号等于 `0`。

如果从动坐标系位于接触表面下方，则轮胎与表面之间的接触无效，模块不会向轮胎施加力和力矩。

#### 依赖关系

要启用此端口，请在 **Sensing** 下选择 **Contact Signal**。

#### 线速度

### **vx** — 相对纵向速度，*m/s* physical signal

physical signal 输出端口，输出沿接触坐标系的 *x* 方向，从动坐标系与几何体上接触点之间的相对速度。该值的单位为 length/time。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Longitudinal Velocity**。

### **vy** — 相对侧向速度，*m/s* physical signal

physical signal 输出端口，输出沿接触坐标系的 *y* 方向，从动坐标系与几何体上接触点之间的相对速度。该值的单位为 length/time。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Lateral Velocity**。

#### 横摆

### **psid** — 横摆角速度，*rad/s* physical signal

physical signal 输出端口，输出横摆角的一阶导数。该值的单位为 angle/time。

#### 依赖关系

要启用此端口，请在 **Sensing > Yaw** 下选择 **Velocity**。

#### 外倾

### **gamma** — 外倾角，*rad* physical signal

physical signal 输出端口，输出轮胎的外倾角。该值的单位为 angle。

#### 依赖关系

要启用此端口，请在 **Sensing > Camber** 下选择 **Angle**。

### **gammad** — 外倾角速度，*rad/s* physical signal

physical signal 输出端口，输出外倾角的一阶导数。该值的单位为 angle/time。

#### 依赖关系

要启用此端口，请在 **Sensing > Camber** 下选择 **Velocity**。

#### 自旋

### **omega** — 自旋角速度，*rad/s* physical signal

physical signal 输出端口，提供自旋角的一阶导数。该值的单位为 angle/time。

#### 依赖关系

要启用此端口，请在 **Sensing > Spin** 下选择 **Velocity**。

#### 轮胎半径

### **rl** — 负载半径，*m* physical signal

physical signal 输出端口，提供从轮胎中心到轮胎与接触表面之间接触点的距离。该值的单位为 length。

#### 依赖关系

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Loaded Radius**。

### **rho** — 径向变形，*m* physical signal

physical signal 输出端口，提供 **Tire Radius** 参数中指定的轮胎半径与 **rl** 端口输出的负载半径之间的差值。该值的单位为 length。

#### 依赖关系

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Radial Deflection**。

#### 接触坐标系

### **Rb** — 基础旋转，unitless physical signal

physical signal 端口，输出一个 3-by-3 旋转矩阵，该矩阵将接触坐标系中的向量映射到基础几何的参考坐标系中的向量。输出信号在关联于基础几何的参考坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Rotation**。

### **pb** — 基础平移，*m* physical signal

physical signal 端口，输出一个 3-by-1 向量，其中包含在基础几何的参考坐标系中解析的接触坐标系原点坐标。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Base Translation**。

### **Rf** — 从动旋转，unitless physical signal

physical signal 端口，输出一个 3-by-3 旋转矩阵，该矩阵将接触坐标系中的向量映射到从动几何的参考坐标系中的向量。输出信号在关联于从动几何的参考坐标系中解析。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Follower Rotation**。

### **pf** — 从动平移，*m* physical signal

physical signal 端口，输出一个 3-by-1 向量，其中包含在从动几何的参考坐标系中解析的接触坐标系原点坐标。

#### 依赖关系

要启用此端口，请在 **Sensing > Contact Frame** 部分中，选择 **Follower Translation**。

## 参数

### **Tire Radius** — 轮胎半径 `1 m` (default) | positive scalar

轮胎半径，指定为具有长度单位的 positive scalar。

### **Contact Frame Computation Method** — 用于计算接触坐标系位置和方向的方法 `Weighted Penetration` (default) | `Closest Point`

用于计算接触坐标系位置和方向的方法，指定为：

- `Closest Point`：将此方法用于单点接触足够的道路驾驶工况。
- `Weighted Penetration`：将此方法用于涉及多点接触的崎岖地面驾驶工况，例如越野场景。

您可以使用计算得到的数据来开发自定义轮胎模型。

## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

### R2024b：计算径向变形和负载半径

您可以使用 **rl** 和 **rho** 端口为自定义轮胎模型计算负载半径和径向变形。负载半径是从轮胎中心到轮胎与接触表面之间接触点的距离，而径向变形是负载半径与 **Tire Radius** 参数中指定的轮胎半径之间的差值。

## 描述

计算轮胎与地面表面之间的相互作用和空间关系

Custom Tire Force and Torque 模块计算轮胎与地面表面之间的相互作用和空间关系。

要对自定义轮胎建模，请使用该模块的输出计算轮胎力和力矩。然后，将这些信号作为输入环回该模块。图像显示了自定义轮胎模型的图。

必须相对于轮胎的接触坐标系计算轮胎力和力矩。接触坐标系位于接触点处，并且该坐标系的 *z* 轴垂直于接触平面。轮胎力必须为非负。如果轮胎力为负，模块会将输入力裁剪为零。此外，必须在整个仿真过程中保持力和力矩的单位一致。

从动坐标系位于轮胎中心。图像显示了零配置下轮胎的从动坐标系和接触坐标系。

横摆角、外倾角和自旋角对应于绕轮胎从动坐标系的 *y*-*x*-*z* 顺序旋转。

该模块有两种方法计算用于表征轮胎与地面之间相互作用和空间关系的数据。最近点方法通过查找地面表面上最靠近轮胎中心且位于轮胎平面内的点来确定接触点。接触法向量位于接触点处，并且在接触点处垂直于接地印迹。

对于轮胎经历多点接触的场景，例如越野地形或减速带等障碍物，请使用加权穿透法。为了因接触表面的不规则性简化计算，该方法在每个仿真时间步计算一个等效接触平面，以近似实际接触区域。接触点是该等效平面上最靠近轮胎中心的点。接触法向量位于接触点处，并垂直于等效平面。例如，图像显示了当轮胎遇到斜坡时，加权穿透法如何计算等效平面、接触点和法向量。

加权穿透法法向量 *n* 与等效接触平面正交。

**注意**

使用加权穿透法时，接触点可能不位于实际地面几何体上。例如，如果接触区域局部凸起或凹陷，接触点可能位于地面表面下方或上方。

您可以使用 **con** 端口指示轮胎与表面是否具有有效接触。如果轮胎与表面未接触或接触无效，则所有感测输出（例如轮胎力、轮胎力矩和外倾角）均变为零。
