---
type: simulink-block
title: 'Simulation 3D Camera Get'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dcameraget'
documentation_source_path: 'simulation3dcameraget.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera Get

## 端口

### 输出

### **Image** — 3D 输出相机图像，*m*-by-*n*-by-3 的 RGB 三元组值数组

3D 输出相机图像，以由 RGB 三元组值组成的 *m*-by-*n*-by-3 数组形式返回。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

## 参数

#### 安装

### **Sensor identifier** — 用于标识唯一传感器的编号 `0`（默认） | 正整数

唯一传感器标识符，指定为正整数。此编号用于标识特定传感器。传感器标识符用于区分多传感器系统中的传感器。

**示例：** 2

### **Parent name** — 父级名称 `Scene Origin`（默认） | 字符向量

父级名称。模块提供模型中父级 actor 的列表。如果选择 `Scene Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认） | `Nose` | `Cockpit` | `CockpitRight` | `CockpitLeft` | `FuselageTop` | `Tail` | `Down` | `Front` | `Back` | `Right` | `Left` | `Top` | `Bottom`

传感器安装位置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点，且 **Mounting location** 只能设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 是车辆名称（例如 `SimulinkVehicle1`）时，该模块将传感器安装到表中所描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

当车辆为 Airliner、Air Transport、General Aviation、Helicopter、Light Helicopter、Multirotor 或 Sky Hogg 之一时，`Mounting Location` 为 `Nose`、`Cockpit`、`CockpitRight`、`CockpitLeft`、`FuselageTop`、`Tail` 或 `Down` 之一。

当车辆为 CubeSat 或 SmallSat 之一时，`Mounting Location` 为 `Front`、`Back`、`Right`、`Left`、`Top`、`Bottom` 或 `Down` 之一。

**示例：** `Origin`

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认） | `on`

选择此参数可指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0,0,0]`（默认） | 实数值 1-by-3 向量

指定相对于安装位置的平移偏移，基于车辆坐标系的 *X*、*Y* 和 *Z* 轴。单位是 meters。

- *X* 轴指向车辆前方。
- *Y* 轴指向车辆左侧（面朝前方时看）。
- *Z* 轴指向上方。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移 `[0,0,0]`（默认） | 实数值 1-by-3 向量

指定相对于安装位置的旋转偏移，基于车辆坐标系的 *X*、*Y* 和 *Z* 轴。单位是 degrees。

- *横滚角* 是绕车辆坐标系 *X* 轴的旋转角度。正横滚角对应于沿 *X* 轴正方向观察时的顺时针旋转。
- *俯仰角* 是绕车辆坐标系 *Y* 轴的旋转角度。正俯仰角对应于沿 *Y* 轴正方向观察时的顺时针旋转。
- *偏航角* 是绕车辆坐标系的 *Z* 轴旋转角度。正偏航角对应于沿 *Z* 轴正方向观察时的顺时针旋转。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认） | 正标量

模块的采样时间，单位为 seconds。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

#### 参数

### **Horizontal resolution** — Pixels `uint32(1280)`（默认） | `scalar`

水平图像分辨率，单位为 pixels。

### **Vertical resolution** — Pixels `uint32(720)`（默认） | `scalar`

垂直图像分辨率，单位为 pixels。

### **Horizontal field of view** — 视场 `single(60)`（默认） | `scalar`

水平视场（FOV），单位为 deg。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2025a：安装参数名称更改

这些 **安装** 参数名已更改。

| 旧参数名 | 新参数名 |
| --- | --- |
| **Sensor identification** | **Sensor identifier** |
| **Vehicle name** | **Parent name** |
| **Vehicle mounting location** | **Mounting location** |

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Camera Get 模块仿真模型需要 Simulink 3D Animation。

## 描述

相机图像

**注意**

使用 Simulation 3D Camera Get 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Camera Get 模块提供与 3D 可视化环境中理想相机的接口。图像输出是红色、绿色和蓝色（RGB）数组。

如果将采样时间设置为 `-1`，该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Camera Get 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Simulation 3D Camera Get 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera Get — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。
