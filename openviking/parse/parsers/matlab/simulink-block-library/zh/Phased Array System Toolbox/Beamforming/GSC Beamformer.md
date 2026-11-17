---
type: simulink-block
title: 'GSC Beamformer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Beamforming'
documentation_page: 'gscbeamformer'
documentation_source_path: 'ref/gscbeamformer.html'
language: zh-CN
chinese_source: worker-translation
---

# GSC Beamformer

## 端口
```yaml
ports:
- name: X
  summary: 输入信号 *M*×*N* 复值矩阵
  direction: input
  data_types: double
- name: Ang
  summary: 波束形成方向 *2*×*1* 实值向量
  direction: input
  data_types: double
- name: Y
  summary: 波束形成输出 *M*×*1* 复值向量
  direction: output
```

### 输入

### **X** — 输入信号 *M*×*N* 复值矩阵

输入信号，指定为 *M*×*N* 矩阵，
其中 *M* 是数据中的样本数，*N* 是阵元数。

输入矩阵第一维的大小可以变化，
以模拟变化的信号长度。例如，在脉冲
重复频率可变的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 波束形成方向 *2*×*1* 实值向量

波束形成方向，指定为 *2*×*1* 实值向量，形式为
`[AzimuthAngle;ElevationAngle]`。
角度单位为度。方位角必须介于
–180° 和 180° 之间（含边界），俯仰角必须介于
–90° 和 90° 之间（含边界）。角度是相对于阵列的局部坐标系
定义的。

#### 依赖关系

要启用此端口，请将 **Source of beamforming
direction** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*×*1* 复值向量

波束形成输出，以 *M*×*1* 复值向量形式返回。
量 *M* 是信号样本数。
## 参数
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 实值正标量
  group: ''
- name: Inherit sample rate
  summary: 从上游模块继承采样率 on（默认）| off
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认）| 正实值标量
  group: ''
- name: Signal path FIR filter length
  summary: 沿信号路径的 FIR 滤波器长度 1（默认）| 正整数
  group: ''
- name: Adaptive filter step size
  summary: LMS 自适应滤波器步长因子 0.1（默认）| 正标量
  group: ''
- name: Beamforming direction (deg)
  summary: 波束形成方向 2×1 实值向量
  group: ''
- name: Source of beamforming direction
  summary: 波束形成方向的来源 Property（默认）| Input port
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
  summary: 自定义天线或麦克风单元的工作频率范围 [0,1e20]（默认）| 实值行向量
  group: ''
- name: Baffle the back of the element
  summary: 将 Isotropic Antenna 元件或 Omni Microphone 元件的后向响应设置为零 off（默认）| on
  group: ''
- name: Exponent of cosine pattern
  summary: 方位角和仰角余弦方向图的指数 [1.5 1.5]（默认）| 非负标量 | 非负实数值 1×2 矩阵
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
  summary: 天线辐射方向图的仰角 [-90:90]（默认）| 实数值行向量
  group: ''
- name: Phi Angles (deg)
  summary: 自定义天线辐射方向图的 Phi 角坐标 0:360 | 实数值 1×*P* 行向量
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
  summary: 将天线阵子旋转到阵列法向 on（默认）| off
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
  summary: ULA 阵列的阵元间距为 0.5，URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量
  group: ''
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: ''
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 正整数向量
  group: ''
- name: Element lattice
  summary: URA 阵元位置的栅格 Rectangular（默认）| Triangular
  group: ''
- name: Array normal
  summary: 阵列法线方向 URA 阵列为 x，UCA 阵列为 z（默认）| y
  group: ''
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: ''
- name: Element positions (m)
  summary: 共形阵列阵元的位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: ''
- name: Element normals (deg)
  summary: 共形阵列单元法向量方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: ''
- name: Taper
  summary: 阵列单元锥削 1（默认）| 复标量 | 复值行向量
  group: ''
```

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认
值是由
`physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，
使用 **Sample rate (Hz)**
参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选
框。

**数据类型：** `double`

### **Signal path FIR filter length** — 沿信号路径的 FIR 滤波器长度 `1`（默认）| 正整数

信号路径 FIR 滤波器的长度，指定为正整数。
FIR 滤波器是 delta 函数。

### **Adaptive filter step size** — LMS 自适应滤波器步长因子 `0.1`（默认）| 正标量

自适应滤波器步长因子，指定为正标量。该
量除以旁瓣对消路径中的总功率后，
确定 LMS 算法所使用的实际自适应滤波器步长。

### **Beamforming direction (deg)** — 波束形成方向 2×1 实值向量

