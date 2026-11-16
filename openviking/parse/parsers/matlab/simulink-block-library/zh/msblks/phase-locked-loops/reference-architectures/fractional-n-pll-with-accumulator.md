---
type: simulink-block
title: 'Fractional N PLL with Accumulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Phase-Locked Loops / Reference Architectures'
documentation_page: 'fractionalnpllwithaccumulator'
documentation_source_path: 'ref/fractionalnpllwithaccumulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Fractional N PLL with Accumulator

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

### **编辑系统** — 断开库模块链接并将内部变量替换为适当值的按钮

单击以断开与库的模块链接。内部变量将替换为其值，并且该模块变为简单子系统。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小按钮

选择以在仿真期间启用增大的缓冲区大小。这增大了 PLL 模型中属于 Mixed-Signal Blockset™/PLL/Building Blocks Simulink® 库的所有构建模块的缓冲区大小。构建模块为 PFD、Charge Pump、Loop Filter、VCO 和 Fractional Clock Divider with Accumulator。默认情况下，此选项未选中。

### **Loop Filter 缓冲区大小** — Loop Filter 的缓冲区大小 `1000` (default) | 正整数标量

Loop Filter 的缓冲区大小，指定为正整数标量。这将在仿真期间可用的额外缓冲区样本数设置为 Loop Filter 内部的 Convert Sample Time 子系统。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **Loop Filter 缓冲区大小** 设置为足够大的值，以使输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当选择 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBufferFilter')` 查看 **Loop Filter 缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBufferFilter',value)` 将 **Loop Filter 缓冲区大小** 设置为特定值。

### **PFD、Charge pump、VCO、prescaler 缓冲区大小** — PFD、Charge pump、VCO 和 prescaler 的缓冲区大小 `10` (default) | 正整数标量

PFD、Charge pump、VCO 和 prescaler 的缓冲区大小，指定为正整数标量。这将设置 PLL 模型内 PFD、Charge Pump、VCO 和 Fractional Clock Divider with Accumulator 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **PFD、Charge pump、VCO、prescaler 缓冲区大小** 设置为足够大的值，以使输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当选择 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **PFD、Charge pump、VCO、prescaler 缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **PFD、Charge pump、VCO、prescaler 缓冲区大小** 设置为特定值。

### PFD

#### 配置

### **死区补偿 (s)** — 在零相位偏移附近为有效输出添加的延迟 `40e-12` (default) | 正实数标量

在零相位偏移附近为有效输出添加的延迟，指定为以秒为单位的正实数标量。死区是零相位偏移附近的相位偏移带，在该带内 PFD 输出可忽略。

#### 程序化使用

- 使用 `get_param(gcb,'DeadbandCompensation')` 查看 **死区补偿 (s)** 的当前值。
- 使用 `set_param(gcb,'DeadbandCompensation',value)` 将 **死区补偿 (s)** 设置为特定值。

**数据类型：** `double`

#### 非理想效应

### **启用非理想效应** — 向仿真添加电路非理想效应 off (default) | on

选择以向仿真添加电路非理想效应，例如上升/下降时间和传播延迟。默认情况下，此选项未选中。

### **输出步长计算** — 确定如何计算输出步长 `Default` (default) | `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据最大关注频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **启用非理想效应**。

### **最大关注频率 (Hz)** — 输出端的最大关注频率 `10e9` (default) | 正实数标量

输出端的最大关注频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **启用非理想效应**，并为 **输出步长计算** 选择 **Advanced**。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **最大关注频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **最大关注频率 (Hz)** 设置为特定值。

**数据类型：** `double`

### **上升/下降时间 (s)** — PFD 的 up 输出端口的 20% – 80% 上升/下降时间 `3e-11` (default) | 正实数标量

PFD 的 up 输出端口的 20% – 80% 上升/下降时间，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **启用非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallTime')` 查看 **上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallTime',value)` 将 **上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 PFD 输入端口到输出端口的延迟 `50e-12` (default) | 正实数标量

从 PFD 的输入端口到输出端口的延迟，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **PFD** 选项卡中选择 **启用非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelay')` 查看 **传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelay',value)` 将 **传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

