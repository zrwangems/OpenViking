---
type: simulink-block
title: 'Simulation 3D Lidar'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
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

### **Point cloud** — 点云数据，*m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组。*m* 和 *n* 定义点云中点的数量，如下式所示：

m×n=VFOVVRES×HFOVHRES

其中：

- *V*FOV 是激光雷达的垂直视场角，以度为单位，由 **Vertical field of view (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，以度为单位，由 **Vertical resolution (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场角，以度为单位，由 **Horizontal field of view (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，以度为单位，由 **Horizontal resolution (deg)** 参数指定。

数组中的每个 *m*×*n* 条目指定传感器坐标系中检测到的点的 *x*、*y* 和 *z* 坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

您可以使用 MATLAB Function 模块中的点云函数从这些返回的点创建点云。

**数据类型：** `single`

### **Distance** — 到对象点的距离，*m*×*n* 正实值矩阵

由激光雷达传感器测量的到对象点的距离，返回为 *m*×*n* 正实值矩阵。矩阵中的每个 *m*×*n* 值对应于 **Point cloud** 输出端口返回的一个 [*x*, *y*, *z*] 坐标点。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上，选择 **Distance outport**。

**数据类型：** `single`

### **Reflectivity** — 表面材质的反射率，*m*×*n* 强度值矩阵，范围 [0, 1]

表面材质的反射率，返回为 *m*×*n* 强度值矩阵，范围在 [0, 1] 内，其中 *m* 是点云中的行数，*n* 是列数。**Reflectivity** 输出中的每个点对应于 **Point cloud** 输出中的一个点。该模块将不属于表面材质的点返回为 `NaN`。

为了计算反射率，激光雷达传感器使用 Phong 反射模型。该模型将表面反射率描述为漫反射（散射反射，例如来自粗糙表面）和镜面反射（类镜面反射，例如来自光滑表面）的组合。有关此模型的更多详细信息，请参阅 Wikipedia 上的 Phong 反射模型页面。

#### 依赖关系

要启用此端口，请选择 **Reflectivity outport** 参数。

**数据类型：** `single`

### **Labels** — 标签标识符 *m*×*n* 数组

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
| `20` | 左向箭头警告标志 |
| `21` | 右向箭头警告标志 |
| `22` | *未使用* |
| `23` | 右向单行道标志 |
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

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output semantic segmentation**。

**数据类型：** `uint8`

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标系中。在此坐标系中，*Z* 轴从地面向上指向。单位为米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标系中。当沿这些轴的正方向观察时，这些值在顺时针方向上为正。单位为弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择的车俩名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装在相对于场景原点的位置，并且在仿真期间，传感器保持静止。
- 当 **Parent name** 为某个车辆的名称时，该模块将传感器安装在相对于车辆原点的位置，并且在仿真期间，传感器随车辆移动。

要指定传感器相对于场景或车辆原点的相对位置和方向，请使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数。

车辆原点的位置取决于车辆类型。要选择车辆类型，请指定您要安装传感器的 Simulation 3D UAV Vehicle 模块的 **Type** 参数。有关车辆尺寸和车辆原点位置的更多信息，请访问每种车辆类型的参考页

### **Specify offset** — 指定相对于安装位置的偏移 `On`（默认）

选择此参数可通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位为米。

如果您通过将 **Parent name** 设置为某个车辆的名称来将传感器安装到该车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，即沿车辆前进方向观察时的左侧。
- *Z* 轴向上指向。

原点是在 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 UAV Toolbox 中 Unreal Engine 仿真的坐标系。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。单位为度。

如果通过将 **Parent name** 设置为某车辆的名称来将传感器安装到该车辆上，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，即沿车辆前进方向观察时的左侧。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的前进方向观察时，roll、pitch 和 yaw 为顺时针正方向。如果从 2D 俯视视角观察场景，则 yaw 角（也称为方位角）为逆时针正方向，因为此时是沿 *Z* 轴的负方向观察场景。

原点是在 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 UAV Toolbox 中 Unreal Engine 仿真的坐标系。

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

### **Distance outport** — 输出到被测对象点的距离 `off`（默认）| `on`

选择此参数可在 **Distance** 端口输出到被测对象点的距离。

### **Reflectivity outport** — 表面材质的输出反射率 `off`（默认）| `on`

选择此参数可在 **Reflectivity** 端口输出表面材质的反射率。

### Ground Truth

### **Output semantic segmentation** — 输出标签 ID 的语义分割图 `off`（默认）| `on`

选择此参数可在 **Labels** 端口输出标签 ID 的语义分割图。

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数可分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Lidar 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中的激光雷达传感器模型

**注意**

使用 Simulation 3D Lidar 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Lidar 模块为 3D 仿真环境中的激光雷达传感器提供接口。此环境使用 Epic Games® 的 Unreal Engine® 进行渲染。该模块返回具有指定视场和角分辨率的点云。您还可以输出从传感器到物体点的距离以及表面材质的反射率。此外，您可以输出传感器在场景世界坐标系中的位置和方向。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，请确保模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Lidar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Lidar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Lidar — `1`

有关执行顺序的详细信息，请参阅 How Unreal Engine Simulation for Automated Driving Works (Automated Driving Toolbox)。
