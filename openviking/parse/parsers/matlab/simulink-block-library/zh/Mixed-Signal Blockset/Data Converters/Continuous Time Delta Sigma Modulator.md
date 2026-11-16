---
type: simulink-block
title: 'Continuous Time Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Data Converters'
documentation_page: 'continuoustimedeltasigmamodulator'
documentation_source_path: 'ref/continuoustimedeltasigmamodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Continuous Time Delta Sigma Modulator

## 端口

### 输入

### **input** — 模拟输入信号标量

模拟输入信号，指定为标量。

**数据类型：** `double`

### **reset** — 复位 delta-sigma 调制器标量

Delta Sigma Modulator 模块的复位信号，指定为标量。

**数据类型：** `double`

### **feedback** — 来自下一级的输出标量

来自下一级的输出。在对多级 DSM 建模时，使用此端口将输出反馈回模块中。如果下一级没有反馈，请将此端口接地。

使用此端口构建级联 DSM 结构，例如 MASH 和 S-MASH。

**数据类型：** `double`

### 输出

### **dsmOut** — 数字输出信号标量

数字输出信号，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **filterOut** — 环路滤波器输出标量

delta-sigma 调制器内部环路滤波器的输出，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **quantOut** — 量化器输出标量

delta-sigma 调制器内部量化器的输出，以标量形式返回。如果不使用此端口，请将其连接到终结器。

如果不使用 **feedback** 端口，则 **quantOut** 和 **dsmOut** 端口具有相同的值。

使用此端口构建级联 DSM 结构，例如 MASH 和 S-MASH。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Delta Sigma Modulator 架构** — delta-sigma 调制器的架构 `CIFB` (默认) | `CIFF`

delta-sigma 调制器的架构，指定为：

- `CIFB` — 反馈积分器级联
- `CIFF` — 前馈积分器级联

#### 程序化使用

|  |
| --- |
| **模块参数：** `dsmArchitecture` |
| **类型：** character vector |
| **取值：** `CIFB` | `CIFF` |
| **默认值：** `CIFB` |

### **Delta Sigma Modulator 阶数** — delta-sigma 调制器的阶数 `2nd order` (默认) | `1st order` | `3rd order` | `4th order`

delta-sigma 调制器的阶数。您可以选择一阶到四阶。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dsmOrder` |
| **类型：** character vector |
| **取值：** `1st order` | `2nd order` | `3rd order` | `4th order` |
| **默认值：** `2nd order` |

### 输入参数

### **系统带宽 (Hz)** — delta-sigma 调制器系统的带宽 `1000` (默认) | nonnegative real scalar

delta-sigma 调制器系统的带宽，指定为非负实标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BandWidth` |
| **类型：** character vector |
| **取值：** nonnegative real scalar |
| **默认值：** `1000` |

### **OSR** — delta-sigma 调制器采样率与 Nyquist 速率之比 `64` (默认) | nonnegative real scalar

delta-sigma 调制器采样率与 Nyquist 速率之比，指定为非负实标量。较高的过采样比可放宽抗混叠滤波器要求并降低带内量化噪声。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OSR` |
| **类型：** character vector |
| **取值：** nonnegative real scalar |
| **默认值：** `64` |

### **采样频率 (Hz)** — delta-sigma 调制器的采样频率 `128e3` (默认) | positive real scalar

delta-sigma 调制器的采样频率。此只读参数根据 **系统带宽** 和 **OSR** 参数计算得出。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SamplingFrequency` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `128e3` |

### **量化器电平数** — delta-sigma 调制器中量化器的电平数 `2` (默认) | positive real integer

delta-sigma 调制器中量化器的电平数，指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumberLevels` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `2` |

### **量化器输出** — 量化器输出的范围 `[-1,1]` (默认) | real-valued vector

delta-sigma 调制器架构中量化器输出的范围，以包含实数的向量形式返回。此参数为只读。

#### 程序化使用

|  |
| --- |
| **模块参数：** `QuantizerOutput` |
| **类型：** character vector |
| **取值：** real valued vector |
| **默认值：** `[-1;1]` |

### **使用自定义系数值** — 使用系数 'a'、'g'、'b' 和 'c' 的自定义值的选项 off (默认) | on

### **系数 'a'** — 来自/去往量化器的反馈/前馈系数 `[0.5714 0.1601]` (默认) | real-valued vector

来自量化器的反馈系数或去往量化器的前馈系数，指定为包含实数的向量。

#### 依赖关系

要启用此参数，请选择 **使用自定义系数值** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `a` |
| **类型：** character vector |
| **取值：** real valued vector |
| **默认值：** `[0.5714 0.1601]` |

### **系数 'g'** — 谐振器系数 `[0.0000]` (默认) | real-valued vector

谐振器系数，指定为包含实数的向量。

#### 依赖关系

要启用此参数，请选择 **使用自定义系数值** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** character vector |
| **取值：** real valued vector |
| **默认值：** `[0.0000]` |

### **系数 'b'** — 从调制器输入到每个积分器的馈入系数 `[1.000 0.5714 0.1601]` (默认) | real-valued vector

从调制器输入到每个积分器的馈入系数，指定为包含实数的向量。

#### 依赖关系

要启用此参数，请选择 **使用自定义系数值** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** character vector |
| **取值：** real valued vector |
| **默认值：** `[1.000 0.5714 0.1601]` |

### **系数 'c'** — 积分器级间系数 `[1.0000 1.0000]` (默认) | real-valued vector

积分器级间系数，指定为包含实数的向量。

#### 依赖关系

要启用此参数，请选择 **使用自定义系数值** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** character vector |
| **取值：** real valued vector |
| **默认值：** `[1.0000 1.0000]` |

### 损伤

### **积分器运放增益** — 运算放大器的开环增益 `Inf` (默认) | positive real scalar

内部运算放大器的开环增益，指定为正实标量。此参数用于分析噪声传递函数 (NTF)。理想 NTF 假设运放增益为无穷大。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OLgain` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `Inf` |

