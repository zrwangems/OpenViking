---
type: simulink-block
title: 'IMU'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Sensor Models'
documentation_page: 'imu'
documentation_source_path: 'ref/imu.html'
language: zh-CN
chinese_source: worker-translation
---

# IMU

## 端口
```yaml
ports:
- name: Linear Acceleration
  summary: IMU 在局部导航坐标系中的加速度 (m/s2) *N*×3 实标量矩阵
  direction: input
  data_types: single | double
- name: Angular Velocity
  summary: IMU 在局部导航坐标系中的角速度 (rad/s) *N*×3 实标量矩阵
  direction: input
  data_types: single | double
- name: Orientation
  summary: IMU 在局部导航坐标系中的姿态 *N*×4 实标量数组 | 3×3×*N* 元素旋转矩阵
  direction: input
  data_types: single | double
- name: Temperature
  summary: IMU 的温度 (℃) *N*×1 实标量向量
  direction: input
  data_types: single | double
- name: Magnetic Field
  summary: 局部导航坐标系中的磁场向量 (μT) *N*×3 实标量矩阵
  direction: input
  data_types: single | double
- name: Accel
  summary: IMU 在传感器体坐标系中的加速度计测量值 (m/s2) *N*×3 实标量矩阵
  direction: output
  data_types: single | double
- name: Gyro
  summary: IMU 在传感器体坐标系中的陀螺仪测量值 (rad/s) *N*×3 实标量矩阵
  direction: output
  data_types: single | double
- name: Mag
  summary: IMU 在传感器体坐标系中的磁力计测量值 (μT) *N*×3 实标量矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Linear Acceleration** — IMU 在局部导航坐标系中的加速度 (m/s2) *N*×3 实标量矩阵

IMU 在局部导航坐标系中的加速度，指定为以米每二次方秒为单位的 *N*×3 实标量矩阵。
*N* 是当前帧中的采样数。请勿在此输入中包含重力加速度，因为传感器默认会对重力加速度进行建模。

要指定 IMU 传感器体坐标系相对于局部导航坐标系的姿态，请使用 **Orientation** 输入端口。

**数据类型：** `single` | `double`

### **Angular Velocity** — IMU 在局部导航坐标系中的角速度 (rad/s) *N*×3 实标量矩阵

IMU 传感器体坐标系在局部导航坐标系中的角速度，指定为以弧度每秒为单位的 *N*×3 标量矩阵。*N* 是当前帧中的采样数。要指定 IMU 传感器体坐标系相对于局部导航坐标系的姿态，请使用 **Orientation** 输入端口。

**数据类型：** `single` | `double`

### **Orientation** — IMU 在局部导航坐标系中的姿态 *N*×4 实标量数组 | 3×3×*N* 元素旋转矩阵

IMU 传感器体坐标系相对于局部导航坐标系的姿态，指定为 *N*×4 实标量数组或 3×3×*N* 旋转矩阵。*N*×4 数组的每一行都被假定为 `quaternion` (Sensor Fusion and Tracking Toolbox) 的四个元素。*N* 是当前帧中的采样数。

**数据类型：** `single` | `double`

### **Temperature** — IMU 的温度 (℃) *N*×1 实标量向量

IMU 的温度，指定为以摄氏度表示的 *N*×1 实标量向量。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡中，选择 **Specify temperature from input port**。

**数据类型：** `single` | `double`

### **Magnetic Field** — 局部导航坐标系中的磁场向量 (μT) *N*×3 实标量矩阵

局部导航坐标系中的磁场向量，指定为以微特斯拉为单位的 *N*×3 标量矩阵。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡中，选择 **Specify magnetic field from input port**。

**数据类型：** `single` | `double`
### 输出

### **Accel** — IMU 在传感器体坐标系中的加速度计测量值 (m/s2) *N*×3 实标量矩阵

IMU 在传感器体坐标系中的加速度计测量值，返回为以米每二次方秒为单位的 *N*×3 实标量矩阵。*N* 是当前帧中的采样数。

**数据类型：** `single` | `double`

### **Gyro** — IMU 在传感器体坐标系中的陀螺仪测量值 (rad/s) *N*×3 实标量矩阵

IMU 在传感器体坐标系中的陀螺仪测量值，返回为以弧度每秒为单位的 *N*×3 实标量矩阵。*N* 是当前帧中的采样数。

**数据类型：** `single` | `double`

### **Mag** — IMU 在传感器体坐标系中的磁力计测量值 (μT) *N*×3 实标量矩阵

IMU 在传感器体坐标系中的磁力计测量值，返回为以微特斯拉为单位的 *N*×3 实标量矩阵。*N* 是当前帧中的采样数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Reference frame
  summary: 导航参考坐标系 NED（默认）| ENU
  group: ''
- name: Specify temperature from input port
  summary: 从输入端口指定温度 关（默认）| 开
  group: ''
- name: Temperature (oC)
  summary: IMU 的工作温度（oC） 25（默认）| 实数标量
  group: ''
- name: Specify magnetic field from input port
  summary: 从输入端口指定磁场 关（默认）| 开
  group: ''
- name: Magnetic field (NED)
  summary: 在 NED 导航坐标系中表示的磁场矢量（μT） [27.5550, -2.4169, -16.0849]（默认）| 1×3 标量向量
  group: ''
- name: MagneticField (ENU)
  summary: 在 ENU 导航坐标系中表示的磁场矢量（μT） [-2.4169, 27.5550, 16.0849]（默认）| 1×3 标量向量
  group: ''
- name: Seed
  summary: 随机化的初始种子 67（默认）| 非负整数
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted Execution（默认）| Code Generation
  group: ''
- name: Maximum readings (m/s2)
  summary: 最大传感器读数（m/s2） inf（默认）| 实正标量
  group: ''
- name: Resolution ((m/s2)/LSB)
  summary: 传感器测量的分辨率（(m/s2)/LSB） 0（默认）| 实非负标量
  group: ''
- name: Constant offset bias (m/s2)
  summary: 恒定传感器偏移偏置 (m/s2) [0 0 0]（默认）| 实数标量 | 实数 3 元素行向量
  group: ''
- name: Axis skew (%)
  summary: 传感器轴偏斜 (%) diag([100 100 100])（默认）| 标量 | 3 元素行向量 | 3×3 矩阵
  group: ''
- name: Velocity random walk (m/s2/√Hz)
  summary: 速度随机游走 (m/s2/√Hz) [0 0 0]（默认）| 实数标量 | 实数 3 元素行向量
  group: ''
- name: Bias Instability (m/s2)
  summary: 偏置偏移的不稳定性 (m/s2) [0 0 0]（默认）| 实数标量 | 实数 3 元素行向量
  group: ''
- name: Bias instability filter numerator coefficients
  summary: 偏置不稳定性滤波器分子系数 fractalcoef.Numerator（默认）| 实值行向量
  group: ''
- name: Bias instability filter denominator coefficients
  summary: 偏置不稳定性滤波器分母系数 fractalcoef.Denominator（默认）| 实值行向量
  group: ''
- name: Acceleration random walk ((m/s2)(√Hz))
  summary: 加速度随机游走 ((m/s2)(√Hz)) [0 0 0]（默认）| 实数标量 | 实数 3 元素行向量
  group: ''
- name: Noise Type
  summary: 随机噪声类型 double-sided（默认）| single-sided
  group: ''
- name: Bias from temperature ((m/s2)/℃)
  summary: 温度引起的传感器偏置 ((m/s2)/℃) [0 0 0]（默认）| 实标量 | 实3元素行向量
  group: ''
- name: Temperature scale factor (%/℃)
  summary: 温度引起的比例因子误差 (%/℃) [0 0 0]（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实3元素行向量
  group: ''
- name: Maximum readings (rad/s)
  summary: 最大传感器读数 (rad/s) inf（默认）| 实正标量
  group: ''
- name: Resolution ((rad/s)/LSB)
  summary: 传感器测量分辨率 ((rad/s)/LSB) 0（默认）| 实非负标量
  group: ''
- name: Constant offset bias (rad/s)
  summary: 恒定传感器偏移偏置 (rad/s) [0 0 0]（默认）| 实标量 | 实3元素行向量
  group: ''
- name: Axis skew (%)
  summary: 传感器轴偏斜 (%) diag([100 100 100])（默认）| 标量 | 3元素行向量 | 3×3矩阵
  group: ''
- name: Bias from acceleration ((rad/s)/(m/s2)
  summary: 线性加速度引起的传感器偏置 (rad/s)/(m/s2) [0 0 0]（默认）| 实标量 | 实3元素行向量
  group: ''
- name: Angle random walk ((rad/s)/(√Hz))
  summary: 角度随机游走 ((rad/s)/(√Hz)) [0 0 0]（默认）| 实标量 | 实3元素行向量
  group: ''
- name: Bias Instability (rad/s)
  summary: 偏置偏移的不稳定性 (rad/s) [0 0 0]（默认）| 实标量 | 实3元素行向量
  group: ''
- name: 偏置不稳定性滤波器分子系数
  summary: 偏置不稳定性滤波器分子系数 fractalcoef.Numerator（默认）| 实值行向量
  group: ''
- name: 偏置不稳定性滤波器分母系数
  summary: 偏置不稳定性滤波器分母系数 fractalcoef.Denominator（默认）| 实值行向量
  group: ''
- name: 噪声类型
  summary: 随机噪声类型 double-sided（默认）| single-sided
  group: ''
- name: 速率随机游走 ((rad/s)(√Hz))
  summary: 传感器的积分白噪声 ((rad/s)(√Hz)) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: 温度引起的偏置 ((rad/s)/℃)
  summary: 温度引起的传感器偏置 ((rad/s)/℃) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: 温度比例因子 (%/℃)
  summary: 温度引起的比例因子误差 (%/℃) [0 0 0]（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实 3 元素行向量
  group: ''
- name: 最大读数 (μT)
  summary: 最大传感器读数 (μT) inf（默认）| 实正标量
  group: ''
- name: 分辨率 ((μT)/LSB)
  summary: 传感器测量分辨率 ((μT)/LSB) 0（默认）| 实非负标量
  group: ''
- name: 恒定偏移偏置 (μT)
  summary: 恒定传感器偏移偏置 (μT) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: Axis skew (%)
  summary: 传感器轴偏斜 (%) diag([100 100 100])（默认）| 标量 | 3 元素行向量 | 3×3 矩阵
  group: ''
- name: White noise PSD (μT/√Hz)
  summary: 传感器噪声的功率谱密度 (μT/√Hz) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: Bias Instability (μT)
  summary: 偏置偏移的不稳定性 (μT) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: Bias instability filter numerator coefficients
  summary: 偏置不稳定性滤波器分子系数 fractalcoef.Numerator（默认）| 实值行向量
  group: ''
- name: Bias instability filter denominator coefficients
  summary: 偏置不稳定性滤波器分母系数 fractalcoef.Denominator（默认）| 实值行向量
  group: ''
- name: Noise Type
  summary: 随机噪声类型 double-sided（默认）| single-sided
  group: ''
- name: Random walk ((μT)\*√Hz)
  summary: 传感器的积分白噪声 ((μT)\*√Hz) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: Bias from temperature (μT/℃)
  summary: 温度引起的传感器偏置 (μT/℃) [0 0 0]（默认）| 实标量 | 实 3 元素行向量
  group: ''
- name: Temperature scale factor (%/℃)
  summary: 温度引起的比例因子误差 (%/℃) [0 0 0]（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实数 3 元素行向量
  group: ''
```

