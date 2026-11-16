---
type: simulink-block
title: 'Monopulse Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'monopulseestimator'
documentation_source_path: 'ref/monopulseestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Monopulse Estimator

## 端口

### 输入

### **SIGMA** — 和通道信号，复值 *N*-by-1 列向量

和通道信号，指定为复值 *N*-by-1 列向量。*N* 为信号中的快拍数。

**数据类型：** `double`
**复数支持：** 是

### **DeltaAz** — 方位差通道信号，复值 *N*-by-1 列向量

方位差通道信号，指定为复值 *N*-by-1 列向量。*N* 为信号中的快拍数。

**数据类型：** `double`
**复数支持：** 是

### **DeltaEl** — 仰角差通道信号，复值 *M*-by-1

仰角差通道信号，指定为复值 *N*-by-1 列向量。*N* 为信号中的快拍数。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 参数设置为 `3D`。

**数据类型：** `double`
**复数支持：** 是

### **STEER** — 阵列转向方向，标量 | 实值 2-by-1 列向量

阵列转向方向，指定为标量或实值 2-by-1 列向量。

- 将 **Monopulse coverage** 参数设置为 `Azimuth` 时，转向方向为标量，表示方位转向角。
- 将 **Monopulse coverage** 参数设置为 `3D` 时，转向方向向量的形式为 `[azimuthAngle; elevationAngle]`，其中 `azimuthAngle` 为方位转向角，`elevationAngle` 为仰角转向角。

单位为度。方位角介于 –180° 和 180° 之间（含端点），仰角介于 –90° 和 90° 之间（含端点）。

**示例：** `[40;10]`

**数据类型：** `double`
### 输出

### **Az** — 目标方位方向的估计值，实值 1-by-*N* 向量

目标方位方向的估计值，返回为实值 1-by-*N* 向量。向量元素包含每个信号快拍处估计的目标方向方位角。单位为度。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `Azimuth`，并将 **OutputFormat** 设置为 `Angle`。

**数据类型：** `double`

### **dAz** — 目标方位方向的估计偏移，实值 1-by-*N* 向量

目标方位方向的估计偏移，返回为实值 1-by-*N* 向量。向量元素包含每个信号快拍处估计的目标方向方位角相对方位转向方向的偏移。单位为度。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `Azimuth`，并将 **OutputFormat** 设置为 `Angle offset`。

**数据类型：** `double`

### **AzEl** — 目标方向的估计值，实值 2-by-*N* 矩阵

目标方向的估计值，返回为实值 2-by-*N* 矩阵。每列包含形式为 `[azimuthAngle; elevationAngle]` 的目标方向估计值，其中 `azimuthAngle` 为估计的方位角，`elevationAngle` 为估计的仰角。单位为度。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `3D`，并将 **OutputFormat** 设置为 `Angle`。

**数据类型：** `double`

### **dAzEl** — 目标方向的估计偏移，实值 2-by-*N* 矩阵

目标方向的估计偏移，返回为实值 2-by-*N* 矩阵。该偏移为目标方向与转向向量之间的差。每列包含形式为 `[dazimuthAngle; delevationAngle]` 的目标方向估计偏移，其中 `dazimuthAngle` 为估计的方位角偏移，`delevationAngle` 为估计的仰角偏移。单位为度。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `3D`，并将 **OutputFormat** 设置为 `Angle offset`。

**数据类型：** `double`

### **AzRatio** — 和通道与方位差通道的比值，实值 1-by-*N* 向量

和通道与方位差通道的比值，返回为实值 1-by-*N* 向量。其元素包含每个信号快拍处和通道与方位差通道的比值。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `Azimuth`，并选中 **Output sum difference ratio** 复选框。

**数据类型：** `double`

### **AzElRatio** — 和通道与方位差通道及仰角差通道的比值，实值 2-by-*N* 矩阵

和通道与方位差通道及仰角差通道的比值，返回为实值 2-by-*N* 矩阵。第一行的元素包含每个信号快拍处和通道与方位差通道的比值。第二行的元素包含每个信号快拍处和通道与仰角差通道的比值。

