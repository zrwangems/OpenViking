---
type: simulink-block
title: 'GPU Constant Gamma Clutter'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Data Synthesis / Waveform-Level Simulations'
documentation_page: 'gpuconstantgammaclutter'
documentation_source_path: 'ref/gpuconstantgammaclutter.html'
language: zh-CN
chinese_source: worker-translation
---

# GPU Constant Gamma Clutter

## 端口

### 输入

### **PRFIdx** — PRF 索引 正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从 **Pulse repetition frequency (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例：**
`4`

#### 依赖关系

要启用此端口，请选择 **Enable PRF selection input**。

**数据类型：** `double`

### **W** — 阵元权重 长度-*N* 复数值向量

应用于阵列中每个阵元的权重，指定为长度-*N* 的复数值向量。*N* 是在 **Sensor array** 面板中选择的阵列中的阵元数。

#### 依赖关系

要启用此端口，请选中 **Enable weights input** 复选框。

**数据类型：** `double`
**复数支持：** Yes

### **WS** — 子阵元权重 *N*E-by-*N*S 复数值矩阵

应用于子阵中每个阵元的权重，指定为 *N*E-by-*N*S 复数值矩阵。

- 当您将 **Specify sensor array** 设置为 `Replicated Subarray` 时，所有子阵具有相同的维度。然后，您可以将子阵元权重指定为复数值 *N*E-by-*N*S 矩阵。*NE* 是每个子阵中的阵元数，*N*S 是子阵数。`WS` 的每一列指定对应子阵的权重。
- 当您将 **Specify sensor array** 设置为 `Partitioned array` 时，子阵不需要具有相同的维度和大小。您可以将子阵元权重指定为复数值 *N*E-by-*N*S 矩阵，其中 *N*E 现在是最大子阵中的阵元数。每一列中的前 *K* 个条目是对应子阵的阵元权重，其中 *K* 是该子阵中的阵元数。

#### 依赖关系

要启用此端口，请将 **Specify sensor array** 设置为 `Partitioned array` 或 `Replicated Subarray`。然后，将 **Subarray steering method** 设置为 `Custom`。

**数据类型：** `double`
**复数支持：** Yes

### **Steer** — 导向角输入 标量 | 2-by-1 实数值向量

导向角，指定为标量或 2-by-1 实数值向量。作为向量时，导向角的形式为 `[AzimuthAngle; ElevationAngle]`。作为标量时，导向角仅表示方位角。此时仰角假定为零 degrees。单位是 degrees

#### 依赖关系

要启用此端口，请将 **Specify sensor array** 设置为 `Partitioned array` 或 `Replicated Subarray`。然后，将 **Subarray steering method** 设置为 `Phase` 或 `Time`。

**数据类型：** `double`

### 输出

### **Out** — 模拟杂波 *N*-by-*M* 复数值矩阵

模拟杂波，返回为 *N*-by-*M* 复数值矩阵。

*N* 是模块输出的样本数。当您将 **Output signal format** 参数设置为 `Samples` 时，使用 **Number of samples in output** 参数指定 *N*。当您将 **Output signal format** 参数设置为 `Pulses` 时，*N* 是接下来 *P* 个脉冲中的总样本数，其中 *P* 在 **Number of pulse in output** 参数中指定。

*M* 要么是

- 如果传感器阵列包含子阵，则为传感器阵列中的子阵数。
- 如果传感器阵列不包含子阵，则为辐射或收集阵元数。

**数据类型：** `double`

## 参数

### 主选项卡

### **Terrain gamma value (dB)** — 杂波模型参数 `0` (default) | 标量

杂波模型参数，指定为标量。此参数包含恒定 γ 杂波模型中使用的 γ 值。γ 值取决于地形类型和工作频率。单位是 dB。

**示例：** `-5.0`

**数据类型：** `double`

### **Earth model** — 地球形状 `Flat` (default) | `Curved`

将杂波仿真中使用的地球模型指定为 `Flat` 或 `Curved`。当您将此参数设置为 `Flat` 时，假定地球为平面。当您将此参数设置为 `Curved` 时，假定地球为球体。

