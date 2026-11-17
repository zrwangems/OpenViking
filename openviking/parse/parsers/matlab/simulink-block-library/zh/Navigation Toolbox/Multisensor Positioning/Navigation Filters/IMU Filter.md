---
type: simulink-block
title: 'IMU Filter'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'imufilter'
documentation_source_path: 'ref/imufilter.html'
language: zh-CN
chinese_source: worker-translation
---

# IMU Filter

## 端口

### 输入

### **Accel** — 传感器机体坐标系下的加速度计读数 (m/s2) 矩阵

传感器机体坐标系下的加速度计读数，单位为 m/s2，指定为 *N*×3 的实数矩阵。*N* 为采样数，每一行的形式为 [*x* *y* *z*]。

**数据类型：** `single` | `double`

### **Gyro** — 传感器机体坐标系下的陀螺仪读数 (rad/s) 矩阵

传感器机体坐标系下的陀螺仪读数，单位为 rad/s，指定为 *N*×3 的实数矩阵。*N* 为采样数，每一行的形式为 [*x* *y* *z*]。

**数据类型：** `single` | `double`
### 输出

### **Orientation** — 传感器机体坐标系相对于导航坐标系的姿态 矩阵 | 数组

传感器机体坐标系相对于导航坐标系的姿态，返回为 *M*×4 的实数矩阵或 3×3×*M* 数组。*M*×4 矩阵的每一行表示 `quaternion` 的四个分量。3×3×*M* 数组的每一页表示一个 3×3 旋转矩阵。

输入采样数 *N* 和 **Decimation factor** 参数决定输出大小 *M*。

输出格式取决于 **Orientation format** 参数的值。

**数据类型：** `single` | `double`

### **Angular Velocity** — 传感器机体坐标系下的角速度 (rad/s) 矩阵

去除陀螺仪偏置后的角速度，位于传感器机体坐标系下，单位为 rad/s，返回为 *M*×3 的实数矩阵。

输入采样数 *N* 和 **Decimation factor** 参数决定输出大小 *M*。

**数据类型：** `single` | `double`

## 参数

### **Reference frame** — 导航参考坐标系 `NED`（默认）| `ENU`

将导航参考坐标系指定为 `NED`（北-东-地）或 `ENU`（东-北-天）。

### **Orientation format** — 姿态输出格式 `quaternion`（默认）| `Rotation Matrix`

指定 **Orientation** 的输出格式为 `quaternion` 或 `Rotation matrix`。

- `quaternion` — **Orientation** 输出 *M*×4 的实数矩阵。矩阵的每一行表示 `quaternion` 的四个分量。
- `Rotation matrix` — **Orientation** 输出 3×3×*M* 数组，其中数组的每一页为一个 3×3 旋转矩阵。

输入采样数 *N* 和 **Decimation factor** 参数决定输出大小 *M*。

### **Decimation factor** — 抽取因子 `1`（默认）| 正整数

指定用于降低输入传感器数据速率的抽取因子，为正整数。

**Accel** 和 **Gyro** 输入的行数必须是抽取因子的整数倍。

### **Initial process noise** — 初始过程噪声 `imufilter.defaultProcessNoise`（默认）| 9×9 实数矩阵

指定初始过程噪声为 9×9 的实数矩阵。`imufilter.defaultProcessNoise` 变量包含默认值。

### **Accelerometer noise ((m/s2)2)** — 加速度计信号噪声方差 (m/s2)2 `0.0001924722`（默认）| 正实数标量

指定加速度计信号噪声的方差，单位为 (m/s2)2，为正实数标量。

### **Gyroscope noise ((rad/s)2)** — 陀螺仪信号噪声方差 (rad/s)2 `9.1385e-5`（默认）| 正实数标量

指定陀螺仪信号噪声的方差，单位为 (rad/s)2，为正实数标量。

### **Gyroscope drift noise ((rad/s)2)** — 陀螺仪偏移漂移方差 (rad/s)2 `3.0462e-13`（默认）| 正实数标量

指定陀螺仪偏移漂移的方差，单位为 (rad/s)2，为正实数标量。

### **Linear acceleration noise ((m/s2)2)** — 线性加速度噪声方差 (m/s2)2 `0.0096236100000000012`（默认）| 正实数标量

指定线性加速度噪声的方差，单位为 (m/s2)2，为正实数标量。该模块将线性加速度建模为低通滤波白噪声过程。

### **Linear acceleration decay factor** — 线性加速度漂移的衰减因子 `0.5`（默认值）| 范围 [0 1) 内的标量

将线性加速度漂移的衰减因子指定为范围 [0 1) 内的标量。如果线性加速度变化较快，请将此参数设置为较低的值。如果线性加速度变化较慢，请将此参数设置为较高的值。该模块将线性加速度漂移建模为低通滤波白噪声过程。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认值）| `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次在此模式下运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生更改，Simulink 就会在后续仿真中重用该 C 代码。此选项在初始运行时需要额外的启动时间，但相对于 `Interpreted execution` 可提高后续仿真的速度。

## 所属库

Navigation Toolbox / Multisensor Positioning / Navigation Filters Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 该模块还支持严格的单精度代码生成。

## 版本历史

**在 R2023b 中引入**

## 描述

使用 IMU Filter 估计姿态

IMU Filter Simulink® 模块融合加速度计和陀螺仪传感器数据，以估计设备姿态。
