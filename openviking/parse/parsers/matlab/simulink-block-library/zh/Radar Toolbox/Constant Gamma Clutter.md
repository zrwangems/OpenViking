---
type: simulink-block
title: 'Constant Gamma Clutter'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'constantgammaclutter'
documentation_source_path: 'ref/constantgammaclutter.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Gamma Clutter

## 端口
```yaml
ports:
- name: PRFIdx
  summary: PRF 索引 正整数
  direction: input
  data_types: double
- name: W
  summary: 阵元权重 长度为 *N* 的复值向量
  direction: input
  data_types: double
- name: WS
  summary: 子阵元权重 *N*E×*N*S 复值矩阵
  direction: input
  data_types: double
- name: Steer
  summary: 导向角输入 标量 | 2×1 实值向量
  direction: input
  data_types: double
- name: Out
  summary: 模拟杂波 *N*×*M* 复值矩阵
  direction: output
  data_types: double
```

### 输入

### **PRFIdx** — PRF 索引 正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从**脉冲重复频率 (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例：**
`4`

#### 依赖关系

要启用此端口，请选择**启用 PRF 选择输入**。

**数据类型：** `double`

### **W** — 阵元权重 长度为 *N* 的复值向量

应用于阵列中每个阵元的权重，指定为长度为 *N* 的复值向量。
*N* 是在**传感器阵列**面板中选择的阵列中的阵元数量。

#### 依赖关系

要启用此端口，请选中**启用权重输入**复选框。

**数据类型：** `double`
**支持复数：** 是

### **WS** — 子阵元权重 *N*E×*N*S 复值矩阵

应用于子阵中每个阵元的权重，指定为
*N*E×*N*S
复值矩阵。

- 当您将**指定传感器阵列**设置为
  `Replicated Subarray` 时，所有
  子阵具有相同的维度。然后，您可以将
  子阵元权重指定为复值
  *N*E×*N*S
  矩阵。*NE* 是
  每个子阵中的阵元数量，
  *N*S 是
  子阵的数量。`WS` 的每一列
  指定对应子阵的权重。
- 当您将**指定传感器阵列**设置为
  `Partitioned array` 时，子阵
  不需要具有相同的维度和大小。您
  可以将子阵元权重指定为复值
  *N*E×*N*S
  矩阵，其中 *N*E
  现在是最大子阵中的阵元数量。每列中的
  前 *K* 个条目是对应子阵的
  阵元权重，其中
  *K* 是该子阵中的阵元数量。

#### 依赖关系

要启用此端口，请将**指定传感器阵列**
设置为 `Partitioned array` 或
`Replicated Subarray`。然后，将
**子阵导向方法**设置为
`Custom`。

**数据类型：** `double`
**支持复数：** 是

### **Steer** — 导向角输入 标量 | 2×1 实值向量

导向角，指定为标量或 2×1 实值向量。
作为向量时，导向角的形式为
`[AzimuthAngle; ElevationAngle]`。作为标量时，导向角
仅表示方位角。此时仰角
假定为零度。单位为度。

#### 依赖关系

要启用此端口，请将**指定传感器阵列**
设置为 `Partitioned array` 或
`Replicated Subarray`。然后，将
**子阵导向方法**设置为
`Phase` 或
`Time`。

**数据类型：** `double`
### 输出

### **Out** — 模拟杂波 *N*×*M* 复值矩阵

模拟杂波，返回为
*N*×*M* 复值
矩阵。

*N* 是模块输出的样本数。
当您将**输出信号格式**参数设置为
`Samples` 时，使用**输出中的样本数**参数
指定 *N*。
当您将**输出信号格式**参数设置为
`Pulses` 时，*N* 是接下来 *P* 个脉冲中的总
样本数，其中
*P* 在**输出中的脉冲数**
参数中指定。

*M* 为以下之一：

- 如果传感器
  阵列包含子阵，则为传感器阵列中的子阵数量。
- 如果传感器阵列不包含子阵，则为辐射或收集阵元的
  数量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Terrain gamma value (dB)
  summary: 杂波模型参数 0（默认）| 标量
  group: 主选项卡
