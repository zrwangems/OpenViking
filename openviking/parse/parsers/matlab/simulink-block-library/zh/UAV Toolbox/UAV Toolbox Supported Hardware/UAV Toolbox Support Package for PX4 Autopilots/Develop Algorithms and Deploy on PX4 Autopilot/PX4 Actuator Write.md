---
type: simulink-block
title: 'PX4 Actuator Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4actuatorwrite'
documentation_source_path: 'px4/ref/px4actuatorwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Actuator Write

## 端口

### 输入

### **Arm** — 解锁 PX4® 飞行控制器 `0` | `1`

用于解锁飞行执行器的使能信号。

值为 `0` 表示飞行执行器未解锁，而值为 `1` 表示飞行执行器已解锁。

**数据类型：** `Boolean`

### **Motor *`x`*** — 输入接受电机值 `[-1,1]`

将 Motor `x` 输入连接到表示单个标量值的信号。

如果提供的输入大于 `1` 或小于 `-1`，该模块会在内部将其分别限幅到 `1` 和 `-1`。

#### 依赖项

要启用这些端口，请从 **Motors** 参数中选择所需数量的电机 `(1-12)`。

**数据类型：** `single`

### **Servo *`x`*** — 输入接受舵机值 `[-1,1]`

将 Servo `x` 输入连接到表示单个标量值的信号。

如果提供的输入大于 `1` 或小于 `-1`，该模块会在内部将其分别限幅到 `1` 和 `-1`。

#### 依赖项

要启用这些端口，请从 **Servos** 参数中选择所需数量的舵机 `(1-8)`。

**数据类型：** `single`

### **Motor Values** — 输入以数组形式接受电机值 `-1` | `1`

将 `Motor Values` 输入连接到表示数组值的信号。

输入值 `1` 表示最大输出，值 `0` 将电机设置为其可能的最低推力，而输入 `-1` 会停止电机。

#### 依赖项

要启用此端口，请选择 **Input Motor Values as an array** 参数。

**数据类型：** `single`

### **Servo Values** — 输入以数组形式接受舵机值 `-1` | `1`

将 `Servo Values` 输入连接到表示数组值的信号。

输入值 `1` 表示最大输出，值 `0` 使舵机居中，而输入 `-1` 表示反方向的最大输出。

#### 依赖项

要启用此端口，请选择 **Input Servo Values as an array** 参数。

**数据类型：** `single`

## 参数

#### Motors 选项卡

### **Motors** — 要将值写入 Motor 编号的电机

选择要将单个标量值发送到的电机编号。模块上 **Motor** 输入端口数取决于您在此参数中选择的电机数量。

### **Input Motor Values as an array** — 用于将电机值指定为数组的选项 `off` (默认) | `on`

选择此参数以启用 **Motor Values** 输入端口。

您可以将电机值作为大小为 `1-by-12` 的数组输入。

#### Servos 选项卡

### **Servos** — 要将值写入 Servo 编号的舵机

选择要将单个标量值发送到的舵机编号。模块上 **Servo** 输入端口数取决于您在此参数中选择的舵机数量。

### **Input Servo Values as an array** — 用于将舵机值指定为数组的选项 `off` (默认) | `on`

选择此参数以启用 **Servo Values** 输入端口。

您可以将舵机值作为大小为 `1-by-8` 的数组输入。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Peripheral Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

设置电机和舵机的执行器值

PX4 Actuator Write 模块通过 PWM 和 UAVCAN 接口写入电机和舵机执行器值。PX4 Actuator Write 模块接受介于 `-1` 到 `1` 之间的单个标量值作为输入，并使用 `ActuatorTest` uORB 主题将这些值写入选定的电机或舵机。

输入值 `1` 表示最大输出，值 `0` 使舵机居中或将电机设置为其可能的最低推力，而输入 `-1` 表示最大输出但方向相反。然而，对于不支持反向运行的电机，任何小于零的值都会停止电机。

将 **Arm** 输入设置为 `true` 值会解锁执行器，而 false 用作终止开关并锁定执行器。

**配置执行器**

对于固件版本 1.14，在 Simulink 中使用 PX4 Actuator Write 模块之前，必须在 QGroundControl 中配置 PWM & AUX 引脚。要配置引脚，必须使用 QGroundControl 版本 4.3.0，该版本可从此位置下载。有关配置执行器的信息，请参阅 Configure and Assign Actuators in QGC。
