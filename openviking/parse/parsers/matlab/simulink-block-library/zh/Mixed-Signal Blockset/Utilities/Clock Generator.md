---
type: simulink-block
title: 'Clock Generator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'clockgenerator'
documentation_source_path: 'ref/clockgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Clock Generator

## 端口
```yaml
ports:
- name: vctrl
  summary: 用于控制输出频率的电压 标量 | 向量
  direction: input
  data_types: double
- name: ReferenceOffset
  summary: 参考频率偏移 标量
  direction: input
  data_types: double
- name: PhaseOffset
  summary: 占空比相位偏移 标量
  direction: input
  data_types: double
- name: clock0
  summary: 饱和输出时钟信号 标量
  direction: output
  data_types: double
- name: clockTime0
  summary: 上次时钟跳变时的仿真时间 标量
  direction: output
  data_types: double
- name: Phase
  summary: 基频时钟的最新时钟相位 标量
  direction: output
  data_types: double
- name: clockValid
  summary: 可变步长离散采样时钟 标量
  direction: output
  data_types: double
- name: clockTime
  summary: 最近一次时钟变化的绝对时钟时间 标量
  direction: output
  data_types: double
```

### 输入

### **vctrl** — 用于控制输出频率的电压 标量 | 向量

用于控制输出频率的电压，指定为标量或向量。

**数据类型：** `double`

### **ReferenceOffset** — 参考频率偏移 标量

参考频率的偏移，指定为标量。如果选择 **ReferenceOffsetPort** 参数，则 **ReferenceOffset** 端口使用来自外部模块的参考偏移值。

**数据类型：** `double`

### **PhaseOffset** — 占空比相位偏移 标量

占空比相位偏移的偏移，指定为标量。如果选择 **PhaseOffsetPort** 参数，则 **PhaseOffset** 端口使用来自外部模块的相位偏移值。

**数据类型：** `double`
### 输出

### **clock0** — 饱和输出时钟信号 标量

饱和输出时钟信号，以标量形式返回。每个输出相位对应一个时钟输出端口。

**clock0** 是该端口的默认名称。端口名 clock 后面的非负标量表示时钟相位。例如，**clock1** 表示相位 1 的饱和输出时钟信号。

输出为方波，其幅度由 **Output amplitude** 参数定义。

**数据类型：** `double`

### **clockTime0** — 上次时钟跳变时的仿真时间 标量

上次时钟跳变时的仿真时间，以标量形式返回。每个输出相位对应一个 clockTime 输出端口。

**clockTime0** 是该端口的默认名称。端口名 clockTime 后面的非负标量表示时钟相位。例如，**clockTime1** 表示相位 1 的时钟跳变时间。

**数据类型：** `double`

### **Phase** — 基频时钟的最新时钟相位 标量

基频时钟的最新时钟相位，以标量形式返回。

**数据类型：** `double`

### **clockValid** — 可变步长离散采样时钟 标量

可变步长离散采样时钟，指定为标量。**clockValid** 端口处信号的边沿采样时间与时钟时间信号中的值完全匹配。

**数据类型：** `double`

### **clockTime** — 最近一次时钟变化的绝对时钟时间 标量

**clockValid** 端口处最近一次时钟变化的绝对时钟时间。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Specify using
  summary: 定义时钟发生器的控制灵敏度 Voltage sensitivity（默认）| Output frequency vs. control voltage | Period offset
  group: ''
  block_parameter: SpecifyUsing
  type: 字符向量
  values: Voltage sensitivity | Output frequency vs. control voltage | Period offset
  default: Voltage sensitivity
- name: Voltage sensitivity (Hz/V)
  summary: 输出频率变化的度量 100e6（默认）| 正实数标量
  group: ''
  block_parameter: Kvco
  type: 字符向量
  values: 正实数标量
  default: 100e6
- name: Free running frequency (Hz)
  summary: 无控制电压时的输出频率 10e9（默认）| 正实数标量
  group: ''
  block_parameter: Fo
  type: character vector
  values: positive real scalar
  default: 10e9
