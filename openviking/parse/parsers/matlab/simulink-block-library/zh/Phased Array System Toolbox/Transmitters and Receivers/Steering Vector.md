---
type: simulink-block
title: 'Steering Vector'
family: 'transmitters-and-receivers'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'steeringvector'
documentation_source_path: 'ref/steeringvector.html'
language: zh-CN
chinese_source: worker-translation
---

# Steering Vector

## 端口

### 输入

### **Freq** — 阵列工作频率，正标量

阵列工作频率，指定为正标量。单位为 Hz。

#### 依赖关系

要启用此端口，请将 **工作频率源** 参数设置为 `Input port`。

**数据类型：** `double`

### **Ang** — 导向矢量方向 `[0;0]` (默认) | 实值长度-*M* 向量 | 实值 2-by-*M* 矩阵

导向矢量方向，指定为实值长度-*M* 向量或实值 2-by-*M* 矩阵。*M* 是导向方向的数量。

- 当 `Ang` 为 2-by-*M* 矩阵时，矩阵的每一列以 `[azimuth;elevation]` 形式指定空间中的导向方向。方位角必须在 –180° 到 180° 之间，俯仰角必须在 –90° 到 90° 之间。
- 当 `Ang` 为长度-*M* 向量时，其值对应于导向矢量方向的方位角，且俯仰角设置为零。

角度单位为 degrees。

**数据类型：** `double`

### 输出

### **SV** — 导向矢量复值 *N*-by-*M*-by-*L* 数组 | struct

导向矢量，输出为复值 *N*-by-*M*-by-*L* 数组或包含数组的 `struct`。*N* 是相控阵阵元的数量。如果阵列包含子阵，则 *N* 是子阵的数量。*M* 是 `Ang` 参数中指定的导向方向数量。*L* 是 `Freq` 参数中指定的频率数量。

**数据类型：** `double`
**复数支持：** Yes

## 参数

#### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率源** — 工作频率源 `Input port` (默认) | `Property`

工作频率源，指定为 `Input Port` 或 `Property`。当此参数设置为 `Input Port` 时，工作频率使用 `Freq` 输入端口设置。当此参数设置为 `Property` 时，工作频率使用 `Operating frequency (Hz)` 参数设置。

#### 编程使用

|  |
| --- |
| **模块参数：**`FrequencySource` |
| **类型：**char | string |
| **值：**`Input port` | Property |
| **默认值：**Input port |

### **工作频率 (Hz)** — 系统工作频率 `3e8` (默认) | 正实标量

系统工作频率，指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请将 `Source of operating frequency` 参数设置为 `Property`。

#### 编程使用

|  |
| --- |
| **模块参数：**`OperatingFrequency` |
| **类型：**double | single |
| **值：**float |
| **默认值：**`0` |

### **输出共轭导向矢量** — 输出共轭导向矢量 on (默认) | off

选中此复选框可输出共轭导向矢量。否则，导向矢量不共轭。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputConjugate` |
| **类型：**check box |
| **值：**0 | 1 |
| **默认值：**`0` |

### **移相器中的位数** — 移相量化位数 `0` (默认) | 非负整数

用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。该模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行该模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则该模块会在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响总体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **指定传感器阵列的方式** — 指定阵列的方法 `Array (no subarrays)` (默认) | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **表达式** — 用于创建 Phased Array System Toolbox™ 阵列 System object 的 MATLAB 表达式

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **指定传感器阵列的方式** 设置为 `MATLAB expression`。

### **指定传感器阵列的方式** — 指定阵列的方法 `Array (no subarrays)` (默认) | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

#### 阵元参数

### **阵元类型** — 阵列阵元类型 `Isotropic Antenna` (默认) | `Cardioid Antenna` | `Cosine Antenna` | `Custom Antenna` | `Gaussian Antenna` | `Sinc Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下选项之一：

- `Isotropic Antenna`
- `Cardioid Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Gaussian Antenna`
- `Sinc Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实值 1-by-2 行向量

将天线或麦克风阵元的工作频率范围指定为 1-by-2 行向量，形式为 `[LowerBound,UpperBound]`。阵元在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **阻挡阵元背面** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off (默认) | on

选中此复选框可阻挡阵元的背面响应。当背面被阻挡时，所有从侧射方向起超出 ±90° 的方位角处的响应均设置为零。侧射方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **阵元类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **零轴方向** — 零轴方向 `-x` (默认) | `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Cardioid Antenna`。

### **余弦方向图指数** — 方位和俯仰余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实值 1-by-2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实值 1-by-2 矩阵。当 **余弦方向图指数** 为 1-by-2 向量时，第一个元素是方位方向的指数，第二个元素是俯仰方向的指数。当您将此参数设置为标量时，方位方向和俯仰方向余弦方向图均提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Cosine Antenna`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实值行向量

将设置天线和麦克风频率响应的频率指定为递增实值的 1-by-*L* 行向量。天线或麦克风阵元在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 设置这些频率处的响应。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实值行向量

自定义天线或自定义麦克风在 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量维度匹配。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **俯仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实值行向量

