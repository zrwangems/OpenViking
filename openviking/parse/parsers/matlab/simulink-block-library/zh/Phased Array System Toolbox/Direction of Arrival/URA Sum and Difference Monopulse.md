---
type: simulink-block
title: 'URA Sum and Difference Monopulse'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'urasumanddifferencemonopulse'
documentation_source_path: 'ref/urasumanddifferencemonopulse.html'
language: zh-CN
chinese_source: worker-translation
---

# URA Sum and Difference Monopulse

## 端口
```yaml
ports: []
```

**注意**

模块输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `X` | 输入信号。输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。 | 双精度浮点 |
| `Steer` | 到达方向的初始估计。 | 双精度浮点 |
| `Ang` | 到达方向的估计。 | 双精度浮点 |
## 参数
```yaml
parameters: []
```

**Signal Propagation speed (m/s)**
:   将信号的传播速度指定为正标量，单位为米每秒。您可以使用函数 `physconst` 来指定光速。

**Operating frequency (Hz)**
:   将系统的工作频率指定为正标量，单位为赫兹。

**Number of bits in phase shifters**
:   用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行得更快。您可以重复执行而无需重新编译。但是，如果您更改任何模块参数，模块将在执行前自动重新编译。

    设置此参数时，必须考虑整体模型仿真模式。下表显示了 **Simulate using** 参数如何与整体仿真模式交互。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
    | `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

    有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

### 阵列参数

**将传感器阵列指定为**
:   直接指定 ULA 传感器阵列，或使用 MATLAB 表达式指定。

    **类型**

    |  |
    | --- |
    | `Array (no subarrays)` |
    | `MATLAB expression` |

**阵列大小**
:   将阵列大小指定为正整数或 1×2 正整数向量。

    - 如果 **Array size** 是 1×2 向量，则该向量具有
      形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
    - 如果 **Array size** 是整数，则该阵列具有相同的
      行数和列数。

    元素沿列从上到下索引，并从左到右继续到
    下一列。在此图中，**Array size**
    为 `[3,2]` 会生成一个具有三行两列的阵列。

**阵元间距**
:   将阵列的阵元间距指定为 1×2
    向量或标量，单位为米。如果 **Element spacing** 是
    1×2 向量，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumns]`。
    有关这些量的讨论，请参阅 `phased.URA`。如果 **Element
    spacing** 是标量，则行间距和列间距
    相等。

**阵元栅格**
:   将阵元栅格指定为 `Rectangular` 或 `Triangular` 之一。

    - `Rectangular` — 将所有
      阵元沿行和列方向对齐。
    - `Triangular` — 将矩形栅格的
      偶数行阵元向正行
      轴方向偏移。阵元沿行方向偏移
      半个阵元间距的距离。

**阵列法线**，
:   当您将 **Geometry** 设置为
    `URA` 或 `UCA` 时，此参数会出现。将
    **Array normal** 指定为 `x`、
    `y` 或 `z`。所有 URA 和 UCA 阵列
    阵元分别放置在阵列坐标系的
    *yz*、*zx* 或
    *xy* 平面中。

**锥削**
:   锥削，也称为*阵元权重*，
    应用于阵列中的传感器阵元。锥削用于修改
    发射或接收数据的幅度和相位。

    将阵元锥削指定为复值标量或复值 *M*×*N* 矩阵。
    在此矩阵中，*M* 是沿
    *z* 轴的阵元数，*N* 是沿
    *y* 轴的阵元数。*M* 和 *N* 对应于
    **Array size** 矩阵中的 `[NumberofRows, NumberOfColumns]` 值。如果 `Taper` 是
    标量，则对每个阵元应用相同的权重。如果
    **Taper** 的值是矩阵，则将该矩阵中的权重
    应用于对应的传感器阵元。必须对传感器阵列中的每个阵元
    应用权重。

**表达式**
:   一个有效的 MATLAB 表达式，包含
    均匀矩形阵列的构造函数，例如 `phased.URA`。

### 传感器阵列选项卡：阵元参数

**阵元类型**
:   将天线或麦克风类型指定为

    - `Isotropic Antenna`
    - `Cosine Antenna`
    - `Custom Antenna`
    - `Omni Microphone`
    - `Custom Microphone`

**余弦方向图指数**
:   当您将 **阵元类型** 设置为 `Cosine Antenna` 时，此参数出现。

    将余弦方向图的指数指定为标量或 1×2 向量。您必须将所有值指定为非负实数。当您将 **余弦方向图指数** 设置为标量时，方位方向余弦方向图和俯仰方向余弦方向图都将提升到指定值。当您将 **余弦方向图指数** 设置为 1×2 向量时，第一个元素是方位方向余弦方向图的指数，第二个元素是俯仰方向余弦方向图的指数。