#### 参数

### **Reference frame** — 导航参考坐标系 `NED`（默认）| `ENU`

导航参考坐标系，指定为 `NED`（北-东-地）或 `ENU`（东-北-天）。

**注意**

- 如果选择 NED 参考坐标系，请在 NED 参考坐标系中指定传感器输入。此外，传感器将重力加速度建模为 [0 0 9.81] m/s2。
- 如果选择 ENU 参考坐标系，请在 ENU 参考坐标系中指定传感器输入。此外，传感器将重力加速度建模为 [0 0 −9.81] m/s2。

### **Specify temperature from input port** — 从输入端口指定温度 关（默认）| 开

选中此复选框可通过 **Temperature** 输入端口输入温度。

### **Temperature (oC)** — IMU 的工作温度（oC） `25`（默认）| 实数标量

IMU 的工作温度，以摄氏度为单位，指定为实数标量。

当模块计算温度比例因子和环境漂移噪声时，25 oC 用作标称温度。

#### 依赖关系

要启用此参数，请清除 **Specify temperature from input port**。

**数据类型：** `single` | `double`

### **Specify magnetic field from input port** — 从输入端口指定磁场 关（默认）| 开

选中此复选框可通过 **Magnetic field** 输入端口输入磁场。

### **Magnetic field (NED)** — 在 NED 导航坐标系中表示的磁场矢量（μT） `[27.5550, -2.4169, -16.0849]`（默认）| 1×3 标量向量

