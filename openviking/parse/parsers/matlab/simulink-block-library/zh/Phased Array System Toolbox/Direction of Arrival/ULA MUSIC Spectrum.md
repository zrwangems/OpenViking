---
type: simulink-block
title: 'ULA MUSIC Spectrum'
family: 'direction-of-arrival'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'ulamusicspectrum'
documentation_source_path: 'ref/ulamusicspectrum.html'
language: zh-CN
chinese_source: worker-translation
---

# ULA MUSIC Spectrum

## 端口

### 输入

### **Port 1** — 接收信号，*M*×*N* 复值矩阵

接收信号，指定为 *M*×*N* 复值矩阵。量 *M* 是信号中包含的样本值（快拍）数，*N* 是阵列中的传感器阵元数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能发生大小变化。

**数据类型：** `double`
**复数支持：** 是
### 输出

### **Y** — MUSIC 空间谱，非负实值列向量

MUSIC 空间谱，返回为非负实值列向量，表示估计的 MUSIC 空间谱的幅度。每个条目对应于 **Scan angles (deg)** 参数指定的角度。

**数据类型：** `double`

### **Ang** — 到达方向，非负实值列向量

信号的到达方向，返回为实值行向量。到达方向角是源方向与阵列轴之间的侧射角。向量长度是由 `Number of signals` 参数指定的信号数。如果对象无法识别频谱中的峰值，它将返回 `NaN`。角度单位为 degrees。

#### 依赖项

选择 **Enable DOA output** 参数以启用此输出端口。

**数据类型：** `double`

## 参数

#### 主选项卡

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为 m/s。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Forward-backward averaging** — 启用前向-后向平均 off（默认）| on

选择此参数以使用前向-后向平均来估计具有共轭对称阵列流形结构的传感器阵列的协方差矩阵。

### **Spatial smoothing** — 启用空间平滑 `0`（默认）| 非负整数

指定空间平滑用于估计协方差矩阵的平均量，指定为非负整数。平滑每增加一次，可处理一个额外的相干源，但有效阵元数减少一。此参数的最大值为 *N* – 2，其中 *N* 是 ULA 中的传感器数。

### **Scan angles (deg)** — 频谱峰值的搜索角度 `-90:90`（默认）| 实值行向量

以度为单位将扫描角度指定为实值行向量。角度是阵列侧射角，必须介于 –90° 和 90°（含）之间。必须以递增顺序指定角度。

### **Enable DOA output** — 通过输出端口输出到达方向 off（默认）| on

选择此参数以通过 **Ang** 输出端口输出信号的到达方向（DOA）。

### **Number of signals** — 预期到达信号数 `1`（默认）| 正整数

将 DOA 估计的预期信号数指定为正标量整数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

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
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块
  参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖项

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### 阵元参数

### **Element type** — 阵元类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或传声器类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **Operating frequency range (Hz)** — 天线或传声器阵元的工作频率范围 `[0,1e20]`（默认）| 实值 1×2 行向量

将天线或传声器阵元的工作频率范围指定为形式为 `[LowerBound,UpperBound]` 的 1×2 行向量。该阵元在此频率范围之外无响应。频率单位为 Hz。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **Operating frequency vector (Hz)** — 自定义天线或传声器阵元的工作频率范围 `[0,1e20]`（默认）| 实值行向量

将设置天线和传声器频率响应的频率指定为 1×*L* 行向量，其中包含递增的实值。天线或传声器阵元在此向量最小和最大元素指定的频率范围之外无响应。频率单位为 Hz。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **Frequency responses (dB)** 设置这些频率下的响应。

### **Baffle the back of the element** — 将 `Isotropic Antenna` 阵元或 `Omni Microphone` 阵元的背面响应设置为零 off（默认）| on

选择此复选框可对元件的背面响应进行挡板。当背面挡板时，所有方位角超过偏离侧射 ±90° 的响应设置为零。侧射方向定义为 0° 方位角和 0° 仰角。

#### 依赖项

