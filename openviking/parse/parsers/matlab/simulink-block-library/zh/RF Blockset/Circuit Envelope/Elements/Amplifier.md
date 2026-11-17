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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: 放大器增益来源
  summary: 放大器增益来源 Available power gain（默认）| Open circuit voltage gain | Data source | Polynomial coefficients | AM/AM-AM/PM
    table
  group: 主
- name: Available power gain
  summary: 可用功率增益 0 dB（默认）| 标量
  group: 主
- name: Open circuit voltage gain
  summary: 开路电压增益 0 dB（默认）| 标量
  group: 主
- name: Data source
  summary: 数据源 Data File（默认）| Network-parameters | Rational Model
  group: 主
- name: Polynomial coefficients
  summary: 多项式系数 [0 1]（默认）| 向量
  group: 主
- name: AM/AM-AM/PM table
  summary: 查找表 [ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]（默认）| *M*×3 实矩阵
  group: 主
- name: Network-parameter object
  summary: 作为数据源的网络参数对象 off（默认）| on
  group: 主
- name: Network parameter type
  summary: 网络参数类型 S-parameters（默认）| Y-parameters | Z-parameters
  group: 主
- name: Input impedance (Ohm)
  summary: 输入阻抗 50（默认）| 正标量
  group: 主
- name: Output impedance (Ohm)
  summary: 输出阻抗 50（默认）| 正标量
  group: 主
- name: Data file
  summary: 网络参数数据文件的名称 unitygain.s2p（默认）| 字符向量
  group: 主
- name: Frequency (dB)
  summary: 网络参数的频率 1e9 Hz（默认）| 标量 | Hz | kHz | MHz | GHz
  group: 主
- name: Reference Impedance(Ohm)
  summary: 网络参数的参考阻抗 50（默认）| 正标量 | 正标量向量
  group: 主
- name: Use rational object
  summary: 将 rational 对象用作数据源 off（默认）| on
  group: 主
- name: Residues
  summary: 按有理模型顺序排列的留数 0（默认）| 向量
  group: 主
- name: Poles
  summary: 按有理模型顺序排列的极点 0（默认）| 向量
  group: 主
- name: Direct feedthrough
  summary: 直接馈通 {0 0:1 0}（默认）| 向量数组
  group: 主
- name: Ground and hide negative terminals
  summary: 接地并隐藏 RF 电路端子 on（默认）| off
  group: 主
- name: Nonlinear polynomial type
  summary: 非线性类型 Even and odd order（默认）| Odd order
  group: 非线性
- name: Intercept points convention
  summary: 截点约定 Output（默认）| Input
  group: 非线性
- name: IP2
  summary: 二阶截点 infdBm（默认）| 标量 | W | mW | dBW | dBm
  group: 非线性
- name: IP3
  summary: 三阶截点 infdBm（默认）| 标量 | W | mW | dBW | dBm
  group: 非线性
- name: 1-dB gain compression power
  summary: 1-dB 增益压缩功率 inf dBm（默认）| 标量 | W | mW | dBW | dBm
  group: 非线性
- name: Output saturation power
  summary: 输出饱和功率 inf dBm（默认）| 标量 | W | mW | dBW | dBm
  group: 非线性
- name: Gain compression at saturation
  summary: 饱和时的增益压缩 inf dBm（默认）| 标量 | W | mW | dBW | dBm
  group: 非线性
- name: Use operation frequency at maximum S21 magnitude
  summary: 指定工作频率 off（默认）| on
  group: 非线性
- name: Operation frequency
  summary: 工作频率 1 GHz（默认）| 标量 | 有限向量 | Hz | KHz | MHz | GHz
  group: 非线性
- name: Use constant S21 and nonlinearity
  summary: 工作频率 off（默认）| on
  group: 非线性
- name: Plot Power Characteristics
  summary: 放大器非线性功率曲线可视化按钮（默认）
  group: 非线性
- name: Simulate noise
  summary: 模拟热噪声 on（默认）| off
  group: 噪声
- name: Noise type
  summary: 噪声类型 Noise figure（默认）| Spot noise data
  group: 噪声
- name: Noise distribution
  summary: 噪声分布 White（默认）| Piece-wise linear | Colored
  group: 噪声
- name: Noise figure (dB)
  summary: 噪声系数 0（默认）| 标量
  group: 噪声
