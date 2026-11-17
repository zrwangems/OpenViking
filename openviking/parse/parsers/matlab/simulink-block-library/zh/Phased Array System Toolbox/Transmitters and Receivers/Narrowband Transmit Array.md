---
type: simulink-block
title: 'Narrowband Transmit Array'
family: 'transmitters-and-receivers'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'narrowbandtransmitarray'
documentation_source_path: 'ref/narrowbandtransmitarray.html'
language: zh-CN
chinese_source: worker-translation
---

# Narrowband Transmit Array

## 端口

### 输入

### **X** — 辐射信号，复数值 *M*×1 向量 | 复数值 *M*×*N* 矩阵

辐射信号，指定为复数值 *M*×1 向量或复数值 *M*×*N* 矩阵。*M* 是信号的长度，*N* 是阵列元素的数量（或当支持子阵时子阵的数量）。

**X 的维度**

| 维度 | 信号 |
| --- | --- |
| *M*×1 向量 | 同一信号从所有阵列元素（或支持子阵时的所有子阵）辐射。 |
| `M-by-N matrix` | 每列对应由对应阵列元素（或支持子阵时的对应子阵）辐射的信号。 |

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 输入实数值 2×*L* 矩阵

信号的辐射方向，指定为实数值 2×*L* 矩阵。每列以 `[AzimuthAngle;ElevationAngle]` 的形式指定一个辐射方向。方位角必须介于 –180° 和 180° 之间（含端值）。俯仰角必须介于 –90° 和 90° 之间（含端值）。单位为度。

**示例：** `[30,20;45,0]`

**数据类型：** `double`

### **W** — 元素或子阵权重 *N*×1 列向量

元素或子阵权重，指定为复数值 *N*×1 列向量，其中 *N* 是阵列元素的数量（或当阵列支持子阵时子阵的数量）。

#### 依赖关系

要启用此端口，请选中 **启用权重输入** 复选框。

**数据类型：** `double`

### **WS** — 子阵元素权重输入端口 复数值 *N*SE×*N* 矩阵 | 1×*N* 元胞数组

子阵元素权重，指定为复数值 *N*SE×*N* 矩阵或 1×*N* 元胞数组，其中 *N* 是子阵的数量。这些权重应用于子阵内的各个元素。

**子阵元素权重**

| 传感器阵列 | 子阵权重 |
| --- | --- |
| Replicated subarray | 所有子阵具有相同的维度和大小。此时，子阵权重形成一个 *N*SE×*N* 矩阵。*N*SE 是每个子阵中的元素数量，*N* 是子阵的数量。`WS` 的每列指定对应子阵的权重。 |
| Partitioned array | 子阵可能不具有相同的维度和大小。在这种情况下，可以将子阵权重指定为
  - 一个
   *N*SE×*N*
   矩阵，其中
   *N*SE 现在
   是最大子阵中的元素数
   量。每列中的前 *Q* 个条目
   是该子阵的元素权重，其中 *Q* 是该子阵中的
   元素数量。
  - 一个 1×*N* 元胞数组。每个
   元胞包含对应子阵的权重列向量。列向量的
   长度等于对应子阵中的元素数量。 |

#### 依赖关系

要启用此端口，请将 `Specify sensor array as` 参数指定为 **Replicated subarray** 或 **Partitioned array**，然后从 **子阵转向方法** 下拉菜单中选择 `Custom`。

**数据类型：** `double`

### **Steer** — 输入实数值 2×1 向量

子阵转向角，指定为长度为 2 的列向量。该向量具有 `[azimuthAngle;elevationAngle]` 形式。方位角必须介于 –180° 和 180° 之间（含端值）。俯仰角必须介于 –90° 和 90° 之间（含端值）。单位为度。

#### 依赖关系

要启用此端口，请从 **子阵转向方法** 下拉菜单中选择 `Phase` 或 `Time`。

**数据类型：** `double`
### 输出

### **Output 1** — 输出复数值 *M*×*L* 矩阵

辐射信号，指定为复数值 *M*×*L* 矩阵，其中 *L* 是 `Ang` 中的辐射角数量。*M* 是输入信号 `X` 的长度。

**数据类型：** `double`

## 参数

### 主选项卡

### **传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 正标量

