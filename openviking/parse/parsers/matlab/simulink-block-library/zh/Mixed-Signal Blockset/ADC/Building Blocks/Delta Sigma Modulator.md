---
type: simulink-block
title: 'Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Building Blocks'
documentation_page: 'deltasigmamodulator'
documentation_source_path: 'ref/deltasigmamodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Delta Sigma Modulator

## 端口
```yaml
ports:
- name: input
  summary: 模拟输入信号 标量
  direction: input
  data_types: double
- name: reset
  summary: 复位 delta-sigma 调制器 标量
  direction: input
  data_types: double
- name: feedback
  summary: 来自下一级的输出 标量
  direction: input
  data_types: double
- name: dsmOut
  summary: 数字输出信号 标量
  direction: output
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: filterOut
  summary: 环路滤波器输出 标量
  direction: output
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: quantOut
  summary: 量化器输出 标量
  direction: output
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### 输入

### **input** — 模拟输入信号 标量

模拟输入信号，指定为标量。

**数据类型：** `double`

### **reset** — 复位 delta-sigma 调制器 标量

Delta Sigma Modulator 模块的复位信号，指定为标量。

**数据类型：** `double`

### **feedback** — 来自下一级的输出 标量

来自下一级的输出。在对多级 DSM 进行建模时，使用此端口将输出反馈回该模块。如果下一级没有反馈，请将此端口连接到接地。

使用此端口可构建级联 DSM 结构，例如 MASH 和 S-MASH。

**数据类型：** `double`
### 输出

### **dsmOut** — 数字输出信号 标量

数字输出信号，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **filterOut** — 环路滤波器输出 标量

delta-sigma 调制器内部环路滤波器的输出，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **quantOut** — 量化器输出 标量

delta-sigma 调制器内部量化器的输出，以标量形式返回。如果不使用此端口，请将其连接到终止器。

如果不使用 **feedback** 端口，则 **quantOut** 和 **dsmOut** 端口具有相同的值。

使用此端口可构建级联 DSM 结构，例如 MASH 和 S-MASH。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## 参数
```yaml
parameters:
- name: Delta Sigma Modulator architecture
  summary: delta-sigma 调制器的架构 CIFB（默认）| CRFB | CIFF | CRFF
  group: ''
  block_parameter: dsmArchitecture
  type: 字符向量
  values: CIFB | CRFB | CIFF | CRFF
  default: CIFB
- name: Delta Sigma Modulator order
  summary: delta-sigma 调制器的阶数 2nd order（默认）| 1st order | 3rd order | 4th order | 5th order | 6th order
  group: ''
  block_parameter: dsmOrder
  type: 字符向量
  values: 1st order | 2nd order | 3rd order | 4th order | 5th order | 6th order
  default: 2nd order
- name: System bandwidth (Hz)
  summary: delta-sigma 调制器系统的带宽 1000（默认）| 非负实数标量
  group: 输入参数
  block_parameter: BandWidth
  type: 字符向量
  values: 非负实数标量
  default: '1000'
- name: OSR
  summary: delta-sigma 调制器采样率与奈奎斯特速率之比 64（默认）| 非负实数标量
  group: 输入参数
  block_parameter: OSR
  type: 字符向量
  values: 非负实数标量
  default: '64'
- name: Sampling frequency (Hz)
  summary: delta-sigma 调制器的采样频率 128e3（默认）| 正实数标量
  group: 输入参数
  block_parameter: SamplingFrequency
  type: 字符向量
  values: 正实数标量
  default: 128e3
- name: Quantizer levels
  summary: delta-sigma 调制器中的量化器级数 2（默认）| 正实数整数
  group: 输入参数
  block_parameter: NumberLevels
  type: character vector
  values: positive real scalar
  default: '2'
- name: Quantizer output
  summary: 量化器输出范围 [-1,1]（默认）| 实值向量
  group: 输入参数
  block_parameter: QuantizerOutput
  type: character vector
  values: real valued vector
  default: '[-1;1]'
- name: Enable dynamic range scaling
  summary: 启用系数的动态范围缩放 off（默认）| on
  group: 输入参数
- name: Use custom coefficient values
  summary: 使用系数 'a'、'g'、'b' 和 'c' 的自定义值的选项 off（默认）| on
  group: 输入参数
- name: Coefficient 'a'
  summary: 来自/到量化器的反馈/前馈系数 [0.1601 0.6515]（默认）| 实值向量
  group: 输入参数
  block_parameter: a
  type: character vector
  values: real valued vector
  default: '[0.1601 0.6515]'
- name: Coefficient 'g'
  summary: 谐振器系数 [0.0000]（默认）| 实值向量
  group: 输入参数
  block_parameter: g
  type: character vector
  values: real valued vector
  default: '[0.0000]'