### Charge pump

#### 配置

### **输出电流 (A)** — 设计输出电流 `1e-3` (default) | 正实数标量

设计输出电流的满量程幅度，指定为以安培为单位的正实数标量。此参数还在 **Loop Filter** 选项卡中报告为 **Charge pump current**，并用于自动计算 Loop Filter 的滤波器元件值。此参数可调。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputCurrent` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `1e-3` |

**数据类型：** `double`

### **输入阈值 (V)** — 输入端口的逻辑切换阈值 `0.5` (default) | 实数标量

输入端口的逻辑切换阈值，指定为以伏特为单位的实数标量。

#### 程序化使用

- 使用 `get_param(gcb,'InputThreshold')` 查看 **输入阈值 (V)** 的当前值。
- 使用 `set_param(gcb,'InputThreshold',value)` 将 **输入阈值 (V)** 设置为特定值。

**数据类型：** `double`

#### 非理想效应

### **启用电流非理想效应** — 向仿真添加电流非理想效应 off (default) | on

选择以向仿真添加电流非理想效应，例如电流不平衡和泄漏电流。默认情况下，此选项未选中。

### **电流不平衡 (A)** — 满量程正电流和负电流之间的差 `1e-7` (default) | 正实数标量

满量程正电流和负电流之间的差，指定为以安培为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用电流非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'CurrentImbalance')` 查看 **电流不平衡 (A)** 的当前值。
- 使用 `set_param(gcb,'CurrentImbalance',value)` 将 **电流不平衡 (A)** 设置为特定值。

**数据类型：** `double`

### **泄漏电流 (A)** — 没有任何输入时的输出电流 `1e-8` (default) | 非负实数标量

当两个输入均为逻辑零时的输出电流，指定为以安培为单位的非负实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用电流非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'LeakageCurrent')` 查看 **泄漏电流 (A)** 的当前值。
- 使用 `set_param(gcb,'LeakageCurrent',value)` 将 **泄漏电流 (A)** 设置为特定值。

**数据类型：** `double`

### **启用时序非理想效应** — 向仿真添加时序非理想效应 off (default) | on

选择以向仿真添加时序非理想效应，例如上升/下降时间和传播延迟。默认情况下，此选项未选中。

### **输出步长计算** — 确定如何计算输出步长 `Default` (default) | `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据最大关注频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **Charge Pump** 选项卡中选择 **启用时序非理想效应**。

### **最大关注频率 (Hz)** — 输出端的最大关注频率 `10e9` (default) | 正实数标量

输出端的最大关注频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge Pump** 选项卡中选择 **启用时序非理想效应**，并为 **输出步长计算** 选择 **Advanced**。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterestCp')` 查看 **最大关注频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterestCp',value)` 将 **最大关注频率 (Hz)** 设置为特定值。

**数据类型：** `double`

#### Up

### **上升/下降时间 (s)** — up 输入端口的 20% – 80% 上升/下降时间 `5e-9` (default) | 正实数标量

charge pump 的 up 输入端口的 20% – 80% 上升/下降时间，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallUp')` 查看 **Up 上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallUp',value)` 将 **Up 上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 charge pump 的 up 输入端口到输出端口的总传播延迟 `6e-9` (default) | 正实数标量

从 charge pump 的 up 输入端口到输出端口的总传播延迟，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Up 传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Up 传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

#### Down

### **上升/下降时间** — down 输入端口的 20% – 80% 上升/下降时间 `2e-9` (default) | 标量

