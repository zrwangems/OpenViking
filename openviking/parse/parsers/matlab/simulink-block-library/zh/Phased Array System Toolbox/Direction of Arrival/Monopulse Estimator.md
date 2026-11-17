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
```yaml
ports:
- name: SIGMA
  summary: 和通道信号，复值 *N*×1 列向量
  direction: input
  data_types: double
- name: DeltaAz
  summary: 方位差通道信号，复值 *N*×1 列向量
  direction: input
  data_types: double
- name: DeltaEl
  summary: 俯仰差通道信号，复值 *M*×1
  direction: input
  data_types: double
- name: STEER
  summary: 阵列导向方向，标量 | 实值 2×1 列向量
  direction: input
  data_types: double
- name: Az
  summary: 目标的估计方位方向，实值 1×*N* 向量
  direction: output
  data_types: double
- name: dAz
  summary: 目标方位方向的估计偏移量，实值 1×*N* 向量
  direction: output
  data_types: double
- name: AzEl
  summary: 目标的估计方向，实值 2×*N* 矩阵
  direction: output
  data_types: double
- name: dAzEl
  summary: 目标方向的估计偏移量，实值 2×*N* 矩阵
  direction: output
  data_types: double
- name: AzRatio
  summary: 和通道与方位差通道的比值，实值 1×*N* 向量
  direction: output
  data_types: double
- name: AzElRatio
  summary: 和通道与方位差通道及俯仰差通道的比值，实值 2×*N* 矩阵
  direction: output
  data_types: double
```

### 输入

### **SIGMA** — 和通道信号，复值 *N*×1 列向量

和通道信号，指定为复值 *N*×1 列向量。*N* 是信号中的快拍数。

**数据类型：** `double`
**支持复数：** 是

### **DeltaAz** — 方位差通道信号，复值 *N*×1 列向量

方位差通道信号，指定为复值 *N*×1 列向量。*N* 是信号中的快拍数。

**数据类型：** `double`
**支持复数：** 是

### **DeltaEl** — 俯仰差通道信号，复值 *M*×1

俯仰差通道信号，指定为复值 *N*×1 列向量。*N* 是信号中的快拍数。

#### 依赖

要启用此输出端口，请将 **Monopulse coverage** 参数设置为 `3D`。

**数据类型：** `double`
**支持复数：** 是

### **STEER** — 阵列导向方向，标量 | 实值 2×1 列向量

阵列导向方向，指定为标量或实值 2×1 列向量。

- 当您将 **Monopulse coverage** 参数设置为 `Azimuth` 时，导向方向为标量，表示方位导向角。
- 当您将 **Monopulse coverage** 参数设置为 `3D` 时，导向方向向量的形式为 `[azimuthAngle; elevationAngle]`，其中 `azimuthAngle` 是方位导向角，`elevationAngle` 是俯仰导向角。

单位为度。方位角范围在 –180° 到 180° 之间（含边界），俯仰角范围在 –90° 到 90° 之间（含边界）。

**示例：** `[40;10]`

**数据类型：** `double`
### 输出

### **Az** — 目标的估计方位方向，实值 1×*N* 向量

目标的估计方位方向，返回为实值 1×*N*。向量元素包含每个信号快拍处估计的目标方向方位角。单位为度。

#### 依赖

要启用此输出端口，请将 **Monopulse coverage** 设置为 `Azimuth`，并将 **OutputFormat** 设置为 `Angle`。

**数据类型：** `double`

### **dAz** — 目标方位方向的估计偏移量，实值 1×*N* 向量

目标方位方向的估计偏移量，返回为实值 1×*N* 向量。向量元素包含每个信号快拍处估计的目标方向方位角相对于方位导向方向的偏移量。单位为度。

#### 依赖

要启用此输出端口，请将 **Monopulse coverage** 设置为 `Azimuth`，并将 **OutputFormat** 设置为 `Angle offset`。

**数据类型：** `double`

### **AzEl** — 目标的估计方向，实值 2×*N* 矩阵

