---
type: simulink-block
title: 'Angle Doppler Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'angledopplerresponse'
documentation_source_path: 'ref/angledopplerresponse.html'
language: zh-CN
chinese_source: worker-translation
---

# Angle Doppler Response

## 端口

### 输入

### **X** — 输入数据 *M*×*N* 复值矩阵 | *M\*N* 元素复值向量

输入信号，指定为 *M*×*N* 复值矩阵或 *M\*N* 复值向量。*M* 是阵元数量或子阵数量（如果阵列支持子阵），在 **Sensor Array** 面板中指定。*N* 是数据样本数。*N* 必须大于或等于二。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `double`
**复数支持：** 是

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as** 参数设置为 `Input port`。

**数据类型：** `double`

### **El** — 仰角 标量

仰角，指定为标量。角度单位为度。仰角必须介于 –90° 和 90° 之间（含边界值）。

#### 依赖关系

要启用此端口，请将 **Source of elevation angle** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Resp** — 角度-多普勒响应 *P*×*Q* 复值矩阵

角度多普勒响应，返回为 *P*×*Q* 矩阵。*P* 由 **Number of Doppler bins** 参数指定，*Q* 由 **Number of angle bins** 参数指定。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 响应矩阵角度值 *Q*×1 实值向量

响应矩阵角度值，返回为 *Q*×1 实值向量。角度值对应于角度-多普勒响应矩阵的列。*Q* 由 **Number of angle bins** 参数指定。

**数据类型：** `double`

### **Dop** — 响应矩阵多普勒值 *P*×1 实值向量

响应矩阵多普勒值，返回为 *P*×1 实值向量。多普勒值对应于角度-多普勒响应矩阵的行。*P* 由 **Number of Doppler bins** 参数指定。

**数据类型：** `double`

## 参数

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Specify PRF as** — PRF 值来源 `Property`（默认）| `Input port`

