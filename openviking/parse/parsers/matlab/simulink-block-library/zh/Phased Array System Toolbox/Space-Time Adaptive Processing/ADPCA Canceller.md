---
type: simulink-block
title: 'ADPCA Canceller'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'adpcacanceller'
documentation_source_path: 'ref/adpcacanceller.html'
language: zh-CN
chinese_source: worker-translation
---

# ADPCA Canceller

## 端口
```yaml
ports:
- name: X
  summary: 输入信号 *M*×*N*×*P* 复值矩阵
  direction: input
  data_types: double
- name: Idx
  summary: 距离单元索引 正整数
  direction: input
  data_types: double
- name: PRF
  summary: 脉冲重复频率 正标量
  direction: input
  data_types: double
- name: Ang
  summary: 目标方向 2×1 实值向量
  direction: input
  data_types: double
- name: Dop
  summary: 目标多普勒频率 标量
  direction: input
  data_types: double
- name: Y
  summary: 波束形成输出 *M*×1 复值向量
  direction: output
  data_types: double
- name: W
  summary: 处理权值 长度 *N*\P* 复值向量
  direction: output
  data_types: double
```

### 输入

### **X** — 输入信号 *M*×*N*×*P* 复值矩阵

输入信号，指定为
*M*×*N*×*P*
复值数组。*M* 为距离
采样数，*N* 为通道数，*P* 为脉冲数。

输入矩阵第一维的大小可以变化，以
模拟变化的信号长度。例如，在脉冲
波形具有可变脉冲重复频率的情况下，大小可能会发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Idx** — 距离单元索引 正整数

用于计算处理权值的距离单元索引。

**示例：** `1`

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，指定为正
标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as**
参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 目标方向 `2`×`1` 实值向量

目标方向，指定为
`2`×*1* 实值向量。该
向量采用
`[AzimuthAngle;ElevationAngle]` 的形式。角度单位为
度。方位角必须介于 –180° 和 180° 之间（含边界值），
俯仰角必须介于 –90° 和 90° 之间（含边界值）。角度
是相对于阵列的局部坐标系
定义的。

#### 依赖关系

要启用此端口，请将 **Specify direction
as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Dop** — 目标多普勒频率 标量

当前脉冲的目标多普勒频率，指定为
标量。

#### 依赖关系

当 **Output pre-Doppler
result** 复选框清除且 **Specify
targeting Doppler as** 参数设置为
`Input port` 时，此端口出现。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*×1 复值向量

处理输出，返回为
*M*×*1* 复值向量。
*M* 为输入端口 `X` 中的距离
采样数。

**数据类型：** `double`
**复数支持：** 是

### **W** — 处理权值 长度 *N*\**P* 复值向量

处理权值，返回为长度
*N*\**P* 复值向量。
*N* 为通道数，*P* 为脉冲数。当
**Specify sensor array as** 参数设置为
`Partitioned array` 或 `Replicated
subarray` 时，*N* 表示子阵
数量。*L* 为在 `Ang` 输入端口或通过
**Beamforming direction (deg)** 参数指定的期望波束形成
方向数。每个波束形成方向对应一组
权值。

#### 依赖关系

要启用此端口，请选中 **Enable weights
output** 复选框。