在 NED 导航坐标系中表示的磁场矢量，指定为 1×3 标量向量。

默认磁场对应于纬度为零、经度为零、高度为零处的磁场。

#### 依赖关系

要启用此参数，请将 **Reference frame** 设置为 `NED`，并清除 **Specify magnetic field from input port**。

**数据类型：** `single` | `double`

### **MagneticField (ENU)** — 在 ENU 导航坐标系中表示的磁场矢量（μT） `[-2.4169, 27.5550, 16.0849]`（默认）| 1×3 标量向量

在 ENU 导航坐标系中表示的磁场矢量，指定为 1×3 标量向量。

默认磁场对应于纬度为零、经度为零、高度为零处的磁场。

#### 依赖关系

要启用此参数，请将 **Reference frame** 设置为 `ENU`，并清除 **Specify magnetic field from input port**。

**数据类型：** `single` | `double`

### **Seed** — 随机化的初始种子 `67`（默认）| 非负整数

随机数生成器算法的初始种子，指定为非负整数。

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。如果模型未更改，C 代码将在后续仿真中重用。此选项需要额外的启动时间。

#### 加速度计

### **Maximum readings (m/s2)** — 最大传感器读数（m/s2） `inf`（默认）| 实正标量

最大传感器读数，以 m/s2 为单位，指定为实正标量。

