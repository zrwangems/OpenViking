---
type: simulink-block
title: 'Simulation 3D Lidar'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3dlidar'
documentation_source_path: 'ref/simulation3dlidar.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Lidar

## 端口

### 输出

### **Point cloud** — 点云数据 *m*×*n*×3 正实值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*×*n*×3 正实值 [*x*, *y*, *z*] 点数组。*m* 和 *n* 定义点云中点的数量，如下式所示：

m×n=VFOVVRES×HFOVHRES

其中：

- *V*FOV 是激光雷达的垂直视场角，单位为 degrees，由 **Vertical field of view (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，单位为 degrees，由 **Vertical resolution (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场角，单位为 degrees，由 **Horizontal field of view (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，单位为 degrees，由 **Horizontal resolution (deg)** 参数指定。

数组中的每个 *m*×*n* 条目指定传感器坐标系中检测到的点的 *x*、*y* 和 *z* 坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

您可以使用 MATLAB Function 模块中的点云函数从这些返回的点创建点云。有关点云处理函数的列表，请参阅 Lidar Processing。有关使用这些函数的示例，请参阅 Design Lidar SLAM Algorithm Using Unreal Engine Simulation Environment。

**数据类型：** `single`

### **Distance** — 到目标点的距离 *m*×*n* 正实值矩阵

激光雷达传感器测得的到目标点的距离，返回为 *m*×*n* 正实值矩阵。矩阵中的每个 *m*×*n* 值对应于 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

#### 依赖项

要启用此端口，请在 **参数** 选项卡上选择 **Distance outport**。

**数据类型：** `single`

### **Reflectivity** — 表面材质的反射率 *m*×*n* 强度值矩阵，范围为 [0, 1]

表面材质的反射率，返回为范围为 [0, 1] 的 *m*×*n* 强度值矩阵，其中 *m* 是点云中的行数，*n* 是列数。**Reflectivity** 输出中的每个点对应于 **Point cloud** 输出中的一个点。该模块将不属于表面材质的点返回为 `NaN`。

为了计算反射率，激光雷达传感器使用 Phong 反射模型。此模型将表面反射率描述为漫反射（散射反射，例如来自粗糙表面的反射）和镜面反射（类似镜面的反射，例如来自光滑表面的反射）的组合。有关此模型的更多详细信息，请参阅 Wikipedia 上的 Phong reflection model 页面。

#### 依赖项

要启用此端口，请选择 **Reflectivity outport** 参数。

**数据类型：** `single`

### **Labels** — 标签标识符 *m*×*n* 标签标识符数组

点云中每个点的标签标识符，输出为 *m*×*n* 数组。矩阵中的每个 *m*×*n* 值对应于 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

下表显示了可从 Simulation 3D Scene Configuration 模块选择的默认场景中使用的对象 ID。如果您使用的是自定义场景，则可以在 Unreal® Editor 中将新的对象类型分配给未使用的 ID。有关更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景包含未分配 ID 的对象，则为该对象分配 ID `0`。不支持检测车道标线。

| ID | 类型 |
| --- | --- |
| `0` | 无/默认 |
| `1` | 建筑 |
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
| `20` | 左人字形警告标志 |
| `21` | 右人字形警告标志 |
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
| 61 | 骑自行车的人 |
| `62-66` | *未使用* |
| `67` | 鹿 |
| `68-70` | *未使用* |
| `71` | 路障 |
| `72` | 摩托车 |
| `73-255` | *未使用* |

#### 依赖项

要启用此端口，请在 **真值** 选项卡上选择 **Output semantic segmentation**。

**数据类型：** `uint8`

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标系中。在此坐标系中，*Z* 轴从地面向上指向。单位为 meters。

#### 依赖项

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的 Roll、pitch 和 yaw 方向。**Rotation** 值位于场景的世界坐标系中。当沿这些轴的正方向观察时，这些值为顺时针正。单位为 radians。

#### 依赖项

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` (默认) | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin` (默认) | 车辆名称

传感器安装到的父对象名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择的车名对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，则该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin` (默认) | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器放置在相对于场景原点或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。您只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装在车辆原点，该原点位于地面上且处于车辆的几何中心（请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox）  车辆传感器安装在原点 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装在前保险杠  车辆传感器安装在前保险杠 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装在后保险杠  车辆传感器安装在后保险杠 | [0, 0, 180] |
| `Right mirror` | 下向传感器，安装在右侧后视镜  车辆传感器安装在右侧后视镜 | [0, –90, 0] |
| `Left mirror` | 下向传感器，安装在左侧后视镜  车辆传感器安装在左侧后视镜 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装在车内后视镜  车辆传感器安装在车内后视镜 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装在发动机舱盖中心  车辆传感器安装在发动机舱盖中心 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装在车顶中心  车辆传感器安装在车顶中心 | [0, 0, 0] |

当沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 分别为顺时针正。当从上方俯视车辆时，yaw 角（方向角）为逆时针正，因为您是沿该轴的负方向观察的。

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标系中的位置，请打开传感器模块。然后，在 **真值** 选项卡上，选择 **Output location (m) and orientation (rad)** 参数，并检查 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off` (默认) | `on`

选择此参数，以使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为 [*X*, *Y*, *Z*] 形式的实值 1×3 向量。单位为 meters。

如果您通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆上，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。

原点是在 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为 [*Roll*, *Pitch*, *Yaw*] 形式的实值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。单位为 degrees。

如果您通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆上，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。
- 当沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 分别为顺时针正。如果从 2D 俯视视角查看场景，则 yaw 角（也称为方向角）为逆时针正，因为您是沿 *Z* 轴的负方向查看场景的。

原点是在 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1` (默认) | 正标量

模块的采样时间，以 seconds 为单位，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

### **Detection range (m)** — 激光雷达传感器测得的最大距离 `120` (默认) | 正标量

激光雷达传感器测得的最大距离，指定为小于或等于 `500` 的正标量。此范围之外的点将被忽略。单位为 meters。

### **Range resolution (m)** — 激光雷达传感器距离分辨率 `0.002` (默认) | 正实标量

激光雷达传感器距离分辨率，以 meters 为单位，指定为正实标量。距离分辨率也称为*量化因子*。此因子的最小值为 *D*range / 224，其中 *D*range 是激光雷达传感器测得的最大距离，如 **Detection range (m)** 参数中所指定。

### **Vertical field of view (deg)** — 垂直视场角 `40` (默认) | 正标量

激光雷达传感器的垂直视场角，指定为小于或等于 `90` 的正标量。单位为 degrees。

### **Vertical resolution (deg)** — 垂直角分辨率 `1.25` (默认) | 正标量

激光雷达传感器的垂直角分辨率，指定为正标量。单位为 degrees。

### **Horizontal field of view (deg)** — 水平视场角 `360` (默认) | 正标量

激光雷达传感器的水平视场角，指定为正标量。单位为 degrees。

### **Horizontal resolution (deg)** — 水平角（方位角）分辨率 `0.16` (默认) | 正标量

激光雷达传感器的水平角（方位角）分辨率，指定为正标量。单位为 degrees。

### **Distance outport** — 输出到测量目标点的距离 `off` (默认) | `on`

选择此参数以在 **Distance** 端口输出到测量目标点的距离。

### **Reflectivity outport** — 输出表面材质的反射率 `off` (默认) | `on`

选择此参数以在 **Reflectivity** 端口输出表面材质的反射率。

### 真值

### **Output semantic segmentation** — 输出标签 ID 的语义分割图 `off` (默认) | `on`

选择此参数以在 **Labels** 端口输出标签 ID 的语义分割图。

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off` (默认) | `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以在 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Lidar 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中的激光雷达传感器模型

**注意**

使用 Simulation 3D Lidar 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Lidar 模块提供与 3D 仿真环境中激光雷达传感器的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块返回具有指定视场角和角分辨率的点云。您还可以输出从传感器到目标点的距离以及表面材质的反射率。此外，您可以输出传感器在场景世界坐标系中的位置和方向。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中有 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Lidar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Lidar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Lidar — `1`

有关执行顺序的详细信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