**数据类型：** `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认值）| 实值正标量
  group: ''
- name: Operating frequency (Hz)
  summary: 系统工作频率 3e8（默认值）| 正实标量
  group: ''
- name: Specify PRF as
  summary: PRF 值来源 Property（默认值）| Input port
  group: ''
- name: Pulse repetition frequency (Hz)
  summary: 脉冲重复频率 1（默认值）| 正标量
  group: ''
- name: Specify direction as
  summary: 指定目标方向来源 Property（默认）| Input port
  group: ''
- name: Receiving mainlobe direction (deg)
  summary: 阵列主瓣的指向方向 [0;0]（默认）| 实值 2×1 向量
  group: ''
- name: Number of bits in phase shifters
  summary: 移相器量化位数 0（默认）| 非负整数
  group: ''
- name: Specify targeting Doppler as
  summary: 目标多普勒来源 Property（默认）| Input port
  group: ''
- name: Targeting Doppler (Hz)
  summary: STAP 处理器的目标多普勒 0（默认）| 标量
  group: ''
- name: Number of guard cells
  summary: 用于训练的保护单元数 2（默认）| 正偶整数
  group: ''
- name: Number of training cells
  summary: 用于训练的单元数 2（默认）| 正偶整数
  group: ''
- name: Enable weights output
  summary: 输出波束形成器权重的选项 off（默认）| on
  group: ''
- name: Output pre-Doppler result
  summary: 多普勒滤波前的输出结果 on（默认）| off
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
- name: Specify sensor array as
  summary: 指定阵列的方法 Array (no subarrays)（默认）| MATLAB expression
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
- name: Operating frequency vector (Hz)
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
  summary: 将天线阵元旋转到阵列法向 on（默认）| off
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
- name: Specify sensor array as
  summary: 阵列类型 Array (no subarrays)（默认）| MATLAB expression
  group: 阵列参数
  type: ''
- name: Number of elements
  summary: U 中的阵列阵元数量 2（默认）| 大于或等于二的整数
  group: 阵列参数
- name: Element spacing
  summary: ULA 阵元之间的间距 0.5（默认）| 正标量
  group: 阵列参数
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: 阵列参数
- name: Taper
  summary: ULA 阵列锥削 1（默认）| 复值向量
  group: 阵列参数
- name: Expression
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox 阵列 System object
  group: 阵列参数
```

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认值）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认
值为
`physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认值）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Specify PRF as** — PRF 值来源 `Property`（默认值）| `Input port`

PRF 值来源，指定为 `Property` 或
`Input port`。当设置为
`Property` 时，**Pulse repetition frequency
(Hz)** 参数设置 PRF。当设置为 `Input
port` 时，通过 `PRF` 输入
端口传入 PRF。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1`（默认值）| 正标量

脉冲重复频率 PRF，指定为正标量。单位为赫兹。
将此参数设置为仿真中使用的任何 `Waveform` 库
模块所设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为
`Property`。

### **Specify direction as** — 指定目标方向来源 `Property`（默认）| `Input port`

指定 STAP 处理器模块的目标方向来自模块参数还是来自 `ANG` 输入端口。此参数的值为

|  |  |
| --- | --- |
| `Property` | - 对于 ADPCA Canceller 和 DPCA Canceller 模块，目标方向使用 **Receiving mainlobe direction (deg)** 指定。 - 对于 SMI Beamformer 模块，目标方向使用 **Targeting direction** 指定。 这些参数仅在 **Specify direction as** 参数设置为 `Property` 时显示。 |
| `Input port` | 使用 `Ang` 输入端口输入目标方向。此端口仅在 **Specify direction as** 设置为 `Input port` 时显示。 |

### **Receiving mainlobe direction (deg)** — 阵列主瓣的指向方向 `[0;0]`（默认）| 实值 2×1 向量

将接收传感器阵列主瓣的方向指定为实值 2×1 向量。方向以
`[AzimuthAngle; ElevationAngle]` 的格式指定。方位角
应介于 –180° 和 180° 之间，仰角应介于
–90° 和 90° 之间。

**示例：** `[100;-45]`

#### 依赖关系

要启用此参数，请将 **Specify direction
as** 设置为 `Property`。

### **Number of bits in phase shifters** — 移相器量化位数 `0`（默认）| 非负整数

用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为
零表示不执行量化。

### **Specify targeting Doppler as** — 目标多普勒来源 `Property`（默认）| `Input port`

指定 STAP 处理器的目标多普勒值来自此模块的
**Targeting Doppler (Hz)** 参数还是使用
`DOP` 输入端口。对于 ADPCA Canceller 和
DPCA Canceller 模块，**Specify targeting Doppler
as** 参数仅在 **Output pre-Doppler
result** 复选框清除时显示。此参数的值为

|  |  |
| --- | --- |
| `Property` | 使用模块的 **Targeting Doppler** 参数指定目标多普勒值。**Targeting Doppler** 参数仅在 **Specify targeting Doppler as** 设置为 `Property` 时显示。 |
| `Input port` | 使用 `Dop` 输入端口指定目标多普勒值。此端口仅在 **Specify targeting Doppler as** 设置为 `Input port` 时显示。 |

