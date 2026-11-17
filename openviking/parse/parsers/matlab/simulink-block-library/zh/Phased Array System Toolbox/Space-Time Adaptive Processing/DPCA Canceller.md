---
type: simulink-block
title: 'DPCA Canceller'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'dpcacanceller'
documentation_source_path: 'ref/dpcacanceller.html'
language: zh-CN
chinese_source: worker-translation
---

# DPCA Canceller

## 端口

### 输入

### **X** — 输入信号 *M*-by-*N*-by-*P* 复值矩阵

输入信号，指定为
*M*-by-*N*-by-*P*
复值数组。*M* 是距离采样数，*N* 是通道数，*P* 是脉冲数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Idx** — 距离单元索引 正整数

用于计算处理权值的距离单元索引。

**示例：** `1`

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 目标方向 `2`-by-`1` 实值向量

目标方向，指定为
`2`-by-*1* 实值向量。该向量采用
`[AzimuthAngle;ElevationAngle]` 的形式。角度单位为度。方位角必须介于 –180° 和 180° 之间（含边界），俯仰角必须介于 –90° 和 90° 之间（含边界）。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，请将 **Specify direction as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Dop** — 目标多普勒频率 标量

当前脉冲的目标多普勒频率，指定为标量。

#### 依赖关系

当 **Output pre-Doppler result** 复选框清除且 **Specify targeting Doppler as** 参数设置为 `Input port` 时，此端口出现。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*-by-1 复值向量

处理输出，返回为
*M*-by-*1* 复值向量。
量 *M* 是输入端口 `X` 中的距离采样数。

**数据类型：** `double`
**复数支持：** 是

### **W** — 处理权值 长度 *N*\**P* 复值向量

处理权值，返回为长度
*N*\**P* 复值向量。量 *N* 是通道数，*P* 是脉冲数。当 **Specify sensor array as** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，*N* 表示子阵数。*L* 是在 `Ang` 输入端口或通过 **Beamforming direction (deg)** 参数指定的期望波束形成方向数。每个波束形成方向有一组权值。

#### 依赖关系

要启用此端口，请选中 **Enable weights output** 复选框。

**数据类型：** `double`
**复数支持：** 是

## 参数

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Specify PRF as** — PRF 值来源 `Property`（默认）| `Input port`

PRF 值来源，指定为 `Property` 或 `Input port`。当设置为 `Property` 时，**Pulse repetition frequency (Hz)** 参数设置 PRF。当设置为 `Input port` 时，使用 `PRF` 输入端口传入 PRF。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1`（默认）| 正标量

脉冲重复频率 PRF，指定为正标量。单位为赫兹。将此参数设置为仿真中使用的任何 `Waveform` 库模块中设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为
`Property`。

### **Specify direction as** — 指定目标方向的来源 `Property`（默认）| `Input port`

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

### **Specify targeting Doppler as** — 目标多普勒的来源 `Property`（默认）| `Input port`

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

### **Enable weights output** — 输出波束形成器权重的选项 off（默认）| on

选中此复选框以从输出端口
`W` 获取波束形成器权重。

### **Output pre-Doppler result** — 在多普勒滤波之前输出结果 on（默认）| off

选中此复选框以在多普勒滤波之前输出结果。
清除此复选框以在多普勒滤波之后输出处理结果。选中此复选框将移除 **Specify
targeting Doppler as** 和 **Targeting Doppler
(Hz)** 参数。

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

将天线或麦克风单元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该单元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风单元的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风单元在此向量最小值和最大值指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。使用
**Frequency responses (dB)** 来设置这些频率下的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的后向响应设置为零 off（默认）| on

选中此复选框以对元件的后向响应进行障板处理。当后向被障板时，
所有超出从正侧 ±90° 范围的方位角处的响应均设置为零。正侧方向
定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将
**Element type** 设置为
`Isotropic Antenna` 或
`Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或
非负实值 1×2 矩阵。当
**Exponent of cosine pattern** 为
1×2 向量时，第一个元素是方位角
方向的指数，第二个元素是
仰角方向的指数。当您将此参数设置为标量时，
方位角方向和仰角方向的余弦
方向图均被提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **Element
type** 设置为 `Cosine
Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义
麦克风在由
**Operating frequency vector
(Hz)** 参数定义的频率处的频率响应。
**Frequency responses (dB)** 的维度必须
与 **Operating frequency vector
(Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将
**Element type** 设置为
`Custom Antenna` 或
`Custom
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

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图的方位角指定为
1×*P* 行向量。*P* 必须
大于 2。方位角必须介于 –180° 和 180° 之间（含端点），
并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图的仰角指定为
1×*Q* 向量。*Q* 必须
大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），
并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为
实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且
严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角度坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图所在点的 Theta 角度，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角度必须介于 0° 和 360° 之间，并且严格递增。

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

指定极坐标方向图响应角度，为 1×*P* 向量。角度从麦克风中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵子极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位面内测量。在方位面内，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### 阵列参数

### **Specify sensor array as** — 阵列类型 `Array (no subarrays)`（默认）| `MATLAB expression`

直接指定 ULA 传感器阵列或使用 MATLAB 表达式指定。

**类型**

|  |
| --- |
| `Array (no subarrays)` |
| `MATLAB expression` |

### **Number of elements** — U 中的阵列阵子数 `2`（默认）| 大于或等于 2 的正整数

ULA 阵列的阵子数，指定为大于或等于 2 的整数。

**示例：** `11`

**数据类型：** `double`

### **Element spacing** — ULA 阵子间距 `0.5`（默认）| 正标量

相邻 ULA 阵子之间的距离，指定为正标量。单位为米。

**示例：** `1.5`

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵子在局部阵列坐标系中沿此轴均匀分布。

#### 依赖

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Taper** — ULA 阵列锥度 `1`（默认）| 复值向量

锥度，也称为*阵元权重*，应用于阵列中的传感器阵元。锥度用于修改发射或接收数据的幅度和相位。

将阵元锥度指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数量。如果 **Taper** 为标量，则相同的权重应用于每个阵元。如果 **Taper** 为向量，则向量中的权重应用于对应的传感器阵元。必须为传感器阵列中的每个阵元应用权重。

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

均匀线阵的位移相位中心阵列（DPCA）脉冲对消器

DPCA Canceller 模块使用位移相位中心阵列脉冲对消器对入射到均匀线阵上的杂波进行滤波。
