---
type: simulink-block
title: 'IMT Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'imtmixer'
documentation_source_path: 'ref/imtmixer.html'
language: zh-CN
chinese_source: worker-translation
---

# IMT Mixer

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Carrier frequency (Hz)
  summary: 载波频率 1e9（默认）| 标量
  group: ''
- name: Local oscillator frequency (Hz)
  summary: 本振（LO）频率 0.9e9（默认）| 标量
  group: ''
- name: Reference input power (dBm)
  summary: 参考输入功率 -10（默认）| 标量
  group: ''
- name: Nominal output power (dbm)
  summary: 标称 LO 功率 -20（默认）| 标量
  group: ''
- name: Use data file
  summary: 指定要使用的数据文件 off（默认）| on
  group: ''
- name: Data file
  summary: 数据文件 samplespur1.s2d（默认）
  group: ''
- name: Input impedance (Ohm)
  summary: 混频器的输入阻抗 50（默认）| 实标量 | 正实标量向量
  group: ''
- name: Output impedance (Ohm)
  summary: 混频器的输出阻抗 50（默认）| 实标量 | 正实标量向量
  group: ''
- name: Ground and hide negative terminals
  summary: 将 RF 负端电路端子接地 on（默认）| off
  group: ''
- name: IMT table
  summary: IMT 杂散可视化 [99 99 99; 99 0 99; 99 99 99]（默认）| 方阵
  group: ''
- name: Output signal power (dBm)
  summary: 期望输出音调的信号功率 0（默认）| 标量
  group: ''
- name: Mixer type
  summary: 混频器类型 Upconverter（默认）| Downconverter
  group: ''
- name: Plot
  summary: 使用指定的信号功率和混频器类型按钮可视化 IMT 表值
  group: ''
- name: Simulate noise
  summary: 模拟器件噪声或相位噪声 on（默认）| off
  group: ''
- name: Noise type
  summary: 噪声类型 Noise figure（默认）| Spot noise data
  group: ''
- name: Noise distribution
  summary: 噪声分布 White（默认）| Piece-wise linear | Colored
  group: ''
- name: Noise figure (dB)
  summary: 噪声系数 0（默认）| 标量
  group: ''
- name: Frequencies (Hz)
  summary: 频率数据 0（默认）| 标量 | 向量
  group: ''
- name: Minimum noise figure (dB)
  summary: 最小噪声系数 0（默认）| 标量 | 向量
  group: ''
- name: Optimal reflection coefficient
  summary: 最佳反射系数 0（默认）| 标量 | 向量
  group: ''
- name: Equivalent normalized noise resistance
  summary: 等效归一化噪声电阻 0（默认）| 标量 | 向量
  group: ''
- name: Add LO phase noise
  summary: 添加相位噪声 off（默认）| on
  group: ''
- name: Phase noise frequency offset (Hz)
  summary: 相位噪声频率偏移 1（默认）| 标量 | 向量
  group: ''
- name: Phase noise level (dBc/Hz)
  summary: 相位噪声电平 -Inf（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: Automatically estimate impulse response duration
  summary: 自动估计冲激响应持续时间 on（默认）| off
  group: ''
- name: Impulse response duration
  summary: 冲激响应持续时间 1e-10s（默认）| 标量
  group: ''