要启用此复选框，请将 **Element type** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **Exponent of cosine pattern** — 方位角和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 非负值的实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实值 1×2 矩阵。当 **Exponent of cosine pattern** 为 1×2 向量时，第一个元素是方位角方向的指数，第二个元素是仰角方向的指数。当将此参数设置为标量时，方位角方向和仰角方向余弦方向图都提升到相同幂。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Cosine Antenna`。

### **Frequency responses (dB)** — 天线和传声器频率响应 `[0,0]`（默认）| 实值行向量

由 **Operating frequency vector (Hz)** 参数定义的频率处自定义天线或自定义传声器的频率响应。**Frequency responses (dB)** 的维度必须与 **Operating frequency vector (Hz)** 参数指定的向量维度匹配。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **Input Pattern Coordinate System** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当指定 `az-el` 时，使用 **Azimuth angles (deg)** 和 **Elevations angles (deg)** 参数指定方向图点的坐标。当指定 `phi-theta` 时，使用 **Phi angles (deg)** 和 **Theta angles (deg)** 参数指定方向图点的坐标。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Azimuth angles (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180°（含）之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Elevation angles (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为 degrees。仰角必须介于 –90° 和 90°（含）之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `az-el`。

### **Phi Angles (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位为 degrees。Phi 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Theta Angles (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为 degrees。Theta 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖项

要启用此参数，请将 **Element type** 参数设置为 `Custom Antenna`，并将 **Input Pattern Coordinate System** 参数设置为 `phi-theta`。

### **Radiation pattern (dB)** — 自定义天线辐射方向图 `zeros(181,361)` | 复值矩阵 | 复值 MATLAB 数组

组合极化天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。*Q* 的值必须等于由 **Elevation angles (deg)** 指定的 *Q* 的值。*P* 的值必须等于由 **Azimuth angles (deg)** 指定的 *P* 的值。*L* 的值必须等于由 **Operating frequency vector (Hz)** 指定的 *L* 的值。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Magnitude pattern (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页为 **Operating frequency vector (Hz)** 参数中指定的*对应*频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页为 **Operating frequency vector (** 中指定的*对应*频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线单元旋转到阵列法向 `on`（默认） | `off`

选中此复选框可将天线单元方向图旋转到与阵列法向对齐。未选中时，不旋转单元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使天线单元坐标系的 *x* 轴沿阵列法向指向。未选中时使用未旋转的单元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使天线单元坐标系的 *z* 轴沿阵列法向指向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极性图麦克风响应频率 1e3（默认） | 实数标量 | 实值 1-by-*L* 行向量

极性图麦克风响应频率，指定为实数标量或实值 1-by-*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极性图响应角度 `[-180:180]`（默认） | 实值 -by-*P* 行向量

将极性图响应角度指定为 1-by-*P* 向量。角度从麦克风的中心拾音轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极性响应 `zeros(1,361)`（默认） | 实值 *L*-by-*P* 矩阵

指定自定义麦克风单元极性图的幅度，指定为 *L*-by-*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测量的极性图幅度。该极性图在方位平面中测量。在方位平面中，仰角为 0°，中心拾音轴为方位角 0°、仰角 0°。极性图绕中心轴对称。可以根据极性图构造 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Number of elements** — U 中阵列单元数 `2`（默认） | 大于或等于 2 的正整数

ULA 阵列的阵列单元数，指定为大于或等于 2 的整数。

**示例：** `11`

**数据类型：** `double`

### **Element spacing** — ULA 单元之间的距离 `0.5`（默认） | 正标量

相邻 ULA 单元之间的距离，指定为正标量。单位为 meters。

**示例：** `1.5`

### **Array axis** — ULA 的线性轴方向 `y`（默认） | `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。然后，所有 ULA 阵列单元在局部阵列坐标系中沿此轴均匀间隔。

### **Taper** — 阵列单元锥削 1（默认） | 复值标量 | 复值行向量

指定单元锥削为复值标量或复值 1-by-*N* 行向量。在此向量中，*N* 表示阵列中的单元数。

也称为 *element weights*，锥削会乘以阵列单元响应。锥削修改响应的幅度和相位，以减少旁瓣或引导主响应轴。

如果 **Taper** 是标量，则对每个单元应用相同的权重。如果 **Taper** 是向量，则将向量中的一个权重应用于对应的传感器单元。权重数必须与阵列的单元数匹配。

**数据类型：** `double`

## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

ULA 的 MUSIC 空间谱估计器

ULA MUSIC Spectrum 模块使用 MUSIC 算法估计入射窄带信号的空间谱。该算法通过扫描宽边角区域来计算 ULA 的 MUSIC 伪谱。该模块通过估计谱峰，可选地计算指定数量信号的到达方向 (DOA)。