- name: Frequencies
  summary: 频率数据 0 Hz（默认）| 实数标量 | 有限向量
  group: 噪声
- name: Minimum noise figure (dB)
  summary: 最小噪声系数 0（默认）| 标量 | 有限向量
  group: 噪声
- name: Optimal reflection coefficient
  summary: 最佳反射系数 0（默认）| 标量 | 有限向量
  group: 噪声
- name: Equivalent normalized noise resistance
  summary: 等效归一化噪声电阻 0（默认）| 标量 | 有限向量
  group: 噪声
- name: Automatically estimate impulse response duration
  summary: 自动估计冲激响应持续时间 on（默认）| off
  group: 噪声
- name: Impulse response duration
  summary: 冲激响应持续时间 1e-10s（默认）| 标量
  group: 噪声
- name: Modeling options
  summary: 对 S 参数建模 Time domain（默认）| Frequency domain
  group: 建模
- name: 拟合选项
  summary: Rationalfit 拟合选项 Fit individually（默认）| Share poles by column | Share all poles
  group: 建模
- name: 期望相对误差 (dB)
  summary: 有理拟合可接受的相对误差 -40（默认）| 标量
  group: 建模
- name: 自动估计冲激响应持续时间
  summary: 自动计算冲激响应 on | off
  group: 建模
- name: 冲激响应持续时间
  summary: 冲激响应持续时间 1e-10（默认）| 标量
  group: 建模
- name: 仅使用带适当延迟的 S 参数幅值
  summary: 仅使用带适当延迟的 S 参数幅值 off（默认）| on
  group: 建模
- name: 频率数据来源
  summary: 频率数据源 Extracted from data source（默认）| User-defined
  group: 可视化
- name: 频率数据
  summary: 频率数据范围 [1e9:1e6:3e9]（默认）| 有限向量 | Hz | kHz | MHz | GHz
  group: 可视化
- name: 绘图类型
  summary: 数据绘图类型 X-Y plane（默认）| Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: 可视化
- name: Parameter 1
  summary: 要绘制的 S 参数类型 S11（默认）| S12 | S21 | S22 | NF
  group: 可视化
- name: Parameter 2
  summary: 要绘制的 S 参数类型 None（默认）| S11 | S12 | S21 | S22 | NF
  group: 可视化
- name: Format1
  summary: 绘图格式 Magnitude (decibels)（默认）| Magnitude (linear) | Angle(degrees) | Real | Imaginary
  group: 可视化
- name: Format2
  summary: 绘图格式 Magnitude (decibels)（默认）| Magnitude (linear) | Angle(degrees) | Real | Imaginary
  group: 可视化
- name: Y-axis scale
  summary: Y 轴刻度 Linear（默认）| Logarithmic
  group: 可视化
- name: X-axis scale
  summary: X 轴刻度 Linear（默认）| Logarithmic
  group: 可视化
- name: Plot
  summary: 绘制指定数据按钮
  group: 可视化