### **Minimum range of clutter region (m)** — 杂波区域最小距离 `0` | 非负标量

将杂波仿真的最小距离指定为正标量。最小距离必须为非负。单位是 meters。

### **Maximum range of clutter region (m)** — 杂波区域最大距离 `5000` | 非负标量

将杂波仿真的最大距离指定为正标量。最大距离必须大于 `Radar height` 参数中指定的值。单位是 meters。

### **Azimuth center of clutter region (deg)** — 杂波区域方位中心 `0` | 标量

地面平面中生成杂波块所围绕的方位角。杂波块围绕该角度对称生成。单位是 degrees。

### **Azimuth span of clutter region (deg)** — 杂波区域方位跨度 `60` (default) | 正标量

将每个杂波块的方位跨度指定为正标量。单位是 degrees。单位是 degrees。

### **Azimuth span of clutter patches (deg)** — 杂波块方位跨度 `1` (default) | 正标量

每个杂波块的方位跨度，指定为正标量。单位是 degrees。

**数据类型：** `double`

### **Clutter coherence time (s)** — 杂波仿真的相干时间 `Inf` (default) | 正标量

杂波仿真的相干时间，指定为正标量。相干时间过后，模块会在下一个脉冲更新其用于杂波仿真的随机数。当您使用默认值 `Inf` 时，随机数永远不会更新。单位是 seconds。

**示例：** `4`

**数据类型：** `double`

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')` (default) | 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。单位是 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **Sample rate (Hz)** — 杂波采样率 `1e6` (default) | 正标量

杂波采样率，指定为正标量。单位是 Hertz。

**示例：** `10e6`

**数据类型：** `double`

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4` (default) | 正标量 | 正值的行向量

脉冲重复频率 (PRF)，指定为正标量或正值的行向量。单位是 Hertz。

**示例：** `[1e4,2e4]`

**数据类型：** `double`

### **Enable PRF selection input** — 选择预定义 PRF off (default) | on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环使用由 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量。如果 **Pulse repetition frequency (Hz)** 是标量，则 PRF 恒定。

### **Output signal format** — 输出信号格式 `Pulses` (default) | `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果您将此参数设置为 `Samples`，则模块输出由多个样本组成。样本数是 **Number of samples in output** 参数的值。

如果您将此参数设置为 `Pulses`，则模块输出由多个脉冲组成。脉冲数是 **Number of pulses in output** 参数的值。

### **Number of samples in output** — 输出中的样本数 `100` (default) | 正整数

模块输出中的样本数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

**数据类型：** `double`

### **Number of pulses in output** — 输出中的脉冲数 `1` (default) | 正整数

模块输出中的脉冲数，指定为正整数。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Pulses`。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution` (default) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，随后可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 雷达选项卡

### **Operating frequency (Hz)** — 系统工作频率 `3.0e8` (default) | 正实标量

系统工作频率，指定为正标量。单位是 Hz。

### **Effective transmitted power (W)** — 雷达系统有效发射功率 `5000` (default) | 正标量

雷达系统的有效辐射功率 (ERP)，指定为正标量。单位是 watts。

**示例：** `3500`

**数据类型：** `double`

### **Radar height (m)** — 雷达高于表面的高度 `0` (default) | 非负标量

雷达高于表面的高度，指定为非负标量。单位是 meters。

**示例：** `50`

**数据类型：** `double`

### **Radar speed (m/s)** — 雷达平台速度 `0` (default) | 非负标量

雷达平台速度，指定为非负标量。单位是 meters per second。

**示例：** `5`

**数据类型：** `double`

### **Radar motion direction (deg)** — 雷达平台运动方向 `[90;0]` (default) | 2-by-1 real vector

将雷达平台运动方向指定为形式为 `[AzimuthAngle;ElevationAngle]` 的 2-by-1 实向量。单位是 degrees。方位角和仰角均在雷达天线或天线阵列的局部坐标系中测量。方位角必须介于 –180° 和 180° 之间。仰角必须介于 –90° 和 90° 之间。

此参数的默认值表示雷达平台垂直于雷达天线阵列的宽边方向运动。

**示例：** `[25;30]`

**数据类型：** `double`

