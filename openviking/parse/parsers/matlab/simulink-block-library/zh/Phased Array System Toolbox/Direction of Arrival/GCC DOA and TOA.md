---
type: simulink-block
title: 'GCC DOA and TOA'
family: 'direction-of-arrival'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'gccdoaandtoa'
documentation_source_path: 'ref/gccdoaandtoa.html'
language: zh-CN
chinese_source: worker-translation
---

# GCC DOA and TOA

## 端口

### 输入

### **Port\_1** — 接收信号 *M*×*N* 复值矩阵

接收信号，输入为 *M*×*N* 复值矩阵。量 *M* 是信号的样本值（快照）数量，*N* 是阵列中的传感器元件数量。对于子阵列，*N* 是子阵列数量。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能发生大小变化。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Ang** — 到达方向 2×1 实数值列向量 | 标量

信号的到达方向，输出为形式为 `[azimuth;elevation]` 的 2×1 实数值列向量。如果阵列为均匀线性阵列，则 `Ang` 是表示侧射角的标量。角度单位是 degrees，相对于阵列的局部坐标系定义。

**数据类型：** `double`

### **Tau** — 到达时延 1×*P* 实数值行向量

到达时延，输出为 1×*P* 实数值行向量。*P* 是从阵列中选择的传感器对数量。

- 当 **传感器对来源** 设置为 `Auto` 时，*P = N - 1*。*N* 是阵列中的元素数量。
- 当 **传感器对来源** 设置为 `Property` 时，*P* 是由 **传感器对** 参数指定的传感器对数量。

时间单位是 seconds。

#### 依赖关系

要启用此端口，请选中 **启用时延输出** 复选框。

**数据类型：** `double`

### **Rxy** — 估计的互相关 (2*M*+1)×*P* 复值矩阵

传感器对之间的估计互相关，输出为 (2*M*+1)×*P* 复值矩阵，其中 *P* 是从阵列中选择的传感器对数量。*M* 是输入信号中的时间样本数。

- 当 **传感器对来源** 设置为 `Auto` 时，*P = N - 1*。*N* 是阵列中的元素数量。`Rxy` 中的列包含第一个传感器与所有其他传感器之间的相关。
- 当 **传感器对来源** 设置为 `Property` 时，*P* 是由 **传感器对** 参数指定的传感器对数量。`Rxy` 中的每列包含对应传感器对的相关。

#### 依赖关系

要启用此端口，请选中 **启用相关输出** 复选框。

**数据类型：** `double`
**复数支持：** Yes

### **Lag** — 时延 *M*×1 实数值列向量

时延，输出为 (2*M*+1)×1 实数值列向量。*M* 是输入信号中的时间样本数。每个时延应用于互相关矩阵中的对应行。

#### 依赖关系

要启用此端口，请选中 **启用相关输出** 复选框。

**数据类型：** `double`

## 参数

### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位是 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **继承采样率** — 从上游模块继承采样率 on (默认) | off

选中此参数以从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **采样率 (Hz)** — 信号采样率 `1e6` (默认) | 正实数值标量

将信号采样率指定为正标量。单位是 Hz。

#### 依赖关系

要启用此参数，请清除 **继承采样率** 复选框。

**数据类型：** `double`

### **传感器对来源** — 传感器对来源 `Auto` (默认) | `Property`

来源

|  |  |
| --- | --- |
| `Property` | 当将此参数设置为 `Property` 时，使用 **传感器对** 参数指定用于计算相关的传感器对。 |
| `Auto` | 当将此参数设置为 `Auto` 时，计算第一个元素与所有其他元素之间的相关。第一个元素用作参考通道。 |

### **传感器对** — 传感器对 `[2;1]` (默认)

传感器对，指定为严格正整数的 2×*M* 矩阵。

#### 依赖关系

仅当将 **传感器对来源** 参数设置为 `Property` 时，此参数才会出现。

### **启用相关输出** — 启用相关输出的选项 off (默认) | on

选中此复选框以输出使用 GCC-PHAT 算法计算的相关以及传感器对之间的对应时延。相关值通过 `Rxy` 端口输出。时延值通过 `Lags` 端口输出。仅当选中 **启用相关输出** 复选框时，这些端口才会出现。清除此复选框可禁用相关输出。

### **启用时延输出** — 启用时延输出的选项 off (默认) | on

选中此复选框以输出对应于每个传感器对之间信号到达角的时延。时延在 `Tau` 端口输出。仅当选中 **启用时延输出** 复选框时，此端口才会出现。清除此复选框可禁用时延输出。

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

下表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

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
| **默认值：** `Interpreted Execution` |

### 传感器阵列选项卡

### **指定传感器阵列方式** — 指定阵列的方法 `Array (no subarrays)` (默认) | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

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

将天线或麦克风元素的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1×2 行向量。该元素在此频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **遮挡元件背面** — 将 `Isotropic Antenna` 元件或 `Omni Microphone` 元件的背面响应设置为零 off (默认) | on

