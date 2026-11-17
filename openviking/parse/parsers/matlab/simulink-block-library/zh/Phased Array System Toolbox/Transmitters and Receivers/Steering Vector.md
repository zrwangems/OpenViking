---
type: simulink-block
title: 'Steering Vector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'steeringvector'
documentation_source_path: 'ref/steeringvector.html'
language: zh-CN
chinese_source: worker-translation
---

# Steering Vector

## 端口
```yaml
ports:
- name: Freq
  summary: 阵列工作频率，正标量
  direction: input
  data_types: double
- name: Ang
  summary: 导向矢量方向 [0;0]（默认）| 实值长度-*M* 向量 | 实值 2×*M* 矩阵
  direction: input
  data_types: double
- name: SV
  summary: 导向矢量，复值 *N*×*M*×*L* 数组 | struct
  direction: output
  data_types: double
```

### 输入

### **Freq** — 阵列工作频率，正标量

阵列工作频率，指定为正标量。单位为 Hz。

#### 依赖

要启用此端口，请将 **Source of operating frequency** 参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 导向矢量方向 `[0;0]`（默认）| 实值长度-*M* 向量 | 实值 2×*M* 矩阵

导向矢量方向，指定为实值长度-*M* 向量或实值 2×*M* 矩阵。*M* 是导向方向的数量。

- 当 `Ang` 是 2×*M* 矩阵时，矩阵的每一列以 `[azimuth;elevation]` 的形式指定空间中的导向方向。方位角必须在 –180° 到 180° 之间，俯仰角必须在 –90° 到 90° 之间。
- 当 `Ang` 是长度-*M* 向量时，其值对应于导向矢量方向的方位角，俯仰角设置为零。

角度单位为度。

**数据类型：** `double`
### 输出

### **SV** — 导向矢量，复值 *N*×*M*×*L* 数组 | struct

导向矢量，输出为复值 *N*×*M*×*L* 数组或包含数组的 `struct`。*N* 是相控阵的元素数量。如果阵列包含子阵，*N* 是子阵的数量。*M* 是在 `Ang` 参数中指定的导向方向数量。*L* 是在 `Freq` 参数中指定的频率数量。

**数据类型：** `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 实值正标量
  group: ''
- name: Source of operating frequency
  summary: 工作频率来源 Input port（默认）| Property
  group: ''
  block_parameter: FrequencySource
  type: char | string
  values: Input port | Property
- name: Operating frequency (Hz)
  summary: 系统工作频率 3e8（默认）| 正实标量
  group: ''
  block_parameter: OperatingFrequency
  type: double | single
  values: float
- name: Output conjugated steering vector
  summary: 输出共轭导向矢量 on（默认）| off
  group: ''
  block_parameter: OutputConjugate
  type: check box
  values: 0 | 1
- name: Number of bits in phase shifters
  summary: 移相器相位量化位数 0（默认）| 非负整数
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
- name: Specify sensor array as
  summary: 指定阵列的方法 Array (no subarrays)（默认）| MATLAB expression
  group: ''
- name: Element type
  summary: 阵列单元类型 Isotropic Antenna（默认）| Cardioid Antenna | Cosine Antenna | Custom Antenna | Gaussian Antenna | Sinc Antenna
    | Omni Microphone | Custom Microphone
  group: ''
- name: Operating frequency range (Hz)
  summary: 天线或麦克风单元的工作频率范围 [0,1e20]（默认）| 实值 1×2 行向量
  group: ''
- name: Baffle the back of the element
  summary: 将 Isotropic Antenna 元件或 Omni Microphone 元件的后向响应设置为零 off（默认）| on
  group: ''
- name: Null axis direction
  summary: 零点轴方向 -x（默认）| +x | +y | -y | +z | -z
  group: ''
- name: Exponent of cosine pattern
  summary: 方位角和仰角余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实数值 1×2 矩阵
  group: ''
- name: Operating frequency vector (Hz)
  summary: 自定义天线或麦克风元件的工作频率范围 [0,1e20]（默认）| 实数值行向量
  group: ''
- name: Frequency responses (dB)
  summary: 天线和麦克风频率响应 [0,0]（默认）| 实数值行向量
  group: ''
- name: Input Pattern Coordinate System
  summary: 自定义天线方向图的坐标系 az-el（默认）| phi-theta
  group: ''
- name: Azimuth angles (deg)
  summary: 天线辐射方向图的方位角 [-180:180]（默认）| 实数值行向量
  group: ''
- name: Elevation angles (deg)
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实值行向量
  group: ''
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角坐标 0:360 | 实值 1×*P* 行向量
  group: ''
- name: Theta Angles (deg)
  summary: 自定义天线辐射方向图的 Theta 角坐标 0:180 | 实值 1×*Q* 行向量
  group: ''
- name: Magnitude pattern (dB)
  summary: 组合天线辐射方向图的幅度 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: 相位方向图 (deg)
  summary: 自定义天线辐射相位方向图 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: ''
- name: 将元件法线对齐到阵列法线
  summary: 将元件法线对齐到阵列法线 开（默认）| 关
  group: ''
- name: 辐射方向图波束宽度 (deg)
  summary: 辐射方向图波束宽度 [10,10]（默认）
  group: ''
- name: 极坐标方向图频率 (Hz)
  summary: 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量
  group: ''
- name: 极坐标方向图角度 (deg)
  summary: 极坐标方向图响应角度 [-180:180]（默认）| 实值 1×*P* 行向量
  group: ''
- name: 极坐标方向图 (dB)
  summary: 自定义麦克风极坐标响应 zeros(1,361)（默认）| 实值 *L*×*P* 矩阵
  group: ''
- name: 几何结构
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: ''
- name: Number of elements
  summary: ULA 阵列的阵元数为 2，UCA 阵列的阵元数为 5（默认）| 大于或等于 2 的整数
  group: ''
- name: Element spacing (m)
  summary: 阵元间距，ULA 阵列为 0.5，URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为由正值组成的 2 元素向量
  group: ''
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: ''
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 由正整数组成的 1×2 向量
  group: ''
- name: Element lattice
  summary: URA 阵元位置的晶格 Rectangular（默认）| Triangular
  group: ''
- name: Array normal
  summary: 阵列法线方向，URA 阵列为 x，UCA 阵列为 z（默认）| y
  group: ''
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: ''
- name: Element positions (m)
  summary: 共形阵列元素的位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: ''
- name: Element normals (deg)
  summary: 共形阵列元素法向量的方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: ''
- name: Taper
  summary: 阵列元素加权 1（默认）| 复标量 | 复值行向量
  group: ''
```

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Source of operating frequency** — 工作频率来源 `Input port`（默认）| `Property`

