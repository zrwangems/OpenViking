---
type: simulink-block
title: 'Integer N PLL with Dual Modulus Prescaler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Architectures'
documentation_page: 'integernpllwithdualmodulusprescaler'
documentation_source_path: 'ref/integernpllwithdualmodulusprescaler.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer N PLL with Dual Modulus Prescaler

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

### **编辑系统** — 断开库模块链接并用适当的值替换内部变量按钮

单击以断开模块与库的链接。内部变量将被替换为其值，模块变为简单子系统。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小按钮

选择以在仿真期间启用增大的缓冲区大小。这会增大 PLL 模型中所有属于 Mixed-Signal Blockset™/PLL/Building Blocks Simulink® library 的构建模块的缓冲区大小。这些构建模块为 PFD、Charge Pump、Loop Filter、VCO 和 Dual Modulus Prescaler。默认情况下，此选项未选中。

### **环路滤波器缓冲区大小** — 环路滤波器缓冲区大小 `1000`（默认）| positive integer scalar

环路滤波器的缓冲区大小，指定为 positive integer scalar。这将设置仿真期间可用于环路滤波器内部 Convert Sample Time 子系统的额外缓冲区样本数。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **环路滤波器缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖项

仅当选择 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBufferFilter')` 查看 **环路滤波器缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBufferFilter',value)` 将 **环路滤波器缓冲区大小** 设置为特定值。

### **PFD、charge pump、VCO、prescaler 的缓冲区大小** — PFD、charge pump、VCO 和 prescaler 的缓冲区大小 `10`（默认）| positive integer scalar

PFD、charge pump、VCO 和 prescaler 的缓冲区大小，指定为 positive integer scalar。这将设置 PLL 模型中 PFD、Charge Pump、VCO 和 Dual Modulus Prescaler 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **PFD、charge pump、VCO、prescaler 的缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖项

仅当选择 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **PFD、charge pump、VCO、prescaler 的缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **PFD、charge pump、VCO、prescaler 的缓冲区大小** 设置为特定值。

### PFD

#### 配置

### **死区补偿 (s)** — 为零相位偏移附近的有效输出添加的延迟 `40e-12`（默认）| positive real scalar

为零相位偏移附近的有效输出添加的延迟，指定为以秒为单位的 positive real scalar。死区是零相位偏移附近的相位偏移带，在此范围内 PFD 输出可忽略。

#### 程序化使用

- 使用 `get_param(gcb,'DeadbandCompensation')` 查看 **死区补偿 (s)** 的当前值。
- 使用 `set_param(gcb,'DeadbandCompensation',value)` 将 **死区补偿 (s)** 设置为特定值。

**数据类型：** `double`

#### 损伤

### **启用损伤** — 将电路损伤添加到仿真 off（默认）| on

选择以将电路损伤（如上升/下降时间和传播延迟）添加到仿真。默认情况下，此选项未选中。

### **输出步长计算** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据最大关注频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖项

要启用此参数，请在 **PFD** 选项卡中选择 **启用损伤**。

### **最大关注频率 (Hz)** — 输出端的最大关注频率 `10e9`（默认）| positive real scalar

输出端的最大关注频率，指定为以 Hz 为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **PFD** 选项卡中选择 **启用损伤**，并为 **输出步长计算** 选择 `Advanced`。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **最大关注频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **最大关注频率 (Hz)** 设置为特定值。

**数据类型：** `double`

### **上升/下降时间 (s)** — PFD 的 up 输出端口的 20% – 80% 上升/下降时间 `3e-11`（默认）| positive real scalar

PFD 的 up 输出端口的 20% – 80% 上升/下降时间，指定为以秒为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **PFD** 选项卡中选择 **启用损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallTime')` 查看 **上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallTime',value)` 将 **上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 PFD 输入端口到输出端口的延迟 `50e-12`（默认）| positive real scalar

从 PFD 输入端口到输出端口的延迟，指定为以秒为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **PFD** 选项卡中选择 **启用损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelay')` 查看 **传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelay',value)` 将 **传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

### Charge pump

#### 配置

### **输出电流 (A)** — 设计输出电流 `1e-3`（默认）| positive real scalar

设计输出电流的满量程幅度，指定为以安培为单位的 positive real scalar。此参数也会在 **Loop Filter** 选项卡中报告为 **Charge pump current**，并用于自动计算环路滤波器的滤波器组件值。此参数可调。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputCurrent` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `1e-3` |

