---
type: simulink-block
title: 'Vehicle Terrain Sensor'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Sensors (requires Simulink 3D Animation)'
documentation_page: 'vehicleterrainsensor'
documentation_source_path: 'ref/vehicleterrainsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Terrain Sensor

## 端口

### 输入

### **VehCntr** — 车辆中心到前端的距离 `scalar`

从车辆中心到前端的距离，*VehCntrLngthVal*，单位为 m。

#### 依赖项

| **到车辆中心的距离** | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从车辆中心到前端的距离, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **TireRadii** — 轮胎半径 `array`

轮胎半径，*TireRadiiVal*，单位为 m。

#### 依赖项

| **到轮胎中心的距离** 设置 | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从轮胎中心到地面的距离, TireRadiiVal** |
| `External input` | `TireRadii` | None |
### 输出

### **Info** — 总线信号 bus

包含模块值的总线信号。这些信号是取决于车轮位置的数组。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `HitFlg` | 车辆和车轮命中标志：  - 命中对象 – `1` - 未命中对象 – `0` | [VehicleFrontLeftFrontRightRearLeftRearRight] | NA |
| `HitLoc` | 车辆 *HitLocVh* 和轮胎 *HitLocTr* 的命中位置，分别在世界坐标系 *X*、*Y* 和 *Z* 轴中 | [VehicleXVehicleYVehicleZFrontLeftXFrontLeftYFrontLeftZFrontRightXFrontRightYFrontRightZRearLeftXRearLeftYRearLeftZRearRearXRearRearYRearRearZ] | m |
| `StartLoc` | 车辆 *StartLocVh* 和轮胎 *StartLocTr* 的射线追踪起始位置，分别在世界坐标系 *X*、*Y* 和 *Z* 轴中 | m |

### **VehHitDist** — 车辆前端到对象的距离 `scalar`

从车辆前端到对象的距离，*DistToHitVhAdjust*，单位为 m。

### **TireHitDist** — 轮胎到地形的距离 `vector`

从轮胎到地形的距离，*DistToHitTrAdjust*，单位为 m。

*DistToHitTrAdjust* = [FrontLeftFrontRightRearLefRearRight]

## 参数

#### Actor 设置

### **3D 场景中 actor 的标签, ActorTag** — 名称 `SimulinVehicle1`（默认）| character vector

Actor 名称。

Actor 是支持 3D 平移、旋转和缩放的场景对象。部件是 Actor 组件。组件本身不存在；它们与 Actor 关联。

该模块不支持同一 actor tag 的多个实例。当你使用 3D 模块对（例如 Simulation 3D Actor Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景 actor 时，请指定相同的 **3D 场景中 actor 的标签, ActorTag** 参数。

### **到车辆中心的距离** — 选择 `Constant`（默认）| `External input`

配置如何提供到车辆中心的距离。

#### 依赖项

| **到车辆中心的距离** | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从车辆中心到前端的距离, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **到轮胎中心的距离** — 选择 `Constant`（默认）| `External input`

配置如何提供到轮胎中心的距离。

#### 依赖项

| **到轮胎中心的距离** 设置 | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从轮胎中心到地面的距离, TireRadiiVal** |
| `External input` | `TireRadii` | None |

### **从车辆中心到前端的距离, VehCntrLngthVal** — 车辆中心 `0`（默认）| `scalar`

从车辆中心到前端的距离，*VehCntrLngthVal*，单位为 m。

#### 依赖项

| **到车辆中心的距离** | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从车辆中心到前端的距离, VehCntrLngthVal** |
| `External input` | `VehCntr` | *None* |

### **从轮胎中心到地面的距离, TireRadiiVal** — 轮胎半径 `0`（默认）| `scalar`

轮胎半径，*TireRadiiVal*，单位为 m。

#### 依赖项

| **到轮胎中心的距离** 设置 | 创建端口 | 创建参数 |
| --- | --- | --- |
| `Constant` | None | **从轮胎中心到地面的距离, TireRadiiVal** |
| `External input` | `TireRadii` | None |

#### 追踪长度

### **车辆车身 x 轴追踪长度, VehRayLngth** — 追踪长度 `5`（默认）| `scalar`

车辆车身追踪长度，*VehRayLngth*，单位为 m。

### **左前轮 z 轴追踪长度, LfRayLngth** — 追踪长度 `5`（默认）| `scalar`

左前轮追踪长度，*LfRayLngth* 和 *LengthTr*，单位为 m。

### **右前轮 z 轴追踪长度, RfRayLngth** — 追踪长度 `5`（默认）| `scalar`

右前轮追踪长度，*RfRayLngth* 和 *LengthTr*，单位为 m。

### **左后轮 z 轴追踪长度, LrRayLngth** — 追踪长度 `5`（默认）| `scalar`

左后轮追踪长度，*LrRayLngth* 和 *LengthTr*，单位为 m。

### **右后轮 z 轴追踪长度, RrRayLngth** — 追踪长度 `5`（默认）| `scalar`

右后轮追踪长度，*RrRayLngth* 和 *LengthTr*，单位为 m。

#### 起始点偏移

### **车辆车身 x 轴追踪偏移, VehRayOffset** — 偏移车辆射线追踪 `0`（默认）| `scalar`

车辆车身追踪偏移，*OffsetVh*，单位为 m。