将计算天线辐射方向图的方位角指定为 1-by-*P* 行向量。*P* 必须大于 2。方位角必须位于 –180° 到 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **俯仰角 (deg)** — 天线辐射方向图的俯仰角 `[-90:90]` (默认) | 实值行向量

将计算辐射方向图的俯仰角指定为 1-by-*Q* 向量。*Q* 必须大于 2。角度单位为 degrees。俯仰角必须位于 –90° 到 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1-by-*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实值 1-by-*P* 行向量。*P* 必须大于 2。角度单位为 degrees。Phi 角必须位于 0° 到 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1-by-*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实值 1-by-*Q* 行向量。*Q* 必须大于 2。角度单位为 degrees。Theta 角必须位于 0° 到 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (默认) | 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **俯仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果值是 *Q*-by-*P*-by-*L* 数组，则数组的每个 *Q*-by-*P* 页指定 **工作频率向量 (Hz)** 参数中指定的*对应*频率的方向图。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **相位方向图 (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)` (默认) | 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的相位，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **俯仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果值是 *Q*-by-*P*-by-*L* 数组，则数组的每个 *Q*-by-*P* 页指定 **工作频率向量 (** 中指定的*对应*频率的方向图。

#### 依赖关系

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **将阵元法线与阵列法线对齐** — 将阵元法线与阵列法线对齐 on (默认) | off

#### 依赖项

当 **Element type** 设置为 `Custom Antenna` 时，启用此参数。

### **Radiation pattern beamwidth (deg)** — 辐射方向图波束宽度 `[10,10]`（默认）

#### 依赖项

当 **Element type** 设置为 `Gaussian Antenna` 时，启用此参数。

### **Polar pattern frequencies (Hz)** — 极性图麦克风响应频率 1e3（默认） | 实数标量 | 实值 1×*L* 行向量

极性图麦克风响应频率，指定为实数标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极性图响应角度 `[-180:180]`（默认） | 实值 1×*P* 行向量

将极性图响应角度指定为 1×*P* 向量。这些角度从麦克风的中心拾取轴测量，并且必须介于 –180° 和 180° 之间（含端点）。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极性响应 `zeros(1,361)`（默认） | 实值 *L*×*P* 矩阵

将自定义麦克风阵元极性图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极性图幅度。该方向图在方位平面中测量。在方位平面中，俯仰角为 0°，中心拾取轴为 0° 方位角和 0° 俯仰角。极性图围绕中心轴对称。您可以根据极性图构建 3-D 空间中的麦克风响应方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何 `ULA`（默认） | `URA` | `UCA` | `Conformal Array`

阵列几何，指定为以下之一：

- `ULA` — 均匀线性阵列
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数 `2`（对于 ULA 阵列）和 `5`（对于 UCA 阵列）（默认） | 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数，指定为大于或等于 2 的整数。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元之间的间距 `0.5`（对于 ULA 阵列）和 `[0.5,0.5]`（对于 URA 阵列）（默认） | 对于 ULA 或 URA 阵列的正标量 | 对于 URA 阵列的 2 元素正值向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 正值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认） | `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖项

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认） | 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量的形式为 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则该阵列在每一行和每一列具有相同的阵元数。

对于 URA，阵列阵元沿最左侧阵列列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 会创建一个具有三行两列的阵列。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 阵元位置的栅格 `Rectangular`（默认） | `Triangular`

URA 阵元位置的栅格，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 在行和列方向对齐所有阵元。
- `Triangular` — 将矩形栅格中偶数行的阵元朝正行轴方向偏移。位移为沿行维度的阵元间距的一半。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向 `x`（对于 URA 阵列）或 `z`（对于 UCA 阵列）（默认） | `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向沿阵列法线方向指向。

| Array normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面。所有阵元视轴向量沿 *x* 轴指向。 |
| `y` | 阵列阵元位于 *zx* 平面。所有阵元视轴向量沿 *y* 轴指向。 |
| `z` | 阵列阵元位于 *xy* 平面。所有阵元视轴向量沿 *z* 轴指向。 |

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认） | 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认） | 3×*N* 实值矩阵

共形阵列中阵元的位置，指定为 3×*N* 实值矩阵，其中 *N* 是共形阵列中的阵元数。此矩阵的每一列表示阵列局部坐标系中一个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列阵元法线向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法线向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的阵元数。如果参数值是矩阵，则每一列以 `[azimuth;elevation]` 的形式指定对应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值是 2×1 列向量，则所有阵列阵元使用相同的指向方向。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意排列，其中成对阵元通过某些变换而不同。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列阵元加权 1（默认） | 复标量 | 复值行向量

将阵元加权指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数。

也称为 *element weights*，加权会乘以阵列阵元响应。加权会修改响应的幅度和相位，以降低旁瓣或调整主响应轴的方向。

如果 **Taper** 是标量，则对每个阵元应用相同的权重。如果 **Taper** 是向量，则将该向量中的一个权重应用于对应的传感器阵元。权重数必须与阵列的阵元数匹配。

**数据类型：** `double`

## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

Array steering vector

计算给定方向和频率下的阵列导向矢量。
