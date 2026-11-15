---
type: simulink-block
title: 'Constant Gamma Clutter'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Data Synthesis / Waveform-Level Simulations'
documentation_page: 'constantgammaclutter'
documentation_source_path: 'ref/constantgammaclutter.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Gamma Clutter

## 端口

### 输入

### **PRFIdx** — PRF 索引 正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从由 **Pulse repetition frequency (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例:**
`4`

#### 依赖关系

要启用此端口，请选择 **Enable PRF selection input**。

**数据类型:** `double`

### **W** — 阵元权值 长度为 *N* 的复数值向量

应用于阵列中每个阵元的权值，指定为长度为 *N* 的复数值向量。*N* 是 **Sensor array** 面板中选择的阵列中的阵元数。

#### 依赖关系

要启用此端口，请选择 **Enable weights input** 复选框。

**数据类型:** `double`
**复数支持:** Yes

### **WS** — 子阵阵元权值 *N*E-by-*N*S 复数值矩阵

应用于子阵中每个阵元的权值，指定为 *N*E-by-*N*S 复数值矩阵。

- 当将 **Specify sensor array** 设置为 `Replicated Subarray` 时，所有子阵具有相同维度。然后，可以将子阵阵元权值指定为复数值 *N*E-by-*N*S 矩阵。*NE* 是每个子阵中的阵元数，*NS* 是子阵数。`WS` 的每列指定对应子阵的权值。
- 当将 **Specify sensor array** 设置为 `Partitioned array` 时，子阵不必具有相同的维度和大小。可以将子阵阵元权值指定为复数值 *N*E-by-*N*S 矩阵，其中 *NE* 现在为最大子阵中的阵元数。每列的前 *K* 个条目是对应子阵的阵元权值，其中 *K* 是该子阵中的阵元数。

#### 依赖关系

要启用此端口，请将 **Specify sensor array** 设置为 `Partitioned array` 或 `Replicated Subarray`。然后，将 **Subarray steering method** 设置为 `Custom`。

**数据类型:** `double`
**复数支持:** Yes

### **Steer** — 转向角输入 标量 | 2-by-1 实数值向量

转向角，指定为标量或 2-by-1 实数值向量。作为向量时，转向角的形式为 `[AzimuthAngle; ElevationAngle]`。作为标量时，转向角仅表示方位角。此时俯仰角假定为零度。单位为 degrees

#### 依赖关系

要启用此端口，请将 **Specify sensor array** 设置为 `Partitioned array` 或 `Replicated Subarray`。然后，将 **Subarray steering method** 设置为 `Phase` 或 `Time`。

**数据类型:** `double`

### 输出

### **Out** — 仿真杂波 *N*-by-*M* 复数值矩阵

仿真杂波，返回为 *N*-by-*M* 复数值矩阵。

*N* 是模块输出的样本数。当将 **Output signal format** 参数设置为 `Samples` 时，使用 **Number of samples in output** 参数指定 *N*。当将 **Output signal format** 参数设置为 `Pulses` 时，*N* 是接下来 *P* 个脉冲中的总样本数，其中 *P* 在 **Number of pulse in output** 参数中指定。

*M* 为以下之一

- 如果传感器阵列包含子阵，则为传感器阵列中的子阵数。
- 如果传感器阵列不包含子阵，则为辐射或收集阵元数。

**数据类型:** `double`

## 参数

### 主选项卡

### **Terrain gamma value (dB)** — 杂波模型参数 `0`（默认）| 标量

杂波模型参数，指定为标量。此参数包含常数 γ 杂波模型中使用的 γ 值。γ 值取决于地形类型和工作频率。单位为 dB。

**示例:** `-5.0`

**数据类型:** `double`

### **Earth model** — 地球形状 `Flat`（默认）| `Curved`

指定杂波仿真中使用的地球模型为 `Flat` 或 `Curved`。当将此参数设置为 `Flat` 时，假定地球为平面。当将此参数设置为 `Curved` 时，假定地球为球面。

### **Minimum range of clutter region (m)** — 杂波区域最小距离 `0` | 非负标量

指定杂波仿真的最小距离为正标量。最小距离必须为非负。单位为 meters。

### **Maximum range of clutter region (m)** — 杂波区域最大距离 `5000` | 非负标量

指定杂波仿真的最大距离为正标量。最大距离必须大于 `Radar height` 参数中指定的值。单位为 meters。

### **Azimuth center of clutter region (deg)** — 杂波区域方位中心 `0` | 标量

在地平面上生成杂波片所围绕的方位角。杂波片围绕该角度对称生成。单位为 degrees。

### **Azimuth span of clutter region (deg)** — 杂波区域方位跨度 `60`（默认）| 正标量

