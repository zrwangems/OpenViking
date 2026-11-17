---
type: simulink-block
title: 'Continuous Time Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Building Blocks'
documentation_page: 'continuoustimedeltasigmamodulator'
documentation_source_path: 'ref/continuoustimedeltasigmamodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Continuous Time Delta Sigma Modulator

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

来自下一级的输出。在对多级 DSM 建模时，使用此端口将输出反馈回该模块。如果下一级没有反馈，请将此端口连接到接地。

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
  summary: delta-sigma 调制器的架构 CIFB（默认）| CIFF
  group: ''
  block_parameter: dsmArchitecture
  type: 字符向量
  values: CIFB | CIFF
- name: Delta Sigma Modulator order
  summary: delta-sigma 调制器的阶数 2nd order（默认）| 1st order | 3rd order | 4th order
  group: ''
  block_parameter: dsmOrder
  type: 字符向量
  values: 1st order | 2nd order | 3rd order | 4th order
- name: System bandwidth (Hz)
  summary: delta-sigma 调制器系统的带宽 1000（默认）| 非负实数标量
  group: 输入参数
  block_parameter: BandWidth
  type: 字符向量
  values: 非负实数标量
- name: OSR
  summary: delta-sigma 调制器采样率与奈奎斯特速率之比 64（默认）| 非负实数标量
  group: 输入参数
  block_parameter: OSR
  type: 字符向量
  values: 非负实数标量
- name: Sampling frequency (Hz)
  summary: delta-sigma 调制器的采样频率 128e3（默认）| 正实数标量
  group: 输入参数
  block_parameter: SamplingFrequency
  type: 字符向量
  values: 正实数标量
- name: Quantizer levels
  summary: delta-sigma 调制器中的量化器级数 2（默认）| 正实数整数
  group: 输入参数
  block_parameter: NumberLevels
  type: 字符向量
  values: 正实数标量
- name: Quantizer output
  summary: 量化器输出范围 [-1,1]（默认）| 实值向量
  group: 输入参数
  block_parameter: QuantizerOutput
  type: 字符向量
  values: 实值向量
- name: Use custom coefficient values
  summary: 使用系数 'a'、'g'、'b' 和 'c' 的自定义值的选项 off（默认）| on
  group: 输入参数
- name: Coefficient 'a'
  summary: 来自/去往量化器的反馈/前馈系数 [0.5714 0.1601]（默认）| 实值向量
  group: 输入参数
  block_parameter: a
  type: 字符向量
  values: 实值向量
- name: Coefficient 'g'
  summary: 谐振器系数 [0.0000]（默认）| 实值向量
  group: 输入参数
  block_parameter: g
  type: 字符向量
  values: 实值向量
- name: Coefficient 'b'
  summary: 从调制器输入到每个积分器的馈入系数 [1.000 0.5714 0.1601]（默认）| 实值向量
  group: 输入参数
  block_parameter: b
  type: 字符向量
  values: 实值向量
- name: Coefficient 'c'
  summary: 积分器级间系数 [1.0000 1.0000]（默认）| 实值向量
  group: 输入参数
  block_parameter: c
  type: 字符向量
  values: 实值向量
- name: Integrator opamp gain
  summary: 运算放大器的开环增益 Inf（默认）| 正实数标量
  group: Impairment
  block_parameter: OLgain
  type: 字符向量
  values: 正实数标量
- name: Enable Noise Impairment
  summary: 启用 delta-sigma 调制器 ADC 中的噪声计算 off（默认）| on
  group: Impairment
- name: Thermal noise value
  summary: 热噪声密度 200e-6（默认）| 实数标量
  group: Impairment
  block_parameter: thermalNoiseValue
  type: 字符向量
  values: 实数标量
  default: '0.125'
- name: 参考电阻 (ohm)
  summary: 用于功率计算的参考电阻 50（默认）| 正实数标量
  group: Impairment
  block_parameter: refResistance
  type: 字符向量
  values: 正实数标量
  default: '50'
- name: 1/f 转角频率 (Hz)
  summary: 闪烁噪声的转角频率 1000（默认）| 正实数标量
  group: Impairment
  block_parameter: fcorner
  type: 字符向量
  values: 正实数标量
  default: '1000'
- name: NTF 零点优化标志
  summary: 优化 NTF 中零点的方法 2（默认）| 0 | 1
  group: 高级
  block_parameter: ntfOptim
  type: 字符向量
  values: 0 | 1 | 2
  default: '2'