**数据类型：** `single` | `double`

### **Resolution ((m/s2)/LSB)** — 传感器测量的分辨率（(m/s2)/LSB） `0`（默认）| 实非负标量

传感器测量的分辨率，以 (m/s2)/LSB 为单位，指定为实非负标量。

**数据类型：** `single` | `double`

### **Constant offset bias (m/s2)** — 恒定传感器偏移偏置 (m/s2) `[0 0 0]`（默认）| 实数标量 | 实数 3 元素行向量

恒定传感器偏移偏置，单位为 m/s2，指定为实数标量或 3 元素行向量。任何标量输入都会转换为实数 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **Axis skew (%)** — 传感器轴偏斜 (%) `diag([100 100 100])`（默认）| 标量 | 3 元素行向量 | 3×3 矩阵

传感器轴偏斜，以百分比表示，指定为标量、3 元素行向量或 3×3 矩阵。矩阵的对角元素表示每个轴的未对准效应。非对角元素表示交叉轴未对准效应。测量状态
*v**measure* 通过未对准矩阵从真实状态 *v**true* 获得，如下所示：

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- 如果将属性指定为标量，则矩阵的所有非对角元素都取指定标量的值，并且所有对角元素都为 100。
- 如果将属性指定为向量 [*a*
  *b*
  *c*]，则 *m*21 =
  *m*31 = *a*，
  *m*12 =
  *m*32 = *b*，并且
  *m*13 =
  *m*23 = *c*。所有对角元素都为 100。