波束形成方向，指定为 2×1 实值向量，形式为
`[AzimuthAngle;ElevationAngle]`。角度单位为度。方位角必须介于 –180° 和 180° 之间。俯仰角必须介于 –90° 和 90° 之间。角度是相对于阵列的局部坐标
系定义的。

#### 依赖关系

要启用此参数，请将 **Source of beamforming
direction** 参数设置为 `Property`。

### **Source of beamforming direction** — 波束形成方向的来源 `Property`（默认）| `Input port`

波束形成方向的来源，指定为 `Property`
或 `Input port`。当您将 **Source of
beamforming direction** 设置为 `Property` 时，
随后使用 **Beamforming direction
(deg)** 参数设置方向。当您选择 `Input
port` 时，方向由
`Ang` 端口的输入决定。

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

将设置天线和麦克风频率响应的频率指定为 1×*L* 行向量，包含递增的实数值。天线或麦克风单元在此向量的最小值和最大值所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom
Antenna` 或 `Custom Microphone`。使用
**Frequency responses (dB)** 来设置这些频率下的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的后向响应设置为零 off（默认）| on

选中此复选框以对元件的后向响应进行障板处理。当后向被障板时，
所有超出从正侧方向 ±90° 的方位角处的响应均设置为零。正侧方向
定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将
**Element type** 设置为
`Isotropic Antenna` 或
`Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或
非负实数值 1×2 矩阵。当
**Exponent of cosine pattern** 为
1×2 向量时，第一个元素是方位角
方向的指数，第二个元素是
仰角方向的指数。当您将此参数设置为标量时，
方位角方向和仰角方向余弦
方向图均被提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **Element
type** 设置为 `Cosine
Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实数值行向量

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

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实数值行向量

将计算辐射方向图的仰角指定为
1×*Q* 向量。*Q* 必须
大于 2。角度单位为度。仰角必须介于 –90° 和 90° 之间
（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **Element type**
参数设置为 `Custom Antenna`，并将
**Input Pattern Coordinate System**
参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为
实数值 1×*P* 行向量。*P* 必须大于
2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且
严格递增。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角度坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角度，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角度必须介于 0° 和 360° 之间，并且严格按递增顺序排列。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量的长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量的长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量的长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量的长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量的长度。

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

将自定义麦克风阵子极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。方向图在方位平面内测量。在方位平面中，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖关系

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

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — ULA 阵列的阵元间距为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量

相邻阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 正数值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在本地阵列坐标系中沿此轴均匀分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列每一行和每一列中的阵元数量相同。

对于 URA，阵列阵元沿最左侧阵列列从上到下索引，并从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 会创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 阵元位置的栅格 `Rectangular`（默认）| `Triangular`

URA 阵元位置的栅格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元沿行方向和列方向对齐。
- `Triangular` — 将矩形栅格的偶数行阵元向正行轴方向偏移。位移为沿行维度阵元间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向 URA 阵列为 `x`，UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向沿阵列法线方向指向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量沿 *x* 轴指向。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量沿 *y* 轴指向。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元的位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中阵元的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的阵元数量。此矩阵的每一列表示阵列本地坐标系中一个阵列阵元的位置 `[x;y;z]`。本地坐标系的原点是 *(0,0,0)*。单位是米。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列单元法向量方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中单元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的单元数量。如果参数值为矩阵，则每一列以相对于局部坐标系的 `[azimuth;elevation]` 形式指定对应单元的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列单元使用相同的指向方向。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意一种单元对之间通过特定变换产生差异的排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列单元锥削 1（默认）| 复标量 | 复值行向量

将单元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的单元数量。

锥削也称为*单元权重*，它与阵列单元响应相乘。锥削修改响应的幅度和相位，以降低旁瓣或控制主响应轴的方向。

如果 **Taper** 为标量，则对每个单元施加相同的权重。如果 **Taper** 为向量，则将向量中的权重施加到对应的传感器单元。权重的数量必须与阵列的单元数量匹配。

**数据类型：** `double`
## 所属库

Phased Array System Toolbox / Beamforming

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

广义旁瓣消除器

GSC Beamformer 模块实现广义旁瓣消除（GSC）波束形成器。GSC 波束形成器将阵列的入射信号分离，并分别通过常规波束形成器路径和旁瓣消除路径发送。该算法首先将阵列预导向到波束形成方向，然后自适应地选择滤波器权重，以最小化旁瓣消除路径输出的功率。该算法使用最小均方（LMS）来计算自适应权重。最终的波束形成信号是两条路径输出之间的差值。