信号传播速度，指定为实数值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8` (默认) | 正实数值标量

系统工作频率，指定为正标量。单位为 Hz。

### **传感器增益度量** — 指定传感器增益 `dB` (默认) | `dBi`

将传感器增益度量指定为 `dB` 或 `dBi`。

- 当将此参数设置为 `dB` 时，输入信号功率会按对应方向上的传感器功率方向图（以 dB 为单位）进行缩放，然后进行合并。
- 当将此参数设置为 `dBi` 时，输入信号功率会按对应方向上的方向性图（以 dBi 为单位）进行缩放，然后进行合并。当您希望将结果与使用 dBi 指定天线增益的雷达方程计算的值进行比较时，此选项很有用。使用 `dBi` 选项的计算开销较大，因为它需要对所有方向进行积分，以计算传感器的总辐射功率。默认值为 `dB`。

### **启用权重输入** — 启用权重输入 off (默认) | on

选中此复选框以使用输入端口 `W` 指定阵列权重。仅当选中此复选框时，输入端口才会出现。

### **模拟使用** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示 **模拟使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **模拟使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 该模块使用 MATLAB 解释器执行。 | 该模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 该模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

### 传感器阵列选项卡

### **将传感器阵列指定为** — 指定阵列的方法 `Array (no subarrays)` (默认) | `Single element` | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定传感器元素或传感器阵列。传感器阵列也可以包含子阵，或者是分区阵列。此参数也可以表示为 MATLAB 表达式。

**类型**

|  |
| --- |
| `Single element` |
| `Array (no subarrays)` |
| `Partitioned array` |
| `Replicated subarray` |
| `MATLAB expression` |

#### 元素参数

### **元素类型** — 阵列元素类型 `Isotropic Antenna` (默认) | `Cardioid Antenna` | `Cosine Antenna` | `Custom Antenna` | `Gaussian Antenna` | `Sinc Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cardioid Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Gaussian Antenna`
- `Sinc Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风元素的工作频率范围 `[0,1e20]` (默认) | 实数值 1×2 行向量

将天线或麦克风元素的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1×2 行向量。该元素在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **对元素背面加障板** — 将 `Isotropic Antenna` 元素或 `Omni Microphone` 元素的后向响应设置为零 off (默认) | on

选中此复选框可对元素的后向响应加障板。当背面加障板时，与视轴成 ±90° 以外的所有方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **元素类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **零陷轴方向** — 零陷轴方向 `-x` (默认) | `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Cardioid Antenna`。

### **余弦方向图指数** — 方位角和俯仰角余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实数值 1×2 矩阵。当 **余弦方向图指数** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是俯仰角方向的指数。当将此参数设置为标量时，方位角方向和俯仰角方向的余弦方向图都提高到相同的幂。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Cosine Antenna`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风元素的工作频率范围 `[0,1e20]` (默认) | 实数值行向量

将用于设置天线和麦克风频率响应的频率指定为递增实数值的 1×*L* 行向量。天线或麦克风元素在此向量最小和最大元素指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 设置这些频率处的响应。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实数值行向量

自定义天线或自定义麦克风在由 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量的维度匹配。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **方位角 (deg)** 和 **俯仰角 (deg)** 参数指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实数值行向量

将用于计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含端值），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **俯仰角 (deg)** — 天线辐射方向图的俯仰角 `[-90:90]` (默认) | 实数值行向量

将用于计算辐射方向图的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须介于 –90° 和 90° 之间（含端值），并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实数值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实数值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (默认) | 实数值 *Q*×*P* 矩阵 | 实数值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **俯仰角 (deg)** 参数指定的向量的长度，*P* 等于 **方位角 (deg)** 参数指定的向量的长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量的长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量的长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页指定 **工作频率向量 (Hz)** 参数中指定的 *对应* 频率的方向图。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认） | 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页都为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Align element normal with array normal** — 将阵元法线与阵列法线对齐 on（默认） | off

#### 依赖关系

当 **Element type** 设置为 `Custom Antenna` 时，此参数启用。

### **Radiation pattern beamwidth (deg)** — 辐射方向图波束宽度 `[10,10]`（默认）

#### 依赖关系

当 **Element type** 设置为 `Gaussian Antenna` 时，此参数启用。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认） | 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认） | 实值 1×*P* 行向量

指定极坐标方向图响应角度，指定为 1×*P* 向量。这些角度从麦克风的中心拾取轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认） | 实值 *L*×*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。方向图在方位平面内测量。在方位平面内，俯仰角为 0°，中心拾取轴为方位角 0° 和俯仰角 0°。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构造 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认） | `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下各项之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数，对于 ULA 阵列为 `2`，对于 UCA 阵列为 `5`（默认） | 大于或等于 2 的整数

ULA 或 UCA 阵列的阵元数，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Array size** — URA 阵列的维度 `[2,2]`（默认） | 正整数 | 正整数的 1×2 向量

URA 阵列的维度，指定为正整数或正整数的 1×2 向量。

- 如果 **Array size** 是 1×2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列具有相同的行数和列数。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵元沿最左侧列从上到下编制索引，然后从左到右继续到后续列。在此图中，**Array size** 值 `[3,2]` 创建具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element spacing (m)** — 阵列阵元之间的间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认） | ULA 或 URA 阵列的正标量 | URA 阵列的 2 元素正值向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或正值的 1×2 向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认） | `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在本地阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Element lattice** — URA 阵元位置的晶格 `Rectangular`（默认） | `Triangular`