### **启用噪声损伤** — 在 delta-sigma 调制器 ADC 中启用噪声计算 off (默认) | on

### **热噪声值** — 热噪声密度 `200e-6` (默认) | real scalar

热噪声密度，以 Vrms 或 dB/Hz 为单位指定。

当以 Vrms 为单位指定热噪声时，此参数的值必须为非负实标量。

#### 依赖关系

要启用此参数，请选择 **启用噪声损伤** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `thermalNoiseValue` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认值：** `0.125` |

### **参考电阻 (ohm)** — 用于功率计算的参考电阻 `50` (默认) | positive real scalar

用于功率计算的参考电阻，指定为以 ohm 为单位的正实标量。

#### 依赖关系

要启用此参数，请选择 **启用噪声损伤** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `refResistance` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `50` |

### **1/f 拐角频率 (Hz)** — 闪烁噪声的拐角频率 `1000` (默认) | positive real scalar

闪烁 (1/f) 噪声的拐角频率，指定为以 Hz 为单位的正实标量。在此频率处，1/f 噪声约等于热噪声。

#### 依赖关系

要启用此参数，请选择 **启用噪声损伤** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fcorner` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `1000` |

### 高级

### **NTF 零点优化标志** — 优化 NTF 中零点的方法 `2` (默认) | `0` | `1`

该模块用于优化 NTF 中零点的方法：

- `0` — 未优化
- `1` — 优化
- `2` — 优化，且至少一个零点位于频带中心

#### 程序化使用

|  |
| --- |
| **模块参数：** `ntfOptim` |
| **类型：** character vector |
| **取值：** `0` | `1` | `2` |
| **默认值：** `2` |

### **调制器通带** — 调制器通带的类型 `Lowpass` (默认) | `Bandpass`

delta-sigma 调制器的通带类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `passbandType` |
| **类型：** character vector |
| **取值：** `Lowpass` | `Bandpass` |
| **默认值：** `Lowpass` |

### **中心频率** — 调制器的中心频率 `0` (默认) | scalar in the range [0 0.5]

调制器的中心频率，指定为范围 [0 0.5] 中的标量。对于低通滤波器，中心频率为零。

#### 依赖关系

要启用此参数，请将 **调制器通带** 参数设置为 `Bandpass`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `centerFrequency` |
| **类型：** character vector |
| **取值：** scalar in the range [0 0.5] |
| **默认值：** `0` |

### **使用 H\_inf 的自定义值** — 使用 H\_inf 自定义值的选项 off (默认) | on

选择此参数以使用 H\_inf 的自定义值。默认情况下，此选项处于清除状态。

### **最大带外 H\_inf** — NTF 的最大带外增益 `1.4` (默认) | positive real scalar

NTF 的最大带外增益。

Lee 规则指出，*H\_inf* < 2 可产生具有二进制量化器的稳定调制器。降低 *H\_inf* 会增加成功的可能性，但会降低 NTF 提供的衰减幅度以及调制器的理论分辨率。

#### 依赖关系

要启用此参数，请选择 **使用 H\_inf 的自定义值** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Hinf` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认值：** `1.4` |

**注意**

您需要 Control System Toolbox™ 许可证才能使用 **高级** 选项卡中的参数。

## 所属库

Mixed-Signal Blockset / ADC / Building Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

基于连续时间 delta-sigma 调制器的 ADC

Continuous Time Delta Sigma Modulator 模块使用两组不同的架构，对基于连续时间 delta-sigma 调制器的 ADC 进行建模。

- 带反馈的积分器级联 (CIFB)
- 带前馈的积分器级联 (CIFF)

您可以对一阶至四阶的连续时间 DSM 进行建模。您还可以使用该模块设计级联结构，例如多级噪声整形 (MASH) 和稳固 MASH (S-MASH)。