### **Sensor mounting angles sensor (deg)** — 传感器安装角度 `[0 0 0]` (default) | 正值的 length-3 向量

指定一个 3 元素向量，给出传感器坐标系相对于惯性坐标系的固有偏航、俯仰和横滚。3 个元素分别按该顺序定义绕 z、y 和 x 轴的旋转。第一次旋转使机体轴绕 z 轴旋转。由于这些角度定义固有旋转，第二次旋转在由前一次旋转产生的新位置上绕 y 轴执行。绕 x 轴的最终旋转是在固有系统中由前两次旋转旋转后的 x 轴上执行。

**示例：** `[0,-10,4]`

**数据类型：** `double`

### **Enable weights input** — 启用天线阵元权重输入端口 unchecked (default) | checked

复选框用于启用天线阵元权重输入端口 `W`。

### 传感器阵列选项卡

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)` (default) | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

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

#### 阵元参数

### **Element type** — 阵列阵元类型 `Isotropic Antenna` (default) | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1.0e20]` (default) | 实数值 1-by-2 行向量

将天线或麦克风阵元的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1-by-2 行向量。阵元在此频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1.0e20]` (default) | 实数值行向量

将设置天线和麦克风频率响应的频率指定为 1-by-*L* 的递增值实数值行向量。天线或麦克风阵元在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 在这些频率处设置响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的后向响应设置为零 off (default) | on

选中此复选框以对消阵元的后向响应。当后向对消时，在距宽边 ±90° 之外的所有方位角处的响应都设置为零。宽边方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]` (default) | 非负标量 | 非负值的实数值 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实数值 1-by-2 矩阵。当 **Exponent of cosine pattern** 是 1-by-2 向量时，第一个元素是方位方向的指数，第二个元素是仰角方向的指数。当您将此参数设置为标量时，方位方向和仰角方向的余弦方向图都升高到相同的幂。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Cosine Antenna`。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| real-valued row vector

自定义天线或自定义麦克风在由 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量的维度匹配。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **方位角 (deg)** 和 **仰角 (deg)** 参数指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| real-valued row vector

将计算天线辐射方向图所在的方位角指定为 1-by-*P* row vector。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **元件类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **仰角 (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| real-valued row vector

将计算辐射方向图所在的仰角指定为 1-by-*Q* vector。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **元件类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | real-valued 1-by-*P* row vector

指定天线辐射方向图所在点的 Phi 角，指定为 real-valued 1-by-*P* row vector。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **元件类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | real-valued 1-by-*Q* row vector

指定天线辐射方向图所在点的 Theta 角，指定为 real-valued 1-by-*Q* row vector。*Q* 必须大于 2。角度单位为度。Theta 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **元件类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

组合天线辐射方向图的幅度，指定为 *Q*-by-*P* matrix 或 *Q*-by-*P*-by-*L* array。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于由 **仰角 (deg)** 参数指定的向量的长度，*P* 等于由 **方位角 (deg)** 参数指定的向量的长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta 角 (deg)** 参数指定的向量的长度，*P* 等于由 **Phi 角 (deg)** 参数指定的向量的长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* matrix，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*-by-*P*-by-*L* array，则数组的每个 *Q*-by-*P* 页指定 **工作频率向量 (Hz)** 参数中指定的 *对应* 频率的方向图。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna`。

### **相位方向图 (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

