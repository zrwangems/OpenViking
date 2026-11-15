---
type: simulink-block
title: 'Simulation 3D Physics Vehicle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dphysicsvehicle'
documentation_source_path: 'ref/simulation3dphysicsvehicle.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Physics Vehicle

## 端口

### 输入

### **SteerCmd** — 归一化转向角标量

归一化转向角，指定为标量。**SteerCmd** 分别对应于由 **Front wheel max steer angle** 和 **Rear wheel max steer angle** 参数确定的转向角最小和最大范围。

### **AccelCmd** — 归一化车辆加速度标量

归一化加速度扭矩请求，发送到车辆动力总成，指定为标量。确切响应由发动机、变速器和其他车辆参数表征。

### **DecelCmd** — 归一化车辆减速度标量

归一化减速度扭矩请求，发送到车辆制动系统，指定为标量。确切制动响应由发动机、变速器和其他车辆参数表征。

### **GearCmd** — 挡位输入 `1` | `-1` | `0`

挡位输入，指定为 `1`、`-1` 或 `0`。

- `1` – 前进挡
- `-1` – 倒挡
- `0` – 空挡

如果选择手动换挡模式，则车辆根据该信号换挡，但列出的值仍然适用。任何不对应有效挡位的输入集都会被忽略。

### 输出

### **Info** — 总线信号 bus

此端口是可选的。

包含这些模块值的总线信号。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿地球固定 *X* 轴的位移 | 计算 | m |
| `Y` | | | 车辆质心沿地球固定 *Y* 轴的位移 | 计算 | m |
| `Z` | | | 车辆质心沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿地球固定 *X* 轴的速度 | 计算 | m/s |
| `Ydot` | | | 车辆质心沿地球固定 *Y* 轴的速度 | 计算 | m/s |
| `Zdot` | | | 车辆质心沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（侧倾） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | 计算 | rad |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算 | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（侧倾角速度） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速度） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） | 计算 | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算 | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算 | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算 | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算 | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | 计算 | rad/s |
| `DCM` | 方向余弦矩阵 | | | | 计算 | rad |
| `Forces` | `Tires` | `FrntTires` | `Lft` | `Fx` | 左前轮胎沿车辆固定 *x* 轴的力 | 估算 | N |
| `Fy` | 左前轮胎沿车辆固定 *y* 轴的力 | 估算 | N |
| `Fz` | 左前轮胎沿车辆固定 *z* 轴的力 | 估算 | N |
| `Rght` | `Fx` | 右前轮胎沿车辆固定 *x* 轴的力 | 估算 | N |
| `Fy` | 右前轮胎沿车辆固定 *y* 轴的力 | 估算 | N |
| `Fz` | 右前轮胎沿车辆固定 *z* 轴的力 | 估算 | N |
| `RearTires` | `Lft` | `Fx` | 左后轮胎沿车辆固定 *x* 轴的力 | 估算 | N |
| `Fy` | 左后轮胎沿车辆固定 *y* 轴的力 | 估算 | N |
| `Fz` | 左后轮胎沿车辆固定 *z* 轴的力 | 估算 | N |
| `Rght` | `Fx` | 右后轮胎沿车辆固定 *x* 轴的力 | 估算 | N |
| `Fy` | 右后轮胎沿车辆固定 *y* 轴的力 | 估算 | N |

**注意**

由于 Epic Games® 从 PhysX® 过渡到 Chaos Physics，Unreal Engine 不再显式提供轮胎力。为轮胎力计算的值是近似估算值。

| 信号 | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- |
| `Mtr` | `MtrSpd` | 施加的驱动轴角速度输入 | *ωi* | RPM |
| `Trans` | `TransGearCmd` | 命令挡位 | *Ncmd* | N/A |
| `TransGear` | 接合挡位 | *N* | N/A |

### **xdot** — 车辆纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，单位为 m/s。

### **ydot** — 车辆横向速度 `scalar`

车辆质心沿车辆固定 *y* 轴的速度，单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的角速度 `r`（横摆角速度），单位为 rad/s。

## 参数

### 底盘

### **Type, PassVehMesh** — 类型 `Muscle car` (默认) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

指定车辆类型。此表提供指向车辆尺寸的链接。

| **Vehicle type** 设置 | 车辆尺寸 |
| --- | --- |
| `Muscle car` | Muscle Car |
| `Sedan` | Sedan |
| `Sport utility vehicle` | Sport Utility Vehicle |
| `Small pickup truck` | Small Pickup Truck |
| `Hatchback` | Hatchback |
| `Box truck` | Box Truck |