URA 阵元位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元在行方向和列方向上对齐。
- `Triangular` — 将矩形晶格的偶数行阵元向正行轴方向移动。位移量为沿行维度的阵元间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向，对于 URA 阵列为 `x`，对于 UCA 阵列为 `z`（默认） | `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向沿阵列法线方向指向。

| Array Normal Parameter Value | Element Positions and Boresight Directions |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量都沿 *x* 轴指向。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量都沿 *y* 轴指向。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量都沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认） | 正标量

UCA 阵列半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认） | 实数值的 3×*N* 矩阵

共形阵列中阵元的位置，指定为实数值的 3×*N* 矩阵，其中 *N* 是共形阵列中的阵元数。此矩阵的每一列表示阵列本地坐标系中一个阵列阵元的位置 `[x;y;z]`。本地坐标系的原点是 *(0,0,0)*。单位是米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列阵元法线向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法线向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的阵元数。对于矩阵，每一列以 `[azimuth;elevation]` 的形式指定对应阵元相对于本地坐标系的法线方向。本地坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值是 2×1 列向量，则所有阵列阵元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数表示其中成对阵元通过某些变换而不同的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列阵元锥削 1（默认） | 复值标量 | 复值行向量

阵元锥削，指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数。

也称为*阵元权重*，锥削会乘以阵列阵元响应。锥削修改响应的幅度和相位，以降低旁瓣或控制主响应轴。

如果 **Taper** 是标量，则对每个阵元应用相同的权重。如果 **Taper** 是向量，则将向量中的一个权重应用于对应的传感器阵元。权重数必须与阵列的阵元数匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的阵元 逻辑矩阵

将子阵列选择指定为 *M*×*N* 矩阵。*M* 是子阵列数，*N* 是阵列中的阵元总数。矩阵的每一行表示一个子阵列，行中的每个条目指示某个阵元何时属于该子阵列。当条目为零时，该阵元不属于该子阵列。非零条目表示应用于对应阵元的复值权重。每一行必须至少包含一个非零条目。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵列导向方法 `None`（默认） | `Phase` | `Time`

子阵列导向方法，指定为以下各项之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `Steer` 输入端口。

选择 `Custom` 会打开 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上的 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵列移相频率 `3.0e8`（默认） | 正实值标量

子阵列导向移相器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵列导向移相量化位数 `0`（默认） | 非负整数

子阵列导向移相量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵列位置指定 `Rectangular`（默认） | `Custom`

将复制子阵列的布局指定为 `Rectangular` 或 `Custom`。

- 当您将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数放置子阵列。
- 当您将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数放置子阵列。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵列网格的维度 `[1,2]`（默认）

矩形子阵列网格大小，指定为单个正整数或正整数的 1×2 行向量。

如果 **Grid size** 是整数标量，则该阵列在每一行和每一列中具有相等数量的子阵列。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个条目是沿每一列的子阵列数。第二个条目是每一行中的子阵列数。行沿本地 *y* 轴，列沿本地 *z* 轴。此图显示了如何使用 **Grid size** 为 `[1,2]` 复制 3×2 URA 子阵列。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵列之间的间距 `Auto`（默认） | 正实值标量 | 正实值的 1×2 向量

子阵列的矩形网格间距，指定为正实值标量、正实值的 1×2 行向量或 `Auto`。单位为米。

- 如果 **Grid spacing** 是标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 是 1×2 行向量，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个条目指定沿列的行之间的间距。第二个条目指定沿行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则在构建完整阵列时，复制会为行和列保留子阵列的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵列位置 `[0,0;0.5,0.5;0,0]`（默认） | 3×*N* 实值矩阵

自定义网格中子阵列的位置，指定为实 3×*N* 矩阵，其中 *N* 是阵列中的子阵列数。矩阵的每一列表示阵列本地坐标系中单个子阵列的位置。坐标以 `[x; y; z]` 形式表示。单位为米。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量的方向 `[0,0;0,0]`（默认） | 2-by-*N* real matrix

指定阵列中子阵的法向方向。此参数值是一个 2-by-*N* matrix，其中 *N* 是阵列中的子阵数。矩阵的每一列以 `[azimuth;elevation]` 形式指定对应子阵的法向方向。角度单位为 degrees。角度是相对于局部坐标系定义的。

你可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示任何这样的排列：其中成对的子阵通过某些变换而不同。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，你不能使用需要绕法向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Expression** — 用于创建 Phased Array System Toolbox™ array System object 的 MATLAB 表达式

用于创建数组的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox array System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

### **Analyze** — 启动 Sensor Array Analyzer（默认）

点击 **Analyze** 按钮将启动 Sensor Array Analyzer 应用程序。该应用程序允许你检查重要的阵列属性，例如阵列响应和阵列几何。

## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

Narrowband transmit array

Narrowband Transmit Array 模块通过相加每个阵元的远场辐射信号，在阵列的远场中生成窄带平面波。将模块输出视为距阵元或阵列中心参考距离处的场。
