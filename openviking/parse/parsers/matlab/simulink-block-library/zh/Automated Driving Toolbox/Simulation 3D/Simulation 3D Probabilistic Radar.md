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

### 输出

### **Detections** — 包含 MATLAB® 结构的目标检测 Simulink 总线

目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。
该结构具有以下形式。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数目 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 长度为 **Maximum reported** 参数所设置值的 object detection structures 数组。其中只有 `NumDetections` 个检测是实际检测。 |

每个 object detection structure 包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性 Kalman 跟踪滤波器初始化函数使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于笛卡尔坐标，`Measurement` 和
  `MeasurementNoise` 以 **Coordinate system** 参数指定的坐标系报告。
- 对于球坐标，`Measurement` 和
  `MeasurementNoise` 以基于传感器笛卡尔坐标系的球坐标系报告。
  `MeasurementParameters` 以传感器笛卡尔坐标报告。

**Measurement and MeasurementNoise**

| **用于报告检测的坐标系** | Measurement and MeasurementNoise 坐标 |
| --- | --- |
| `'Ego Cartesian'` | 此表显示了当您使用 **Enable range rate measurements** 参数启用或禁用距离变化率测量时的坐标依赖关系。  | 距离变化率测量 | 坐标 | | --- | --- | | 已启用 | `[x;y;z;vx;vy;vz]` | | 已禁用 | `[x;y;z]` | |
| `'Sensor Cartesian'` |
| `'Sensor spherical'` | 此表显示了当您分别使用 **Enable range rate measurements** 和 **Enable elevation angle measurements** 参数启用或禁用距离变化率和俯仰角测量时的坐标依赖关系。  | 距离变化率测量 | 俯仰角测量 | 坐标 | | --- | --- | --- | | 已启用 | 已启用 | `[az;el;rng;rr]` | | 已启用 | 已禁用 | `[az;rng;rr]` | | 已禁用 | 已启用 | `[az;el;rng]` | | 已禁用 | 已禁用 | `[az;rng]` |

**Measurement Parameters**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量值的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于自车原点的 3D 向量偏移。该向量分别派生自 **Mounting location** 参数指定的传感器位置和高度，以及 **Relative translation [X, Y, Z] (m)** 参数的 *Z* 值。 |
| `Orientation` | 雷达传感器坐标系相对于自车坐标系的方向。该方向派生自 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数中指定的 roll、pitch 和 yaw 值。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含俯仰角分量。 |

每个检测的 `ObjectAttributes` 属性是具有以下字段的结构体。

| 字段 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的参与者标识符 `ActorID`。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

每个检测的 `ObjectClassID` 属性具有对应于对象 ID 的值。该表显示了可从 Simulation 3D Scene Configuration 模块选择的默认场景中使用的对象 ID。如果您使用自定义场景，可以在 Unreal® Editor 中将新对象类型分配给未使用的 ID。有关更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景包含未分配 ID 的对象，则该对象被分配 ID `0`。不支持车道标线的检测。

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
| `20` | 左 V 形警告标志 |
| `21` | 右 V 形警告标志 |
| `22` | *未使用* |
| `23` | 右单行道标志 |
| `24` | *未使用* |
| `25` | 仅校车标志 |
| `26-38` | *未使用* |
| `39` | 人行横道标志 |
| `40` | *未使用* |
| `41` | 交通信号 |
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

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` (default) | positive integer

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例:** `2`

### **Parent name** — 父车辆名称 `Scene Origin` (default) | vehicle name

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。可选择的车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，模块将传感器放置在场景原点。

**示例:** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin` (default) | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器相对于场景原点或车辆原点放置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，模块将传感器安装到表中描述的一个预定义安装位置。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装在车辆原点；该原点位于地面上且位于车辆的几何中心（请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation） 安装有原点传感器的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装在前保险杠 安装有前保险杠传感器的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装在后保险杠 安装有后保险杠传感器的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装在右侧后视镜 安装有右侧后视镜传感器的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装在左侧后视镜 安装有左侧后视镜传感器的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装在车内后视镜 安装有车内后视镜传感器的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装在引擎盖中心 安装有引擎盖中心传感器的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装在车顶中心 安装有车顶中心传感器的车辆 | [0, 0, 0] |

当沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、Pitch 和 Yaw 分别为顺时针正方向。当从上方观察车辆时，Yaw 角（方向角）为逆时针正方向，因为您是沿该轴的负方向观察的。

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用传感器所安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标系中的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation (rad)** 参数，并检查 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移量 `off` (default) | `on`

选择此参数可使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移量。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移量 `[0, 0, 0]` (default) | real-valued 1-by-3 vector

传感器相对于安装位置的平移偏移量，指定为 [*X*, *Y*, *Z*] 形式的实数值 1×3 向量。单位为 m。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。

原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**示例:** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移量 `[0, 0, 0]` (default) | real-valued 1-by-3 vector

传感器相对于安装位置的旋转偏移量，指定为 [*Roll*, *Pitch*, *Yaw*] 形式的实数值 1×3 向量。Roll、Pitch 和 Yaw 分别是围绕 *X*、*Y* 和 *Z* 轴的旋转角度。单位为 deg。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。
- 当沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、Pitch 和 Yaw 分别为顺时针正方向。如果从 2D 自上而下的视角查看场景，则 Yaw 角（也称为方向角）为逆时针正方向，因为您是沿 *Z* 轴的负方向查看场景的。

原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**示例:** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1` (default) | positive scalar

模块的采样时间，单位为秒，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

#### 精度设置

### **Azimuthal resolution of radar (deg)** — 雷达的方位角分辨率 `4` (default) | positive real scalar

雷达的方位角分辨率，指定为正实标量。方位角分辨率定义雷达能够区分两个目标的最小方位角间隔。方位角分辨率通常是雷达方位角波束宽度的 3dB 下降点。单位为 deg。

**示例:** `6.5`

#### 依赖关系

方位角分辨率必须小于或等于 `Field of view (deg)` 参数中指定的方位角视场。

### **Elevation resolution of radar (deg)** — 雷达的俯仰角分辨率 `5` (default) | positive real scalar

雷达的俯仰角分辨率，指定为正实标量。俯仰角分辨率定义雷达能够区分两个目标的最小俯仰角间隔。俯仰角分辨率通常是雷达俯仰角波束宽度的 3dB 下降点。单位为 deg。

**示例:** `3.5`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable elevation angle measurements**。

俯仰角分辨率必须小于或等于 `Field of view (deg)` 参数中指定的俯仰角视场。

### **Range resolution of radar (m)** — 雷达的距离分辨率 `2.5` (default) | positive real scalar

雷达的距离分辨率，指定为正实标量。距离分辨率定义雷达能够区分两个目标的最小距离间隔。单位为 m。

**示例:** `5.0`

### **Range rate resolution of radar (m/s)** — 雷达的距离变化率分辨率 `0.5` (default) | positive real scalar

雷达的距离变化率分辨率，指定为正实标量。距离变化率分辨率定义雷达能够区分两个目标的最小距离变化率间隔。单位为 m/s。

**示例:** `0.75`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable range rate measurements**。

#### 偏差设置

### **Fractional azimuthal bias component** — 方位角偏差分数 `0.1` (default) | nonnegative real scalar

雷达的方位角偏差分数，指定为非负实标量。方位角偏差表示为 **Azimuthal resolution of radar (deg)** 参数中指定的方位角分辨率的一部分。单位为无量纲。

**示例:** 0.3

### **Fractional elevation bias component** — 俯仰角偏差分数 `0.1` (default) | nonnegative real scalar

雷达的俯仰角偏差分数，指定为非负实标量。俯仰角偏差表示为 **Elevation resolution of radar (deg)** 参数中指定的俯仰角分辨率的一部分。单位为无量纲。

**示例:** 0.2

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable elevation angle measurements**。

### **Fractional range bias component** — 距离偏差分数 `0.05` (default) | nonnegative real scalar

雷达的距离偏差分数，指定为非负实标量。距离偏差表示为 **Range resolution of radar (m)** 参数中指定的距离分辨率的一部分。单位为无量纲。

**示例:** `0.15`

### **Fractional range rate bias component** — 距离变化率偏差分数 `0.05` (default) | nonnegative real scalar

雷达的距离变化率偏差分数，指定为非负实标量。距离变化率偏差表示为 **Range rate resolution of radar (m/s)** 参数中指定的距离变化率分辨率的一部分。单位为无量纲。

**示例:** `0.2`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable range rate measurements**。

#### 检测器设置

### **Field of view (deg)** — 视场 `[20, 5]` (default) | positive real-valued 1-by-2 vector

雷达的视场，指定为 `[azfov, elfov]` 形式的正实数值 1×2 向量。`azfov` 是方位角视场。`elfov` 是俯仰角视场。视场定义传感器跨越的角度范围。每个分量必须位于区间 (0,180] 内。雷达视场之外的目标不会被检测到。单位为 deg。

**示例:** `[14 7]`

### **Detection ranges (m)** — 检测距离 `[1, 150]` (default) | positive real-valued 1-by-2 vector

雷达能够检测目标的检测距离，单位为米。

- 要仅设置最大检测距离，请将此参数指定为正实标量。默认情况下，最小检测距离为 0。
- 要同时设置最小和最大检测距离，请将此参数指定为 `[min, max]` 形式的正实数值 1×2 向量。

**示例:** `250`

### **Range rates (m/s)** — 最小和最大检测距离变化率 `[-100, 100]` (default) | real-valued 1-by-2 vector

最小和最大检测距离变化率，指定为实数值 1×2 向量。雷达只能在此距离变化率区间内检测目标。单位为 m/s。

**示例:** `[-200 200]`

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡的 **Radar model** 部分中，选择 **Enable range rate measurements**。

### **Detection probability** — 雷达检测到目标的概率 `0.9` (default) | real scalar in the range (0, 1]

雷达检测到目标的概率，指定为范围 (0, 1] 内的实标量。此量定义在 **Detection probability range (m)** 参数指定的参考检测距离处，检测具有 **Reference radar cross section (dBsm)** 参数指定的雷达横截面的目标的概率。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**示例:** `0.95`

### **False alarm rate** — 虚警率 `1e-6` (default) | positive real scalar in range [10–7, 10–3]

雷达分辨率单元内的虚警率，指定为范围 [10–7, 10–3] 内的正实标量。单位为无量纲。

**示例:** `1e-5`

### **Detection probability range (m):** — 给定检测概率的参考距离 `100` (default) | positive real scalar

给定检测概率的参考距离，指定为正实标量。参考距离是雷达以 **Detection probability** 参数指定的检测概率检测具有 **Reference radar cross section (dBsm)** 指定的雷达横截面的目标时的距离。单位为米。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**示例:** `150`

### **Reference radar cross section (dBsm)** — 给定检测概率的参考雷达横截面 `0` (default) | real scalar

给定检测概率的参考雷达横截面 (RCS)，指定为实标量。参考雷达横截面 (RCS) 定义在 **Detection probability range (m)** 指定的距离处，雷达以 **Detection probability** 指定的概率检测目标时目标的 RCS 值。单位为 dBsm。

有关概率检测参数之间关系的更多信息，请参阅 Probabilistic Radar Detection Parameters。

**注意**

雷达横截面值的替代单位是 m2。您可以使用以下方程将 RCS 值从 m2 转换为 dBsm，并在 **Reference radar cross section (dBsm)** 参数中指定它：

|  |  |
| --- | --- |
| RCS in dBsm = 10 log (RCS in m2) | **(1)** |

**示例:** `2.0`

#### 雷达模型

### **Enable elevation angle measurements** — 使雷达能够测量俯仰角 `on` (default) | `off`

选择此参数以对能够测量目标俯仰角的雷达建模。此参数启用 **Elevation resolution of radar (deg)** 和 **Fractional elevation bias component** 参数。

### **Enable range rate measurements** — 使雷达能够测量距离变化率 `on` (default) | `off`

选择此参数以对能够测量目标距离变化率的雷达建模。此参数启用 **Range rate resolution of radar (m/s)**、**Fractional range bias component** 和 **Range rates (m/s)** 参数。

### **Enable measurement noise** — 启用向雷达传感器测量值添加噪声 `on` (default) | `off`

选择此参数以向雷达传感器测量值添加噪声。否则，测量值无噪声。每个检测的 `MeasurementNoise` 属性始终会计算，并且不受您为 **Enable measurement noise** 参数指定的值影响。通过不选择此参数，您可以将传感器真值测量值传入 Multi-Object Tracker 模块。

### **Enable false detections** — 启用报告虚警雷达检测 `on` (default) | `off`

选择此参数以启用报告虚警雷达测量值。否则，仅报告实际检测。

### **Random number generator method** — 设置随机数生成器种子的方法 `Repeatable` (default) | `Specify seed` | `Not repeatable`

用于设置随机数生成器种子的方法，指定为表中的选项之一。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 模块为第一次仿真生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数以从统计传感器模型生成可重复结果。要更改此初始种子，请在 MATLAB 命令提示符下输入 `clear all`。 |
| `Specify seed` | 使用 **Specify seed** 参数指定您自己的随机初始种子以获得可重现结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数以从统计传感器模型生成不可重复结果。 |

### **Initial seed** — 随机数生成器种子 `0` (default) | scalar in range [0, 232)

随机数生成器种子，指定为范围 [0, 232) 内的标量

**示例:** `2001`

#### 依赖关系

要启用此参数，请将 **Random number generator method** 参数设置为 `Specify seed`。

#### 检测报告

### **Maximum reported** — 报告的最大检测数目 `50` (default) | positive integer

报告的最大检测数目，指定为正整数。单位为无量纲。

**示例:** `35`

### **Coordinate system** — 报告的检测所使用的坐标系 `Ego Cartesian` (default) | `Sensor Cartesian` | `Sensor spherical`

报告的检测所使用的坐标系，指定为以下值之一：

- `Ego Cartesian` — 雷达在自车笛卡尔坐标系中报告检测。
- `Sensor Cartesian`— 雷达在传感器笛卡尔坐标系中报告检测。
- `Sensor spherical` — 雷达在球坐标系中报告检测。此坐标系以雷达为中心，并与雷达在自车上的方向对齐。

### **Specify output bus name** — 指定输出总线名称 `off` (default) | `on`

选择此参数以指定模块输出到基础工作区的总线名称。在 **Output bus name** 参数中指定此名称。

### **Output bus name** — 输出总线名称 `BusSimulation3DRadarTruthSensor` (default) | valid bus name

模块输出到基础工作区的总线名称。

#### 依赖关系

要启用此参数，请选择 **Specify output bus name** 参数。

## 所属库

Automated Driving Toolbox / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Probabilistic Radar 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中的概率雷达传感器模型

**注意**

使用 Simulation 3D Probabilistic Radar 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Probabilistic Radar 模块提供与 3D 仿真环境中的概率雷达传感器的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。您可以指定雷达模型以及精度、偏差和检测参数。模块使用采样时间来捕获雷达检测，并输出目标检测报告列表。要跨模型中的所有雷达配置 3D 环境中参与者的概率雷达特征，请使用 Simulation 3D Probabilistic Radar Configuration 模块。如果未使用 Simulation 3D Probabilistic Radar Configuration 模块指定雷达特征，则所有目标的雷达横截面值将为 `-20` dBsm。

如果将 **Sample time** 设置为 `-1`，则模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，模型中必须包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Probabilistic Radar 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Probabilistic Radar 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Probabilistic Radar — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