#### 依赖关系

选择 `Custom` 会启用允许您为车辆导入自定义网格的参数。

### **Color, VehColor** — 车辆颜色 `Red` (默认) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver` | `Dazzle camouflage`

选择车辆颜色。

### **Name, ActorName** — 车辆名称 `SimulinkVehicle1` (默认) | character vector

默认情况下，当您在模型中使用此模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Physics Vehicle 和 Simulation 3D Vehicle 模块的数量。

### **Initial position [X, Y, Z], InitialPos [m]** — 车辆初始位置 `[ 0, 0, -0.5]` (默认) | 1-by-3 array

车辆初始位置，指定为 1-by-3 array，单位为 m。数组元素分别是沿 **Coordinate system** 参数 *X*、*Y* 和 *Z* 轴的值。

### **Initial rotation [Roll, Pitch, Yaw], InitialRot [rad]** — 车辆初始旋转 `[ 0, 0, 0 ]` (默认) | 1-by-3 array

车辆初始旋转，指定为 1-by-3 array，单位为 rad。数组元素分别是绕 **Coordinate system** 参数 *X*、*Y* 和 *Z* 轴的值。

### **Mass, Mass [kg]** — 车辆质量 `1500` (默认) | scalar

车辆质量，单位为 kg。此值不包括车轮质量。

### **Center of mass offset vector, CgOffset [m]** — 质心偏移 `[0, 0, 0]` (默认) | three-element vector

质心偏移，指定为 three-element vector，单位为米。

### **Inertia tensor scaling vector, IvehScale []** — 惯性张量缩放 `[1, 1, 1]` (默认) | three-element vector

惯性张量缩放，指定为 three-element 无量纲向量。

### **Chassis height (used in drag), ChassisHeight [m]** — 底盘高度 `1.0` (默认) | scalar

用于计算阻力的底盘高度，以米为单位指定。

### **Drag coefficient, Cd []** — 车辆阻力系数 `0.3` (默认) | scalar

车辆阻力系数，无量纲。

### **Drag lift coefficient, Cl []** — 纵向升力系数 `0.1` (默认) | scalar

纵向升力系数，无量纲。

### **Path to custom mesh, MeshPath** — 自定义网格路径 character vector

自定义网格文件的路径。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Track width, TrackWidth [m]** — 车轮间距离 `1.9` (默认) | scalar

车辆轮距是指车轮之间的距离，即轴长，以米为单位指定。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel base in custom mesh [m]** — 自定义网格中的轴距 `3` (默认) | scalar

轴距，单位为米。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Front Wheel radius, FrntWhlRadius [m]** — 前轮半径 `0.23` (默认) | scalar

前轮半径，单位为米。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Front wheel width, FrntWhlWidth [m]** — 前轮宽度 `0.20` (默认) | scalar

前轮宽度，单位为米。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Rear Wheel radius, RearWhlRadius [m]** — 后轮半径 `0.23` (默认) | scalar

后轮半径，单位为米。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Rear wheel width, RearWhlWidth [m]** — 后轮宽度 `0.20` (默认) | scalar

后轮宽度，单位为米。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### 动力总成与传动系统

#### 动力总成

### **Motor torque indices, TrqCrv [Nm]** — 电机扭矩索引 `[ 75, 75, 97, 117, 152, 175, 175, 175, 175, 165, 155, 145, 140, 135, 125, 115, 50 ]` (默认) | vector

电机扭矩索引，单位为 N·m。您可以使用这些变速器前值来表示电动机或传统发动机。

**数据类型：** `double`

### **Motor speed breakpoints, SpdCrv [rpm]** — 电机转速断点 `[ 0, 750, 1054, 1357, 1660, 1964, 2267, 2571, 2875, 3178, 3482, 3785, 4089, 4393, 4696, 5000, 7000 ]` (默认) | vector

电机转速断点，单位为 rpm。

**数据类型：** `double`

### **Maximum powertrain speed, MaxRPM [rpm]** — 最大动力总成转速 `7000` (默认) | scalar

最大动力总成转速，单位为 rpm。如果选择自动变速器选项，此值还对应于升挡和降挡逻辑中使用的归一化换挡点。

**数据类型：** `double`

### **Powertrain rotational inertia, Jmot [kg\*m^2]** — 动力总成转动惯量 `1.0` (默认) | scalar

动力总成转动惯量，单位为 kg·m2。

