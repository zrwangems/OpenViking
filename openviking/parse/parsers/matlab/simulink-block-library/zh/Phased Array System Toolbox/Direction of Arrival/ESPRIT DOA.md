---
type: simulink-block
title: 'ESPRIT DOA'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'espritdoablock'
documentation_source_path: 'ref/espritdoablock.html'
language: zh-CN
chinese_source: worker-translation
---

# ESPRIT DOA

## 端口

### 输入

### **Port\_1** — 输入信号 *N*×*M* 复数值矩阵

输入信号，指定为 *N*×*M* 复数值矩阵。*N* 对应样本数。*M* 对应数据通道数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，对于脉冲重复频率可变的脉冲波形，大小可能会发生变化。

**数据类型：** `double`

### 输出

### **Ang** — 估计的宽边到达方向角 *M*×1 实数值向量

估计的宽边到达方向角，以 *M*×1 实数值向量返回。单位是 degrees。

**数据类型：** `double`

## 参数

### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实数值正标量

信号传播速度，指定为实数值正标量。光速默认值是 `physconst('LightSpeed')` 返回的值。单位是 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8` (默认) | 正实标量

系统工作频率，指定为正标量。单位是 Hz。

### **信号数量** — 信号数量 `1` (默认) | 正整数标量

将信号数量指定为正整数标量。

### **空间平滑** — 启用空间平滑 `0` (默认) | 非负整数

指定空间平滑用于估计协方差矩阵的平均量，作为非负整数。平滑每增加一，可多处理一个相干源，但有效阵元数减少一。此参数的最大值为 *N – 2*，其中 *N* 是 ULA 中的传感器数量。

### **最小二乘方法类型** — 最小二乘方法类型 `TLS` (默认) | `LS`

指定用于 ESPRIT 的最小二乘方法，为 `TLS` 或 `LS` 之一，其中 `TLS` 指 total least squares，`LS` 指 least squares。

### **前向-后向平均** — 启用前向-后向平均 off (默认) | on

选择此参数以使用前向-后向平均，为具有共轭对称阵列流形结构的传感器阵列估计协方差矩阵。

### **行加权因子** — 行加权因子 `1` (默认)

将信号子空间特征向量的行加权因子指定为正整数标量。此参数控制应用于选择矩阵的权重。大多数情况下，值越高越好。但是，该值绝不能大于 *(N-1)/2*，其中 *N* 是阵列的阵元数。

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都会被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

### 传感器阵列选项卡

### **指定传感器阵列的方式** — 指定阵列的方法 `Array (no subarrays)` (默认) | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

#### 阵元参数

### **阵元类型** — 阵列阵元类型 `Isotropic Antenna` (默认) | `Cardioid Antenna` | `Cosine Antenna` | `Custom Antenna` | `Gaussian Antenna` | `Sinc Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cardioid Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Gaussian Antenna`
- `Sinc Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实数值 1×2 行向量

将天线或麦克风阵元的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1×2 行向量。阵元在此频率范围之外没有响应。频率单位是 Hz。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **遮挡阵元背面** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off (默认) | on

选中此复选框以遮挡阵元的背面响应。背面遮挡后，所有偏离宽边 ±90° 以外的方位角处的响应都设置为零。宽边方向定义为 0° 方位角和 0° 仰角。

#### 依赖项

要启用此复选框，请将 **阵元类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **零点轴方向** — 零点轴方向 `-x` (默认) | `+x` | `+y` | `-y` | `+z` | `-z`

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Cardioid Antenna`。

### **余弦方向图指数** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实数值 1×2 矩阵。当 **余弦方向图指数** 为 1×2 向量时，第一个元素是方位方向上的指数，第二个元素是仰角方向上的指数。将此参数设置为标量时，方位方向和仰角方向的余弦方向图都提高相同的幂。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Cosine Antenna`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风阵元的工作频率范围 `[0,1e20]` (默认) | 实数值行向量

