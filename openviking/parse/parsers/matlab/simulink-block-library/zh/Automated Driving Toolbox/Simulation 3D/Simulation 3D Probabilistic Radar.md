---
type: simulink-block
title: 'Simulation 3D Probabilistic Radar'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dprobabilisticradar'
documentation_source_path: 'ref/simulation3dprobabilisticradar.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Probabilistic Radar

## 端口
```yaml
ports:
- name: Detections
  summary: 目标检测结果，以包含 MATLAB® 结构的 Simulink 总线形式返回
  direction: output
```

### 输出

### **Detections** — 目标检测结果，以包含 MATLAB® 结构的 Simulink 总线形式返回

目标检测结果，以包含 MATLAB 结构的 Simulink 总线形式返回。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。
该结构具有以下形式。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时刻请求更新时为 False | Boolean |
| `Detections` | 目标检测结果 | 长度为 **Maximum reported** 参数所设定值的 object detection 结构体数组。这些检测中只有 `NumDetections` 个是实际检测。 |

每个 object detection 结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数所使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于笛卡尔坐标，`Measurement` 和
  `MeasurementNoise` 以 **Coordinate system** 参数
  指定的坐标系报告。
- 对于球坐标，`Measurement` 和
  `MeasurementNoise` 以基于传感器笛卡尔坐标系的球坐标系
  报告。
  `MeasurementParameters` 以传感器笛卡尔坐标
  报告。

**Measurement 和 MeasurementNoise**

| **用于报告检测结果的坐标系** | Measurement 和 MeasurementNoise 坐标 |
| --- | --- |
| `'Ego Cartesian'` | 此表显示了使用 **Enable range rate measurements** 参数启用或禁用距离变化率测量时的坐标依赖关系。  | 距离变化率测量 | 坐标 | | --- | --- | | 启用 | `[x;y;z;vx;vy;vz]` | | 禁用 | `[x;y;z]` | |
| `'Sensor Cartesian'` |
| `'Sensor spherical'` | 此表显示了分别使用 **Enable range rate measurements** 和 **Enable elevation angle measurements** 参数启用或禁用距离变化率和仰角测量时的坐标依赖关系。  | 距离变化率测量 | 仰角测量 | 坐标 | | --- | --- | --- | | 启用 | 启用 | `[az;el;rng;rr]` | | 启用 | 禁用 | `[az;rng;rr]` | | 禁用 | 启用 | `[az;el;rng]` | | 禁用 | 禁用 | `[az;rng]` | |

**Measurement Parameters**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测结果以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测结果以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于自车原点的 3D 矢量偏移。该矢量分别由 **Mounting location** 参数指定的传感器位置和高度，以及 **Relative translation [X, Y, Z] (m)** 参数的 *Z* 值导出。 |
| `Orientation` | 雷达传感器坐标系相对于自车坐标系的姿态。该姿态由 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数中指定的横滚角、俯仰角和偏航角值导出。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

每个检测的 `ObjectAttributes` 属性是一个
包含以下字段的结构体。

| 字段 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的 actor 的标识符 `ActorID`。对于虚警，该值为负数。 |
| `SNR` | 检测的信噪比。单位为分贝。 |