目标的估计方向，返回为实值 2×*N* 矩阵。每一列包含形式为 `[azimuthAngle; elevationAngle]` 的估计目标方向，其中 `azimuthAngle` 是估计的方位角，`elevationAngle` 是估计的俯仰角。单位为度。

#### 依赖

要启用此输出端口，请将 **Monopulse coverage** 设置为 `3D`，并将 **OutputFormat** 设置为 `Angle`。

**数据类型：** `double`

### **dAzEl** — 目标方向的估计偏移量，实值 2×*N* 矩阵

目标方向的估计偏移量，返回为实值 2×*N* 矩阵。偏移量是目标方向与导向向量之间的差值。每一列包含形式为 `[dazimuthAngle; delevationAngle]` 的估计目标方向偏移量，其中 `dazimuthAngle` 是估计的方位角偏移量，`delevationAngle` 是估计的俯仰角偏移量。单位为度。

#### 依赖

要启用此输出端口，请将 **Monopulse coverage** 设置为 `3D`，并将 **OutputFormat** 设置为 `Angle offset`。

**数据类型：** `double`

### **AzRatio** — 和通道与方位差通道的比值，实值 1×*N* 向量

和通道与方位差通道的比值，以实值 1×*N* 向量返回。其元素包含每个信号快拍处和通道与方位差通道的比值。

#### 依赖

要启用此输出端口，请将**单脉冲覆盖**设置为 `Azimuth`，并选中**输出和差比**复选框。

**数据类型：** `double`

### **AzElRatio** — 和通道与方位差通道及俯仰差通道的比值，实值 2×*N* 矩阵

和通道与方位差通道及俯仰差通道的比值，以实值 2×*N* 矩阵返回。第一行的元素包含每个信号快拍处和通道与方位差通道的比值。第二行的元素包含每个信号快拍处和通道与俯仰差通道的比值。

#### 依赖

