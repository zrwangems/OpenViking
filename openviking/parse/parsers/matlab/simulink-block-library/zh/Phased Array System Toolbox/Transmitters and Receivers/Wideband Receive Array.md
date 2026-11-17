---
type: simulink-block
title: 'Wideband Receive Array'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'widebandreceivearray'
documentation_source_path: 'ref/widebandreceivearray.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband Receive Array

## 端口

**注意**

模块输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `X` | 到达信号输入端口。输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。 | 双精度浮点 |
| `Ang` | 信号入射方向输入端口。 | 双精度浮点 |
| `W` | 阵列或子阵列权重输入端口。要启用此端口，请选中 **Enable weights input** 复选框。 | 双精度浮点 |
| `WS` | 子阵列阵元权重输入端口。要启用此端口，请从 **Subarray steering method** 下拉菜单中选择 `Custom`。 |  |
| `Steer` | 转向角输入端口。要启用此端口，请从 **Subarray steering method** 下拉菜单中选择 `Phase` 或 `Time`。 | 双精度浮点 |
| `Out` | 收集的信号 | 双精度浮点 |

## 参数

**Signal Propagation speed (m/s)**
:   将信号的传播速度指定为正标量，单位为米每秒。你可以使用函数 `physconst` 来指定光速。

**Inherit sample rate**
:   选中此复选框以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**Sample rate (Hz)**
:   将信号采样率（以赫兹为单位）指定为正标量。此参数仅在未选中 **Inherit sample rate** 参数时显示。

**Assume modulated input**
:   选中此复选框以指示输入信号在载波频率处被解调。

**Carrier frequency**
:   当选中 **Assume modulated input** 复选框时，此参数显示。该参数将载波频率指定为正标量，单位为赫兹。

**Number of subbands**
:   处理子带的数量，指定为正整数。

**Sensor gain measure**
:   传感器增益度量，指定为 `dB` 或 `dBi`。

    - 当将此参数设置为 `dB` 时，输入信号功率按对应方向上的传感器功率方向图（以 dB 为单位）进行缩放，然后进行合并。
    - 当将此参数设置为 `dBi` 时，输入信号功率按对应方向上的方向性方向图（以 dBi 为单位）进行缩放，然后进行合并。当你希望将结果与使用 dBi 指定天线增益的雷达方程计算的值进行比较时，此选项非常有用。使用 `dBi` 选项的计算开销较大，因为它需要对所有方向进行积分以计算传感器的总辐射功率。默认值为 `dB`。

**Enable weights input**
:   选中此复选框以使用输入端口 `W` 指定阵列权重。该输入端口仅在选中此复选框时显示。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果你希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果你希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    当你正在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。你可以快速更改并执行模型。当你对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行得更快。你可以重复执行而无需重新编译。但是，如果你更改了任何模块参数，模块将在执行前自动重新编译。

    设置此参数时，你必须考虑整体模型仿真模式。下表显示了 **Simulate using** 参数如何与整体仿真模式交互。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
    | `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

    有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

### 数组参数

**将传感器阵列指定为**
:   指定传感器阵元或传感器阵列。传感器阵列也可以包含子阵列或为分区阵列。此参数也可以表示为 MATLAB 表达式。

    **类型**

    |  |
    | --- |
    | `Single element` |
    | `Array (no subarrays)` |
    | `Partitioned array` |
    | `Replicated subarray` |
    | `MATLAB expression` |

**几何结构**
:   将阵列几何结构指定为以下之一：

    - `ULA` — 均匀线阵
    - `URA` — 均匀矩形阵
    - `UCA` — 均匀圆阵
    - `Conformal Array` — 任意阵元位置

**阵元数**
:   阵列阵元数。

    阵列阵元数，指定为正整数。当**几何结构**设置为 `ULA` 或 `UCA` 时，此参数出现。如果**传感器阵列**具有 `Replicated subarray` 选项，则此参数适用于子阵列。

**阵列大小**
:   当**几何结构**设置为 `URA` 时，此参数出现。当**传感器阵列**设置为 `Replicated subarray` 时，此参数适用于子阵列。

    将阵列大小指定为正整数或由正整数组成的 1×2 向量。

    - 如果**阵列大小**是 1×2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
    - 如果**阵列大小**是整数，则阵列具有相同的行数和列数。

    对于 URA，阵元沿一列从上到下索引，并从左到右继续到下一列。在此图中，**阵列大小**为 `[3,2]` 会生成一个三行两列的阵列。

**阵元间距 (m)**
:   当**几何结构**设置为 `ULA` 或 `URA` 时，此参数出现。当**传感器阵列**具有 `Replicated subarray` 选项时，此参数适用于子阵列。

    - 对于 `ULA`，将阵列中两个相邻阵元之间的间距（以米为单位）指定为标量。
    - 对于 `URA`，将阵列的阵元间距（以米为单位）指定为 1×2 向量或标量。如果**阵元间距**是 1×2 向量，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumns]`。有关这些量的讨论，请参阅 `phased.URA`。如果**阵元间距**是标量，则行间距和列间距相等。

