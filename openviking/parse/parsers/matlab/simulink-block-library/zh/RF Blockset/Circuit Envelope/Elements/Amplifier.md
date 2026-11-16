---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'amplifier'
documentation_source_path: 'ref/amplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Amplifier

## 端口

R2025b 中未记录。

## 参数

### 主

### **放大器增益源** — 放大器增益源 `Available power gain` (default) | `Open circuit voltage gain` | `Data source` | `Polynomial coefficients` | `AM/AM-AM/PM table`

放大器增益源，指定为以下之一：

- `Available power gain` —
  该模块使用 **可用功率增益** 参数计算 *a1*，即多项式 VCVS 的线性电压增益项。此计算假定放大器为匹配负载端接。
- `Open circuit voltage gain`
  — 该模块使用 **开路电压增益** 参数计算 *a1*，即多项式 VCVS 的线性电压增益项。
- `Data source` — 该模块使用 **数据源** 参数计算线性电压增益。当您使用数据源选项时，该模块使用 *S*11 和 *S*22 作为输入和输出阻抗。
- `Polynomial coefficients`
  — 该模块使用 **多项式系数** 参数计算非线性电压增益。
- `AM/AM-AM/PM table` — 该模块使用 **AM/AM-AM/PM 表** 参数确定放大器的功率特性。

### **可用功率增益** — 可用功率增益 0 `dB` (default) | scalar

放大器的可用功率增益，指定为 dB 标量。
从相应的下拉列表中指定单位。

#### 依赖项

要启用此参数，请在 **放大器增益源** 选项卡中选择 `Available power
gain`。

### **开路电压增益** — 开路电压增益 0 `dB` (default) | scalar

放大器的开路电压，指定为 dB 标量。
从相应的下拉列表中指定单位。

#### 依赖项

要启用此参数，请在 **放大器增益源** 选项卡中选择 `Open circuit voltage
gain`。

### **数据源** — 数据源 `Data File` (default) | `Network-parameters` | `Rational Model`

数据源，指定为以下之一：

- `Data file` — 扩展名为`.s2p` 的 Touchstone 文件的名称。
- `Network-parameters` —
  提供 **网络参数** 数据，例如
  `S-parameters`、
  `Y-parameters` 和
  `Z-parameters`，并带有放大器的相应 **频率** 和
  **参考阻抗 (ohms)**。
- `Rational model` — 为 **留数**、
  **极点** 和 **直接
  馈通** 参数提供值，这些参数对应于有理模型方程

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  在此有理模型方程中，每个
  *Ck* 是极点
  *Ak* 的留数。如果
  *Ck* 是复数，则还必须枚举相应的复共轭极点和留数。此对象具有属性
  `C`、`A` 和
  `D`。您可以使用这些属性指定 **留数**、
  **极点** 和 **直接
  馈通** 参数。

当放大器为非线性时，非线性仅适用于表示 2 端口元件的散射参数的 S21 项。在这种情况下，S21 与频率无关，其常数值为用户指定的工作频率处的 S21 值或 S21 的最大值。其他散射参数 S11、S12 和 S22 与线性情况相同。

#### 依赖项

要启用此参数，请在 **放大器增益源** 选项卡中选择 `Data
source`。

### **多项式系数** — 多项式系数 `[0 1]` (default) | vector

多项式的阶数，指定为向量。

多项式的阶数必须小于或等于 9。系数按升幂排序。如果向量有 10 个系数，
`[a0,a1,a2,
... a9]`，
则其表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

其中
*a*1 表示线性增益项，高阶项根据 [1] 建模。

例如，向量
`[a0,a1,a2,a3]`
指定关系 *Vout* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3。尾随零被省略。因此，
`[a0,a1,a2]`
定义的多项式与
`[a0,a1,a2,
0]` 相同。此参数的默认值为 [0,1]，
对应于线性关系
*Vout* =
*Vin*。

#### 依赖项

要启用此参数，请在 **放大器增益源** 选项卡中选择 `Polynomial
coefficients`。

### **AM/AM-AM/PM 表** — 查找表 `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]` (default) | *M*-by-3 real matrix

表查找条目，指定为实数 *M*×3 矩阵。矩阵的第二列表示 AM/AM–AM/PM 模型的输出功率，单位为 dBm。第三列表示模型相位变化，单位为度。第二列和第三列的值与矩阵第一列表示的输入信号功率的绝对值相关。第一列中的输入功率必须单调递增。

#### 依赖项

要启用此参数，请将 **放大器增益源** 设置为 `AM/AM - AM/PM
table`。

