---
type: simulink-block
title: 'Simulation 3D Lidar'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dlidar'
documentation_source_path: 'simulation3dlidar.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Lidar

## 端口

### 输出

### **Point cloud** — 点云数据，*m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组。*m* 和 *n* 定义点云中的点数，如下式所示：

m×n=VFOVVRES×HFOVHRES

其中：

- *V*FOV 是激光雷达的垂直视场角，以度为单位，由 **Vertical field of view (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，以度为单位，由 **Vertical resolution (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场角，以度为单位，由 **Horizontal field of view (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，以度为单位，由 **Horizontal resolution (deg)** 参数指定。

数组中的每个 *m*×*n* 条目指定传感器坐标系中检测到的点的 *x*、*y* 和 *z* 坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

您可以使用 MATLAB Function 模块中的点云函数从这些返回的点创建点云。

**数据类型：** `single`

### **Distance** — 到对象点的距离，*m*×*n* 的正实值矩阵

由激光雷达传感器测量的到对象点的距离，返回为 *m*×*n* 的正实值矩阵。矩阵中的每个 *m*×*n* 值对应于 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上选择 **Distance outport**。

**数据类型：** `single`

### **Reflectivity** — 表面材质的反射率，*m*×*n* 的强度值矩阵，范围 [0, 1]

表面材质的反射率，返回为 *m*×*n* 的强度值矩阵，范围在 [0, 1] 内，其中 *m* 是点云中的行数，*n* 是列数。**Reflectivity** 输出中的每个点对应于 **Point cloud** 输出中的一个点。该模块将不属于表面材质的点返回为 `NaN`。

为了计算反射率，激光雷达传感器使用 Phong 反射模型。该模型将表面反射率描述为漫反射（散射反射，例如来自粗糙表面）和镜面反射（类镜面反射，例如来自光滑表面）的组合。有关此模型的更多详细信息，请参阅 Wikipedia 上的 Phong reflection model 页面。

#### 依赖关系

要启用此端口，请选择 **Reflectivity outport** 参数。

**数据类型：** `single`

### **Labels** — 标签标识符 *m*×*n* 标签标识符数组

点云中每个点的标签标识符，输出为 *m*×*n* 数组。矩阵中的每个 *m*×*n* 值对应于 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

下表显示了可从 Simulation 3D Scene Configuration 模块选择的默认场景中使用的对象 ID。如果您使用的是自定义场景，可以在 Unreal® Editor 中为未使用的 ID 分配新的对象类型。如果场景中包含未分配 ID 的对象，则该对象被分配 ID `0`。不支持车道标线检测。

| ID | 类型 |
| --- | --- |
| `0` | 无/默认 |
| `1` | 建筑物 |
| `2` | *未使用* |
| `3` | 其他 |
| `4` | 行人 |
| `5` | 杆 |
| `6` | 车道标线 |
| `7` | 道路 |
| `8` | 人行道 |
| `9` | 植被 |
| `10` | 车辆 |
| `11` | *未使用* |
| `12` | 通用交通标志 |
| `13` | 停车标志 |
| `14` | 让行标志 |
| `15` | 限速标志 |
| `16` | 限重标志 |
| `17-18` | *未使用* |
| `19` | 左右箭头警告标志 |
| `20` | 左箭头警告标志 |
| `21` | 右箭头警告标志 |
| `22` | *未使用* |
| `23` | 右单行道标志 |
| `24` | *未使用* |
| `25` | 仅校车标志 |
| `26-38` | *未使用* |
| `39` | 人行横道标志 |
| `40` | *未使用* |
| `41` | 交通信号灯 |
| `42` | 右弯警告标志 |
| `43` | 左弯警告标志 |
| `44` | 右上箭头警告标志 |
| `45-47` | *未使用* |
| `48` | 铁路道口标志 |
| `49` | 街道标志 |
| `50` | 环岛警告标志 |
| `51` | 消防栓 |
| `52` | 出口标志 |
| `53` | 自行车道标志 |
| `54-56` | *未使用* |
| `57` | 天空 |
| `58` | 路缘 |
| `59` | 立交匝道 |
| `60` | 道路护栏 |
| 61 | 骑自行车者 |
| `62-66` | *未使用* |
| `67` | 鹿 |
| `68-70` | *未使用* |
| `71` | 路障 |
| `72` | 摩托车 |
| `73-255` | *未使用* |

#### 依赖

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output semantic segmentation**。

**数据类型：** `uint8`

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。

#### 依赖

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。

#### 依赖

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分不同的传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择车辆名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，该模块将传感器放置在场景原点。

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

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **Parent name** 为 `Scene
  Origin` 时，该模块将传感器安装到场景的原点。您只能将 **Mounting location** 设置为
  `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。例如，该表提供了 ISO 8855 标准坐标系中的安装位置。

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装在车辆原点，该原点位于地面上且位于车辆的几何中心（请参阅 Coordinate Systems in Simulink 3D Animation） 传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装在前保险杠上 传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装在后保险杠上 传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装在右侧后视镜上 传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装在左侧后视镜上 传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装在车内后视镜上 传感器安装在车内后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装在发动机罩中心 传感器安装在发动机罩中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装在车顶中心 传感器安装在车顶中心的车辆 | [0, 0, 0] |

传感器相对于车辆的
*X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with
Ground Following 的 **Type** 参数。要获取某车辆类型的
*X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location and
orientation** 参数，并检查来自 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选择此参数以通过 **Relative translation [X, Y, Z]** 和 **Relative rotation [Roll, Pitch, Yaw]**
参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为 [*X*，*Y*，*Z*] 形式的实值 1×3 向量。

您可以通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为 [*Roll*，*Pitch*，*Yaw*] 形式的实值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。

您可以通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

### **Detection range (m)** — 激光雷达传感器测量的最大距离 `120`（默认）| 正标量

激光雷达传感器测量的最大距离，指定为小于或等于 `500` 的正标量。超出此范围的点将被忽略。单位为米。

### **Range resolution (m)** — 激光雷达传感器距离分辨率 `0.002`（默认）| 正实标量

激光雷达传感器距离分辨率，以米为单位，指定为正实标量。距离分辨率也称为*量化因子*。该因子的最小值为 *D*range / 224，其中 *D*range 是激光雷达传感器测量的最大距离，如 **Detection range (m)** 参数中所指定。

### **Vertical field of view (deg)** — 垂直视场 `40`（默认）| 正标量

激光雷达传感器的垂直视场，指定为小于或等于 `90` 的正标量。单位为度。

### **Vertical resolution (deg)** — 垂直角分辨率 `1.25`（默认）| 正标量

激光雷达传感器的垂直角分辨率，指定为正标量。单位为度。

### **Horizontal field of view (deg)** — 水平视场 `360`（默认）| 正标量

激光雷达传感器的水平视场，指定为正标量。单位为度。

### **Horizontal resolution (deg)** — 水平角（方位角）分辨率 `0.16`（默认）| 正标量

激光雷达传感器的水平角（方位角）分辨率，指定为正标量。单位为度。

### **Distance outport** — 到测量对象点的输出距离 `off`（默认）| `on`

选择此参数以在 **Distance** 端口输出到测量对象点的距离。

### **Reflectivity outport** — 表面材质的输出反射率 `off`（默认）| `on`

选择此参数可在 **Reflectivity** 端口输出表面材质的反射率。

### Ground Truth

### **Output semantic segmentation** — 输出标签 ID 的语义分割图 `off`（默认）| `on`

选择此参数可在 **Labels** 端口输出标签 ID 的语义分割图。

### **Output location and orientation** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数可分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a: 设置坐标系参数

在 Simulation 3D Lidar 模块中设置 **Coordinate system** 参数，以表示 3D 环境中执行器变换的坐标系。

### R2025a: 性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

## 描述

3D 仿真环境中的激光雷达传感器模型

Simulation 3D Lidar 模块为 3D 仿真环境中的激光雷达传感器提供接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块返回具有指定视场和角分辨率的点云。您还可以输出从传感器到对象点的距离以及表面材质的反射率。此外，您还可以输出传感器在场景世界坐标系中的位置和方向。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Lidar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Lidar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Lidar — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order (Simulink)。

该模块的 **Coordinate system** 参数指定执行器变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