### **左前轮 z 轴追踪偏移, LfRayOffset** — 偏移左前轮射线追踪 `0`（默认）| `scalar`

左前轮追踪偏移，*LfRayOffset* 和 *OffsetTr*，单位为 m。

### **右前轮 z 轴追踪偏移, RfRayOffset** — 偏移右前轮射线追踪 `0`（默认）| `scalar`

右前轮追踪偏移，*RfRayOffset* 和 *OffsetTr*，单位为 m。

### **左后轮 z 轴追踪偏移, LrRayOffset** — 偏移左后轮射线追踪 `0`（默认）| `scalar`

左后轮追踪偏移，*LrRayOffset* 和 *OffsetTr*，单位为 m。

### **右后轮 z 轴追踪偏移, RrRayOffset** — 偏移右后轮射线追踪 `0`（默认）| `scalar`

右后轮追踪偏移，*RrRayOffset* 和 *OffsetTr*，单位为 m。

#### 启用追踪

### **车辆车身** — 启用车辆车身射线追踪 on（默认）| off

启用车辆车身射线追踪。

### **左前轮胎** — 启用左前轮胎射线追踪 on（默认）| off

启用左前轮胎射线追踪。

### **右前轮胎** — 启用右前轮胎射线追踪 on（默认）| off

启用右前轮胎射线追踪。

### **左后轮胎** — 启用左后轮胎射线追踪 on（默认）| off

启用左后轮胎射线追踪。

### **右后轮胎** — 启用右后轮胎射线追踪 on（默认）| off

启用右后轮胎射线追踪。

### **追踪线可视化** — 可视化射线追踪 on（默认）| off

启用追踪线可视化。

### **采样时间** — 采样时间 `-1`（默认）| `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Vehicle Terrain Sensor 模块仿真模型需要 Simulink 3D Animation。

### R2024a：将被移除

Vehicle Terrian Sensor 模块将在未来版本中移除。请改用 Simulation 3D Terrain Sensor 模块实现射线追踪，以检测车辆轮胎下方的地形。

## 描述

车辆和轮胎到对象的距离

**注意**

使用 Vehicle Terrain Sensor 模块仿真模型需要 Simulink® 3D Animation™。

Vehicle Terrain Sensor 模块实现射线追踪，以检测轮胎下方的地形以及车辆前方的对象。具体而言，对于这些 actor 组件，该模块返回命中位置（在世界坐标系中）和到对象的距离。

- 车辆车身
- 左前轮
- 右前轮
- 左后轮
- 右后轮

**提示**

验证 Vehicle Terrain Sensor 模块在 Simulation 3D Fisheye Camera 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Vehicle Terrain Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Vehicle Terrain Sensor — `1`

有关执行顺序的详细信息，请参阅控制并显示执行顺序。

Actor 是支持 3D 平移、旋转和缩放的场景对象。部件是 Actor 组件。组件本身不存在；它们与 Actor 关联。

### 命中距离

为了计算图中所示的命中距离，该模块实现以下方程。

|  |  |
| --- | --- |
| 车辆前端到对象，*DistToHitVhAdjust* | ``` DistToHitVh = GetLength(CntrLocVh,HitLocVh) DistToHitVhAdjust = DistToHitVh - VehCntrLngthVal  EndLocVh = CntrLocVh + VehRayLngth - VehRayOffset VehRayOffset = CntrLocVh - StartLocVh VehRayLngth = StartLocVh - EndLocVh ``` |
| 轮胎到地形，*DistToHitTrAdjust* | ``` DistToHitTr = GetLength(CntrLocTr, HitLocTr) DistToHitTrAdjust = DistToHitTr - TireRadiiVal  EndLocTr = CntrLocTr + LengthTr - OffsetTr OffsetTr = CntrLocTr - StartLocTr LengthTr = StartLocTr - EndLocTr ``` |

显示对象和地形的车辆图像

此图和方程使用以下变量。

|  |  |
| --- | --- |
| *CntrLocVh* | 车辆中心位置 |
| *DistToHitVh* | 从车辆中心位置到对象的距离 |
| *DistToHitVhAdjust* | 从车辆前端到对象的距离 |
| *EndLocVh* | 车辆射线追踪终点 |
| *HitLocVh* | 车辆命中位置 |
| *OffsetVh* | 车辆追踪偏移 |
| *StartLocVh* | 车辆射线追踪起点 |
| *VehRayLngth* | 车辆追踪长度 |
| *VehCntrLngthVal* | 从车辆中心到前端的距离 |
| *CntrLocTr* | 轮胎中心位置 |
| *DistToHitTr* | 从轮胎中心位置到地形的距离 |
| *DistToHitTrAdjust* | 从轮胎到地形的距离 |
| *HitLocTr* | 轮胎命中位置 |
| *EndLocTr* | 轮胎射线追踪终点 |
| *OffsetTr* | 轮胎追踪偏移 |
| *StartLocTr* | 轮胎射线追踪起点 |
| *LengthTr* | 轮胎追踪长度 |
| *TireRadiiVal* | 轮胎半径 |

### 命中事件

为了确定命中事件，该模块使用射线追踪。该模块提供世界坐标系中的命中位置。

起始位置、命中位置和对象的示意图

### 未命中事件

为了确定未命中事件，该模块使用射线追踪。

起始位置和对象的示意图