- name: Earth model
  summary: 地球形状 Flat（默认）| Curved
  group: 主选项卡
- name: Minimum range of clutter region (m)
  summary: 杂波区域最小距离 0 | 非负标量
  group: 主选项卡
- name: Maximum range of clutter region (m)
  summary: 杂波区域最大距离 5000 | 非负标量
  group: 主选项卡
- name: Azimuth center of clutter region (deg)
  summary: 杂波区域方位中心 0 | 标量
  group: 主选项卡
- name: Azimuth span of clutter region (deg)
  summary: 杂波区域方位跨度 60（默认）| 正标量
  group: 主选项卡
- name: Azimuth span of clutter patches (deg)
  summary: 杂波块方位跨度 1（默认）| 正标量
  group: 主选项卡
- name: Clutter coherence time (s)
  summary: 杂波仿真的相干时间 Inf（默认）| 正标量
  group: 主选项卡
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 实值正标量
  group: 主选项卡
- name: Sample rate (Hz)
  summary: 杂波采样率 1e6（默认）| 正标量
  group: 主选项卡
- name: Pulse repetition frequency (Hz)
  summary: 脉冲重复频率 1e4（默认）| 正标量 | 正数值行向量
  group: 主选项卡
- name: Enable PRF selection input
  summary: 选择预定义 PRF off（默认）| on
  group: 主选项卡
- name: Source of simulation sample time
  summary: 仿真采样时间来源 Derive from waveform parameters（默认）| Inherit from Simulink engine
  group: 主选项卡
- name: Output signal format
  summary: 输出信号 Pulses（默认）| Samples 的格式
  group: 主选项卡
- name: Number of samples in output
  summary: 输出中的样本数 100（默认）| 正整数
  group: 主选项卡
- name: Number of pulses in output
  summary: 输出中的脉冲数 1（默认）| 正整数
  group: 主选项卡
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: 主选项卡
- name: Operating frequency (Hz)
  summary: 系统工作频率 3.0e8（默认）| 正实数标量
  group: 主选项卡
- name: Effective transmitted power (W)
  summary: 雷达系统有效发射功率 5000（默认）| 正标量
  group: 主选项卡
- name: Radar height (m)
  summary: 雷达离地面高度 0（默认）| 非负标量
  group: 主选项卡
- name: Radar speed (m/s)
  summary: 雷达平台速度 0（默认）| 非负标量
  group: 主选项卡
- name: Radar motion direction (deg)
  summary: 雷达平台运动方向 [90;0]（默认）| 2×1 实向量
  group: 主选项卡
- name: Sensor mounting angles sensor (deg)
  summary: 传感器安装角度 [0 0 0]（默认）| 长度为 3 的正值向量
  group: 主选项卡
- name: Enable weights input
  summary: 启用天线阵元权重输入端口 未选中（默认）| 选中
  group: 主选项卡
- name: Specify sensor array as
  summary: 指定阵列的方法 Array (no subarrays)（默认）| Partitioned array | Replicated subarray | MATLAB expression
  group: Sensor Array Tab
- name: Expression
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object
  group: Sensor Array Tab
- name: Element type
  summary: 阵元类型 Isotropic Antenna（默认）| Cosine Antenna | Custom Antenna | Omni Microphone | Custom Microphone
  group: Sensor Array Tab
- name: Operating frequency range (Hz)
  summary: 天线或麦克风阵元的工作频率范围 [0,1.0e20]（默认）| 实值 1×2 行向量
  group: Sensor Array Tab
- name: Operating frequency vector (Hz)
  summary: 自定义天线或麦克风阵元的工作频率范围 [0,1.0e20]（默认）| 实值行向量
  group: Sensor Array Tab
- name: Baffle the back of the element
  summary: 将 Isotropic Antenna 元件或 Omni Microphone 元件的后向响应设置为零 off（默认）| on
  group: Sensor Array Tab