**数据类型：** `double`

### **输入阈值 (V)** — 输入端口处的逻辑切换阈值 `0.5`（默认）| real scalar

输入端口处的逻辑切换阈值，指定为以伏特为单位的 real scalar。

#### 程序化使用

- 使用 `get_param(gcb,'InputThreshold')` 查看 **输入阈值 (V)** 的当前值。
- 使用 `set_param(gcb,'InputThreshold',value)` 将 **输入阈值 (V)** 设置为特定值。

**数据类型：** `double`

#### 损伤

### **启用电流损伤** — 将电流损伤添加到仿真 off（默认）| on

选择以将电流损伤（如电流不平衡和泄漏电流）添加到仿真。默认情况下，此选项未选中。

### **电流不平衡 (A)** — 满量程正电流与负电流之间的差 `1e-7`（默认）| positive real scalar

满量程正电流与负电流之间的差，指定为以安培为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用电流损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'CurrentImbalance')` 查看 **电流不平衡 (A)** 的当前值。
- 使用 `set_param(gcb,'CurrentImbalance',value)` 将 **电流不平衡 (A)** 设置为特定值。

**数据类型：** `double`

### **泄漏电流 (A)** — 没有任何输入时的输出电流 `1e-8`（默认）| nonnegative real scalar

当两个输入均处于逻辑零时的输出电流，指定为以安培为单位的 nonnegative real scalar。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用电流损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'LeakageCurrent')` 查看 **泄漏电流 (A)** 的当前值。
- 使用 `set_param(gcb,'LeakageCurrent',value)` 将 **泄漏电流 (A)** 设置为特定值。

**数据类型：** `double`

### **启用时序损伤** — 将时序损伤添加到仿真 off（默认）| on

选择以将时序损伤（如上升/下降时间和传播延迟）添加到仿真。默认情况下，此选项未选中。

### **输出步长计算** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据最大关注频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖项

要启用此参数，请在 **Charge Pump** 选项卡中选择 **启用时序损伤**。

### **最大关注频率 (Hz)** — 输出端的最大关注频率 `10e9`（默认）| positive real scalar

输出端的最大关注频率，指定为以 Hz 为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **Charge Pump** 选项卡中选择 **启用时序损伤**，并为 **输出步长计算** 选择 `Advanced`。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterestCp')` 查看 **最大关注频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterestCp',value)` 将 **最大关注频率 (Hz)** 设置为特定值。

**数据类型：** `double`

#### Up

### **上升/下降时间 (s)** — up 输入端口处的 20% – 80% 上升/下降时间 `5e-9`（默认）| positive real scalar

charge pump 的 up 输入端口处的 20% – 80% 上升/下降时间，指定为以秒为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallUp')` 查看 **Up 上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallUp',value)` 将 **Up 上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 up 输入端口到 charge pump 输出端口的总传播延迟 `6e-9`（默认）| positive real scalar

从 up 输入端口到 charge pump 输出端口的总传播延迟，指定为以秒为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Up 传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Up 传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

#### Down

### **上升/下降时间** — down 输入端口处的 20% – 80% 上升/下降时间 `2e-9`（默认）| scalar

charge pump 的 down 输入端口处的 20% – 80% 上升/下降时间。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallDown')` 查看 **Down 上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallDown',value)` 将 **Down 上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 up 输入端口到 charge pump 输出端口的总传播延迟 `4e-9`（默认）| positive real scalar

从 up 输入端口到 charge pump 输出端口的总传播延迟，指定为以秒为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Down 传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Down 传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

### VCO

### **指定方式** — 定义如何指定 VCO 输出频率 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage`

定义如何指定 VCO 输出频率：

- 选择 `Voltage sensitivity` 以根据 **电压灵敏度 (Hz/V)** 和 **自由运行频率 (Hz)** 指定输出频率。
- 选择 `Output frequency vs. control voltage` 以根据 **控制电压 (V)** 向量与 **输出频率 (Hz)** 向量进行插值来得到输出频率。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** character vector |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认值：** `Voltage sensitivity` |

