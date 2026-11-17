---
type: simulink-block
title: 'Motion Platform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'motionplatform'
documentation_source_path: 'ref/motionplatform.html'
language: zh-CN
chinese_source: worker-translation
---

# Motion Platform

## 端口

### 输入

### **Ref** — 参考时间输入标量

参考时间输入，指定为标量。单位为秒。

#### 依赖关系

要启用此端口，请将 **Source of elapsed simulation time** 参数设置为 `Derive from reference input port`。

**数据类型：** `double`

### **Vel** — 平台速度输入实数值 3×*N* 矩阵

平台速度，指定为实数值 3×*N* 矩阵，其中 *N* 为要建模的平台数量。单位为米每秒。

#### 依赖关系

要启用此端口，请将 **Model of object motion** 参数设置为 `Velocity`，并将 **Source of velocity** 参数设置为 `Input port`。

**数据类型：** `double`

### **Acl** — 平台加速度输入实数值 3×*N* 矩阵

平台加速度输入，指定为实数值 3×*N* 矩阵，其中 *N* 为要建模的平台数量。单位为米每二次方秒。

#### 依赖关系

要启用此端口，请将 **Model of object motion** 参数设置为 `Acceleration`，并将 **Source of acceleration** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Pos** — 平台位置输出实数值 3×*N* 矩阵

平台的当前位置，以 `[x;y;z]` 形式的实数值 3×1 列向量或实数值 3×*N* 矩阵返回，其中 *N* 为要建模的平台数量。每列的形式为 `[x;y;z]`。单位为米。

**数据类型：** `double`

### **Vel** — 平台速度输出实数值 3×*N* 矩阵

平台的当前速度，指定为 `[vx;vy;vz]` 形式的实数值 3×1 列向量或实数值 3×*N* 矩阵，其中 *N* 为要建模的平台数量。每列的形式为 `[vx;vy;vz]`。速度单位为米每秒。

**数据类型：** `double`

### **LAxes** — 平台方向输出实数值 3×3×*N* 矩阵

当前平台方向轴，以实数值 3×3×*N* 矩阵返回，其中 *N* 为要建模的平台数量。每个 3×3 子矩阵为正交矩阵。当您将 `OrientationAxesOutputPort` 属性设置为 `true` 时，此输出启用。当前平台轴围绕平台路径的法向量旋转。

#### 依赖关系

要启用此端口，请选中 **Enable orientation axes output** 复选框。

**数据类型：** `double`

## 参数

### **Model of object motion** — 物体运动模型 `Velocity`（默认）| `Acceleration` | `Custom`

将物体运动模型指定为 `Velocity`、`Acceleration` 或 `Custom`。当您将此参数设置为 `Velocity` 时，平台在每个仿真步长中遵循恒定速度轨迹。当您将此参数设置为 `Acceleration` 时，平台在每个仿真步长中遵循恒定加速度轨迹。当您将此参数设置为 `Custom` 时，平台运动遵循由 **Custom trajectory waypoints** 参数指定的航点序列。物体对航点执行分段三次插值，以推导每个时间步长的位置和速度。

### **Initial position (m)** — 平台初始位置 `[0;0;0]`（默认）

以米为单位指定平台的初始位置，为 3×*N* 矩阵，其中每列以 `[x;y;z]` 形式表示一个平台的初始位置。*N* 为平台数量。

### **Initial velocity (m/s)** — 平台初始速度 `[0;0;0]`（默认）

以 m/s 为单位指定平台的初始速度，为 3×*N* 矩阵，其中每列以 `[vx;vy;vz]` 形式表示一个平台的初始速度。*N* 为平台数量。

#### 依赖关系

仅当您将 **Source of velocity** 或 **Source of acceleration** 参数设置为 `Input port` 时，此参数才会出现。

### **Source of velocity** — 速度数据源 `Property`（默认）| `Input port`

此参数仅在将 **Model of object motion** 参数设置为 `Velocity` 时出现。
然后，您必须为模型提供速度数据。将 **Source of velocity** 数据指定为来自 `Property` 或 `Input port`。

| **Source of velocity** | 使用这些模型参数或端口 |
| --- | --- |
| **Property** | **Initial position (m)** 参数  **Velocity (m/s)** 参数 |
| `Input port` | **Initial position (m)** 参数  **Initial velocity (m/s)** 参数  `Vel` 输入端口 |

#### 依赖关系

此参数仅在将 **Model of object motion** 参数设置为 `Velocity` 时出现。

### **Velocity (m/s)** — 平台的当前速度 `[0;0;0]`（默认）

以 m/s 为单位指定平台的当前速度，形式为 3×*N* 矩阵，其中每一列以 `[vx;vy;vz]` 的形式表示一个平台的当前速度。

#### 依赖关系

此参数仅在将 **Model of object motion** 参数设置为 `Velocity` 并将 **Source of velocity** 参数设置为 `Property` 时出现。

### **Source of acceleration** — 加速度数据源 `Property`（默认）| `Input port`

此参数仅在将 **Model of object motion** 参数设置为 `Acceleration` 时出现。
然后，您必须为模型提供加速度值。将 **Source of acceleration** 数据指定为来自 `Property` 或 `Input port`。