```

### 主

### **放大器增益来源** — 放大器增益来源 `Available power gain`（默认）| `Open circuit voltage gain` | `Data source` | `Polynomial coefficients` | `AM/AM-AM/PM table`

放大器增益的来源，指定为以下选项之一：

- `Available power gain` —
  该模块使用 **Available power gain** 参数来计算 *a1*，即多项式 VCVS 的线性电压增益项。此计算假设放大器为匹配负载端接。
- `Open circuit voltage gain`
  — 该模块使用 **Open circuit voltage gain** 参数来计算 *a1*，即多项式 VCVS 的线性电压增益项。
- `Data source` — 该模块使用 **Data
  source** 参数来计算线性电压增益。当使用数据源选项时，该模块使用 *S*11 和
  *S*22 作为输入和输出阻抗。
- `Polynomial coefficients`
  — 该模块使用 **Polynomial coefficients** 参数来计算非线性电压增益。
- `AM/AM-AM/PM table` — 该模块使用 **AM/AM-AM/PM table** 参数来确定放大器的功率特性。

### **Available power gain** — 可用功率增益 0 `dB`（默认）| 标量

放大器的可用功率增益，指定为以 dB 为单位的标量。从相应的下拉列表中指定单位。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 选项卡中选择 `Available power
gain`。

### **Open circuit voltage gain** — 开路电压增益 0 `dB`（默认）| 标量

放大器的开路电压，指定为以 dB 为单位的标量。从相应的下拉列表中指定单位。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 选项卡中选择 `Open circuit voltage
gain`。

### **Data source** — 数据源 `Data File`（默认）| `Network-parameters` | `Rational Model`

数据源，指定为以下选项之一：

- `Data file` — 扩展名为 `.s2p` 的 Touchstone 文件名。
- `Network-parameters` —
  提供 **Network parameter** 数据，例如 `S-parameters`、`Y-parameters` 和 `Z-parameters`，以及放大器对应的 **Frequency** 和 **Reference impedance (ohms)**。
- `Rational model` — 提供 **Residues**、**Poles** 和 **Direct
  feedthrough** 参数的值，这些参数对应于有理模型的方程

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  在此有理模型方程中，每个 *Ck* 是极点 *Ak* 的留数。如果 *Ck* 为复数，则还必须枚举对应的复共轭极点和留数。此对象具有属性 `C`、`A` 和 `D`。您可以使用这些属性来指定 **Residues**、**Poles** 和 **Direct
  feedthrough** 参数。

当放大器为非线性时，非线性仅适用于表示 2 端口元件的散射参数的 S21 项。在这种情况下，S21 与频率无关，其常数值为 S21 的最大值，或用户指定的工作频率处的 S21 值。其他散射参数 S11、S12 和 S22 与线性情况相同。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 选项卡中选择 `Data
source`。

### **Polynomial coefficients** — 多项式系数 `[0 1]`（默认）| 向量

多项式的阶数，指定为向量。

多项式的阶数必须小于或等于 9。系数按升幂排列。如果向量有 10 个系数，
`[a0,a1,a2,
... a9]`，
它所表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

其中
*a*1 表示线性增益项，高阶项根据 [1] 建模。

例如，向量
`[a0,a1,a2,a3]`
指定关系 *Vout* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3。末尾的零被省略。因此，
`[a0,a1,a2]`
定义的多项式与
`[a0,a1,a2,
0]` 相同。此参数的默认值为 [0,1]，
对应于线性关系
*Vout* =
*Vin*。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 选项卡中选择 `Polynomial
coefficients`。

### **AM/AM-AM/PM table** — 查找表 `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]`（默认）| *M*×3 实矩阵

查找表条目，指定为实 *M*×3
矩阵。矩阵的第二列表示 AM/AM–AM/PM 模型的输出功率，单位为 dBm。第三列表示模型相位变化，单位为度。第二列和第三列的值与矩阵第一列中表示的输入信号功率的绝对值相关。第一列中的输入功率必须单调递增。

#### 依赖关系

要启用此参数，请将 **Source of amplifier
gain** 设置为 `AM/AM - AM/PM
table`。

### **Network-parameter object** — 作为数据源的网络参数对象 `off`（默认）| `on`

选择此参数以使用网络参数对象作为放大器增益的来源。

选择此参数后，在打开的文本框中，指定以下之一：

- 网络参数对象。
- MATLAB® 基础工作区变量或 Simulink® 模型工作区变量。如果指定的变量是网络参数对象，则该模块会对其进行求值。

您可以指定的网络参数对象包括：

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### 依赖关系

要启用此参数，请先在 **Source of amplifier
gain** 中选择 `Data
source`，然后在 **Data
source** 中选择
`Network-parameters`。

### **Network parameter type** — 网络参数类型 `S-parameters`（默认）| `Y-parameters` | `Z-parameters`

网络参数类型，指定为 `S-parameters`、
`Y-parameters` 或
`Z-parameters`。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier
gain** 中选择 `Data
source`，然后在
**Data source** 中选择
`Network-parameters`。

### **Input impedance (Ohm)** — 输入阻抗 `50`（默认）| 正标量

放大器的输入阻抗，指定为以欧姆为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 中选择 `Available power
gain`、`Open circuit voltage
gain` 或 `Polynomial
coefficients`。

### **Output impedance (Ohm)** — 输出阻抗 `50`（默认）| 正标量

放大器的输出阻抗，指定为以欧姆为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Source of amplifier
gain** 中选择 `Available power
gain`、`Open circuit voltage
gain` 或 `Polynomial
coefficients`。

### **Data file** — 网络参数数据文件的名称 `unitygain.s2p`（默认）| 字符向量

网络参数数据文件的名称，指定为字符向量。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier
gain** 中选择 `Data
source`，然后在 **Data source** 中选择 `Data
file`。

### **Frequency (dB)** — 网络参数的频率 `1e9 Hz`（默认）| 标量 | `Hz` | `kHz` | `MHz` | `GHz`

网络参数的频率，指定为以 Hz 为单位的标量。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Network-parameters`。