charge pump 的 down 输入端口的 20% – 80% 上升/下降时间。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallDown')` 查看 **Down 上升/下降时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallDown',value)` 将 **Down 上升/下降时间 (s)** 设置为特定值。

**数据类型：** `double`

### **传播延迟 (s)** — 从 charge pump 的 up 输入端口到输出端口的总传播延迟 `4e-9` (default) | 正实数标量

从 charge pump 的 up 输入端口到输出端口的总传播延迟，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Charge pump** 选项卡中选择 **启用时序非理想效应**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Down 传播延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Down 传播延迟 (s)** 设置为特定值。

**数据类型：** `double`

### VCO

### **指定依据** — 定义如何指定 VCO 输出频率 `Voltage sensitivity` (default) | `Output frequency vs. control voltage`

定义如何指定 VCO 输出频率：

- 选择 `Voltage sensitivity` 以根据 **电压灵敏度 (Hz/V)** 和 **自由运行频率 (Hz)** 指定输出频率。
- 选择 `Output frequency vs. control voltage` 以根据 **控制电压 (V)** 向量与 **输出频率 (Hz)** 向量插值输出频率。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** character vector |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认：** `Voltage sensitivity` |

### **电压灵敏度 (Hz/V)** — VCO 输出频率变化的度量 `100e6` (default) | 正实数标量

针对输入电压变化的输出频率变化度量，指定为以 Hz/V 为单位的正实数标量。此参数还在 **Loop Filter** 选项卡中报告为 **VCO 电压灵敏度**，并用于自动计算 Loop Filter 的滤波器元件值。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **指定依据** 中选择 `Voltage sensitivity`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `100e6` |

**数据类型：** `double`

### **自由运行频率 (Hz)** — 无控制电压时的 VCO 输出频率 `1.8e9` (default) | 正实数标量

没有任何控制电压输入（`0` V）时 VCO 的频率，或静态频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **指定依据** 中选择 `Voltage sensitivity`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `1.8e9` |

**数据类型：** `double`

### **控制电压 (V)** — 控制电压值 `[-5 0 5]` (default) | 实数值向量

VCO 的控制电压值，指定为以伏特为单位的实数值向量。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **指定依据** 中选择 `Output frequency vs. control voltage`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认：** `[-5 0 5]` |

**数据类型：** `double`

### **输出频率 (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]` (default) | 实数值向量

与 **控制电压 (V)** 向量对应的 VCO 的输出频率值，以 Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡的 **指定依据** 中选择 `Output frequency vs. control voltage`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **输出幅度** — VCO 输出电压的最大幅度 `1`（默认） | 正实数标量