将设置天线和麦克风频率响应的频率指定为递增实数值的 1×*L* 行向量。天线或麦克风阵元在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位是 Hz。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 在这些频率处设置响应。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实数值行向量

自定义天线或自定义麦克风在 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量的维度匹配。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实数值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须位于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖项

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **仰角 (deg)** — 天线辐射方向图的仰角 `[-90:90]` (默认) | 实数值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位是 degrees。仰角必须位于 –90° 和 90° 之间（含端点），并且严格递增。

#### 依赖项

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位是 degrees。Phi 角必须位于 0° 和 360° 之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实数值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实数值 1×*Q* 行向量。*Q* 必须大于 2。角度单位是 degrees。Theta 角必须位于 0° 和 360° 之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **阵元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (默认) | 实数值 *Q*×*P* 矩阵 | 实数值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页为 **工作频率向量 (Hz)** 参数中指定的 *对应* 频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **相位方向图 (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)` (默认) | 实数值 *Q*×*P* 矩阵 | 实数值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页为 **工作频率向量 (** 中指定的 *对应* 频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Antenna`。

### **将阵元法线与阵列法线对齐** — 将阵元法线与阵列法线对齐 on (默认) | off

#### 依赖项

当 **阵元类型** 设置为 `Custom Antenna` 时，此参数启用。

### **辐射方向图波束宽度 (deg)** — 辐射方向图波束宽度 `[10,10]` (默认)

#### 依赖项

当 **阵元类型** 设置为 `Gaussian Antenna` 时，此参数启用。

### **极坐标方向图频率 (Hz)** — 极坐标方向图麦克风响应频率 1e3 (默认) | 实标量 | 实数值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实数值 1×*L* 向量。响应频率位于 **工作频率向量 (Hz)** 向量指定的频率范围内。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Microphone`。

### **极坐标方向图角度 (deg)** — 极坐标方向图响应角度 `[-180:180]` (默认) | 实数值 -by-*P* 行向量

将极坐标方向图响应角度指定为 1×*P* 向量。角度从麦克风的中心拾取轴测量，必须位于 –180° 和 180° 之间（含端点）。

#### 依赖项

要启用此参数，请将 **阵元类型** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极性响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元极性图的幅值指定为 *L*×*P* 矩阵。*L* 是在 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是在 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度下测得的极性图幅值。该图在方位平面中测量。在方位平面中，俯仰角为 0°，并且中心拾音轴为方位角 0°、俯仰角 0°。极性图围绕中心轴对称。您可以根据该极性图构建三维空间中的麦克风响应图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### ULA 参数

### **Number of elements** — U 中的阵元数量 `2`（默认）| 大于或等于 2 的正整数

ULA 阵列的阵元数量，指定为大于或等于 2 的整数。

**示例：** `11`

**数据类型：** `double`

### **Element spacing** — ULA 阵元之间的距离 `0.5`（默认）| 正标量

相邻 ULA 阵元之间的距离，指定为正标量。单位是 meters.

**示例：** `1.5`

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵元在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Taper** — ULA 阵列锥削 `1`（默认）| 复值向量

锥削（也称为*阵元权重*）应用于阵列中的传感器阵元。锥削用于修改所发射或接收数据的幅度和相位。

将阵元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数量。如果 **Taper** 是标量，则对每个阵元应用相同的权重。如果 **Taper** 是向量，则将向量中的一个权重应用于对应的传感器阵元。必须为传感器阵列中的每个阵元应用一个权重。

**示例：** [0.5;1;0.5]

**数据类型：** `double`
**复数支持：** Yes

### **Expression** — 用于创建 Phased Array System Toolbox™ 阵列 System object 的 MATLAB 表达式

用于创建 ULA 阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.ULA('NumElements',13)`

#### 依赖关系

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2014b 中引入**

## 描述

用于 ULA 的 ESPRIT 到达方向（DOA）估计器

ESPRIT DOA 模块使用 ESPRIT 算法估计入射到均匀线性阵列上的指定数量窄带信号的到达方向。
