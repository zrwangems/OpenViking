---
type: simulink-block
title: 'Simulation 3D Camera'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine 3-D Simulation'
documentation_page: 'simulation3dcamera'
documentation_source_path: 'ref/simulation3dcamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera

## 端口

### 输入

### **Rel Translation** — 传感器相对于安装点的相对平移 (m) `[0 0 0]` (默认) | 形式为 [*X* *Y* *Z*] 的实值 1×3 向量

传感器相对于其在车辆上安装点的相对平移，以 meters 为单位，指定为形式为 [*X*
*Y*
*Z*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative translation [X, Y, Z] (m)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅传感器位置变换。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — 传感器相对于安装点的相对旋转 (deg) `[0 0 0]` (默认) | 形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量

传感器相对于其在车辆上安装点的相对旋转，以 degrees 为单位，指定为形式为 [*Roll*
*Pitch*
*Yaw*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅传感器位置变换。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出

### **Image** — 3D 输出相机图像 *m*×*n*×3 的 RGB 三元组值数组

3D 输出相机图像，以 *m*×*n*×3 的 RGB 三元组值数组形式返回。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

### **Depth** — 从 0 m 到 1000 m 的对象深度 *m*×*n* 的对象深度数组

图像中每个像素的对象深度，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。深度范围为 0 到 1000 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output depth**。

**数据类型：** `double`

### **Labels** — 标签标识符 *m*×*n* 的标签标识符数组

图像中每个像素的标签标识符，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

该表显示了可从模块选择的默认场景中使用的对象 ID。如果您使用自定义场景，在 Unreal® Editor 中，您可以将新的对象类型分配给未使用的 ID。如果场景包含未分配 ID 的对象，则该对象会分配 ID `0`。不支持车道标线检测。

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
| `20` | 左人字形警告标志 |
| `21` | 右人字形警告标志 |
| `22` | *未使用* |
| `23` | 右侧单行道标志 |
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

**注意**

启用 `Labels` 需要将带有标签 `SemanticSegmentationSensor<N>` 的 `Sim 3D Semantic` actor 放置在相同位置。N 是传感器标识符。当启用 `Labels` 输出时，Simulation 3D Camera 模块会实例化 `Sim 3D Camera` 和 `Sim 3d Semantic`。

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标中。在此坐标系中，*Z* 轴从地面向上指向。单位为 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器围绕场景 *X* 轴、*Y* 轴和 *Z* 轴的 roll、pitch 和 yaw 方向。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为 radians。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` (默认) | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin` (默认) | 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin` (默认) | ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器相对于场景原点或车辆原点放置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器相对于场景原点安装，并且在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，模块将传感器相对于车辆原点安装，并且在仿真期间，传感器随车辆移动。

要指定传感器相对于场景原点或车辆原点的相对位置和方向，请使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数。

车辆原点的位置取决于车辆类型。要选择车辆类型，请指定您要将传感器安装到的 Simulation 3D UAV Vehicle 模块的 **Type** 参数。有关车辆尺寸和车辆原点位置的更多信息，请访问每种车辆类型的参考页

### **Specify offset** — 指定距安装位置的偏移 `On` (默认)

选择此参数以通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定距安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位为 meters。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆向前方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。

原点是 **Mounting location** 参数中指定的安装位置。此原点与车辆原点不同，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 UAV Toolbox 中 Unreal Engine 仿真的坐标系。

**示例：** `[0,0,0.01]`

#### 在仿真期间调整相对平移

要在仿真期间调整传感器的相对平移，请通过选择 **Relative translation [X, Y, Z] (m)** 参数旁边的 **Input** 参数来启用 **Rel Translation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅传感器位置变换。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。Roll、pitch 和 yaw 分别是围绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。单位为 degrees。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆向前方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，roll、pitch 和 yaw 为顺时针正。如果您从 2D 俯视视角观察场景，则 yaw 角（也称为方向角）为逆时针正，因为您是沿 *Z* 轴的负方向观察场景。

原点是 **Mounting location** 参数中指定的安装位置。此原点与车辆原点不同，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 UAV Toolbox 中 Unreal Engine 仿真的坐标系。

**示例：** `[0,0,10]`

#### 在仿真期间调整相对旋转

要在仿真期间调整传感器的相对旋转，请通过选择 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数来启用 **Rel Rotation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅传感器位置变换。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1` (默认) | 正标量

模块的采样时间，以 seconds 为单位，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

这些固有相机参数等效于 `cameraIntrinsics` (Computer Vision Toolbox) 对象的属性。要获取相机的固有参数，请使用 Camera Calibrator 应用。任意组合的固有相机参数会产生无效图像。Simulation 3D Camera 模块支持带畸变的最大 95 degrees 视场角。有关不同相机模型的最大视场角列表，请参阅 Fisheye Calibration Basics (Computer Vision Toolbox)。

有关相机校准过程的详细信息，请参阅 Using the Single Camera Calibrator App (Computer Vision Toolbox) 和 What Is Camera Calibration? (Computer Vision Toolbox)。

### **Focal length (pixels)** — 相机焦距 `[1109, 1109]` (默认) | 1×2 正整数向量

将相机焦距指定为形式为 [*fx*, *fy*] 的 1×2 正整数向量。单位为 pixels。

*fx* = *F* ×
*sx*

*fy* = *F* ×
*sy*

其中：

- *F* 是以世界单位表示的焦距，通常为 millimeters。
- [*sx*, *sy*] 分别是 *x* 和 *y* 方向上每世界单位的像素数。

此参数等效于 `cameraIntrinsics` 对象的 `FocalLength` (Computer Vision Toolbox) 属性。

### **Optical center (pixels)** — 相机光学中心 `[640, 360]` (默认) | 1×2 正整数向量

将相机的光学中心指定为形式为 [*cx*,*cy*] 的 1×2 正整数向量。单位为 pixels。

此参数等效于 `cameraIntrinsics` 对象的 `PrincipalPoint` (Computer Vision Toolbox) 属性。

### **Image size (pixels)** — 相机生成的图像大小 `[720, 1280]` (默认) | 1×2 正整数向量

将相机生成的图像大小指定为形式为 [*mrows*,*ncols*] 的 1×2 正整数向量。单位为 pixels。您可以指定的最大图像大小为 `[1080,1920]`。

此参数等效于 `cameraIntrinsics` 对象的 `ImageSize` (Computer Vision Toolbox) 属性。

### **Radial distortion coefficients** — 径向畸变系数 `[0, 0]` (默认) | 实值 2 元素向量 | 实值 3 元素向量 | 实值 6 元素向量

将径向畸变系数指定为实值 2 元素、3 元素或 6 元素向量。径向畸变是图像点沿从主点延伸的径向线的位移。

- 当图像点远离主点（正径向位移）时，图像放大率减小，并且在图像上出现枕形畸变。
- 当图像点朝向主点移动（负径向位移）时，图像放大率增加，并且在图像上出现桶形畸变。

相机传感器使用二系数、三系数或六系数公式计算点的 (*x*d,*y*d) 径向畸变位置。此表显示了各种公式，其中：

- (*x*,*y*) = 未畸变像素位置
- *k*1,*k*2,*k*3,*k*4,*k*5,*k*6 = 镜头的径向畸变系数
- *r*2 = *x*2 + *y*2

|  |  |  |
| --- | --- | --- |
| **系数** | **公式** | **描述** |
| `[k1, k2]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` (Computer Vision Toolbox) 属性使用的二系数模型。 |
| `[k1, k2, k3]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` (Computer Vision Toolbox) 属性使用的三系数模型。 |
| `[k1, k2, k3, k4, k5, k6]` | xd=x×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6yd=y×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6 | 六系数模型基于 OpenCV 径向畸变模型。  **注意**  Camera Calibrator 应用不支持此模型。要使用此模型校准相机，请参阅 OpenCV 文档中的 Camera Calibration and 3D Reconstruction。 |

### **切向畸变系数** — 切向畸变系数 `[0, 0]` (default) | real-valued 2-element vector

将切向畸变系数指定为 real-valued 2-element vector。当镜头和图像平面不平行时，会发生切向畸变。

零切向畸变和切向畸变的比较。

相机传感器使用以下公式计算点的切向畸变位置，(*x*d, *y*d)：

*x*d = *x* + [2*p*1*xy* + *p*2 × (*r*2 + 2*x*2)]

*y*d = *y* + [*p*1 × (*r*2 + 2*y*2) + 2*p*2*xy*]

其中：

- *x*, *y* = 未畸变像素位置
- *p*1, *p*2 = 镜头的切向畸变系数
- *r*2 = *x*2 + *y*2

未畸变像素位置出现在归一化图像坐标中，原点位于光学中心。坐标以世界单位表示。

此参数等效于 `cameraIntrinsics` 对象的 `TangentialDistortion` (Computer Vision Toolbox) 属性。

### **轴倾斜** — 相机轴的倾斜角 `0` (default) | nonnegative real-valued scalar

将相机轴的倾斜角指定为 nonnegative real-valued scalar。如果 *X* 轴和 *Y* 轴恰好垂直，则倾斜必须为 `0`。单位为无量纲。

此参数等效于 `cameraIntrinsics` 对象的 `Skew` (Computer Vision Toolbox) 属性。

### **可视化视场** — 用于可视化相机视场的选项 `off` (default) | `on`

*自 R2025a 起*

选择此参数可在 3D 环境中可视化相机覆盖范围。此参数支持使用分段球体可视化视场，以标注视场的边界和范围。

### **视场范围 (m)** — 可视化范围 `61` (default) | positive real scalar

*自 R2025a 起*

指定相机覆盖范围的可视化范围。此参数设置分段球体的半径。单位是米。

#### 依赖关系

要启用此参数，请选择 **可视化视场** 参数。

### 真值

### **输出深度** — 输出深度图 `off` (default) | `on`

选择此参数以在 **Depth** 端口输出深度图。

### **输出语义分割** — 输出标签 ID 的语义分割图 `off` (default) | `on`

选择此参数以在 **Labels** 端口输出标签 ID 的语义分割图。

### **输出位置 (m) 和方向 (rad)** — 输出传感器的位置和方向 `off` (default) | `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a: 可视化相机视场

在 **参数** 选项卡中使用这些参数，可在 3D 环境中可视化相机视场并设置相机覆盖范围的可视化范围。

- **可视化视场**
- **视场范围 (m)**

### R2025a: 性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新改进了帧率和模型执行时间。

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Camera 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中带镜头的相机传感器模型

**注意**

使用 Simulation 3D Camera 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Camera 模块提供与 3D 仿真环境中带镜头的相机的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该传感器基于理想针孔相机模型，并添加了镜头以表示完整的相机模型（包括镜头畸变）。此相机模型支持高达 150 度的无畸变视场。有关详细信息，请参阅算法。

如果将 **采样时间** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您的模型中必须包含一个 Simulation 3D Scene Configuration 模块。

该模块输出仿真期间相机捕获的图像。您可以使用这些图像来可视化和验证您的驾驶算法。此外，在 **真值** 选项卡上，您可以选择选项来输出真值数据，以开发深度估计和语义分割算法。您还可以输出相机在场景世界坐标系中的位置和方向。该图显示了启用了所有端口的模块。

启用了所有端口的 Simulation 3D Camera 模块

下表总结了端口以及如何启用它们。

| 端口 | 描述 | 启用端口的参数 | 可视化示例 |
| --- | --- | --- | --- |
| **Image** | 输出相机捕获的 RGB 图像 | n/a | 城市场景的示例图像输出 |
| **Depth** | 输出深度图，其值从 0 m 到 1000 meters | **输出深度** | 城市场景的示例深度输出 |
| **Labels** | 输出与场景中对象对应的标签 ID 的语义分割图 | **输出语义分割** | 城市场景的示例图像语义分割 |
| **Translation** | 输出相机在世界坐标系中的位置 | **输出位置 (m) 和方向 (rad)** | n/a |
| **Rotation** | 输出相机在世界坐标系中的方向 | **输出位置 (m) 和方向 (rad)** | n/a |

**注意**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Camera 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Camera 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera — `1`

有关执行顺序的更多信息，请参阅 Unreal Engine 自动驾驶仿真工作原理 (Automated Driving Toolbox)。