VCO 输出电压的最大幅度，指定为正实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1` |

**数据类型：** `double`

#### 损伤

### **添加相位噪声** — 添加作为频率函数的相位噪声 off（默认） | on

选择此项可向 VCO 引入作为频率函数的相位噪声。默认情况下，此选项未选中。

### **相位噪声频率偏移 (Hz)** — 相位噪声相对于载波频率的频率偏移 `[10e3 100e3 1e6 3e6 10e6]`（默认） | 实值向量

相位噪声相对于载波频率的频率偏移，指定为实值向量，单位为 Hz。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

#### 编程使用

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** character vector |
| **值：** 实值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **相位噪声电平 (dBc/Hz)** — 在相对于载波的指定频率偏移处的相位噪声功率 `[-77 -108 -134 -145 -154]`（默认） | 实值向量

实值向量，指定以相对于载波的指定频率偏移为中心的 1 Hz 带宽内的相位噪声功率。该值以 dBc/Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

#### 编程使用

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** character vector |
| **值：** 实值向量 |
| **默认值：** `[-77 -108 -134 -145 -154]` |

**数据类型：** `double`

### **估计相位噪声参数** — 自动估计相位噪声参数 on（默认） | off

选择此项可自动估计相位噪声参数。默认情况下，此选项已选中。

您可以取消选择此选项，以定义自定义的周期抖动和闪烁拐角频率。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**。

**数据类型：** `double`

### **周期抖动 (S)** — 周期抖动的标准差 `2.6794e-15`（默认） | 正实数标量

周期抖动的标准差，指定为正实数标量，单位为 seconds。周期抖动是时钟信号周期时间相对于理想周期的偏差。

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**，并取消选择 **估计相位噪声参数**。

#### 编程使用

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `2.6794e-15` |

**数据类型：** `double`

### **闪烁拐角频率 (Hz)** — 闪烁噪声的拐角频率 `517103.8168`（默认） | 标量

闪烁噪声的拐角频率，指定为标量，单位为 hertz。**闪烁拐角频率 (Hz)** 定义为由于闪烁噪声导致相位噪声从 1/*f*2 转变为 1/*f*3 的频率。在该频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 依赖关系

要启用此参数，请在 **VCO** 选项卡中选择 **添加相位噪声**，并取消选择 **估计相位噪声参数**。

#### 编程使用

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** character vector |
| **值：** 标量 |
| **默认值：** `517103.8168` |

**数据类型：** `double`

### **绘制拟合** — 绘制指定的和预期的 VCO 输出相位噪声密度按钮

单击以绘制指定的相位噪声密度以及 VCO 可实现的预期输出相位噪声密度。

### Prescaler

### **小数时钟分频器值** — 时钟分频器对输入频率进行分频的值 `70.20`（默认） | 正实数标量

时钟分频器对输入频率进行分频的值，指定为正实数标量。此参数可调。

#### 编程使用

- 使用 `get_param(gcb,'N')` 查看
  **小数时钟分频器值** 的当前值。
- 使用 `set_param(gcb,'N',value)` 将
  **小数时钟分频器值** 设置为特定值。

### **最小时钟分频器值** — 时钟分频器可对输入频率进行分频的最小值 `70`（默认） | 正实数标量

时钟分频器可对输入频率进行分频的最小值，指定为正实数标量。此参数也会报告在 **Loop Filter** 选项卡中，并用于自动计算环路滤波器的滤波器元件值。

#### 编程使用

- 使用 `get_param(gcb,'Nmin')` 查看
  **最小时钟分频器值** 的当前值。
- 使用 `set_param(gcb,'Nmin',value)` 将 **最小时钟分频器值** 设置为特定值。

### Loop Filter

### **滤波器元件值** — 确定如何计算滤波器元件 `Automatic`（默认） | `Manual`

选择如何计算环路滤波器的滤波器元件：

- 选择 `Automatic` 以根据系统规格自动计算滤波器元件。如果选择此选项，**Loop Filter** 选项卡中的电阻和电容编辑框不可编辑。相反，滤波器元件值根据 **环路带宽 (Hz)**、**相位裕度 (degrees)**、**VCO 电压灵敏度**、**电荷泵电流** 和 **最小时钟分频器值** 计算。默认情况下，此选项已选中。
- 选择 `Manual` 以手动输入电阻和电容值，设计自定义环路滤波器。

### **环路带宽 (Hz)** — 开环传递函数的幅度变为 1 时的频率 `0.5e6`（默认） | 正实数标量

开环传递函数的幅度变为 1 时的频率，指定为正实数标量，单位为 Hz。**环路带宽 (Hz)** 的较低值会降低相位噪声和参考杂散，但代价是更长的锁定时间和更小的相位裕度。

#### 依赖关系

仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Automatic` 时，此参数才可用。

#### 编程使用

- 使用 `get_param(gcb,'Fc')` 查看 **环路带宽 (Hz)** 的当前值。
- 使用 `set_param(gcb,'Fc',value)` 将 **环路带宽 (Hz)** 设置为特定值。

### **相位裕度 (degrees)** — 在环路带宽处从 180° 中减去的开环传递函数相位 `45`（默认） | 正实数标量

在环路带宽处从 180° 中减去的开环传递函数相位，指定为正实数标量，单位为 degrees。为获得最佳锁定时间，请选择 40° 到 55° 之间的相位裕度。

#### 依赖关系

仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Automatic` 时，此参数才可用。

#### 编程使用

- 使用 `get_param(gcb,'Phi')` 查看 **相位裕度 (degrees)** 的当前值。
- 使用 `set_param(gcb,'Phi',value)` 将 **相位裕度 (degrees)** 设置为特定值。

**数据类型：** `double`

### **环路滤波器类型** — 环路滤波器的阶数 `3rd Order Passive`（默认） | `2nd Order Passive` | `4th Order Passive`

环路滤波器的阶数。在 PLL 系统中应用二阶、三阶或四阶无源 RC 环路滤波器。

### **C1 (F)** — 电容 1 `3e-11`（默认） | 正实数标量

电容器值 C1，指定为正实数标量，单位为 farad。

#### 依赖关系

仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'C1')` 查看 **C1 (F)** 的当前值。
- 使用 `set_param(gcb,'C1',value)` 将 **C1 (F)** 设置为特定值。

**数据类型：** `double`

### **C2 (F)** — 电容 2 `3.3e-10`（默认） | 正实数标量

电容器值 C2，指定为正实数标量，单位为 farad。

#### 依赖关系

仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'C2')` 查看 **C2 (F)** 的当前值。
- 使用 `set_param(gcb,'C2',value)` 将 **C2 (F)** 设置为特定值。

**数据类型：** `double`

### **C3 (F)** — 电容 3 `2.15e-12`（默认） | 正实数标量

电容器值 C3，指定为正实数标量，单位为 farad。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'C3')` 查看 **C3 (F)** 的当前值。
- 使用 `set_param(gcb,'C3',value)` 将 **C3 (F)** 设置为特定值。

**数据类型：** `double`

### **C4 (F)** — 电容 4 `1e-12`（默认） | 正实数标量

电容器值 C4，指定为正实数标量，单位为 farad。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'C4')` 查看 **C4 (F)** 的当前值。
- 使用 `set_param(gcb,'C4',value)` 将 **C4 (F)** 设置为特定值。

**数据类型：** `double`

### **R2 (ohms)** — 电阻 2 `2.33e+03`（默认） | 正实数标量

电阻器值 R2，指定为正实数标量，单位为 ohms。

#### 依赖关系

仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'R2')` 查看 **R2 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R2',value)` 将 **R2 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R3 (ohms)** — 电阻 3 `2.98e+04`（默认） | 正实数标量

电阻器值 R3，指定为正实数标量，单位为 ohms。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `3rd Order Passive` 或 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'R3')` 查看 **R3 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R3',value)` 将 **R3 (ohms)** 设置为特定值。

**数据类型：** `double`

### **R4 (ohms)** — 电阻 4 `12e3`（默认） | 正实数标量

电阻器值 R4，指定为正实数标量，单位为 ohms。

#### 依赖关系

- 要启用此参数，请在 **环路滤波器类型** 中选择 `4th Order Passive`。
- 仅当在 **Loop Filter** 选项卡中为 **滤波器元件值** 参数选择 `Manual` 时，此参数才可编辑。

#### 编程使用

- 使用 `get_param(gcb,'R4')` 查看 **R4 (ohms)** 的当前值。
- 使用 `set_param(gcb,'R4',value)` 将 **R4 (ohms)** 设置为特定值。

**数据类型：** `double`

### **启用损伤** — 将电路损伤添加到仿真 off（默认） | on

选择此项可将电路损伤（例如工作温度）添加到仿真中，以确定热噪声。默认情况下，此选项未选中。

### **工作温度 (℃)** — 用于确定热噪声水平的温度 `30`（默认） | 实标量

电阻器的温度，指定为实标量，单位为 ℃。**工作温度** 确定热（Johnson）噪声的水平。

#### 依赖关系

要启用此参数，请在 **Loop Filter** 选项卡中选择 **启用损伤**。

#### 编程使用

- 使用 `get_param(gcb,'Temperature')` 查看 **工作温度** 的当前值。
- 使用 `set_param(gcb,'Temperature',value)` 将 **工作温度** 设置为特定值。

**数据类型：** `double`

### **导出环路滤波器元件值** — 导出环路滤波器元件值按钮

单击以将环路滤波器元件值导出到电子表格（XLS 文件）或作为逗号分隔值（CSV 文件）。

### 探测

### **PFD up 和 PFD down (pfd\_up 和 pfd\_down)** — 选择以探测 PFD 输出 off（默认） | on

选择以探测 PFD 输出线（pfd\_up 和 pfd\_down），查看 PFD 的响应。