要启用此输出端口，请将**单脉冲覆盖**设置为 `3D`，并选中**输出和差比**复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: 信号传播速度 (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 实值正标量
  group: ''
- name: 工作频率 (Hz)
  summary: 系统工作频率 3e8（默认）| 正实标量
  group: ''
- name: 单脉冲覆盖
  summary: 单脉冲覆盖方向 3D（默认）| Azimuth
  group: ''
- name: 斜视角 (度)
  summary: 斜视角 10（默认）| 标量 | 实值 2×1 向量
  group: ''
- name: 输出格式
  summary: 输出方向格式 Angle（默认）| Angle offset
  group: ''
- name: 输出和差比
  summary: 启用和差比输出端口 off（默认）| on
  group: ''
- name: Generate Monopulse Feed
  summary: 创建单脉冲馈源模块按钮
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
- name: Specify sensor array as
  summary: 指定阵列的方法 Array (no subarrays)（默认）| Partitioned array | Replicated subarray | MATLAB expression
  group: ''
- name: Expression
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object
  group: ''
- name: Element type
  summary: 阵列单元类型 Isotropic Antenna（默认）| Cosine Antenna | Custom Antenna | Omni Microphone | Custom Microphone
  group: ''
- name: Operating frequency range (Hz)
  summary: 天线或麦克风单元的工作频率范围 [0,1e20]（默认）| 实值 1×2 行向量
  group: ''
- name: 工作频率向量 (Hz)
  summary: 自定义天线或麦克风元件的工作频率范围 [0,1e20]（默认）| 实值行向量
  group: ''
- name: Baffle the back of the element
  summary: 将 Isotropic Antenna 元件或 Omni Microphone 元件的背面响应设置为零 off（默认）| on
  group: ''
- name: Exponent of cosine pattern
  summary: 方位角和仰角余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实值 1×2 矩阵
  group: ''
- name: Frequency responses (dB)
  summary: 天线和麦克风频率响应 [0,0]（默认）| 实值行向量
  group: ''
- name: Input Pattern Coordinate System
  summary: 自定义天线方向图的坐标系 az-el（默认）| phi-theta
  group: ''
- name: Azimuth angles (deg)
  summary: 天线辐射方向图的方位角 [-180:180]（默认）| 实值行向量
  group: ''
- name: Elevation angles (deg)
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实值行向量
  group: ''
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角度坐标 0:360 | 实值 1×*P* 行向量
  group: ''
- name: Theta Angles (deg)
  summary: 自定义天线辐射方向图的 Theta 角度坐标 0:180 | 实值 1×*Q* 行向量
  group: ''
- name: Magnitude pattern (dB)
  summary: 组合天线辐射方向图的幅度 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: Phase pattern (deg)
  summary: 自定义天线辐射相位方向图 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: MatchArrayNormal
  summary: 将天线阵子旋转至阵列法向 on（默认）| off
  group: ''
- name: Polar pattern frequencies (Hz)
  summary: 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量
  group: ''
- name: Polar pattern angles (deg)
  summary: 极坐标方向图响应角度 [-180:180]（默认）| 实值 1×*P* 行向量
  group: ''
- name: Polar pattern (dB)
  summary: 自定义麦克风极坐标响应 zeros(1,361)（默认）| 实值 *L*×*P* 矩阵
  group: ''
- name: Geometry
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: ''
- name: Number of elements
  summary: 阵列阵子数量 ULA 阵列为 2，UCA 阵列为 5（默认）| 大于或等于 2 的整数
  group: ''
- name: Element spacing (m)
  summary: 阵列元素间距，对于 ULA 阵列为 0.5，对于 URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量
  group: ''
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: ''
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 的正整数向量
  group: ''
- name: Element lattice
  summary: URA 元素位置的晶格 Rectangular（默认）| Triangular
  group: ''
- name: Array normal
  summary: 阵列法线方向，对于 URA 阵列为 x，对于 UCA 阵列为 z（默认）| y
  group: ''
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: ''
- name: Element positions (m)
  summary: 共形阵列元素的位置 [0;0;0]（默认）| 3×*N* 的实数值矩阵
  group: ''
- name: Element normals (deg)
  summary: 共形阵列元素法向量的方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: ''
- name: Taper
  summary: 阵列元素加权 1（默认）| 复数值标量 | 复数值行向量
  group: ''
- name: Subarray definition matrix
  summary: 定义属于子阵列的元素 逻辑矩阵
  group: ''
- name: Subarray steering method
  summary: 指定子阵导向方法 None（默认）| Phase | Time
  group: ''
- name: Phase shifter frequency (Hz)
  summary: 子阵相移频率 3.0e8（默认）| 正实值标量
  group: ''
- name: Number of bits in phase shifters
  summary: 子阵导向相移量化位数 0（默认）| 非负整数
  group: ''
- name: Subarrays layout
  summary: 子阵位置指定 Rectangular（默认）| Custom
  group: ''
- name: Grid size
  summary: 矩形子阵网格的维度 [1,2]（默认）
  group: ''
- name: Grid spacing (m)
  summary: 矩形网格上子阵之间的间距 Auto（默认）| 正实值标量 | 正实值的 1×2 向量
  group: ''
- name: Subarray positions (m)
  summary: 子阵位置 [0,0;0.5,0.5;0,0]（默认）| 3×*N* 实值矩阵
  group: ''
- name: Subarray normals
  summary: 子阵法向量方向 [0,0;0,0]（默认）| 2×*N* 实矩阵
  group: ''
```

#### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **单脉冲覆盖** — 单脉冲覆盖方向 `3D`（默认）| `Azimuth`

单脉冲覆盖方向，指定为 `3D` 或 `Azimuth`。当您将此参数设置为 `3D` 时，单脉冲估计器使用和通道以及方位差通道和俯仰差通道。当您将此参数设置为 `Azimuth` 时，单脉冲估计器使用和通道以及方位差通道。

### **斜视角 (度)** — 斜视角 `10`（默认）| 标量 | 实值 2×1 向量

斜视角，指定为标量或实值 2×1 向量。斜视角是和波束与沿方位方向和俯仰方向的波束之间的分离角。

- 当您将 `Monopulse coverage` 参数设置为 `Azimuth` 时，将 `Squint angle` 参数设置为标量。
- 当您将 `Monopulse coverage` 参数设置为 `3D` 时，您可以将斜视角指定为标量或向量。如果您将 `Squint angle` 参数设置为标量，则斜视角沿方位方向和俯仰方向相同。如果您将 `Squint angle` 参数设置为 2×1 向量，则其元素分别指定沿方位方向和俯仰方向的斜视角。

**示例：** `[20;5]`

### **输出格式** — 输出方向格式 `Angle`（默认）| `Angle offset`

方向输出的格式，指定为 `Angle` 或 `Angle offset`。当您将此参数设置为 `Angle` 时，输出端口标记为 `AzEl` 或 `Az`，并且是目标的实际方向。当您将此属性设置为 `Angle offset` 时，输出端口标记为 `dAzEl` 或 `dAz`，并且是目标相对于阵列 steering 方向的角度偏移。

### **输出和差比** — 启用和差比输出端口 `off`（默认）| `on`

选中此复选框以输出方位方向和俯仰方向上和通道与差通道的比值。当您将**单脉冲覆盖**设置为 `Azimuth` 时，该模块使用 `AzRatio` 端口输出和-方位差比。当您将**单脉冲覆盖**设置为 `3D` 时，该模块使用 `AzElRatio` 端口输出和-方位差通道与和-俯仰差通道的比值。

### **Generate Monopulse Feed** — 创建单脉冲馈源模块按钮

点击此按钮，基于此模块中的参数创建 Monopulse Feed 模块。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

解释执行在开发和调整模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

#### Sensor Arrays Tab

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**Example:** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### Element Parameters

### **Element type** — 阵列单元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风单元的工作频率范围 `[0,1e20]`（默认）| 实值 1×2 行向量

将天线或麦克风单元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该单元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风元件的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为一个 1×*L* 的递增实值行向量。天线或麦克风元件在该向量最小值和最大值所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的背面响应设置为零 off（默认）| on

选中此复选框以遮挡元件的背面响应。当背面被遮挡时，所有偏离视轴方向超过 ±90° 的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在 **Operating frequency vector (Hz)** 参数所定义的频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图的方位角指定为一个 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图的仰角指定为一个 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角度坐标 `0:360` | 实值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角度，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角度必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角度坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角度，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角度必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵子旋转至阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵子方向图旋转至与阵列法向对齐。未选中时，阵子方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵子坐标系的 *x* 轴指向阵列法向。未选中时使用未旋转的阵子方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵子坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风中心拾音轴测量，必须介于 –180° 和 180° 之间（含边界值）。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵子极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵子位置

### **Number of elements** — 阵列阵子数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵子数量，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列元素间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 的正数值向量。如果 **Element spacing (m)** 为标量，则行间距和列间距相等。如果 **Element spacing (m)** 为向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列元素在本地阵列坐标系中沿此轴均匀分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 的正整数向量

URA 阵列的维度，指定为正整数或 1×2 的正整数向量。

- 如果 **Array size** 为 1×2 向量，则该向量的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 为整数，则阵列的行数和列数相同。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列元素沿最左侧列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值为 `[3,2]` 会创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 元素位置的晶格 `Rectangular`（默认）| `Triangular`

URA 元素位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有元素沿行和列方向对齐。
- `Triangular` — 将矩形晶格的偶数行元素向正行轴方向偏移。位移为沿行维度元素间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向，对于 URA 阵列为 `x`，对于 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的元素位于与所选阵列法线方向正交的平面内。元素视轴方向沿阵列法线方向指向。

| 阵列法向参数值 | 阵元位置和波束指向方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面内。所有元素视轴向量沿 *x* 轴指向。 |
| `y` | 阵列元素位于 *zx* 平面内。所有元素视轴向量沿 *y* 轴指向。 |
| `z` | 阵列元素位于 *xy* 平面内。所有元素视轴向量沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认）| 3×*N* 的实数值矩阵

共形阵列中元素的位置，指定为 3×*N* 的实数值矩阵，其中 *N* 是共形阵列中的元素数量。该矩阵的每一列表示阵列局部坐标系中一个阵列元素的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列元素法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中元素法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的元素数量。对于矩阵，每一列以 `[azimuth;elevation]` 的形式指定相应元素相对于局部坐标系的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列元素使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示元素对之间通过特定变换产生差异的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法向方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列元素加权 1（默认）| 复数值标量 | 复数值行向量

元素加权，指定为复数值标量或复数值 1×*N* 行向量。在此向量中，*N* 表示阵列中的元素数量。

也称为*元素权重*，加权对阵列元素响应进行乘法运算。加权修改响应的幅度和相位，以减少旁瓣或调整主响应轴的方向。

如果 **Taper** 是标量，则对每个元素应用相同的权重。如果 **Taper** 是向量，则将向量中的权重应用于相应的传感器元素。权重的数量必须与阵列的元素数量匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的元素 逻辑矩阵

将子阵列选择指定为 *M*×*N* 矩阵。*M* 是子阵列的数量，*N* 是阵列中元素的总数。矩阵的每一行表示一个子阵列，行中的每个条目指示元素何时属于该子阵列。当条目为零时，该元素不属于该子阵列。非零条目表示应用于相应元素的复数值权重。每一行必须至少包含一个非零条目。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵导向方法 `None`（默认）| `Phase` | `Time`

子阵导向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵相移频率 `3.0e8`（默认）| 正实值标量

子阵导向相移器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵导向相移量化位数 `0`（默认）| 非负整数

子阵导向相移量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认）| `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 当将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 当将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认）

矩形子阵网格大小，指定为单个正整数，或正整数的 1×2 行向量。

如果 **Grid size** 是整数标量，则阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个条目是沿每一列的子阵数量。第二个条目是每一行中的子阵数量。行沿局部 *y* 轴，列沿局部 *z* 轴。此处的图显示了如何使用 **Grid size** 为 `[1,2]` 来复制 3×2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认）| 正实值标量 | 正实值的 1×2 向量

子阵的矩形网格间距，指定为正实值标量、正实值的 1×2 行向量，或 `Auto`。单位为米。

- 如果 **Grid spacing** 是标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 是 1×2 行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个条目指定沿列的行之间的间距。第二个条目指定沿行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则复制在构建完整阵列时对行和列均保留子阵的阵元间距。仅当将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为
`Replicated subarray`，并将 **Subarrays layout**
设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵位置 `[0,0;0.5,0.5;0,0]`（默认）| 3×*N* 实值矩阵

自定义网格中子阵的位置，指定为实值
3×*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示阵列局部坐标系中单个
子阵的位置。坐标以
`[x; y; z]` 形式表示。单位为米。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为
`Replicated subarray`，并将 **Subarrays layout**
设置为 `Custom`。

### **Subarray normals** — 子阵法向量方向 `[0,0;0,0]`（默认）| 2×*N* 实矩阵

指定阵列中子阵的法线方向。此参数值为
2×*N* 矩阵，其中 *N* 是阵列中的
子阵数量。矩阵的每一列指定对应子阵的法线方向，形式为 `[azimuth;elevation]`。角度单位
为度。角度相对于局部坐标系定义。

您可以使用 **Subarray positions** 和 **Subarray
normals** 参数来表示子阵对之间通过特定变换产生差异的任何排列。这些变换可以组合
平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法线旋转的
变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为
`Replicated subarray`，并将 **Subarrays
layout** 设置为 `Custom`。
## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

根据和差通道估计目标方向

Monopulse Estimator 基于初始猜测，通过对阵列接收的和差通道信号应用振幅单脉冲处理，估计窄带信号的到达方向。您可以使用 Monopulse
Feed 模块创建这些通道。