**阵列轴**
:   当**几何结构**参数设置为 `ULA`，或当该模块仅支持 ULA 阵列几何结构时，此参数出现。将阵列轴指定为 `x`、`y` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀分布。

**阵列法线**，
:   当将**几何结构**设置为 `URA` 或 `UCA` 时，此参数出现。将**阵列法线**指定为 `x`、`y` 或 `z`。所有 URA 和 UCA 阵列阵元分别放置在阵列坐标系的 *yz*、*zx* 或 *xy* 平面中。

**UCA 半径 (m)**
:   均匀圆阵的半径，指定为正标量。单位为米。

    当**几何结构**设置为 `UCA` 时，此参数出现。

**锥削**
:   锥削，也称为*阵元权重*，应用于阵列中的传感器阵元。锥削用于修改发射或接收数据的幅度和相位。

    此参数适用于所有阵列类型，但当将**传感器阵列**设置为 `Replicated subarray` 时，此参数适用于子阵列。

- 对于 `ULA` 或 `UCA`，将阵元锥削指定为复值标量或复值 1×*N* 行向量。在该向量中，*N* 表示阵列中的阵元数量。如果 **Taper** 为标量，则对每个阵元应用相同的权重。如果 **Taper** 为向量，则将向量中的权重应用于对应的传感器阵元。必须为传感器阵列中的每个阵元应用权重。
- 对于 `URA`，将阵元锥削指定为复值标量或复值 *M*×*N* 矩阵。在该矩阵中，*M* 是沿 *z* 轴的阵元数量，*N* 是沿 *y* 轴的阵元数量。*M* 和 *N* 对应于 **Array size** 矩阵中 `[NumberofArrayRows,NumberOfArrayColumns]` 的值。如果 `Taper` 为标量，则对每个阵元应用相同的权重。如果 **Taper** 为矩阵，则将矩阵中的权重应用于对应的传感器阵元。必须为传感器阵列中的每个阵元应用权重。
- 对于 `Conformal Array`，将阵元锥削指定为复值标量或复值 1×*N* 向量。在该向量中，*N* 是由 **Element positions** 向量的大小确定的阵列中的阵元数量。如果 **Taper** 为标量，则对每个阵元应用相同的权重。如果 **Taper** 的值为向量，则将向量中的权重应用于对应的传感器阵元。必须为传感器阵列中的每个阵元应用权重。

**Element lattice**
:   当 **Geometry** 设置为 `URA` 时，此参数出现。当 **Sensor Array** 设置为 `Replicated subarray` 时，此参数应用于子阵列。

    将阵元栅格指定为 `Rectangular` 或 `Triangular`

    - `Rectangular` — 将所有阵元沿行和列方向对齐。
    - `Triangular`— 将矩形栅格的偶数行阵元向正行轴方向偏移。位移为沿行维度的阵元间距的一半。

**Element positions (m)**
:   当 **Geometry** 设置为 `Conformal Array` 时，此参数出现。当 **Sensor Array** 设置为 `Replicated subarray` 时，此参数应用于子阵列。

    将共形阵列阵元的位置指定为 3×*N* 矩阵，其中 *N* 是共形阵列中的阵元数量。**Element positions (m)** 的每一列表示单个阵元在阵列局部坐标系中的位置，形式为 `[x;y;z]`。局部坐标系的原点位于任意点。单位为米。

**Element normals (deg)**
:   当 **Geometry** 设置为 `Conformal Array` 时，此参数出现。当 **Sensor Array** 设置为 `Replicated subarray` 时，此参数应用于子阵列。

    将共形阵列中阵元的法线方向指定为 2×*N* 矩阵或 2×1 列向量，单位为度。变量 *N* 表示阵列中的阵元数量。如果 **Element normals (deg)** 为矩阵，则每一列以 `[azimuth;elevation]` 的形式指定对应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果 **Element normals (deg)** 为 2×1 列向量，则该向量为阵列中的所有阵元指定相同的指向方向。

你可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意一种排列方式，其中成对的元素通过某些变换而不同。你可以组合平移、方位角旋转和俯仰角旋转变换。但是，不能使用需要绕法线旋转的变换。