PRF 值来源，指定为 `Property` 或 `Input port`。当指定为 `Property` 时，**Pulse repetition frequency (Hz)** 参数设置 PRF。当设置为 `Input port` 时，通过 `PRF` 输入端口传入 PRF。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1`（默认）| 正标量

脉冲重复频率，PRF，指定为正标量。单位为赫兹。将此参数设置为仿真中使用的任何 `Waveform` 库模块中设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为 `Property`。

### **Source of elevation angle** — 仰角来源 `Property`（默认）| `Input port`

仰角来源，指定为 `Property` 或 `Input port`。此参数的值为

|  |  |
| --- | --- |
| `Property` | 此模块的 **Elevation angle (deg)** 参数指定仰角。 |
| `Input port` | 仰角使用 `El` 输入端口设置。 |

### **Elevation angle (deg)** — 用于计算角度-多普勒响应的仰角 `0`（默认）| 标量

用于计算角度-多普勒响应的仰角，指定为标量。单位为度。该角度必须介于 –90° 和 90° 之间。

**示例：** `-45`

#### 依赖关系

要启用此参数，请将 **Source of elevation angle** 设置为 `Property`

**数据类型：** `double`

### **Number of angle bins** — 角度样本数 `256`（默认）| 大于 2 的正整数

用于计算角度-多普勒响应的角度域样本数，指定为大于 2 的正整数。

**示例：** `600`

**数据类型：** `double`

### **Number of Doppler bins** — 角度样本数 `256`（默认）| 大于 2 的正整数

用于计算角度-多普勒响应的多普勒域样本数，指定为大于 2 的正整数。

**示例：** `128`

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

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

**示例：** `phased.URA('Size',[5,3])`

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

将设置天线和麦克风频率响应的频率指定为 1×*L* 的递增实值行向量。天线或麦克风单元在此向量的最小和最大元素所指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率处的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 单元或 `Omni Microphone` 单元的后向响应设置为零 关（默认）| 开

选中此复选框以遮挡单元的后向响应。当后向被遮挡时，所有偏离视轴方向 ±90° 以外的方位角处的响应均设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当将此参数设置为标量时，方位角方向和仰角方向的余弦方向图均取相同的幂。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实值行向量

自定义天线或自定义麦克风在 **Operating frequency vector (Hz)** 参数所定义频率处的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数所指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数来指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数来指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

指定用于计算天线辐射方向图的方位角，指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须位于 –180° 到 180° 之间（含端点），并且必须严格递增。

#### 依赖

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

指定用于计算辐射方向图的仰角，指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须位于 –90° 到 90° 之间（含端点），并且必须严格递增。

#### 依赖

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

用于指定天线辐射方向图的点的 Phi 角，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须位于 0° 到 360° 之间，并且必须严格递增。

#### 依赖

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

用于指定天线辐射方向图的点的 Theta 角，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须位于 0° 到 360° 之间，并且必须严格递增。

#### 依赖

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为
*Q*×*P* 矩阵或
*Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数
  设置为 `az-el` 时，*Q* 等于
  由 **Elevation angles
  (deg)** 参数指定的向量长度，*P* 等于
  由 **Azimuth angles (deg)**
  参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数
  设置为 `phi-theta` 时，*Q* 等于
  由 **Theta Angles
  (deg)** 参数指定的向量长度，*P* 等于
  由 **Phi Angles (deg)**
  参数指定的向量长度。

量 *L* 等于
**Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P*
  矩阵，则同一方向图应用于 **Operating frequency vector (Hz)**
  参数中指定的*所有*频率。
- 如果该值是
  *Q*×*P*×*L*
  数组，则该数组的每个 *Q*×*P* 页
  为 **Operating frequency vector (** 中指定的*对应*频率
  指定一个方向图。

#### 依赖

要启用此参数，请将 **Element type** 设置为
`Custom Antenna`。

### **MatchArrayNormal** — 将天线阵子旋转至阵列法向 `on`（默认）| `off`

选中此复选框可将天线阵子方向图旋转至与阵列法向对齐。未选中时，阵子方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵子坐标系的 *x* 轴指向阵列法向。未选中时使用未经旋转的阵子方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵子坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

#### 依赖

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或
实值 1×*L* 向量。响应频率位于
**Operating frequency vector (Hz)**
向量指定的频率范围内。

#### 依赖

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 1×*P* 行向量

指定极坐标方向图响应角度，为 1×*P* 向量。这些
角度从麦克风的中心拾音轴测量，必须介于
–180° 和 180° 之间（含端点）。

#### 依赖

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极性响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元极性响应的幅度指定为
*L*×*P* 矩阵。*L* 是在 **Polar pattern frequencies (Hz)** 中指定的频率数量。
*P* 是在 **Polar pattern
angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar
pattern frequencies (Hz)** 中指定的对应频率以及 **Polar
pattern angles (deg)** 中指定的所有角度下测得的极性响应幅度。该响应在
方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0°
方位角和 0° 仰角。极性响应围绕中心轴对称。您可以根据
极性响应构建三维空间中的麦克风响应模式。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为
`Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵元
  位置

### **Number of elements** — 阵列阵元数量 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数量，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated
subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元之间的间距 ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列为正标量 | URA 阵列为由正值组成的 2 元素向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或由正值组成的 1×2 向量。如果 **Element spacing (m)** 是标量，
  则行间距和列间距相等。如果 **Element spacing
  (m)** 是向量，则该向量的形式为
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为
  `Replicated subarray` 时，此参数适用于每个
  子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、
`x` 或 `z`。所有 ULA 阵列
阵元在局部阵列坐标系中沿此轴均匀间隔分布。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为
  `ULA`。
- 当该模块仅支持 ULA
  阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 由正整数组成的 1×2 向量

URA 阵列的维度，指定为正整数或由正整数组成的 1×2 向量。

