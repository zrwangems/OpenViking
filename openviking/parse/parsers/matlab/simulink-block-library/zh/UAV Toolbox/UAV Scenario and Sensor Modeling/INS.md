---
type: simulink-block
title: 'INS'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'ins'
documentation_source_path: 'ref/ins.html'
language: zh-CN
chinese_source: worker-translation
---

# INS

## 端口

### 输入

### **Position** — INS 传感器的位置 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的位置，以米为单位，指定为 *N*×3 实值矩阵。*N* 为采样数。

**数据类型：** `single` | `double`

### **Velocity** — INS 传感器的速度 *N*×3 实值标量矩阵

INS 传感器相对于导航坐标系的速度，以米每秒为单位，指定为 *N*×3 实值矩阵。*N* 为采样数。

**数据类型：** `single` | `double`

### **Orientation** — INS 传感器的姿态 3×3×*N* 实值数组 | *N*×4 实值矩阵 | *N*×3 欧拉角矩阵

INS 传感器相对于导航坐标系的姿态，指定为以下格式之一：

- 3×3×*N* 实值数组，其中数组的每一页（3×3 矩阵）为一个旋转矩阵。
- *N*×4 实值矩阵，其中矩阵的每一行为四元数的四个元素。
- *N*×3 欧拉角矩阵，其中矩阵的每一行为对应于 z-y-x 旋转约定的三个欧拉角。

*N* 为采样数。

**数据类型：** `single` | `double`

### **Acceleration** — INS 传感器的加速度 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的加速度，以米每二次方秒为单位，指定为 *N*×3 实值矩阵。*N* 为采样数。

#### 依赖

要启用此输入端口，请选择 **Use acceleration and angular velocity**。

**数据类型：** `single` | `double`

### **AngularVelocity** — INS 传感器的角速度 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的角速度，以度每秒为单位，指定为 *N*×3 实值矩阵。*N* 为采样数。

#### 依赖

要启用此输入端口，请选择 **Use acceleration and angular velocity**。

**数据类型：** `single` | `double`

### **HasGNSSFix** — 启用 GNSS 定位 *N*×1 逻辑向量

启用 GNSS 定位，指定为 *N*×1 逻辑向量。*N* 为采样数。将此输入指定为 `false` 以模拟 GNSS 接收机定位丢失。当 GNSS 接收机定位丢失时，位置测量值以 **Position error factor** 参数指定的速率漂移。

#### 依赖

要启用此输入端口，请选择 **Enable HasGNSSFix port**。

**数据类型：** `single` | `double`
### 输出

### **Position** — INS 传感器的位置 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的位置，以米为单位，返回为 *N*×3 实值矩阵。*N* 为输入中的采样数。

**数据类型：** `single` | `double`

### **Velocity** — INS 传感器的速度 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的速度，以米每秒为单位，返回为 *N*×3 实值矩阵。*N* 为输入中的采样数。

**数据类型：** `single` | `double`

### **Orientation** — INS 传感器的姿态 3×3×*N* 实值数组 | *N*×4 实值矩阵

INS 传感器相对于导航坐标系的姿态，返回为以下格式之一：

- 3×3×*N* 实值数组，其中数组的每一页（3×3 矩阵）为一个旋转矩阵。
- *N*×4 实值矩阵，其中矩阵的每一行为四元数的四个元素。
- *N*×3 欧拉角矩阵，其中矩阵的每一行为对应于 z-y-x 旋转约定的三个欧拉角。

*N* 为输入中的采样数。

**数据类型：** `single` | `double`

### **Acceleration** — INS 传感器的加速度 *N*×3 实值矩阵

INS 传感器相对于导航坐标系的加速度，以米每二次方秒为单位，返回为 *N*×3 实值矩阵。*N* 为采样数。

#### 依赖项

要启用此输出端口，请选择 **Use acceleration and angular velocity**。

**数据类型：** `single` | `double`

### **AngularVelocity** — INS 传感器的角速度，*N*×3 实值矩阵

INS 传感器相对于导航坐标系的角速度，以度/秒为单位，返回为 *N*×3 实值矩阵。
*N* 是采样数。

#### 依赖项

要启用此输出端口，请选择 **Use acceleration and angular velocity**。

**数据类型：** `single` | `double`

## 参数

### **Mounting location (m)** — 传感器在平台上的位置 (m) `[0 0 0]`（默认）| 形式为 [*x* *y* *z*] 的三元素实值向量

传感器在平台上的位置，以米为单位，指定为形式为 [*x*
*y*
*z*] 的三元素实值向量。该向量定义传感器原点相对于平台原点的偏移。

**数据类型：** `single` | `double`

### **Roll (X-axis) accuracy (deg)** — 横滚测量精度 (deg) `0.2`（默认）| 非负实标量

传感器本体的横滚测量精度，以度为单位，指定为非负实标量。

横滚定义为绕传感器本体 *x* 轴的旋转。
横滚噪声建模为白过程噪声，其标准差等于指定的 **Roll accuracy**（以度为单位）。

**数据类型：** `single` | `double`