| Source of acceleration | 使用这些模型参数或端口 |
| --- | --- |
| `Property` | **Initial Position (m)** 参数  **Initial Velocity (m/s)** 参数  **Acceleration (m/s^2)** 参数 |
| `Input port` | **Initial Position (m)** 参数  **Initial Velocity (m/s)** 参数  `Acl` 输入端口 |

#### 依赖关系

此参数仅在将 **Model of object motion** 参数设置为 `Acceleration` 时出现。

### **Acceleration (m/s^2)** — 平台的加速度 `[0;0;0]`（默认）

以 m/s^2 为单位指定平台的当前加速度，形式为 3×*N* 矩阵，其中每一列以 `[ax;ay;az]` 的形式表示一个平台的当前加速度。

#### 依赖关系

此参数在将 **Model of object motion** 参数设置为 `Acceleration` 并将 **Source of acceleration** 参数设置为 `Property` 时出现。

### **Custom trajectory waypoints** — 自定义轨迹航点 `[ 0, 0, 0, 0, 0, 0, 0; 1, 0, 0, 0, 0, 0, 0 ]`（默认）

自定义轨迹航点，指定为实数值 *M*×*L* 矩阵或 *M*×*L*×*N* 数组。*M* 是航点数量。*L* 为 4 或 7。

- 当 *L* 为 4 时，第一列表示测量平台位置的时间。第 2 至 4 列是 x、y 和 z 坐标中的位置测量值。速度由位置测量值推导得出。
- 当 *L* 为 7 时，矩阵中的第 5 至 7 列是 x、y 和 z 坐标中的速度测量值。

当您将 **Custom trajectory waypoints** 参数设置为三维数组时，页数 *N* 表示平台数量。时间单位为秒，位置单位为米，速度单位为米每秒。

#### 依赖关系

要启用此属性，请将 **Model of object motion** 属性设置为 `Custom`。

### **Mechanical scanning mode** — 机械扫描模式 `None`（默认）| `Circular` | `Sector`

平台的机械扫描模式，指定为 `None`、`Circular` 或 `Sector`，其中 `None` 为默认值。当您将 **Mechanical scanning mode** 参数设置为 `Circular` 时，平台沿平台朝向轴的方位方向顺时针连续扫描 360 度。当您将 **Mechanical scanning mode** 参数设置为 `Sector` 时，平台在平台朝向轴的方位方向上，在 **Azimuth scan angle span (deg)** 参数指定的范围内顺时针扫描。当扫描达到范围边界时，扫描反向并扫描回另一个扫描边界。扫描在平台的朝向轴内进行。

### **Initial scan angle (deg)** — 平台的初始扫描角 `0`（默认）

平台的初始扫描角，指定为 1×*N* 向量，其中 *N* 是平台数量。扫描在平台的局部坐标系中进行。**Initial orientation axes** 参数指定原始局部坐标系。在仿真开始时，由 **Initial orientation axes** 指定的朝向轴会按照 `InitialScanAngle`**Initial scan angle (deg)** 参数指定的角度进行旋转。默认值为零。单位为度。

#### 依赖关系

当您将 **Mechanical scanning mode** 参数设置为 `Circular` 或 `Sector` 时，此参数适用。

### **Azimuth scan angle span (deg)** — 方位角跨度 `[-60,60]`（默认）

将方位角跨度指定为 *N*×2 矩阵，其中 *N* 是平台数量。矩阵的每一行以 `[ScanAngleLowerBound ScanAngleHigherBound]` 的形式指定对应平台的扫描范围。默认值为 `[-60 60]`。单位为度。

#### 依赖关系

要启用此参数，请将 **Mechanical scanning mode** 参数设置为 `Sector`。

### **Azimuth scan rate (deg/s)** — 方位扫描速率 `10`（默认）

将方位扫描速率指定为 1×*N* 向量，其中 *N* 是平台数量。向量中的每个条目是对应平台的方位扫描速率。默认值为 10 度/秒。单位为度/秒。

#### 依赖关系

要启用此参数，请将 **Mechanical scanning mode** 参数设置为 `Circular` 或 `Sector`。

### **Initial orientation axes** — 平台的初始朝向轴 `eye(3)`（默认）

将定义平台处初始局部 *(x,y,z)* 坐标系的三个轴指定为 3×3×*N* 矩阵。矩阵的每一列表示局部坐标系的一个轴。三个轴必须正交归一。

### **Enable orientation axes output** — 输出朝向轴 off（默认）| on

选中此复选框可通过输出端口 `LAxes` 获取平台的瞬时朝向轴。仅当选中该复选框时，该端口才会出现。

### **Source of elapsed simulation time** — 经过仿真时间的来源 `Auto`（默认）| `Derive from reference input port`

将经过仿真时间的来源指定为 `Auto` 或 `Derive from reference input port`。当您选择 `Auto` 时，模块计算经过时间。当您选择 `Derive from reference input port` 时，模块使用传入 `Ref` 输入端口的参考信号的时长。

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间编译，但通常运行
更快。

当您开发和调整模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比
解释执行运行得更快。您可以重复执行而无需重新编译，但如果
更改任何模块参数，则模块会在
执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

Motion platform

Motion Platform 模块对多个平台（例如飞机、地面车辆和/或接收与发射传感器阵列）的运动进行建模，确定其位置和速度。平台按照由初始位置和速度确定的轨迹移动，具体取决于您选择的运动模型——速度模型或加速度模型。平台位置和速度在每个仿真步长更新。此外，您可以为平台指定初始方向并获得方向更新。
