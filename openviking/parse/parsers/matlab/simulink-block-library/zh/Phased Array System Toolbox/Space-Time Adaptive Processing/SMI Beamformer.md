---
type: simulink-block
title: 'SMI Beamformer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'smibeamformer'
documentation_source_path: 'ref/smibeamformer.html'
language: zh-CN
chinese_source: worker-translation
---

# SMI Beamformer

## 端口

### 输入

### **X** — 输入信号 *M*-by-*N*-by-*P* 复值矩阵

输入信号，指定为
*M*-by-*N*-by-*P*
复值数组。*M* 是距离
样本数，*N* 是通道数，*P* 是脉冲数。

输入矩阵第一维的大小可以变化，以
模拟变化的信号长度。例如，在脉冲
重复频率可变的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Idx** — 距离单元索引 正整数

用于计算处理权重的距离单元索引。

**示例：** `1`

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，指定为正
标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as**
参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 目标方向 `2`-by-`1` 实值向量

目标方向，指定为
`2`-by-*1* 实值向量。该
向量采用
`[AzimuthAngle;ElevationAngle]` 的形式。角度单位为
度。方位角必须介于 –180° 和 180° 之间（含边界），
俯仰角必须介于 –90° 和 90° 之间（含边界）。角度
是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，请将 **Specify direction
as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Dop** — 目标多普勒频率 标量

当前脉冲的目标多普勒频率，指定为
标量。

#### 依赖关系

要启用此端口，请将 **Specify targeting Doppler
as** 参数设置为 `Input
port`。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*-by-1 复值向量

处理输出，返回为
*M*-by-*1* 复值向量。
量 *M* 是输入端口 `X` 中的距离
样本数。

**数据类型：** `double`
**复数支持：** 是

### **W** — 处理权重 长度 *N*\**P* 复值向量

处理权重，返回为长度
*N*\**P* 复值向量。量
*N* 是通道数，*P* 是脉冲数。当
**Specify sensor array as** 参数设置为
`Partitioned array` 或 `Replicated
subarray` 时，*N* 表示子阵
数。*L* 是在 `Ang` 输入端口或通过
**Beamforming direction (deg)** 参数指定的期望波束形成
方向数。每个波束形成方向有一组权重。

#### 依赖关系

要启用此端口，请选中 **Enable weights
output** 复选框。

**数据类型：** `double`
**复数支持：** 是

## 参数

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认
值是
`physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Specify PRF as** — PRF 值的来源 `Property`（默认）| `Input port`

PRF 值的来源，指定为 `Property` 或
`Input port`。当设置为
`Property` 时，**Pulse repetition frequency
(Hz)** 参数设置 PRF。当设置为 `Input
port` 时，通过 `PRF` 输入
端口传入 PRF。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1`（默认）| 正标量

脉冲重复频率，PRF，指定为正标量。单位为赫兹。
将此参数设置为仿真中使用的任何 `Waveform` 库
模块中设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为
`Property`。

### **Specify direction as** — 指定目标方向的来源 `Property`（默认）| `Input port`

指定 STAP 处理器模块的目标方向来自模块参数还是来自 `ANG` 输入端口。此参数的值为

|  |  |
| --- | --- |
| `Property` | - 对于 ADPCA Canceller 和 DPCA Canceller 模块，目标方向使用 **Receiving mainlobe direction (deg)** 指定。 - 对于 SMI Beamformer 模块，目标方向使用 **Targeting direction** 指定。 这些参数仅在 **Specify direction as** 参数设置为 `Property` 时显示。 |
| `Input port` | 使用 `Ang` 输入端口输入目标方向。此端口仅在 **Specify direction as** 设置为 `Input port` 时显示。 |

### **Targeting direction (deg)** — 处理器目标方向 `[0;0]`（默认）| 实值长度为 2 的列向量

处理器目标方向，指定为方位角和俯仰角的实值长度为 2 的列向量，
`[AzimuthAngle;ElevationAngle]`。
方位角介于 –180° 和 180° 之间，俯仰角
介于 –90° 和 90° 之间。单位为度。

#### 依赖关系

要启用此参数，请将 **Specify direction
as** 设置为
`Property`。

### **Number of bits in phase shifters** — 移相器量化位数 `0`（默认）| 非负整数

用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **Specify targeting Doppler as** — 目标多普勒的来源 `Property`（默认）| `Input port`

指定 STAP 处理器的目标多普勒值来自此模块的 **Targeting Doppler (Hz)** 参数还是使用 `DOP` 输入端口。对于 ADPCA Canceller 和 DPCA Canceller 模块，**Specify targeting Doppler as** 参数仅在 **Output pre-Doppler result** 复选框清除时显示。此参数的值为

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
在可能的情况下，保护单元集合被等分为测试单元之前和之后的区域。