指定每个杂波片的方位跨度为正标量。单位为 degrees。单位为 degrees。

### **Azimuth span of clutter patches (deg)** — 杂波片方位跨度 `1`（默认）| 正标量

每个杂波片的方位跨度，指定为正标量。单位为 degrees。

**数据类型:** `double`

### **Clutter coherence time (s)** — 杂波仿真相干时间 `Inf`（默认）| 正标量

杂波仿真的相干时间，指定为正标量。相干时间过后，模块在下一个脉冲更新其用于杂波仿真的随机数。使用默认值 `Inf` 时，随机数从不更新。单位为 seconds。

**示例:** `4`

**数据类型:** `double`

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为 meters per second。

**示例:** `3e8`

**数据类型:** `double`

### **Sample rate (Hz)** — 杂波采样率 `1e6`（默认）| 正标量

杂波采样率，指定为正标量。单位为 Hertz。

**示例:** `10e6`

**数据类型:** `double`

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量 | 正数值行向量

脉冲重复频率，PRF，指定为正标量或正数值行向量。单位为 Hertz。

**示例:** `[1e4,2e4]`

**数据类型:** `double`

### **Enable PRF selection input** — 选择预定义 PRF off（默认）| on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环使用 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量。如果 **Pulse repetition frequency (Hz)** 是标量，则 PRF 恒定。

### **Source of simulation sample time** — 仿真采样时间来源 `Derive from waveform parameters`（默认）| `Inherit from Simulink engine`

仿真采样时间来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 决定的可变速率运行。经过时间是可变的。设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **Enable PRF selection input** 参数。

### **Output signal format** — 输出信号格式 `Pulses`（默认）| `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，模块输出由多个样本组成。样本数是 **Number of samples in output** 参数的值。

如果将此参数设置为 `Pulses`，模块输出由多个脉冲组成。脉冲数是 **Number of pulses in output** 参数的值。

### **Number of samples in output** — 输出中的样本数 `100`（默认）| 正整数

模块输出中的样本数，指定为正整数。

**示例:** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

**数据类型:** `double`

### **Number of pulses in output** — 输出中的脉冲数 `1`（默认）| 正整数

模块输出中的脉冲数，指定为正整数。

**示例:** `2`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Pulses`。

**数据类型:** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，选择 `Interpreted Execution`。如果希望模块作为编译代码运行，选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

在开发和调优模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长仿真使用生成的代码比解释执行运行更快。可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

下表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 雷达选项卡

### **Operating frequency (Hz)** — 系统工作频率 `3.0e8`（默认）| 正实数值标量

系统工作频率，指定为正标量。单位为 Hz。

### **Effective transmitted power (W)** — 雷达系统有效发射功率 `5000`（默认）| 正标量

雷达系统的有效辐射功率 (ERP)，指定为正标量。单位为 watts。

**示例:** `3500`

**数据类型:** `double`

### **Radar height (m)** — 雷达离表面高度 `0`（默认）| 非负标量

雷达离表面高度，指定为非负标量。单位为 meters。

**示例:** `50`

**数据类型:** `double`

### **Radar speed (m/s)** — 雷达平台速度 `0`（默认）| 非负标量

雷达平台速度，指定为非负标量。单位为 meters per second。

**示例:** `5`

**数据类型:** `double`

### **Radar motion direction (deg)** — 雷达平台运动方向 `[90;0]`（默认）| 2-by-1 实数值向量

指定雷达平台运动方向为 2-by-1 实数值向量，形式为 `[AzimuthAngle;ElevationAngle]`。单位为 degrees。方位角和俯仰角均在雷达天线或天线阵列的局部坐标系中测量。方位角必须介于 –180° 和 180° 之间。俯仰角必须介于 –90° 和 90° 之间。

此参数的默认值表示雷达平台垂直于雷达天线阵列的宽边方向运动。

**示例:** `[25;30]`

**数据类型:** `double`

### **Sensor mounting angles sensor (deg)** — 传感器安装角度 `[0 0 0]`（默认）| 长度为 3 的正数值向量

指定一个 3 元素向量，给出传感器坐标系相对于惯性坐标系的固有偏航、俯仰和横滚。3 个元素分别定义绕 z、y 和 x 轴的旋转，按此顺序。第一个旋转绕 z 轴旋转机体轴。由于这些角度定义固有旋转，第二个旋转绕 y 轴在其经前一次旋转后的新位置执行。绕 x 轴的最终旋转在固有系统中绕已被前两次旋转旋转后的 x 轴执行。

**示例:** `[0,-10,4]`

**数据类型:** `double`

### **Enable weights input** — 启用天线阵元权值输入端口 unchecked（默认）| checked

复选框用于启用天线阵元权值输入端口 `W`。

### 传感器阵列选项卡

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ array System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox™ array System object。

**示例:** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### 阵元参数

### **Element type** — 阵列阵元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1.0e20]`（默认）| 实数值 1-by-2 行向量