#### 依赖关系

要启用此输出端口，请将 **Monopulse coverage** 设置为 `3D`，并选中 **Output sum difference ratio** 复选框。

**数据类型：** `double`

## 参数

#### Main 选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。单位为米/秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实数标量

系统工作频率，指定为正标量。单位为 Hz。

### **Monopulse coverage** — 单脉冲覆盖方向 `3D`（默认）| `Azimuth`

单脉冲覆盖方向，指定为 `3D` 或 `Azimuth`。将此参数设置为 `3D` 时，单脉冲估计器使用和通道以及方位差通道和仰角差通道。将此参数设置为 `Azimuth` 时，单脉冲估计器使用和通道和方位差通道。

### **Squint angle (degrees)** — 偏斜角 `10`（默认）| 标量 | 实值 2-by-1 向量

偏斜角，指定为标量或实值 2-by-1 向量。偏斜角是和波束与沿方位和仰角方向的波束之间的分离角。

- 将 `Monopulse coverage` 参数设置为 `Azimuth` 时，请将 `Squint angle` 参数设置为标量。
- 将 `Monopulse coverage` 参数设置为 `3D` 时，可以将偏斜角指定为标量或向量。如果将 `Squint angle` 参数设置为标量，则方位和仰角方向上的偏斜角相同。如果将 `Squint angle` 参数设置为 2-by-1 向量，则其元素分别指定方位和仰角方向上的偏斜角。

**示例：** `[20;5]`

### **Output format** — 输出方向格式 `Angle`（默认）| `Angle offset`

方向输出的格式，指定为 `Angle` 或 `Angle offset`。将此参数设置为 `Angle` 时，输出端口标记为 `AzEl` 或 `Az`，输出为目标的实际方向。将此属性设置为 `Angle offset` 时，输出端口标记为 `dAzEl` 或 `dAz`，输出为目标相对阵列转向方向的角度偏移。

### **Output sum difference ratio** — 启用和差比输出端口 `off`（默认）| `on`

选中此复选框可输出方位和仰角方向上和通道与差通道的比值。将 **Monopulse coverage** 设置为 `Azimuth` 时，模块通过 `AzRatio` 端口输出和-方位差比值。将 **Monopulse coverage** 设置为 `3D` 时，模块通过 `AzElRatio` 端口输出和-方位差及和-仰角差通道比值。

### **Generate Monopulse Feed** — 创建单脉冲馈源模块的按钮

点击此按钮可基于本模块中的参数创建一个 Monopulse Feed 模块。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真方式，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要一定的编译时间，但通常运行速度更快。

解释执行适用于开发和调优模型。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，即可使用 `Code Generation` 运行模块。对于长时间仿真，使用生成代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### Sensor Arrays 选项卡

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式，Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### 阵元参数

### **Element type** — 阵列阵元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下类型之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认）| 实值 1-by-2 行向量

将天线或麦克风阵元的工作频率范围指定为形如 `[LowerBound,UpperBound]` 的 1-by-2 行向量。阵元在此频率范围之外无响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为由递增实值组成的 1-by-*L* 行向量。天线或麦克风阵元在由此向量的最小元素和最大元素指定的频率范围之外无响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率下的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off（默认）| on

选中此复选框可屏蔽阵元的背面响应。背面屏蔽后，对于偏离侧射方向超过 ±90° 的所有方位角，响应均设置为零。侧射方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负值实值 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或非负值实值 1-by-2 矩阵。当 **Exponent of cosine pattern** 为 1-by-2 向量时，第一个元素为方位方向上的指数，第二个元素为仰角方向上的指数。将此参数设置为标量时，方位方向和仰角方向的余弦方向图均采用相同的幂次。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在由 **Operating frequency vector (Hz)** 参数定义的频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定向量的维度一致。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图时使用的方位角指定为 1-by-*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并按严格递增顺序排列。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图时使用的仰角指定为 1-by-*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），并按严格递增顺序排列。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1-by-*P* 行向量

