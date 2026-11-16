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

输入信号，指定为 *M*-by-*N*-by-*P* 复值数组。*M* 是距离采样数，*N* 是通道数，*P* 是脉冲数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **Idx** — 距离单元索引正整数

用于计算处理权值的距离单元索引。

**示例：** `1`

**数据类型：** `double`

### **PRF** — 脉冲重复频率正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，将 **将 PRF 指定为** 参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 目标方向 `2`-by-`1` 实值向量

目标方向，指定为 `2`-by-*1* 实值向量。该向量采用 `[AzimuthAngle;ElevationAngle]` 形式。角度单位为度。方位角必须介于 –180° 和 180° 之间（含端点），俯仰角必须介于 –90° 和 90° 之间（含端点）。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，将 **将方向指定为** 参数设置为 `Input port`。

**数据类型：** `double`

### **Dop** — 目标多普勒频率标量

当前脉冲的目标多普勒频率，指定为标量。

#### 依赖关系

当 **输出多普勒前结果** 复选框被清除，并且 **将目标多普勒指定为** 参数设置为 `Input port` 时，此端口出现。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*-by-1 复值向量

处理输出，以 *M*-by-*1* 复值向量形式返回。量 *M* 是输入端口 `X` 中的距离采样数。

**数据类型：** `double`
**复数支持：** Yes

### **W** — 处理权值长度 *N*\**P* 复值向量

处理权值，以长度 *N*\**P* 复值向量形式返回。量 *N* 是通道数，*P* 是脉冲数。当 **将传感器阵列指定为** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，*N* 表示子阵列数。*L* 是在 `Ang` 输入端口或通过 **波束形成方向 (deg)** 参数指定的所需波束形成方向数。每个波束形成方向有一组权值。

#### 依赖关系

要启用此端口，请选中 **启用权值输出** 复选框。

**数据类型：** `double`
**复数支持：** Yes

## 参数

#### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8` (默认) | 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **将 PRF 指定为** — PRF 值的来源 `Property` (默认) | `Input port`

PRF 值的来源，指定为 `Property` 或 `Input port`。当设置为 `Property` 时，**脉冲重复频率 (Hz)** 参数设置 PRF。当设置为 `Input port` 时，使用 `PRF` 输入端口传入 PRF。

### **脉冲重复频率 (Hz)** — 脉冲重复频率 `1` (默认) | 正标量

脉冲重复频率 PRF，指定为正标量。单位为 Hz。将此参数设置为仿真中使用的任何 `Waveform` 库模块中设置的相同值。

#### 依赖关系

要启用此参数，将 **将 PRF 指定为** 参数设置为 `Property`。

### **将方向指定为** — 指定目标方向的来源 `Property` (默认) | `Input port`

指定 STAP 处理器模块的目标方向来自模块参数还是来自 `ANG` 输入端口。此参数的值包括

|  |  |
| --- | --- |
| `Property` | - 对于 ADPCA Canceller 和 DPCA Canceller 模块，目标方向使用 **接收主瓣方向 (deg)** 指定。<br>- 对于 SMI Beamformer 模块，目标方向使用 **目标方向** 指定。<br>这些参数仅在 **将方向指定为** 参数设置为 `Property` 时出现。 |
| `Input port` | 使用 `Ang` 输入端口输入目标方向。此端口仅在 **将方向指定为** 设置为 `Input port` 时出现。 |

### **接收主瓣方向 (deg)** — 阵列主瓣的指向方向 `[0;0]` (默认) | 实值 2-by-1 向量

将接收传感器阵列主瓣的方向指定为实值 2-by-1 向量。方向采用 `[AzimuthAngle; ElevationAngle]` 格式指定。方位角应介于 –180° 和 180° 之间，俯仰角应介于 –90° 和 90° 之间。

**示例：** `[100;-45]`

#### 依赖关系

要启用此参数，将 **将方向指定为** 设置为 `Property`。

### **移相器中的位数** — 相移量化位数 `0` (默认) | 非负整数

用于量化波束形成器或导向矢量权值的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **将目标多普勒指定为** — 目标多普勒的来源 `Property` (默认) | `Input port`

指定 STAP 处理器的目标多普勒值来自此模块的 **目标多普勒 (Hz)** 参数，还是使用 `DOP` 输入端口。对于 ADPCA Canceller 和 DPCA Canceller 模块，**将目标多普勒指定为** 参数仅在 **输出多普勒前结果** 复选框被清除时出现。此参数的值包括

|  |  |
| --- | --- |
| `Property` | 使用模块的 **目标多普勒** 参数指定目标多普勒值。**目标多普勒** 参数仅在 **将目标多普勒指定为** 设置为 `Property` 时出现。 |
| `Input port` | 使用 `Dop` 输入端口指定目标多普勒值。此端口仅在 **将目标多普勒指定为** 设置为 `Input port` 时出现。 |

### **目标多普勒 (Hz)** — STAP 处理器的目标多普勒 `0` (默认) | 标量

STAP 处理器的目标多普勒，指定为标量。

#### 依赖关系

- 要为 SMI Beamformer 模块启用此参数，将 **将目标多普勒指定为** 设置为 `Property`。
- 要为 ADPCA Canceller 和 DPCA Canceller 模块启用此参数，请先清除 **输出多普勒前结果** 复选框。然后将 **将目标多普勒指定为** 参数设置为 `Property`。

### **启用权值输出** — 输出波束形成器权值的选项 off (默认) | on

选中此复选框以从输出端口 `W` 获取波束形成器权值。