每个检测的 `ObjectClassID` 属性具有一个对应
目标 ID 的值。该表显示了可从 Simulation 3D Scene
Configuration 模块选择的默认场景中使用的目标 ID。如果您使用的是自定义场景，可以在 Unreal® Editor 中为未使用的 ID 分配新的目标类型。有关更多详细信息，
请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景
包含未分配 ID 的目标，则该目标被分配 ID
`0`。不支持车道标线的检测。

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
| `20` | 左向 chevron 警告标志 |
| `21` | 右向 chevron 警告标志 |
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
## 参数
```yaml
parameters:
- name: Sensor identifier
  summary: 唯一传感器标识符 1（默认）| 正整数
  group: 安装
- name: Parent name
  summary: 父级车辆名称 Scene Origin（默认）| 车辆名称
  group: 安装
- name: Mounting location
  summary: 传感器安装位置 Origin（默认）| Front bumper | Rear bumper | Right mirror | Left mirror | Rearview mirror | Hood center | Roof
    center | ...
  group: 安装
- name: Specify offset
  summary: 指定相对于安装位置的偏移 off（默认）| on
  group: 安装
- name: Relative translation [X, Y, Z] (m)
  summary: 相对于安装位置的平移偏移 [0, 0, 0]（默认）| 实值 1×3 向量
  group: 安装
- name: Relative rotation [Roll, Pitch, Yaw] (deg)
  summary: 相对于安装位置的旋转偏移 [0, 0, 0]（默认）| 实值 1×3 向量
  group: 安装
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: 安装
- name: Azimuthal resolution of radar (deg)
  summary: 雷达方位角分辨率 4（默认）| 正实标量
  group: 参数
- name: Elevation resolution of radar (deg)
  summary: 雷达仰角分辨率 5（默认）| 正实标量
  group: 参数
- name: Range resolution of radar (m)
  summary: 雷达距离分辨率 2.5（默认）| 正实标量
  group: 参数
- name: Range rate resolution of radar (m/s)
  summary: 雷达距离变化率分辨率 0.5（默认）| 正实标量
  group: 参数
- name: Fractional azimuthal bias component
  summary: 方位偏差比例 0.1（默认）| 非负实数标量
  group: 参数
- name: Fractional elevation bias component
  summary: 俯仰偏差比例 0.1（默认）| 非负实数标量
  group: 参数
- name: Fractional range bias component
  summary: 距离偏差比例 0.05（默认）| 非负实数标量
  group: 参数
- name: Fractional range rate bias component
  summary: 距离变化率偏差比例 0.05（默认）| 非负实数标量
  group: 参数
- name: Field of view (deg)
  summary: 视场 [20, 5]（默认）| 正实值 1×2 向量
  group: 参数
- name: Detection ranges (m)
  summary: 检测距离 [1, 150]（默认）| 正实值 1×2 向量
  group: 参数
- name: Range rates (m/s)
  summary: 最小和最大检测距离变化率 [-100, 100]（默认）| 实值 1×2 向量
  group: 参数
- name: Detection probability
  summary: 雷达检测到目标的概率 0.9（默认）| 范围 (0, 1] 内的实数标量
  group: 参数
- name: False alarm rate
  summary: 虚警率 1e-6（默认）| 范围 [10–7, 10–3] 内的正实数标量
  group: 参数
- name: 'Detection probability range (m):'
  summary: 给定检测概率的参考距离 100（默认）| 正实数标量
  group: 参数
- name: Reference radar cross section (dBsm)
  summary: 给定检测概率的参考雷达截面 0（默认）| 实数标量
  group: 参数
- name: Enable elevation angle measurements
  summary: 启用雷达测量俯仰角 on（默认）| off
  group: 参数
- name: Enable range rate measurements
  summary: 启用雷达测量距离变化率 on（默认）| off
  group: 参数
- name: Enable measurement noise
  summary: 启用向雷达传感器测量添加噪声 on（默认）| off
  group: 参数
- name: Enable false detections
  summary: 启用报告虚警雷达检测 on（默认）| off
  group: 参数
- name: Random number generator method
  summary: 设置随机数生成器种子的方法 Repeatable（默认）| Specify seed | Not repeatable
  group: 参数
- name: Initial seed
  summary: 随机数生成器种子 0（默认）| 范围 [0, 232) 内的标量
  group: 参数
- name: Maximum reported
  summary: 最大报告检测数 50（默认）| 正整数
  group: 参数
- name: Coordinate system
  summary: 报告检测的坐标系 Ego Cartesian（默认）| Sensor Cartesian | Sensor spherical
  group: 参数
- name: Specify output bus name
  summary: 指定输出总线的名称 off（默认）| on
  group: 参数
- name: Output bus name
  summary: 输出总线的名称 BusSimulation3DRadarTruthSensor（默认）| 有效总线名称
  group: 参数
```

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符
使您能够区分不同的传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N*
+ 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier**
值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin`（默认）| 车辆名称

传感器所安装到的父级名称，指定为 `Scene
Origin` 或模型中车辆的名称。您可以选择
的车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果您选择 `Scene
Origin`，该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name**
参数将传感器相对于场景或车辆原点放置。

- 当 **Parent name** 为 `Scene
  Origin` 时，该模块将传感器安装到
  场景原点。您只能将 **Mounting location** 设置为
  `Origin`。在仿真期间，传感器
  保持静止。
- 当 **Parent name** 为车辆名称时，该模块
  将传感器安装到表中描述的某个预定义安装位置。
  在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的姿态 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆的几何中心（参见 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox）  传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠  传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠  传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装到右侧后视镜  传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装到左侧后视镜  传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜  传感器安装在后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到引擎盖中心  传感器安装在引擎盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心  传感器安装在车顶中心的车辆 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向
观察时，横滚角、俯仰角和偏航角为顺时针为正。当
从上方观察车辆时，偏航角（姿态角）为
逆时针为正，因为您是沿轴的负方向
观察的。

传感器相对于车辆的
*X*-*Y*-*Z* 安装
位置取决于车辆类型。要指定
车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with
Ground Following 的 **Type** 参数。要获取
某车辆类型的 *X*-*Y*-*Z* 安装
位置，请参阅该车辆的参考页。

要确定传感器在世界坐标系中的位置，请打开传感器模块。然后，
在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation
(rad)** 参数并检查
**Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选择此参数以使用 **Relative
translation [X, Y, Z] (m)** 和 **Relative
rotation [Roll, Pitch, Yaw] (deg)**
参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为
形式为 [*X*, *Y*,
*Z*] 的实值 1×3 向量。单位为
米。

如果您通过将 **Parent name** 设置为某车辆的名称来将传感器安装到
该车辆，则
*X*、*Y* 和 *Z* 位于
车辆坐标系中，其中：

- *X* 轴从车辆指向前方。
- *Y* 轴指向车辆左侧，
  当沿车辆前方方向观察时。
- *Z* 轴指向上方。

原点是 **Mounting
location** 参数中指定的安装位置。该原点不同于车辆原点，
车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到
场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标中。

有关车辆和世界
坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为
形式为 [*Roll*,
*Pitch*, *Yaw*] 的实值 1×3 向量。横滚角、俯仰角和偏航角分别是
绕 *X* 轴、*Y* 轴和
*Z* 轴的旋转角度。单位为
度。

如果您通过将 **Parent name** 设置为某车辆的名称来将传感器安装到
该车辆，则
*X*、*Y* 和 *Z* 位于
车辆坐标系中，其中：

- *X* 轴从车辆指向前方。
- *Y* 轴指向车辆左侧，
  当沿车辆前方方向观察时。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴
  和 *Z* 轴的正方向观察时，横滚角、俯仰角和偏航角为顺时针为正。如果您从 2D
  俯视视角观察场景，则偏航角（也称为姿态角）
  为逆时针为正，因为您是沿 *Z* 轴的
  负方向观察场景的。

原点是 **Mounting
location** 参数中指定的安装位置。该原点不同于车辆原点，
车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到
场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标中。

有关车辆和世界
坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真
环境帧率是采样时间的倒数。

如果您将采样时间设置为 `-1`，则该模块从
Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

#### 精度设置

### **Azimuthal resolution of radar (deg)** — 雷达方位角分辨率 `4`（默认）| 正实标量

雷达的方位角分辨率，指定为正实标量。方位角
分辨率定义了雷达能够区分两个目标的最小方位角
间隔。方位角分辨率通常为雷达方位角
波束宽度的 3dB 下降点。单位为度。

**示例：** `6.5`

#### 依赖关系

方位角分辨率必须小于或等于
`Field of view (deg)` 参数中指定的方位角视场。

### **Elevation resolution of radar (deg)** — 雷达仰角分辨率 `5`（默认）| 正实标量

雷达的仰角分辨率，指定为正实标量。仰角
分辨率定义了雷达能够区分两个目标的最小仰角
间隔。仰角分辨率通常为雷达仰角
波束宽度的 3dB 下降点。单位为度。

**示例：** `3.5`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的
**Radar model** 部分中，选择 **Enable elevation angle
measurements**。

仰角分辨率必须小于或等于
`Field of view (deg)` 参数中指定的仰角视场。

### **Range resolution of radar (m)** — 雷达距离分辨率 `2.5`（默认）| 正实标量

雷达的距离分辨率，指定为正实标量。距离
分辨率定义了雷达能够区分两个目标的最小距离
间隔。单位为米。

**示例：** `5.0`

### **Range rate resolution of radar (m/s)** — 雷达距离变化率分辨率 `0.5`（默认）| 正实标量

雷达的距离变化率分辨率，指定为正实标量。距离
变化率分辨率定义了雷达能够区分两个目标的最小距离变化率
间隔。单位为米每秒。

**示例：** `0.75`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的
**Radar model** 部分中，选择 **Enable range rate
measurements**。

#### 偏置设置

### **Fractional azimuthal bias component** — 方位偏差比例 `0.1`（默认）| 非负实数标量

雷达的方位偏差比例，指定为非负实数标量。方位偏差表示为 **Azimuthal resolution of radar (deg)** 参数中指定的方位分辨率的比例。单位为无量纲。

**示例：** 0.3

### **Fractional elevation bias component** — 俯仰偏差比例 `0.1`（默认）| 非负实数标量

雷达的俯仰偏差比例，指定为非负实数标量。俯仰偏差表示为 **Elevation resolution of radar (deg)** 参数中指定的俯仰分辨率的比例。单位为无量纲。

**示例：** 0.2

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable elevation angle measurements**。

### **Fractional range bias component** — 距离偏差比例 `0.05`（默认）| 非负实数标量

雷达的距离偏差比例，指定为非负实数标量。距离偏差表示为 **Range resolution of radar (m)** 参数中指定的距离分辨率的比例。单位为无量纲。

**示例：** `0.15`

### **Fractional range rate bias component** — 距离变化率偏差比例 `0.05`（默认）| 非负实数标量

雷达的距离变化率偏差比例，指定为非负实数标量。距离变化率偏差表示为 **Range rate resolution of radar (m/s)** 参数中指定的距离变化率分辨率的比例。单位为无量纲。

**示例：** `0.2`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable range rate measurements**。

#### 检测器设置

### **Field of view (deg)** — 视场 `[20, 5]`（默认）| 正实值 1×2 向量

雷达的视场，指定为形式为 `[azfov, elfov]` 的正实值 1×2 向量。`azfov` 是方位角视场。`elfov` 是俯仰角视场。视场定义了传感器所覆盖的角度范围。每个分量必须位于区间 (0,180] 内。雷达视场外的目标不会被检测到。单位为度。

**示例：** `[14 7]`

### **Detection ranges (m)** — 检测距离 `[1, 150]`（默认）| 正实值 1×2 向量

雷达可以检测到目标的检测距离，以米为单位。

- 要仅设置最大检测距离，请将此参数指定为正实数标量。默认情况下，最小检测距离为 0。
- 要同时设置最小和最大检测距离，请将此参数指定为形式为 `[min, max]` 的正实值 1×2 向量。

**示例：** `250`

### **Range rates (m/s)** — 最小和最大检测距离变化率 `[-100, 100]`（默认）| 实值 1×2 向量

最小和最大检测距离变化率，指定为实值 1×2 向量。雷达只能检测此距离变化率区间内的目标。单位为米每秒。

**示例：** `[-200 200]`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable range rate measurements**。

### **Detection probability** — 雷达检测到目标的概率 `0.9`（默认）| 范围 (0, 1] 内的实数标量

雷达检测到目标的概率，指定为范围 (0, 1] 内的实数标量。此量定义了在 **Detection probability range (m)** 参数指定的参考检测距离处，检测具有 **Reference radar cross section (dBsm)** 参数指定的雷达截面的目标的概率。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**示例：** `0.95`

### **False alarm rate** — 虚警率 `1e-6`（默认）| 范围 [10–7, 10–3] 内的正实数标量

雷达分辨率单元内的虚警率，指定为范围 [10–7, 10–3] 内的正实数标量。单位为无量纲。

**示例：** `1e-5`

### **Detection probability range (m):** — 给定检测概率的参考距离 `100`（默认）| 正实数标量

给定检测概率的参考距离，指定为正实数标量。参考距离是雷达以 **Detection probability** 参数指定的检测概率检测具有 **Reference radar cross section (dBsm)** 指定的雷达截面的目标时的距离。单位为米。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**示例：** `150`

### **Reference radar cross section (dBsm)** — 给定检测概率的参考雷达截面 `0`（默认）| 实数标量

给定检测概率的参考雷达截面（RCS），指定为实数标量。参考雷达截面（RCS）定义了在 **Detection probability range (m)** 指定的距离处目标的 RCS 值，使雷达以 **Detection probability** 指定的概率检测这些目标。单位为分贝每平方米。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**注意**

雷达截面值的另一种单位是 m2。您可以使用以下方程将 RCS 值从 m2 转换为 dBsm，并在 **Reference radar cross section (dBsm)** 参数中指定：

|  |  |
| --- | --- |
| RCS in dBsm = 10 log (RCS in m2) | **(1)** |

**示例：** `2.0`

#### 雷达模型

### **Enable elevation angle measurements** — 启用雷达测量俯仰角 `on`（默认）| `off`

选择此参数以对能够测量目标俯仰角的雷达进行建模。此参数启用 **Elevation resolution of radar (deg)** 和 **Fractional elevation bias component** 参数。

### **Enable range rate measurements** — 启用雷达测量距离变化率 `on`（默认）| `off`

选择此参数以对能够测量目标距离变化率的雷达进行建模。此参数启用 **Range rate resolution of radar (m/s)**、**Fractional range bias component** 和 **Range rates (m/s)** 参数。

### **Enable measurement noise** — 启用向雷达传感器测量添加噪声 `on`（默认）| `off`

选择此参数以向雷达传感器测量添加噪声。否则，测量为无噪声。每个检测的 `MeasurementNoise` 属性始终会被计算，且不受 **Enable measurement noise** 参数所指定值的影响。通过不选择此参数，您可以将传感器真值测量传入 Multi-Object Tracker 模块。

### **Enable false detections** — 启用报告虚警雷达检测 `on`（默认）| `off`

选择此参数以启用报告虚警雷达测量。否则，仅报告实际检测。

### **Random number generator method** — 设置随机数生成器种子的方法 `Repeatable`（默认）| `Specify seed` | `Not repeatable`

设置随机数生成器种子的方法，指定为表中的选项之一。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 该模块在首次仿真时生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数以从统计传感器模型生成可重复的结果。要更改此初始种子，请在 MATLAB 命令提示符下输入 `clear all`。 |
| `Specify seed` | 通过 **Specify seed** 参数指定您自己的随机初始种子以获得可重复的结果。 |
| `Not repeatable` | 该模块在每次仿真运行后生成新的随机初始种子。选择此参数以从统计传感器模型生成不可重复的结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认）| 范围 [0, 232) 内的标量

随机数生成器种子，指定为范围 [0, 232) 内的标量

**示例：** `2001`

#### 依赖关系

要启用此参数，请将 **Random number generator method** 参数设置为 `Specify seed`。

#### 检测报告

### **Maximum reported** — 最大报告检测数 `50`（默认）| 正整数

最大报告检测数，指定为正整数。单位为无量纲。

**示例：** `35`

### **Coordinate system** — 报告检测的坐标系 `Ego Cartesian`（默认）| `Sensor Cartesian` | `Sensor spherical`

报告检测的坐标系，指定为以下值之一：

- `Ego Cartesian` — 雷达在自车笛卡尔坐标系中报告检测。
- `Sensor Cartesian`— 雷达在传感器笛卡尔坐标系中报告检测。
- `Sensor spherical` — 雷达在球坐标系中报告检测。此坐标系以雷达为中心，并与雷达在自车上的朝向对齐。

### **Specify output bus name** — 指定输出总线的名称 `off`（默认）| `on`

选择此参数以指定该模块输出到基础工作区的总线名称。在 **Output bus name** 参数中指定此名称。

### **Output bus name** — 输出总线的名称 `BusSimulation3DRadarTruthSensor`（默认）| 有效总线名称

该模块输出到基础工作区的总线名称。

#### 依赖关系

要启用此参数，请选择 **Specify output bus name** 参数。
## 所属库

Automated Driving Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Probabilistic Radar 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中的概率雷达传感器模型

**注意**

使用 Simulation 3D Probabilistic Radar 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Probabilistic Radar 模块提供了与 3D 仿真环境中概率雷达传感器的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。您可以指定雷达模型以及精度、偏差和检测参数。该模块使用采样时间来捕获雷达检测，并输出目标检测报告列表。要跨模型中所有雷达配置 3D 环境中参与者的概率雷达特征，请使用 Simulation 3D Probabilistic Radar Configuration 模块。如果您未使用 Simulation 3D Probabilistic Radar Configuration 模块指定雷达特征，则所有目标的雷达截面值将为 `-20` dBsm。

如果您将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Probabilistic Radar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Probabilistic Radar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Probabilistic Radar — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
