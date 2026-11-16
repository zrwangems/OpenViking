---
type: simulink-block
title: 'Differential Drive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Drivetrain'
documentation_page: 'differentialtankdrive'
documentation_source_path: 'vexv5/ref/differentialtankdrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential Drive

## 端口

### 输入

### **Ref** — 参考位姿三元素向量

最终位姿或路点，指定为 `[x y θ]` 的三元素向量，其中 x 和 y 对应位置，*θ* 对应方向角。正角度是从正 *x* 轴相对于起始位姿逆时针测量的。

由于差速驱动机器人不能侧向移动，位置 (x, y) 和角度 *θ* 参考值会依次控制。首先机器人移动到指定位置，然后转向指定角度。
### 输出

### **Status** — 驱动器的活动状态 0 | `1`

此端口输出驱动模块是否处于活动状态。使用此输出来确定是否到达当前路点。当以下情况时，状态为活动：

- 驱动器正在移动或转向。
- 传感器（inertial sensor 或 gyroscope）正在校准。

当驱动器活动时，端口返回 `1`，否则返回 `0`。

**数据类型：** `Boolean`

### **WWheel** — 目标轮速两元素向量

此端口按从右到左的顺序输出目标轮速，以 radians per second 为单位测量。此模块包含控制器逻辑，用于提供轮速命令，这些命令对应于发送到 Smart Motor write 模块的电机命令。

您可以使用此输出来监控轮速命令，或添加额外的 Smart Motors。

#### 依赖关系

要启用此端口，请选择 **Target wheel speeds in right, left order (rad/s)** 参数。

**数据类型：** `double`

### **Pose** — 当前机器人位姿三元素向量

当前车辆位姿，指定为 `[x y θ]` 的三元素向量，其中 x 和 y 对应位置，*θ* 对应方向角。正角度是从正 *x* 轴逆时针测量的。

使用此模块监控机器人当前的位置和航向。

#### 依赖关系

要启用此端口，请选择 **Current Pose** 参数。
### 可选输出

### **Target wheel speeds in right, left order (rad/s)** — 目标轮速 `off`（默认） | `on`

选择 **Target wheel speeds in right, left order (rad/s)** 参数以启用 **WWheel** 端口。有关 **Wheel** 端口的更多信息，请参阅 Wheel。

### **Current pose (x,y, θ)** — 当前位置和方向 `off`（默认） | `on`

选择 **Current pose (x,y, θ)** 参数以启用 **Pose** 端口。有关 **Pose** 端口的更多信息，请参阅 Pose。

## 参数

### 驱动

### **Configuration** — 传动系统配置 `2-Motor Differential (Tank) Drive`（默认） | `4-Motor Differential (Tank) Drive`

根据存在的智能电机数量选择传动系统配置。如果机器人传动系统由两个电机驱动，请选择 `2-Motor Differential (Tank) Drive`。如果由四个电机驱动，请选择 `4-Motor Differential (Tank) Drive`。

### **Flip drive direction** — 更改驱动方向 `off`（默认） | `on`

此参数翻转或反转传动系统中使用的所有智能电机（左和右）的方向。默认值适用于电机与轮子之间没有方向反转的配置（例如 V5 speed bot）。

当电机和轮子之间有齿轮时，电机和轮子可能沿相反方向移动。在这种情况下，请选择此选项。错误地选择此参数会破坏航向控制的稳定性。

### **Left smart motor ports** — 选择左侧智能端口 1（默认） | `1` 到 `21`

选择左侧电机连接的智能端口。V5 Robot Brain 上有 21 个智能端口。为每个电机分配唯一的端口号。

### **Left smart motor ports** — 选择左侧智能端口 3（默认） | `1` 到 `21`

选择左侧电机连接的智能端口。V5 Robot Brain 上有 21 个智能端口。为每个电机分配唯一的端口号。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为 `4-Motor Differential (Tank) Drive`。

### **Right smart motor ports** — 选择右侧智能端口 2（默认） | `1` 到 `21`

选择右侧电机连接的智能端口。V5 Robot Brain 上有 21 个智能端口。为每个电机分配唯一的端口号。

### **Right smart motor ports** — 选择右侧智能端口 4（默认） | `1` 到 `21`

选择右侧电机连接的智能端口。V5 Robot Brain 上有 21 个智能端口。为每个电机分配唯一的端口号。

#### 依赖关系

仅当您选择 `4-Motor Differential (Tank) Drive` 参数时，此端口才可用。

### **Motor gear catridge** — 电机齿轮箱比率 18:1（默认） | `36:1` | `6:1`

选择传动系统中使用的智能电机的内部齿轮比。

### **Gear ratio (motor to wheel)** — 齿轮比（电机到轮子）的值 1（默认） | 正值

输入 VEX V5 Differential (Tank) Drive 的电机到轮子齿轮比的值。