### **电压灵敏度 (Hz/V)** — VCO 输出频率变化的度量 `100e6`（默认）| positive real scalar

对应于输入电压变化的输出频率变化的度量，指定为以 Hz/V 为单位的 positive real scalar。此参数也会在 **Loop Filter** 选项卡中报告为 **VCO voltage sensitivity**，并用于自动计算环路滤波器的滤波器组件值。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡的 **指定方式** 中选择 `Voltage sensitivity`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `100e6` |

**数据类型：** `double`

### **自由运行频率 (Hz)** — 没有控制电压时的 VCO 输出频率 `1.8e9`（默认）| positive real scalar

没有任何控制电压输入（`0` V）时的 VCO 频率，或静态频率，指定为以 Hz 为单位的 positive real scalar。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡的 **指定方式** 中选择 `Voltage sensitivity`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `1.8e9` |

**数据类型：** `double`

### **控制电压 (V)** — 控制电压值 `[-5 0 5]`（默认）| real valued vector

VCO 的控制电压值，指定为以伏特为单位的 real valued vector。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡的 **指定方式** 中选择 `Output frequency vs. control voltage`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `[-5 0 5]` |

**数据类型：** `double`

### **输出频率 (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]`（默认）| real valued vector

VCO 的输出频率值，对应于 **控制电压 (V)** 向量，以 Hz 为单位指定。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡的 **指定方式** 中选择 `Output frequency vs. control voltage`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **Output amplitude** — VCO 输出电压的最大幅度 `1` (默认) | 正实数标量