### **Reference Impedance(Ohm)** — 网络参数的参考阻抗 `50`（默认）| 正标量 | 正标量向量

网络参数的参考阻抗，指定为以欧姆为单位的正标量或正标量向量。

**注意**

当您将其指定为正标量向量时，所有端口的参考阻抗必须相等。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Network-parameters`。

### **Use rational object** — 将 rational 对象用作数据源 `off`（默认）| `on`

选择此参数以使用 `rational` 对象作为数据源来对放大器增益进行建模。

选择此参数后，在打开的文本框中，指定以下内容之一：

- `rational` 对象。
- MATLAB 基础工作区变量或 Simulink 模型工作区变量。如果指定的变量是 rational 对象，模块将对其进行求值。”

您可以指定的 `rational` 对象包括：

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Rational model`。

### **Residues** — 按有理模型顺序排列的留数 `0`（默认）| 向量

按有理模型顺序排列的留数，指定为向量。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Rational model`。

### **Poles** — 按有理模型顺序排列的极点 `0`（默认）| 向量

按有理模型顺序排列的极点，指定为向量。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Rational model`。

### **Direct feedthrough** — 直接馈通 `{0 0:1 0}`（默认）| 向量数组

直接馈通，指定为向量数组。

#### 依赖关系

要启用此参数，请先在 **Source of amplifier gain** 中选择 `Data source`，然后在 **Data source** 中选择 `Rational model`。

### **Ground and hide negative terminals** — 接地并隐藏 RF 电路端子 `on`（默认）| `off`

选择此选项可接地并隐藏负端子。清除此参数可暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

默认情况下，此选项处于选中状态。

### 非线性

### **Nonlinear polynomial type** — 非线性类型 `Even and odd order`（默认）| `Odd order`

非线性类型，指定为 `Even and odd order` 或 `Odd order`。

- 当您选择 `Even and odd order` 时，放大器除了产生线性项之外，还可以产生二阶和三阶互调频率。
- 当您选择 `Odd order` 时，放大器仅产生奇数阶互调频率。

  线性增益决定线性 *a*1 项。模块根据指定的参数计算其余项。这些参数为 **IP3**、**1-dB gain compression power**、**Output saturation power** 和 **Gain compression at saturation**。您指定的约束数量决定模型的阶数。该图展示了非线性放大器参数的图形化定义。

  Po 对 Pi 图，用于表示非线性放大器参数。

### **Intercept points convention** — 截点约定 `Output`（默认）| `Input`

截点约定，指定为 `Input` 参考约定或 `Output` 参考约定。将此规范用于截点、1-dB 增益压缩功率和饱和功率。

### **IP2** — 二阶截点 `inf``dBm`（默认）| 标量 | `W` | `mW` | `dBW` | `dBm`

二阶截点，指定为标量。

#### 依赖关系

要设置此参数，请在**非线性多项式类型**中选择 `Even and odd order`。

### **IP3** — 三阶截点 `inf``dBm`（默认）| 标量 | `W` | `mW` | `dBW` | `dBm`

