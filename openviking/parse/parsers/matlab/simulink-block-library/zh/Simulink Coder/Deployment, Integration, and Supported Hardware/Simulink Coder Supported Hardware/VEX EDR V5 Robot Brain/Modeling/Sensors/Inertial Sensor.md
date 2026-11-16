---
type: simulink-block
title: 'Inertial Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'inertialsensor'
documentation_source_path: 'vexv5/ref/inertialsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Inertial Sensor

## 端口

### 输出

### **Yaw** — 绕垂直 z 轴矢量的旋转

此端口表示绕垂直 *z* 轴的旋转。

#### 依赖关系

要启用此端口，请选择 **Euler angles (deg)** 参数。

**数据类型：** `double`

### **Pitch** — *x* 轴与水平面之间的角度矢量

此端口表示 *x* 轴与水平面之间的角度。

#### 依赖关系

要启用此端口，请选择 **Euler angles (deg)** 参数。

**数据类型：** `double`

### **Roll** — 绕纵轴矢量的旋转

此端口表示绕传感器纵轴（*x* 轴）的旋转。

#### 依赖关系

要启用此端口，请选择 **Euler angles (deg)** 参数。

**数据类型：** `double`

### **Quat** — 以四元数四元数数组形式给出的传感器方向

**Quat** 端口以 4×1 向量形式输出传感器沿 *w-*、*x-*、*y-* 和 *z-* 轴的方向。方向以四元数测量。有关四元数的更多信息，请参阅 Quaternion。

#### 依赖关系

仅当您选择 **Quaternion** 参数时，**Quat** 端口才可用。

### **Ang rate** — 绕传感器各轴每秒旋转角度矢量

**Ang rate** 端口以 3×1 向量形式输出绕传感器 *x-*、*y-* 和 *z-* 轴每秒旋转的角度。角速度以 deg/s 为单位测量。

#### 依赖关系

要启用此端口，请选择 **Angular rate (deg/s)** 参数。

**数据类型：** `double`

### **Accel** — 包括重力在内的沿传感器各轴的加速度矢量

**Accel** 端口以 3×1 向量形式输出沿传感器 *x*、*y* 和 *z* 轴的加速度。加速度以 m/s2 为单位测量，并且还包括重力加速度。

#### 依赖关系

要启用此端口，请选择 **Acceleration (m/s^2)** 参数。

**数据类型：** `double`

### **Status** — 校准状态布尔值

**Status** 端口输出校准状态。该端口将状态输出为 `boolean` 值。在校准完成之前，状态保持为 0。传感器需要 2 秒完成校准。

此表显示向量中每个元素值关于传感器校准状态所表示的含义。

| 值 | 校准状态 |
| --- | --- |
| `0` | Uncalibrated |
| `1` | Calibrated |

#### 依赖关系

要启用此端口，请选择 **Calibration Status** 参数。

**数据类型：** `Boolean`

## 参数

### **Smart Port** — 连接 VEX V5 Inertial Sensor 的 Smart Port 1（默认） | `1` 到 `21`

选择 V5 机器人上 VEX V5 惯性传感器所连接的 Smart Port。V5 机器人上有 21 个 Smart Port。

为模型中的每个模块分配唯一的 Smart Port。如果您使用多个 Inertial Sensor 模块且它们使用相同的端口，则最后执行的 Inertial Sensor 模块可能是唯一处于活动状态的模块。

### **Sample time** — 从传感器读取值的时间间隔 `0.2`（默认） | `-1` | 正标量

指定采样时间（以秒为单位），以确定模块从传感器读取值的频率。将此参数指定为 `-1` 时，Simulink® 会根据模块在模型中的上下文确定该模块的最佳采样时间。

### 选择输出

### **Euler angles (deg)** — 传感器方向 `on`（默认） | `off`

选择 **Euler angles (deg)** 参数以启用 **Yaw**、**Pitch** 和 **Roll** 端口。有关更多信息，请参阅 Yaw、Pitch 和 Roll。

### **Quaternion** — 传感器方向 `off`（默认） | `on`

选择 **Quaternion** 参数以启用 **Quat** 端口。有关 **Quat** 端口的更多信息，请参阅 Quat。

**数据类型：** `double`

### **Angular rate (deg/s)** — 传感器各轴每秒旋转角度 `off`（默认） | `on`

选择 **Angular rate (deg/s)** 参数以启用 **Ang rate** 端口。有关 **Ang rate** 端口的更多信息，请参阅 Ang rate。

### **Acceleration (m/s^2)** — 包括重力在内的沿传感器各轴的加速度 `off`（默认） | `on`

选择 **Acceleration (m/s^2)** 参数以启用 **Accel** 端口。有关 **Accel** 端口的更多信息，请参阅 Accel。

### **Calibration Status** — 校准状态 `off`（默认） | `on`

选择 **Calibration Status** 参数以启用 **Status** 端口。有关 **Status** 端口的更多信息，请参阅 Status。

### 其他选项

### **Yaw reset mode** — 用于重置惯性传感器读数的选项 `No reset`（默认） | `Reset by external signal`

指定是否必须通过外部信号重置 yaw 模式。

- `No reset` – 该模块不重置惯性传感器读数，并输出总旋转角度。

  例如，在表中 T = 1 时，惯性传感器逆时针旋转 20 度，因此输出为 20。

  在 T = 1 和 T = 2 之间，惯性传感器逆时针旋转 10 度。因此，在 T = 2 时 yaw 旋转为 30（来自 T = 1 的 20 加上来自 T = 2 的 10）。

  在此重置模式下，任意时刻的输出是先前 yaw 旋转与当前 yaw 旋转的累计和。

- `Reset by external signal`  – 惯性传感器读数会根据 `Rst` 端口的输入值重置为 0。当您向模块输入发送非 0 值时，惯性传感器读数会重置为 0。对于每个采样周期，该模块输出自上次重置以来的惯性传感器读数。

  重置模式

#### 依赖关系

要启用此参数，请选择 **Euler Angles** 参数。

### **Yaw wrap around** — 指定 yaw 环绕的角度 `No wrap around`（默认） | `0 to 360` | `-180 to 180`

指定惯性传感器的 yaw 角度限制。

将该参数设置为以下值之一：

`0 to 360` -- yaw 角度在达到 360 度后翻转为 0。

`-180 to 180` -- yaw 角度在达到 180 度后翻转为 -180 度。

`No wrap around`-- yaw 角度可以超过 360 度。

#### 依赖关系

要启用此参数，请选择 **Euler Angles** 参数。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

测量方向、加速度和角速度

Inertial Sensor 模块从连接到 VEX® V5 Brain 的惯性传感器读取数据。

默认情况下，该模块输出 yaw、pitch 和 roll（作为遵循 3-2-1 约定的欧拉角）。该模块还输出四元数、角速度和加速度。该模块以 `x-y-z` 顺序返回角速度和加速度，形式为 3×1 double 向量；四元数以 4×1 double 返回。

VEX V5 惯性传感器会自动检测并调整安装位置。这允许传感器即使在倒置安装时也能输出相同的方向（欧拉角）。有关更多信息，请参阅 Using the V5 Inertial Sensor。

启动程序时，传感器大约需要 2 秒进行校准。在启动程序时，请确保惯性传感器在水平表面上保持稳定。

**注意**

当传感器放置在水平表面上时，如果 pitch 或 roll 角度显示错误（超过 1 度），则可能需要校准加速度计。