- name: Control voltage (V)
  summary: 控制电压值 [-5 0 5]（默认）| 实数值向量
  group: ''
  block_parameter: ControlVoltage
  type: character vector
  values: real valued vector
  default: '[-5 0 5]'
- name: Output frequency (Hz)
  summary: 时钟发生器输出频率值 [9.9e9 10e9 10.5e9]（默认）| 正实数值向量
  group: ''
  block_parameter: OutputFrequency
  type: character vector
  values: positive real valued vector
  default: '[9.9e9 10e9 10.5e9]'
- name: Output amplitude (V)
  summary: 时钟发生器输出电压的最大幅度 1（默认）| 正实数标量
  group: ''
  block_parameter: Amplitude
  type: character vector
  values: positive real scalar
  default: '1'
- name: Phase unit
  summary: 输出相位和占空比的单位 Degrees（默认）| Fraction of a clock cycle
  group: ''
  block_parameter: PhaseUnits
  type: character vector
  values: Degrees | Fraction of a clock cycle
  default: Degrees
- name: Output phase
  summary: 输出时钟信号的相位 [0]（默认）| 非负实数标量 | 非负实数值向量
  group: ''
  block_parameter: OutputPhase
  type: character vector
  values: nonnegative real scalar | nonnegative real valued vector
  default: '[0]'
- name: Output duty cycle
  summary: 输出时钟信号的占空比 [180]（默认）| 正实数标量 | 正实数值向量
  group: ''
  block_parameter: OutputDutyCycle
  type: character vector
  values: positive real scalar | positive real valued vector
  default: '[180]'
- name: PhaseOffsetPort
  summary: 通过输入端口定义占空比相位偏移 on（默认）| off
  group: ''
- name: 相位偏移（符号时间）
  summary: 占空比相位偏移 0（默认）| [-0.5,0.5] 范围内的标量
  group: ''
  block_parameter: PhaseOffset
  type: 字符向量
  values: 标量
- name: ReferenceOffsetPort
  summary: 通过输入端口定义参考频率偏移 开（默认）| 关
  group: ''
- name: 参考时钟频率偏移（ppm）
  summary: 标称输出频率偏移的因子 0（默认）| [-300,300] 范围内的标量
  group: ''
  block_parameter: ReferenceOffset
  type: 字符向量
  values: '[-300,300] 范围内的标量'
- name: 仿真方式
  summary: 选择仿真模式 代码生成（默认）| 解释执行
  group: ''
  block_parameter: SimulateUsing
  type: 字符向量
  values: Code generation| Interpreted execution
- name: 添加相位噪声
  summary: 添加作为频率函数的相位噪声 开（默认）| 关
  group: ''
- name: 相位噪声频率偏移（Hz）
  summary: 指定相位噪声相对于载波频率的频率偏移 [30e3 100e3 1e6 3e6 10e6]（默认）| 正实值向量
  group: ''
  block_parameter: Foffset
  type: 字符向量
  values: 正实值向量
- name: 相位噪声电平（dBc/Hz）
  summary: 指定相位噪声频率偏移处相对于载波的相位噪声功率 [-56 -106 -132 -143 -152]（默认）| 负实值向量
  group: ''
  block_parameter: PhaseNoise
  type: 字符向量
  values: 负实值向量
  default: '[-56 -106 -132 -143 -152]'
- name: Estimate phase noise parameters
  summary: 从测得的相位噪声数据估计相位噪声参数按钮
  group: ''
- name: Period jitter (S)
  summary: 周期抖动的标准差 1.7e-15（默认）| 正实标量
  group: ''
  block_parameter: PeriodJitter
  type: 字符向量
  values: 正实标量
  default: '1.7e-15'
- name: Flicker corner frequency (Hz)
  summary: 闪烁噪声的拐角频率 0（默认）| 标量
  group: ''
  block_parameter: CornerFrequency
  type: 字符向量
  values: 标量
  default: '0'
- name: Customize flicker exponent (Advanced feature)
  summary: 自定义闪烁噪声功率谱分布 关（默认）| 开
  group: ''
- name: Flicker exponent
  summary: 闪烁噪声功率指数 1.0（默认）| 0.8 | 0.9 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5
  group: ''
  block_parameter: FlickerExponent
  type: 字符向量
  values: 1.0 | 0.8 | 0.9 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5
  default: '1.0'
