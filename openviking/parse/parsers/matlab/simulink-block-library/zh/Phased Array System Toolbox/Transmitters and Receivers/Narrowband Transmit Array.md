---
type: simulink-block
title: 'Narrowband Transmit Array'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'narrowbandtransmitarray'
documentation_source_path: 'ref/narrowbandtransmitarray.html'
language: zh-CN
chinese_source: worker-translation
---

# Narrowband Transmit Array

## 端口
```yaml
ports:
- name: X
  summary: 辐射信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵
  direction: input
  data_types: double
- name: Ang
  summary: 输入 实值 2×*L* 矩阵
  direction: input
  data_types: double
- name: W
  summary: 元素或子阵列权重 *N*×1 列向量
  direction: input
  data_types: double
- name: WS
  summary: 子阵列元素权重输入端口 复值 *N*SE×*N* 矩阵 | 1×*N* 元胞数组
  direction: input
  data_types: double
- name: Steer
  summary: 输入 实值 2×1 向量
  direction: input
  data_types: double
- name: Output 1
  summary: 输出 复值 *M*×*L* 矩阵
  direction: output
  data_types: double
```

### 输入

### **X** — 辐射信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵

辐射信号，指定为复值 *M*×1 向量或复值 *M*×*N* 矩阵。*M* 是信号的长度，*N* 是阵列元素的数量（或当支持子阵列时的子阵列数量）。

**X 的维度**

| 维度 | 信号 |
| --- | --- |
| *M*×1 向量 | 相同的信号从所有阵列元素（或当支持子阵列时的所有子阵列）辐射。 |
| `M-by-N matrix` | 每一列对应于相应阵列元素（或当支持子阵列时的相应子阵列）辐射的信号。 |

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 输入 实值 2×*L* 矩阵

信号的辐射方向，指定为实值 2×*L* 矩阵。每一列以 `[AzimuthAngle;ElevationAngle]` 的形式指定一个辐射方向。方位角必须介于 –180° 和 180° 之间（含边界值）。仰角必须介于 –90° 和 90° 之间（含边界值）。单位为度。

**示例：** `[30,20;45,0]`

**数据类型：** `double`

### **W** — 元素或子阵列权重 *N*×1 列向量

元素或子阵列权重，指定为复值 *N*×1 列向量，其中 *N* 是阵列元素的数量（或当阵列支持子阵列时的子阵列数量）。

#### 依赖关系

要启用此端口，请选中 **Enable weights input** 复选框。

**数据类型：** `double`

### **WS** — 子阵列元素权重输入端口 复值 *N*SE×*N* 矩阵 | 1×*N* 元胞数组

子阵列元素权重，指定为复值 *N*SE×*N* 矩阵或 1×*N* 元胞数组，其中 *N* 是子阵列的数量。这些权重应用于子阵列内的各个元素。

**子阵列元素权重**

| 传感器阵列 | 子阵列权重 |
| --- | --- |
| 复制子阵列 | 所有子阵列具有相同的维度和大小。此时，子阵列权重构成一个 *N*SE×*N* 矩阵。*N*SE 是每个子阵列中元素的数量，*N* 是子阵列的数量。`WS` 的每一列指定对应子阵列的权重。 |
| 分区阵列 | 子阵列可能不具有相同的维度和大小。在这种情况下，您可以将子阵列权重指定为  - 一个 *N*SE×*N* 矩阵，其中 *N*SE 现在是最大子阵列中元素的数量。每列中的前 *Q* 个条目是子阵列的元素权重，其中 *Q* 是该子阵列中元素的数量。 - 一个 1×*N* 元胞数组。每个元胞包含对应子阵列的权重列向量。列向量的长度等于对应子阵列中元素的数量。 |

#### 依赖关系

要启用此端口，请将 `Specify sensor array as` 参数指定为 **Replicated subarray** 或 **Partitioned array**，然后从 **Subarray steering method** 下拉菜单中选择 `Custom`。

**数据类型：** `double`

### **Steer** — 输入 实值 2×1 向量

子阵列转向角，指定为长度为 2 的列向量。该向量具有 `[azimuthAngle;elevationAngle]` 的形式。方位角必须介于 –180° 和 180° 之间（含边界值）。仰角必须介于 –90° 和 90° 之间（含边界值）。单位为度。

#### 依赖关系

要启用此端口，请从 **Subarray steering method** 下拉菜单中选择 `Phase` 或 `Time`。

**数据类型：** `double`
### 输出

### **Output 1** — 输出 复值 *M*×*L* 矩阵

