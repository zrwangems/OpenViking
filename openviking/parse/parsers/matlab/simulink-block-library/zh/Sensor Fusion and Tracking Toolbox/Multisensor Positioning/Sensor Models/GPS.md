---
type: simulink-block
title: 'GPS'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Sensor Models'
documentation_page: 'gps'
documentation_source_path: 'ref/gps.html'
language: zh-CN
chinese_source: worker-translation
---

# GPS

## 端口
```yaml
ports:
- name: Position
  summary: GPS 接收机在导航坐标系中的位置 矩阵
  direction: input
  data_types: single | double
- name: Velocity
  summary: 本地导航坐标系中的速度 (m/s) 矩阵
  direction: input
  data_types: single | double
- name: LLA
  summary: LLA 坐标系中的位置 矩阵
  direction: output
  data_types: single | double
- name: Velocity
  summary: 本地导航坐标系中的速度 (m/s) 矩阵
  direction: output
  data_types: single | double
- name: Groundspeed
  summary: 本地导航坐标系中水平速度的幅值 (m/s) 向量
  direction: output
  data_types: single | double
- name: Course
  summary: 本地导航坐标系中水平速度的方向（°）向量
  direction: output
  data_types: single | double
```

### 输入

### **Position** — GPS 接收机在导航坐标系中的位置 矩阵

将 GPS 接收机在导航坐标系中的输入位置指定为实数、有限的 *N*×3 矩阵。*N* 是当前帧中的样本数。矩阵行的格式取决于 **Position input format** 参数的值。

- 如果 **Position input format** 参数的值为 `Local`，则将 **Position** 的每一行指定为相对于本地导航参考框架的笛卡尔坐标，单位为米，该参考框架由 **Reference frame** 参数指定，原点由 **Reference location** 参数指定。
- 如果 **Position input format** 参数的值为 `Geodetic`，则将 **Position** 输入的每一行指定为 `[latitude longitude altitude]` 形式的大地坐标。`latitude` 和 `longitude` 的值以度为单位。`Altitude` 是高于 WGS84 椭球模型的高度，单位为米。

**数据类型：** `single` | `double`

### **Velocity** — 本地导航坐标系中的速度 (m/s) 矩阵

将 GPS 接收机在导航坐标系中的输入速度指定为实数、有限的 *N*×3 矩阵，单位为米每秒。*N* 是当前帧中的样本数。矩阵行的格式取决于 **Position input format** 参数的值。

- 如果 **Position input format** 参数的值为 `Local`，则将 **Velocity** 的每一行指定为相对于本地导航参考框架（NED 或 ENU）的值，该参考框架由 **Reference frame** 参数指定，原点由 **Reference location** 参数指定。
- 如果 **Position input format** 参数的值为 `Geodetic`，则将 **Velocity** 的每一行指定为相对于导航参考框架（NED 或 ENU）的值，该参考框架由 **Reference frame** 参数指定，原点由 **Position** 指定。

**数据类型：** `single` | `double`
### 输出

### **LLA** — LLA 坐标系中的位置 矩阵

GPS 接收机在大地纬度、经度和高度 (LLA) 坐标系中的位置，返回为实数、有限的 *N*×3 数组。纬度和经度以度为单位，北和东为正。高度以米为单位。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`

### **Velocity** — 本地导航坐标系中的速度 (m/s) 矩阵

GPS 接收机在本地导航坐标系中的速度，单位为米每秒，返回为实数、有限的 *N*×3 矩阵。*N* 是当前帧中的样本数。矩阵行的格式取决于 **Position input format** 参数的值。

- 如果 **Position input format** 参数的值为 `Local`，则 **Velocity** 输出是相对于本地导航参考框架（NED 或 ENU）的值，该参考框架由 **Reference frame** 参数指定，原点由 **Reference location** 参数指定。
- 如果 **Position input format** 参数的值为 `Geodetic`，则 **Velocity** 输出是相对于导航参考框架（NED 或 ENU）的值，该参考框架由 **Reference frame** 参数指定，原点由 **LLA** 指定。

**数据类型：** `single` | `double`

### **Groundspeed** — 本地导航坐标系中水平速度的幅值 (m/s) 向量

GPS 接收机在本地导航坐标系中水平速度的幅值，单位为米每秒，返回为实数、有限的 *N* 元素列向量。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`