三阶截点，指定为标量。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf dBm`（默认）| 标量 | `W` | `mW` | `dBW` | `dBm`

1-dB 增益压缩功率，指定为标量。

#### 依赖关系

要设置此参数，请在**非线性多项式类型**中选择 `Odd order`。

### **Output saturation power** — 输出饱和功率 `inf dBm`（默认）| 标量 | `W` | `mW` | `dBW` | `dBm`

输出饱和功率，指定为标量。该模块使用此值来计算非线性模型中使用的电压饱和点。在这种情况下，多项式的一阶导数为零，二阶导数为负。

#### 依赖关系

要设置此参数，请在**非线性多项式类型**中选择 `Odd order`。

### **Gain compression at saturation** — 饱和时的增益压缩 `inf dBm`（默认）| 标量 | `W` | `mW` | `dBW` | `dBm`

饱和时的增益压缩，指定为标量。

当**非线性多项式类型**为 `Odd order` 时，指定饱和时的增益压缩。

#### 依赖关系

要设置此参数，请先在**非线性多项式类型**中选择 `Odd order`。然后，更改**输出饱和功率**的默认值。

### **Use operation frequency at maximum S21 magnitude** — 指定工作频率 `off`（默认）| `on`

选择此参数以在 S21 的最大幅度处指定工作频率。

#### 依赖关系

要启用此参数：

- 首先，在**主**选项卡的**放大器增益来源**参数中选择 `Data source`。
- 其次，在**非线性**选项卡中指定非线性。
- 最后，点击**应用**按钮。

### **Operation frequency** — 工作频率 `1 GHz`（默认）| 标量 | 有限向量 | `Hz` | `KHz` | `MHz` | `GHz`

工作频率，指定为标量或有限向量。

#### 依赖关系

要启用此参数：

- 首先，在**主**选项卡的**放大器增益来源**参数中选择 `Data source`。
- 其次，在**非线性**选项卡中指定非线性。
- 最后，点击**应用**按钮。

**注意**

如果选择了 **Use constant S21 and nonlinearity** 参数，请清除此参数以启用**工作频率**参数。

### **Use constant S21 and nonlinearity** — 工作频率 `off`（默认）| `on`

选择此参数以在放大器模型中使用恒定的 S21 幅度和非线性。

#### 依赖关系

要启用此参数：

- 首先，在**主**选项卡的**放大器增益来源**参数中选择 `Data source`。
- 其次，在**非线性**选项卡中指定非线性。
- 最后，点击**应用**按钮。

### **Plot Power Characteristics** — 放大器非线性功率曲线可视化按钮（默认）

使用此按钮可根据**非线性**选项卡中指定的非线性参数绘制放大器的功率特性。当您清除 **Use constant S21 and nonlinearity** 参数时，功率曲线反映在**工作频率**参数中指定的频率处测得的放大器功率。

#### 依赖关系

要启用此参数，请将**主**选项卡中的**放大器增益来源**设置为 `Available power gain`、`Open circuit voltage gain` 或 `Data source`。

### 噪声

### **Simulate noise** — 模拟热噪声 `on`（默认）| `off`

选择此参数，以模拟模块参数中或文件中指定的噪声。

如果噪声在 `.s2p` 文件中指定，则将其用于仿真。

### **Noise type** — 噪声类型 `Noise figure`（默认）| `Spot noise data`

噪声类型，指定为 `Noise figure` 或 `Spot noise data`。

### **Noise distribution** — 噪声分布 `White`（默认）| `Piece-wise linear` | `Colored`

噪声分布，指定为：

- `White`，频谱密度为单个非负值。噪声的功率值取决于载波的带宽，而带宽取决于时间步长。这是一个不相关的噪声源。
- `Piece-wise linear`，频谱密度为值向量 [pi]。对于每个载波，噪声源表现为白噪声不相关噪声。噪声源的功率取决于载波。
- `Colored`，取决于载波和带宽。这是一个相关噪声源。

### **Noise figure (dB)** — 噪声系数 0（默认）| 标量

噪声系数，指定为以分贝为单位的标量。

### **Frequencies** — 频率数据 `0 Hz`（默认）| 实数标量 | 有限向量

频率数据，指定为以 Hz、kHz、MHz 或 GHz 为单位的实数标量或有限向量。

#### 依赖关系

要设置此参数，请先在 **Noise distribution** 中选择 `Piece-wise linear` 或 `Colored`。

### **Minimum noise figure (dB)** — 最小噪声系数 `0`（默认）| 标量 | 有限向量

最小噪声系数，指定为以分贝为单位的标量或有限向量。

#### 依赖关系

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳反射系数 `0`（默认）| 标量 | 有限向量

最佳反射系数，指定为标量或有限向量。

#### 依赖关系

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 等效归一化噪声电阻 `0`（默认）| 标量 | 有限向量

等效归一化噪声电阻，指定为标量或有限向量。

#### 依赖关系

要设置此参数，请先在 **Noise type** 中选择 `Spot noise data`。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此参数可自动计算频率相关噪声的冲激响应。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。当放大器为非线性时，您无法指定冲激响应，因为在这种情况下噪声被模拟为白噪声。

#### 依赖关系

要设置此参数，请先在 **Noise distribution** 中选择 `Colored`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于模拟频率相关噪声的冲激响应持续时间，指定为以秒为单位的标量。如果放大器为非线性，则无法指定冲激响应。

#### 依赖关系

要设置此参数，请先清除 **Automatically estimate impulse response duration**。

### 建模

### **Modeling options** — 对 S 参数建模 `Time domain`（默认）| `Frequency domain`

对 S 参数建模，指定为：

- `Time domain` 技术创建一个解析有理模型，近似整个数据范围。使用 `Time domain` 建模时，`Visualization` 选项卡中的 **Plot** 会绘制 `Data Source` 中定义的数据以及 `rationalfit` 函数中的值。
- `Frequency domain` 独立计算每个载波频率的基带冲激响应。此技术基于卷积。可以选择指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- 对于 Amplifier、Antenna 和 S-Parameters 模块，默认值为 `Time domain`。对于 Transmission Line 模块，默认值为 `Frequency domain`。

#### 依赖关系

要设置此参数，请先在**放大器增益来源**中选择 `Data source`。该选择会激活**建模**选项卡，其中包含**建模选项**。

### **拟合选项** — Rationalfit 拟合选项 `Fit individually`（默认）| `Share poles by column` | `Share all poles`

Rationalfit 拟合选项，指定为 `Fit individually`、`Share poles by column` 或 `Share all poles`。

**有理拟合结果**显示**独立拟合数量**、**所需极点数量**和**达到的相对误差 (dB)**的值。

#### 依赖关系

要设置此参数，请在**建模选项**中选择 `Time domain`。

### **期望相对误差 (dB)** — 有理拟合可接受的相对误差 `-40`（默认）| 标量

有理拟合可接受的相对误差，指定为以分贝为单位的标量。

#### 依赖关系

要设置此参数，请在**建模选项**中选择 `Time domain`。

### **自动估计冲激响应持续时间** — 自动计算冲激响应 `on` | `off`

选择此参数可自动计算冲激响应。清除此参数可使用**冲激响应持续时间**手动指定冲激响应持续时间。

#### 依赖关系

要设置此参数，请在**建模选项**中选择 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10`（默认）| 标量