**数据类型：** `double`

### **Powertrain damping at full torque request, bEngMax [Nms/rad]** — 全扭矩请求下的动力总成阻尼 `0.15` (默认) | scalar

全扭矩请求下的动力总成阻尼，单位为 kg·m2/s。

**数据类型：** `double`

### **Powertrain damping at zero torque request in gear, bEngMin [Nms/rad]** — 挂挡时零扭矩请求下的动力总成阻尼 `2` (默认) | scalar

挂挡时零扭矩请求下的动力总成阻尼，单位为 kg·m2/s。

**数据类型：** `double`

#### 传动系统

### **Drivetrain type** — 传动系统 `Rear Wheel Drive` (默认) | `Front Wheel Drive` | `All Wheel Drive`

实现后轮、前轮或全轮驱动。

### **Front to rear torque split ratio, FrntRearSplit []** — 前后扭矩分配比 0.5 (默认) | scalar in the range (0,1)

前后扭矩分配比，无量纲。

`1` 表示 100% 扭矩传递到前轮。`0` 表示 100% 传递到后轮。

#### 依赖关系

要启用此参数，请将 **Drivetrain type** 设置为 `All Wheel Drive`。

### **Transmission type** — 变速器 `Automatic` (默认) | `Manual`

实现自动或手动变速器。

**注意**

即使 **Transmission type** 设置为 `Automatic`，也必须提供 **GearCmd** 输入。

### **Gear number vector, G []** — 挡位编号 `[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]` (默认) | vector

挡位编号向量，无量纲。

**数据类型：** `double`

### **Gear ratio vector, N []** — 传动比 `[ -3.5, 1, 4.75, 3.75, 3.25, 2.75, 2.25, 1.5, 1, 0.75 ]` (默认) | vector

传动比，无量纲。

**注意**

必须至少为倒挡提供一个负传动比。还必须提供一个空挡传动比，其中数组长度对应于前进挡数量加二，一个用于倒挡，一个用于空挡。

**数据类型：** `double`

### **Upshift speed, UpShiftRPM [rpm]** — 升挡转速 4000 (默认) | scalar greater than `DownShiftRPM`

升挡转速，单位为 rpm。

### **Downshift speed, DownShiftRPM [rpm]** — 降挡转速 2000 (默认) | scalar in the range [0, `UpShiftRPM` )

降挡转速，单位为 rpm。

### **Minimum (idle) speed, MinRPM [rpm]** — 最小（怠速）动力总成转速 `750` (默认) | scalar in the range [`0`, `MaxRPM`]

最小动力总成转速，单位为 rpm。

### **Shift time, tShift [s]** — 完成换挡所需时间 `0.1` (默认) | scalar

完成换挡所需时间，指定为标量，单位为 s。

**数据类型：** `double`

### **Final drive ratio, NDiff []** — 主减速器传动比 `3.2` (默认) | scalar

主减速器传动比，无量纲。此值是变速器后传动比，通常见于差速器或主减速器齿轮箱中。

**数据类型：** `double`

### **Transmission efficiency, eta []** — 效率系数 0.94 (默认) | scalar in the range [0,1)

效率系数，无量纲。

### 转向与制动

#### 转向

### **Steering type** — 设置转向类型的选项 `Ackermann` (默认) | `Linear`

转向类型，指定为 `Ackermann` 或 `Linear`。

### **Outside to inside steering ratio, SteerAngleRatio []** — 外侧与内侧转向角比 1.0 (默认) | scalar

外侧与内侧转向角比，无量纲。

#### 依赖关系

要启用此参数，请将 **Steering type** 设置为 `Linear`。

### **Front wheel max steer angle, FrntWhlMaxSteer [rad]** — 前轮最大转向角 `45*pi/180` (默认) | scalar

前轮最大转向角，单位为弧度。此值是前轮在 `-1` 或 `1` 转向命令输入信号下转动的绝对角度。

**数据类型：** `double`

### **Rear wheel max steer angle, RearWhlMaxSteer [rad]** — 后轮最大转向角 0 (默认) | scalar

后轮最大转向角，单位为弧度。此值是后轮在 `-1` 或 `1` 转向命令输入信号下转动的绝对角度。

**数据类型：** `double`

### **Maximum steering ratio breakpoints, SteerCrv []** — 最大转向比 `[ 1, 0.8, 0.7 ]` (默认) | vector

最大转向比断点，无量纲。此值是转向命令受车速断点影响的增益。