- name: Plot fit
  summary: 绘制拟合的相位噪声曲线按钮
  group: ''
- name: Symbol time (s)
  summary: 单个符号持续时间的时间 100e-12（默认）| 实正标量
  group: ''
  block_parameter: SymbolTime
  type: 字符向量
  values: 实正标量
  default: 100e-12
- name: Sample interval (s)
  summary: 波形的均匀时间步长 6.25e-12（默认）| 实正标量
  group: ''
  block_parameter: SampleInterval
  type: 字符向量
  values: 实正标量
  default: '6.25e-12'
- name: Modulation (2:NRZ, 3:PAM3, 4:PAM4)
  summary: 调制方案 2（默认）| 3 | 4
  group: ''
  block_parameter: Modulation
  type: 字符向量
  values: 2 | 3 | 4
  default: '2'
- name: 输入波形类型
  summary: 输入波形的类型 Sample（默认）| Impulse
  group: ''
  block_parameter: WaveType
  type: 字符向量
  values: Sample | Impulse
```

#### 主

### **Specify using** — 定义时钟发生器的控制灵敏度 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage` | `Period offset`

定义时钟发生器的控制灵敏度。

- 选择 `Voltage sensitivity`，通过 **Voltage sensitivity (Hz/V)** 和 **Free running frequency (Hz)** 参数指定输出频率。
- 选择 `Output frequency vs. control voltage`，通过 **Control voltage (V)** 向量与 **Output frequency (Hz)** 向量插值得到输出频率。
- 选择 `Period offset`，按标称时钟周期的比例调整周期时间。使用 **Control voltage (V)** 参数指定该比例。该模块使用 **Symbol time (s)** 参数中设置的值来确定 **Voltage sensitivity (Hz/V)** 和 **Free running frequency (Hz)** 参数的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** 字符向量 |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` | `Period offset` |
| **默认值：** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — 输出频率变化的度量 `100e6`（默认）| 正实数标量

输入电压变化引起的输出频率变化的度量，指定为以 Hz/V 为单位的正实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `100e6` |

**数据类型：** `double`

### **Free running frequency (Hz)** — 无控制电压时的输出频率 `10e9`（默认）| 正实数标量

时钟发生器在没有任何控制电压输入
（`0` V）时的频率，或静态频率，指定为以赫兹为单位的正实数
标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Fo` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`10e9` |

**Data Types:** `double`

### **Control voltage (V)** — 控制电压值 `[-5 0 5]`（默认）| 实数值向量

时钟发生器的控制电压值，指定为以伏特为单位的实数值向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`[-5 0 5]` |

**Data Types:** `double`

### **Output frequency (Hz)** — 时钟发生器输出频率值 `[9.9e9 10e9 10.5e9]`（默认）| 正实数值向量

对应于 **Control voltage (V)** 向量的时钟发生器输出频率，以赫兹为单位指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型**：character vector |
| **值**：positive real valued vector |
| **默认值**：`[9.9e9 10e9 10.5e9]` |

**Data Types:** `double`

### **Output amplitude (V)** — 时钟发生器输出电压的最大幅度 `1`（默认）| 正实数标量

时钟发生器输出电压的最大幅度，指定为正实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`1` |

**Data Types:** `double`

### **Phase unit** — 输出相位和占空比的单位 `Degrees`（默认）| `Fraction of a clock cycle`

输出相位和占空比的单位，指定为
`Degrees` 或 `Fraction of a clock
cycle`。

#### 编程使用

|  |
| --- |
| **模块参数：** `PhaseUnits` |
| **类型**：character vector |
| **值**：`Degrees` | `Fraction of a clock cycle` |
| **默认值**：`Degrees` |

### **Output phase** — 输出时钟信号的相位 `[0]`（默认）| 非负实数标量 | 非负实数值向量