工作频率来源，指定为 `Input Port` 或 `Property`。当此参数设置为 `Input Port` 时，工作频率使用 `Freq` 输入端口设置。当此参数设置为 `Property` 时，工作频率使用 `Operating frequency (Hz)` 参数设置。

#### 编程使用

|  |
| --- |
| **模块参数：**`FrequencySource` |
| **类型：**char | string |
| **值：**`Input port` | Property |
| **默认：**Input port |

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

#### 依赖

要启用此参数，请将 `Source of operating frequency` 参数设置为 `Property`。

#### 编程使用

|  |
| --- |
| **模块参数：**`OperatingFrequency` |
| **类型：**double | single |
| **值：**float |
| **默认：**`0` |

### **Output conjugated steering vector** — 输出共轭导向矢量 on（默认）| off

选中此复选框以输出共轭导向矢量。否则，导向矢量不进行共轭。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputConjugate` |
| **类型：**check box |
| **值：**0 | 1 |
| **默认：**`0` |

### **Number of bits in phase shifters** — 移相器相位量化位数 `0`（默认）| 非负整数

用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

#### Sensor Array Tab

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

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

#### Element Parameters

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

要启用此参数，请将 **Element type** 设置为
`Isotropic Antenna`、`Cosine Antenna` 或
`Omni Microphone`。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的后向响应设置为零 off（默认）| on

选中此复选框以遮挡元件的后向响应。当后向遮挡时，
从正侧向起超过 ±90° 的所有方位角处的响应
均设置为零。正侧向方向
定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将
**Element type** 设置为
`Isotropic Antenna` 或
`Omni Microphone`。

### **Null axis direction** — 零点轴方向 `-x`（默认）| `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cardioid Antenna`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或
非负实数值 1×2 矩阵。当
**Exponent of cosine pattern** 为
1×2 向量时，第一个元素是方位角
方向的指数，第二个元素是
仰角方向的指数。当您将此参数设置为标量时，
方位角方向和仰角方向的余弦
方向图均被提升到相同的幂次。

#### 依赖关系

要启用此参数，请将 **Element
type** 设置为 `Cosine
Antenna`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风元件的工作频率范围 `[0,1e20]`（默认）| 实数值行向量

将天线和麦克风频率响应设置为
1×*L* 行向量，其中元素为递增的实数值。天线或
麦克风元件在此向量的最小值和最大值元素所指定的频率范围之外
没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。使用
**Frequency responses (dB)** 设置这些
频率处的响应。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实数值行向量

自定义天线或自定义
麦克风在 **Operating frequency vector
(Hz)** 参数所定义的频率处的频率响应。
**Frequency responses (dB)** 的维度必须
与 **Operating frequency vector
(Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将
**Element type** 设置为
`Custom Antenna` 或 `Custom
Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为
`az-el` 或 `phi-theta`。当您
指定 `az-el` 时，使用 **Azimuth angles
(deg)** 和 **Elevations angles (deg)** 参数来
指定方向图点的坐标。当您指定
`phi-theta` 时，使用 **Phi angles (deg)**
和 **Theta angles (deg)** 参数来指定
方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实数值行向量