**数据类型：** `double`

### **Steering ratio speed breakpoints, SteerSpdCrv [m/s]** — 转向比速度断点 `[ 0, 60, 120 ]./3.6` (默认) | vector

转向比速度断点，单位为 m/s。此值是转向比增益使用的车辆前进速度断点。

**数据类型：** `double`

#### 制动

### **Maximum front wheel torque, FrntWhlMaxTrq [Nm]** — 最大前轮扭矩 `1500` (默认) | scalar

最大前轮扭矩，单位为 N·m。此值是对应于归一化 **DecelCmd** 输入施加到前轮的最大制动扭矩。

**数据类型：** `double`

### **Maximum rear wheel torque, RearWhlMaxTrq [Nm]** — 最大后轮扭矩 `1500` (default) | scalar

最大后轮扭矩，单位为 N·m。该值是对应于归一化 **DecelCmd** 输入施加到后轮的最大制动扭矩。

**数据类型:** `double`

### **Option to enable handbrake input** — 启用驻车制动输入 `off` (default) | `on`

选择此参数以启用驻车制动输入。

**数据类型:** `Boolean`

### **Front wheels affected by handbrake** — 前轮驻车制动选项 `off` (default) | `on`

启用此参数可使驻车制动影响前轮。

#### 依赖项

要启用此参数，请选择 **Enable handbrake input**。

**数据类型:** `Boolean`

### **Rear wheels affected by handbrake** — 后轮驻车制动选项 `off` (default) | `on`

启用此参数可使驻车制动影响后轮。

#### 依赖项

要启用此参数，请选择 **Enable handbrake input**。

**数据类型:** `Boolean`

### **Maximum front wheel hand brake torque, FrntWhlMaxHndBrkTrq [Nm]** — 最大前轮驻车制动扭矩 `3000` (default) | scalar

最大前轮驻车制动扭矩，单位为 Nm。

#### 依赖项

要启用此参数，请选择 **Front wheels affected by
handbrake**。

### **Maximum rear wheel hand brake torque, RearWhlMaxHndBrkTrq [Nm]** — 最大后轮驻车制动扭矩 `3000` (default) | scalar

最大后轮驻车制动扭矩，单位为 Nm。

#### 依赖项

要启用此参数，请选择 **Front wheels affected by
handbrake**。

### 悬架、车轮和轮胎

#### 悬架

### **Front suspension force offset location, FrntSuspFOffset [m]** — 前悬架力偏移 `[0,0,0]` (default) | 三元素向量

前悬架力偏移，指定为三元素向量，单位为米。

### **Maximum front suspension compression (jounce), FrntSuspMaxComp [m]** — 最大前悬架压缩 `0.15` (default) | scalar

最大前悬架压缩或 jounce，指定为标量，单位为米。
Jounce 是悬架组件的向上运动或压缩。

### **Front spring preload, FrntSpringPreload [N]** — 前悬架预紧力 `200` (default) | scalar

前悬架预紧力，单位为 N。

### **Front spring stiffness, FrntSpringRate [N/m]** — 前悬架弹簧刚度 `30e3` (default) | scalar

前悬架弹簧刚度，单位为 N/m。

### **Maximum front suspension extension (rebound), FrntSuspMaxExt [m]** — 最大前悬架伸张 `0.1` (default) | scalar

最大前悬架伸张或回弹，指定为标量，单位为米。
回弹是悬架组件的向下运动或伸张。

### **Front suspension damping ratio, FrntSuspDamping []** — 前悬架阻尼比 `0.5` (default) | scalar

前悬架阻尼比，无量纲。阻尼比是减振器在其峰值水平时的系数，此时车辆处于完全稳定状态。

### **Front roll bar stiffness scaling, FrntRollbarScaling []** — 前防倾杆效果 0.15 (default) | 范围 (0,1) 内的标量

前防倾杆效果，无量纲。

### **Rear suspension force offset location, RearSuspFOffset [m]** — 后悬架力偏移 `[0,0,0]` (default) | 三元素向量

后悬架力偏移，指定为三元素向量，单位为米。

### **Maximum rear suspension compression (jounce), RearSuspMaxComp [m]** — 最大后悬架压缩 `0.15` (default) | scalar

最大后悬架压缩或 jounce，指定为标量，单位为米。
Jounce 是悬架组件的向上运动或压缩。

### **Rear spring preload, RearSpringPreload [N]** — 后悬架预紧力 `200` (default) | scalar

后悬架预紧力，单位为 N。