### **网络参数对象** — 网络参数对象作为数据源 `off` (default) | `on`

选择此参数以使用网络参数对象作为放大器增益源。

选择此参数后，在打开的文本框中指定以下之一：

- 网络参数对象。
- MATLAB® 基础工作区变量或 Simulink® 模型工作区变量。如果指定的变量是网络参数对象，则该模块会对其进行计算。

您可以指定的网络参数对象包括：

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择
`Network-parameters`。

### **网络参数类型** — 网络参数类型 `S-parameters` (default) | `Y-parameters` | `Z-parameters`

网络参数类型，指定为 `S-parameters`、
`Y-parameters` 或
`Z-parameters`。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择
`Network-parameters`。

### **输入阻抗 (Ohm)** — 输入阻抗 `50` (default) | positive scalar

放大器的输入阻抗，指定为以欧姆为单位的正标量。

#### 依赖项

要启用此参数，请在 **放大器增益源** 中选择 `Available power
gain`、`Open circuit voltage
gain` 或 `Polynomial
coefficients`。

### **输出阻抗 (Ohm)** — 输出阻抗 `50` (default) | positive scalar

放大器的输出阻抗，指定为以欧姆为单位的正标量。

#### 依赖项

要启用此参数，请在 **放大器增益源** 中选择 `Available power
gain`、`Open circuit voltage
gain` 或 `Polynomial
coefficients`。

### **数据文件** — 网络参数数据文件的名称 `unitygain.s2p` (default) | character vector

网络参数数据文件的名称，指定为字符向量。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择 `Data
file`。

### **频率 (dB)** — 网络参数的频率 `1e9 Hz` (default) | scalar | `Hz` | `kHz` | `MHz` | `GHz`

网络参数的频率，指定为 Hz 标量。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择
`Network-parameters`。

### **参考阻抗(Ohm)** — 网络参数的参考阻抗 `50` (default) | positive scalar | vector of positive scalars

网络参数的参考阻抗，指定为以欧姆为单位的正标量或正标量向量。

**注意**

当您将其指定为正标量向量时，所有端口的参考阻抗必须相等。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择
`Network-parameters`。

### **使用有理对象** — 有理对象作为数据源 `off` (default) | `on`

选择此参数以使用 `rational` 对象作为数据源来建模放大器增益。

选择此参数后，在打开的文本框中指定以下之一：

- `rational` 对象。
- MATLAB 基础工作区变量或 Simulink 模型工作区变量。如果指定的变量是有理对象，则该模块会对其进行计算。"

您可以指定的 `rational` 对象包括：

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择 `Rational
model`。

### **留数** — 有理模型顺序中的留数 `0` (default) | vector

有理模型顺序中的留数，指定为向量。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择 `Rational
model`。

### **极点** — 有理模型顺序中的留数 `0` (default) | vector

有理模型顺序中的极点，指定为向量。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择 `Rational
model`。

### **直接馈通** — 直接馈通 `{0 0:1 0}` (default) | array of vectors

直接馈通，指定为数组向量。

#### 依赖项

要启用此参数，请先在 **放大器增益源** 中选择 `Data
source`，然后在 **数据源** 中选择 `Rational
model`。

### **接地并隐藏负端子** — 将 RF 电路端子接地 `on` (default) | `off`

选择此选项以将负端子接地并隐藏。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

### 非线性

### **非线性多项式类型** — 非线性类型 `Even and odd order` (default) | `Odd order`

非线性类型，指定为 `Even and odd
order` 或 `Odd order`。

- 当您选择 `Even and odd order` 时，
  除了线性项之外，放大器还可以产生二阶和三阶互调频率。
- 当您选择 `Odd order` 时，
  放大器仅产生奇阶互调频率。

  线性增益决定线性
  *a*1 项。该模块根据指定的参数计算其余项。
  这些参数为 **IP3**、**1-dB
  增益压缩功率**、**输出
  饱和功率** 和 **饱和时的
  增益压缩**。您指定的约束数量决定模型的阶数。该图显示了非线性放大器参数的图形定义。

  Po vs. Pi 图表示非线性放大器参数。

### **截点约定** — 截点约定 `Output` (default) | `Input`

截点约定，指定为
`Input` 参考或
`Output` 参考约定。将此规范用于截点、1-dB 增益压缩功率和饱和功率。

### **IP2** — 二阶截点 `inf``dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

二阶截点，指定为标量。

#### 依赖项

要设置此参数，请在 **非线性多项式类型** 中选择 `Even and odd
order`。

### **IP3** — 三阶截点 `inf``dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

三阶截点，指定为标量。

