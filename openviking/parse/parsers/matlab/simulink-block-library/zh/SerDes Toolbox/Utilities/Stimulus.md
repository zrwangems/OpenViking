---
type: simulink-block
title: 'Stimulus'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'stimulus'
documentation_source_path: 'ref/stimulus.html'
language: zh-CN
chinese_source: worker-translation
---

# Stimulus

## 端口
```yaml
ports:
- name: WaveOut
  summary: 具有特定 PRBS 模式向量的输出信号
  direction: output
  data_types: double
```

### 输出

### **WaveOut** — 具有特定 PRBS 模式向量的输出信号

具有特定 PRBS 模式的输出模式，指定为向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Number of symbols
  summary: 用于仿真的激励模式长度 20000（默认）| 正实数整数
  group: Stimulus
  block_parameter: NumberOfSymbols
  type: 字符向量
  values: 正实数整数
- name: Use recommended simulation stop time
  summary: 将推荐的仿真停止时间设置为仿真停止时间 开（默认）| 关
  group: Stimulus
- name: Waveform creation method
  summary: 定义激励波形的创建方式 Random Symbols（默认）| Serial PRBS | Symbol Pattern | Binary Pattern | Symbol Voltage Pattern | Sampled
    Voltage | Parallel PRBS
  group: Stimulus
  block_parameter: CreationMethod
  type: 字符向量
  values: Random Symbols | Serial PRBS | Symbol Pattern | Binary Pattern | Symbol Voltage Pattern | Sampled Voltage | Parallel
    PRBS
- name: Random symbols seed
  summary: 用于生成随机符号波形的种子 1431655765（默认）| 正实数标量
  group: Stimulus
  block_parameter: soPAMnSeed
  type: 字符向量
  values: 正实数标量
- name: PRBS order
  summary: 伪随机二进制序列的阶数 11（默认）| 7 | 9 | 13 | 15 | 20 | 23 | 31 | 47
  group: Stimulus
  block_parameter: PRBS
  type: 字符向量
  values: 7 | 9 | 11 | 13 | 15 | 20 | 23 | 31 | 47
- name: PRBS seed
  summary: 伪随机二进制序列的种子 1（默认）| 范围 [1, 2Order-1] 内的整数
  group: Stimulus
  block_parameter: PRBSSeed
  type: 字符向量
  values: 范围 [1, 2Order-1] 内的整数
  default: '1'
- name: Reverse PRBS in time
  summary: 通过反转特征多项式的抽头位置在时间上反转 PRBS 关闭（默认）| 打开
  group: Stimulus
- name: Invert PRBS in voltage
  summary: 通过翻转 0 和 1 的值在电压上反转 PRBS 关闭（默认）| 打开
  group: Stimulus
- name: Symbol pattern
  summary: 以符号时间间隔间隔的符号整数向量 [0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]（默认）| 元素值在范围 [0, (Number of modulation levels-1)] 内的向量
  group: Stimulus
  block_parameter: SymbolPattern
  type: 字符向量
  values: 元素值在范围 [0, (Number of modulation levels-1)] 内的向量
  default: '[0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]'
- name: Binary pattern
  summary: 以采样时间间隔间隔的 1 和 0 向量 [0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]（默认）| 具有二进制元素的向量
  group: Stimulus
  block_parameter: BinaryPattern
  type: 字符向量
  values: 具有二进制元素的向量
  default: '[0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]'
- name: Symbol voltage pattern
  summary: 以符号时间间隔间隔的符号电压向量 1/2*[1 1 1 1 -1 -1 -1 -1]（默认）| 具有十进制值的向量
  group: Stimulus
  block_parameter: SymbolVoltageDataPattern
  type: 字符向量
  values: 具有十进制值的向量
  default: 1/2*[1 1 1 1 -1 -1 -1 -1]