输出时钟信号的相位，指定为标量向量。如果指定为向量，每个元素定义一个输出。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputPhase` |
| **类型**：character vector |
| **值**：nonnegative real scalar | nonnegative real valued vector |
| **默认值**：`[0]` |

### **Output duty cycle** — 输出时钟信号的占空比 `[180]`（默认）| 正实数标量 | 正实数值向量

输出时钟信号的占空比，指定为标量或向量。时钟输出相位指的是输出时钟的上升沿。

如果指定为向量，每个元素定义一个输出。向量中缺失或为空的元素将使用默认占空比。多余的元素将被忽略。

占空比必须大于 Sample intervalSymbol time 但小于 1−Sample intervalSymbol time，定义为时钟周期的分数。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputDutyCycle` |
| **类型**：character vector |
| **值**：positive real scalar | positive real valued vector |
| **默认值**：`[180]` |

### **PhaseOffsetPort** — 通过输入端口定义占空比相位偏移 on（默认）| off

通过来自外部模块的 **PhaseOffset**
输入端口定义占空比相位偏移。如果取消选择
**PhaseOffsetPort** 参数，它将从 AMI 文件中移除。这
实际上将相位偏移硬编码为 **Phase offset
(symbol time)** 参数定义的值。

### **相位偏移（符号时间）** — 占空比相位偏移 `0`（默认）| [-0.5,0.5] 范围内的标量

占空比相位偏移，指定为以符号时间分数表示的 [-0.5, 0.5] 范围内的标量。相位偏移手动移动时钟概率分布函数（PDF），以获得更好的误码率（BER）。

#### 依赖关系

要启用此参数，请取消选择 **PhaseOffsetPort**。

#### 编程使用

|  |
| --- |
| **模块参数：** `PhaseOffset` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `0` |

### **ReferenceOffsetPort** — 通过输入端口定义参考频率偏移 开（默认）| 关

通过来自外部模块的 **ReferenceOffset** 输入端口定义参考频率偏移。如果取消选择 **ReferenceOffsetPort** 参数，它将从 AMI 文件中移除。这实际上将 **参考偏移** 硬编码为 **参考时钟频率偏移（ppm）** 参数定义的值。

### **参考时钟频率偏移（ppm）** — 标称输出频率偏移的因子 `0`（默认）| [-300,300] 范围内的标量

标称输出频率相对于 1 符号时间偏移的因子，指定为以百万分之一为单位的 [-300,300] 范围内的标量。它是发射机振荡器频率与接收机振荡器频率之间的偏差。

#### 依赖关系

