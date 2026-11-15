---
type: simulink-block
title: 'Simulation 3D Ray Tracer'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3draytracer'
documentation_source_path: 'ref/simulation3draytracer.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ray Tracer

## 端口

### 输出

### **HitLocations** — 命中位置 实数值 *N(B+1)*×3 数组

命中位置，返回为 [*X*, *Y*, *Z*] 形式的实数值 *N(B+1)*×3 数组，单位为 meters。*N* 是射线数，*B* 是每条射线的反弹次数。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴从车辆向前指向
- *Y* 轴指向车辆右侧，当沿车辆前进方向观察时
- *Z* 轴指向上方

**数据类型：** `double`

### **HitNormals** — 到命中位置的射线法线 实数值 *N(B+1)*×3 数组

到命中位置的射线法线，返回为 [*X*, *Y*, *Z*] 形式的实数值 *N(B+1)*×3 数组，单位为 meters。*N* 是射线数，*B* 是每条射线的反弹次数。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴从车辆向前指向
- *Y* 轴指向车辆右侧，当沿车辆前进方向观察时
- *Z* 轴指向上方

**数据类型：** `double`

### **HitDistances** — 到命中位置的射线距离 实数值 *N(B+1)*×1 数组

到命中位置的射线距离，返回为实数值 *N(B+1)*×1 向量 *N*，单位为 meters。*N* 是射线数，*B* 是每条射线的反弹次数。

**数据类型：** `double`

### **SurfaceIds** — 命中表面的对象 ID 整数值 *N(B+1)*×1 向量 | `0`

射线命中表面的对象标识符，返回为整数值 *N(B+1)*×1 向量 *N*。*N* 是射线数，*B* 是每条射线的反弹次数。

返回的表面标识符是在 Unreal® Editor 中创建自定义表面时指定的对象值。如果表面标识符未知，则模块会为其分配 ID `0`。有关添加表面的信息，请参见 Unreal Engine 文档中的 Add a Surface Type。

**数据类型：** `uint8`

### **IsValidHit** — 命中标志 *N*×1 向量

命中标志，返回为 *N*×1 布尔向量。*N* 是射线数。值为 1 表示射线命中了表面。

**数据类型：** `Boolean`

## 参数

#### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` (默认) | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级名称 `Scene Origin` (默认)

传感器安装到的父级名称，指定为模型中车辆的名称，或 `Scene Origin`。您可以选择车辆名称，这些名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。

### **Mounting location** — 传感器安装位置 `Origin` (默认) | ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器放置在相对于场景原点或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器安装到场景原点。您只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 朝前传感器，安装在车辆原点；车辆原点位于地面上且位于车辆的几何中心（请参见 Vehicle Dynamics Blockset 中的 Coordinate Systems）  车辆，传感器安装在原点 | [0, 0, 0] |
| `Front bumper`  `Front center` | 朝前传感器，安装在前保险杠  车辆，传感器安装在前保险杠 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 朝后传感器，安装在后保险杠  车辆，传感器安装在后保险杠 | [0, 0, 180] |
| `Right mirror` | 朝下传感器，安装在右侧后视镜  车辆，传感器安装在右侧后视镜 | [0, –90, 0] |
| `Left mirror` | 朝下传感器，安装在左侧后视镜  车辆，传感器安装在左侧后视镜 | [0, –90, 0] |
| `Rearview mirror` | 朝前传感器，安装在车内后视镜  车辆，传感器安装在车内后视镜 | [0, 0, 0] |
| `Hood center` | 朝前传感器，安装在发动机罩中心  车辆，传感器安装在发动机罩中心 | [0, 0, 0] |
| `Roof center` | 朝前传感器，安装在车顶中心  车辆，传感器安装在车顶中心 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 为顺时针为正。当从上方观察车辆时，yaw 角（方向角）为逆时针为正，因为您是沿该轴的负方向观察。

要确定传感器的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation (rad)** 参数，并检查 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off` (默认) | `on`

选择此参数可通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]` (默认) | 实数值 1×3 向量

相对于传感器安装位置的平移偏移，指定为 [*X*, *Y*, *Z*] 形式的实数值 1×3 向量，单位为 meters。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向
- *Y* 轴指向车辆左侧，当沿车辆前进方向观察时
- *Z* 轴指向上方

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参见 Vehicle Dynamics Blockset 中的 Coordinate Systems。

**示例：** `[0,0,0.01]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]` (默认) | 实数值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为 [*Roll*, *Pitch*, *Yaw*] 形式的实数值 1×3 向量，单位为 degrees。Roll、pitch 和 yaw 分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，当沿车辆前进方向观察时。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 为顺时针为正。如果从 2D 俯视视角查看场景，则 yaw 角（也称为方向角）为逆时针为正，因为您是沿 *Z* 轴的负方向查看场景。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参见 Vehicle Dynamics Blockset 中的 Coordinate Systems。

**示例：** `[0,0,10]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

#### 参数

### **Ray origins** — 射线原点 `zeros(10,3)` (默认) | 实数值 *N*×3 数组

相对于传感器安装位置的射线原点，指定为 [*X*, *Y*, *Z*] 形式的实数值 *N*×3 数组，单位为 meters。*N* 是射线数。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴从车辆向前指向
- *Y* 轴指向车辆右侧，当沿车辆前进方向观察时
- *Z* 轴指向上方

**示例：** `zeros(10,3)`

### **Ray directions** — 归一化射线方向 `ones(10,3)` (默认) | 实数值 *N*×3 数组

相对于传感器安装位置的归一化射线方向，指定为 [*X*, *Y*, *Z*] 形式的实数值 *N*×3 数组。*N* 是射线数。单位为无量纲。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴从车辆向前指向
- *Y* 轴指向车辆右侧，当沿车辆前进方向观察时
- *Z* 轴指向上方

**示例：** `ones(10,3)`

### **Max ray lengths** — 最大总射线长度 `ones(10,1)*10` (默认) | 实数值 *N*×1 向量

多反弹追踪路径的最大总射线长度，指定为实数值 *N*×1 向量，单位为 meters。*N* 是射线数。

**示例：** `ones(10,1)*10`

### **Number of bounces** — 每条射线的反弹次数 `2` (默认) | 正整数

追踪在终止之前可具有的反弹次数 *B*，指定为整数。

**示例：** `0`

### **Visualize trace line** — 可视化射线追踪 on (默认) | off

是否启用射线追踪器的 Unreal Engine 追踪线可视化。

### **Enable optimization** — 启用优化 on (默认) | off

是否启用射线追踪器的优化。启用此参数允许模块执行并发追踪。当追踪数量很大且您的机器具有多个核心时，请启用此参数。

### **Sample time** — 采样时间 `-1` (默认) | 正标量

模块的采样时间，单位为 seconds，指定为正标量。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Ray Tracer 模块对模型进行仿真需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现射线追踪

**注意**

使用 Simulation 3D Ray Tracer 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Ray Tracer 模块实现射线追踪，以获取场景中物体的位置、表面法线、表面标识符和距离。您可以指定模块参数来配置射线原点、方向和长度，以针对您的场景和测试场景调整射线追踪传感器模式。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Ray Tracer 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Simulation 3D Ray Tracer 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Terrain Sensor — `1`

有关执行顺序的更多信息，请参见 Control and Display Execution Order。