```

#### 主

### **Carrier frequency (Hz)** — 载波频率 `1e9`（默认）| 标量

载波频率，指定为以赫兹为单位的标量。当输入连接上存在多个载波时，此载波频率被选为 RF 信号输入。相邻载波之间的间隔必须大于 (1−1e−8)Fc。

**数据类型：** `double`

### **Local oscillator frequency (Hz)** — 本振（LO）频率 `0.9e9`（默认）| 标量

本振（LO）频率，指定为以赫兹为单位的标量。

### **Reference input power (dBm)** — 参考输入功率 `-10`（默认）| 标量

参考输入功率，指定为以 dBm 为单位的标量。指定参考输入功率下归一化输入信号的表达式为：

10((−Prf+20log10(1Rin)+30)20)

互调表假设杂散电平是在参考输入和输出功率下测量的。例如，如果将输入功率增加 10 dB，则由二阶非线性引起的杂散将增加 20 dB，由三阶非线性引起的杂散将增加 30 dB，依此类推。

### **Nominal output power (dbm)** — 标称 LO 功率 `-20`（默认）| 标量

标称输出功率，指定为以 dBm 为单位的标量。指定参考输入功率下归一化输出信号的表达式为：

2x10((Pif−20log10(1Rout)−30)20)

### **Use data file** — 指定要使用的数据文件 `off`（默认）| `on`

选择此参数以指定要用于提取杂散表的数据文件。清除以指定您自己的杂散值。数据文件可以包含 S2D 或 P2D 格式的 IMT 表、AC 数据和有色点噪声的任意组合。参见 [4]。

### **Data file** — 数据文件 `samplespur1.s2d`（默认）

数据文件，指定为 IMT 数据、AC 数据和有色点噪声。要了解数据文件可以具有的输入组合以及此模块如何提取和计算参数，请参见使用数据文件时的模块参数。

#### 依赖关系

要设置此参数，请先选择 **Use data file**。

### **Input impedance (Ohm)** — 混频器的输入阻抗 `50`（默认）| 实标量 | 正实标量向量

混频器的输入阻抗，指定为以欧姆为单位的实标量或正实标量向量。

**注意**

对于非 50 欧姆的输入和输出阻抗，IMT 数据被归一化到 50 欧姆。

### **Output impedance (Ohm)** — 混频器的输出阻抗 `50`（默认）| 实标量 | 正实标量向量

混频器的输出阻抗，指定为以欧姆为单位的实标量或正实标量向量。

**注意**

对于非 50 欧姆的输入和输出阻抗，IMT 数据被归一化到 50 欧姆。

### **Ground and hide negative terminals** — 将 RF 负端电路端子接地 `on`（默认）| `off`

选择此参数以在内部将负端子接地并隐藏。要暴露负端子，请清除此参数。如果端子被暴露，输入信号不以地为参考。

#### IMT

### **IMT table** — IMT 杂散可视化 `[99 99 99; 99 0 99; 99 99 99]`（默认）| 方阵

IMT 杂散可视化，指定为方阵。

### **Output signal power (dBm)** — 期望输出音调的信号功率 `0`（默认）| 标量

绘制互调产物时期望输出音调的信号功率，指定为标量。

### **Mixer type** — 混频器类型 `Upconverter`（默认）| `Downconverter`

混频器类型，指定为 `Upconverter` 或
`Downconverter`。

对于由频率为
*FLO* 的本振信号非线性调制的单音载波 *Fcar*，
混频器输出互调产物出现在以下频率：

Fout(M,N)=|M×Fcar±N×FLO|

其中：

- *Fcar* – 输入射频
  信号载波频率
- *FLO* – 本地
  振荡器频率
- *M* 和 *N* 是非负
  整数（0,1,…, 非线性阶数）

对于下变频器，期望的输出音为 |Fcar−FLO|，对于上变频器为 |Fcar+FLO|。*M* 和
*N* 的所有其他组合表示杂散互调
产物。

### **Plot** — 使用指定的信号功率和混频器类型按钮可视化 IMT 表值

使用指定的信号功率和混频器
类型可视化 IMT 表值。

#### 噪声

### **Simulate noise** — 模拟器件噪声或相位噪声 `on`（默认）| `off`

选择此参数以按照模块参数
或文件中指定的方式模拟噪声。

如果在 `.s2p` 文件中指定了噪声，则将其
用于仿真。

### **Noise type** — 噪声类型 `Noise figure`（默认）| `Spot noise data`

噪声类型，指定为 `Noise figure` 或
`Spot noise data`。

#### 依赖关系

要设置此参数，请先选择 **Simulate
noise**。

### **Noise distribution** — 噪声分布 `White`（默认）| `Piece-wise linear` | `Colored`

噪声分布，指定为：

- `White` – 频谱密度为
  单个非负值。噪声的功率值取决于
  载波的带宽，而带宽取决于
  时间步长。这是一个不相关噪声源。
- `Piece-wise linear` – 频谱
  密度为值向量
  [*pi*]。对于每个
  载波，噪声源的行为类似于白不相关
  噪声。噪声源的功率取决于
  载波。
- `Colored` – 取决于载波
  和带宽。这是一个相关噪声源。

#### 依赖关系

要设置此参数，请先选择 **Simulate
noise**。

### **Noise figure (dB)** — 噪声系数 `0`（默认）| 标量

噪声系数，以分贝为单位指定为标量。

#### 依赖关系

要设置此参数，请先选择 **Simulate
noise**。

### **Frequencies (Hz)** — 频率数据 `0`（默认）| 标量 | 向量

频率数据，对于白噪声指定为标量，对于
分段线性或有色噪声指定为向量，单位为赫兹。

#### 依赖关系

要设置此参数，请先选择 **Select noise**，
然后在 **Noise
distribution** 中选择 `Piece-wise linear` 或
`Colored`。

### **Minimum noise figure (dB)** — 最小噪声系数 `0`（默认）| 标量 | 向量

最小噪声系数，以分贝为单位指定为标量或向量。

#### 依赖关系

要设置此参数，请先在 **Noise type** 中选择 `Spot noise
data`。

#### 依赖关系

要设置此参数，请先选择 **Select noise**，
然后在 **Noise Type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳反射系数 `0`（默认）| 标量 | 向量

最佳反射系数，指定为标量或向量。

#### 依赖关系

要设置此参数，请先选择 **Select noise**，
然后在 **Noise Type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 等效归一化噪声电阻 `0`（默认）| 标量 | 向量

等效归一化噪声电阻，指定为标量或
向量。

#### 依赖关系

要设置此参数，请先选择 **Select noise**，
然后在 **Noise Type** 中选择 `Spot noise data`。

### **Add LO phase noise** — 添加相位噪声 `off`（默认）| `on`

选择此参数以使用连续
波源向系统添加相位噪声。

#### 依赖关系

要设置此参数，请选择 **Simulate
noise**。

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `1`（默认）| 标量 | 向量

相对于 LO 信号的相位噪声频率偏移，指定为标量或向量，每个元素的单位为赫兹。

频率偏移值必须受仿真包络带宽的限制。有关详细信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请先选择 **Simulate noise**，然后选择 **Add phase noise**。

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `-Inf`（默认）| 标量 | 向量 | 矩阵

相位噪声电平，指定为标量、向量或矩阵，元素单位为分贝每赫兹。

如果指定矩阵，每一列应对应 CW 源的一个非直流载波频率。频率偏移值必须受仿真包络带宽的限制。有关详细信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请先选择 **Simulate noise**，然后选择 **Add phase noise**。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此参数可自动计算频率相关噪声的冲激响应。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请先选择 **Simulate noise**，然后选择 **Add phase noise**。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于仿真频率相关噪声的冲激响应持续时间，指定为以秒为单位的标量。该时间应为配置模块中步长的整数倍，`Tduration = NTstep`。

#### 依赖关系

要设置此参数，请先清除 **Automatically estimate impulse response duration**。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2022a：从数据文件中提取参考输入功率和标称输出功率

您现在可以从数据文件中提取参考输入功率和标称输出功率。有关详细信息，请参阅 Block Parameters When Using Data File。

### R2021b：IMT Mixer 模块图标已更新

从 R2021b 开始，IMT Mixer 模块图标已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 IMT Mixer 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

使用互调表（IMT）对混频器建模

使用 IMT Mixer 对单音载波与本振（LO）信号混频时在互调表中定义的频率变换执行操作（参见 [1]、[2]、[3] 和 [4]）。该模块包括非线性放大、器件和相位噪声以及混频器杂散可视化。对于频率为 *FLO* 的 LO 信号进行非线性调制的单音载波 *Fcar*，混频器输出互调产物出现在以下频率：

Fout(M,N)=|M×Fcar±N×FLO|

其中：

- *Fcar* – 输入 RF 信号载波频率
- *FLO* – 本振频率
- *M* 和 *N* 为非负整数（0,1,…, 非线性阶数）

对于下变频器，期望的输出音为 |Fcar−FLO|，对于上变频器为 |Fcar+FLO|。*M* 和 *N* 的所有其他组合表示杂散互调产物。

IMT Mixer 模块掩码图标是动态的，并指示所应用噪声参数的当前状态。有关详细信息，请参阅 IMT Mixer Icons。