- 如果 **Array size** 是由正整数组成的 1×2 向量，则该向量的形式为
  `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列具有相同的
  行数和列数。
- 当您将 **Specify sensor array as** 设置为
  `Replicated subarray` 时，此参数适用于每个
  子阵列。

对于 URA，阵列阵元沿最左侧列从上到下进行索引，然后
从左到右继续到下一列。在此
图中，**Array size** 值 `[3,2]` 会创建一个
具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 阵元位置的晶格 `Rectangular`（默认）| `Triangular`

URA 阵元位置的晶格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元沿行和列方向对齐。
- `Triangular` — 将矩形晶格的偶数行阵元向行轴正方向偏移。位移为沿行维度阵元间距的一半。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向 URA 阵列为 `x` 或 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向指向阵列法线方向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量均指向 *x* 轴方向。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量均指向 *y* 轴方向。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量均指向 *z* 轴方向。 |

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中阵元的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的阵元数。该矩阵的每一列表示阵列局部坐标系中一个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列阵元法向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的阵元数。对于矩阵，每一列以 `[azimuth;elevation]` 的形式指定相应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值为 2×1 列向量，则所有阵列阵元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示阵元对之间通过某些变换产生差异的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法线方向旋转的变换。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵元锥削 1（默认）| 复值标量 | 复值行向量

阵元锥削，指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数量。

也称为*阵元权重*，锥削对阵列阵元响应进行加权。锥削修改响应的幅度和相位，以降低旁瓣或调整主响应轴方向。

如果 **Taper** 为标量，则对每个阵元施加相同的权重。如果 **Taper** 为向量，则将向量中的权重施加到对应的传感器阵元。权重数量必须与阵列的阵元数量匹配。

当将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

### **Subarray definition matrix** — 定义属于子阵的阵元 逻辑矩阵

将子阵选择指定为 *M*×*N* 矩阵。*M* 是子阵数量，*N* 是阵列中阵元的总数。矩阵的每一行代表一个子阵，行中的每个条目指示阵元何时属于该子阵。当条目为零时，该阵元不属于该子阵。非零条目表示施加到对应阵元的复值权重。每一行必须至少包含一个非零条目。

每个子阵的相位中心位于子阵几何中心。子阵几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵导向方法 `None`（默认）| `Phase` | `Time`

子阵导向方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 将在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `Steer` 输入端口。

选择 `Custom` 将在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵移相频率 `3.0e8`（默认）| 正实值标量

子阵导向移相器的工作频率，指定为正实值标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵导向移相量化位数 `0`（默认）| 非负整数

子阵导向移相量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认）| `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数来放置子阵。
- 将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数来放置子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认值）

矩形子阵网格大小，指定为正整数或由正整数组成的 1×2 行向量。

如果 **Grid size** 为整数标量，则阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 为形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个元素是沿每一列的子阵数量。第二个元素是每一行中的子阵数量。行沿局部 *y* 轴方向，列沿局部 *z* 轴方向。此处的图展示了如何使用 **Grid size** 为 `[1,2]` 来复制一个 3×2 URA 子阵。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认值） | 正实值标量 | 正实值组成的 1×2 向量

子阵的矩形网格间距，指定为正实值标量、由正实值组成的 1×2 行向量或 `Auto`。单位为米。

- 如果 **Grid spacing** 为标量，则沿行的间距与沿列的间距相同。
- 如果 **Grid spacing** 为 1×2 行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个元素指定沿列方向各行之间的间距。第二个元素指定沿行方向各列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则复制在构建完整阵列时会为行和列保留子阵的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项才可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵的位置 `[0,0;0.5,0.5;0,0]`（默认值） | 3×*N* 实值矩阵

自定义网格中子阵的位置，指定为实 3×*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标以 `[x; y; z]` 的形式表示。单位为米。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量的方向 `[0,0;0,0]`（默认值） | 2×*N* 实矩阵

指定阵列中子阵的法向方向。此参数值为 2×*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列以 `[azimuth;elevation]` 的形式指定对应子阵的法向方向。角度单位为度。角度是相对于局部坐标系定义的。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示子阵对之间通过某些变换而不同的任何排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

## 所属库

Phased Array System Toolbox / Space-Time Adaptive Processing

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

角度-多普勒响应

Angle Doppler Response 模块计算输入信号的角度-多普勒响应。输出响应是一个矩阵，其行表示多普勒 bin，其列表示角度 bin。
