---
type: simulink-block
title: 'ULA MVDR Spectrum'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'ulamvdrspectrum'
documentation_source_path: 'ref/ulamvdrspectrum.html'
language: zh-CN
chinese_source: worker-translation
---

# ULA MVDR Spectrum

## 端口

**注意**

模块的输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `In` | 输入信号。输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。 | 双精度浮点 |
| `Ang` | 估计的侧射 DOA 角度。 | 双精度浮点 |
| `Y` | 估计的空间谱。 | 双精度浮点 |

## 参数

**Signal Propagation speed (m/s)**
:   将信号的传播速度指定为正标量，单位为米每秒。您可以使用函数 `physconst` 来指定光速。

**Operating frequency (Hz)**
:   将系统的工作频率指定为正标量，单位为赫兹。

**Number of bits in phase shifters**
:   用于量化波束成形器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

**Forward-backward averaging**
:   选择此参数以使用前向-后向平均来估计具有共轭对称阵列流形的传感器阵列的协方差矩阵。

**Spatial smoothing**
:   将空间平滑用于估计协方差矩阵的平均量 *L* 指定为非负整数。平滑每增加一次可处理一个额外的相干源，但有效阵元数减少一个。此参数的最大值为 *N – 2*，其中 *N* 是传感器数量。

**Scan angles (deg)**
:   将扫描角度指定为实数向量，单位为度。角度为侧射角，必须在 –90° 到 90° 之间（含端点）。您必须按递增顺序指定角度。

**Enable DOA output**
:   选择此参数以通过 **Ang** 输出端口输出信号的到达方向（DOA）。选择此参数会启用 **Number of signals** 参数。

**Number of signals**
:   将 DOA 估计的信号数量指定为正标量整数。当您选中 **Enable DOA output** 复选框时，此参数会出现。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    当您在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行得更快。您可以重复执行而无需重新编译。但是，如果您更改任何模块参数，则模块会在执行前自动重新编译。

    设置此参数时，您必须考虑整体模型仿真模式。下表显示了 **Simulate using** 参数如何与整体仿真模式交互。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
    | `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

    有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

### 数组参数

**将传感器阵列指定为**
:   直接指定 ULA 传感器阵列，或通过 MATLAB 表达式指定。

    **类型**

    |  |
    | --- |
    | `Array (no subarrays)` |
    | `MATLAB expression` |

**阵元数**
:   以整数形式指定阵列中的阵元数。

**阵元间距**
:   指定阵列中两个相邻阵元之间的间距，单位为米。

**阵列轴**
:   当 **Geometry** 参数设置为 `ULA` 时，或当该模块仅支持 ULA 阵列几何结构时，将显示此参数。将阵列轴指定为 `x`、`y` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀分布。

**锥削**
:   锥削，也称为*阵元权重*，应用于阵列中的传感器阵元。锥削用于修改发射或接收数据的幅度和相位。

    将阵元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数。如果 **Taper** 为标量，则对每个阵元应用相同的权重。如果 **Taper** 为向量，则将向量中的权重应用于对应的传感器阵元。必须对传感器阵列中的每个阵元应用权重。

**表达式**
:   一个有效的 MATLAB 表达式，包含均匀线阵的构造函数，例如 `phased.ULA`。

### 传感器阵列选项卡：阵元参数

**阵元类型**
:   将天线或麦克风类型指定为

    - `Isotropic Antenna`
    - `Cosine Antenna`
    - `Custom Antenna`
    - `Omni Microphone`
    - `Custom Microphone`

**余弦方向图指数**
:   当您将**阵元类型**设置为 `Cosine Antenna` 时，此参数出现。

    将余弦方向图的指数指定为标量或 1×2 向量。您必须将所有值指定为非负实数。当您将**余弦方向图指数**设置为标量时，方位方向余弦方向图和俯仰方向余弦方向图都将提升到指定值。当您将**余弦方向图指数**设置为 1×2 向量时，第一个元素是方位方向余弦方向图的指数，第二个元素是俯仰方向余弦方向图的指数。

**工作频率范围 (Hz)**
:   当**阵元类型**设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone` 时，此参数出现。

    将天线阵元的工作频率范围（以赫兹为单位）指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。天线阵元在指定频率范围之外没有响应。

**工作频率向量 (Hz)**
:   当**阵元类型**设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数出现。

    将用于设置天线和麦克风频率响应的频率（以 Hz 为单位）指定为 1×*L* 行向量，其值递增。使用**频率响应**来设置频率响应。天线或麦克风阵元在**工作频率向量 (Hz)** 的最小和最大元素指定的频率范围之外没有响应。

**频率响应 (dB)**
:   当**阵元类型**设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数出现。

    将此参数指定为天线或麦克风的频率响应（以分贝为单位），对应于**工作频率向量 (Hz)** 定义的频率。将**频率响应 (dB)** 指定为与**工作频率向量 (Hz)** 中指定的向量维度匹配的 1×*L* 向量。

**输入方向图坐标系**
:   自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用**方位角 (deg)** 和**俯仰角 (deg)** 参数来指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数来指定方向图点的坐标。

**方位角 (deg)**
:   当**阵元类型**设置为 `Custom Antenna` 且**输入方向图坐标系**参数设置为 `az-el` 时，此参数出现。

    将用于计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。角度单位为度。方位角必须介于 –180° 和 180° 之间，并且严格递增。

**俯仰角 (deg)**
:   当**阵元类型**设置为 `Custom Antenna` 且**输入方向图坐标系**参数设置为 `az-el` 时，此参数出现。

    将用于计算辐射方向图的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须介于 –90° 和 90° 之间，并且严格递增。

**Phi 角 (deg)**
:   当**阵元类型**设置为 `Custom Antenna` 且**输入方向图坐标系**参数设置为 `phi-theta` 时，此参数出现。

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

当该天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使单元坐标系的 *x* 轴指向阵列法线方向。不选中时使用未旋转的单元方向图。

当该天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使单元坐标系的 *z* 轴指向阵列法线方向。

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

    选中此复选框以对天线单元背面加障板。在这种情况下，天线对偏离 *broadside* 超过 ±90° 的所有方位角的响应均设置为零。将 broadside 方向定义为 0° 方位角和 0° 仰角。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

ULA 的 MVDR 空间谱估计器

ULA MVDR Spectrum 模块通过使用窄带最小方差无失真响应（MVDR）波束形成器对均匀线性阵列的 broadside 角度区域进行扫描，来估计入射窄带信号的空间谱。该模块可选地通过估计频谱峰值来计算指定数量信号的到达方向（DOA）。MVDR DOA 估计器也称为 Capon DOA 估计器。