- name: 调制器通带
  summary: 调制器通带的类型 Lowpass（默认）| Bandpass
  group: 高级
  block_parameter: passbandType
  type: 字符向量
  values: Lowpass | Bandpass
  default: Lowpass
- name: 中心频率
  summary: 调制器的中心频率 0（默认）| 范围 [0 0.5] 内的标量
  group: 高级
  block_parameter: centerFrequency
  type: 字符向量
  values: 范围 [0 0.5] 内的标量
  default: '0'
- name: 使用自定义 H_inf 值
  summary: 使用自定义 H_inf 值的选项 off（默认）| on
  group: 高级
- name: 最大带外 H_inf
  summary: NTF 的最大带外增益 1.4（默认）| 正实数标量
  group: 高级
  block_parameter: Hinf
  type: 字符向量
  values: 正实数标量
  default: '1.4'
```

### **Delta Sigma Modulator architecture** — delta-sigma 调制器的架构 `CIFB`（默认）| `CIFF`

delta-sigma 调制器的架构，指定为：

- `CIFB` — 反馈积分器级联
- `CIFF` — 前馈积分器级联

#### 编程使用

|  |
| --- |
| **模块参数：** `dsmArchitecture` |
| **类型：** 字符向量 |
| **值：** `CIFB` | `CIFF` |
| **默认：** `CIFB` |

### **Delta Sigma Modulator order** — delta-sigma 调制器的阶数 `2nd order`（默认）| `1st order` | `3rd order` | `4th order`

delta-sigma 调制器的阶数。您可以选择一阶到四阶。

#### 编程使用

|  |
| --- |
| **模块参数：** `dsmOrder` |
| **类型：** 字符向量 |
| **值：** `1st order` | `2nd order` | `3rd order` | `4th order` |
| **默认：** `2nd order` |

### 输入参数

### **System bandwidth (Hz)** — delta-sigma 调制器系统的带宽 `1000`（默认）| 非负实数标量

delta-sigma 调制器系统的带宽，指定为非负实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `BandWidth` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `1000` |

### **OSR** — delta-sigma 调制器采样率与奈奎斯特速率之比 `64`（默认）| 非负实数标量

delta-sigma 调制器采样率与奈奎斯特速率之比，指定为非负实数标量。较高的过采样比可放宽抗混叠滤波器要求并降低带内量化噪声。

#### 编程使用

|  |
| --- |
| **模块参数：** `OSR` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `64` |

### **Sampling frequency (Hz)** — delta-sigma 调制器的采样频率 `128e3`（默认）| 正实数标量

delta-sigma 调制器的采样频率。此只读参数根据 **System bandwidth** 和 **OSR** 参数计算得出。

#### 编程使用

|  |
| --- |
| **模块参数：** `SamplingFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `128e3` |

### **Quantizer levels** — delta-sigma 调制器中的量化器级数 `2`（默认）| 正实数整数

delta-sigma 调制器中的量化器级数，指定为正实数整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumberLevels` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `2` |

### **Quantizer output** — 量化器输出范围 `[-1,1]`（默认）| 实值向量

delta-sigma 调制器架构中量化器输出的范围，以包含实数元素的向量形式返回。此参数为只读。

#### 编程使用

|  |
| --- |
| **模块参数：** `QuantizerOutput` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[-1;1]` |

### **Use custom coefficient values** — 使用系数 'a'、'g'、'b' 和 'c' 的自定义值的选项 off（默认）| on

使用系数 'a'、'g'、'b' 和 'c' 的自定义值。

### **Coefficient 'a'** — 来自/去往量化器的反馈/前馈系数 `[0.5714 0.1601]`（默认）| 实值向量

来自量化器的反馈系数或去往量化器的前馈系数，指定为包含实数元素的向量。

#### 依赖关系

要启用此参数，请选中 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `a` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[0.5714 0.1601]` |

### **Coefficient 'g'** — 谐振器系数 `[0.0000]`（默认）| 实值向量

谐振器系数，指定为包含实数元素的向量。

#### 依赖关系

要启用此参数，请选中 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[0.0000]` |

### **Coefficient 'b'** — 从调制器输入到每个积分器的馈入系数 `[1.000 0.5714 0.1601]`（默认）| 实值向量

从调制器输入到每个积分器的馈入系数，指定为包含实数元素的向量。

#### 依赖关系