冲激响应持续时间，指定为以秒为单位的标量。

#### 依赖关系

要设置此参数，请先在**建模选项**中选择 `Frequency domain`。然后，清除 `Automatically estimate impulse response duration`。

### **仅使用带适当延迟的 S 参数幅值** — 仅使用带适当延迟的 S 参数幅值 `off`（默认）| `on`

选择此参数可仅使用 S 参数相位，并将冲激响应延迟其长度的一半。此参数仅适用于在时域中建模的 S 参数数据。您可以使用此参数通过仅指定幅值来塑造具有滤波器效果的频谱内容。

**注意**

此参数会向系统引入人为延迟。

### 可视化

### **频率数据来源** — 频率数据源 `Extracted from data source`（默认）| `User-defined`

频率数据源，指定为：

当**频率数据来源**为 `Extracted from data source` 时，**数据源**必须设置为 `Data file`。请验证指定的**数据文件**包含频率数据。

当**频率数据来源**为 `User-specified` 时，请在**频率数据**参数中指定频率向量。同时，从相应的下拉列表中指定单位。

#### 依赖关系

要设置此参数，请先在**放大器增益来源**中选择 `Data source`。该选择会激活**可视化**选项卡，其中包含**频率数据来源**。

### **频率数据** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| 有限向量 | `Hz` | `kHz` | `MHz` | `GHz`

频率数据范围，指定为有限向量。

#### 依赖关系