### **1-dB 增益压缩功率** — 1-dB 增益压缩功率 `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

1-dB 增益压缩功率，指定为标量。

#### 依赖项

要设置此参数，请在 **非线性多项式类型** 中选择 `Odd order`。

### **输出饱和功率** — 输出饱和功率 `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

输出饱和功率，指定为标量。该模块使用此值计算非线性模型中使用的电压饱和点。在这种情况下，多项式的一阶导数为零，二阶导数为负。

#### 依赖项

要设置此参数，请在 **非线性多项式类型** 中选择 `Odd order`。

### **饱和时的增益压缩** — 饱和时的增益压缩 `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

饱和时的增益压缩，指定为标量。

当 **非线性多项式类型** 为
`Odd order` 时，指定饱和时的增益压缩。

#### 依赖项

要设置此参数，请先在 **非线性多项式类型** 中选择 `Odd
order`。然后，更改
**输出饱和功率** 的默认值。

### **在最大 S21 幅度处使用工作频率** — 指定工作频率 `off` (default) | `on`

选择此参数以在 S21 的最大幅度处指定工作频率。

#### 依赖项

要启用此参数：

- 首先，在**主**选项卡的 **放大器增益源**
  参数中选择 `Data source`。
- 其次，在 **非线性** 选项卡中指定非线性。
- 最后，点击 **Apply**
  按钮。

### **工作频率** — 工作频率 `1 GHz` (default) | scalar | finite vector | `Hz` | `KHz` | `MHz` | `GHz`

工作频率，指定为标量或有限向量。

#### 依赖项

要启用此参数：

- 首先，在**主**选项卡的 **放大器增益源**
  参数中选择 `Data source`。
- 其次，在 **非线性** 选项卡中指定非线性。
- 最后，点击 **Apply**
  按钮。

**注意**

如果选择了 **使用常数 S21 和非线性** 参数，请清除此参数以启用 **工作频率** 参数。

### **使用常数 S21 和非线性** — 工作频率 `off` (default) | `on`

选择此参数以在放大器模型中使用 S21 的常数幅度和非线性。

#### 依赖项

要启用此参数：

- 首先，在**主**选项卡的 **放大器增益源**
  参数中选择 `Data source`。
- 其次，在 **非线性** 选项卡中指定非线性。
- 最后，点击 **Apply**
  按钮。

### **绘制功率特性** — 放大器非线性功率曲线可视化按钮 (default)

使用此按钮可根据 **非线性** 选项卡上指定的非线性参数绘制放大器的功率特性。当您清除 **使用
常数 S21 和非线性** 参数时，功率曲线反映在 **工作频率** 参数中指定的频率处测得的放大器功率。

#### 依赖项

要启用此参数，请将 **主** 选项卡中的 **放大器增益源**
设置为
`Available power gain`、
`Open circuit voltage gain` 或
`Data source`。

### 噪声

### **模拟噪声** — 模拟热噪声 `on` (default) | `off`

选择此参数，以模拟模块参数或文件中指定的噪声。

如果噪声在 `.s2p` 文件中指定，则将其用于仿真。

### **噪声类型** — 噪声类型 `Noise figure` (default) | `Spot noise data`

噪声类型，指定为 `Noise figure` 或
`Spot noise data`。

### **噪声分布** — 噪声分布 `White` (default) | `Piece-wise linear` | `Colored`

噪声分布，指定为：

- `White`，频谱密度是单个非负值。噪声的功率值取决于载波的带宽，而带宽取决于时间步长。这是不相关噪声源。
- `Piece-wise linear`，频谱密度是值向量 [pi]。
  对于每个载波，噪声源表现为白噪声不相关噪声。噪声源的功率取决于载波。
- `Colored`，取决于载波和带宽。这是相关噪声源。

### **噪声系数 (dB)** — 噪声系数 0 (default) | scalar

噪声系数，指定为以分贝为单位的标量。

### **Frequencies** — 频率数据 `0 Hz` (default) | real scalar | finite vector

频率数据，指定为以 Hz、kHz、MHz 或 GHz 为单位的 real scalar 或 finite vector。

#### 依赖项

要设置此参数，请先在 **Noise distribution** 中选择 `Piece-wise linear` 或 `Colored`。

### **Minimum noise figure (dB)** — 最小噪声系数 `0` (default) | scalar | finite vector

最小噪声系数，指定为以分贝为单位的 scalar 或 finite vector。

#### 依赖项

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最优反射系数 `0` (default) | scalar | finite vector

最优反射系数，指定为 scalar 或 finite vector。