- name: Sampled voltage pattern
  summary: 以采样间隔间隔的电压向量 [zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5（默认）| 实值向量
  group: Stimulus
  block_parameter: CustomStimulus
  type: 字符向量
  values: 实值向量
  default: '[zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5'
- name: Sub symbol time delay (s)
  summary: 将激励波形延迟模符号时间 0（默认）| 非负实数标量
  group: Stimulus
  block_parameter: soDelay
  type: 字符向量
  values: 非负实数标量
  default: '0'
- name: Change in IBIS-AMI Manager
  summary: 修改 Rx_Use_Clock_Input 保留 AMI 参数按钮
  group: 时钟转发
- name: Generate Clock or Strobe Waveform
  summary: 从波形参数生成时钟或选通波形 关（默认）| 开
  group: 时钟转发
- name: Use External Waveform or Clock Times Array
  summary: 使用外部波形进行转发 开（默认）| 关
  group: 时钟转发
- name: Include Analog Channel Model in clock waveform
  summary: 在时钟波形中包含模拟通道模型 开（默认）| 关
  group: 时钟转发
- name: Clock Pattern
  summary: 转发时钟模式 关（默认）| 开
  group: 时钟转发
- name: Strobe Pattern
  summary: 转发选通模式 开（默认）| 关
  group: 时钟转发
- name: Delay (s)
  summary: 延迟转发时钟 0（默认）| 非负实数标量
  group: 时钟转发
  block_parameter: CF_Delay
  type: 字符向量
  values: 非负实数标量
- name: Burst Length
  summary: 选通突发模式之间的符号数 16（默认）| 非负标量整数
  group: 时钟转发
  block_parameter: CF_BurstLen
  type: 字符向量
  values: 非负标量整数
- name: Idle Length
  summary: 突发之间的符号数 8（默认）| 非负标量整数
  group: 时钟转发
  block_parameter: CF_IdleLen
  type: 字符向量
  values: 非负标量整数
- name: Preamble
  summary: 添加到每个突发开始处的额外时钟周期数 2（默认）| 非负标量整数
  group: 时钟转发
  block_parameter: CF_Preamble
  type: 字符向量
  values: 非负标量整数
- name: Postamble
  summary: 添加到每个突发末尾的额外时钟周期数 0（默认）| 非负标量整数
  group: 时钟转发
  block_parameter: CF_Postamble
  type: 字符向量
  values: 非负标量整数
- name: Include Transmitter Jitter
  summary: 在前传时钟中包含发射机抖动 on（默认）| off
  group: 时钟转发
- name: Tx_Dj (UI)
  summary: 发射机确定性抖动 0（默认）| 范围 [0 1] 内的标量
  group: 时钟转发
  block_parameter: CF_TxDj
  type: 字符向量
  values: 范围 [0 1] 内的标量
- name: Tx_Rj (UI)
  summary: 发射机随机抖动 0（默认）| 范围 [0 1] 内的标量
  group: 时钟转发
  block_parameter: CF_TxRj
  type: 字符向量
  values: 范围 [0 1] 内的标量
- name: Tx_DCD (UI)
  summary: 发射机占空比失真 0（默认）| 范围 [0 1] 内的标量
  group: 时钟转发
  block_parameter: CF_TxDCD
  type: 字符向量
  values: 范围 [0 1] 内的标量
- name: Tx_Sj (UI)
  summary: 发射机正弦抖动 0（默认）| 范围 [0 1] 内的标量
  group: 时钟转发
  block_parameter: CF_Sj
  type: 字符向量
  values: 范围 [0 1] 内的标量
- name: Tx_Sj_Frequency (Hz)
  summary: 发射机正弦抖动频率 0（默认）| 范围 [0 100e9] 内的标量
  group: 时钟转发
  block_parameter: CF_TxSjFreq
  type: 字符向量
  values: 范围 [0 100e9] 内的标量
  default: '0'
- name: Waveform Name
  summary: 工作区中波形参数的名称 defaultClockWave（默认）| 字符串
  group: 时钟转发
  block_parameter: CF_WaveformName
  type: 字符向量
  values: 字符串
  default: '0'
- name: Waveform Delay (s)
  summary: 转发时钟的延迟 0（默认）| 非负标量整数
  group: 时钟转发
  block_parameter: CF_WaveDelay
  type: 字符向量
  values: 非负标量整数
  default: '0'
- name: Clock Times Name
  summary: 工作区中时钟时间参数的名称 defaultClockTimes（默认）| 字符串
  group: 时钟转发
  block_parameter: CF_ClockTimesName
  type: 字符向量
  values: 字符串
  default: '0'
```

### Stimulus

### **Number of symbols** — 用于仿真的激励模式长度 `20000`（默认）| 正实数整数

用于仿真的激励模式长度，指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumberOfSymbols` |
| **类型：** 字符向量 |
| **值：** 正实数整数 |
| **默认：** `20000` |

### **Use recommended simulation stop time** — 将推荐的仿真停止时间设置为仿真停止时间 开（默认）| 关

选择此选项可直接将 **Recommended simulation stop time** 设置为仿真停止时间。默认情况下，此选项处于选中状态。

**Recommended simulation stop time** 定义了仿真必须运行以获得有意义结果的最短时间。它通过将 Configuration 模块中的 **Sample Interval** 与 **Number of symbols** 相乘来计算。

### **Waveform creation method** — 定义激励波形的创建方式 `Random Symbols`（默认）| `Serial PRBS` | `Symbol Pattern` | `Binary Pattern` | `Symbol Voltage Pattern` | `Sampled Voltage` | `Parallel PRBS`

定义激励波形的创建方式：

- `Random Symbols` — 直接从均匀分布中随机生成符号。
- `Serial PRBS` — 定义二进制序列并映射到高阶调制符号。映射序列取决于 Configuration 模块中定义的调制方案。
- `Symbol Pattern` — 直接将符号模式定义为从 0 到（调制电平数 – 1）的整数。
- `Binary Pattern` — 直接定义二进制模式并映射到高阶调制符号。映射序列取决于 Configuration 模块中定义的调制方案。
- `Symbol Voltage Pattern` — 直接定义符号间隔模式的电压。
- `Sampled Voltage` — 直接定义采样间隔间隔的波形。
- `Parallel PRBS` — 利用多个 PRBS 流形成 PAM4、PAM8、PAM16 和 PAM32 符号。对于 PAM32，您最多可以定义 5 个 PRBS 流。NRZ 调制方案使用单个 PRBS 流。其他调制方案使用随机符号波形创建方法。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CreationMethod` |
| **类型：** 字符向量 |
| **值：** `Random Symbols` | `Serial PRBS` | `Symbol Pattern` | `Binary Pattern` | `Symbol Voltage Pattern` | `Sampled Voltage` | `Parallel PRBS` |
| **默认：** `Random Symbols` |

### **Random symbols seed** — 用于生成随机符号波形的种子 `1431655765`（默认）| 正实数标量

用于生成随机符号波形的种子，指定为正实数标量。

#### 依赖关系

- 要启用此参数，请将 **Waveform creation method** 参数设置为 `Random Symbols`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `soPAMnSeed` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1431655765` |

### **PRBS order** — 伪随机二进制序列的阶数 `11`（默认）| `7` | `9` | `13` | `15` | `20` | `23` | `31` | `47`

使用串行 PRBS 或并行 PRBS 方法创建激励波形时伪随机二进制序列的阶数。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Serial PRBS` 或 `Parallel PRBS`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PRBS` |
| **类型：** 字符向量 |
| **值：** `7` | `9` | `11` | `13` | `15` | `20` | `23` | `31` | `47` |
| **默认：** `11` |

### **PRBS seed** — 伪随机二进制序列的种子 `1`（默认）| 范围 [1, 2Order-1] 内的整数

用于生成伪随机二进制序列的种子，指定为范围 [1, 2Order-1] 内的整数。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Serial PRBS` 或 `Parallel PRBS`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PRBSSeed` |
| **类型：** 字符向量 |
| **值：** 范围 [1, 2Order-1] 内的整数 |
| **默认值：** `1` |

### **Reverse PRBS in time** — 通过反转特征多项式的抽头位置在时间上反转 PRBS 关闭（默认）| 打开

通过反转特征多项式的抽头位置，在时间上（沿 *x* 轴）反转 PRBS。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Serial PRBS` 或 `Parallel PRBS`。

### **Invert PRBS in voltage** — 通过翻转 0 和 1 的值在电压上反转 PRBS 关闭（默认）| 打开

通过将 0 转换为 1、将 1 转换为 0，在电压上（沿 *y* 轴）反转 PRBS。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Serial PRBS` 或 `Parallel PRBS`。

### **Symbol pattern** — 以符号时间间隔间隔的符号整数向量 `[0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]`（默认）| 元素值在范围 [0, (Number of modulation levels-1)] 内的向量

以符号时间间隔间隔的符号整数向量。向量元素的值必须在范围 [0, (Number of modulation levels-1)] 内。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Symbol Pattern`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SymbolPattern` |
| **类型：** 字符向量 |
| **值：** 元素值在范围 [0, (Number of modulation levels-1)] 内的向量 |
| **默认值：** `[0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]` |

### **Binary pattern** — 以采样时间间隔间隔的 1 和 0 向量 `[0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]`（默认）| 具有二进制元素的向量

以符号时间间隔间隔的二进制元素（1 和 0）向量。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Binary Pattern`。

#### 编程使用

|  |
| --- |
| **模块参数：** `BinaryPattern` |
| **类型：** 字符向量 |
| **值：** 具有二进制元素的向量 |
| **默认值：** `[0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]` |

### **Symbol voltage pattern** — 以符号时间间隔间隔的符号电压向量 `1/2*[1 1 1 1 -1 -1 -1 -1]`（默认）| 具有十进制值的向量

以符号时间间隔间隔的符号电压向量。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Symbol Voltage Pattern`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SymbolVoltageDataPattern` |
| **类型：** 字符向量 |
| **值：** 具有十进制值的向量 |
| **默认值：** `1/2*[1 1 1 1 -1 -1 -1 -1]` |

### **Sampled voltage pattern** — 以采样间隔间隔的电压向量 `[zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5`（默认）| 实值向量

以采样间隔间隔的电压向量。

#### 依赖关系

要启用此参数，请将 **Waveform creation method** 参数设置为 `Sampled Voltage`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CustomStimulus` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认值：** `[zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5` |

### **Sub symbol time delay (s)** — 将激励波形延迟模符号时间 `0`（默认）| 非负实数标量

将激励波形延迟模符号时间，以略微偏移眼图或恢复时钟相位。

模运算求除法后的余数。

#### 编程使用

|  |
| --- |
| **模块参数：** `soDelay` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `0` |

### 时钟转发

### **Change in IBIS-AMI Manager** — 修改 Rx\_Use\_Clock\_Input 保留 AMI 参数按钮

使用 SerDes IBIS-AMI Manager 对话框修改 **Rx\_Use\_Clock\_Input** 保留 AMI 参数。您可以在 SerDes IBIS-AMI Manager 的 **AMI-Rx** 选项卡中更改该参数。

您可以使用波形或时钟时间数据作为时钟转发。**Current State** 参数显示您正在转发哪种类型的数据。

### **Generate Clock or Strobe Waveform** — 从波形参数生成时钟或选通波形 关（默认）| 开

从指定的波形参数生成时钟或选通波形。

您可以定义带延迟的时钟模式。或者，您可以定义带延迟、突发长度、空闲长度、前导码和后导码的选通模式。

您还可以定义生成时钟或选通模式时要包含的发射器抖动参数。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`。

### **Use External Waveform or Clock Times Array** — 使用外部波形进行转发 开（默认）| 关

使用外部时钟进行转发。您可以在基础工作区或模型工作区中定义外部时钟，并使用 **Waveform Name** 参数指向它。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`。

### **Include Analog Channel Model in clock waveform** — 在时钟波形中包含模拟通道模型 开（默认）| 关

选择以在时钟波形中包含模拟通道模型。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`。

### **Clock Pattern** — 转发时钟模式 关（默认）| 开

选择以生成转发时钟模式。您还可以定义时钟延迟并包含发射器抖动。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

### **Strobe Pattern** — 转发选通模式 开（默认）| 关

选择以生成转发选通模式。您还可以定义选通延迟、突发长度、空闲长度、前导码、后导码，并包含发射器抖动。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

### **Delay (s)** — 延迟转发时钟 `0`（默认）| 非负实数标量

延迟转发时钟，指定为非负实数标量。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 编程使用

|  |
| --- |
| **模块参数：** `CF_Delay` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `0` |

### **Burst Length** — 选通突发模式之间的符号数 `16`（默认）| 非负标量整数

选通突发模式或时钟模式之间的符号数，指定为非负标量整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `CF_BurstLen` |
| **类型：** 字符向量 |
| **值：** 非负标量整数 |
| **默认：** `0` |

### **Idle Length** — 突发之间的符号数 `8`（默认）| 非负标量整数

突发之间的符号数，指定为非负标量整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `CF_IdleLen` |
| **类型：** 字符向量 |
| **值：** 非负标量整数 |
| **默认：** `0` |

### **Preamble** — 添加到每个突发开始处的额外时钟周期数 `2`（默认）| 非负标量整数

添加到每个突发开始处的额外时钟周期数，指定为非负标量整数。一个时钟周期由两个符号组成。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_Preamble` |
| **类型：** 字符向量 |
| **值：** 非负标量整数 |
| **默认：** `2` |

### **Postamble** — 添加到每个突发末尾的额外时钟周期数 `0`（默认）| 非负标量整数

添加到每个突发末尾的额外时钟周期数，指定为非负标量整数。一个时钟周期由两个符号组成。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_Postamble` |
| **类型：** 字符向量 |
| **值：** 非负标量整数 |
| **默认：** `0` |

### **Include Transmitter Jitter** — 在前传时钟中包含发射机抖动 on（默认）| off

选择以在前传时钟中包含发射机抖动。

### **Tx\_Dj (UI)** — 发射机确定性抖动 `0`（默认）| 范围 [0 1] 内的标量

发射机确定性抖动，指定为范围 [0 1] 内的标量。它定义为峰峰值最坏情况变化的一半。

确定性抖动通常建模为有界均匀抖动。它也称为*非相关有界高概率抖动*。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_TxDj` |
| **类型：** 字符向量 |
| **值：** 范围 [0 1] 内的标量 |
| **默认：** `0` |

### **Tx\_Rj (UI)** — 发射机随机抖动 `0`（默认）| 范围 [0 1] 内的标量

发射机随机抖动，指定为范围 [0 1] 内的标量。它定义为白高斯相位噪声过程的标准差。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_TxRj` |
| **类型：** 字符向量 |
| **值：** 范围 [0 1] 内的标量 |
| **默认：** `0` |

### **Tx\_DCD (UI)** — 发射机占空比失真 `0`（默认）| 范围 [0 1] 内的标量

发射机占空比失真，指定为范围 [0 1] 内的标量。它定义为一个符号与下一个符号之间符号持续时间峰峰值差的一半。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_TxDCD` |
| **类型：** 字符向量 |
| **值：** 范围 [0 1] 内的标量 |
| **默认：** `0` |

### **Tx\_Sj (UI)** — 发射机正弦抖动 `0`（默认）| 范围 [0 1] 内的标量

发射机正弦抖动，指定为范围 [0 1] 内的标量。它定义为正弦相位噪声幅度峰峰值变化的一半。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CF_Sj` |
| **类型：** 字符向量 |
| **值：** 范围 [0 1] 内的标量 |
| **默认：** `0` |

### **Tx\_Sj\_Frequency (Hz)** — 发射机正弦抖动频率 `0`（默认）| 范围 [0 100e9] 内的标量

发射机正弦抖动的频率，指定为范围 [0 100e9] 内的标量。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Generate Clock or Strobe Waveform** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `CF_TxSjFreq` |
| **类型：** 字符向量 |
| **值：** 范围 [0 100e9] 内的标量 |
| **默认值：** `0` |

### **Waveform Name** — 工作区中波形参数的名称 `defaultClockWave`（默认）| 字符串

基础工作区或模型工作区中包含外部波形数据的波形参数的名称。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Use External Waveform or Clock Times Array** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `CF_WaveformName` |
| **类型：** 字符向量 |
| **值：** 字符串 |
| **默认值：** `0` |

### **Waveform Delay (s)** — 转发时钟的延迟 `0`（默认）| 非负标量整数

转发时钟的延迟，指定为非负标量整数。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Wave`，并选择 **Use External Waveform or Clock Times Array** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `CF_WaveDelay` |
| **类型：** 字符向量 |
| **值：** 非负标量整数 |
| **默认值：** `0` |

### **Clock Times Name** — 工作区中时钟时间参数的名称 `defaultClockTimes`（默认）| 字符串

基础工作区或模型工作区中包含外部时钟时间数据的时钟时间参数的名称。

#### 依赖关系

要启用此参数，请将 **Rx\_Use\_Clock\_Input** 参数的 **Current value** 选择为 `Time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CF_ClockTimesName` |
| **类型：** 字符向量 |
| **值：** 字符串 |
| **默认值：** `0` |
## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

### R2023b：时钟转发

使用 Stimulus 模块中的 **Clock Forwarding** 选项卡生成时钟激励模式。

## 描述

设置波形生成方法以及 SerDes 模型中要仿真的符号数

Stimulus 模块定义了如何创建波形以及在 SerDes Toolbox™ 模型中要仿真的符号数。您可以直接指定 PAMn 符号模式，或定义二进制到 PAMn 的映射方案。

当您在 SerDes IBIS-AMI Manager 对话框中启用时钟转发时，可以使用 Stimulus 模块从外部时钟时间数组或波形生成时钟时间。