**Subarray definition matrix**
:   当 **Specify sensor array as** 设置为 `Partitioned array` 时，此参数出现。

    将子阵选择指定为一个 *M*×*N* 矩阵。*M* 是子阵的数量，*N* 是阵列中元素的总数。矩阵的每一行对应一个子阵，行中的每个条目指示某个元素是否属于该子阵。当条目为零时，该元素不属于该子阵。非零条目表示施加到对应元素上的复值权重。每一行必须至少包含一个非零条目。

    每个子阵的相位中心是其几何中心。**Subarray definition matrix** 和 **Geometry** 决定几何中心。

**Subarray steering method**
:   当 **Specify sensor array as** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，此参数出现。

    将子阵导向方法指定为以下之一

    - `None`
    - `Phase`
    - `Time`
    - `Custom`

    选择 `Phase` 或 `Time` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `Steer` 输入端口。

    选择 `Custom` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `WS` 输入端口。

**Phase shifter frequency (Hz)**
:   当您将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并且将 **Subarray steering method** 设置为 `Phase` 时，此参数出现。

    将用于执行子阵导向的移相器工作频率（以赫兹为单位）指定为正标量。

**Number of bits in phase shifters**
:   当您将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并且将 **Subarray steering method** 设置为 `Phase` 时，此参数出现。

    用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

**Subarrays layout**
:   当您将 **Sensor array** 设置为 `Replicated subarray` 时，此参数出现。

    将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

**Grid size**
:   当您将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular` 时，此参数出现。

    矩形子阵网格大小，指定为单个正整数或正整数值的 1×2 行向量。

    如果 **Grid size** 是整数标量，则阵列在每一行和每一列中具有相同数量的子阵。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1×2 向量，则第一个条目是沿每一列的子阵数量。第二个条目是每一行中的子阵数量。行沿局部 *y* 轴，列沿局部 *z* 轴。此处的图显示了如何使用 **Grid size** 为 `[1,2]` 来复制一个 3×2 URA 子阵。

**Grid spacing**
:   当您将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular` 时，此参数出现。

将子阵列的矩形网格间距指定为实值正标量、1×2 行向量或 `Auto`。
网格间距单位以米表示。

- 如果 **Grid spacing** 是标量，
  则沿行的间距与沿列的间距
  相同。
- 如果 **Grid spacing** 是 1×2
  行向量，则该向量的形式为 `[SpacingBetweenRows,SpacingBetweenColumn]`。
  第一个元素指定沿列方向的行间距。
  第二个元素指定沿行方向的列间距。
- 如果 **Grid spacing** 设置为 `Auto`，
  则复制在构建完整阵列时对行和列均保留子阵列的
  阵元间距。此选项仅在您将 **Geometry** 指定为 `ULA` 或 `URA` 时
  可用。

**Subarray positions (m)**
:   当您将 **Sensor array** 设置为 `Replicated
    subarray` 且将 **Subarrays layout** 设置为 `Custom` 时，此参数
    出现。

    将自定义网格中子阵列的位置指定为
    3×*N* 矩阵，其中 *N* 是阵列中的子阵列数量。矩阵的每一列表示
    单个子阵列在阵列局部坐标系中的位置，单位为米。坐标以 `[x;
    y; z]` 的形式表示。

**Subarray normals**
:   当您将 **Sensor array** 参数
    设置为 `Replicated subarray` 且将 **Subarrays
    layout** 设置为 `Custom` 时，此参数出现。

    指定阵列中子阵列的法线方向。
    此参数值为 2×*N* 矩阵，其中 *N* 是
    阵列中的子阵列数量。矩阵的每一列以 `[azimuth;
    elevation]` 的形式指定对应子阵列的法线方向。每个角度均以度为单位，并在
    局部坐标系中定义。

    您可以使用 **Subarray positions** 和 **Subarray
    normals** 参数来表示子阵列对之间通过某些变换产生差异的任意排列。这些变换
    可以组合平移、方位角旋转和俯仰角旋转。
    但是，您不能使用需要绕法线旋转的变换。

**Expression**
:   包含数组构造函数（例如 `phased.URA`）的有效 MATLAB 表达式。

### 传感器阵列选项卡：阵元参数

**Element type**
:   将天线或麦克风类型指定为

    - `Isotropic Antenna`
    - `Cosine Antenna`
    - `Custom Antenna`
    - `Omni Microphone`
    - `Custom Microphone`

**Exponent of cosine pattern**
:   当您将 **Element type** 设置为 `Cosine Antenna` 时，此参数会出现。

    将余弦方向图的指数指定为标量或 1×2 向量。您必须将所有值指定为非负实数。当您将 **Exponent of cosine pattern** 设置为标量时，方位方向余弦方向图和俯仰方向余弦方向图都会提升到指定值。当您将 **Exponent of cosine pattern** 设置为 1×2 向量时，第一个元素是方位方向余弦方向图的指数，第二个元素是俯仰方向余弦方向图的指数。

