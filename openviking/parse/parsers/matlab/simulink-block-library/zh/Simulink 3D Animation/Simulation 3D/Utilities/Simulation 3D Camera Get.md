---
type: simulink-block
title: 'Simulation 3D Camera Get'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Utilities'
documentation_page: 'simulation3dcameraget'
documentation_source_path: 'simulation3dcameraget.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera Get

## 端口
```yaml
ports:
- name: Image
  summary: 3D 输出相机图像，*m*×*n*×3 的 RGB 三元组值数组
  direction: output
  data_types: int8 | uint8
```

### 输出

### **Image** — 3D 输出相机图像，*m*×*n*×3 的 RGB 三元组值数组

3D 输出相机图像，以 *m*×*n*×3 的 RGB 三元组值数组形式返回。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`
## 参数
```yaml
parameters:
- name: Sensor identifier
  summary: 用于标识唯一传感器的编号 0（默认）| 正整数
  group: ''
- name: Parent name
  summary: 父级名称 Scene Origin（默认）| 字符向量
  group: ''
- name: Coordinate system
  summary: 用于 actor 变换的坐标系 Default（默认）| MATLAB | ISO8855 | AERO | VRML | SAE
  group: ''
- name: Mounting location
  summary: 传感器安装位置 Origin（默认）| Front bumper | Rear bumper | Right mirror | Left mirror | Rearview mirror | Hood center | Roof
    center
  group: ''
- name: Specify offset
  summary: 指定相对于安装位置的偏移量 off（默认）| on
  group: ''
- name: Relative translation [X, Y, Z]
  summary: 相对于安装位置的平移偏移量 [0,0,0]（默认）| 实值 1×3 向量
  group: ''
- name: Relative rotation [Roll, Pitch, Yaw]
  summary: 相对于安装位置的旋转偏移量 [0,0,0]（默认）| 实值 1×3 向量
  group: ''
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: ''
- name: Horizontal resolution
  summary: 像素 uint32(1280)（默认）| scalar
  group: ''
- name: Vertical resolution
  summary: 像素 uint32(720)（默认）| scalar
  group: ''
- name: Horizontal field of view
  summary: 视场角 single(60)（默认）| scalar
  group: ''
```

#### 安装

### **Sensor identifier** — 用于标识唯一传感器的编号 `0`（默认）| 正整数

唯一传感器标识符，指定为正整数。此编号用于标识特定传感器。传感器标识符用于区分多传感器系统中的不同传感器。

**示例：** 2

### **Parent name** — 父级名称 `Scene Origin`（默认）| 字符向量

父级名称。模块提供模型中父级 actor 的列表。如果选择 `Scene Origin`，模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Coordinate system** — 用于 actor 变换的坐标系 `Default`（默认）| `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定 actor 在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB® 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例：** `MATLAB`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center`

传感器安装位置。

- 当 **Parent name** 为 `Scene
  Origin` 时，模块将传感器安装到场景原点，并且 **Mounting location** 只能设置为
  `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称（例如
  `SimulinkVehicle1`）时，模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，
  传感器随车辆移动。例如，
  该表提供了 ISO 8855 标准坐标系中的安装位置。

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆的几何中心（参见 Coordinate Systems in Simulink 3D Animation） 传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠 传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠 传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装到右侧后视镜 传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装到左侧后视镜 传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜 传感器安装在车内后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到发动机舱盖中心 传感器安装在发动机舱盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心 传感器安装在车顶中心的车辆 | [0, 0, 0] |

传感器相对于车辆的 (*X*, *Y*, *Z*)
位置取决于车辆类型。要指定
车辆类型，请使用您所安装到的 Simulation 3D Vehicle with
Ground Following 模块的 **Type** 参数。

例如，这些表显示了 ISO
8855 标准坐标系中传感器的 *X*、
*Y* 和 *Z* 位置。

**Box Truck — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 5.10 | 0 | 0.60 |
| `Rear bumper` | –5 | 0 | 0.60 |
| `Right mirror` | 2.90 | 1.60 | 2.10 |
| `Left mirror` | 2.90 | –1.60 | 2.10 |
| `Rearview mirror` | 2.60 | 0.20 | 2.60 |
| `Hood center` | 3.80 | 0 | 2.10 |
| `Roof center` | 1.30 | 0 | 4.20 |