辐射信号，指定为复值 *M*×*L* 矩阵，其中 *L* 是 `Ang` 中辐射角的数量。*M* 是输入信号 `X` 的长度。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: 传播速度 (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: 主选项卡
- name: 工作频率 (Hz)
  summary: 系统工作频率 3e8（默认）| 正实标量
  group: 主选项卡
- name: 传感器增益度量
  summary: 指定传感器增益 dB（默认）| dBi
  group: 主选项卡
- name: 启用权重输入
  summary: 启用权重输入 off（默认）| on
  group: 主选项卡
- name: 仿真方式
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: 主选项卡
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
- name: 指定传感器阵列方式
  summary: 指定阵列的方法 Array (no subarrays)（默认）| Single element | Partitioned array | Replicated subarray | MATLAB expression
  group: 传感器阵列选项卡
  type: ''
- name: Element type
  summary: 阵列单元类型 Isotropic Antenna（默认）| Cardioid Antenna | Cosine Antenna | Custom Antenna | Gaussian Antenna | Sinc Antenna
    | Omni Microphone | Custom Microphone
  group: 传感器阵列选项卡
- name: Operating frequency range (Hz)
  summary: 天线或麦克风单元的工作频率范围 [0,1e20]（默认）| 实值 1×2 行向量
  group: 传感器阵列选项卡
- name: Baffle the back of the element
  summary: 将 Isotropic Antenna 单元或 Omni Microphone 单元的后向响应设置为零 off（默认）| on
  group: 传感器阵列选项卡
- name: Null axis direction
  summary: 零轴方向 -x（默认）| +x | +y | -y | +z | -z
  group: 传感器阵列选项卡
- name: Exponent of cosine pattern
  summary: 方位角和仰角余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实值 1×2 矩阵
  group: 传感器阵列选项卡
- name: Operating frequency vector (Hz)
  summary: 自定义天线或麦克风单元的工作频率范围 [0,1e20]（默认）| 实值行向量
  group: 传感器阵列选项卡
- name: Frequency responses (dB)
  summary: 天线和麦克风频率响应 [0,0]（默认）| 实值行向量
  group: 传感器阵列选项卡
- name: Input Pattern Coordinate System
  summary: 自定义天线方向图的坐标系 az-el（默认）| phi-theta
  group: 传感器阵列选项卡
- name: Azimuth angles (deg)
  summary: 天线辐射方向图的方位角 [-180:180]（默认）| 实值行向量
  group: 传感器阵列选项卡
- name: Elevation angles (deg)
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实值行向量
  group: 传感器阵列选项卡
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角坐标 0:360 | 实值 1×*P* 行向量
  group: 传感器阵列选项卡
- name: Theta Angles (deg)
  summary: 自定义天线辐射方向图的 Theta 角坐标 0:180 | 实值 1×*Q* 行向量
  group: 传感器阵列选项卡
- name: Magnitude pattern (dB)
  summary: 组合天线辐射方向图的幅度 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: 传感器阵列选项卡
- name: Phase pattern (deg)
  summary: 自定义天线辐射相位方向图 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: 传感器阵列选项卡
- name: Align element normal with array normal
  summary: 将阵元法线与阵列法线对齐 on（默认）| off
  group: 传感器阵列选项卡
- name: Radiation pattern beamwidth (deg)
  summary: 辐射方向图波束宽度 [10,10]（默认）
  group: 传感器阵列选项卡
- name: Polar pattern frequencies (Hz)
  summary: 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量
  group: 传感器阵列选项卡
- name: Polar pattern angles (deg)
  summary: 极坐标方向图响应角度 [-180:180]（默认）| 实值 1×*P* 行向量
  group: 传感器阵列选项卡
- name: Polar pattern (dB)
  summary: 自定义麦克风极性响应 zeros(1,361)（默认）| 实值 *L*×*P* 矩阵
  group: 传感器阵列选项卡
- name: Geometry
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: 传感器阵列选项卡
- name: Number of elements
  summary: 阵列阵元数量 ULA 阵列为 2，UCA 阵列为 5（默认）| 大于或等于 2 的整数
  group: 传感器阵列选项卡
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 正整数向量
  group: 传感器阵列选项卡
- name: Element spacing (m)
  summary: 阵列阵元之间的间距 ULA 阵列为 0.5，URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为 2 元素正数值向量
  group: 传感器阵列选项卡
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: 传感器阵列选项卡
- name: Element lattice
  summary: URA 阵元位置的晶格 Rectangular（默认）| Triangular
  group: 传感器阵列选项卡
- name: Array normal
  summary: 阵列法线方向 URA 阵列为 x 或 UCA 阵列为 z（默认）| y
  group: 传感器阵列选项卡
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: 传感器阵列选项卡
- name: Element positions (m)
  summary: 共形阵列阵元位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: 传感器阵列选项卡
- name: Element normals (deg)
  summary: 共形阵列阵元法向量的方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: 传感器阵列选项卡
- name: Taper
  summary: 阵元锥削 1（默认）| 复值标量 | 复值行向量
  group: 传感器阵列选项卡
- name: Subarray definition matrix
  summary: 定义属于子阵的阵元 逻辑矩阵
  group: 传感器阵列选项卡
- name: Subarray steering method
  summary: 指定子阵导向方法 None（默认）| Phase | Time
  group: 传感器阵列选项卡
- name: Phase shifter frequency (Hz)
  summary: 子阵移相频率 3.0e8（默认）| 正实值标量
  group: 传感器阵列选项卡
- name: Number of bits in phase shifters
  summary: 子阵导向移相量化位数 0（默认）| 非负整数
  group: 传感器阵列选项卡
- name: Subarrays layout
  summary: 子阵位置指定 Rectangular（默认）| Custom
  group: 传感器阵列选项卡
- name: Grid size
  summary: 矩形子阵网格的维度 [1,2]（默认值）
  group: 传感器阵列选项卡
- name: Grid spacing (m)
  summary: 矩形网格上子阵之间的间距 Auto（默认值） | 正实值标量 | 由正实值组成的 1×2 向量
  group: 传感器阵列选项卡
- name: Subarray positions (m)
  summary: 子阵的位置 [0,0;0.5,0.5;0,0]（默认值） | 3×*N* 实值矩阵
  group: 传感器阵列选项卡
- name: Subarray normals
  summary: 子阵法向量的方向 [0,0;0,0]（默认值） | 2×*N* 实矩阵
  group: 传感器阵列选项卡
- name: Expression
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object
  group: 传感器阵列选项卡
- name: Analyze
  summary: 启动 Sensor Array Analyzer（默认）
  group: 传感器阵列选项卡
```

### 主选项卡

### **传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **传感器增益度量** — 指定传感器增益 `dB`（默认）| `dBi`

将传感器增益度量指定为 `dB` 或 `dBi`。

- 当您将此参数设置为 `dB` 时，输入信号功率按对应方向上的传感器功率方向图（以 dB 为单位）进行缩放，然后进行合并。
- 当您将此参数设置为 `dBi` 时，输入信号功率按对应方向上的方向性方向图（以 dBi 为单位）进行缩放，然后进行合并。当您希望将结果与使用 dBi 指定天线增益的雷达方程计算的值进行比较时，此选项非常有用。使用 `dBi` 选项的计算开销较大，因为它需要对所有方向进行积分以计算传感器的总辐射功率。默认值为 `dB`。

### **启用权重输入** — 启用权重输入 off（默认）| on

选中此复选框以使用输入端口 `W` 指定阵列权重。仅当选中此复选框时，输入端口才会出现。

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |

### 传感器阵列选项卡

### **指定传感器阵列方式** — 指定阵列的方法 `Array (no subarrays)`（默认）| `Single element` | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定传感器元件或传感器阵列。传感器阵列还可以包含子阵列或为分区阵列。此参数也可以表示为 MATLAB 表达式。

**类型**

|  |
| --- |
| `Single element` |
| `Array (no subarrays)` |
| `Partitioned array` |
| `Replicated subarray` |
| `MATLAB expression` |

#### 元件参数

### **Element type** — 阵列单元类型 `Isotropic Antenna`（默认）| `Cardioid Antenna` | `Cosine Antenna` | `Custom Antenna` | `Gaussian Antenna` | `Sinc Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cardioid Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Gaussian Antenna`
- `Sinc Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风单元的工作频率范围 `[0,1e20]`（默认）| 实值 1×2 行向量

将天线或麦克风单元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该单元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 单元或 `Omni Microphone` 单元的后向响应设置为零 off（默认）| on

选中此复选框以遮挡该单元的后向响应。当后向遮挡时，所有偏离视轴方向 ±90° 以外的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Null axis direction** — 零轴方向 `-x`（默认）| `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cardioid Antenna`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风单元的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风单元在此向量的最小和最大元素所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在 **Operating frequency vector (Hz)** 参数所定义的频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数来指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数来指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

指定计算天线辐射方向图时所使用的方位角，指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须位于 –180° 到 180° 之间（含边界值），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

指定计算辐射方向图时所使用的仰角，指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须位于 –90° 到 90° 之间（含边界值），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

指定天线辐射方向图时所使用的点的 Phi 角，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须位于 0° 到 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图时所使用的点的 Theta 角，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须位于 0° 到 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值为 *Q*×*P*×*L* 数组，则数组的每一 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值为 *Q*×*P*×*L* 数组，则数组的每一 *Q*×*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Align element normal with array normal** — 将阵元法线与阵列法线对齐 on（默认）| off

#### 依赖关系

当 **Element type** 设置为 `Custom Antenna` 时，此参数启用。

### **Radiation pattern beamwidth (deg)** — 辐射方向图波束宽度 `[10,10]`（默认）

#### 依赖关系

当 **Element type** 设置为 `Gaussian Antenna` 时，此参数启用。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量所指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

将极坐标方向图响应角度指定为 1×*P* 向量。角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含边界值）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极性响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元极性响应的幅度指定为 *L*×*P* 矩阵。*L* 是在 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是在 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极性响应幅度。该响应在方位角平面中测量。在方位角平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极性响应围绕中心轴对称。您可以根据极性响应构建三维空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数量，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列具有相同的行数和列数。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列阵元沿最左列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值为 `[3,2]` 会创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element spacing (m)** — 阵列阵元之间的间距 ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为 2 元素正数值向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 正数值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在本地阵列坐标系中沿此轴均匀间隔分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Element lattice** — URA 阵元位置的晶格 `Rectangular`（默认）| `Triangular`

URA 阵元位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元沿行和列方向对齐。
- `Triangular` — 将矩形晶格的偶数行阵元向行轴正方向偏移。位移为沿行维度阵元间距的一半。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向 URA 阵列为 `x` 或 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向指向阵列法线方向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量均指向 *x* 轴方向。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量均指向 *y* 轴方向。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量均指向 *z* 轴方向。 |

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中阵元的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的阵元数。该矩阵的每一列表示阵列局部坐标系中一个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列阵元法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的阵元数。对于矩阵，每一列以 `[azimuth;elevation]` 的形式指定相应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值为 2×1 列向量，则所有阵列阵元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示阵元对之间通过某些变换产生差异的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法线方向旋转的变换。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵元锥削 1（默认）| 复值标量 | 复值行向量

阵元锥削，指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数量。

也称为*阵元权重*，锥削对阵列阵元响应进行加权。锥削修改响应的幅度和相位，以降低旁瓣或调整主响应轴方向。

如果 **Taper** 为标量，则对每个阵元施加相同的权重。如果 **Taper** 为向量，则将向量中的权重施加到对应的传感器阵元。权重数量必须与阵列的阵元数量匹配。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

### **Subarray definition matrix** — 定义属于子阵的阵元 逻辑矩阵

将子阵选择指定为 *M*×*N* 矩阵。*M* 是子阵的数量，*N* 是阵列中阵元的总数。矩阵的每一行代表一个子阵，行中的每个条目指示阵元何时属于该子阵。当条目为零时，该阵元不属于该子阵。非零条目表示施加到对应阵元的复值权重。每一行必须至少包含一个非零条目。

每个子阵的相位中心位于子阵几何中心。子阵几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵导向方法 `None`（默认）| `Phase` | `Time`

子阵导向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 将在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `Steer` 输入端口。

选择 `Custom` 将在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵移相频率 `3.0e8`（默认）| 正实值标量

子阵导向移相器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵导向移相量化位数 `0`（默认）| 非负整数

子阵导向移相量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认）| `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认值）

矩形子阵网格大小，指定为正整数或由正整数组成的 1×2 行向量。

如果 **Grid size** 为整数标量，则阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 为形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个元素是沿每一列的子阵数量。第二个元素是每一行中的子阵数量。行沿局部 *y* 轴方向，列沿局部 *z* 轴方向。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 来复制一个 3×2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认值） | 正实值标量 | 由正实值组成的 1×2 向量

子阵的矩形网格间距，指定为正实值标量、由正实值组成的 1×2 行向量或 `Auto`。单位为米。

- 如果 **Grid spacing** 为标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 为 1×2 行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个元素指定沿列方向各行之间的间距。第二个元素指定沿行方向各列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则复制在构建完整阵列时会为行和列保留子阵的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵的位置 `[0,0;0.5,0.5;0,0]`（默认值） | 3×*N* 实值矩阵

自定义网格中子阵的位置，指定为实 3×*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标以 `[x; y; z]` 的形式表示。单位为米。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量的方向 `[0,0;0,0]`（默认值） | 2×*N* 实矩阵

指定阵列中子阵的法向方向。此参数值为 2×*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列以 `[azimuth;elevation]` 的形式指定对应子阵的法向方向。角度单位为度。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示子阵对之间通过某些变换而不同的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

### **Analyze** — 启动 Sensor Array Analyzer（默认）

点击 **Analyze** 按钮将启动 Sensor Array Analyzer 应用。该应用允许您检查重要的阵列属性，例如阵列响应和阵列几何结构。
## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

窄带发射阵列

Narrowband Transmit Array 模块通过将每个阵元的远场辐射信号相加，在阵列远场中生成窄带平面波。可将模块输出视为距阵元或阵列中心某一参考距离处的场。