要启用此参数，请取消选择 **ReferenceOffsetPort**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ReferenceOffset` |
| **类型：** 字符向量 |
| **值：** [-300,300] 范围内的标量 |
| **默认：** `0` |

### **仿真方式** — 选择仿真模式 `代码生成`（默认）| `解释执行`

选择仿真模式。此选择会影响仿真性能。

使用 `代码生成` 方法仿真模型需要额外的启动时间，但后续仿真运行更快。使用 `解释执行` 方法仿真模型可能会减少启动时间，但后续仿真运行较慢。有关详细信息，请参阅解释执行与代码生成。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** 字符向量 |
| **值：** `Code generation`| `Interpreted execution` |
| **默认：** `Code generation` |

#### 相位噪声

### **添加相位噪声** — 添加作为频率函数的相位噪声 开（默认）| 关

选择以引入作为频率函数的相位噪声。默认情况下，此选项处于选中状态。

### **相位噪声频率偏移（Hz）** — 指定相位噪声相对于载波频率的频率偏移 `[30e3 100e3 1e6 3e6 10e6]`（默认）| 正实值向量

指定相位噪声相对于载波频率的频率偏移，指定为以赫兹表示的正实值向量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Add phase noise**。

#### 编程使用

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** 字符向量 |
| **值：** 正实值向量 |
| **默认：** `[30e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **相位噪声电平（dBc/Hz）** — 指定相位噪声频率偏移处相对于载波的相位噪声功率 `[-56 -106 -132 -143 -152]`（默认）| 负实值向量

指定以相位噪声频率偏移为中心、相对于载波的 1 Hz 带宽内的相位噪声功率，指定为以 dBc/Hz 表示的负实值向量。**相位噪声电平** 的元素对应于 **相位噪声频率偏移（Hz）** 参数中的相对元素。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** 字符向量 |
| **值：** 负实值向量 |
| **默认值：** `[-56 -106 -132 -143 -152]` |

**数据类型：** `double`

### **Estimate phase noise parameters** — 从测得的相位噪声数据估计相位噪声参数按钮

点击以从测得的相位噪声数据中估计相位噪声参数。该操作根据**Phase noise frequency offset (Hz)**和**Phase noise level (dBc/Hz)**参数计算**Period jitter (S)**和**Flicker corner frequency (Hz)**参数。因此，相位噪声曲线与物理模型匹配。

### **Period jitter (S)** — 周期抖动的标准差 `1.7e-15`（默认）| 正实标量

周期抖动的标准差，指定为以秒为单位的正实标量。周期抖动是时钟信号周期时间相对于理想周期的偏差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** 字符向量 |
| **值：** 正实标量 |
| **默认值：** `1.7e-15` |

### **Flicker corner frequency (Hz)** — 闪烁噪声的拐角频率 `0`（默认）| 标量

闪烁噪声的拐角频率，指定为以赫兹为单位的标量。**Flicker corner frequency (Hz)**定义为由于闪烁噪声导致相位噪声从1/*f*2过渡到1/*f*3的频率。在该频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `0` |

### **Customize flicker exponent (Advanced feature)** — 自定义闪烁噪声功率谱分布 关（默认）| 开

选择此参数以自定义闪烁噪声的功率谱分布。传统上，闪烁噪声定义为1/*f*噪声，但它可以变化为1/*fV*，其中0.8<*V*<1.5。

### **Flicker exponent** — 闪烁噪声功率指数 `1.0`（默认）| `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5`

闪烁噪声功率指数，指定在`0.8`到`1.5`之间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FlickerExponent` |
| **类型：** 字符向量 |
| **值：** `1.0` | `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5` |
| **默认值：** `1.0` |

### **Plot fit** — 绘制拟合的相位噪声曲线按钮

点击以绘制拟合的相位噪声曲线。这允许您查看拟合模型与指定相位噪声数据的匹配程度。

#### 高级

### **Symbol time (s)** — 单个符号持续时间的时间 `100e-12`（默认）| 实正标量

单个符号持续时间的时间，指定为以秒为单位的实正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SymbolTime` |
| **类型：** 字符向量 |
| **值：** 实正标量 |
| **默认值：** `100e-12` |

**数据类型：** `double`

### **Sample interval (s)** — 波形的均匀时间步长 `6.25e-12`（默认）| 实正标量

波形的均匀时间步长，指定为以秒为单位的实正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleInterval` |
| **类型：** 字符向量 |
| **值：** 实正标量 |
| **默认值：** `6.25e-12` |

**数据类型：** `double`

### **Modulation (2:NRZ, 3:PAM3, 4:PAM4)** — 调制方案 `2`（默认）| `3` | `4`

调制方案中的逻辑电平数：

- 如果调制方案为NRZ（不归零），选择`2`。
- 如果调制方案为PAM3（脉冲幅度调制电平3），选择`3`。
- 如果调制方案为PAM4（脉冲幅度调制电平4），选择`4`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Modulation` |
| **类型：** 字符向量 |
| **值：** `2` | `3` | `4` |
| **默认值：** `2` |

**数据类型：** `char`

### **输入波形类型** — 输入波形的类型 `Sample`（默认）| `Impulse`

输入波形的类型，可以是逐样本信号或冲激响应信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `WaveType` |
| **类型：** 字符向量 |
| **值：** `Sample` | `Impulse` |
| **默认：** `Sample` |
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

生成具有一个或多个相位的时钟信号

Clock Generator 模块生成具有多个输出相位和详细相位噪声建模的时钟信号。两个输出端口上的信号共同为每个相位建模输出时钟信号。这些信号是：时钟端口上的饱和时钟信号和 clockTime 端口上的时钟转换时间。

您可以使用该模块对任何使用压控振荡器 (VCO) 的时钟恢复环路进行建模。该模块始终提供噪声底低于 –150 dBC/Hz 的时钟时间。您还可以使用该模块包含与物理模型匹配的相位噪声。