### **输出多普勒前结果** — 输出多普勒滤波前的结果 on (默认) | off

选中此复选框以输出多普勒滤波前的结果。清除此复选框以输出多普勒滤波后的处理结果。选中此复选框将移除 **将目标多普勒指定为** 和 **目标多普勒 (Hz)** 参数。

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您开发和调优模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。与解释执行相比，长时间仿真使用生成的代码运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关更多信息，请参阅选择仿真模式 (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **将传感器阵列指定为** — 指定阵列的方法 `Array (no subarrays)` (默认) | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **表达式** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，将 **将传感器阵列指定为** 设置为 `MATLAB expression`。

#### 阵元参数

### **阵元类型** — 阵列阵元类型 `Isotropic Antenna` (默认) | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实值 1-by-2 行向量

将天线或麦克风阵元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1-by-2 行向量。阵元在此频率范围之外无响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，将 **阵元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实值行向量

将用于设置天线和麦克风频率响应的频率指定为递增实数值的 1-by-*L* 行向量。天线或麦克风阵元在此向量的最小和最大元素指定的频率范围之外无响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 在这些频率处设置响应。

### **遮挡阵元背面** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off (默认) | on

选中此复选框以遮挡阵元的背面响应。当背面被遮挡时，距侧射方向超过 ±90° 的所有方位角处的响应均设置为零。侧射方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，将 **阵元类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **余弦方向图指数** — 方位和俯仰余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实值 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实值 1-by-2 矩阵。当 **余弦方向图指数** 为 1-by-2 向量时，第一个元素是方位方向的指数，第二个元素是俯仰方向的指数。将此参数设置为标量时，方位方向和俯仰方向的余弦方向图均被提高到相同幂次。

#### 依赖关系

要启用此参数，将 **阵元类型** 设置为 `Cosine Antenna`。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实值行向量

自定义天线或自定义麦克风在 **工作频率向量 (Hz)** 参数所定义频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **俯仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，将 **阵元类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实值行向量

将用于计算天线辐射方向图的方位角指定为 1-by-*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端点），并且必须严格递增。

#### 依赖关系

要启用此参数，将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **俯仰角 (deg)** — 天线辐射方向图的俯仰角 `[-90:90]` (默认) | 实值行向量

将用于计算辐射方向图的俯仰角指定为 1-by-*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须介于 –90° 和 90° 之间（含端点），并且必须严格递增。

#### 依赖关系

要启用此参数，将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1-by-*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实值 1-by-*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实数值 1-by-*Q* 行向量

指定天线辐射方向图所在点的 Theta 角，指定为实数值 1-by-*Q* 行向量。*Q* 必须大于 2。角度单位是 degrees。Theta 角必须位于 0° 和 360° 之间，并按严格递增顺序排列。

#### 依赖关系

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实数值 *Q*-by-*P* 矩阵 | 实数值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于
  **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于
  **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于
  **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于
  **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则该数组的每个 *Q*-by-*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实数值 *Q*-by-*P* 矩阵 | 实数值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的相位，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于
  **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于
  **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于
  **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于
  **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则该数组的每个 *Q*-by-*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵元方向图旋转至与阵列法向对齐。未选中时，阵元方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴指向阵列法向。未选中则使用未旋转的阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数一起使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实数值标量 | 实数值 1-by-*L* 行向量

极坐标方向图麦克风响应频率，指定为实数值标量或实数值 1-by-*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实数值 -by-*P* 行向量

将极坐标方向图响应角度指定为 1-by-*P* 向量。这些角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实数值 *L*-by-*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*-by-*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。方向图在方位面中测量。在方位面中，仰角为 0° 且中心拾音轴为 0° degrees 方位角和 0° degrees 仰角。极坐标方向图关于中心轴对称。可以根据极坐标方向图构建 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### 数组参数

### **Specify sensor array as** — 阵列类型 `Array (no subarrays)`（默认）| `MATLAB expression`

直接指定 ULA 传感器阵列，或使用 MATLAB 表达式指定。

**类型**

|  |
| --- |
| `Array (no subarrays)` |
| `MATLAB expression` |

### **Number of elements** — U 中的阵列元素数量 `2`（默认）| 大于或等于二的整数

ULA 阵列的阵列元素数量，指定为大于或等于二的整数。

**示例：** `11`

**数据类型：** `double`

### **Element spacing** — ULA 阵元之间的距离 `0.5`（默认）| 正标量

相邻 ULA 阵元之间的距离，指定为正标量。单位是 meters。

**示例：** `1.5`

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列元素在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Taper** — ULA 阵列锥削 `1`（默认）| 复数值向量

锥削，也称为*阵元权重*，应用于阵列中的传感器阵元。锥削用于修改发射或接收数据的幅度和相位。

将阵元锥削指定为复数值标量或复数值 1-by-*N* 行向量。在此向量中，*N* 表示阵列中的阵元数量。如果 **Taper** 是标量，则同一权重应用于每个阵元。如果 **Taper** 是向量，则向量中的权重应用于对应的传感器阵元。传感器阵列中的每个阵元都必须应用一个权重。

**示例：** [0.5;1;0.5]

**数据类型：** `double`
**复数支持：** Yes

### **Expression** — 用于创建 Phased Array System Toolbox 阵列 System object 的 MATLAB 表达式

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

用于均匀线性阵列的位移相位中心阵列 (DPCA) 脉冲对消器

DPCA Canceller 模块使用位移相位中心阵列脉冲对消器对入射到均匀线性阵列上的杂波进行滤波。