- name: Exponent of cosine pattern
  summary: 方位角和仰角余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实数值 1×2 矩阵
  group: Sensor Array Tab
- name: Frequency responses (dB)
  summary: 天线和麦克风频率响应 [0,0]（默认）| 实数值行向量
  group: Sensor Array Tab
- name: Input Pattern Coordinate System
  summary: 自定义天线方向图的坐标系 az-el（默认）| phi-theta
  group: Sensor Array Tab
- name: Azimuth angles (deg)
  summary: 天线辐射方向图的方位角 [-180:180]（默认）| 实数值行向量
  group: Sensor Array Tab
- name: Elevation angles (deg)
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实数值行向量
  group: Sensor Array Tab
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角坐标 0:360 | 实数值 1×*P* 行向量
  group: Sensor Array Tab
- name: Theta Angles (deg)
  summary: 自定义天线辐射方向图的 Theta 角度坐标 0:180 | 实值 1×*Q* 行向量
  group: Sensor Array Tab
- name: Magnitude pattern (dB)
  summary: 组合天线辐射方向图的幅度 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: Sensor Array Tab
- name: Phase pattern (deg)
  summary: 自定义天线辐射相位方向图 zeros(181,361)（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组
  group: Sensor Array Tab
- name: MatchArrayNormal
  summary: 将天线阵子旋转至阵列法向 on（默认）| off
  group: Sensor Array Tab
- name: Polar pattern frequencies (Hz)
  summary: 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量
  group: Sensor Array Tab
- name: Polar pattern angles (deg)
  summary: 极坐标方向图响应角度 [-180:180]（默认）| 实值 1×*P* 行向量
  group: Sensor Array Tab
- name: Polar pattern (dB)
  summary: 自定义麦克风极坐标响应 zeros(1,361)（默认）| 实值 *L*×*P* 矩阵
  group: Sensor Array Tab
- name: Geometry
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: Sensor Array Tab
- name: Number of elements
  summary: 阵列阵子数量 ULA 阵列为 2，UCA 阵列为 5（默认）| 大于或等于 2 的整数
  group: Sensor Array Tab
- name: Element spacing (m)
  summary: 阵列元素间距，对于 ULA 阵列为 0.5，对于 URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量
  group: Sensor Array Tab
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: Sensor Array Tab
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 的正整数向量
  group: Sensor Array Tab
- name: Element lattice
  summary: URA 元素位置的晶格 Rectangular（默认）| Triangular
  group: Sensor Array Tab
- name: Array normal
  summary: 阵列法线方向，对于 URA 阵列为 x，对于 UCA 阵列为 z（默认）| y
  group: Sensor Array Tab
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: Sensor Array Tab
- name: Element positions (m)
  summary: 共形阵列单元的位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: Sensor Array Tab
- name: Element normals (deg)
  summary: 共形阵列单元法向量的方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: Sensor Array Tab
- name: Taper
  summary: 阵列单元锥削 1（默认）| 复值标量 | 复值行向量
  group: Sensor Array Tab
- name: Subarray definition matrix
  summary: 定义属于子阵列的单元 逻辑矩阵
  group: Sensor Array Tab
- name: Subarray steering method
  summary: 指定子阵导向方法 None（默认）| Phase | Time
  group: Sensor Array Tab
- name: Phase shifter frequency (Hz)
  summary: 子阵相移频率 3.0e8（默认）| 正实值标量
  group: Sensor Array Tab
- name: Number of bits in phase shifters
  summary: 子阵导向相移量化位数 0（默认）| 非负整数
  group: Sensor Array Tab
- name: Subarrays layout
  summary: 子阵位置指定 Rectangular（默认）| Custom
  group: Sensor Array Tab
- name: Grid size
  summary: 矩形子阵网格的维度 [1,2]（默认）
  group: Sensor Array Tab
- name: Grid spacing (m)
  summary: 矩形网格上子阵之间的间距 Auto（默认）| 正实值标量 | 由正实值组成的 1×2 向量
  group: Sensor Array Tab