VCO 输出电压的最大幅度，指定为正实数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1` |

**数据类型：** `double`

#### 损伤

### **Add phase noise** — 将相位噪声作为频率的函数添加 off (默认) | on

选择以将相位噪声作为频率的函数引入 VCO。默认情况下，此选项未选中。

### **Phase noise frequency offset (Hz)** — 相位噪声相对于载波频率的频率偏移 `[10e3 100e3 1e6 3e6 10e6]` (默认) | 实数值向量

相位噪声相对于载波频率的频率偏移，指定为以 Hz 为单位的实数值向量。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡中选择 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — 相对于载波在指定频率偏移处的相位噪声功率 `[-77 -108 -134 -145 -154]` (默认) | 实数值向量

实数值向量，指定在相对于载波的指定频率偏移处、1 Hz 带宽内的相位噪声功率。该值以 dBc/Hz 为单位指定。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡中选择 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认值：** `[-77 -108 -134 -145 -154]` |

**数据类型：** `double`

### **Estimate phase noise parameters** — 自动估计相位噪声参数 on (默认) | off

选择以自动估计相位噪声参数。默认情况下，此选项已选中。

您可以取消选择此选项以定义自定义周期抖动和闪烁转角频率。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡中选择 **Add phase noise**。

**数据类型：** `double`

### **Period jitter (S)** — 周期抖动的标准差 `2.6794e-15` (默认) | 正实数标量

周期抖动的标准差，指定为以 seconds 为单位的正实数标量。周期抖动是时钟信号周期时间相对于理想周期的偏差。

要启用此参数，请在 **VCO** 选项卡中选择 **Add phase noise**，并取消选择 **Estimate phase noise parameters**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `2.6794e-15` |

**数据类型：** `double`

### **Flicker corner frequency (Hz)** — 闪烁噪声的转角频率 `517103.8168` (默认) | 标量

闪烁噪声的转角频率，指定为以 hertz 为单位的标量。**Flicker corner frequency (Hz)** 定义为由于闪烁噪声，相位噪声从 1/*f*2 过渡到 1/*f*3 的频率。在此频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 依赖项

要启用此参数，请在 **VCO** 选项卡中选择 **Add phase noise**，并取消选择 **Estimate phase noise parameters**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** character vector |
| **值：** 标量 |
| **默认值：** `517103.8168` |

**数据类型：** `double`

### **Plot fit** — 绘制指定和预期的 VCO 输出相位噪声密度按钮

点击以绘制指定的相位噪声密度和可实现的 VCO 期望输出相位噪声密度。

### Prescaler

### **Program counter value, P** — 双模预分频器内部程序计数器的值 `18` (默认) | 正实数标量

双模预分频器内部程序计数器的值，指定为正实数标量。**Program counter value, P** 用于计算有效分频值。此参数可调。有关更多信息，请参阅 Dual Modulus Prescaler。

#### 程序化使用

- 使用 `get_param(gcb,'ProgramCounter')` 查看当前 **Program counter value, P**。
- 使用 `set_param(gcb,'ProgramCounter',value)` 将 **Program counter value, P** 设置为特定值。

**数据类型：** `double`

### **Prescaler divider value, N** — 双模预分频器内部预分频器分频器的值 `5` (默认) | 正实数标量

双模预分频器内部预分频器分频器的值，指定为正实数标量。**Prescaler divider value, N** 用于计算有效分频值。此参数可调。有关更多信息，请参阅 Dual Modulus Prescaler。

#### 程序化使用

- 使用 `get_param(gcb,'PrescalerDivider')` 查看当前 **Prescaler divider value, N**。
- 使用 `set_param(gcb,'PrescalerDivider',value)` 将 **Prescaler divider value, N** 设置为特定值。

**数据类型：** `double`

### **Swallow counter value, S** — 双模预分频器内部吞脉冲计数器的值 `10` (默认) | 正实数标量

双模预分频器内部吞脉冲计数器的值，指定为正实数标量。**Swallow counter value, S** 用于计算有效分频值。有关更多信息，请参阅 Dual Modulus Prescaler。

#### 程序化使用

- 使用 `get_param(gcb,'SwallowCounter')` 查看当前 **Swallow counter value, S**。
- 使用 `set_param(gcb,'SwallowCounter',value)` 将 **Swallow counter value, S** 设置为特定值。

**数据类型：** `double`

### **Min clock divider value** — 时钟分频器可以对输入频率进行分频的最小值 `100` (默认) | 正实数标量

时钟分频器可以对输入频率进行分频的最小值，指定为正实数标量。此参数也在 **Loop Filter** 选项卡中报告，并用于自动计算环路滤波器的滤波器元件值。

#### 程序化使用

- 使用 `get_param(gcb,'Nmin')` 查看当前 **Min clock divider value** 的值。
- 使用 `set_param(gcb,'Nmin',value)` 将 **Min clock divider value** 设置为特定值。

**数据类型：** `double`

### Loop Filter

### **Filter component values** — 确定如何计算滤波器元件 `Automatic` (默认) | `Manual`

选择如何计算环路滤波器的滤波器元件：

- 选择 `Automatic` 以根据系统规格自动计算滤波器元件。如果选择此选项，则 **Loop Filter** 选项卡中的电阻和电容编辑框不可编辑。相反，滤波器元件值根据 **Loop bandwidth (Hz)**、**Phase margin (degrees)**、**VCO voltage sensitivity**、**Charge pump current** 和 **Min clock divider value** 计算。默认情况下，此选项已选中。
- 选择 `Manual` 以手动输入电阻和电容值，从而设计自定义环路滤波器。

### **Loop bandwidth (Hz)** — 开环传递函数的幅度变为 1 的频率 `1e6` (默认) | 正实数标量

开环传递函数的幅度变为 1 的频率，指定为以 Hz 为单位的正实数标量。

根据经验，环路带宽应为输入参考时钟的 1/10。较低的 **Loop bandwidth (Hz)** 值会降低相位噪声和参考杂散，但代价是更长的锁定时间和更小的相位裕度。

#### 依赖项

仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Automatic` 时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'Fc')` 查看当前 **Loop bandwidth (Hz)** 的值。
- 使用 `set_param(gcb,'Fc',value)` 将 **Loop bandwidth (Hz)** 设置为特定值。

**数据类型：** `double`

### **Phase margin (degrees)** — 从 180° 中减去开环传递函数在环路带宽处的相位 `45` (默认) | 正实数标量

从 180° 中减去开环传递函数在环路带宽处的相位，指定为以 degrees 为单位的正实数标量。为获得最佳锁定时间，请选择 40° 到 55° 之间的相位裕度。

#### 依赖项

仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Automatic` 时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'Phi')` 查看当前 **Phase margin (degrees)** 的值。
- 使用 `set_param(gcb,'Phi',value)` 将 **Phase margin (degrees)** 设置为特定值。

**数据类型：** `double`

### **Loop filter type** — 环路滤波器的阶数 `3rd Order Passive` (默认) | `2nd Order Passive` | `4th Order Passive`

环路滤波器的阶数。在 PLL 系统中应用二阶、三阶或四阶无源 RC 环路滤波器。

### **C1 (F)** — 电容 1 `5.24e-12` (默认) | 正实数标量

电容器值 C1，指定为以 farad 为单位的正实数标量。

#### 依赖项

仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'C1')` 查看当前 **C1 (F)** 的值。
- 使用 `set_param(gcb,'C1',value)` 将 **C1 (F)** 设置为特定值。