如果电机直接连接到轮子而没有任何齿轮减速（direct drive），则 **Gear ratio (motor to wheel)** 为 1，否则设置齿轮比。例如，如果电机每旋转两圈轮子旋转一圈，则比率为 2/1 或 2。

### **VEX wheel diameter** — 轮子直径 4"（默认） | `2.75"` | `3.25"` | `5"` | `6"` | `other`

选择以 inches 为单位的轮子直径。如果您的轮子直径未列出，请选择 `other`，然后输入轮子直径。

### **Wheel diameter (m)** — 轮子直径 0.1016（默认） | 正值

输入以 meters 为单位的轮子直径。

#### 依赖关系

要启用此参数，请在 **VEX wheel diameter** 参数中选择 `other`。

### **Track width (m)** — track width 的值 0.2950（默认） | 正值

输入以 meters 为单位的 track width。

### 传感器

### **Heading sensor** — 选择航向传感器 `Inertial sensor`（默认） | `Gyroscope` | `smart motor encoders`

选择提供航向反馈的传感器。

为获得最佳结果，请选择 `Inertial sensor`。陀螺仪往往会随时间漂移，而 `smart motor encoders` 容易受到轮子打滑的影响，可能导致航向不准确。

### **Port** — 设置 Inertial Sensor 的端口 5（默认） | `1` 到 `21`

选择电机连接的智能端口。V5 Robot Brain 上有 21 个智能端口。为每个电机分配唯一的端口号。

#### 依赖关系

要启用此参数，请在 **Heading sensor** 参数中选择 `Inertial sensor`。

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的智能端口 `None`（默认） | `1` 到 `21`

如果您使用 3-Wire Expander，请指定扩展器连接到 VEX EDR V5 Robot Brain 上的智能端口。

#### 依赖关系

要启用此参数，请在 **Heading sensor** 参数中选择 `Gyroscope`。

### **Port** — 设置 gyroscope 的端口 A（默认） | `A` 到 `H`

选择模块连接到机器人上的端口。

#### 依赖关系

要启用此参数，请在 **Heading sensor** 参数中选择 `Gyroscope`。

### **Gyroscope scale factor** — 陀螺仪的比例因子 1.34（默认） | 任意正值

设置陀螺仪的比例因子值。有关更多信息，请参阅 Monitoring Signals for Gyroscope Calibration Using the VEX V5 Touch Screen

**数据类型：** `double`

### **Mounted direction** — 陀螺仪方向 Z-axis downwards（默认） | Z-axis upwards

指定陀螺仪的安装方式。此参数指示陀螺仪的方向。

### 控制器参数

**距离**

### **Drive speed (m/s)** — 设置驱动速度 0.3（默认） | 正标量

设置机器人的线速度，以 meters per second 为单位。

### **Deadband (m)** — 设置死区距离 0,04（默认） | 任意正标量

设置以 meters 为单位的死区。此参数设置位置控制的精度。一旦距离误差（当前与参考位置之间）低于死区值，机器人就会停止。

设置非常低的值可能会破坏机器人运动的稳定性。

### **Hysteresis (m)** — 设置滞环距离 0.01（默认） | 正标量

设置以 meters 为单位的滞环距离。由于机器人使用 on-off 型控制器，当机器人接近目标时，电机速度可能会多次切换。滞环可防止控制器过于频繁地切换。

**角度**

### **Turn rate (dps)** — 设置角速度 50（默认） | 正标量

设置机器人的角速度或转向速率。

### **Deadband (deg)** — 设置死区角度 4（默认） | 正标量

设置角度控制的精度。

由于即使机器人朝参考位置移动时也会控制航向角，设置低死区可能导致振荡运动。设置高 Deadband 可能会影响角度精度。

### **Hysteresis (deg)** — 设置滞环角度 5（默认） | 正标量

设置以 degrees 为单位的滞环角度。由于机器人使用 on-off 型航向控制器，电机可能会多次开启和关闭。滞环可防止控制器过于频繁地开启-关闭。

### 采样时间

### **Sample time** — 采样之间的离散间隔 `0.02`（默认） | -1 | 正标量

通过输入正标量值（例如 0.1）来指定采样时间。离散采样时间 -1 表示模块从上游模块继承其采样时间。

如果将采样时间设置为高值，机器人运动可能不稳定。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Drivetrain

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

设置差速驱动并控制机器人位姿

使用 Differential (Tank) Drive 模块控制 VEX® V5 机器人传动系统的位姿（位置和航向）。

提供位置和最终航向路点作为输入，使机器人移动到指定位置并转向最终航向。

此模块还允许您配置驱动参数，例如 track width 或 wheel size，并更改控制器参数，例如 drive speed 和 accuracy。

此模块需要 Stateflow® 许可证。

**注意**

要研究或修改模块算法，请单击模块中的任意位置。在 Simulink 工具条上出现的 **Block** 选项卡中，单击 **Disable Link**，然后单击 **Look inside mask**。