### **Course** — 本地导航坐标系中水平速度的方向（°）向量

GPS 接收机在本地导航坐标系中水平速度的方向，以度为单位，返回为从 0 到 360 的实数、有限 *N* 元列向量。北对应 0 度，东对应 90 度。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Reference frame
  summary: 参考坐标系 NED（默认）| ENU
  group: ''
- name: Position input format
  summary: 位置坐标输入格式 Local（默认）| Geodetic
  group: ''
- name: Reference location
  summary: 本地导航参考坐标系的原点 [0,0,0]（默认）| 三元素向量
  group: ''
- name: Horizontal position accuracy
  summary: 水平位置精度（m） 1.6（默认）| 非负实数标量
  group: ''
- name: Vertical position accuracy
  summary: 垂直位置精度（m） 3（默认）| 非负实数标量
  group: ''
- name: Velocity accuracy
  summary: 速度精度（m/s） 0.1（默认）| 非负实数标量
  group: ''
- name: Decay factor
  summary: 全局位置噪声衰减因子 0.999（默认）| 范围 [0, 1] 内的标量
  group: ''
- name: Seed
  summary: 初始种子 67（默认）| 非负整数
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Reference frame** — 参考坐标系 `NED`（默认）| `ENU`

将参考坐标系指定为 `NED`（北-东-下）或 `ENU`（东-北-上）。

### **Position input format** — 位置坐标输入格式 `Local`（默认）| `Geodetic`

将位置坐标输入格式指定为 `Local` 或 `Geodetic`。

- 如果将此参数设置为 `Local`，则 **Position** 端口的输入必须为相对于本地导航坐标系的笛卡尔坐标形式，该本地导航坐标系由 **Reference Frame** 参数指定，其原点固定并由 **Reference location** 参数定义。**Velocity** 输入端口的输入也必须相对于此本地导航坐标系。
- 如果将此参数设置为 `Geodetic`，则 **Position** 端口的输入必须为 `[latitude longitude altitude]` 形式的大地坐标。**Velocity** 输入端口的输入也必须相对于由 **Reference frame** 参数指定的导航坐标系，其原点对应于 **Position** 端口。

### **Reference location** — 本地导航参考坐标系的原点 `[0,0,0]`（默认）| 三元素向量

将本地参考坐标系的原点指定为大地坐标 `[latitude longitude altitude]` 形式的三元素行向量，其中 `altitude` 是相对于参考椭球模型 WGS84 的高度。参考位置值的单位分别为度、度和米。度的格式为十进制度（DD）。

#### 依赖关系

要启用此参数，请将 **Position input format** 参数设置为 `Local`。

### **Horizontal position accuracy** — 水平位置精度（m） `1.6`（默认）| 非负实数标量

将水平位置精度指定为非负实数标量，单位为米。水平位置精度指定水平位置测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **Vertical position accuracy** — 垂直位置精度（m） `3`（默认）| 非负实数标量

将垂直位置精度指定为非负实数标量，单位为米。垂直位置精度指定垂直位置测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **Velocity accuracy** — 速度精度（m/s） `0.1`（默认）| 非负实数标量

将每秒速度精度指定为非负实数标量，单位为米。速度精度指定速度测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **Decay factor** — 全局位置噪声衰减因子 `0.999`（默认）| 范围 [0, 1] 内的标量

将全局位置噪声衰减因子指定为范围 [0, 1] 内的数值标量。衰减因子为 `0` 时，将全局位置噪声建模为白噪声过程。衰减因子为 1 时，将全局位置噪声建模为随机游走过程。

**可调：** 是

### **Seed** — 初始种子 `67`（默认）| 非负整数

将 mt19937ar 随机数生成器算法的初始种子指定为非负整数。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，后续仿真将复用该 C 代码。
## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling Navigation Toolbox / Multisensor Positioning / Sensor Models Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

使用噪声仿真 GPS 传感器读数

该模块基于局部坐标系或大地坐标系中的输入位置和速度，输出受噪声影响的 GPS 测量值。它使用 WGS84 地球模型将局部坐标转换为纬度-经度-高度 LLA 坐标。