**Hatchback — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 1.93 | 0 | 0.51 |
| `Rear bumper` | –1.93 | 0 | 0.51 |
| `Right mirror` | 0.43 | –0.84 | 1.01 |
| `Left mirror` | 0.43 | 0.84 | 1.01 |
| `Rearview mirror` | 0.32 | 0 | 1.27 |
| `Hood center` | 1.44 | 0 | 1.01 |
| `Roof center` | 0 | 0 | 1.57 |

**Muscle Car — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.47 | 0 | 0.45 |
| `Rear bumper` | –2.47 | 0 | 0.45 |
| `Right mirror` | 0.43 | –1.08 | 1.01 |
| `Left mirror` | 0.43 | 1.08 | 1.01 |
| `Rearview mirror` | 0.32 | 0 | 1.20 |
| `Hood center` | 1.28 | 0 | 1.14 |
| `Roof center` | –0.25 | 0 | 1.58 |

**Sedan — Sensor Locations Relative to Vehicle Origin**

| 安装位置 | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.42 | 0 | 0.51 |
| `Rear bumper` | –2.42 | 0 | 0.51 |
| `Right mirror` | 0.59 | –0.94 | 1.09 |
| `Left mirror` | 0.59 | 0.94 | 1.09 |
| `Rearview mirror` | 0.43 | 0 | 1.31 |
| `Hood center` | 1.46 | 0 | 1.11 |
| `Roof center` | –0.45 | 0 | 1.69 |

**小型皮卡车 — 传感器位置相对于车辆原点**

| 安装位置 | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 3.07 | 0 | 0.51 |
| `Rear bumper` | –3.07 | 0 | 0.51 |
| `Right mirror` | 1.10 | –1.13 | 1.52 |
| `Left mirror` | 1.10 | 1.13 | 1.52 |
| `Rearview mirror` | 0.85 | 0 | 1.77 |
| `Hood center` | 2.22 | 0 | 1.59 |
| `Roof center` | 0 | 0 | 2.27 |

**运动型多用途车 — 传感器位置相对于车辆原点**

| 安装位置 | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.42 | 0 | 0.51 |
| `Rear bumper` | –2.42 | 0 | 0.51 |
| `Right mirror` | 0.60 | –1 | 1.35 |
| `Left mirror` | 0.60 | 1 | 1.35 |
| `Rearview mirror` | 0.39 | 0 | 1.55 |
| `Hood center` | 1.58 | 0 | 1.39 |
| `Roof center` | –0.56 | 0 | 2 |

**示例：** `Origin`

### **Specify offset** — 指定相对于安装位置的偏移量 `off`（默认）| `on`

选择此参数以指定相对于安装位置的偏移量。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移量 `[0,0,0]`（默认）| 实值 1×3 向量

指定相对于安装位置绕 *X*、*Y* 和 *Z* 轴的平移偏移量。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移量 `[0,0,0]`（默认）| 实值 1×3 向量

指定相对于安装位置绕 *X*、*Y* 和 *Z* 轴的旋转偏移量。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

#### 参数

### **Horizontal resolution** — 像素 `uint32(1280)`（默认）| `scalar`

水平图像分辨率，以像素为单位。

### **Vertical resolution** — 像素 `uint32(720)`（默认）| `scalar`

垂直图像分辨率，以像素为单位。

### **Horizontal field of view** — 视场角 `single(60)`（默认）| `scalar`

水平视场角（FOV），以度为单位。
## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2025a：安装参数名称变更

以下 **Mounting** 参数名称已更改。

| 旧参数名称 | 新参数名称 |
| --- | --- |
| **Sensor identification** | **Sensor identifier** |
| **Vehicle name** | **Parent name** |
| **Vehicle mounting location** | **Mounting location** |

### R2025a：设置坐标系参数

在 Simulation 3D Camera Get 模块中设置 **Coordinate system** 参数，以表示 3D 环境中执行器变换的坐标系。

## 描述

相机图像

Simulation 3D Camera Get 模块为 3D 可视化环境中的理想相机提供接口。图像输出为红、绿、蓝（RGB）数组。

如果将采样时间设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

确认 Simulation 3D Scene Configuration 模块在 Simulation 3D Camera Get 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Simulation 3D Camera Get 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera Get — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order (Simulink)。

该模块的 **Coordinate system** 参数指定了 actor 变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