### **Number of training cells** — 用于训练的单元数 `2`（默认）| 正偶整数

用于训练的单元数，指定为正偶整数。在可能的情况下，
训练单元集合被等分为测试单元之前和之后的区域。

### **Enable weights output** — 输出波束形成器权重的选项 关（默认）| 开

选中此复选框以从输出端口 `W` 获取波束形成器权重。

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

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

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

### **Operating frequency vector (Hz)** — 自定义天线或麦克风元件的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风元件在此向量最小值和最大值所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的背面响应设置为零 off（默认）| on

选中此复选框可对元件的背面响应进行 baffle。当背面 baffled 时，所有偏离 broadside 超过 ±90° 的方位角处的响应均设置为零。broadside 方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当您将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

由 **Operating frequency vector (Hz)** 参数定义的频率处自定义天线或自定义麦克风的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间（含端点），并且严格递增。

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

### **MatchArrayNormal** — 将天线阵子旋转到阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵子方向图旋转至与阵列法向对齐。未选中时，阵子方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵子坐标系的 *x* 轴指向阵列法向。未选中时使用不旋转的阵子方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵子坐标系的 *z* 轴指向阵列法向。

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

将自定义麦克风阵子极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是在 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是在 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

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

### **Element spacing (m)** — 阵列元素之间的间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 的正数值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列元素在本地阵列坐标系中沿此轴均匀分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列的行数和列数相同。
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

| 阵列法向参数值 | 阵元位置和视轴方向 |
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

### **Element positions (m)** — 共形阵列单元的位置 `[0;0;0]`（默认）| 由实数值组成的 3×*N* 矩阵

共形阵列中单元的位置，指定为由实数值组成的 3×*N* 矩阵，其中 *N* 是共形阵列中的单元数。该矩阵的每一列表示阵列局部坐标系中一个阵列单元的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位是米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列单元法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中单元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的单元数。对于矩阵，每一列以相对于局部坐标系的 `[azimuth;elevation]` 形式指定对应单元的法向方向。局部坐标系使正 *x* 轴与共形阵列的法向方向对齐。如果参数值是 2×1 列向量，则所有阵列单元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意一种单元对之间通过某些变换不同的排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法向方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列单元加权 1（默认）| 复数值标量 | 复数值行向量

单元加权，指定为复数值标量或复数值 1×*N* 行向量。在此向量中，*N* 表示阵列中的单元数。

也称为*单元权重*，加权会乘以阵列单元响应。加权会修改响应的幅度和相位，以减少旁瓣或控制主响应轴。

如果 **Taper** 是标量，则对每个单元应用相同的权重。如果 **Taper** 是向量，则将向量中的一个权重应用于对应的传感器单元。权重数量必须与阵列的单元数匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的单元 逻辑矩阵

将子阵列选择指定为 *M*×*N* 矩阵。*M* 是子阵列的数量，*N* 是阵列中单元的总数。矩阵的每一行表示一个子阵列，行中的每个条目指示某个单元何时属于该子阵列。当条目为零时，该单元不属于该子阵列。非零条目表示应用于对应单元的复数值权重。每一行必须至少包含一个非零条目。

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

如果 **Grid size** 是整数标量，则阵列在每行和每列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个条目是沿每列的子阵数量。第二个条目是每行中的子阵数量。行沿局部 *y* 轴方向，列沿局部 *z* 轴方向。此处的图显示了如何使用 **Grid size** 为 `[1,2]` 来复制 3×2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认）| 正实值标量 | 正实值的 1×2 向量

子阵的矩形网格间距，指定为正实值标量、正实值的 1×2 行向量或 `Auto`。单位为米。

- 如果 **Grid spacing** 是标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 是 1×2 行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个条目指定沿列的行间距。第二个条目指定沿行的列间距。
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
子阵数量。矩阵的每一列以
`[azimuth;elevation]` 形式指定对应子阵的法线方向。角度
单位为度。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray
normals** 参数来表示子阵对之间通过某些变换产生差异的任何排列。这些变换可以组合
平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法线旋转的
变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为
`Replicated subarray`，并将 **Subarrays
layout** 设置为 `Custom`。

## 所属库

Phased Array System Toolbox / Space-Time Adaptive Processing

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

采样矩阵求逆 (SMI) 波束形成器

SMI Beamformer 模块实现采样矩阵求逆 (SMI)
空时自适应波束形成器，使用采样空时协方差矩阵。