**数据类型：** `single` | `double`

### **Velocity random walk (m/s2/√Hz)** — 速度随机游走 (m/s2/√Hz) `[0 0 0]`（默认）| 实数标量 | 实数 3 元素行向量

速度随机游走，单位为 (m/s2/√Hz)，指定为实数标量或 3 元素行向量。此属性对应于传感器噪声的功率谱密度。任何标量输入都会转换为实数 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **Bias Instability (m/s2)** — 偏置偏移的不稳定性 (m/s2) `[0 0 0]`（默认）| 实数标量 | 实数 3 元素行向量

偏置偏移的不稳定性，单位为 m/s2，指定为实数标量或 3 元素行向量。任何标量输入都会转换为实数 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **Bias instability filter numerator coefficients** — 偏置不稳定性滤波器分子系数 `fractalcoef.Numerator`（默认）| 实值行向量

偏置不稳定性滤波器分子系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **Bias instability filter denominator coefficients** — 偏置不稳定性滤波器分母系数 `fractalcoef.Denominator`（默认）| 实值行向量

偏置不稳定性滤波器分母系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **Acceleration random walk ((m/s2)(√Hz))** — 加速度随机游走 ((m/s2)(√Hz)) `[0 0 0]`（默认）| 实数标量 | 实数 3 元素行向量

传感器的加速度随机游走，单位为 (m/s2)(√Hz)，指定为实数标量或 3 元素行向量。任何标量输入都会转换为实数 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **Noise Type** — 随机噪声类型 `double-sided`（默认）| `single-sided`

选择随机噪声类型：

- `double-sided` — 随机噪声系数的比例因子为 2。
- `single-sided` — 随机噪声系数的比例因子为 1。

**数据类型：** `single` | `double`

### **Bias from temperature ((m/s2)/℃)** — 温度引起的传感器偏置 ((m/s2)/℃) `[0 0 0]`（默认）| 实标量 | 实3元素行向量

温度引起的传感器偏置，单位为 (m/s2)/℃，指定为实标量或3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

### **Temperature scale factor (%/℃)** — 温度引起的比例因子误差 (%/℃) `[0 0 0]`（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实3元素行向量

温度引起的比例因子误差，单位为 %/℃，指定为取值范围为0到100的实标量或实3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

#### Gyroscope

### **Maximum readings (rad/s)** — 最大传感器读数 (rad/s) `inf`（默认）| 实正标量

最大传感器读数，单位为 rad/s，指定为实正标量。

**数据类型：** `single` | `double`

### **Resolution ((rad/s)/LSB)** — 传感器测量分辨率 ((rad/s)/LSB) `0`（默认）| 实非负标量

传感器测量分辨率，单位为 (rad/s)/LSB，指定为实非负标量。

**数据类型：** `single` | `double`

### **Constant offset bias (rad/s)** — 恒定传感器偏移偏置 (rad/s) `[0 0 0]`（默认）| 实标量 | 实3元素行向量

恒定传感器偏移偏置，单位为 rad/s，指定为实标量或3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

### **Axis skew (%)** — 传感器轴偏斜 (%) `diag([100 100 100])`（默认）| 标量 | 3元素行向量 | 3×3矩阵