**工作频率范围 (Hz)**
:   当 **阵元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone` 时，此参数出现。

    将天线阵元的工作频率范围（以赫兹为单位）指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。天线阵元在指定频率范围之外没有响应。

**工作频率向量 (Hz)**
:   当 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数出现。

    将设置天线和麦克风频率响应所在的频率（以 Hz 为单位）指定为 1×*L* 行向量，其值递增。使用 **频率响应** 设置频率响应。天线或麦克风阵元在 **工作频率向量 (Hz)** 的最小和最大元素指定的频率范围之外没有响应。

**频率响应 (dB)**
:   当 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone` 时，此参数出现。

    将此参数指定为天线或麦克风的频率响应（以分贝为单位），对应于 **工作频率向量 (Hz)** 定义的频率。将 **频率响应 (dB)** 指定为与 **工作频率向量 (Hz)** 中指定的向量维度匹配的 1×*L* 向量。

**输入方向图坐标系**
:   自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **俯仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

**方位角 (deg)**
:   当 **阵元类型** 设置为 `Custom Antenna` 且 **输入方向图坐标系** 参数设置为 `az-el` 时，此参数出现。

    将计算天线辐射方向图所在的方位角指定为 1×*P* 行向量。*P* 必须大于 2。角度单位为度。方位角必须位于 –180° 和 180° 之间，并且严格递增。

**俯仰角 (deg)**
:   当 **阵元类型** 设置为 `Custom Antenna` 且 **输入方向图坐标系** 参数设置为 `az-el` 时，此参数出现。

    将计算辐射方向图所在的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。俯仰角必须位于 –90° 和 90° 之间，并且严格递增。

**Phi 角 (deg)**
:   当 **阵元类型** 设置为 `Custom Antenna` 且 **输入方向图坐标系** 参数设置为 `phi-theta` 时，此参数出现。

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

    - 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

**Phase pattern (dB)**
:   当 **Element type** 设置为 `Custom Antenna` 时，此参数出现。

    组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

    - 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数所指定向量的长度，*P* 等于 **Azimuth angles (deg)** 参数所指定向量的长度。
    - 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数所指定向量的长度，*P* 等于 **Phi Angles (deg)** 参数所指定向量的长度。

    量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

    - 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

    - 如果此参数为 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
    - 如果该值为 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

**MatchArrayNormal**
:   当 **Element type** 设置为 `Custom Antenna` 时，此参数出现。

    选中此复选框可将天线阵元方向图旋转至与阵列法线对齐。未选中时，阵元方向图不旋转。

当该天线用于天线阵列中，且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使单元坐标系的 *x* 轴指向阵列法线方向。不选中时，使用未经旋转的单元方向图。

当该天线用于天线阵列中，且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使单元坐标系的 *z* 轴指向阵列法线方向。

将该参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数配合使用。

**Polar pattern frequencies (Hz)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将极坐标方向图的测量频率指定为 1×*M* 向量。测量频率位于 **Operating frequency vector (Hz)** 参数指定的频率范围内。频率单位为 Hz。

**Polar pattern angles (deg)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将极坐标方向图的测量角度指定为 1×*N* 向量。角度从麦克风的中心拾取轴测量，必须介于 –180° 和 180° 之间（含端点）。

**Polar pattern (dB)**
:   当 **Element type** 设置为 `Custom Microphone` 时，此参数出现。

    将麦克风单元极坐标方向图的幅度指定为 *M*×*N* 矩阵。*M* 是 **Polar pattern frequencies (Hz)** 中指定的测量频率数量。*N* 是 **Polar pattern angles (deg)** 中指定的测量角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极坐标方向图幅度。假设方向图在方位平面内测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。假设极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建麦克风在三维空间中的响应方向图。

**Baffle the back of the element**
:   此复选框仅在 **Element type** 参数设置为 `Isotropic Antenna` 或 `Omni Microphone` 时出现。

    选中此复选框以对天线单元背面加装障板。在这种情况下，天线对偏离*宽边*方向 ±90° 以外的所有方位角的响应均设置为零。将宽边方向定义为 0° 方位角和 0° 仰角。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

URA 的和差单脉冲

URA Sum-and-Difference Monopulse 模块基于和差单脉冲算法的初始猜测，估计均匀矩形阵列（URA）上窄带信号的到达方向。该模块通过将和波束 steering vector 的后半部分进行相位反转来获得差波束 steering vector。