- name: Subarray positions (m)
  summary: 子阵位置 [0,0;0.5,0.5;0,0]（默认）| 3×*N* 实值矩阵
  group: Sensor Array Tab
- name: Subarray normals
  summary: 子阵法向量方向 [0,0;0,0]（默认）| 2×*N* 实矩阵
  group: Sensor Array Tab
```

### 主选项卡

### **Terrain gamma value (dB)** — 杂波模型参数 `0`（默认）| 标量

杂波模型参数，指定为标量。此参数
包含常数 γ 杂波模型中使用的 γ 值。γ 值取决于地形类型和工作
频率。单位为 dB。

**示例：** `-5.0`

**数据类型：** `double`

### **Earth model** — 地球形状 `Flat`（默认）| `Curved`

指定杂波仿真中使用的地球模型为 `Flat` 或 `Curved`。当您将此参数设置为 `Flat` 时，假定地球为平面。当您将此参数设置为 `Curved` 时，假定地球为球面。

### **Minimum range of clutter region (m)** — 杂波区域最小距离 `0` | 非负标量

将杂波仿真的最小距离指定为正标量。最小距离必须为非负值。单位为米。

### **Maximum range of clutter region (m)** — 杂波区域最大距离 `5000` | 非负标量

将杂波仿真的最大距离指定为正标量。最大距离必须大于 `Radar height` 参数指定的值。单位为米。

### **Azimuth center of clutter region (deg)** — 杂波区域方位中心 `0` | 标量

在地平面中生成杂波块的方位角。杂波块围绕该角度对称生成。单位为度。

### **Azimuth span of clutter region (deg)** — 杂波区域方位跨度 `60`（默认）| 正标量

将每个杂波块的方位跨度指定为正标量。单位为度。单位为度。

### **Azimuth span of clutter patches (deg)** — 杂波块方位跨度 `1`（默认）| 正标量

每个杂波块的方位跨度，指定为正标量。单位为度。

**数据类型：** `double`

### **Clutter coherence time (s)** — 杂波仿真的相干时间 `Inf`（默认）| 正标量

杂波仿真的相干时间，指定为正标量。相干时间过后，模块在下一个脉冲更新其用于杂波仿真的随机数。当您使用默认值 `Inf` 时，随机数永不更新。单位为秒。

**示例：** `4`

**数据类型：** `double`

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Sample rate (Hz)** — 杂波采样率 `1e6`（默认）| 正标量

杂波采样率，指定为正标量。单位为赫兹。

**示例：** `10e6`

**数据类型：** `double`

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量 | 正数值行向量

脉冲重复频率，PRF，指定为正标量或正数值行向量。单位为赫兹。

**示例：** `[1e4,2e4]`

**数据类型：** `double`

### **Enable PRF selection input** — 选择预定义 PRF off（默认）| on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环使用 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量。如果 **Pulse repetition frequency (Hz)** 为标量，则 PRF 恒定。

### **Source of simulation sample time** — 仿真采样时间来源 `Derive from waveform parameters`（默认）| `Inherit from Simulink engine`

仿真采样时间来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。当设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 决定的可变速率运行。经过时间是可变的。当设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **Enable PRF selection input** 参数。

### **Output signal format** — 输出信号 `Pulses`（默认）| `Samples` 的格式

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，则模块的输出由多个样本组成。样本数量为 **Number of samples in output** 参数的值。

如果将此参数设置为 `Pulses`，则模块的输出由多个脉冲组成。脉冲数量为 **Number of pulses in output** 参数的值。

### **Number of samples in output** — 输出中的样本数 `100`（默认）| 正整数

模块输出中的样本数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

**数据类型：** `double`

### **Number of pulses in output** — 输出中的脉冲数 `1`（默认）| 正整数

模块输出中的脉冲数，指定为正整数。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Pulses`。

**数据类型：** `double`

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

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### Radar 选项卡

### **Operating frequency (Hz)** — 系统工作频率 `3.0e8`（默认）| 正实数标量

系统工作频率，指定为正标量。单位为 Hz。