### **电荷泵输出 (cp_out)** — 选择以探测电荷泵输出 off（默认） | on

选择以探测电荷泵输出线（cp_out），查看 Charge Pump 的响应。

### **环路滤波器输出 (lf_out)** — 选择以探测环路滤波器输出 off（默认） | on

选择以探测环路滤波器输出线（lf_out），查看 Loop Filter 的响应。环路滤波器输出向 VCO 提供控制电压。

### **Prescaler 输出 (ps_out)** — 选择以探测 Prescaler 输出 off（默认） | on

选择以探测 Prescaler 输出线（ps_out），查看 Fractional Clock Divider with Accumulator 的响应。

### 分析

### **开环分析** — 绘制仿真前开环分析 on（默认） | off

选择以在仿真前绘制 PLL 系统的增益裕度和相位裕度。默认情况下，此选项已选中。

### **闭环分析** — 绘制仿真前闭环分析 off（默认） | on

选择以在仿真前绘制 PLL 系统的零极点图、环路带宽、阶跃响应和冲激响应。您必须拥有 Control System Toolbox™ 许可证才能绘制 PLL 系统的阶跃响应和冲激响应。默认情况下，此选项未选中。

### **绘制环路动态** — 绘制 PLL 系统的环路动态按钮

单击以绘制 PLL 系统的仿真前环路动态。

### **估计相位噪声** — 从输入时钟估计相位噪声 off（默认） | on

选择以从输入时钟估计相位噪声。默认情况下，此选项未选中。

### **参考频率 (Hz)** — 输入时钟的参考频率 `10e6`（默认） | 正实数标量

输入时钟的参考频率，指定为正实数标量。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程使用

|  |
| --- |
| **模块参数：** `RefFreq` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `10e6` |

### **分辨率带宽 (Hz)** — 可分辨的最小正频率 `10e3`（默认） | 正实数标量

可分辨的最小正频率，指定为正实数标量。**分辨率带宽 (Hz)** 用于确定使用 Welch 方法进行频谱分析的窗长。有关详细信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**分辨率带宽 (Hz)** 应小于最低偏移频率值。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程使用

|  |
| --- |
| **模块参数：** `Rbw` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `10e3` |

### **频率偏移向量 (Hz)** — 相对于基频计算相位噪声的频率点 `[10e3 100e3 1e6 3e6 10e6]`（默认） | 实值向量

相对于基频计算相位噪声的频率点，指定为实值向量，单位为 Hz。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrOffset` |
| **类型：** character vector |
| **值：** 实值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

### **目标相位噪声电平 (dBc/Hz)** — 给定频率偏移向量的目标相位噪声曲线 `-inf`（默认） | vector | scalar

给定频率偏移向量的目标相位噪声曲线，以 dBc/Hz 为单位指定。
**目标相位噪声电平 (dBc/Hz)** 是在相对于载波的指定频率偏移处、以该偏移为中心、1 Hz 带宽内的相位噪声功率。

#### 依赖关系

要启用此参数，请在 **分析** 选项卡中选择 **估计相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `TargetPn` |
| **类型：** character vector |
| **值：** vector | scalar |
| **默认值：** `-inf` |

### **绘制估计的相位噪声** — 绘制估计的输入时钟相位噪声按钮

单击以绘制估计的输入时钟相位噪声。

## 所属库

Mixed-Signal Blockset / PLL / Architectures

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

### R2023b：估计 VCO 相位噪声参数

您可以估计 VCO 的相位噪声参数，也可以手动定义自定义周期抖动和闪烁拐点频率。您还可以绘制 VCO 的指定输出相位噪声密度和期望输出相位噪声密度。

## 描述

采用基于累加器的分数 N PLL 架构的频率合成器

Fractional N PLL with Accumulator 参考架构使用 Fractional Clock Divider with Accumulator 模块作为 PLL 系统中的分频器。该分频器将 VCO 输出信号的频率除以一个分数值，以使其与 PFD 参考信号频率相当。
