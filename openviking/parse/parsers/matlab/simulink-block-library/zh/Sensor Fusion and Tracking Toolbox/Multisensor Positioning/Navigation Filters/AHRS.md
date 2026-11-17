---
type: simulink-block
title: 'AHRS'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'ahrs'
documentation_source_path: 'ref/ahrs.html'
language: zh-CN
chinese_source: worker-translation
---

# AHRS

## 端口

### 输入

### **Accel** — 传感器机体坐标系下的加速度计读数 (m/s2) *N*×3 的实数标量矩阵

传感器机体坐标系下的加速度计读数，单位为 m/s2，指定为 *N*×3 的实数标量矩阵。*N* 是采样数，`Accel` 的三列分别表示 [*x* *y* *z*] 测量值。

**数据类型：** `single` | `double`

### **Gyro** — 传感器机体坐标系下的陀螺仪读数 (rad/s) *N*×3 的实数标量矩阵

传感器机体坐标系下的陀螺仪读数，单位为 rad/s，指定为 *N*×3 的实数标量矩阵。*N* 是采样数，`Gyro` 的三列分别表示 [*x* *y* *z*] 测量值。

**数据类型：** `single` | `double`

### **Mag** — 传感器机体坐标系下的磁力计读数 (µT) *N*×3 的实数标量矩阵

传感器机体坐标系下的磁力计读数，单位为 µT，指定为 *N*×3 的实数标量矩阵。*N* 是采样数，`magReadings` 的三列分别表示 [*x* *y* *z*] 测量值。

**数据类型：** `single` | `double`
### 输出

### **Orientation** — 传感器机体坐标系相对于导航坐标系的姿态 *M*×4 的标量数组 | 3×3×*M* 元素的旋转矩阵

传感器机体坐标系相对于导航坐标系的姿态，返回为 *M*×4 的标量数组或 3×3×*M* 的旋转矩阵数组。*N*×4 数组的每一行假定为 `quaternion` 的四个元素。输入采样数 *N* 和 **Decimation Factor** 参数决定输出大小 *M*。

**数据类型：** `single` | `double`

### **Angular Velocity** — 传感器机体坐标系下的角速度 (rad/s) *M*×3 的实数标量数组（默认）

去除陀螺仪偏置后的传感器机体坐标系下的角速度，单位为 rad/s，返回为 *M*×3 的实数标量数组。输入采样数 *N* 和 **Decimation Factor** 参数决定输出大小 *M*。

**数据类型：** `single` | `double`

## 参数

#### 主

### **Reference frame** — 导航参考坐标系 `NED`（默认）| `ENU`

导航参考坐标系，指定为 `NED`（北-东-地）或 `ENU`（东-北-天）。

### **Decimation factor** — 抽取因子 `1`（默认）| 正整数

用于降低输入传感器数据速率的抽取因子，指定为正整数。

输入的行数——**Accel**、**Gyro** 和 **Mag**——必须是抽取因子的倍数。

**数据类型：** `single` | `double`

### **初始过程噪声** — 初始过程噪声 `ahrsfilter.defaultProcessNoise`（默认）| 12×12 实数标量矩阵

初始过程噪声，指定为 12×12 的实数标量矩阵。默认值 `ahrsfilter.defaultProcessNoise` 是一个 12×12 的对角矩阵，如下所示：

```
  Columns 1 through 6

   0.000006092348396                   0                   0                   0                   0                   0
                   0   0.000006092348396                   0                   0                   0                   0
                   0                   0   0.000006092348396                   0                   0                   0
                   0                   0                   0   0.000076154354947                   0                   0
                   0                   0                   0                   0   0.000076154354947                   0
                   0                   0                   0                   0                   0   0.000076154354947
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0

  Columns 7 through 12

                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
   0.009623610000000                   0                   0                   0                   0                   0
                   0   0.009623610000000                   0                   0                   0                   0
                   0                   0   0.009623610000000                   0                   0                   0
                   0                   0                   0   0.600000000000000                   0                   0
                   0                   0                   0                   0   0.600000000000000                   0
                   0                   0                   0                   0                   0   0.600000000000000
```

