---
type: simulink-block
title: 'GPS Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'v5gpssensor'
documentation_source_path: 'vexv5/ref/v5gpssensor.html'
language: zh-CN
chinese_source: worker-translation
---

# GPS Sensor

## 端口

### 输出

### **[X, Y, θ]** — 位姿三元向量

位姿指定为 `[x y
θ]` 的三元向量，其中 x 和 y 对应位置，*θ* 对应方向角。*θ* 为顺时针正方向，其范围为 `0-360` 度。

**数据类型：** `double`

### **Error** — 位置误差估计标量

该端口输出位置误差的估计值，单位为米。

#### 依赖项

**数据类型：** `double`

### **Euler** — 偏航、俯仰和滚转角向量

**Euler** 端口按 *z*-*y*-*x* 顺序输出偏航、俯仰和滚转角，形式为 3×1 向量。

#### 依赖项

要启用此端口，请选择 **Euler angles (deg)** 参数。

**数据类型：** `double`

### **Accel** — 加速度向量

**Accel** 端口按 *x*、*y* 和 *z* 顺序输出加速度（或比力），形式为 3×1 向量。加速度以 m/s2 为单位测量。

#### 依赖项

要启用此端口，请选择 **Acceleration (m/s^2)** 参数。

**数据类型：** `double`

### **Ang rate** — 绕传感器各轴每秒旋转角度向量

**Ang rate** 端口输出绕传感器 *x-*、*y-* 和 *z-* 轴每秒旋转角度，形式为 3×1 向量。角速度以 deg/s 为单位测量。

#### 依赖项

要启用此端口，请选择 **Angular rate (deg/s)** 参数。

**数据类型：** `double`

## 参数

### **Smart Port** — VEX V5 GPS Sensor 连接到的 Smart Port 1（默认）| `1` 到 `21`

选择 V5 机器人上 VEX V5 GPS sensor 连接到的 smart port。V5 机器人上有 21 个 smart port。

为模型中的每个模块分配唯一的 smart port。如果对多个 GPS Sensor 模块使用相同端口，则最后执行的 GPS Sensor 模块会设置传感器参数。

### **Visualize** — 传感器和机器人配置 GPS 安装位置和初始位姿

单击 **Visualize** 以在图形中查看 GPS 安装位置和机器人的初始位姿。下面显示了一个示例屏幕。

### GPS 安装位置（在机器人上）

### **X (m)** — 位置坐标 0（默认）| scalar

设置 GPS 传感器相对于机器人中心的 *x* 轴位置坐标

### **Y (m)** — 位置坐标 0（默认）| scalar

设置 GPS 传感器相对于机器人中心的 *y* 轴位置坐标。

### **θ (deg)** — 方向角 0（默认）| scalar

设置 GPS 传感器相对于机器人前进轴的方向角。方向角按顺时针测量。如果 GPS 传感器位于机器人前进方向，此参数将为 `0`。

### 初始机器人位姿

这些参数帮助 GPS 传感器在场地条带不清晰可见时初始化输出。如果场地条带可见且传感器不太靠近条带，则无需设置这些参数。

### **X (m)** — 位置坐标 0（默认）| positive scalar

设置机器人在 V5 Field 上初始位置的 *x* 轴位置坐标。`0` 对应场地中心。

### **Y (m)** — 位置坐标 0（默认）| positive scalar

设置机器人在 V5 Field 上初始位置的 *y* 轴位置坐标。`0` 对应场地中心。

### **θ (deg)** — 方向角 0（默认）| positive scalar

设置机器人相对于场地的初始方向角。方向角按顺时针测量。如果机器人完全对齐场地代码条带编号 `4`，方向角将为 `0`。

### 附加输出

### **Euler Angles (deg)** — 偏航、俯仰和滚转角 `off`（默认）| `on`

选择 **Euler angles (deg)** 参数以启用 **Euler** 端口。有关更多信息，请参阅 Euler。

### **Acceleration (m/s^2)** — 加速度 `off`（默认）| `on`

选择 **Acceleration (m/s^2)** 参数以启用 **Accel** 端口。有关 **Accel** 端口的更多信息，请参阅 Accel。

### **Angular rate (deg/s)** — 传感器各轴每秒旋转角度 `off`（默认）| `on`

选择 **Angular rate (deg/s)** 参数以启用 **Ang rate** 端口。有关 **Ang rate** 端口的更多信息，请参阅 Ang rate。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

读取位置和朝向

GPS Sensor 模块从连接到机器人的 VEX V5 GPS Sensor 读取位置和朝向。

该模块将位姿输出为 3×1 向量，表示 *X*、*Y* 坐标和 *θ* 方向角。此外，它还输出位置误差的估计值。

该模块还允许你可视化传感器和机器人配置。