**Operating frequency range (Hz)**
:   当 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone` 时，此参数会出现。

    将天线阵元的工作频率范围（以赫兹为单位）指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。天线阵元在指定频率范围之外没有响应。

**Operating frequency vector (Hz)**
:   当 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数会出现。

    将用于设置天线和麦克风频率响应的频率（以 Hz 为单位）指定为按递增顺序排列的 1×*L* 行向量。使用 **Frequency responses** 设置频率响应。天线或麦克风阵元在 **Operating frequency vector (Hz)** 的最小和最大元素指定的频率范围之外没有响应。

**Frequency responses (dB)**
:   当 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数会出现。

    将此参数指定为天线或麦克风在 **Operating frequency vector (Hz)** 定义的频率处的频率响应（以分贝为单位）。将 **Frequency responses (dB)** 指定为与 **Operating frequency vector (Hz)** 中指定的向量维度匹配的 1×*L* 向量。

**Input Pattern Coordinate System**
:   自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

**Azimuth angles (deg)**
:   当 **Element type** 设置为 `Custom Antenna` 且 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，此参数会出现。

    将用于计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。角度单位为度。方位角必须位于 –180° 和 180° 之间，并且严格按递增顺序排列。

**Elevation angles (deg)**
:   当 **Element type** 设置为 `Custom Antenna` 且 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，此参数会出现。

    将用于计算辐射方向图的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须位于 –90° 和 90° 之间，并且严格按递增顺序排列。

**Phi Angles (deg)**
:   当 **Element type** 设置为 `Custom Antenna` 且 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，此参数会出现。

**Phi Angles (deg)**
:   当 **Element type** 设置为 `Custom Antenna` 且 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，此参数出现。

    指定天线辐射方向图各点的 Phi 角度，指定为 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角度必须介于 0° 和 360° 之间，并且严格递增。

**Theta Angles (deg)**
:   当 **Element type** 设置为 `Custom Antenna` 且 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，此参数出现。

    指定天线辐射方向图各点的 Theta 角度，指定为 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角度必须介于 0° 和 180° 之间，并且严格递增。

**Magnitude pattern (dB)**
:   当 **Element type** 设置为 `Custom Antenna` 时，此参数出现。

    组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

    - 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
    - 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

    量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

    - 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

**Phase pattern (dB)**
:   当 **Element type** 设置为 `Custom Antenna` 时，此参数出现。

    组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

    - 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
    - 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

    量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

    - 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

    - 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

**MatchArrayNormal**
:   当 **Element type** 设置为 `Custom Antenna` 时，此参数出现。

    选中此复选框可旋转天线单元方向图，使其与阵列法线对齐。未选中时，单元方向图不旋转。

当该天线用于天线阵列中且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使单元坐标系的 *x* 轴指向阵列法线方向。不选中则使用未经旋转的单元方向图。

当该天线用于天线阵列中且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使单元坐标系的 *z* 轴指向阵列法线方向。

将该参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

**Polar pattern frequencies (Hz)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将极坐标方向图的测量频率指定为 1×*M* 向量。测量频率位于 **Operating frequency vector (Hz)** 参数指定的频率范围内。频率单位为 Hz。

**Polar pattern angles (deg)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将极坐标方向图的测量角度指定为 1×*N* 向量。角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

**Polar pattern (dB)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将麦克风单元极坐标方向图的幅度指定为 *M*×*N* 矩阵。*M* 是 **Polar pattern frequencies (Hz)** 中指定的测量频率数量。*N* 是 **Polar pattern angles (deg)** 中指定的测量角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。假设方向图在方位平面内测量。在方位平面中，仰角为 0°，中心拾音轴为 0° 方位角和 0° 仰角。假设极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建麦克风在三维空间中的响应方向图。

**Baffle the back of the element**
:   此复选框仅在 **Element type** 参数设置为 `Isotropic Antenna` 或 `Omni Microphone` 时出现。

    选中此复选框以对天线单元背面加障板。在这种情况下，天线对偏离*正侧*方向 ±90° 以外的所有方位角的响应均设置为零。将正侧方向定义为 0° 方位角和 0° 仰角。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

宽带接收阵列

Wideband Receive Array 模块接收入射到传感器阵列单元上的宽带平面波。该模块将输入信号划分为子带，然后根据入射方向在每个子带中施加相移。随后将得到的子带信号合并以形成输出。