将计算天线辐射方向图的方位角指定为
1×*P* 行向量。*P* 必须
大于 2。方位角必须介于 –180° 和 180° 之间
（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

指定用于计算辐射方向图的仰角，指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

指定用于指定天线辐射方向图的点的 Phi 角，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

指定用于指定天线辐射方向图的点的 Theta 角，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **相位方向图 (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于由 **仰角 (deg)** 参数指定的向量长度，*P* 等于由 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于由 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **工作频率向量 (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna`。

### **将元件法线对齐到阵列法线** — 将元件法线对齐到阵列法线 开（默认）| 关

#### 依赖关系

当 **元件类型** 设置为 `Custom Antenna` 时，此参数启用。

### **辐射方向图波束宽度 (deg)** — 辐射方向图波束宽度 `[10,10]`（默认）

#### 依赖关系

当 **元件类型** 设置为 `Gaussian Antenna` 时，此参数启用。

### **极坐标方向图频率 (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **工作频率向量 (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

### **极坐标方向图角度 (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风中心拾取轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

### **极坐标方向图 (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风元件极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **极坐标方向图频率 (Hz)** 中指定的频率数量。*P* 是 **极坐标方向图角度 (deg)** 中指定的角度数量。矩阵的每一行表示在 **极坐标方向图频率 (Hz)** 中指定的对应频率以及 **极坐标方向图角度 (deg)** 中指定的所有角度处测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

#### 阵列参数

### **几何结构** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意元件位置

### **Number of elements** — ULA 阵列的阵元数为 `2`，UCA 阵列的阵元数为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵元数，指定为大于或等于 2 的整数。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `UCA`。

### **Element spacing (m)** — 阵元间距，ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为由正值组成的 2 元素向量

相邻阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或由正值组成的 1×2 向量。如果 **Element spacing (m)** 为标量，
  则行间距和列间距相等。如果 **Element spacing
  (m)** 为向量，则该向量的形式为
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、
`x` 或 `z`。所有 ULA 阵列
阵元在局部阵列坐标系中沿此轴均匀分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为
  `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 由正整数组成的 1×2 向量

URA 阵列的维度，指定为正整数或由
正整数组成的 1×2 向量。

- 如果 **Array size** 为 1×2 向量，则该向量的形式为
  `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 为整数，则该阵列每一行和每一列中的
  阵元数相同。

对于 URA，阵元从最左侧阵列列沿自上而下的方向进行索引，然后从左到右继续到下一列。在此
图中，**Array size** 值为 `[3,2]` 会创建一个
具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 阵元位置的晶格 `Rectangular`（默认）| `Triangular`

URA 阵元位置的晶格，指定为 `Rectangular`
或 `Triangular`。

- `Rectangular` — 将所有阵元在
  行和列方向上对齐。
- `Triangular` — 将矩形晶格的偶数行
  阵元向正行轴方向偏移。
  位移为沿行维度阵元间距的
  一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Array normal** — 阵列法线方向，URA 阵列为 `x`，UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为
`x`、
`y` 或
`z`。

平面阵列的阵元位于与所选阵列法线方向正交的
平面内。阵元视轴
方向指向阵列法线
方向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量均指向 *x* 轴。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量均指向 *y* 轴。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量均指向 *z* 轴。 |

#### 依赖关系

要启用此参数，请将
**Geometry** 设置为
`URA` 或
`UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中元素的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的元素数量。该矩阵的每一列表示阵列局部坐标系中一个阵列元素的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列元素法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中元素法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的元素数量。如果参数值为矩阵，则每一列以 `[azimuth;elevation]` 的形式指定对应元素相对于局部坐标系的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列元素使用相同的指向方向。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示元素对之间通过某些变换产生差异的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列元素加权 1（默认）| 复标量 | 复值行向量

将元素加权指定为复标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的元素数量。

也称为*元素权重*，加权会乘以阵列元素响应。加权会修改响应的幅度和相位，以减少旁瓣或调整主响应轴的指向。

如果 **Taper** 为标量，则对每个元素应用相同的权重。如果 **Taper** 为向量，则将向量中的权重应用于对应的传感器元素。权重数量必须与阵列的元素数量匹配。

**数据类型：** `double`
## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

阵列导向矢量

计算给定方向和频率下的阵列导向矢量。