#### 依赖项

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 等效归一化噪声电阻 `0` (default) | scalar | finite vector

等效归一化噪声电阻，指定为 scalar 或 finite vector。

#### 依赖项

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on` (default) | `off`

选择此参数可自动计算频率相关噪声的冲激响应。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。当放大器为非线性时，您不能指定冲激响应，因为在这种情况下噪声按白噪声仿真。

#### 依赖项

要设置此参数，请先在 **Noise distribution** 中选择 `Colored`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s` (default) | scalar

用于仿真频率相关噪声的冲激响应持续时间，指定为以秒为单位的 scalar。如果放大器为非线性，则不能指定冲激响应。

#### 依赖项

要设置此参数，请先清除 **Automatically estimate impulse response duration**。

### 建模

### **Modeling options** — 对 S 参数建模 `Time domain` (default) | `Frequency domain`

对 S 参数建模，指定为：

- `Time domain` 技术创建解析有理模型，近似整个数据范围。使用 `Time domain` 建模时，`Visualization` 选项卡中的 **Plot** 会绘制 `Data Source` 中定义的数据以及 `rationalfit` 函数中的值。
- `Frequency domain` 针对每个载波频率独立计算基带冲激响应。此技术基于卷积。可选择一个选项来指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- 对于 Amplifier、Antenna 和 S-Parameters 模块，默认值为 `Time domain`。对于 Transmission Line 模块，默认值为 `Frequency domain`。

#### 依赖项

要设置此参数，请先在 **Source of amplifier gain** 中选择 `Data source`。此选择会激活包含 **Modeling options** 的 **Modeling** 选项卡。

### **Fitting options** — Rationalfit 拟合选项 `Fit individually` (default) | `Share poles by column` | `Share all poles`

Rationalfit 拟合选项，指定为 `Fit individually`、`Share poles by column` 或 `Share all poles`。

**Rational fitting results** 显示 **Number of independent fits**、**Number of required poles** 和 **Relative error achieved (dB)** 的值。

#### 依赖项

要设置此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Relative error desired (dB)** — 有理拟合可接受的相对误差 `-40` (default) | scalar

有理拟合可接受的相对误差，指定为以分贝为单位的 scalar。

#### 依赖项

要设置此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应 `on` | `off`

选择此参数可自动计算冲激响应。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。

#### 依赖项