**数据类型：** `single` | `double`

### **姿态格式** — 姿态输出格式 `'quaternion'`（默认）| `'Rotation matrix'`

输出姿态格式，指定为 `'quaternion'` 或 `'Rotation matrix'`：

- `'quaternion'` —— 输出为 *M*×4 的实数标量数组。数组的每一行表示一个 `quaternion` 的四个分量。
- `'Rotation matrix'` —— 输出为 3×3×*M* 的旋转矩阵。

输出大小 *M* 取决于输入维度 *N* 和 **抽取因子** 参数。

**数据类型：** `char` | `string`

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间。

#### 测量噪声

### **Accelerometer noise ((m/s2)2)** — 加速度计信号噪声的方差 ((m/s2)2) `0.0001924722`（默认）| 正实数标量

加速度计信号噪声的方差，单位为 (m/s2)2，指定为正实数标量。

**数据类型：** `single` | `double`

### **Gyroscope noise ((rad/s)2)** — 陀螺仪信号噪声的方差 ((rad/s)2) `9.1385e-5`（默认）| 正实数标量

陀螺仪信号噪声的方差，单位为 (rad/s)2，指定为正实数标量。

**数据类型：** `single` | `double`

### **Magnetometer noise (μT2)** — 磁力计信号噪声的方差 (μT2) `0.1`（默认）| 正实数标量

磁力计信号噪声的方差，单位为 μT2，指定为正实数标量。

**数据类型：** `single` | `double`

### **Gyroscope drift noise (rad/s)** — 陀螺仪偏移漂移的方差 ((rad/s)2) `3.0462e-13`（默认）| 正实数标量

陀螺仪偏移漂移的方差，单位为 (rad/s)2，指定为正实数标量。

**数据类型：** `single` | `double`

#### 环境噪声

### **Linear acceleration noise ((m/s2)2)** — 线性加速度噪声的方差 (m/s2)2 `0.0096236100000000012`（默认）| 正实数标量

线性加速度噪声的方差，单位为 (m/s2)2，指定为正实数标量。线性加速度建模为低通滤波白噪声过程。

**数据类型：** `single` | `double`

### **Magnetic disturbance noise (μT2)** — 磁干扰噪声的方差 ((μT)2) `0.5`（默认）| 实有限正标量

磁干扰噪声的方差，单位为 μT2，指定为实有限正标量。

**数据类型：** `single` | `double`

### **Linear acceleration decay factor** — 线性加速度漂移的衰减因子 `0.5`（默认）| 范围 [0,1) 内的标量

线性加速度漂移的衰减因子，指定为范围 [0,1) 内的标量。如果线性加速度变化较快，请将此参数设置为较低的值。如果线性加速度变化较慢，请将此参数设置为较高的值。线性加速度漂移建模为低通滤波白噪声过程。

**数据类型：** `single` | `double`

### **Magnetic disturbance decay factor** — 磁干扰的衰减因子 `0.5`（默认）| 范围 [0,1] 内的正标量

磁干扰的衰减因子，指定为范围 [0,1] 内的正标量。磁干扰建模为一阶马尔可夫过程。

**数据类型：** `single` | `double`

### **Magnetic field strength (μT)** — 磁场强度 (μT) `50`（默认）| 实正标量

磁场强度，单位为 μT，指定为实正标量。磁场强度是当前位置处地球磁场强度的估计值。

**数据类型：** `single` | `double`

## 所属库

Navigation Toolbox / Multisensor Positioning / Navigation Filters Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 此模块还支持严格的单精度代码生成。

## 版本历史

**在 R2020a 中引入**

## 描述

根据加速度计、陀螺仪和磁力计读数计算姿态

`AHRS`
Simulink® 模块融合加速度计、磁力计和陀螺仪传感器数据来估计设备姿态。