- name: Coefficient 'b'
  summary: 从调制器输入到每个积分器的馈入系数 [0.1601 0.6515 1.0000]（默认）| 实值向量
  group: 输入参数
  block_parameter: b
  type: character vector
  values: real valued vector
  default: '[0.1601 0.6515 1.0000]'
- name: Coefficient 'c'
  summary: 积分器级间系数 [1.0000 1.0000]（默认）| 实值向量
  group: 输入参数
  block_parameter: c
  type: character vector
  values: real valued vector
  default: '[1.0000 1.0000]'
- name: Integrator opamp gain
  summary: 运算放大器的开环增益 Inf（默认）| 正实数标量
  group: Impairment
  block_parameter: OLgain
  type: character vector
  values: positive real scalar
  default: Inf
- name: Enable Noise Impairment
  summary: 启用 delta-sigma 调制器 ADC 中的噪声计算 off（默认）| on
  group: Impairment
- name: Thermal noise value
  summary: 热噪声密度 200e-6（默认）| 实数标量
  group: Impairment
  block_parameter: thermalNoiseValue
  type: 字符向量
  values: 实数标量
- name: Reference resistance (ohm)
  summary: 用于功率计算的参考电阻 50（默认）| 正实数标量
  group: Impairment
  block_parameter: refResistance
  type: 字符向量
  values: 正实数标量
- name: 1/f corner frequency (Hz)
  summary: 闪烁噪声的转角频率 1000（默认）| 正实数标量
  group: Impairment
  block_parameter: fcorner
  type: 字符向量
  values: 正实数标量
- name: NTF zeros opitimization flag
  summary: 优化 NTF 中零点的方法 2（默认）| 0 | 1
  group: 高级
  block_parameter: ntfOptim
  type: 字符向量
  values: 0 | 1 | 2
- name: Modulator passband
  summary: 调制器通带类型 Lowpass（默认）| Bandpass
  group: 高级
  block_parameter: passbandType
  type: 字符向量
  values: Lowpass | Bandpass
- name: Center frequency
  summary: 调制器中心频率 0（默认）| 范围 [0 0.5] 内的标量
  group: 高级
  block_parameter: centerFrequency
  type: 字符向量
  values: 范围 [0 0.5] 内的标量
- name: Use custom value of H_inf
  summary: 使用自定义 H_inf 值的选项 关（默认）| 开
  group: 高级
- name: Maximum out-of-band H_inf
  summary: NTF 的最大带外增益 1.4（默认）| 正实数标量
  group: 高级
  block_parameter: Hinf
  type: 字符向量
  values: 正实数标量
- name: Noise transfer function (NTF)
  summary: 绘制 NTF 开（默认）| 关
  group: 分析
- name: NTF pole-zero plot
  summary: 可视化 NTF 的极点零点位置 off（默认）| on
  group: 分析
- name: Signal transfer function (STF)
  summary: 绘制 STF（默认）|
  group: 分析
- name: Predict SNR
  summary: 预测二进制调制器的 SNR off（默认）| on
  group: 分析
- name: Append plots
  summary: 将图追加到当前图窗 off（默认）| on
  group: 分析
- name: Generate analysis plots
  summary: 绘制选定的分析函数 按钮
  group: 分析
- name: Export analysis data to workspace
  summary: 将分析数据导出到基础工作区 off（默认）| on
  group: 分析
```

### **Delta Sigma Modulator architecture** — delta-sigma 调制器的架构 `CIFB`（默认）| `CRFB` | `CIFF` | `CRFF`

delta-sigma 调制器的架构，指定为：

- `CIFB` — 反馈积分器级联
- `CRFB` — 反馈谐振器级联
- `CIFF` — 前馈积分器级联
- `CRFF` — 前馈谐振器级联

#### 编程用法

|  |
| --- |
| **模块参数：** `dsmArchitecture` |
| **类型：** 字符向量 |
| **值：** `CIFB` | `CRFB` | `CIFF` | `CRFF` |
| **默认值：** `CIFB` |

### **Delta Sigma Modulator order** — delta-sigma 调制器的阶数 `2nd order`（默认）| `1st order` | `3rd order` | `4th order` | `5th order` | `6th order`

delta-sigma 调制器的阶数。您可以选择一阶到六阶。

#### 编程用法

|  |
| --- |
| **模块参数：** `dsmOrder` |
| **类型：** 字符向量 |
| **值：** `1st order` | `2nd order` | `3rd order` | `4th order` | `5th order` | `6th order` |
| **默认值：** `2nd order` |

### 输入参数

### **System bandwidth (Hz)** — delta-sigma 调制器系统的带宽 `1000`（默认）| 非负实数标量

delta-sigma 调制器系统的带宽，指定为非负实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `BandWidth` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `1000` |

### **OSR** — delta-sigma 调制器采样率与奈奎斯特速率之比 `64`（默认）| 非负实数标量

delta-sigma 调制器采样率与奈奎斯特速率之比，指定为非负实数标量。较高的过采样比可放宽抗混叠滤波器的要求并降低带内量化噪声。

#### 编程用法

|  |
| --- |
| **模块参数：** `OSR` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `64` |

### **Sampling frequency (Hz)** — delta-sigma 调制器的采样频率 `128e3`（默认）| 正实数标量

delta-sigma 调制器的采样频率。此只读参数根据 **System bandwidth** 和 **OSR** 参数计算得出。

#### 编程用法

|  |
| --- |
| **模块参数：** `SamplingFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `128e3` |