### **Rear spring stiffness, RearSpringRate [N/m]** — 后悬架弹簧刚度 `30e3` (default) | scalar

后悬架弹簧刚度，单位为 N/m。

### **Maximum rear suspension extension (rebound), RearSuspMaxExt [m]** — 最大后悬架伸张 `0.1` (default) | scalar

最大后悬架伸张或回弹，指定为标量，单位为米。
回弹是悬架组件的向下运动或伸张。

### **Rear suspension damping ratio, RearSuspDamping []** — 后悬架阻尼比 `0.5` (default) | scalar

后悬架阻尼比，无量纲。阻尼比是减振器在其峰值水平时的系数，此时车辆处于完全稳定状态。

### **Rear roll bar stiffness scaling, RearRollbarScaling []** — 后防倾杆效果 0.15 (default) | 范围 (0,1) 内的标量

后防倾杆效果，无量纲。

#### 车轮

### **Enable anti-lock braking** — 启用防抱死制动的选项 `off` (default) | `on`

选择此参数以启用防抱死制动。

**数据类型:** `Boolean`

### **Enable traction control** — 启用牵引力控制的选项 `off` (default) | `on`

选择此参数以启用牵引力控制。

**数据类型:** `Boolean`

#### 轮胎

### **Front wheel corner stiffness, Cy\_f [N/rad]** — 前侧偏刚度 `70e3` (default) | scalar

前侧偏刚度，单位为 N/rad。

### **Front wheel slip modifier, FrntSideSlipModifier []** — 前侧滑修正系数 `20` (default) | 范围 (0,1) 内的标量

前侧滑修正系数，无量纲。

### **Rear wheel corner stiffness, Cy\_r [N/rad]** — 后侧偏刚度 `70e3` (default) | scalar

后侧偏刚度，单位为 N/rad。

### **Rear wheel slip modifier, RearSideSlipModifier []** — 后侧滑修正系数 `20` (default) | 范围 (0,1) 内的标量

后侧滑修正系数，无量纲。

### **Friction scaling factor, lambda\_mu []** — 摩擦缩放 `1.0` (default) | scalar

标称摩擦缩放，无量纲。

**数据类型:** `double`

### 灯光控制

### **Enable light controls** — 控制车辆车灯的选项 `off` (default) | `on`

选择是否控制车辆前照灯。使用启用的参数设置灯光参数，包括前照灯强度。

#### 依赖项

选择此参数会：

- 创建输入端口 `Light
  controls`。
- 启用这些灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam   intensity** - **Low beam   intensity** - **High beam cone half   angle** - **Low beam cone half   angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **倒车灯** | **Reverse light intensity** |
  | **转向信号灯** | - **Turn signal light   intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B], HeadlightColor** — 前照灯颜色 `[1,1,1]` (default) | 1-by-3 vector of RGB triplet values

前照灯颜色，指定为归一化 1-by-3 RGB 三元组值向量。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — 远光灯强度 `100000` (default) | 正标量

远光灯强度，单位为 cd。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Low beam intensity, LowBeamIntensity** — 近光灯强度 `60000` (default) | 正标量

近光灯强度，单位为 cd。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **High beam cone half angle, HighBeamConeAngle** — 远光灯锥半角 `1.22` (default) | 小于 pi/2 的正标量

远光灯锥半角，单位为 rad。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Low beam cone half angle, LowBeamConeAngle** — 近光灯锥半角 `1.22` (default) | 小于 pi/2 的正标量

近光灯锥半角，单位为 rad。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — 左前照灯光束方向 `[0,0]` (default) | 值介于 -pi 和 pi 之间的 1-by-2 向量

左前照灯光束方向在 *Z*-down 坐标系中的俯仰和偏航方向，指定为 1-by-2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — 右前照灯光束方向 `[0,0]` (default) | 值介于 -pi 和 pi 之间的 1-by-2 向量

右前照灯光束方向在 *Z*-down 坐标系中的俯仰和偏航方向，指定为 1-by-2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

#### 制动灯

### **Brake light intensity, BrakelightIntensity** — 制动灯强度 `500` (default) | 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

#### 倒车灯

### **Reverse light intensity, ReverselightIntensity** — 倒车灯强度 `500` (default) | 正标量

倒车灯强度，单位为 cd/m^2。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

#### 转向信号灯

### **Turn signal light intensity, SignallightIntensity** — 转向信号灯强度 `500` (default) | 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Period, SignallightPeriod** — 转向信号灯周期 `1` (default) | 正标量

