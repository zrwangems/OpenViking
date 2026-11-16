---
type: simulink-block
title: 'Fractional N PLL with Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Architectures'
documentation_page: 'fractionalnpllwithdeltasigmamodulator'
documentation_source_path: 'ref/fractionalnpllwithdeltasigmamodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Fractional N PLL with Delta Sigma Modulator

## 端口

### 输入

### **clk in** — 输入时钟信号标量

输入时钟信号，指定为标量。**clk in** 端口处的信号用作 PLL 系统中 PFD 模块的参考信号。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟信号标量

输出时钟信号，指定为标量。**clk out** 端口处的信号是 PLL 系统中 VCO 模块的输出。

**数据类型：** `double`

## 参数

### **Edit System** — 断开库模块链接并用适当值替换内部变量按钮

单击以断开模块与库的链接。内部变量替换为其值，模块变为简单子系统。

### **Enable increased buffer size** — 启用增加的缓冲区大小按钮

选择以在仿真期间启用增加的缓冲区大小。这会增加 PLL 模型中属于 Mixed-Signal Blockset™/PLL/Building Blocks Simulink® 库的所有构建模块的缓冲区大小。构建模块包括 PFD、Charge Pump、Loop Filter、VCO 和 Fractional Clock Divider with DSM。默认情况下，此选项未选中。

### **Buffer size for loop filter** — 循环滤波器缓冲区大小 `1000`（默认）| 正整数标量

循环滤波器的缓冲区大小，指定为正整数标量。这会将仿真期间可用的额外缓冲区样本数设置为循环滤波器内部的 Convert Sample Time 子系统。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **Buffer size for loop filter** 设置为足够大的值，以便输入缓冲区包含所有所需的输入样本。

#### 依赖关系

仅当选择 **Enable increased buffer size** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBufferFilter')` 查看 **Buffer size for loop filter** 的当前值。
- 使用 `set_param(gcb,'NBufferFilter',value)` 将 **Buffer size for loop filter** 设置为特定值。

### **Buffer size for PFD, charge pump, VCO, prescaler** — PFD、charge pump、VCO 和 prescaler 的缓冲区大小 `10`（默认）| 正整数标量

PFD、charge pump、VCO 和 prescaler 的缓冲区大小，指定为正整数标量。这会设置 PLL 模型中 PFD、Charge Pump、VCO 和 Fractional Clock Divider with DSM 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **Buffer size for PFD, charge pump, VCO, prescaler** 设置为足够大的值，以便输入缓冲区包含所有所需的输入样本。

#### 依赖关系

仅当选择 **Enable increased buffer size** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size for PFD, charge pump, VCO, prescaler** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size for PFD, charge pump, VCO, prescaler** 设置为特定值。

### PFD

#### 配置

### **Deadband compensation (s)** — 为接近零相位偏移时的有效输出增加的延迟 `40e-12`（默认）| 正实数标量

为接近零相位偏移时的有效输出增加的延迟，指定为以 seconds 为单位的正实数标量。Deadband 是接近零相位偏移的相位偏移带，在该带内 PFD 输出可忽略。

#### 编程用法

- 使用 `get_param(gcb,'DeadbandCompensation')` 查看 **Deadband compensation (s)** 的当前值。
- 使用 `set_param(gcb,'DeadbandCompensation',value)` 将 **Deadband compensation (s)** 设置为特定值。

**数据类型：** `double`

#### 损伤

### **Enable impairments** — 将电路损伤添加到仿真 off（默认）| on

选择以将 rise/fall time 和 propagation delay 等电路损伤添加到仿真。默认情况下，此选项未选中。

### **Output step size calculation** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据 rise/fall time 计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据 maximum frequency of interest 计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **Enable Impairments**。

### **Maximum frequency of interest (Hz)** — 输出端感兴趣的最大频率 `10e9`（默认）| 正实数标量

输出端感兴趣的最大频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **Enable Impairments**，并为 **Output step size calculation** 选择 **Advanced**。