**数据类型：** `double`

### **C2 (F)** — 电容 2 `5.77e-11` (默认) | 正实数标量

电容器值 C2，指定为以 farad 为单位的正实数标量。

#### 依赖项

仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'C2')` 查看当前 **C2 (F)** 的值。
- 使用 `set_param(gcb,'C2',value)` 将 **C2 (F)** 设置为特定值。

**数据类型：** `double`

### **C3 (F)** — 电容 3 `3.76e-13` (默认) | 正实数标量

电容器值 C3，指定为以 farad 为单位的正实数标量。

#### 依赖项

- 要启用此参数，请在 **Loop filter type** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'C3')` 查看当前 **C3 (F)** 的值。
- 使用 `set_param(gcb,'C3',value)` 将 **C3 (F)** 设置为特定值。

**数据类型：** `double`

### **C4 (F)** — 电容 4 `1e-12` (默认) | 正实数标量

电容器值 C4，指定为以 farad 为单位的正实数标量。

#### 依赖项

- 要启用此参数，请在 **Loop filter type** 中选择 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'C4')` 查看当前 **C4 (F)** 的值。
- 使用 `set_param(gcb,'C4',value)` 将 **C4 (F)** 设置为特定值。

**数据类型：** `double`

### **R2 (ohms)** — 电阻 2 `6.66e+03` (默认) | 正实数标量

电阻器值 R2，指定为以 ohms 为单位的正实数标量。

#### 依赖项

仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'R2')` 查看当前 **R2 (ohms)** 的值。
- 使用 `set_param(gcb,'R2',value)` 将 **R2 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R3 (ohms)** — 电阻 3 `8.51e+04` (默认) | 正实数标量

电阻器值 R3，指定为以 ohms 为单位的正实数标量。

#### 依赖项

- 要启用此参数，请在 **Loop filter type** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'R3')` 查看当前 **R3 (ohms)** 的值。
- 使用 `set_param(gcb,'R3',value)` 将 **R3 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R4 (ohms)** — 电阻 4 `12e3` (默认) | 正实数标量

电阻器值 R4，指定为以 ohms 为单位的正实数标量。

#### 依赖项

- 要启用此参数，请在 **Loop filter type** 中选择 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **Filter Component values** 参数选择 `Manual` 时，此参数才可编辑。

#### 程序化使用

- 使用 `get_param(gcb,'R4')` 查看当前 **R4 (ohms)** 的值。
- 使用 `set_param(gcb,'R4',value)` 将 **R4 (ohms)** 设置为特定值。

**数据类型：** `double`

### **Enable impairments** — 将电路损伤添加到仿真 off (默认) | on

选择以将电路损伤（例如用于确定热噪声的工作温度）添加到仿真。默认情况下，此选项未选中。

### **Operating temperature (℃)** — 确定热噪声水平的温度 `30` (默认) | 实数标量

电阻器的温度，指定为以 ℃ 为单位的实数标量。**Operating temperature** 确定热（Johnson）噪声的水平。

#### 依赖项

要启用此参数，请在 **Loop Filter** 选项卡中选择 **Enable impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'Temperature')` 查看当前 **Operating temperature** 的值。
- 使用 `set_param(gcb,'Temperature',value)` 将 **Operating temperature** 设置为特定值。

**数据类型：** `double`

### **Export Loop Filter Component Values** — 导出环路滤波器元件值按钮

点击以将环路滤波器元件值导出到电子表格（XLS file）或导出为逗号分隔值（CSV file）。