### **Quantizer levels** — delta-sigma 调制器中的量化器级数 `2`（默认）| 正实数整数

delta-sigma 调制器中的量化器级数，指定为正实数整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumberLevels` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`2` |

### **Quantizer output** — 量化器输出范围 `[-1,1]`（默认）| 实值向量

delta-sigma 调制器架构中量化器输出的范围，以具有实数元素的向量形式返回。此参数为只读。

#### 编程使用

|  |
| --- |
| **模块参数：** `QuantizerOutput` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[-1;1]` |

### **Enable dynamic range scaling** — 启用系数的动态范围缩放 off（默认）| on

启用系数的动态范围缩放。这可防止内部状态过早饱和。

#### 依赖关系

当启用此参数时，**Use custom coefficient values** 选项被取消选择。

### **Use custom coefficient values** — 使用系数 'a'、'g'、'b' 和 'c' 的自定义值的选项 off（默认）| on

使用系数 'a'、'g'、'b' 和 'c' 的自定义值。

#### 依赖关系

当启用此参数时，**Enable dynamic range scaling** 选项被取消选择。

### **Coefficient 'a'** — 来自/到量化器的反馈/前馈系数 `[0.1601 0.6515]`（默认）| 实值向量

来自量化器的反馈系数或到量化器的前馈系数，指定为具有实数元素的向量。

#### 依赖关系

要启用此参数，请选择 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `a` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[0.1601 0.6515]` |

### **Coefficient 'g'** — 谐振器系数 `[0.0000]`（默认）| 实值向量

谐振器系数，指定为具有实数元素的向量。

#### 依赖关系

要启用此参数，请选择 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `g` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[0.0000]` |

### **Coefficient 'b'** — 从调制器输入到每个积分器的馈入系数 `[0.1601 0.6515 1.0000]`（默认）| 实值向量

从调制器输入到每个积分器的馈入系数，指定为具有实数元素的向量。

#### 依赖关系

要启用此参数，请选择 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `b` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[0.1601 0.6515 1.0000]` |

### **Coefficient 'c'** — 积分器级间系数 `[1.0000 1.0000]`（默认）| 实值向量

积分器级间系数，指定为具有实数元素的向量。

#### 依赖关系

要启用此参数，请选择 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `c` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[1.0000 1.0000]` |

### Impairment

### **Integrator opamp gain** — 运算放大器的开环增益 `Inf`（默认）| 正实数标量

内部运算放大器的开环增益，指定为正实数标量。此参数用于噪声传递函数（NTF）的分析。理想 NTF 假设运算放大器增益为无穷大。

#### 编程使用

|  |
| --- |
| **模块参数：** `OLgain` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`Inf` |

### **Enable Noise Impairment** — 启用 delta-sigma 调制器 ADC 中的噪声计算 off（默认）| on

启用 delta-sigma 调制器 ADC 中的噪声计算。

### **Thermal noise value** — 热噪声密度 `200e-6`（默认）| 实数标量

热噪声密度，以 Vrms 或 dB/Hz 为单位指定。

当以 Vrms 为单位指定热噪声时，此参数的值必须为非负实数标量。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `thermalNoiseValue` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0.125` |

### **Reference resistance (ohm)** — 用于功率计算的参考电阻 `50`（默认）| 正实数标量

用于功率计算的参考噪声，以欧姆为单位指定为正实数标量。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `refResistance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `50` |

### **1/f corner frequency (Hz)** — 闪烁噪声的转角频率 `1000`（默认）| 正实数标量