选中此复选框可遮挡元件的背面响应。当背面遮挡时，所有从侧射方向起超过 ±90° 的方位角处的响应均设置为零。侧射方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **元素类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **零陷轴方向** — 零陷轴方向 `-x` (默认) | `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Cardioid Antenna`。

### **余弦方向图指数** — 方位和仰角余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实数值 1×2 矩阵。当 **余弦方向图指数** 为 1×2 向量时，第一个元素是方位方向的指数，第二个元素是仰角方向的指数。将此参数设置为标量时，方位方向和仰角方向的余弦方向图都提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Cosine Antenna`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风元件的工作频率范围 `[0,1e20]` (默认) | 实数值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 行向量，其中元素为递增实数值。天线或麦克风元件在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 设置这些频率处的响应。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实数值行向量

自定义天线或自定义麦克风在由 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。指定 `az-el` 时，使用 **方位角 (deg)** 和 **仰角 (deg)** 参数指定方向图点的坐标。指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实数值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180°（含）之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **仰角 (deg)** — 天线辐射方向图的仰角 `[-90:90]` (默认) | 实数值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位是 degrees。仰角必须介于 –90° 和 90°（含）之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位是 degrees。Phi 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实数值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实数值 1×*Q* 行向量。*Q* 必须大于 2。角度单位是 degrees。Theta 角必须介于 0° 和 360° 之间，并且必须严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (默认) | 实数值 *Q*×*P* 矩阵 | 实数值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页指定 **工作频率向量 (Hz)** 参数中指定的 *对应* 频率的方向图。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| real-valued *Q*-by-*P* matrix | real-valued *Q*-by-*P*-by-*L* array

组合天线辐射方向图的相位，指定为
*Q*-by-*P* 矩阵或
*Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于由 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于由 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于由 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于由 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则数组的每一 *Q*-by-*P* 页为 **Operating frequency vector (Hz)** 中指定的*对应*频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Align element normal with array normal** — 将阵元法线对准阵列法线 on（默认）| off

#### 依赖关系

当 **Element type** 设置为 `Custom Antenna` 时，此参数启用。

### **Radiation pattern beamwidth (deg)** — 辐射方向图波束宽度 `[10,10]`（默认）

#### 依赖关系

当 **Element type** 设置为 `Gaussian Antenna` 时，此参数启用。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| real scalar | real-valued 1-by-*L* row vector

极坐标方向图麦克风响应频率，指定为 real scalar，或
real-valued、1-by-*L* vector。响应频率位于
**Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| real-valued -by-*P* row vector

将极坐标方向图响应角度指定为 1-by-*P* vector。这些角度从麦克风的中心拾音轴测量，且必须介于
–180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| real-valued *L*-by-*P* matrix

将自定义麦克风阵元极坐标方向图的幅度指定为
*L*-by-*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。
*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。该方向图在方位平面中测量。在方位平面中，俯仰角为 0°，中心拾音轴为 0° 方位角和 0° 俯仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建三维空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一：

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列元素数量，对于 ULA 阵列为 `2`，对于 UCA 阵列为 `5`（默认）| integer greater than or equal to 2

ULA 或 UCA 阵列的阵列元素数量，指定为大于或等于 2 的 integer。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| positive integer | 1-by-2 vector of positive integers

URA 阵列的维度，指定为 positive integer 或 1-by-2 vector of positive integers。

- 如果 **Array size** 是 1-by-2 vector，则该向量形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是 integer，则阵列的行数和列数相同。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

对于 URA，阵列元素沿最左列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element spacing (m)** — 阵列元素之间的间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认）| positive scalar for ULA or URA arrays | 2-element vector of positive values for URA arrays

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为 positive scalar。
- URA — 将间距指定为 positive scalar 或 1-by-2 vector of positive values。如果 **Element spacing (m)** 是 scalar，则行间距和列间距相等。如果 **Element spacing (m)** 是 vector，则该向量形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列元素在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Element lattice** — URA 阵元位置的格子 `Rectangular`（默认）| `Triangular`

URA 阵元位置的格子，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有元素沿行和列方向对齐。
- `Triangular` — 将矩形格子的偶数行元素向正行轴方向移动。位移是沿行维度的元素间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向，对于 URA 阵列为 `x`，对于 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的元素位于与所选阵列法线方向正交的平面内。元素波束指向方向沿阵列法线方向。

| Array Normal Parameter Value | 元素位置和波束指向方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz*-平面内。所有元素波束指向向量沿 *x*-轴。 |
| `y` | 阵列元素位于 *zx*-平面内。所有元素波束指向向量沿 *y*-轴。 |
| `z` | 阵列元素位于 *xy*-平面内。所有元素波束指向向量沿 *z*-轴。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| positive scalar

UCA 阵列半径，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认）| 3-by-*N*matrix of real values

共形阵列中元素的位置，指定为 3-by-*N* matrix of real values，其中 *N* 是共形阵列中的元素数量。此矩阵的每一列表示阵列局部坐标系中一个阵列元素的位置 `[x;y;z]`。局部坐标系的原点是 *(0,0,0)*。单位是 meters。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列元素法线向量的方向 `[0;0]` | 2-by-1 column vector | 2-by-*N* matrix