### **Targeting Doppler (Hz)** — STAP 处理器的目标多普勒 `0`（默认）| 标量

STAP 处理器的目标多普勒，指定为标量。

#### 依赖关系

- 要为 SMI Beamformer 模块启用此参数，
  请将 **Specify targeting Doppler as** 设置为
  `Property`。
- 要为 ADPCA Canceller 和
  DPCA Canceller 模块启用此参数，请先清除
  **Output pre-Doppler result** 复选框。然后
  将 **Specify targeting Doppler as** 参数设置为
  `Property`。

### **Number of guard cells** — 用于训练的保护单元数 `2`（默认）| 正偶整数

用于训练的保护单元数，指定为正偶整数。
在可能的情况下，保护单元集会被等分为测试单元之前和
之后的区域。

### **Number of training cells** — 用于训练的单元数 `2`（默认）| 正偶整数

用于训练的单元数，指定为正偶整数。在可能的情况下，
训练单元集会被等分为测试单元之前和
之后的区域。

### **Enable weights output** — 输出波束形成器权重的选项 off（默认）| on

选中此复选框可从输出端口
`W` 获取波束形成器权重。

### **Output pre-Doppler result** — 多普勒滤波前的输出结果 on（默认）| off

选中此复选框可输出多普勒滤波前的结果。清除此复选框可输出多普勒滤波后的处理结果。选中此复选框将移除 **Specify targeting Doppler as** 和 **Targeting Doppler (Hz)** 参数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

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

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
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

将天线或麦克风单元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该单元在此频率范围之外无响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风元件的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为一个 1×*L* 的递增实值行向量。天线或麦克风元件在该向量最小值和最大值所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的背面响应设置为零 off（默认）| on

选中此复选框可对元件的背面响应进行障板处理。进行背面障板处理后，所有偏离视轴超过 ±90° 的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当您将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在 **Operating frequency vector (Hz)** 参数所定义频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

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

### **MatchArrayNormal** — 将天线阵元旋转到阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵元方向图旋转至与阵列法向对齐。未选中时，阵元方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴指向阵列法向。未选中时使用不旋转的阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风中心拾取轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是在 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是在 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### 阵列参数

### **Specify sensor array as** — 阵列类型 `Array (no subarrays)`（默认）| `MATLAB expression`

直接指定 ULA 传感器阵列，或使用 MATLAB 表达式指定。

**类型**

|  |
| --- |
| `Array (no subarrays)` |
| `MATLAB expression` |

### **Number of elements** — U 中的阵列阵元数量 `2`（默认）| 大于或等于二的整数

ULA 阵列的阵列阵元数量，指定为大于或等于二的整数。

**示例：** `11`

**数据类型：** `double`

### **Element spacing** — ULA 阵元之间的间距 `0.5`（默认）| 正标量

相邻 ULA 阵元之间的间距，指定为正标量。单位为米。

**示例：** `1.5`

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀分布。

#### 依赖

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Taper** — ULA 阵列锥削 `1`（默认）| 复值向量

锥削，也称为*阵元权重*，应用于阵列中的传感器阵元。锥削用于修改发射或接收数据的幅度和相位。

将阵元锥削指定为复值标量或复值 1×*N* 行向量。在该向量中，*N* 表示阵列中的阵元数量。如果 **Taper** 为标量，则对每个阵元应用相同的权重。如果 **Taper** 为向量，则将向量中的权重应用于对应的传感器阵元。必须对传感器阵列中的每个阵元应用权重。

**示例：** [0.5;1;0.5]

**数据类型：** `double`
**复数支持：** 是

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox 阵列 System object

用于创建 ULA 阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.ULA('NumElements',13)`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。
## 所属库

Phased Array System Toolbox / Space-Time Adaptive Processing

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

均匀线性阵列的自适应位移相位中心阵列（ADPCA）脉冲对消器

ADPCA Canceller 模块使用位移相位中心阵列脉冲对消器对入射到均匀线性阵列上的杂波进行滤波。
