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

### 输入

### **Position** — GPS 接收机在导航坐标系中的位置矩阵

将 GPS 接收机在导航坐标系中的输入位置指定为实数、有限的 *N*-by-3 矩阵。*N* 是当前帧中的样本数。矩阵行的格式取决于 **位置输入格式** 参数的值。

- 如果 **位置输入格式** 参数的值为 `Local`，则将 **Position** 的每一行指定为笛卡尔坐标，以 meters 为单位，相对于由 **参考坐标系** 参数指定的本地导航参考坐标系，其原点由 **参考位置** 参数指定。
- 如果 **位置输入格式** 参数的值为 `Geodetic`，则将 **Position** 输入的每一行指定为形式为 `[latitude longitude altitude]` 的大地坐标。`latitude` 和 `longitude` 的值以 degrees 为单位。`Altitude` 是高出 WGS84 椭球模型的高度，以 meters 为单位。

**数据类型：** `single` | `double`

### **Velocity** — 本地导航坐标系中的速度 (m/s) 矩阵

将 GPS 接收机在导航坐标系中的输入速度指定为实数、有限的 *N*-by-3 矩阵，以 meters per second 为单位。*N* 是当前帧中的样本数。矩阵行的格式取决于 **位置输入格式** 参数的值。

- 如果 **位置输入格式** 参数的值为 `Local`，则将 **Velocity** 的每一行指定为相对于本地导航参考坐标系（NED 或 ENU）的值，该坐标系由 **参考坐标系** 参数指定，其原点由 **参考位置** 参数指定。
- 如果 **位置输入格式** 参数的值为 `Geodetic`，则将 **Velocity** 的每一行指定为相对于导航参考坐标系（NED 或 ENU）的值，该坐标系由 **参考坐标系** 参数指定，其原点由 **Position** 指定。

**数据类型：** `single` | `double`

### 输出

### **LLA** — LLA 坐标系中的位置矩阵

GPS 接收机在大地纬度、经度和高度 (LLA) 坐标系中的位置，以实数、有限的 *N*-by-3 数组形式返回。纬度和经度以 degrees 为单位，北和东为正。高度以 meters 为单位。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`

### **Velocity** — 本地导航坐标系中的速度 (m/s) 矩阵

GPS 接收机在本地导航坐标系中的速度，以 meters per second 为单位，以实数、有限的 *N*-by-3 矩阵形式返回。*N* 是当前帧中的样本数。矩阵行的格式取决于 **位置输入格式** 参数的值。

- 如果 **位置输入格式** 参数的值为 `Local`，则 **Velocity** 输出是相对于本地导航参考坐标系（NED 或 ENU）的，该坐标系由 **参考坐标系** 参数指定，其原点由 **参考位置** 参数指定。
- 如果 **位置输入格式** 参数的值为 `Geodetic`，则 **Velocity** 输出是相对于导航参考坐标系（NED 或 ENU）的，该坐标系由 **参考坐标系** 参数指定，其原点由 **LLA** 指定。

**数据类型：** `single` | `double`

### **Groundspeed** — 本地导航坐标系中的水平速度大小 (m/s) 向量

GPS 接收机在本地导航坐标系中的水平速度大小，以 meters per second 为单位，以实数、有限的 *N*-element 列向量形式返回。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`

### **Course** — 本地导航坐标系中的水平速度方向 (°) 向量

GPS 接收机在本地导航坐标系中的水平速度方向，以 degrees 为单位，以实数、有限的 *N*-element 列向量形式返回，值范围为 0 到 360。北对应 0 degrees，东对应 90 degrees。

*N* 是当前帧中的样本数。

**数据类型：** `single` | `double`

## 参数

### **参考坐标系** — 参考坐标系 `NED` (默认) | `ENU`

将参考坐标系指定为 `NED`（North-East-Down）或 `ENU`（East-North-Up）。

### **位置输入格式** — 位置坐标输入格式 `Local` (默认) | `Geodetic`

将位置坐标输入格式指定为 `Local` 或 `Geodetic`。

- 如果将此参数设置为 `Local`，则 **Position** 端口的输入必须采用笛卡尔坐标形式，相对于由 **参考坐标系** 参数指定的本地导航坐标系，其原点固定并由 **参考位置** 参数定义。**Velocity** 输入端口的输入也必须相对于此本地导航坐标系。
- 如果将此参数设置为 `Geodetic`，则 **Position** 端口的输入必须是 `[latitude longitude altitude]` 形式的大地坐标。**Velocity** 输入端口的输入也必须相对于由 **参考坐标系** 参数指定的导航坐标系，其原点对应于 **Position** 端口。

### **参考位置** — 本地导航参考坐标系的原点 `[0,0,0]` (默认) | 三元素向量

将本地参考坐标系的原点指定为大地坐标 `[latitude longitude altitude]` 中的三元素行向量，其中 `altitude` 是高出参考椭球模型 WGS84 的高度。参考位置值分别以 degrees、degrees 和 meters 为单位。度数格式为十进制度 (DD)。

#### 依赖项

要启用此参数，请将 **位置输入格式** 参数设置为 `Local`。

### **水平位置精度** — 水平位置精度 (m) `1.6` (默认) | 非负实数标量

将水平位置精度指定为非负实数标量，以 meters 为单位。水平位置精度指定水平位置测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **垂直位置精度** — 垂直位置精度 (m) `3` (默认) | 非负实数标量

将垂直位置精度指定为非负实数标量，以 meters 为单位。垂直位置精度指定垂直位置测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **速度精度** — 速度精度 (m/s) `0.1` (默认) | 非负实数标量

将速度精度（每秒）指定为非负实数标量，以 meters 为单位。速度精度指定速度测量中噪声的标准差。增大此值会向测量中添加噪声，从而降低其精度。

**可调：** 是

### **衰减因子** — 全局位置噪声衰减因子 `0.999` (默认) | [0, 1] 范围内的标量

将全局位置噪声衰减因子指定为 [0, 1] 范围内的数值标量。衰减因子为 `0` 时，将全局位置噪声建模为白噪声过程。衰减因子为 1 时，将全局位置噪声建模为随机游走过程。

**可调：** 是

### **种子** — 初始种子 `67` (默认) | 非负整数

将 mt19937ar 随机数生成器算法的初始种子指定为非负整数。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling Navigation Toolbox / Multisensor Positioning / Sensor Models Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

仿真带噪声的 GPS 传感器读数

该模块基于本地坐标系或大地坐标系中的输入位置和速度，输出受噪声影响的 GPS 测量值。它使用 WGS84 地球模型将本地坐标转换为纬度-经度-高度 LLA 坐标。