传感器轴偏斜，以百分比表示，指定为标量、3元素行向量或3×3矩阵。矩阵的对角元素表示每个轴的失准效应。非对角元素表示交叉轴失准效应。测量状态
*v**measure* 通过失准矩阵从真实状态 *v**true* 获得，如下所示：

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- 如果将属性指定为标量，则矩阵的所有非对角元素均取该指定标量的值，且所有对角元素均为100。
- 如果将属性指定为向量 [*a*
  *b*
  *c*]，则 *m*21 =
  *m*31 = *a*，
  *m*12 =
  *m*32 = *b*，且
  *m*13 =
  *m*23 = *c*。所有对角元素均为100。

**数据类型：** `single` | `double`

### **Bias from acceleration ((rad/s)/(m/s2)** — 线性加速度引起的传感器偏置 (rad/s)/(m/s2) `[0 0 0]`（默认）| 实标量 | 实3元素行向量

线性加速度引起的传感器偏置，单位为 (rad/s)/(m/s2)，指定为实标量或3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

### **Angle random walk ((rad/s)/(√Hz))** — 角度随机游走 ((rad/s)/(√Hz)) `[0 0 0]`（默认）| 实标量 | 实3元素行向量

传感器的角度随机游走，单位为 (rad/s)/(√Hz)，指定为实标量或3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

### **Bias Instability (rad/s)** — 偏置偏移的不稳定性 (rad/s) `[0 0 0]`（默认）| 实标量 | 实3元素行向量

偏置偏移的不稳定性，单位为 rad/s，指定为实标量或3元素行向量。任何标量输入都会转换为实3元素行向量，其中每个元素均具有该输入标量值。

**数据类型：** `single` | `double`

### **偏置不稳定性滤波器分子系数** — 偏置不稳定性滤波器分子系数 `fractalcoef.Numerator`（默认）| 实值行向量

偏置不稳定性滤波器分子系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **偏置不稳定性滤波器分母系数** — 偏置不稳定性滤波器分母系数 `fractalcoef.Denominator`（默认）| 实值行向量

偏置不稳定性滤波器分母系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **噪声类型** — 随机噪声类型 `double-sided`（默认）| `single-sided`

选择随机噪声类型：

- `double-sided` — 随机噪声系数的比例因子为 2。
- `single-sided` — 随机噪声系数的比例因子为 1。

**数据类型：** `single` | `double`

### **速率随机游走 ((rad/s)(√Hz))** — 传感器的积分白噪声 ((rad/s)(√Hz)) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

传感器的积分白噪声，单位为 (rad/s)(√Hz)，指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **温度引起的偏置 ((rad/s)/℃)** — 温度引起的传感器偏置 ((rad/s)/℃) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

温度引起的传感器偏置，单位为 (rad/s)/℃, 指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **温度比例因子 (%/℃)** — 温度引起的比例因子误差 (%/℃) `[0 0 0]`（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实 3 元素行向量

温度引起的比例因子误差，单位为 %/℃, 指定为实标量或值范围为 0 到 100 的实 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

#### 磁力计

### **最大读数 (μT)** — 最大传感器读数 (μT) `inf`（默认）| 实正标量

最大传感器读数，单位为 μT, 指定为实正标量。

**数据类型：** `single` | `double`

### **分辨率 ((μT)/LSB)** — 传感器测量分辨率 ((μT)/LSB) `0`（默认）| 实非负标量

传感器测量分辨率，单位为 (μT)/LSB, 指定为实非负标量。

**数据类型：** `single` | `double`

### **恒定偏移偏置 (μT)** — 恒定传感器偏移偏置 (μT) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

恒定传感器偏移偏置，单位为 μT, 指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素都具有输入的标量值。

**数据类型：** `single` | `double`

### **Axis skew (%)** — 传感器轴偏斜 (%) `diag([100 100 100])`（默认）| 标量 | 3 元素行向量 | 3×3 矩阵