指定天线辐射方向图时所用点的 Phi 角，指定为实值 1-by-*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并按严格递增顺序排列。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1-by-*Q* 行向量

指定天线辐射方向图所在点的 Theta 角，以实值 1-by-*Q* 行向量形式指定。*Q* 必须大于
2。角度单位为度。Theta 角必须介于 0° 和 360° 之间，并严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认值）| 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的幅度，指定为
*Q*-by-*P* 矩阵或
*Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数
  设置为 `az-el` 时，*Q* 等于
  **Elevation angles
  (deg)** 参数所指定向量的长度，*P* 等于
  **Azimuth angles (deg)**
  参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数
  设置为 `phi-theta` 时，*Q* 等于
  **Theta Angles
  (deg)** 参数所指定向量的长度，*P* 等于
  **Phi Angles (deg)**
  参数所指定向量的长度。

量 *L* 等于
**Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P*
  矩阵，则相同的方向图应用于 **Operating frequency vector (Hz)**
  参数中指定的*所有*频率。
- 如果该值是
  *Q*-by-*P*-by-*L*
  数组，则数组的每个 *Q*-by-*P* 页
  为 **Operating frequency vector (Hz)**
  参数中指定的*相应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认值）| 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的相位，指定为
*Q*-by-*P* 矩阵或
*Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数
  设置为 `az-el` 时，*Q* 等于
  **Elevation angles
  (deg)** 参数所指定向量的长度，*P* 等于
  **Azimuth angles (deg)**
  参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数
  设置为 `phi-theta` 时，*Q* 等于
  **Theta Angles
  (deg)** 参数所指定向量的长度，*P* 等于
  **Phi Angles (deg)**
  参数所指定向量的长度。

量 *L* 等于
**Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P*
  矩阵，则相同的方向图应用于 **Operating frequency vector (Hz)**
  参数中指定的*所有*频率。