要启用此参数，请选中 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[1.000 0.5714 0.1601]` |

### **Coefficient 'c'** — 积分器级间系数 `[1.0000 1.0000]`（默认）| 实值向量

积分器级间系数，指定为包含实数元素的向量。

#### 依赖关系

要启用此参数，请选中 **Use custom coefficient values** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[1.0000 1.0000]` |

### Impairment

### **Integrator opamp gain** — 运算放大器的开环增益 `Inf`（默认）| 正实数标量

内部运算放大器的开环增益，指定为正实数标量。此参数用于噪声传递函数（NTF）的分析。理想 NTF 假设运算放大器增益为无穷大。

#### 编程使用

|  |
| --- |
| **模块参数：** `OLgain` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `Inf` |

### **Enable Noise Impairment** — 启用 delta-sigma 调制器 ADC 中的噪声计算 off（默认）| on

启用 delta-sigma 调制器 ADC 中的噪声计算。

### **Thermal noise value** — 热噪声密度 `200e-6`（默认）| 实数标量

热噪声密度，以 Vrms 或 dB/Hz 为单位指定。

当以 Vrms 为单位指定热噪声时，此参数的值必须为非负实数标量。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `thermalNoiseValue` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `0.125` |

### **参考电阻 (ohm)** — 用于功率计算的参考电阻 `50`（默认）| 正实数标量

用于功率计算的参考噪声，指定为以欧姆为单位的正实数标量。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `refResistance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `50` |

### **1/f 转角频率 (Hz)** — 闪烁噪声的转角频率 `1000`（默认）| 正实数标量

闪烁 (1/f) 噪声的转角频率，指定为以 Hz 为单位的正实数标量。在该频率处，1/f 噪声近似等于热噪声。

#### 依赖关系

要启用此参数，请选中 **Enable Noise Impairment** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `fcorner` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `1000` |

### 高级

### **NTF 零点优化标志** — 优化 NTF 中零点的方法 `2`（默认）| `0` | `1`

模块用于优化 NTF 中零点的方法：

- `0` — 未优化
- `1` — 已优化
- `2` — 已优化，且至少有一个零点位于频带中心

#### 编程用法

|  |
| --- |
| **模块参数：** `ntfOptim` |
| **类型：** 字符向量 |
| **值：** `0` | `1` | `2` |
| **默认值：** `2` |

### **调制器通带** — 调制器通带的类型 `Lowpass`（默认）| `Bandpass`

Delta-Sigma 调制器的通带类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `passbandType` |
| **类型：** 字符向量 |
| **值：** `Lowpass` | `Bandpass` |
| **默认值：** `Lowpass` |

### **中心频率** — 调制器的中心频率 `0`（默认）| 范围 [0 0.5] 内的标量

调制器的中心频率，指定为范围 [0 0.5] 内的标量。对于低通滤波器，中心频率为零。

#### 依赖关系

要启用此参数，请将 **Modulator passband** 参数设置为 `Bandpass`。

#### 编程用法

|  |
| --- |
| **模块参数：** `centerFrequency` |
| **类型：** 字符向量 |
| **值：** 范围 [0 0.5] 内的标量 |
| **默认值：** `0` |

### **使用自定义 H\_inf 值** — 使用自定义 H\_inf 值的选项 off（默认）| on

选中此参数以使用 H\_inf 的自定义值。默认情况下，此选项处于清除状态。

### **最大带外 H\_inf** — NTF 的最大带外增益 `1.4`（默认）| 正实数标量

NTF 的最大带外增益。

Lee 法则指出，*H\_inf* < 2 时可得到使用二值量化器的稳定调制器。减小 *H\_inf* 会增加成功的可能性，但会降低 NTF 提供的衰减幅度以及调制器的理论分辨率。

#### 依赖关系

要启用此参数，请选中 **Use custom value of H\_inf** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `Hinf` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `1.4` |

**注意**

您需要 Control System Toolbox™ 许可证才能使用 **Advanced** 选项卡中的参数。
## 所属库

Mixed-Signal Blockset / ADC / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

基于连续时间 delta-sigma 调制器的 ADC

Continuous Time Delta Sigma Modulator 模块使用两种不同的架构集对基于连续时间 delta-sigma 调制器的 ADC 进行建模。

- 带反馈的积分器级联（CIFB）
- 带前馈的积分器级联（CIFF）

您可以对一阶到四阶的连续时间 DSM 进行建模。您还可以使用该模块设计级联结构，例如多级噪声整形（MASH）和稳固 MASH（S-MASH）。