### Probe

### **PFD up and PFD down (pfd\_up and pfd\_down)** — 选择以探测 PFD 输出 off (默认) | on

选择以探测 PFD 输出线（pfd\_up 和 pfd\_down），以查看 PFD 的响应。

### **Charge pump output (cp\_out)** — 选择以探测 charge pump 输出 off (默认) | on

选择以探测 charge pump 输出线（cp\_out），以查看 Charge Pump 的响应。

### **Loop filter output (lf\_out)** — 选择以探测 loop filter 输出 off (默认) | on

选择以探测 loop filter 输出线（lf\_out），以查看 Loop Filter 的响应。环路滤波器输出向 VCO 提供控制电压。

### **Prescaler output (ps\_out)** — 选择以探测预分频器输出 off (默认) | on

选择以探测预分频器输出线（ps\_out），以查看 Fractional Clock Divider with Accumulator 的响应。

### Analysis

### **Open Loop Analysis** — 绘制仿真前的开环分析 on (默认) | off

选择以在仿真前绘制 PLL 系统的增益裕度和相位裕度。默认情况下，此选项已选中。

### **Closed Loop Analysis** — 绘制仿真前的闭环分析 off (默认) | on

选择以在仿真前绘制 PLL 系统的零极点图、环路带宽、阶跃响应和冲激响应。您必须拥有 Control System Toolbox™ 的许可证，才能绘制 PLL 系统的阶跃响应和冲激响应。默认情况下，此选项未选中。

### **Plot Loop Dynamics** — 绘制 PLL 系统的环路动态按钮

点击以绘制 PLL 系统的仿真前环路动态。

### **Estimate phase noise** — 从输入时钟估计相位噪声 off (默认) | on

选择以从输入时钟估计相位噪声。默认情况下，此选项未选中。

### **Reference frequency (Hz)** — 输入时钟的参考频率 `10e6` (默认) | 正实数标量

输入时钟的参考频率，指定为正实数标量。

#### 依赖项

要启用此参数，请在 **分析** 选项卡中选择 **Estimate Phase Noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RefFreq` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `10e6` |

### **分辨率带宽 (Hz)** — 可分辨的最小正频率 `10e3`（默认值）| 正实数标量

可分辨的最小正频率，指定为正实数标量。**分辨率带宽 (Hz)** 用于确定使用 Welch 方法进行频谱分析时的窗长度。有关详细信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**分辨率带宽 (Hz)** 应小于最低偏移频率值。

#### 依赖关系

要启用此参数，请在 **Analysis** 选项卡中选择 **Estimate Phase Noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Rbw` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `10e3` |

### **频率偏移向量 (Hz)** — 相对于基频计算相位噪声的频率点 `[10e3 100e3 1e6 3e6 10e6]`（默认值）| 实数值向量

相对于基频计算相位噪声的频率点，指定为以 Hz 为单位的实数值向量。

#### 依赖关系

要启用此参数，请在 **Analysis** 选项卡中选择 **Estimate Phase Noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrOffset` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

### **目标相位噪声电平 (dBc/Hz)** — 给定频率偏移向量的目标相位噪声曲线 `-inf`（默认值）| 向量 | 标量

给定频率偏移向量的目标相位噪声曲线，以 dBc/Hz 为单位指定。**目标相位噪声电平 (dBc/Hz)** 是在相对于载波的指定频率偏移处、以 1 Hz 带宽为中心的相位噪声功率。

#### 依赖关系

要启用此参数，请在 **Analysis** 选项卡中选择 **Estimate Phase Noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetPn` |
| **类型：** character vector |
| **值：** 向量 | 标量 |
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

### R2023b：估计 VCO 相位噪声参数

您可以估计 VCO 的相位噪声参数，或手动定义自定义周期抖动和闪烁拐角频率。您还可以绘制 VCO 的指定输出相位噪声密度和预期输出相位噪声密度。

## 描述

基于双模预分频器的整数 N PLL 架构的频率合成器

Integer N PLL with Dual Modulus Prescaler 参考架构在 PLL 系统中使用 Dual Modulus Prescaler 模块作为分频器。该分频器将 VCO 输出信号的频率除以一个整数值，使其可与 PFD 参考信号频率进行比较。