- 如果该值是
  *Q*-by-*P*-by-*L*
  数组，则数组的每个 *Q*-by-*P* 页
  为*相应*频率指定一个方向图，该频率指定于
  **Operating frequency vector (**


#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Antenna`。

### **MatchArrayNormal** — 旋转天线元素以对准阵列法向 `on`（默认值）| `off`

选中此复选框可旋转天线元素方向图，使其与阵列法向对齐。未选中时，不旋转元素方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使元素坐标系的 *x* 轴沿阵列法向指向。不选中此复选框则使用未旋转的元素方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使元素坐标系的 *z* 轴沿阵列法向指向。

请将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认值）| 实数标量 | 实值 1-by-*L* 行向量

极坐标方向图麦克风响应频率，指定为实数标量或
实值 1-by-*L* 向量。响应频率位于
**Operating frequency vector (Hz)**
向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认值）| 实值 -by-*P* 行向量

将极坐标方向图响应角度指定为 1-by-*P* 向量。这些
角度相对于麦克风的中心拾取轴测量，并且必须介于
–180° 和 180° 之间（含边界值）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认值）| 实值 *L*-by-*P* 矩阵

将自定义麦克风元素极坐标方向图的幅度指定为
*L*-by-*P* 矩阵。*L* 是
**Polar pattern frequencies (Hz)** 中指定的频率数量。
*P* 是 **Polar pattern
angles (deg)** 中指定的角度数量。矩阵的每一行表示在
**Polar
pattern frequencies (Hz)** 指定的相应频率以及 **Polar
pattern angles (deg)** 指定的所有角度下测得的极坐标方向图幅度。方向图在方位平面内测量。在
方位平面内，仰角为 0°，中心拾取轴位于方位角 0°
和仰角 0° 处。极坐标方向图关于中心轴对称。您可以根据极坐标方向图构建三维空间中的
麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认值）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下值之一：

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意元素
  位置

### **Number of elements** — 阵列元素数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认值）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列元素数量，指定为大于
或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated
subarray` 时，此参数应用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列元素之间的间距 ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认值）| 适用于 ULA 或 URA 阵列的正标量 | 适用于 URA 阵列的正值二元素向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为正标量。
- URA — 将间距指定为正标量或正值 1-by-2 向量。
  如果 **Element spacing (m)** 是标量，
  则行间距和列间距相等。如果 **Element spacing
  (m)** 是向量，则该向量的形式为
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为
  `Replicated subarray` 时，此参数应用于每个
  子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认值）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、
`x` 或 `z`。所有 ULA 阵列
元素在阵列局部坐标系中沿此轴均匀间隔分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为
  `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认值）| 正整数 | 正整数 1-by-2 向量

URA 阵列的维度，指定为正整数或正整数 1-by-2
向量。

- 如果 **Array size** 是 1-by-2 向量，则该向量的
  形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列具有相同的
  行数和列数。
- 当您将 **Specify sensor array as** 设置为
  `Replicated subarray` 时，此参数应用于每个
  子阵列。

对于 URA，阵列元素沿最左列从上到下编索引，
然后从左到右继续对后续各列编索引。在此
图中，**Array size** 值 `[3,2]` 创建一个
三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 元素位置的点阵 `Rectangular`（默认值）| `Triangular`

URA 元素位置的点阵，指定为 `Rectangular`
或 `Triangular`。

- `Rectangular` — 使所有元素在
  行和列方向上对齐。
- `Triangular` — 将矩形点阵的偶数行
  元素沿行轴正方向移动。
  位移为沿行维度元素间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Array normal** — 阵列法向方向 URA 阵列为 `x`，UCA 阵列为 `z`（默认值）| `y`

阵列法向方向，指定为
`x`、
`y` 或
`z`。

平面阵列的元素位于与
所选阵列法向方向正交的平面内。元素瞄准
方向沿阵列法向
方向指向。

| 阵列法向参数值 | 元素位置和瞄准方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面内。所有元素瞄准向量均沿 *x* 轴指向。 |
| `y` | 阵列元素位于 *zx* 平面内。所有元素瞄准向量均沿 *y* 轴指向。 |
| `z` | 阵列元素位于 *xy* 平面内。所有元素瞄准向量均沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将
**Geometry** 设置为
`URA` 或
`UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认值）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认值）| 实值 3-by-*N* 矩阵

共形阵列中元素的位置，指定为
实值 3-by-*N* 矩阵，其中 *N* 是
共形阵列中的元素数量。此矩阵的每一列表示
阵列局部坐标系中一个阵列元素的位置
`[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。
单位为米。

当您将 **Specify sensor array as** 设置为 `Replicated
subarray` 时，此参数应用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal
Array`。

### **Element normals (deg)** — 共形阵列元素法向量的方向 `[0;0]` | 2-by-1 列向量 | 2-by-*N* 矩阵

共形阵列中元素法向量的方向，指定为 2-by-1 列
向量或 2-by-*N* 矩阵。*N* 表示阵列中
的元素数量。对于矩阵，每一列以
`[azimuth;elevation]` 的形式指定相应元素相对于局部坐标系的法向
方向。局部坐标系将 *x* 轴正方向与共形阵列的法向方向对齐。如果
参数值是 2-by-1 列向量，则所有
阵列元素使用相同的指向。

当您将 **Specify sensor array as** 设置为 `Replicated
subarray` 时，此参数应用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element
normals (deg)** 参数表示元素对之间存在特定变换差异的任何排列。这些变换可以组合平移、
方位旋转和仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`Conformal Array`。

### **Taper** — 阵列元素锥削 1（默认值）| 复值标量 | 复值行向量

元素锥削，指定为复值标量或
复值 1-by-*N* 行向量。在此
向量中，*N* 表示阵列中
的元素数量。

锥削也称为*元素权重*，会与
阵列元素响应相乘。锥削同时修改响应的幅度和
相位，以降低旁瓣或使主
响应轴转向。

如果 **Taper** 是标量，则相同的权重应用于
每个元素。如果 **Taper** 是向量，则
向量中的权重应用于相应的传感器
元素。权重数量必须与阵列的元素
数量相匹配。

当您将 **Specify sensor array as** 设置为
`Replicated subarray` 时，此
参数应用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的元素 logical matrix

将子阵列选择指定为 *M*-by-*N*
矩阵。*M* 是子阵列的数量，*N* 是
阵列中元素的总数。矩阵的每一行表示一个子阵列，
该行中的每个条目指示对应元素是否属于该子阵列。当条目
为零时，元素不属于该子阵列。非零条目表示
应用于相应元素的复值权重。每行必须至少包含
一个非零条目。

每个子阵列的相位中心位于子阵列的几何中心。子阵列的
几何中心取决于 **Subarray definition matrix** 和
**Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为
`Partitioned array`。

### **Subarray steering method** — 指定子阵列转向方法 `None`（默认值）| `Phase` | `Time`

子阵列转向方法，指定为以下值之一：

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会在
Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、
Wideband Transmit Array 模块以及 Constant Gamma
Clutter 和 GPU Constant Gamma Clutter 模块上打开
`Steer` 输入端口。

选择 `Custom` 会在
Narrowband Receive Array、Narrowband Transmit Array、
Wideband Receive Array、Wideband Transmit Array
模块以及 Constant Gamma Clutter 和 GPU Constant Gamma
Clutter 模块上打开 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为
`Partitioned array` 或 `Replicated
subarray`。

### **Phase shifter frequency (Hz)** — 子阵列相移频率 `3.0e8`（默认值）| 正实值标量

子阵列转向移相器的工作频率，指定为正
实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为
`Partitioned array` 或 `Replicated subarray`，
并将 **Subarray steering method** 设置为
`Phase`。

### **Number of bits in phase shifters** — 子阵列转向相移量化位数 `0`（默认值）| 非负整数

子阵列转向相移量化位数，指定为非负整数。
值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为
`Partitioned array` 或 `Replicated subarray`，
并将 **Subarray steering method** 设置为
`Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular` (默认) | `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 当将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 当将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`。

### **Grid size** — 矩形子阵网格的尺寸 `[1,2]` (默认)

矩形子阵网格的大小，指定为单个正整数，或由正整数组成的 1-by-2 行向量。

如果 **Grid size** 是整数标量，则阵列的每行和每列包含相同数量的子阵。如果 **Grid size** 是形如 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 向量，则第一个元素是沿每列排列的子阵数量，第二个元素是每行中的子阵数量。行沿局部 *y* 轴方向，列沿局部 *z* 轴方向。此处的图显示了如何将 **Grid size** 设置为 `[1,2]` 来复制 3-by-2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto` (默认) | 正实数标量 | 由正实数组成的 1-by-2 向量

子阵的矩形网格间距，指定为正实数标量、由正实数组成的 1-by-2 行向量或 `Auto`。单位为 meters。

- 如果 **Grid spacing** 是标量，则沿行方向的间距与沿列方向的间距相同。
- 如果 **Grid spacing** 是 1-by-2 行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个元素指定沿列方向的行间距，第二个元素指定沿行方向的列间距。
- 如果 **Grid spacing** 设置为 `Auto`，则在构建完整阵列时，复制操作会保留子阵在行和列两个方向上的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵的位置 `[0,0;0.5,0.5;0,0]` (默认) | 实数 3-by-*N* 矩阵

自定义网格中子阵的位置，指定为实数 3-by-*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示单个子阵在阵列局部坐标系中的位置。坐标以 `[x; y; z]` 的形式表示。单位为 meters。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量的方向 `[0,0;0,0]` (默认) | 实数 2-by-*N* 矩阵

指定阵列中各子阵的法线方向。此参数值是一个 2-by-*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列以 `[azimuth;elevation]` 的形式指定对应子阵的法线方向。角度单位为 degrees。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示任意布置，其中成对的子阵之间可通过特定变换相互转换。这些变换可以组合平移、方位角旋转和仰角旋转。但是，不能使用需要绕法线旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2018b 中引入**

## 描述

通过和通道与差通道估计目标方向

Monopulse Estimator 模块根据初始估计值，对阵列接收的和通道与差通道信号应用幅度单脉冲处理，以估计窄带信号的到达方向。您可以使用 Monopulse Feed 模块创建这些通道。