转向信号灯周期，单位为 s。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Pulse width, SignalPulseWidth** — 脉冲宽度 `50` (default) | 小于 100 的正标量

转向信号灯脉冲宽度，指定为周期的百分比。

#### 依赖项

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### 采样时间

### **Sample time, SampleTime** — 采样时间 `-1` (default) | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

### 真值

### **Output location and orientation** — 返回位置和方向的选项 `off` (default) | `on`

选择此参数以返回位置和方向。

**数据类型:** `Boolean`

### **Output nominal vehicle state feedback** — 返回标称车辆状态反馈的选项 `off` (default) | `on`

选择此参数以返回标称车辆状态反馈。

**数据类型:** `Boolean`

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

### R2024b：新的 Simulation 3D Physics Vehicle 模块颜色选项

从 R2024b 开始，您可以为 Simulation 3D Physics Vehicle 模块将 **Color, VehColor** 指定为 `Dazzle Camouflage`。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Physics Vehicle 模块仿真模型需要 Simulink
3D Animation。

### R2024a：从 PhysX 过渡到 Chaos Physics

从 R2024a 开始，Simulink
3D Animation 随附的 Unreal Engine 版本使用 Chaos Physics，而不是 PhysX 物理引擎。由于此更改，多个参数已被移除和添加。

下表列出了已移除的参数。

| 车辆元素 | 已移除参数 |
| --- | --- |
| **动力总成** | **Powertrain damping at zero torque request, in neutral** |
| **传动系统** | **Shift down indices** |
| **Shift up indices** |
| **Clutch slip torque** |
| **Minimum shift latency** |
| **转向** | **Percent Ackermann** |
| **悬架** | **Front suspension natural frequency** |
| **Rear suspension natural frequency** |
| **车轮** | **Front wheel mass** |
| **Rear wheel mass** |
| **Front wheel damping** |
| **Rear wheel damping** |
| **轮胎** | **Front tire lateral stiffness** |
| **Rear tire lateral stiffness** |
| **Front tire longitudinal stiffness** |
| **Rear tire longitudinal stiffness** |
| **Front tire max lateral stiffness factor** |
| **Rear tire max lateral stiffness factor** |

下表列出了已添加的参数。

| 车辆元素 | 已添加参数 |
| --- | --- |
| **底盘** | **Drag lift coefficient** |
| **Front wheel width** |
| **Rear wheel width** |
| **动力总成** | **Minimum (idle) speed** |
| **传动系统** | **Downshift speed** |
| **Upshift speed** |
| **Transmission efficiency** |
| **转向** | **Steer type** |
| **Outside to inside steering ratio** |
| **悬架** | **Front spring stiffness** |
| **Front spring preload** |
| **Rear spring stiffness** |
| **Rear spring preload** |
| **Front roll bar stiffness scaling** |
| **Rear roll bar stiffness scaling** |
| **车轮** | **Enable anti-lock braking** |
| **Enable traction control** |
| **轮胎** | **Front wheel corner stiffness** |
| **Front wheel slip modifier** |
| **Rear wheel corner stiffness** |
| **Rear wheel slip modifier** |

### R2023a：兼容 Unreal Engine 4.27

Simulation 3D Physics Vehicle 模块与 Unreal Engine 4.27 兼容。对 Unreal Engine 未来版本的支持可能需要更改模块参数，包括传动系统动力学、换挡调度和轮胎参数。

## 描述

实现可控 6DOF 车辆 3D 环境

**注意**

使用 Simulation 3D Physics Vehicle 模块仿真模型需要 Simulink®
3D Animation™。

Simulation 3D Physics Vehicle 模块在 3D 仿真环境中实现一个可控的 10DOF 车辆，其中每个车轮具有一个垂直 DOF，底盘具有 6DOF。

要使用 Simulation 3D Physics Vehicle 模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Physics Vehicle 模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

模块输入使用 SAE J670[1] 中定义的车辆 *Z*-down *right-handed* (RH) *Cartesian* 坐标系。该坐标系是惯性的，并且初始与车辆几何中心对齐：

- *X* 轴 — 沿车辆纵轴，指向前方
- *Y* 轴 — 沿车辆横轴，指向右侧
- *Z* 轴 — 指向下方

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Physics Vehicle 模块之前执行。按此顺序，Unreal Engine® 3D 可视化环境会在 Simulation 3D Physics Vehicle 模块接收数据之前准备数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Physics Vehicle — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。
