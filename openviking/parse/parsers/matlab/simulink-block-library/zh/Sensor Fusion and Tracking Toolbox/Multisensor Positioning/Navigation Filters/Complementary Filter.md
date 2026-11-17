---
type: simulink-block
title: 'Complementary Filter'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'complementaryfilter'
documentation_source_path: 'ref/complementaryfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Complementary Filter

## 端口
```yaml
ports:
- name: Accel
  summary: 传感器机体坐标系下的加速度计读数 (m/s2) 矩阵
  direction: input
  data_types: single | double
- name: Gyro
  summary: 传感器机体坐标系下的陀螺仪读数 (rad/s) 矩阵
  direction: input
  data_types: single | double
- name: Mag
  summary: 传感器机体坐标系下的磁力计读数 (µT) 矩阵
  direction: input
  data_types: single | double
- name: Orientation
  summary: 传感器机体坐标系相对于导航坐标系的姿态 矩阵 | 数组
  direction: output
  data_types: single | double
- name: Angular Velocity
  summary: 传感器机体坐标系下的角速度 (rad/s) 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Accel** — 传感器机体坐标系下的加速度计读数 (m/s2) 矩阵

传感器机体坐标系下的加速度计读数，单位为 m/s2，指定为 *N*×3 的实数矩阵。*N* 是样本数，每一行的形式为 [*x* *y* *z*]。

**数据类型：** `single` | `double`

### **Gyro** — 传感器机体坐标系下的陀螺仪读数 (rad/s) 矩阵

传感器机体坐标系下的陀螺仪读数，单位为 rad/s，指定为 *N*×3 的实数矩阵。*N* 是样本数，每一行的形式为 [*x* *y* *z*]。

**数据类型：** `single` | `double`

### **Mag** — 传感器机体坐标系下的磁力计读数 (µT) 矩阵

传感器机体坐标系下的磁力计读数，单位为 µT，指定为 *N*×3 的实数矩阵。*N* 是样本数，每一行的形式为 [*x* *y* *z*]。

#### 依赖

要启用此输入端口，请选择 `Enable Magnetometer input` 参数。

**数据类型：** `single` | `double`
### 输出

### **Orientation** — 传感器机体坐标系相对于导航坐标系的姿态 矩阵 | 数组

传感器机体坐标系相对于导航坐标系的姿态，返回为 *M*×4 的实数矩阵或 3×3×*M* 数组。*M*×4 矩阵的每一行表示 `quaternion` 的四个分量。3×3×*M* 数组的每一页表示一个 3×3 旋转矩阵。

输入样本数 *N* 决定输出大小 *M*。

输出格式取决于 `Orientation format` 参数的值。

**数据类型：** `single` | `double`

### **Angular Velocity** — 传感器机体坐标系下的角速度 (rad/s) 矩阵

去除陀螺仪偏置后的角速度，位于传感器机体坐标系下，单位为 rad/s，返回为 *M*×3 的实数矩阵。

输入样本数 *N* 决定输出大小 *M*。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Reference frame
  summary: 导航参考坐标系 NED（默认）| ENU
  group: ''
- name: Orientation format
  summary: 姿态输出格式 quaternion（默认）| Rotation matrix
  group: ''
- name: Accelerometer gain
  summary: 加速度计增益 0.01（默认）| 范围 [0, 1] 内的实标量
  group: ''
- name: Enable Magnetometer input
  summary: 接受磁力计读数输入 on（默认）| off
  group: ''
- name: Magnetometer gain
  summary: 磁力计增益 0.01（默认）| 范围 [0, 1] 内的实标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted Execution（默认）| Code Generation
  group: ''
```

### **Reference frame** — 导航参考坐标系 `NED`（默认）| `ENU`

将导航参考坐标系指定为 `NED`（北-东-下）或 `ENU`（东-北-上）。

### **Orientation format** — 姿态输出格式 `quaternion`（默认）| `Rotation matrix`

指定 `Orientation` 的输出格式为 `quaternion` 或 `Rotation matrix`：

- `quaternion` — `Orientation` 输出 *M*×4 的实数矩阵。矩阵的每一行表示 `quaternion` 的四个分量。
- `Rotation matrix` — `Orientation` 输出 3×3×*M* 数组，其中数组的每一页是一个 3×3 旋转矩阵。

输入样本数 *N* 决定输出大小 *M*。

### **Accelerometer gain** — 加速度计增益 `0.01`（默认）| 范围 [0, 1] 内的实标量

将加速度计增益指定为范围 [0, 1] 内的实标量。该增益决定在姿态估计中，模块相对于陀螺仪测量对加速度计测量的信任程度。

**示例：** `0.02`

**数据类型：** `single` | `double`

### **Enable Magnetometer input** — 接受磁力计读数输入 `on`（默认）| `off`

选择此参数以启用 `Mag` 端口处的磁力计读数输入。

### **Magnetometer gain** — 磁力计增益 `0.01`（默认）| 范围 [0, 1] 内的实标量

将磁力计增益指定为范围 [0, 1] 内的实标量。该增益决定在姿态估计中，模块相对于陀螺仪测量对磁力计测量的信任程度。

**示例：** `0.02`

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次在此模式下运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，Simulink 会在后续仿真中复用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
## 所属库

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters Navigation Toolbox / Multisensor Positioning / Navigation Filters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

使用互补滤波器估计姿态

Complementary Filter Simulink® 模块融合加速度计、磁力计和陀螺仪传感器数据，以估计设备姿态。