### **Effective transmitted power (W)** — 雷达系统有效发射功率 `5000`（默认）| 正标量

雷达系统的有效辐射功率（ERP），指定为正标量。单位为瓦特。

**示例：** `3500`

**数据类型：** `double`

### **Radar height (m)** — 雷达离地面高度 `0`（默认）| 非负标量

雷达离地面的高度，指定为非负标量。单位为米。

**示例：** `50`

**数据类型：** `double`

### **Radar speed (m/s)** — 雷达平台速度 `0`（默认）| 非负标量

雷达平台速度，指定为非负标量。单位为米每秒。

**示例：** `5`

**数据类型：** `double`

### **Radar motion direction (deg)** — 雷达平台运动方向 `[90;0]`（默认）| 2×1 实向量

将雷达平台运动方向指定为 `[AzimuthAngle;ElevationAngle]` 形式的 2×1 实向量。单位为度。方位角和俯仰角均在雷达天线或天线阵列的局部坐标系中测量。方位角必须介于 –180° 和 180° 之间。俯仰角必须介于 –90° 和 90° 之间。

该参数的默认值表示雷达平台垂直于雷达天线阵列视轴方向运动。

**示例：** `[25;30]`

**数据类型：** `double`

### **Sensor mounting angles sensor (deg)** — 传感器安装角度 `[0 0 0]`（默认）| 长度为 3 的正值向量

指定一个 3 元素向量，给出传感器坐标系相对于惯性坐标系的固有偏航角、俯仰角和横滚角。这 3 个元素分别定义绕 z、y 和 x 轴的旋转，按此顺序。第一次旋转使机体轴绕 z 轴旋转。由于这些角度定义固有旋转，第二次旋转是绕其因前一次旋转而产生的新位置上的 y 轴进行的。最后一次绕 x 轴的旋转是在固有系统中经过前两次旋转后的 x 轴上进行的。

**示例：** `[0,-10,4]`

**数据类型：** `double`

### **Enable weights input** — 启用天线阵元权重输入端口 未选中（默认）| 选中

选中此复选框以启用天线阵元权重输入端口 `W`。

### Sensor Array Tab

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### Element Parameters

### **Element type** — 阵元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1.0e20]`（默认）| 实值 1×2 行向量

将天线或麦克风阵元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该阵元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1.0e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风阵元在此向量最小值和最大值所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。使用 **Frequency
responses (dB)** 来设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的后向响应设置为零 off（默认）| on

选中此复选框以对元件的后向响应进行障板处理。当后向障板处理后，所有偏离视轴方向超过 ±90° 的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic
Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实数值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine
Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实数值行向量

