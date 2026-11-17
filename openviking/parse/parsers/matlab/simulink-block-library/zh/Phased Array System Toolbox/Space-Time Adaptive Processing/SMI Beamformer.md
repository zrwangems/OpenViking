---
type: simulink-block
title: 'SMI Beamformer'
family: 'space-time-adaptive-processing'
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

### **X** — 输入信号 *M*×*N*×*P* 复数值矩阵

输入信号，指定为 *M*×*N*×*P* 复数值数组。*M* 是距离样本数，*N* 是通道数，*P* 是脉冲数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **Idx** — 距离单元索引 正整数

用于计算处理权值的距离单元索引。

**示例：** `1`

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 目标方向 `2`×`1` 实数值向量

目标方向，指定为 `2`×*1* 实数值向量。该向量的形式为 `[AzimuthAngle;ElevationAngle]`。角度单位为度。方位角必须介于 –180° 和 180° 之间（含两端），俯仰角必须介于 –90° 和 90° 之间（含两端）。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，请将 **Specify direction as** 参数设置为 `Input port`。

**数据类型：** `double`

### **Dop** — 目标 Doppler 频率 标量

当前脉冲的目标 Doppler 频率，指定为标量。

#### 依赖关系

要启用此端口，请将 **Specify targeting Doppler as** 参数设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 波束形成输出 *M*×1 复数值向量

处理输出，返回为 *M*×*1* 复数值向量。量 *M* 是输入端口 `X` 中的距离样本数。

**数据类型：** `double`
**复数支持：** Yes

### **W** — 处理权值 长度 *N*\**P* 复数值向量

处理权值，返回为长度 *N*\**P* 复数值向量。量 *N* 是通道数，*P* 是脉冲数。当 **Specify sensor array as** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，*N* 表示子阵列数。*L* 是在 `Ang` 输入端口中或通过 **Beamforming direction (deg)** 参数指定的所需波束形成方向数。每个波束形成方向有一组权值。

#### 依赖关系

要启用此端口，请选中 **Enable weights output** 复选框。

**数据类型：** `double`
**复数支持：** Yes

## 参数

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认） | 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位是米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认） | 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Specify PRF as** — PRF 值的来源 `Property`（默认） | `Input port`