指定天线或麦克风阵元的工作频率范围为 1-by-2 行向量，形式为 `[LowerBound,UpperBound]`。阵元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1.0e20]`（默认）| 实数值行向量

指定用于设置天线和麦克风频率响应的频率为 1-by-*L* 实数递增值行向量。天线或麦克风阵元在此向量最小和最大元素指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的后向响应设置为零 off（默认）| on

选择此复选框以阻挡阵元后向响应。当后向阻挡时，所有偏离宽边 ±90° 以外的方位角处的响应设置为零。宽边方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和俯仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 由非负值组成的实值 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或由非负值组成的实值 1-by-2 矩阵。当 **Exponent of cosine pattern** 为 1-by-2 向量时，第一个元素是方位角方向的指数，第二个元素是俯仰角方向的指数。当将此参数设置为标量时，方位角方向和俯仰角方向余弦方向图均提升到相同的幂。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在由 **Operating frequency vector (Hz)** 参数定义的频率处的频率响应。**Frequency responses (dB)** 的维度必须与由 **Operating frequency vector (Hz)** 参数指定的向量的维度匹配。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图时的方位角指定为 1-by-*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的俯仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图时的俯仰角指定为 1-by-*Q* 向量。*Q* 必须大于 2。角度单位为 degrees。俯仰角必须介于 –90° 和 90° 之间（含端点），并严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1-by-*P* 行向量

指定天线辐射方向图所在点的 Phi 角，指定为实值 1-by-*P* 行向量。*P* 必须大于 2。角度单位为 degrees。Phi 角必须介于 0° 和 360° 之间，并严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1-by-*Q* 行向量

指定天线辐射方向图所在点的 Theta 角，指定为实值 1-by-*Q* 行向量。*Q* 必须大于 2。角度单位为 degrees。Theta 角必须介于 0° 和 360° 之间，并严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量的长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量的长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则数组的每个 *Q*-by-*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的相位，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量的长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量的长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则数组的每个 *Q*-by-*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵元方向图旋转到与阵列法向对齐。未选中时，不旋转阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴沿阵列法向指向。未选中则使用未旋转的阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴沿阵列法向指向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1-by-*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1-by-*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 -by-*P* 行向量

指定极坐标方向图响应角度，指定为 1-by-*P* 向量。角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*-by-*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*-by-*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。该方向图在方位平面中测量。在方位平面中，俯仰角为 0°，中心拾音轴为 0° degrees azimuth 和 0° degrees elevation。极坐标方向图关于中心轴对称。可以根据极坐标方向图构造 3-D 空间中的麦克风响应方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数 `ULA` 阵列为 `2`，`UCA` 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵元数，指定为大于或等于 2 的整数。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元之间的间距 `ULA` 阵列为 `0.5`，`URA` 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元素正值向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或正值的 1-by-2 向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀分布。

#### 依赖项

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 正整数的 1-by-2 向量

URA 阵列的维度，指定为正整数或正整数的 1-by-2 向量。

- 如果 **Array size** 是 1-by-2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列具有相同的行数和列数。
- 当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

对于 URA，阵列阵元沿最左列从上到下索引，然后从左到右继续下一列。在此图中，**Array size** 值 `[3,2]` 创建一个具有三行两列的阵列。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 阵元位置的点阵 `Rectangular`（默认）| `Triangular`

URA 阵元位置的点阵，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元按行方向和列方向对齐。
- `Triangular` — 将矩形点阵的偶数行阵元向正行轴方向偏移。位移为沿行维度的阵元间距的一半。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法向方向 `URA` 阵列为 `x`，`UCA` 阵列为 `z`（默认）| `y`

阵列法向方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法向方向正交的平面内。阵元视轴方向沿阵列法向方向指向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵元位于 *yz* 平面内。所有阵元视轴向量均沿 *x* 轴指向。 |
| `y` | 阵元位于 *zx* 平面内。所有阵元视轴向量均沿 *y* 轴指向。 |
| `z` | 阵元位于 *xy* 平面内。所有阵元视轴向量均沿 *z* 轴指向。 |

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列半径，指定为正标量。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认）| 实值的 3-by-*N*matrix

共形阵列中阵元的位置，指定为实值的 3-by-*N* 矩阵，其中 *N* 是共形阵列中的阵元数。此矩阵的每一列表示阵列局部坐标系中某个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点是 *(0,0,0)*。单位是 meters。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列阵元法向向量的方向 `[0;0]` | 2-by-1 列向量 | 2-by-*N* 矩阵

共形阵列中阵元法向向量的方向，指定为 2-by-1 列向量或 2-by-*N* 矩阵。*N* 表示阵列中的阵元数。对于矩阵，每一列以 `[azimuth;elevation]` 形式指定相应阵元相对于局部坐标系的法向方向。局部坐标系使正 *x* 轴与共形阵列的法向方向对齐。如果参数值是 2-by-1 列向量，则所有阵列阵元使用相同的指向方向。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数表示任何成对阵元之间通过某些变换相关联的排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵元锥削 1（默认） | complex-valued scalar | complex-valued row vector

阵元锥削，指定为 complex-valued scalar 或 complex-valued 1-by-*N* row vector。在此向量中，*N* 表示阵列中的阵元数。

也称为 *element weights*，taper 将阵元响应相乘。taper 修改响应的幅度和相位，以减少旁瓣或引导主响应轴。

如果 **Taper** 是 scalar，则对每个阵元施加相同的权重。如果 **Taper** 是 vector，则将向量中的一个权重施加到对应的传感器阵元。权重数量必须与阵列的阵元数匹配。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数应用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的阵元 logical matrix

将子阵列选择指定为 *M*-by-*N* matrix。*M* 是子阵列数，*N* 是阵列中的阵元总数。矩阵的每一行表示一个子阵列，行中的每个条目指示对应阵元是否属于该子阵列。当条目为零时，阵元不属于该子阵列。非零条目表示施加到对应阵元的 complex-valued weight。每一行必须至少包含一个非零条目。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖项

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵列转向方法 `None`（默认） | `Phase` | `Time`

子阵列转向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖项

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵列相移频率 `3.0e8`（默认） | positive real-valued scalar

子阵列转向移相器的工作频率，指定为 positive real-valued scalar。单位为 Hz。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵列转向相移量化位数 `0`（默认） | non-negative integer

子阵列转向相移量化位数，指定为 non-negative integer。值为零表示不执行量化。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵列位置指定 `Rectangular`（默认） | `Custom`

将复制子阵列的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，
  使用 **Grid size** 和 **Grid spacing** 参数放置子阵列。
- 将此参数设置为 `Custom` 时，
  使用 **Subarray positions (m)** 和 **Subarray normals** 参数放置子阵列。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵列网格的维度 `[1,2]`（默认）

矩形子阵列网格大小，指定为单个 positive integer，或 positive integers 的 1-by-2 row vector。

如果 **Grid size** 是 integer scalar，则阵列在每一行和每一列中具有相同数量的子阵列。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 vector，则第一个条目是沿每一列的子阵列数。第二个条目是每一行中的子阵列数。行沿局部 *y* 轴，列沿局部 *z* 轴。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 复制 3-by-2 URA 子阵列。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵列之间的间距 `Auto`（默认） | positive real-valued scalar | 1-by-2 vector of positive real-values

子阵列的矩形网格间距，指定为 positive, real-valued scalar、positive, real-values 的 1-by-2 row vector，或 `Auto`。单位为 meters。

- 如果 **Grid spacing** 是 scalar，
  则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 是 1-by-2
  row vector，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumn]`。
  第一个条目指定沿列的行之间的间距。
  第二个条目指定沿行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，
  则复制在构建完整阵列时保留子阵列在行和列两个方向上的阵元间距。仅当将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵列的位置 `[0,0;0.5,0.5;0,0]`（默认） | 3-by-*N* real-valued matrix

自定义网格中子阵列的位置，指定为 real 3-by-*N* matrix，其中 *N* 是阵列中的子阵列数。矩阵的每一列表示阵列局部坐标系中单个子阵列的位置。坐标以 `[x; y; z]` 形式表示。单位为 meters。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵列法向量的方向 `[0,0;0,0]`（默认） | 2-by-*N* real matrix

指定阵列中子阵列的法线方向。此参数值是 2-by-*N* matrix，其中 *N* 是阵列中的子阵列数。矩阵的每一列指定对应子阵列的法线方向，形式为 `[azimuth;elevation]`。角度单位为 degrees。角度是相对于局部坐标系定义的。

可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示任意这样的排列：成对的子阵列通过某些变换而不同。这些变换可以组合平移、方位角旋转和仰角旋转。但是，不能使用需要绕法线旋转的变换。

#### 依赖项

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

## 所属库

Radar Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

恒定 gamma 杂波仿真

Constant Gamma Clutter 模块为向自由空间发射窄带信号的单基地雷达生成从均匀地形反射的恒定 gamma 杂波。假设雷达以恒定高度和恒定速度运动。