共形阵列中元素法线向量的方向，指定为 2-by-1 column vector 或 2-by-*N* matrix。*N* 表示阵列中的元素数量。对于矩阵，每一列以 `[azimuth;elevation]` 形式指定对应元素相对于局部坐标系的法线方向。局部坐标系将正 *x*-轴与共形阵列的法线方向对齐。如果参数值是 2-by-1 column vector，则所有阵列元素使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数表示任意这样的排列：成对元素之间通过某些变换不同。这些变换可以组合平移、方位旋转和俯仰旋转。但是，不能使用需要绕法线方向旋转的变换。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列元素锥削 1（默认）| complex-valued scalar | complex-valued row vector

元素锥削，指定为 complex-valued scalar 或
complex-valued 1-by-*N* row vector。在此
向量中，*N* 表示阵列中的元素数量。

也称为*元素权重*，锥削乘以阵列元素响应。锥削修改响应的幅度和相位，以降低旁瓣或控制主响应轴。

如果 **Taper** 是 scalar，则每个元素应用相同权重。如果 **Taper** 是 vector，则向量中的一个权重应用于对应传感器元素。权重数量必须与阵列的元素数量匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵列。

### **Subarray definition matrix** — 定义属于子阵列的阵元的 logical matrix

将子阵列选择指定为 *M*-by-*N* 矩阵。*M* 是子阵列数量，*N* 是阵列中元素总数。矩阵的每一行表示一个子阵列，行中的每个条目指示元素何时属于该子阵列。当条目为零时，该元素不属于该子阵列。非零条目表示应用于对应元素的 complex-valued weight。每一行必须至少包含一个非零条目。

每个子阵列的相位中心位于子阵列几何中心。子阵列几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵列控制方法 `None`（默认）| `Phase` | `Time`

子阵列控制方法，指定为以下之一：

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `Steer` 输入端口。

选择 `Custom` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `WS` 输入端口。

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵列相移频率 `3.0e8`（默认）| positive real-valued scalar

子阵列控制移相器的工作频率，指定为 positive real-valued scalar。单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵列控制相移量化位数 `0`（默认）| non-negative integer

子阵列控制相移量化位数，指定为 non-negative integer。值为零表示不执行量化。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵列位置指定 `Rectangular`（默认）| `Custom`

将复制子阵列的布局指定为 `Rectangular` 或 `Custom`。

- 当您将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数放置子阵列。
- 当您将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数放置子阵列。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`。

### **Grid size** — 矩形子阵列网格的维度 `[1,2]`（默认）

矩形子阵列网格大小，指定为单个 positive integer，或 1-by-2 row vector of positive integers。

如果 **Grid size** 是 integer scalar，则阵列在每一行和每一列具有相同数量的子阵列。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 vector，则第一个条目是沿每一列的子阵列数量。第二个条目是每一行中的子阵列数量。行沿局部 *y*-轴，列沿局部 *z*-轴。此处图显示如何使用 **Grid size** `[1,2]` 复制 3-by-2 URA 子阵列。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵列之间的间距 `Auto`（默认）| positive real-valued scalar | 1-by-2 vector of positive real-values

子阵列的矩形网格间距，指定为 positive、real-valued scalar，1-by-2 row vector of positive、real-values，或 `Auto`。单位是 meters。

- 如果 **Grid spacing** 是 scalar，则沿行的间距和沿列的间距相同。
- 如果 **Grid spacing** 是 1-by-2 row vector，则该向量形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个条目指定沿列的行之间的间距。第二个条目指定沿行的列之间的间距。
- 如果 **Grid spacing** 设置为 `Auto`，则复制在构建完整阵列时保留子阵列在行和列两个方向上的元素间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项可用。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Subarray positions (m)** — 子阵列的位置 `[0,0;0.5,0.5;0,0]`（默认）| 3-by-*N* real-valued matrix

自定义网格中子阵列的位置，指定为 real 3-by-*N* 矩阵，其中 *N* 是阵列中的子阵列数量。矩阵的每一列表示阵列局部坐标系中单个子阵列的位置。坐标以 `[x; y; z]` 形式表示。单位是 meters。

#### 依赖关系

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Subarray normals** — 子阵法向量的方向 `[0,0;0,0]`（默认） | 2-by-*N* real matrix

指定阵列中子阵的法向方向。此参数值为一个 2-by-*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列以 `[azimuth;elevation]` 形式指定对应子阵的法向方向。角度单位为 degrees。角度相对于局部坐标系定义。

您可以使用 **Subarray positions** 和 **Subarray normals** 参数来表示任意排列，其中成对的子阵通过某些变换而彼此不同。这些变换可以组合平移、方位角旋转和仰角旋转。但是，不能使用需要绕法线旋转的变换。

#### 依赖关系

要启用此参数，请将 **Sensor array** 参数设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Custom`。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ array System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox array System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2015b 中引入**

## 描述

带相位变换的广义互相关器

GCC DOA and TOA 模块估计信号在阵列处的到达方向与到达时间。该模块使用带相位变换的广义互相关 *(GCC-PHAT)* 算法。