PRF 值的来源，指定为 `Property` 或 `Input port`。当设置为 `Property` 时，**Pulse repetition frequency (Hz)** 参数设置 PRF。当设置为 `Input port` 时，使用 `PRF` 输入端口传入 PRF。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1`（默认） | 正标量

脉冲重复频率，PRF，指定为正标量。单位为 Hertz。将此参数设置为仿真中使用的任何 `Waveform` 库模块中设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为 `Property`。

### **Specify direction as** — 指定目标方向的来源 `Property`（默认） | `Input port`

指定 STAP processor 模块的目标方向来自模块参数还是 `ANG` 输入端口。此参数的值为

|  |  |
| --- | --- |
| `Property` | - 对于 ADPCA Canceller 和 DPCA Canceller 模块，目标方向使用 **Receiving mainlobe direction (deg)** 指定。 - 对于 SMI Beamformer 模块，目标方向使用 **Targeting direction** 指定。 仅当 **Specify direction as** 参数设置为 `Property` 时，这些参数才会出现。 |
| `Input port` | 使用 `Ang` 输入端口输入目标方向。仅当 **Specify direction as** 设置为 `Input port` 时，此端口才会出现。 |

### **Targeting direction (deg)** — 处理器目标方向 `[0;0]`（默认） | 实数值长度为 2 的列向量

处理器目标方向，指定为方位角和俯仰角的实数值长度为 2 的列向量，`[AzimuthAngle;ElevationAngle]`。方位角介于 –180° 和 180° 之间，俯仰角介于 –90° 和 90° 之间。单位为度。

#### 依赖关系

要启用此参数，请将 **Specify direction as** 设置为 `Property`。

### **Number of bits in phase shifters** — 移相器中的位数 `0`（默认） | 非负整数

用于量化波束形成器或导向矢量权值的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **Specify targeting Doppler as** — 目标 Doppler 的来源 `Property`（默认） | `Input port`

指定 STAP processor 的目标 Doppler 值来自此模块的 **Targeting Doppler (Hz)** 参数，还是使用 `DOP` 输入端口。对于 ADPCA Canceller 和 DPCA Canceller 模块，仅当清除 **Output pre-Doppler result** 复选框时，**Specify targeting Doppler as** 参数才会出现。此参数的值为

|  |  |
| --- | --- |
| `Property` | 使用模块的 **Targeting Doppler** 参数指定目标 Doppler 值。仅当 **Specify targeting Doppler as** 设置为 `Property` 时，**Targeting Doppler** 参数才会出现。 |
| `Input port` | 使用 `Dop` 输入端口指定目标 Doppler 值。仅当 **Specify targeting Doppler as** 设置为 `Input port` 时，此端口才会出现。 |

### **Targeting Doppler (Hz)** — STAP processor 的目标 Doppler `0`（默认） | 标量

STAP processor 的目标 Doppler，指定为标量。

#### 依赖关系

- 要为 SMI Beamformer 模块启用此参数，请将 **Specify targeting Doppler as** 设置为 `Property`。
- 要为 ADPCA Canceller 和 DPCA Canceller 模块启用此参数，请先清除 **Output pre-Doppler result** 复选框。然后将 **Specify targeting Doppler as** 参数设置为 `Property`。

### **Number of guard cells** — 用于训练的保护单元数 `2`（默认） | 正偶数整数

用于训练的保护单元数，指定为正偶数整数。在可能的情况下，保护单元集被等分为测试单元之前和之后的区域。

### **Number of training cells** — 用于训练的单元数 `2`（默认） | 正偶数整数

用于训练的单元数，指定为正偶数整数。在可能的情况下，训练单元集被等分为测试单元之前和之后的区域。

### **Enable weights output** — 输出波束形成器权值的选项 off（默认） | on

选中此复选框可从输出端口 `W` 获取波束形成器权值。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以在不重新编译的情况下重复执行，但如果更改任何模块参数，模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **Specify sensor array as** — 指定传感器阵列的方法 `Array (no subarrays)`（默认） | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ array System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### 阵元参数

### **Element type** — 阵列阵元类型 `Isotropic Antenna`（默认） | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认） | 实数值 1×2 行向量

将天线或麦克风阵元的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1×2 行向量。阵元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]`（默认） | 实数值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 行向量，其中包含递增的实数值。天线或麦克风阵元在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off（默认） | on

选中此复选框以遮挡阵元的背面响应。背面遮挡时，所有偏离视轴 ±90° 以外的方位角处的响应都设置为零。视轴方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和俯仰角余弦方向图的指数 `[1.5 1.5]`（默认） | 非负标量 | 由非负值组成的实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或由非负值组成的实数值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是俯仰角方向的指数。当您将此参数设置为标量时，方位角方向和俯仰角方向余弦方向图都提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认） | 实数值行向量

自定义天线或自定义麦克风在 **Operating frequency vector (Hz)** 参数定义的频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认） | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认） | 实数值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含两端），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的俯仰角 `[-90:90]`（默认） | 实数值行向量

将计算辐射方向图的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须介于 –90° 和 90° 之间（含两端），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta 角度 (deg)** — 自定义天线辐射方向图的 Theta 角度坐标 `0:180` | real-valued 1×*Q* row vector

指定天线辐射方向图的点的 Theta 角度，指定为 real-valued 1×*Q* row vector。*Q* 必须大于 2。角度单位为 degrees。Theta 角度必须位于 0° 到 360° 之间，并且按严格递增顺序排列。

#### 依赖关系

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| real-valued *Q*×*P* matrix | real-valued *Q*×*P*×*L* array