#### 编程用法

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **Maximum frequency of interest (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **Maximum frequency of interest (Hz)** 设置为特定值。

**数据类型：** `double`

### **Rise/fall time (s)** — PFD 的 up 输出端口的 20% – 80% rise/fall time `3e-11`（默认）| 正实数标量

PFD 的 up 输出端口的 20% – 80% rise/fall time，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **Enable Impairments**。

#### 编程用法

- 使用 `get_param(gcb,'RiseFallTime')` 查看 **Rise/fall time (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallTime',value)` 将 **Rise/fall time (s)** 设置为特定值。

**数据类型：** `double`

### **Propagation Delay (s)** — 从 PFD 的输入端口到输出端口的延迟 `50e-12`（默认）| 正实数标量

从 PFD 的输入端口到输出端口的延迟，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **Enable Impairments**。

#### 编程用法

- 使用 `get_param(gcb,'PropDelay')` 查看 **Propagation Delay (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelay',value)` 将 **Propagation Delay (s)** 设置为特定值。

**数据类型：** `double`

### Charge pump

#### 配置

### **Output current (A)** — 设计输出电流 `1e-3`（默认）| 正实数标量

设计输出电流的满量程幅度，指定为以 amperes 为单位的正实数标量。此参数在 **Loop Filter** 选项卡中也报告为 **Charge pump current**，并用于自动计算循环滤波器的滤波器元件值。此参数可调。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputCurrent` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `1e-3` |

**数据类型：** `double`

### **Input threshold (V)** — 输入端口的逻辑切换阈值 `0.5`（默认）| 实数标量

输入端口的逻辑切换阈值，指定为以 volts 为单位的实数标量。

#### 编程用法

- 使用 `get_param(gcb,'InputThreshold')` 查看 **Input threshold (V)** 的当前值。
- 使用 `set_param(gcb,'InputThreshold',value)` 将 **Input threshold (V)** 设置为特定值。

**数据类型：** `double`

#### 损伤

### **Enable current impairments** — 将电流损伤添加到仿真 off（默认）| on

选择以将 current imbalance 和 leakage current 等电流损伤添加到仿真。默认情况下，此选项未选中。

### **Current imbalance (A)** — 满量程正电流和负电流之间的差 `1e-7`（默认）| 正实数标量

满量程正电流和负电流之间的差，指定为以 amperes 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable current impairments**。

#### 编程用法

- 使用 `get_param(gcb,'CurrentImbalance')` 查看 **Current imbalance (A)** 的当前值。
- 使用 `set_param(gcb,'CurrentImbalance',value)` 将 **Current imbalance (A)** 设置为特定值。

**数据类型：** `double`

### **Leakage current (A)** — 没有任何输入时的输出电流 `1e-8`（默认）| 非负实数标量

当两个输入均为逻辑零时的输出电流，指定为以 amperes 为单位的非负实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable current impairments**。

#### 编程用法

- 使用 `get_param(gcb,'LeakageCurrent')` 查看 **Leakage current (A)** 的当前值。
- 使用 `set_param(gcb,'LeakageCurrent',value)` 将 **Leakage current (A)** 设置为特定值。

**数据类型：** `double`

### **Enable timing impairments** — 将时序损伤添加到仿真 off（默认）| on

选择以将 rise/fall time 和 propagation delay 等时序损伤添加到仿真。默认情况下，此选项未选中。

### **Output step size calculation** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据 rise/fall time 计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据 maximum frequency of interest 计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **Charge Pump** 选项卡中选择 **Enable timing impairments**。

### **Maximum frequency of interest (Hz)** — 输出端感兴趣的最大频率 `10e9`（默认）| 正实数标量

输出端感兴趣的最大频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge Pump** 选项卡中选择 **Enable timing impairments**，并为 **Output step size calculation** 选择 **Advanced**。

#### 编程用法

- 使用 `get_param(gcb,'MaxFreqInterestCp')` 查看 **Maximum frequency of interest (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterestCp',value)` 将 **Maximum frequency of interest (Hz)** 设置为特定值。

**数据类型：** `double`

#### Up

### **Rise/fall time (s)** — up 输入端口的 20% – 80% rise/fall time `5e-9`（默认）| 正实数标量

charge pump 的 up 输入端口的 20% – 80% rise/fall time，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable timing impairments**。

#### 编程用法

- 使用 `get_param(gcb,'RiseFallUp')` 查看 **Up Rise/fall time (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallUp',value)` 将 **Up Rise/fall time (s)** 设置为特定值。

**数据类型：** `double`

### **Propagation delay (s)** — 从 charge pump 的 up 输入端口到输出端口的总传播延迟 `6e-9`（默认）| 正实数标量

从 charge pump 的 up 输入端口到输出端口的总传播延迟，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable timing impairments**。

#### 编程用法

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Up Propagation delay (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Up Propagation delay (s)** 设置为特定值。

**数据类型：** `double`

#### Down

### **Rise/fall time** — down 输入端口的 20% – 80% rise/fall time `2e-9`（默认）| 标量

charge pump 的 down 输入端口的 20% – 80% rise/fall time。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable timing impairments**。

#### 编程用法

- 使用 `get_param(gcb,'RiseFallDown')` 查看 **Down Rise/fall time (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallDown',value)` 将 **Down Rise/fall time (s)** 设置为特定值。

**数据类型：** `double`

### **Propagation delay (s)** — 从 charge pump 的 up 输入端口到输出端口的总传播延迟 `4e-9`（默认）| 正实数标量

从 charge pump 的 up 输入端口到输出端口的总传播延迟，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **Enable timing impairments**。

#### 编程用法

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Down Propagation delay (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Down Propagation delay (s)** 设置为特定值。

**数据类型：** `double`

### VCO

### **Specify using** — 定义如何指定 VCO 输出频率 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage`

定义如何指定 VCO 输出频率：

- 选择 `Voltage sensitivity` 以根据 **Voltage sensitivity (Hz/V)** 和 **Free running frequency (Hz)** 指定输出频率。
- 选择 `Output frequency vs. control voltage` 以根据 **Control voltage (V)** 向量与 **Output frequency (Hz)** 向量插值输出频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** character vector |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认：** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — VCO 输出频率变化的度量 `100e6`（默认）| 正实数标量

输入电压变化引起的输出频率变化的度量，指定为以 Hz/V 为单位的正实数标量。此参数在 **Loop Filter** 选项卡中也报告为 **VCO voltage sensitivity**，并用于自动计算循环滤波器的滤波器元件值。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **Specify using** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `100e6` |

**数据类型：** `double`

### **Free running frequency (Hz)** — 无控制电压时的 VCO 输出频率 `1.8e9`（默认）| 正实数标量

没有任何控制电压输入（`0` V）时的 VCO 频率，或静态频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **Specify using** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `1.8e9` |

**数据类型：** `double`

### **Control voltage (V)** — 控制电压值 `[-5 0 5]`（默认）| 实数值向量

VCO 的控制电压值，指定为以 volts 为单位的实数值向量。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **Specify using** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认：** `[-5 0 5]` |

**数据类型：** `double`

### **Output frequency (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]`（默认）| 实数值向量

VCO 的输出频率值，对应于 **Control voltage (V)** 向量，以 Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **Specify using** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **输出幅度** — VCO 输出电压的最大幅度 `1`（默认）| positive real scalar

VCO 输出电压的最大幅度，指定为正实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `1` |

**数据类型：** `double`

#### 损伤

### **添加相位噪声** — 作为频率的函数添加相位噪声 off（默认）| on

选择以将作为频率函数的相位噪声引入 VCO。默认情况下，此选项未选中。

### **相位噪声频率偏移 (Hz)** — 相位噪声相对于载波频率的频率偏移 `[10e3 100e3 1e6 3e6 10e6]`（默认）| real valued vector

相位噪声相对于载波频率的频率偏移，指定为以 Hz 为单位的实数值向量。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **相位噪声电平 (dBc/Hz)** — 在相对于载波的指定频率偏移处的相位噪声功率 `[-77 -108 -134 -145 -154]`（默认）| real valued vector

实数值向量，指定在相对于载波的指定频率偏移处、以该偏移为中心 1 Hz 带宽内的相位噪声功率。该值以 dBc/Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `[-77 -108 -134 -145 -154]` |

**数据类型：** `double`

### **估计相位噪声参数** — 自动估计相位噪声参数 on（默认）| off

选择以自动估计相位噪声参数。默认情况下，此选项已选中。

您可以取消选择此选项，以定义自定义周期抖动和闪烁拐角频率。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

**数据类型：** `double`

### **周期抖动 (S)** — 周期抖动的标准差 `2.6794e-15`（默认）| positive real scalar

周期抖动的标准差，指定为以 seconds 为单位的正实数标量。周期抖动是时钟信号的周期时间相对于理想周期的偏差。

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声** 并取消选择 **估计相位噪声参数**。

#### 编程用法

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `2.6794e-15` |

**数据类型：** `double`

### **闪烁拐角频率 (Hz)** — 闪烁噪声的拐角频率 `517103.8168`（默认）| scalar

闪烁噪声的拐角频率，指定为以 hertz 为单位的标量。**闪烁拐角频率 (Hz)** 定义为由于闪烁噪声，相位噪声从 1/*f*2 过渡到 1/*f*3 的频率。在该频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声** 并取消选择 **估计相位噪声参数**。

#### 编程用法

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** character vector |
| **值：** scalar |
| **默认值：** `517103.8168` |

**数据类型：** `double`

### **绘制拟合** — 绘制指定和预期的 VCO 输出相位噪声密度按钮

点击以绘制 VCO 的指定相位噪声密度和可实现预期输出相位噪声密度。

### 预分频器

### **小数时钟分频器值** — 时钟分频器对输入频率进行分频的值 `70.20`（默认）| positive real scalar

时钟分频器对输入频率进行分频的值，指定为正实数标量。此参数可调。

#### 编程用法

- 使用 `get_param(gcb,'N')` 查看 **小数时钟分频器值** 的当前值。
- 使用 `set_param(gcb,'N',value)` 将 **小数时钟分频器值** 设置为特定值。

### **Delta Sigma Modulator 阶数** — Delta Sigma Modulator 的阶数 `3rd order`（默认）| `1st order` | `2nd order` | `4th order`

Delta Sigma Modulator 的阶数。有关更多信息，请参阅 Fractional Clock Divider with DSM。

#### 编程用法

- 使用 `get_param(gcb,'dsm')` 查看当前的 **Delta Sigma Modulator 阶数**。
- 使用 `set_param(gcb,'dsm',value)` 将 **Delta Sigma Modulator 阶数** 设置为特定值。

### **最小时钟分频器值** — 时钟分频器可以对输入频率进行分频的最小值 `70`（默认）| positive real scalar

时钟分频器可以对输入频率进行分频的最小值，指定为正实数标量。此参数也会在 **环路滤波器** 选项卡中报告，并用于自动计算环路滤波器的滤波器元件值。

#### 编程用法

- 使用 `get_param(gcb,'Nmin')` 查看 **最小时钟分频器值** 的当前值。
- 使用 `set_param(gcb,'Nmin',value)` 将 **最小时钟分频器值** 设置为特定值。

### 环路滤波器

### **滤波器元件值** — 确定滤波器元件如何计算 `Automatic`（默认）| `Manual`

选择如何计算环路滤波器的滤波器元件：

- 选择 `Automatic` 以根据系统规格自动计算滤波器元件。如果选择此选项，则 **环路滤波器** 选项卡中的电阻和电容编辑框不可编辑。相反，滤波器元件值根据 **环路带宽 (Hz)**、**相位裕度 (degrees)**、**VCO 电压灵敏度**、**电荷泵电流** 和 **最小时钟分频器值** 计算。默认情况下，此选项已选中。
- 选择 `Manual` 以手动输入电阻和电容值，从而设计自定义环路滤波器。

### **环路带宽 (Hz)** — 开环传递函数的幅度变为 1 时的频率 `0.5e6`（默认）| positive real scalar

开环传递函数的幅度变为 1 时的频率，指定为以 Hz 为单位的正实数标量。较低的 **环路带宽 (Hz)** 值会降低相位噪声和参考杂散，但代价是更长的锁定时间和更小的相位裕度。

#### 依赖关系

此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Automatic` 时可用。

#### 编程用法

- 使用 `get_param(gcb,'Fc')` 查看 **环路带宽 (Hz)** 的当前值。
- 使用 `set_param(gcb,'Fc',value)` 将 **环路带宽 (Hz)** 设置为特定值。

### **相位裕度 (degrees)** — 从 180° 中减去环路带宽处开环传递函数的相位 `45`（默认）| positive real scalar

从 180° 中减去环路带宽处开环传递函数的相位，指定为以 degrees 为单位的正实数标量。为获得最佳锁定时间，请选择 40° 到 55° 之间的相位裕度。

#### 依赖关系

此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Automatic` 时可用。

#### 编程用法

- 使用 `get_param(gcb,'Phi')` 查看 **相位裕度 (degrees)** 的当前值。
- 使用 `set_param(gcb,'Phi',value)` 将 **相位裕度 (degrees)** 设置为特定值。

**数据类型：** `double`

### **环路滤波器类型** — 环路滤波器的阶数 `3rd Order Passive`（默认）| `2nd Order Passive` | `4th Order Passive`

环路滤波器的阶数。在 PLL 系统中应用二阶、三阶或四阶无源 RC 环路滤波器。

### **C1 (F)** — 电容 1 `3e-11`（默认）| positive real scalar

电容器值 C1，指定为以 farad 为单位的正实数标量。

#### 依赖关系

此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'C1')` 查看 **C1 (F)** 的当前值。
- 使用 `set_param(gcb,'C1',value)` 将 **C1 (F)** 设置为特定值。

**数据类型：** `double`

### **C2 (F)** — 电容 2 `3.3e-10`（默认）| positive real scalar

电容器值 C2，指定为以 farad 为单位的正实数标量。

#### 依赖关系

此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'C2')` 查看 **C2 (F)** 的当前值。
- 使用 `set_param(gcb,'C2',value)` 将 **C2 (F)** 设置为特定值。

**数据类型：** `double`

### **C3 (F)** — 电容 3 `2.15e-12`（默认）| positive real scalar

电容器值 C3，指定为以 farad 为单位的正实数标量。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'C3')` 查看 **C3 (F)** 的当前值。
- 使用 `set_param(gcb,'C3',value)` 将 **C3 (F)** 设置为特定值。

**数据类型：** `double`

### **C4 (F)** — 电容 4 `1e-12`（默认）| positive real scalar

电容器值 C4，指定为以 farad 为单位的正实数标量。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order Passive`。
- 此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'C4')` 查看 **C4 (F)** 的当前值。
- 使用 `set_param(gcb,'C4',value)` 将 **C4 (F)** 设置为特定值。

**数据类型：** `double`

### **R2 (ohms)** — 电阻 2 `2.33e+03`（默认）| positive real scalar

电阻器值 R2，指定为以 ohms 为单位的正实数标量。

#### 依赖关系

此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'R2')` 查看 **R2 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R2',value)` 将 **R2 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R3 (ohms)** — 电阻 3 `2.98e+04`（默认）| positive real scalar

电阻器值 R3，指定为以 ohms 为单位的正实数标量。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'R3')` 查看 **R3 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R3',value)` 将 **R3 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R4 (ohms)** — 电阻 4 `12e3`（默认）| positive real scalar

电阻器值 R4，指定为以 ohms 为单位的正实数标量。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order Passive`。
- 此参数仅在 **环路滤波器** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时可编辑。

#### 编程用法

- 使用 `get_param(gcb,'R4')` 查看 **R4 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R4',value)` 将 **R4 (ohms)** 设置为特定值。

**数据类型：** `double`

### **启用损伤** — 将电路损伤添加到仿真 off（默认）| on

选择以将电路损伤（例如用于确定热噪声的工作温度）添加到仿真中。默认情况下，此选项未选中。

### **工作温度 (℃)** — 用于确定热噪声水平的温度 `30`（默认）| real scalar

电阻器的温度，指定为以 ℃ 为单位的实数标量。**工作温度** 确定热（Johnson）噪声的水平。

#### 依赖关系

要启用此参数，请在 **环路滤波器** 选项卡中选择 **启用损伤**。

#### 编程用法

- 使用 `get_param(gcb,'Temperature')` 查看 **工作温度** 的当前值。
- 使用 `set_param(gcb,'Temperature',value)` 将 **工作温度** 设置为特定值。

**数据类型：** `double`

### **导出环路滤波器元件值** — 导出环路滤波器元件值按钮

点击以将环路滤波器元件值导出到电子表格（XLS 文件）或导出为逗号分隔值（CSV 文件）。

### 探测

### **PFD up 和 PFD down (pfd\_up and pfd\_down)** — 选择以探测 PFD 输出 off（默认）| on

选择以探测 PFD 输出线（pfd\_up and pfd\_down）以查看 PFD 的响应。

### **电荷泵输出 (cp\_out)** — 选择以探测电荷泵输出 off（默认）| on

选择以探测电荷泵输出线（cp\_out）以查看电荷泵的响应。

### **环路滤波器输出 (lf\_out)** — 选择以探测环路滤波器输出 off（默认）| on

选择以探测环路滤波器输出线（lf\_out）以查看 Loop Filter 的响应。环路滤波器输出为 VCO 提供控制电压。

### **预分频器输出 (ps\_out)** — 选择以探测预分频器输出 off（默认）| on

选择以探测预分频器输出线（ps\_out）以查看 Fractional Clock Divider with Accumulator 的响应。

### 分析

### **开环分析** — 绘制预仿真开环分析 on（默认）| off

选择以在仿真前绘制 PLL 系统的增益裕度和相位裕度。默认情况下，此选项已选中。

### **闭环分析** — 绘制预仿真闭环分析 off（默认）| on

选择以在仿真前绘制 PLL 系统的零极点图、环路带宽、阶跃响应和冲激响应。您必须拥有 Control System Toolbox™ 的许可证才能绘制 PLL 系统的阶跃响应和冲激响应。默认情况下，此选项未选中。

### **绘制环路动态** — 绘制 PLL 系统的环路动态按钮

点击以绘制 PLL 系统的预仿真环路动态。

### **估计相位噪声** — 根据输入时钟估计相位噪声 off（默认）| on

选择以根据输入时钟估计相位噪声。默认情况下，此选项未选中。

### **参考频率 (Hz)** — 输入时钟的参考频率 `10e6`（默认）| positive real scalar

输入时钟的参考频率，指定为正实数标量。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `RefFreq` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `10e6` |

### **分辨率带宽 (Hz)** — 可分辨的最小正频率 `10e3`（默认）| positive real scalar

可分辨的最小正频率，指定为实数正标量。**分辨率带宽 (Hz)** 用于确定使用 Welch 方法进行频谱分析时的窗长。有关更多信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**分辨率带宽 (Hz)** 应小于最低偏移频率值。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Rbw` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `10e3` |

### **频率偏移向量 (Hz)** — 相对于基频的频率点，用于计算相位噪声 `[10e3 100e3 1e6 3e6 10e6]`（默认）| real valued vector

相对于基频的频率点，用于计算相位噪声，
指定为以 Hz 为单位的 real valued vector。

#### 依赖项

要启用此参数，请在
**分析**选项卡中选择 **估计相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `FrOffset` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

### **目标相位噪声电平 (dBc/Hz)** — 给定频率偏移向量的目标相位噪声曲线 `-inf`（默认）| vector | scalar

给定频率偏移向量的目标相位噪声曲线，以 dBc/Hz 为单位指定。
**目标相位噪声电平 (dBc/Hz)** 是在相对于载波的指定频率偏移处、以 1 Hz 带宽为中心的相位噪声功率。

#### 依赖项

要启用此参数，请在
**分析**选项卡中选择 **估计相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `TargetPn` |
| **类型：** character vector |
| **值：** vector | scalar |
| **默认值：** `-inf` |

### **绘制估计的相位噪声** — 绘制估计的输入时钟相位噪声按钮

点击以绘制估计的输入时钟相位噪声。

## 所属库

Mixed-Signal Blockset / PLL / Architectures

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

### R2023b: 估计 VCO 相位噪声参数

您可以估计 VCO 的相位噪声参数，也可以手动定义自定义周期抖动和闪烁拐角频率。您还可以绘制 VCO 的指定输出相位噪声密度和预期输出相位噪声密度。

## 描述

基于 delta sigma 调制器的分数 N PLL 架构的频率合成器

Fractional N PLL with Delta Sigma Modulator 参考架构使用
Fractional Clock Divider
with DSM 模块作为 PLL 系统中的分频器。该分频器
使用 delta sigma 调制技术将 VCO 输出信号的频率除以
一个小数值，使其可与
PFD 参考信号
频率相比较。
