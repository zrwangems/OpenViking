---
type: simulink-block
title: 'Simulation 3D Lidar'
family: 'simulation-3d'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dlidar'
documentation_source_path: 'ref/simulation3dlidar.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Lidar

## 端口

### 输出

### **Point cloud** — 点云数据，*m*×*n*×3 的正实数值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*×*n*×3 的正实数值 [*x*, *y*, *z*] 点数组。*m* 和 *n* 定义点云中的点数，如下式所示：

m×n=VFOVVRES×HFOVHRES

其中：

- *V*FOV 是激光雷达的垂直视场角，单位为度，由 **Vertical field of view (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，单位为度，由 **Vertical resolution (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场角，单位为度，由 **Horizontal field of view (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，单位为度，由 **Horizontal resolution (deg)** 参数指定。

数组中的每个 *m*×*n* 条目指定传感器坐标系中检测点的 *x*、*y* 和 *z* 坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

您可以使用 MATLAB Function 模块中的点云函数，从这些返回的点创建点云。

**数据类型：** `single`

### **Distance** — 到对象点的距离，*m*×*n* 正实数值矩阵

由激光雷达传感器测量的到对象点的距离，返回为 *m*×*n* 正实数值矩阵。矩阵中的每个 *m*×*n* 值对应 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

#### 依赖关系

要启用此端口，请在 **参数** 选项卡上选择 **Distance outport**。

**数据类型：** `single`

### **Reflectivity** — 表面材料的反射率，范围 [0, 1] 内的 *m*×*n* 强度值矩阵

表面材料的反射率，返回为范围 [0, 1] 内的 *m*×*n* 强度值矩阵，其中 *m* 是点云中的行数，*n* 是列数。**Reflectivity** 输出中的每个点对应 **Point cloud** 输出中的一个点。该模块将不属于表面材料的点返回为 `NaN`。

为了计算反射率，激光雷达传感器使用 Phong 反射模型。该模型将表面反射率描述为漫反射（散射反射，例如来自粗糙表面）和镜面反射（类似镜面的反射，例如来自光滑表面）的组合。有关此模型的更多详细信息，请参阅 Wikipedia 上的 Phong reflection model 页面。

#### 依赖关系

要启用此端口，请选择 **Reflectivity outport** 参数。

**数据类型：** `single`

### **Labels** — 标签标识符，*m*×*n* 标签标识符数组

点云中每个点的标签标识符，输出为 *m*×*n* 数组。矩阵中的每个 *m*×*n* 值对应 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

下表显示了可从 Simulation 3D Scene Configuration 模块中选择的默认场景中使用的对象 ID。如果您使用自定义场景，可以在 Unreal® Editor 中将新的对象类型分配给未使用的 ID。如果场景包含没有分配 ID 的对象，则该对象被分配 ID `0`。不支持车道标记检测。

| ID | 类型 |
| --- | --- |
| `0` | None/default |
| `1` | Building |
| `2` | *Not used* |
| `3` | Other |
| `4` | Pedestrians |
| `5` | Pole |
| `6` | Lane Markings |
| `7` | Road |
| `8` | Sidewalk |
| `9` | Vegetation |
| `10` | Vehicle |
| `11` | *Not used* |
| `12` | Generic traffic sign |
| `13` | Stop sign |
| `14` | Yield sign |
| `15` | Speed limit sign |
| `16` | Weight limit sign |
| `17-18` | *Not used* |
| `19` | Left and right arrow warning sign |
| `20` | Left chevron warning sign |
| `21` | Right chevron warning sign |
| `22` | *Not used* |
| `23` | Right one-way sign |
| `24` | *Not used* |
| `25` | School bus only sign |
| `26-38` | *Not used* |
| `39` | Crosswalk sign |
| `40` | *Not used* |
| `41` | Traffic signal |
| `42` | Curve right warning sign |
| `43` | Curve left warning sign |
| `44` | Up right arrow warning sign |
| `45-47` | *Not used* |
| `48` | Railroad crossing sign |
| `49` | Street sign |
| `50` | Roundabout warning sign |
| `51` | Fire hydrant |
| `52` | Exit sign |
| `53` | Bike lane sign |
| `54-56` | *Not used* |
| `57` | Sky |
| `58` | Curb |
| `59` | Flyover ramp |
| `60` | Road guard rail |
| 61 | Bicyclist |
| `62-66` | *Not used* |
| `67` | Deer |
| `68-70` | *Not used* |
| `71` | Barricade |
| `72` | Motorcycle |
| `73-255` | *Not used* |

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output semantic segmentation**。

**数据类型：** `uint8`

### **Translation** — 传感器位置，实数值 1×3 向量

传感器沿场景的 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标系中。在此坐标系中，*Z* 轴从地面向上。单位是米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向，实数值 1×3 向量

传感器绕场景的 *X* 轴、*Y* 轴和 *Z* 轴的滚转、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标系中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位是弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择车辆名称，这些名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，则该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数，将传感器放置在场景或车辆原点处。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的预定义安装位置之一。在仿真期间，传感器随车辆移动。

| 机器人安装位置 | 描述 | 相对于机器人原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到机器人原点，该原点位于地面上，在机器人的几何中心处。车辆，传感器安装在原点处。 | [0, 0, 0] |

当沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，滚转、俯仰和偏航在顺时针方向为正。当从上方观察车辆时，偏航角（方向角）在逆时针方向为正，因为您沿轴的负方向观察。

传感器相对于机器人的 (*X*, *Y*, *Z*) 安装位置取决于机器人类型。要指定车辆类型，请使用您要安装到的 Simulation 3D Robot 模块的 **Type** 参数。要获取某个机器人类型的 (*X*, *Y*, *Z*) 安装位置，请参阅 Simulation 3D Robot 模块。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选择此参数以使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实数值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实数值 1×3 向量。单位是米。

如果您通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆的左侧（当沿车辆前进方向观察时）。
- *Z* 轴向上指向。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 How Unreal Engine Simulation for Robots Works。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实数值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实数值 1×3 向量。滚转、俯仰和偏航分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。单位是度。

如果您通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆的左侧（当沿车辆前进方向观察时）。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，滚转、俯仰和偏航在顺时针方向为正。如果您从 2D 俯视视角观察场景，则偏航角（也称为方向角）在逆时针方向为正，因为您沿 *Z* 轴的负方向观察场景。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Robotics System Toolbox。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，单位为秒，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

### **Detection range (m)** — 激光雷达传感器测量的最大距离 `120`（默认）| 正标量

激光雷达传感器测量的最大距离，指定为小于或等于 `500` 的正标量。超出此范围的点将被忽略。单位是米。

### **Range resolution (m)** — 激光雷达传感器距离分辨率 `0.002`（默认）| 正实标量

激光雷达传感器距离的分辨率，单位为米，指定为正实标量。距离分辨率也称为 *量化因子*。该因子的最小值为 *D*range / 224，其中 *D*range 是激光雷达传感器测量的最大距离，由 **Detection range (m)** 参数指定。

### **Vertical field of view (deg)** — 垂直视场角 `40`（默认）| 正标量

激光雷达传感器的垂直视场角，指定为小于或等于 `90` 的正标量。单位是度。

### **Vertical resolution (deg)** — 垂直角分辨率 `1.25`（默认）| 正标量

激光雷达传感器的垂直角分辨率，指定为正标量。单位是度。

### **Horizontal field of view (deg)** — 水平视场角 `360`（默认）| 正标量

激光雷达传感器的水平视场角，指定为正标量。单位是度。

### **Horizontal resolution (deg)** — 水平角（方位角）分辨率 `0.16`（默认）| 正标量

激光雷达传感器的水平角（方位角）分辨率，指定为正标量。单位是度。

### **Distance outport** — 输出到测量对象点的距离 `off`（默认）| `on`

选择此参数以在 **Distance** 端口输出到测量对象点的距离。

### **Reflectivity outport** — 输出表面材料的反射率 `off`（默认）| `on`

选择此参数以在 **Reflectivity** 端口输出表面材料的反射率。

### Ground Truth

### **Output semantic segmentation** — 输出标签 ID 的语义分割图 `off`（默认）| `on`

选择此参数以在 **Labels** 端口输出标签 ID 的语义分割图。

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

## 描述

3D 仿真环境中的激光雷达传感器模型

**注意**

使用 Simulation 3D Lidar 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Lidar 模块为 3D 仿真环境中的激光雷达传感器提供接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块返回具有指定视场和角分辨率的点云。还可以输出从传感器到对象点的距离以及表面材质的反射率。此外，还可以输出传感器在场景世界坐标系中的位置和姿态。

如果将 **采样时间** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Lidar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Lidar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Lidar — `1`

有关执行顺序的更多信息，请参阅《Unreal Engine 机器人仿真工作原理》。