组合天线辐射方向图的幅度，指定为 *Q*×*P* matrix 或 *Q*×*P*×*L* array。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角度 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角度 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* matrix，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* array，则该数组的每个 *Q*×*P* 页为 **工作频率向量 (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **相位方向图 (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| real-valued *Q*×*P* matrix | real-valued *Q*×*P*×*L* array

组合天线辐射方向图的相位，指定为 *Q*×*P* matrix 或 *Q*×*P*×*L* array。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角度 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角度 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* matrix，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* array，则该数组的每个 *Q*×*P* 页为 **工作频率向量 (** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法线 `on`（默认）| `off`

选中此复选框可将天线阵元方向图旋转到与阵列法线对齐。未选中时，阵元方向图不旋转。

当天线用于天线阵列且 **输入方向图坐标系** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x*-轴指向阵列法线方向。不选中则使用未旋转的阵元方向图。

当天线用于天线阵列且 **输入方向图坐标系** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z*-轴指向阵列法线方向。

将此参数与 `URA` 和 `UCA` 阵列的 **阵列法线** 参数结合使用。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **极坐标方向图频率 (Hz)** — 极坐标方向图麦克风响应频率 `1e3`（默认）| real scalar | real-valued 1×*L* row vector

极坐标方向图麦克风响应频率，指定为 real scalar 或 real-valued 1×*L* vector。响应频率位于 **工作频率向量 (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Microphone`。

### **极坐标方向图角度 (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| real-valued -by-*P* row vector

将极坐标方向图响应角度指定为 1×*P* vector。角度从麦克风的中心拾音轴测量，并且必须介于 –180° 和 180° 之间（含端值）。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Microphone`。

### **极坐标方向图 (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| real-valued *L*×*P* matrix

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*×*P* matrix。*L* 是 **极坐标方向图频率 (Hz)** 中指定的频率数量。*P* 是 **极坐标方向图角度 (deg)** 中指定的角度数量。矩阵的每一行表示在 **极坐标方向图频率 (Hz)** 中指定的对应频率以及 **极坐标方向图角度 (deg)** 中指定的所有角度处测得的极坐标方向图幅度。该方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。可以根据极坐标方向图在 3-D 空间中构造麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Microphone`。

#### 阵列参数

### **几何结构** — 阵列几何 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何，指定为以下之一

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **阵元数量** — 阵列阵元数量 `2`（对于 ULA 阵列）和 `5`（对于 UCA 阵列）（默认）| integer greater than or equal to 2

ULA 或 UCA 阵列的阵列阵元数量，指定为大于或等于 2 的 integer。

当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `ULA` 或 `UCA`。

### **阵元间距 (m)** — 阵列阵元之间的间距 `0.5`（对于 ULA 阵列）和 `[0.5,0.5]`（对于 URA 阵列）（默认）| positive scalar（对于 ULA 或 URA 阵列）| 2-element vector of positive values（对于 URA 阵列）

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为 positive scalar。
- URA — 将间距指定为 positive scalar 或 1×2 vector of positive values。如果 **阵元间距 (m)** 是 scalar，则行间距和列间距相等。如果 **阵元间距 (m)** 是 vector，则该 vector 的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `ULA` 或 `URA`。

### **阵列轴** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在本地阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **几何结构** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **阵列大小** — URA 阵列的维度 `[2,2]`（默认）| positive integer | 1×2 vector of positive integers

URA 阵列的维度，指定为 positive integer 或 1×2 vector of positive integers。

- 如果 **阵列大小** 是 1×2 vector，则该 vector 的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **阵列大小** 是 integer，则该阵列具有相同的行数和列数。
- 当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列阵元沿最左列从上到下索引，然后从左到右继续到下一列。在此图中，**阵列大小** 值为 `[3,2]` 会创建具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA`。

### **阵元点阵** — URA 阵元位置的点阵 `Rectangular`（默认）| `Triangular`

URA 阵元位置的点阵，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元沿行和列方向对齐。
- `Triangular` — 将矩形点阵的偶数行阵元向正行轴方向移动。位移为沿行维度的阵元间距的一半。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA`。

### **阵列法线** — 阵列法线方向 `x`（对于 URA 阵列）或 `z`（对于 UCA 阵列）（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元轴视方向指向阵列法线方向。

| 阵列法线参数值 | 阵元位置和轴视方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元轴视向量指向 *x*-轴。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元轴视向量指向 *y*-轴。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元轴视向量指向 *z*-轴。 |

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `URA` 或 `UCA`。

### **UCA 半径 (m)** — UCA 阵列半径 `0.5`（默认）| positive scalar

UCA 阵列半径，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `UCA`。

### **阵元位置 (m)** — 共形阵列阵元的位置 `[0;0;0]`（默认）| 3×*N* matrix of real values

共形阵列中阵元的位置，指定为 3×*N* matrix of real values，其中 *N* 是共形阵列中的阵元数量。此矩阵的每一列表示阵列本地坐标系中阵列阵元的位置 `[x;y;z]`。本地坐标系的原点是 *(0,0,0)*。单位为 m。

当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `Conformal Array`。

### **阵元法线 (deg)** — 共形阵列阵元法线向量的方向 `[0;0]` | 2×1 column vector | 2×*N* matrix

共形阵列中阵元法线向量的方向，指定为 2×1 column vector 或 2×*N* matrix。*N* 表示阵列中的阵元数量。对于 matrix，每一列以 `[azimuth;elevation]` 形式指定对应阵元相对于本地坐标系的法线方向。本地坐标系将正 *x*-轴与共形阵列的法线方向对齐。如果参数值是 2×1 column vector，则所有阵列阵元使用相同的指向方向。

当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

可以使用 **阵元位置 (m)** 和 **阵元法线 (deg)** 参数表示任意排列，其中阵元对之间通过某些变换不同。这些变换可以组合平移、方位角旋转和仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **几何结构** 设置为 `Conformal Array`。

### **锥削** — 阵列阵元锥削 `1`（默认）| complex-valued scalar | complex-valued row vector

阵元锥削，指定为 complex-valued scalar 或 complex-valued 1×*N* row vector。在此 vector 中，*N* 表示阵列中的阵元数量。

也称为阵元权重，锥削会乘以阵列阵元响应。锥削修改响应的幅度和相位，以减少旁瓣或操纵主响应轴。

如果 **锥削** 是 scalar，则对每个阵元应用相同权重。如果 **锥削** 是 vector，则 vector 中的权重应用于对应传感器阵元。权重数量必须与阵列的阵元数量匹配。

当将 **指定传感器阵列为** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **子阵列定义矩阵** — 定义属于子阵列的阵元 logical matrix

将子阵列选择指定为 *M*×*N* matrix。*M* 是子阵列数量，*N* 是阵列中阵元总数。矩阵的每一行表示一个子阵列，行中的每一项指示阵元何时属于该子阵列。当项为零时，该阵元不属于该子阵列。非零项表示应用于对应阵元的 complex-valued 权重。每行必须至少包含一个非零项。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **子阵列定义矩阵** 和 **几何结构** 参数。

#### 依赖关系

要启用此参数，请将 **指定传感器阵列为** 设置为 `Partitioned array`。

### **子阵列转向方法** — 指定子阵列转向方法 `None`（默认）| `Phase` | `Time`

子阵列转向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **指定传感器阵列为** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **移相器频率 (Hz)** — 子阵列移相频率 `3.0e8`（默认）| positive real-valued scalar

子阵列转向移相器的工作频率，指定为 positive real-valued scalar。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **传感器阵列** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **子阵列转向方法** 设置为 `Phase`。

### **移相器中的位数** — 子阵列转向相移量化位数 `0`（默认）| non-negative integer

子阵列转向相移量化位数，指定为 non-negative integer。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **传感器阵列** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **子阵列转向方法** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认） | `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认）

矩形子阵网格大小，指定为单个 positive integer，或 positive integers 的 1-by-2 row vector。

如果 **Grid size** 是 integer scalar，则阵列在每行和每列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 vector，则第一个元素是沿每列的子阵数量。第二个元素是每行的子阵数量。行沿局部 *y* 轴，列沿局部 *z* 轴。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 复制一个 3-by-2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认） | positive real-valued scalar | 1-by-2 vector of positive real-values

子阵的矩形网格间距，指定为 positive, real-valued scalar、positive, real-values 的 1-by-2 row vector 或 `Auto`。单位为 meters。

- 如果 **Grid spacing** 是 scalar，则沿行的间距和沿列的间距相同。
- 如果 **Grid spacing** 是 1-by-2 row vector，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个元素指定沿某一列的行之间的间距。第二个元素指定沿某一行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则在构建完整阵列时，复制会为行和列保留子阵的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵的位置 `[0,0;0.5,0.5;0,0]`（默认） | 3-by-*N* real-valued matrix

自定义网格中子阵的位置，指定为 real 3-by-*N* matrix，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标以 `[x; y; z]` 形式表示。单位为 meters。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向向量的方向 `[0,0;0,0]`（默认） | 2-by-*N* real matrix

指定阵列中子阵的法向方向。此参数值是 2-by-*N* matrix，其中 *N* 是阵列中的子阵数量。矩阵的每一列以 `[azimuth;elevation]` 形式指定对应子阵的法向方向。角度单位为 degrees。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示任意排列，其中成对的子阵通过某些变换而不同。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

## 所属库

Phased Array System Toolbox / Space-Time Adaptive Processing

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

采样矩阵求逆（SMI）波束形成器

SMI Beamformer 模块实现采用采样空时协方差矩阵的采样矩阵求逆（SMI）空时自适应波束形成器。