### **Pitch (Y-axis) accuracy (deg)** — 俯仰测量精度 (deg) `0.2`（默认）| 非负实标量

传感器本体的俯仰测量精度，以度为单位，指定为非负实标量。

俯仰定义为绕传感器本体 *y* 轴的旋转。俯仰噪声建模为白过程噪声，其标准差等于指定的 **Pitch accuracy**（以度为单位）。

**数据类型：** `single` | `double`

### **Yaw (Z-axis) accuracy (deg)** — 偏航测量精度 (deg) `1`（默认）| 非负实标量

传感器本体的偏航测量精度，以度为单位，指定为非负实标量。

偏航定义为绕传感器本体 *z* 轴的旋转。
偏航噪声建模为白过程噪声，其标准差等于指定的 **Yaw accuracy**（以度为单位）。

**数据类型：** `single` | `double`

### **Position accuracy (m)** — 位置测量精度 (m) `1`（默认）| 非负实标量 | 1×3 非负值向量

传感器本体的位置测量精度，以米为单位，指定为非负实标量或 1×3 非负值向量。如果将该参数指定为标量值，则模块会将所有三个位置分量的精度设置为该值。

位置噪声建模为白过程噪声，其标准差等于指定的 **Position accuracy**（以米为单位）。

**数据类型：** `single` | `double`

### **Velocity accuracy (m/s)** — 速度测量精度 (m/s) `0.05`（默认）| 非负实标量

传感器本体的速度测量精度，以米/秒为单位，指定为非负实标量。

速度噪声建模为白过程噪声，其标准差等于指定的 **Velocity accuracy**（以米/秒为单位）。

**数据类型：** `single` | `double`

### **Use acceleration and angular velocity** — 使用加速度和角速度 off（默认）| on

选中此复选框可通过 **Acceleration** 和
**AngularVelocity** 输入端口分别启用模块的加速度和角速度输入。同时，模块通过
**Acceleration** 和 **AngularVelocity** 输出端口分别输出加速度和角速度测量值。此外，选择此参数还允许您指定
**Acceleration accuracy** 和 **Angular velocity
accuracy** 参数。

### **加速度精度 (m/s2)** — 加速度测量精度 (m/s2) `0`（默认）| 非负实数标量

传感器本体的加速度测量精度，以米为单位，指定为非负实数标量。

加速度噪声建模为白过程噪声，其标准差等于指定的**加速度精度**，单位为米每二次方秒。

#### 依赖关系

要启用此参数，请选择**使用加速度和角速度**。

**数据类型：** `single` | `double`

### **角速度精度 (deg/s)** — 角速度测量精度 (deg/s) `0`（默认）| 非负实数标量

传感器本体的角速度测量精度，以米为单位，指定为非负实数标量。

角速度噪声建模为白过程噪声，其标准差等于指定的**角速度精度**，单位为度每秒。

#### 依赖关系

要启用此参数，请选择**使用加速度和角速度**。

**数据类型：** `single` | `double`

### **启用 HasGNSSFix 端口** — 启用 `HasGNSSFix` 输入端口 关（默认）| 开

选中此复选框以启用 **HasGNSSFix** 输入端口。当 **HasGNSSFix** 输入指定为 `false` 时，位置测量按照**位置误差因子**参数指定的速率漂移。

### **位置误差因子** — 位置误差因子 (m) `[0 0 0]`（默认）| 非负标量 | 1×3 实值向量

无 GNSS 定位时的位置误差因子，指定为标量或 1×3 实值向量。如果将参数指定为标量值，则模块将全部三个位置分量的位置误差因子设置为该值。

当 **HasGNSSFix** 输入指定为 `false` 时，由于加速度计中的恒定偏置，位置误差以二次速率增长。位置分量 *E*(*t*) 的位置误差可表示为 *E*(*t*) = 1/2*α**t*2，其中 *α* 是对应分量的位置误差因子，*t* 是自 GNSS 定位丢失以来的时间。*x*、*y* 和 *z* 分量的计算值 *E*(*t*) 会加到**位置**输出的对应位置分量上。

#### 依赖关系

要启用此参数，请选择**启用 HasGNSSFix 端口**。

**数据类型：** `double`

### **种子** — 随机化的初始种子 `67`（默认）| 非负整数

随机数生成器算法的初始种子，指定为非负整数。

**数据类型：** `single` | `double`

### **仿真方式** — 要运行的仿真类型 `代码生成`（默认）| `解释执行`

- `解释执行` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `解释执行` 模式下，可以调试模块的源代码。
- `代码生成` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。如果模型未更改，C 代码将复用于后续仿真。此选项需要额外的启动时间。

## 所属库

Navigation Toolbox / Multisensor Positioning / Sensor Models Automated Driving Toolbox / Driving Scenario and Sensor Modeling Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

模拟 INS 传感器

该模块模拟 INS 传感器，根据相应的输入输出受噪声影响的位置、速度和姿态。该模块还可以根据相应的输入可选地输出加速度和角速度。要更改输出中存在的噪声水平，您可以调整横滚、俯仰、偏航、位置、速度、加速度和角速度精度。精度定义为噪声的标准差。