传感器轴偏斜，以百分比指定，指定为标量、3 元素行向量或 3×3 矩阵。矩阵的对角元素表示每个轴的失准效应。非对角元素表示交叉轴失准效应。测量状态 *v**measure* 通过失准矩阵从真实状态 *v**true* 获得，如下所示：

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- 如果将该属性指定为标量，则矩阵的所有非对角元素取指定标量的值，所有对角元素为 100。
- 如果将该属性指定为向量 [*a* *b* *c*]，则 *m*21 = *m*31 = *a*，*m*12 = *m*32 = *b*，且 *m*13 = *m*23 = *c*。所有对角元素均为 100。

### **White noise PSD (μT/√Hz)** — 传感器噪声的功率谱密度 (μT/√Hz) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

传感器噪声的功率谱密度，以 μT/√Hz 为单位，指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素具有输入的标量值。

**数据类型：** `single` | `double`

### **Bias Instability (μT)** — 偏置偏移的不稳定性 (μT) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

偏置偏移的不稳定性，以 μT 为单位，指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素具有输入的标量值。

**数据类型：** `single` | `double`

### **Bias instability filter numerator coefficients** — 偏置不稳定性滤波器分子系数 `fractalcoef.Numerator`（默认）| 实值行向量

偏置不稳定性滤波器分子系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **Bias instability filter denominator coefficients** — 偏置不稳定性滤波器分母系数 `fractalcoef.Denominator`（默认）| 实值行向量

偏置不稳定性滤波器分母系数，指定为实值行向量。要为分形噪声指定系数，请使用 `fractalcoef`（Sensor Fusion and Tracking Toolbox）函数。

**数据类型：** `single` | `double`

### **Noise Type** — 随机噪声类型 `double-sided`（默认）| `single-sided`

选择随机噪声类型：

- `double-sided` — 随机噪声系数的比例因子为 2。
- `single-sided` — 随机噪声系数的比例因子为 1。

**数据类型：** `single` | `double`

### **Random walk ((μT)\*√Hz)** — 传感器的积分白噪声 ((μT)\*√Hz) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

传感器的积分白噪声，以 (μT)\*√Hz 为单位，指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素具有输入的标量值。

**数据类型：** `single` | `double`

### **Bias from temperature (μT/℃)** — 温度引起的传感器偏置 (μT/℃) `[0 0 0]`（默认）| 实标量 | 实 3 元素行向量

温度引起的传感器偏置，以 μT/℃ 为单位，指定为实标量或 3 元素行向量。任何标量输入都会转换为实 3 元素行向量，其中每个元素具有输入的标量值。

**数据类型：** `single` | `double`

### **Temperature scale factor (%/℃)** — 温度引起的比例因子误差 (%/℃) `[0 0 0]`（默认）| 范围 [0,100] 内的实标量 | 范围 [0,100] 内的实数 3 元素行向量

温度引起的比例因子误差，以 %/℃ 为单位，指定为实标量或取值范围为 0 到 100 的实数 3 元素行向量。任何标量输入都会转换为实数 3 元素行向量，其中每个元素都具有该输入标量值。

**数据类型：** `single` | `double`
## 所属库

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models Navigation Toolbox / Multisensor Positioning / Sensor Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023b：为加速度计、陀螺仪和磁力计指定零偏不稳定性噪声系数和噪声类型

您可以在 **Accelerometer、Gyroscope 或 Magnetometer** 选项卡中使用这些新参数来指定用于生成零偏不稳定性噪声的传递函数系数，并指定噪声系数的比例因子。

- **Bias instability filter numerator coefficients**
- **Bias instability filter denominator
  coefficients**
- **Noise type**

## 描述

IMU 仿真模型

IMU Simulink® 模块对从由加速度计、陀螺仪和磁力计传感器组成的惯性测量单元 (IMU) 接收的数据进行建模。您可以通过使用 **Reference Frame** 参数，将模块输入的参考坐标系指定为 `NED`（北-东-地）或 `ENU`（东-北-天）坐标系。
