---
type: simulink-block
title: 'Simulation 3D Terrain Sensor'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3dterrainsensor'
documentation_source_path: 'ref/simulation3dterrainsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Terrain Sensor

## 端口

### 输出

### **Info** — Bus signal bus

包含模块值的总线信号。这些信号是取决于车轮位置的数组。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `WheelWPositions` | 车轮 *`W`* 射线命中位置，相对于射线原点，指定为 3D 可视化引擎世界坐标系中形式为 [*X*, *Y*, *Z*] 的实值 *N*×3 数组。*N* 是每个车轮的射线数。 | m |
| `WheelWStatus` | 车轮 *`W`* 射线命中状态，指定为 *N*×1 数组。*N* 是每个车轮的射线数。  - 命中对象 – `1` - 未命中对象 – `0` | NA |

## 参数

#### 安装

### **Sensor identifier, sensorId** — 唯一传感器标识符 `0`（默认） | 正整数

唯一传感器标识符，指定为正整数。在多传感器系统中，传感器标识符用于区分传感器。向模型添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1。*N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name, VehTag** — 传感器安装到的父级名称 `SimulinkVehicle1`（默认） | 车辆名称

传感器安装到的父级名称，指定为模型中车辆的名称。可以从下拉列表中选择的车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。

**示例：** `SimulinkVehicle2`

#### 参数

### **Ray origins, RayOrigins** — 射线原点 `[0 0 1]`（默认） | 实值 *N*×3 数组

相对于车轮旋转轴的射线原点，指定为形式为 [*X*, *Y*, *Z*] 的实值 *N*×3 数组。*N* 是射线数。单位为米。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴指向车辆前方。
- *Y* 轴指向车辆右侧（从车辆前方观察时）。
- *Z* 轴指向上方。

**示例：** `zeros(10,3)`

### **Ray directions, RayDirections** — 归一化射线方向 `[0 0 -1]`（默认） | 实值 *N*×3 数组

相对于车轮的归一化射线方向，指定为形式为 [*X*, *Y*, *Z*] 的实值 *N*×3 数组。*N* 是射线数。单位为无量纲。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于 3D 可视化引擎坐标系中，其中：

- *X* 轴指向车辆前方。
- *Y* 轴指向车辆右侧（从车辆前方观察时）。
- *Z* 轴指向上方。

**示例：** `ones(10,3)`

### **Ray lengths, RayLengths** — 长度 `20`（默认） | 实值 *N*×1 向量

射线长度，指定为实值 *N*×1 向量，其中 *N* 是射线数。单位为米。

**示例：** `ones(10,1)*10`

### **Number of wheels on parent vehicle** — 车轮数量 `4`（默认） | 正整数

传感器安装到的父级车辆上的车轮数量。车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。

**示例：** `6`

### **Visualize trace line** — 可视化射线轨迹 off（默认） | on

启用轨迹线可视化。

### **Sample time** — 采样时间 `-1`（默认） | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Terrain Sensor 模块仿真模型需要 Simulink 3D Animation。

### R2023b：支持多轴车辆和摩托车

Simulation 3D Terrain Sensor 模块支持与 simulation 3D motorcycle、tractor 和 trailer 模块一起使用。

### R2023b：参数名称更改

**Parent name, VehicleIdentifier** 参数重命名为 **Parent name, VehTag**。

## 描述

在 3D 环境中实现多点地形传感器

**注意**

使用 Simulation 3D Terrain Sensor 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Terrain Sensor 模块在 Unreal Engine® 中实现多点地形传感器。使用该模块在车辆高速通过地形变化（包括减速带）时进行接触建模。该模块实现射线追踪以检测轮胎下方的地形。使用模块参数以：

- 感知场景中任何 simulation 3D vehicle actor 下方的地形，包括由 Simulation 3D Vehicle 和 Simulation 3D Motorcycle 模块创建的 actor。
- 配置射线原点、方向和长度，以调整适用于场景和测试场景的地形传感器模式。

该模块为车辆 actor 上的每个车轮创建地形传感器模式。对于特定模式，下表提供相应的参数设置。

| 模式 | 参数设置 |
| --- | --- |
| 四轮车辆上的地形感知模式  - 每轮五条射线 - 射线起始于车轮旋转轴指定的点 - 射线以 15° 间隔向下延伸 - 射线长度为 6 m | - **Ray origins** – `zeros(5,3)` - **Ray directions** – `[sqrt(3)/2 0 -1/2;1/2 0   -sqrt(3)/2; 0 0 -1; -1/2 0 -sqrt(3)/2; -sqrt(3)/2 0 -1/2]` - **Ray lengths** – `ones(5,1)*6` - **Number of wheels on parent vehicle** –   `4` |
| 四轮车辆上的地形感知模式  - 每轮五条射线 - 射线起始于由 .37 m 车轮半径指定的点 - 射线以 15° 间隔向下延伸 - 射线长度为 4 m | - **Ray origins** – `zeros(5,3)+[0 0   -.37]` - **Ray directions** – `[sqrt(3)/2 0 -1/2;1/2 0   -sqrt(3)/2; 0 0 -1; -1/2 0 -sqrt(3)/2; -sqrt(3)/2 0 -1/2]` - **Ray lengths** – `ones(5,1)*4` - **Number of wheels on parent vehicle** –   `4` |
| 四轮车辆上的地形感知模式    - 每轮九条射线 - 射线起始于由 .37 m 车轮半径指定的点，沿 Z-up 车辆坐标系的 *Y* 轴 - 射线向下延伸，沿 Z-up 车辆坐标系的 *Z* 轴 - 射线长度为 2 m | - **Ray origins** –   `[[0.2:-0.05:-0.2];zeros(1,9);zeros(1,9)]'+[0 0   -.37]` - **Ray directions** – `zeros(9,3)+[0 0   -1]` - **Ray lengths** – `ones(9,1)*2` - **Number of wheels on parent vehicle** –   `4` |

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Terrain Sensor 模块之前执行。这样，Unreal Engine 3D 可视化环境在 Simulation 3D Terrain Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Terrain Sensor — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。