自定义天线或自定义麦克风在 **Operating frequency vector
(Hz)** 参数所定义频率处的频率响应。**Frequency responses
(dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数来指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数来指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实数值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含边界值），且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实数值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含边界值），且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为
`Custom Antenna`，并将 **Input Pattern Coordinate
System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角度坐标 `0:180` | 实值 1×*Q* 行向量

用于指定天线辐射方向图的点的 Theta 角度，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角度必须介于 0° 和 360° 之间，并且严格递增。

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

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵子旋转至阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵子方向图旋转至与阵列法向对齐。未选中时，阵子方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵子坐标系的 *x* 轴指向阵列法向。未选中时使用未经旋转的阵子方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵子坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵子极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位面内测量。在方位面内，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵子位置

### **Number of elements** — 阵列阵子数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵子数量，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列元素间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 的正数值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列元素在局部阵列坐标系中沿此轴均匀分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 的正整数向量

URA 阵列的维度，指定为正整数或 1×2 的正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列具有相同的行数和列数。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列元素沿最左侧列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 元素位置的晶格 `Rectangular`（默认）| `Triangular`

URA 元素位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 在行和列方向上对齐所有元素。
- `Triangular` — 将矩形晶格的偶数行元素向正行轴方向偏移。位移为沿行维度元素间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向，对于 URA 阵列为 `x`，对于 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的元素位于与所选阵列法线方向正交的平面内。元素视轴方向指向阵列法线方向。

| Array Normal 参数值 | 元素位置和视轴方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面内。所有元素视轴向量指向 *x* 轴。 |
| `y` | 阵列元素位于 *zx* 平面内。所有元素视轴向量指向 *y* 轴。 |
| `z` | 阵列元素位于 *xy* 平面内。所有元素视轴向量指向 *z* 轴。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列单元的位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中单元的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的单元数。该矩阵的每一列表示阵列局部坐标系中一个阵列单元的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列单元法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中单元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的单元数。对于矩阵，每一列以 `[azimuth;elevation]` 的形式指定对应单元相对于局部坐标系的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列单元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示单元对之间通过某些变换产生差异的任何排列。这些变换可以组合平移、方位旋转和俯仰旋转。但是，不能使用需要绕法向方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列单元锥削 1（默认）| 复值标量 | 复值行向量

单元锥削，指定为复值标量或复值 1×*N* 行向量。在该向量中，*N* 表示阵列中的单元数。

也称为*单元权重*，锥削对阵列单元响应进行加权。锥削修改响应的幅度和相位，以降低旁瓣或控制主响应轴的方向。

如果 **Taper** 为标量，则对每个单元施加相同的权重。如果 **Taper** 为向量，则将向量中的权重施加到对应的传感器单元。权重数量必须与阵列的单元数匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的单元 逻辑矩阵

将子阵列选择指定为 *M*×*N* 矩阵。*M* 是子阵列的数量，*N* 是阵列中单元的总数。矩阵的每一行表示一个子阵列，行中的每个条目指示单元何时属于该子阵列。当条目为零时，该单元不属于该子阵列。非零条目表示施加到对应单元的复值权重。每一行必须至少包含一个非零条目。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵导向方法 `None`（默认）| `Phase` | `Time`

子阵导向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开窄带接收阵列、窄带发射阵列、宽带接收阵列、宽带发射阵列、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开窄带接收阵列、窄带发射阵列、宽带接收阵列、宽带发射阵列、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵相移频率 `3.0e8`（默认）| 正实值标量

子阵导向相移器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵导向相移量化位数 `0`（默认）| 非负整数

子阵导向相移量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认）| `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认）

矩形子阵网格大小，指定为单个正整数，或由正整数组成的 1×2 行向量。

如果 **Grid size** 是整数标量，则阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个元素是沿每一列的子阵数量。第二个元素是每一行中的子阵数量。行沿局部 *y* 轴方向，列沿局部 *z* 轴方向。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 来复制 3×2 URA 子阵。

#### 依赖

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认）| 正实值标量 | 由正实值组成的 1×2 向量

子阵的矩形网格间距，指定为正实值标量、由正实值组成的 1×2 行向量，或 `Auto`。单位为米。

- 如果 **Grid spacing** 是标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 是由 1×2 行向量组成，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个元素指定沿列的行之间的间距。第二个元素指定沿行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则复制在构建完整阵列时会为行和列保留子阵的阵元间距。仅当将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated
subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵位置 `[0,0;0.5,0.5;0,0]`（默认）| 3×*N* 实值矩阵

自定义网格中子阵的位置，指定为实值 3×*N* 矩阵，其中 *N* 是阵列中子阵的数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标以 `[x; y; z]` 的形式表示。单位是米。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated
subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量方向 `[0,0;0,0]`（默认）| 2×*N* 实矩阵

指定阵列中子阵的法线方向。此参数值为 2×*N* 矩阵，其中 *N* 是阵列中子阵的数量。矩阵的每一列以 `[azimuth;elevation]` 的形式指定对应子阵的法线方向。角度单位为度。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray
normals** 参数来表示子阵对之间通过某些变换产生差异的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法线旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays
layout** 设置为 `Custom`。
## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

恒定伽马杂波仿真

Constant Gamma Clutter 模块为在自由空间中发射窄带信号的单基地雷达生成从均匀地形反射的恒定伽马杂波。假设雷达处于恒定高度并以恒定速度移动。