要启用此参数，请将**频率数据来源**设置为 `User-specified`。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认）| `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用数据生成的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置**Y 轴刻度**和**X 轴刻度**。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

### **Parameter 1** — 要绘制的 S 参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `NF`

要绘制的 S 参数类型，指定为 `S11`、`S12`、`S21` 或 `S22`。当噪声为频谱噪声时，可以绘制 `NF`。

#### 依赖关系

要启用 `NF`，请将 **Noise type** 设置为 `Noise figure`，然后选择 **Apply**。

### **Parameter 2** — 要绘制的 S 参数类型 `None`（默认）| `S11` | `S12` | `S21` | `S22` | `NF`

要绘制的 S 参数类型，指定为 `S11`、`S12`、`S21` 或 `S22`。当噪声为频谱噪声时，可以绘制 `NF`。

#### 依赖关系

要启用 `NF`，请将 **Noise distribution** 设置为 `Piece-wise linear` 或 `Colored`，然后选择 **Apply**。

### **Format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Y-axis scale** — Y 轴刻度 `Linear`（默认）| `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X-axis scale** — X 轴刻度 `Linear`（默认）| `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据按钮

使用绘制按钮绘制指定数据。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2025a：改进多项式模型以计算非线性

Amplifier 模块现在支持改进的多项式模型来计算非线性，该模型更好地遵循用户规格。

当您打开在 R2025a 之前创建的包含 Amplifier 模块的模型时，软件会使用改进的多项式模型来计算非线性，数值结果可能会有所不同。

### R2024b：`Time domain (rationalfit)` 参数已重命名

Amplifier 模块中 **Modeling options** 参数里的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 Amplifier 模块的模型时，参数名称显示为 `Time domain`。

### R2022b：新增三个参数

Amplifier 模块新增了三个参数。

- **Network-parameter object** — 使用此参数指定网络参数对象作为放大器增益的来源。
- **Use rational object** — 使用此参数指定 `rational` 对象作为放大器增益的来源。
- **Plot power characteristics** — 使用此按钮基于指定的非线性绘制放大器的功率特性。

### R2022b：两个模块参数已重命名

**Pick operation frequency at maximum S21 magnitude** 和 **Frequency data** 参数已分别重命名为 **Use operation frequency at maximum S21 magnitude** 和 **Source of frequency data**。

当您打开在 R2022b 之前创建的包含 Amplifier 模块的模型时，软件会将旧参数名称替换为新名称。

### R2022a：在非线性电路包络放大器中建模噪声

当您的放大器工作于非线性区域时，Amplifier 模块现在使您能够将频率相关噪声建模为有色噪声。

当您打开在 R2022a 之前创建的包含工作于非线性区域且具有频率相关噪声的 Amplifier 模块的模型时，软件会按照模块中的指定对噪声进行建模。

### R2022a: 新增两个参数

Amplifier 模块新增了两个参数。

- **AM/AM-AM/PM table** — 使用此参数通过 AM/AM-AM/PM 表指定放大器功率特性。
- **Use
  constant S21 and nonlinearity** — 使用此参数在非线性区域工作时对频率相关增益（S21）进行建模。

### R2021b: Amplifier 模块图标已更新

从 R2021b 开始，Amplifier 模块图标已更新。该模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Amplifier 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

在 RF 系统中对放大器进行建模

使用 Amplifier 模块对线性或非线性放大器进行建模，可选择是否包含噪声。使用数据源定义放大器增益同时也会定义输入数据可视化和建模。使用 **Main** 选项卡参数通过数据手册值、标准 `s2p` 文件、S 参数或电路包络多项式系数来指定放大器增益和噪声。

放大器实现为多项式压控电压源（VCVS），除非放大器增益来自 `Data source`。VCVS 包含使用 **Nonlinearity** 选项卡中列出的参数描述的非线性特性。要对线性放大进行建模，放大器在输入和输出电压之间实现关系 *V*out = a1\**V*in。输入电压为 *V*i(*t*) = *A*i(*t*)ejωt，输出电压为 *V*o(*t*) = *A*o(*t*)ejωt，在 RF Blockset™ 环境中的每个载波 *w* = 2π*f* 处。

如果放大器增益来自数据源，放大器实现基于 S 参数数据。非线性放大建模为多项式（饱和功率自动计算）。它还会产生额外的互调频率。

Amplifier 模块掩码图标是动态的，并显示所应用噪声参数的当前状态。下表显示了此模块上的图标如何根据模块上 **Noise figure (dB)** 参数的状态而变化。

| Noise Figure (dB): `10` | Noise Figure (dB): `0` |
| --- | --- |
| Noise figure (dB) 设置为 10 时的 Amplifier 模块图标。 | Noise figure (dB) 设置为 0 时的 Amplifier 模块图标。 |