要设置此参数，请在 **Modeling options** 中选择 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10` (default) | scalar

冲激响应持续时间，指定为以秒为单位的 scalar。

#### 依赖项

要设置此参数，请先在 **Modeling options** 中选择 `Frequency domain`。然后，清除 `Automatically estimate impulse response duration`。

### **Use only S-parameter magnitude with appropriate delay** — 仅使用具有适当延迟的 S 参数幅度 `off` (default) | `on`

选择此参数可忽略 S 参数相位，并将冲激响应延迟其长度的一半。此参数仅适用于在 time domain 中建模的 S 参数数据。您可以使用此参数通过仅指定幅度来塑造具有滤波器效应的频谱内容。

**注意**

此参数会向系统引入人工延迟。

### 可视化

### **Source of frequency data** — 频率数据源 `Extracted from data source` (default) | `User-defined`

频率数据源，指定为：

- 当 **Source of frequency data** 为 `Extracted from data source` 时，**Data source** 必须设置为 `Data file`。验证指定的 **Data file** 包含频率数据。
- 当 **Source of frequency data** 为 `User-specified` 时，在 **Frequency data** 参数中指定频率向量。另外，从相应下拉列表指定单位。

#### 依赖项

要设置此参数，请先在 **Source of amplifier gain** 中选择 `Data source`。此选择会激活包含 **Source of frequency data** 的 **Visualization** 选项卡。

### **Frequency data** — 频率数据范围 `[1e9:1e6:3e9]` (default) | finite vector | `Hz` | `kHz` | `MHz` | `GHz`

频率数据范围，指定为 finite vector。

#### 依赖项

要启用此参数，请将 **Source of frequency data** 设置为 `User-specified`。

### **Plot type** — 数据绘图类型 `X-Y plane` (default) | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

您希望使用数据生成的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建 linear、semilog 或 log-log 图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Parameter 1** — 要绘制的 S 参数类型 `S11` (default) | `S12` | `S21` | `S22` | `NF`

要绘制的 S 参数类型，指定为 `S11`、`S12`、`S21` 或 `S22`。当噪声为频谱噪声时，可以进行 `NF` 绘图。

#### 依赖项

要启用 `NF`，请将 **Noise type** 设置为 `Noise figure`，然后选择 **Apply**。

### **Parameter 2** — 要绘制的 S 参数类型 `None` (default) | `S11` | `S12` | `S21` | `S22` | `NF`

要绘制的 S 参数类型，指定为 `S11`、`S12`、`S21` 或 `S22`。当噪声为频谱噪声时，可以进行 `NF` 绘图。

#### 依赖项

要启用 `NF`，请将 **Noise distribution** 设置为 `Piece-wise linear` 或 `Colored`，然后选择 **Apply**。

### **Format1** — 绘图格式 `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Format2** — 绘图格式 `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Y-axis scale** — Y 轴刻度 `Linear` (default) | `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X-axis scale** — X 轴刻度 `Linear` (default) | `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定的数据按钮

使用 plot 按钮绘制指定的数据。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2010b 中引入**

### R2025a：改进用于计算非线性的多项式模型

Amplifier 模块现在支持改进的多项式模型来计算非线性，该模型更好地符合用户规范。

当您打开在 R2025a 之前创建且包含 Amplifier 模块的模型时，软件使用改进的多项式模型来计算非线性，数值结果可能会有所不同。

### R2024b：`Time domain (rationalfit)` 参数已重命名

**Modeling options** 参数中的 `Time domain (rationalfit)` 参数值已在 Amplifier 模块中重命名为 `Time domain`。

当您打开在 R2024b 之前创建且包含 Amplifier 模块的模型时，参数名显示为 `Time domain`。

### R2022b：添加了三个新参数

Amplifier 模块有三个新参数。

- **Network-parameter object** — 使用此参数指定网络参数对象作为放大器增益源。
- **Use rational object** — 使用此参数指定 `rational` 对象作为放大器增益源。
- **Plot power characteristics** — 使用此按钮基于指定的非线性绘制放大器的功率特性。

### R2022b：两个模块参数已重命名

**Pick operation frequency at maximum S21 magnitude** 和 **Frequency data** 参数已分别重命名为 **Use operation frequency at maximum S21 magnitude** 和 **Source of frequency data**。

当您打开在 R2022b 之前创建且包含 Amplifier 模块的模型时，软件会将旧参数名替换为新名称。

### R2022a：在非线性电路包络放大器中建模噪声

Amplifier 模块现在允许您在放大器工作于非线性区域时将频率相关噪声建模为有色噪声。

当您打开在 R2022a 之前创建且包含工作于非线性区域且具有频率相关噪声的 Amplifier 模块的模型时，软件按照模块中的指定对噪声建模。

### R2022a：添加了两个新参数

Amplifier 模块有两个新参数。

- **AM/AM-AM/PM table** — 使用此参数通过 AM/AM-AM/PM 表指定放大器功率特性。
- **Use constant S21 and nonlinearity** — 使用此参数对工作于非线性区域时的频率相关增益 (S21) 建模。

### R2021b：Amplifier 模块图标已更新

从 R2021b 开始，Amplifier 模块图标已更新。该模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建且包含 Amplifier 模块的模型时，软件将该模块图标替换为 R2021b 版本。

## 描述

在 RF 系统中对放大器建模

使用 Amplifier 模块对线性或非线性放大器建模，可包含或不包含噪声。使用数据源定义放大器增益还会定义输入数据可视化和建模。使用 **Main** 选项卡参数，通过数据表值、标准 `s2p` 文件、S 参数或电路包络多项式系数来指定放大器增益和噪声。

除放大器增益从 `Data source` 获取的情况外，放大器实现为多项式压控电压源 (VCVS)。VCVS 包含非线性，这些非线性使用 **Nonlinearity** 选项卡中列出的参数来描述。为对线性放大建模，放大器在输入和输出电压之间实现关系 *V*out = a1\**V*in。输入电压为 *V*i(*t*) = *A*i(*t*)ejωt，输出电压为 *V*o(*t*) = *A*o(*t*)ejωt，在 RF Blockset™ 环境中的每个载波 *w* = 2π*f* 处。

如果放大器增益从数据源获取，则放大器实现基于 S 参数数据。非线性放大建模为多项式（饱和功率自动计算）。它还会产生额外的互调频率。

Amplifier 模块掩膜图标是动态的，并显示所应用噪声参数的当前状态。下表说明此模块上的图标如何根据模块上 **Noise figure (dB)** 参数的状态而变化。

| Noise Figure (dB)：`10` | Noise Figure (dB)：`0` |
| --- | --- |
| Amplifier 模块图标，其中 Noise figure (dB) 设置为 10。 | Amplifier 模块图标，其中 Noise figure (dB) 设置为 0。 |
