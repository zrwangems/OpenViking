---
type: simulink-block
title: 'Simulation 3D Ray Tracer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'simulation3draytracer'
documentation_source_path: 'simulation3draytracer.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ray Tracer

## 端口

### 输出

### **HitLocations** — 命中位置，实数值 *N(B+1)*×3 数组

命中位置，返回为形式为 [*X*, *Y*, *Z*] 的实数值 *N(B+1)*×3 数组，单位为 meters。*N* 是光线数量，*B* 是每条光线的反弹次数。

**数据类型：** `double`

### **HitNormals** — 命中位置处的光线法线，实数值 *N(B+1)*×3 数组

命中位置处的光线法线，返回为形式为 [*X*, *Y*, *Z*] 的实数值 *N(B+1)*×3 数组，单位为 meters。*N* 是光线数量，*B* 是每条光线的反弹次数。

**数据类型：** `double`

### **HitDistances** — 到命中位置的光线距离，实数值 *N(B+1)*×1 数组

到命中位置的光线距离，返回为实数值 *N(B+1)*×1 向量 *N*，单位为 meters。*N* 是光线数量，*B* 是每条光线的反弹次数。

**数据类型：** `double`

### **SurfaceIds** — 命中表面的对象 ID，整数值 *N(B+1)*×1 向量 | `0`

光线命中的表面的对象标识符，返回为整数值 *N(B+1)*×1 向量 *N*。*N* 是光线数量，*B* 是每条光线的反弹次数。

返回的表面标识符是在 Unreal® Editor 中创建自定义表面时指定的对象值。如果表面标识符未知，模块会为其分配 ID `0`。有关添加表面的信息，请参阅 Unreal Engine 文档中的 Add a Surface Type。

**数据类型：** `uint8`

### **IsValidHit** — 命中标志，*N*×1 向量

命中标志，返回为 *N*×1 Boolean 向量。*N* 是光线数量。值 1 表示光线命中了表面。

**数据类型：** `Boolean`

## 参数

#### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认） | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中的最高 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级名称 `Scene Origin`（默认）

传感器安装到的父级名称，指定为模型中的车辆名称，或 `Scene Origin`。您可以选择的车俩名称对应于模型中 Simulation 3D Vehicle 模块的 **Name** 参数。

### **Coordinate system** — 用于 actor 变换的坐标系 `Default`（默认） | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

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

### **Mounting location** — 传感器安装位置 `Origin`（默认） | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，模块将传感器安装到表中所述的一个预定义安装位置。在仿真期间，传感器随车辆移动。例如，下表提供了 ISO 8855 标准坐标系中的安装位置。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器安装在车辆原点，该原点位于地面上且位于车辆几何中心（请参阅 Simulink 3D Animation 中的坐标系）  车辆传感器安装在原点 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器安装在前保险杠上  车辆传感器安装在前保险杠上 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器安装在后保险杠上  车辆传感器安装在后保险杠上 | [0, 0, 180] |
| `Right mirror` | 下向传感器安装在右侧后视镜上  车辆传感器安装在右侧后视镜上 | [0, –90, 0] |
| `Left mirror` | 下向传感器安装在左侧后视镜上  车辆传感器安装在左侧后视镜上 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器安装在车辆内部的后视镜上  车辆传感器安装在后视镜上 | [0, 0, 0] |
| `Hood center` | 前向传感器安装在发动机舱盖中心  车辆传感器安装在发动机舱盖中心 | [0, 0, 0] |
| `Roof center` | 前向传感器安装在车顶中心  车辆传感器安装在车顶中心 | [0, 0, 0] |

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用传感器所安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location and orientation** 参数，并检查来自 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认） | `on`

选择此参数可使用 **Relative translation [X, Y, Z]** 和 **Relative rotation [Roll, Pitch, Yaw]** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认） | 实数值 1×3 向量

相对于传感器安装位置的平移偏移，指定为 [*X*, *Y*, *Z*] 形式的实数值 1×3 向量，单位为 meters。

您可以通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认） | 实数值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为 [*Roll*, *Pitch*, *Yaw*] 形式的实数值 1×3 向量。Roll、Pitch 和 Yaw 分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。

您可以通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

#### 参数

### **Ray origins** — 光线起点 `zeros(10,3)`（默认） | 实数值 *N*×3 数组

相对于传感器安装位置的光线起点，指定为 [*X*, *Y*, *Z*] 形式的实数值 *N*×3 数组，单位为 meters。*N* 是光线数量。

**示例：** `zeros(10,3)`

### **Ray directions** — 归一化光线方向 `ones(10,3)`（默认） | 实数值 *N*×3 数组

相对于传感器安装位置的归一化光线方向，指定为 [*X*, *Y*, *Z*] 形式的实数值 *N*×3 数组。*N* 是光线数量。单位为无量纲。

**示例：** `ones(10,3)`

### **Max ray lengths** — 最大总光线长度 `ones(10,1)*10`（默认） | 实数值 *N*×1 向量

多次反弹追踪路径的最大总光线长度，指定为实数值 *N*×1 向量，单位为 meters。*N* 是光线数量。

**示例：** `ones(10,1)*10`

### **Number of bounces** — 每条光线的反弹次数 `2`（默认） | 正整数

一条追踪在终止前可具有的反弹次数 *B*，指定为整数。

**示例：** `0`

### **Visualize trace line** — 可视化光线追踪 on（默认） | off

是否启用光线追踪器的 Unreal Engine 追踪线可视化。

### **Enable optimization** — 启用优化 on（默认） | off

是否启用光线追踪器的优化。启用此参数可使模块执行并发追踪。当追踪数量很大且您的机器具有多个核心时，请启用此参数。

### **Sample time** — 采样时间 `-1`（默认） | 正标量

模块的采样时间，单位为 seconds，指定为正标量。3D 仿真环境帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2024a 中引入**

### R2025a：设置 Coordinate system 参数

在 Simulation 3D Ray Tracer 模块中设置 **Coordinate system** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

在 3D 环境中实现光线追踪

Simulation 3D Ray Tracer 模块实现光线追踪，以获取场景中对象的位置、表面法线、表面标识符和距离。您可以指定模块参数来配置光线起点、方向和长度，以调整适用于您的场景和测试场景的光线追踪传感器模式。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Ray Tracer 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Simulation 3D Ray Tracer 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Terrain Sensor — `1`

有关执行顺序的更多信息，请参阅控制和显示执行顺序 (Simulink)。

模块的 **Coordinate system** 参数指定 actor 变换在 3D 环境中的应用方式。模块的输出也遵循指定的坐标系。