组合天线辐射方向图的相位，指定为 *Q*-by-*P* matrix 或 *Q*-by-*P*-by-*L* array。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于由 **仰角 (deg)** 参数指定的向量的长度，*P* 等于由 **方位角 (deg)** 参数指定的向量的长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta 角 (deg)** 参数指定的向量的长度，*P* 等于由 **Phi 角 (deg)** 参数指定的向量的长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* matrix，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*-by-*P*-by-*L* array，则数组的每个 *Q*-by-*P* 页指定在 **工作频率向量 (** 中指定的 *对应* 频率的方向图。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法线 `on`（默认）| `off`

选中此复选框可将天线阵元方向图旋转以与阵列法线对齐。未选中时，阵元方向图不旋转。

当天线用于天线阵列且 **输入方向图坐标系** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴指向阵列法线。不选中则使用未旋转的阵元方向图。

当天线用于天线阵列且 **输入方向图坐标系** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴指向阵列法线。

将此参数与 `URA` 和 `UCA` 阵列的 **阵列法线** 参数结合使用。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Antenna`。

### **极化方向图频率 (Hz)** — 极化方向图麦克风响应频率 1e3（默认）| real scalar | real-valued 1-by-*L* row vector

极化方向图麦克风响应频率，指定为 real scalar，或 real-valued, 1-by-*L* vector。响应频率位于 **工作频率向量 (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

### **极化方向图角度 (deg)** — 极化方向图响应角度 `[-180:180]`（默认）| real-valued -by-*P* row vector

将极化方向图响应角度指定为 1-by-*P* vector。角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

### **极化方向图 (dB)** — 自定义麦克风极化响应 `zeros(1,361)`（默认）| real-valued *L*-by-*P* matrix

将自定义麦克风阵元极化方向图的幅度指定为 *L*-by-*P* matrix。*L* 是 **极化方向图频率 (Hz)** 中指定的频率数量。*P* 是 **极化方向图角度 (deg)** 中指定的角度数量。矩阵的每一行表示在 **极化方向图频率 (Hz)** 中指定的对应频率以及 **极化方向图角度 (deg)** 中指定的所有角度处测得的极化方向图幅度。该方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极化方向图围绕中心轴对称。您可以从极化方向图构建 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **元件类型** 设置为 `Custom Microphone`。

#### 阵列参数

### **几何结构** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **阵元数量** — 阵列阵元数量，ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| integer greater than or equal to 2

ULA 或 UCA 阵列的阵元数量，指定为 integer greater than or equal to 2。

当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `ULA` 或 `UCA`。

### **阵元间距 (m)** — 阵列阵元之间的间距，ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| positive scalar for ULA or URA arrays | 2-element vector of positive values for URA arrays

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为 positive scalar。
- URA — 将间距指定为 positive scalar 或 1-by-2 vector of positive values。如果 **阵元间距 (m)** 是标量，则行间距和列间距相等。如果 **阵元间距 (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `ULA` 或 `URA`。

### **阵列轴** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **几何结构** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **阵列大小** — URA 阵列的维度 `[2,2]`（默认）| positive integer | 1-by-2 vector of positive integers

URA 阵列的维度，指定为 positive integer 或 1-by-2 vector of positive integers。

- 如果 **阵列大小** 是 1-by-2 vector，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **阵列大小** 是整数，则阵列具有相同的行数和列数。
- 当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列阵元沿最左侧列从上到下编制索引，然后从左到右继续到下一列。在此图中，**阵列大小** 值 `[3,2]` 创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA`。

### **阵元晶格** — URA 阵元位置的晶格 `Rectangular`（默认）| `Triangular`

URA 阵元位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 在行和列方向上对齐所有阵元。
- `Triangular` — 将矩形晶格的偶数行阵元向正行轴方向偏移。位移为沿行维度的阵元间距的一半。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA`。

### **阵列法线** — 阵列法线方向，URA 阵列为 `x` 或 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元波束指向方向沿阵列法线方向。

| 阵列法线参数值 | 阵元位置和波束指向方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面。所有阵元波束指向矢量沿 *x* 轴。 |
| `y` | 阵列阵元位于 *zx* 平面。所有阵元波束指向矢量沿 *y* 轴。 |
| `z` | 阵列阵元位于 *xy* 平面。所有阵元波束指向矢量沿 *z* 轴。 |

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA` 或 `UCA`。

### **UCA 半径 (m)** — UCA 阵列半径 0.5（默认）| positive scalar

UCA 阵列的半径，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `UCA`。

### **阵元位置 (m)** — 共形阵列阵元的位置 `[0;0;0]`（默认）| 3-by-*N*matrix of real values

共形阵列中阵元的位置，指定为 3-by-*N* matrix of real values，其中 *N* 是共形阵列中的阵元数量。此矩阵的每一列表示阵列局部坐标系中某个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点是 *(0,0,0)*。单位是米。

当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `Conformal Array`。

### **阵元法线 (deg)** — 共形阵列阵元法线向量的方向 `[0;0]` | 2-by-1 column vector | 2-by-*N* matrix

共形阵列中阵元法线向量的方向，指定为 2-by-1 column vector 或 2-by-*N* matrix。*N* 表示阵列中的阵元数量。对于矩阵，每一列以 `[azimuth;elevation]` 形式指定对应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值是 2-by-1 column vector，则所有阵列阵元使用相同的指向方向。

当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **阵元位置 (m)** 和 **阵元法线 (deg)** 参数来表示任何这样的排列：其中成对的阵元通过某些变换而不同。这些变换可以组合平移、方位旋转和仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `Conformal Array`。

### **加权** — 阵列阵元加权 1（默认）| complex-valued scalar | complex-valued row vector

阵元加权，指定为 complex-valued scalar 或 complex-valued 1-by-*N* row vector。在此向量中，*N* 表示阵列中的阵元数量。

也称为 *阵元权重*，加权会乘以阵列阵元响应。加权会修改响应的幅度和相位，以减少旁瓣或控制主响应轴方向。

如果 **加权** 是标量，则对每个阵元应用相同的权重。如果 **加权** 是向量，则向量中的一个权重应用于对应的传感器阵元。权重数量必须与阵列的阵元数量匹配。

当您将 **将传感器阵列指定为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵的元素逻辑矩阵

将子阵选择指定为 *M*-by-*N* 矩阵。*M* 是子阵的数量，*N* 是阵列中元素的总数。矩阵的每一行表示一个子阵，行中的每个条目指示元素何时属于该子阵。当条目为零时，该元素不属于该子阵。非零条目表示应用于对应元素的复值权重。每一行必须至少包含一个非零条目。

每个子阵的相位中心位于子阵几何中心。子阵几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵转向方法 `None`（默认）| `Phase` | `Time`

子阵转向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵相移频率 `3.0e8`（默认）| 正实值标量

子阵转向移相器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵转向相移量化位数 `0`（默认）| 非负整数

子阵转向相移量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认）| `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，
  使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 将此参数设置为 `Custom` 时，
  使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认）

矩形子阵网格大小，指定为单个正整数，或由正整数组成的 1-by-2 行向量。

如果 **Grid size** 是整数标量，则该阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 向量，则第一个条目是沿每一列的子阵数量。第二个条目是每一行中的子阵数量。一行沿局部 *y* 轴，一列沿局部 *z* 轴。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 复制 3-by-2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认）| 正实值标量 | 正实值组成的 1-by-2 向量

子阵的矩形网格间距，指定为正实值标量、正实值组成的 1-by-2 行向量或 `Auto`。单位为 meters。

- 如果 **Grid spacing** 是标量，
  则沿行的间距和沿列的间距相同。
- 如果 **Grid spacing** 是 1-by-2 行向量，
  则该向量形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。
  第一个条目指定沿一列的行之间的间距。
  第二个条目指定沿一行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，
  则在构建完整阵列时，复制会为行和列保留子阵的元素间距。仅当将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵位置 `[0,0;0.5,0.5;0,0]`（默认）| 3-by-*N* 实值矩阵

自定义网格中子阵的位置，指定为实值 3-by-*N* 矩阵，其中 *N* 是阵列中子阵的数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标以 `[x; y; z]` 形式表示。单位为 meters。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量方向 `[0,0;0,0]`（默认）| 2-by-*N* 实矩阵

指定阵列中子阵的法向方向。此参数值是 2-by-*N* 矩阵，其中 *N* 是阵列中子阵的数量。矩阵的每一列以 `[azimuth;elevation]` 形式指定对应子阵的法向方向。角度单位为 degrees。角度相对于局部坐标系定义。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数表示任意排列，其中成对的子阵通过某些变换而不同。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

## 所属库

Radar Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

使用 GPU 的恒定 gamma 杂波仿真

GPU Constant Gamma Clutter 模块使用图形处理单元 (GPU) 生成由均匀地形反射的恒定 gamma 杂波，适用于向自由空间发射窄带信号的单基地雷达。假设该雷达处于恒定高度并以恒定速度运动。