闪烁（1/f）噪声的转角频率，以 Hz 为单位指定为正实数标量。在该频率处，1/f 噪声近似等于热噪声。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `fcorner` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1000` |

### 高级

### **NTF zeros opitimization flag** — 优化 NTF 中零点的方法 `2`（默认）| `0` | `1`

模块用于优化 NTF 中零点的方法：

- `0` — 不优化
- `1` — 优化
- `2` — 优化，且至少有一个零点位于频带中心

#### 编程使用

|  |
| --- |
| **模块参数：** `ntfOptim` |
| **类型：** 字符向量 |
| **值：** `0` | `1` | `2` |
| **默认：** `2` |

### **Modulator passband** — 调制器通带类型 `Lowpass`（默认）| `Bandpass`

Delta-Sigma 调制器的通带类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `passbandType` |
| **类型：** 字符向量 |
| **值：** `Lowpass` | `Bandpass` |
| **默认：** `Lowpass` |

### **Center frequency** — 调制器中心频率 `0`（默认）| 范围 [0 0.5] 内的标量

调制器的中心频率，指定为范围 [0 0.5] 内的标量。对于低通滤波器，中心频率为零。

#### 依赖关系

要启用此参数，请将 **Modulator passband** 参数设置为 `Bandpass`。

#### 编程使用

|  |
| --- |
| **模块参数：** `centerFrequency` |
| **类型：** 字符向量 |
| **值：** 范围 [0 0.5] 内的标量 |
| **默认：** `0` |

### **Use custom value of H\_inf** — 使用自定义 H\_inf 值的选项 关（默认）| 开

选中此参数以使用 H\_inf 的自定义值。默认情况下，此选项处于清除状态。

### **Maximum out-of-band H\_inf** — NTF 的最大带外增益 `1.4`（默认）| 正实数标量

NTF 的最大带外增益。

Lee 准则指出，*H\_inf* < 2 时可得到具有二进制量化器的稳定调制器。减小 *H\_inf* 会增加成功的可能性，但会降低 NTF 提供的衰减幅度以及调制器的理论分辨率。

#### 依赖关系

要启用此参数，请选中 **Use custom value of H\_inf** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `Hinf` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1.4` |

**注意**

使用 **Advanced** 选项卡中的参数需要 Control System Toolbox™ 许可证。

### 分析

### **Noise transfer function (NTF)** — 绘制 NTF 开（默认）| 关

选中此项可在生成分析图时绘制噪声传递函数（NTF）。

### **NTF pole-zero plot** — 可视化 NTF 的极点零点位置 off（默认）| on

选择此项可在生成分析图时可视化 NTF 的极点零点位置。

### **Signal transfer function (STF)** — 绘制 STF（默认）|

选择此项可在生成分析图时绘制信号传递函数（STF）。

### **Predict SNR** — 预测二进制调制器的 SNR off（默认）| on

选择此项可预测二进制调制器的信噪比（SNR）。

如果 **Quantizer levels** 设置为 `2` 以外的任何值，此选项将被禁用。

### **Append plots** — 将图追加到当前图窗 off（默认）| on

选择此项可将新的分析图追加到当前图窗。

### **Generate analysis plots** — 绘制选定的分析函数 按钮

绘制选定的分析函数：NTF、STF、NTF 极点零点图和预测 SNR。

### **Export analysis data to workspace** — 将分析数据导出到基础工作区 off（默认）| on

选择此项可将分析数据以结构体形式导出到基础工作区。该结构体包含 NTF、STF、最大 SNR 和最大稳定幅度（MSA）。

要导出数据，请点击 **Generate analysis plots** 按钮。

**注意**

您需要 Control System Toolbox 许可证才能使用 **Analysis** 选项卡中的参数。

**注意**

分析结果仅包含 **Integrator opamp gain** 参数中定义的有限运放增益的影响。该模块在估计 **Analysis** 选项卡中的结果时忽略热噪声的影响。
## 所属库

Mixed-Signal Blockset / ADC / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024a：绘制 NTF 和 STF

绘制二进制调制器的噪声传递函数（NTF）、信号传递函数（STF）和预测 SNR。

### R2023b：基于过采样比和带宽生成系数

使用动态范围缩放规格生成 delta-sigma 调制器系数 *a*、*g*、*b* 和 *c*，用于晶体管级设计。

## 描述

基于 delta-sigma 调制器的 ADC

Delta Sigma Modulator 模块使用四种不同的架构集对基于 delta-sigma 调制器的 ADC 进行建模。

- 带反馈的谐振器级联（CRFB）
- 带反馈的积分器级联（CIFB）
- 带前馈的谐振器级联（CRFF）
- 带前馈的积分器级联（CIFF）

您可以对一阶到六阶的 DSM 进行建模。您还可以使用该模块设计级联结构，例如多级噪声整形（MASH）和坚固 MASH（S-MASH）。您还可以对基于电路的噪声进行建模。您可以绘制噪声传递函数（NTF）、信号传递函数（STF），并预测信噪比（SNR）。
