---
type: simulink-block
title: 'Sampling Clock Source'
family: 'adc'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Building Blocks'
documentation_page: 'samplingclocksource'
documentation_source_path: 'ref/samplingclocksource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sampling Clock Source

## 端口

### 输出

### **clk** — 带孔径抖动的输出时钟 scalar

带孔径抖动的输出时钟信号，以 scalar 形式返回。该时钟是周期脉冲序列，根据 **Clock type** 参数，可以是正弦波或方波。

**数据类型：** `double`

## 参数

### **Clock type** — 输出时钟信号形状 `Square wave`（默认）| `Sine wave`

输出时钟信号的形状。

- `Square wave` — 返回幅度为 1 volts、频率为指定值的方波。
- `Sine wave` — 返回幅度为 1 volts、频率为指定值的正弦波。

#### 程序化用法

|  |
| --- |
| **模块参数：** `SignalType` |
| **类型：** character vector |
| **取值：** `Square wave` | `Sine wave` |
| **默认值：** `Square wave` |

### **Clock frequency (Hz)** — 输出时钟信号的期望频率 `1e6`（默认）| scalar

输出时钟信号的期望频率，指定为以 hertz 为单位的 scalar。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Freq` |
| **类型：** character vector |
| **取值：** scalar |
| **默认值：** `1e6` |

### **Min (V)** — 最小时钟输出电压 `0`（默认）| real scalar

输出时钟信号的最小电压，指定为以 volts 为单位的 real scalar。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Min` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认值：** `0` |

### **Max (V)** — 最大时钟输出电压 `1`（默认）| real scalar

输出时钟信号的最大电压，指定为以 volts 为单位的 real scalar。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Max` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认值：** `1` |

### **RMS aperture jitter (s)** — 时钟边沿位置的标准差 `1e-12`（默认）| real nonnegative scalar

时钟边沿位置的标准差，由相对于理想时钟的受损时钟生成。**RMS aperture jitter** 指定为以 seconds 为单位的 real nonnegative scalar。

孔径延迟是采样时钟信号与实际采集样本时刻之间的延迟。孔径抖动是孔径延迟的样本间变化。孔径抖动会导致 ADC 中产生误差电压，该误差电压与抖动大小以及到 ADC 的输入信号压摆率成正比。

#### 程序化用法

|  |
| --- |
| **模块参数：** `RMSJitt` |
| **类型：** character vector |
| **取值：** nonnegative real scalar |
| **默认值：** `1e-12` |

#### 高级

### **Specify custom seed** — 指定种子 off（默认）| on

选择此项可指定用于生成时钟信号的自定义种子。默认情况下，此选项未选中。

### **Seed** — 用于生成时钟信号的种子 `0`（默认）| nonnegative real scalar

用于生成时钟信号的种子，指定为 nonnegative real scalar。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Seed` |
| **类型：** character vector |
| **取值：** nonnegative real scalar |
| **默认值：** `0` |

#### 依赖关系

要启用此参数，请在 **高级** 选项卡中选择 **Specify custom seed**。

### **Specify custom initial output** — 指定初始输出 off（默认）| on

选择此项可为采样时钟源指定自定义初始输出。默认情况下，此选项未选中。

### **Initial output** — 采样时钟的初始输出 `1`（默认）| real scalar

采样时钟源的初始输出，指定为 real scalar。

#### 程序化用法

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认值：** `0` |

#### 依赖关系

要启用此参数，请在 **高级** 选项卡中选择 **Specify custom initial output**。

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Sampling Clock Source 模块内部 Variable Pulse Delay 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲的样本数 `50`（默认）| positive integer scalar

仿真期间可用的输入缓冲的样本数，指定为 positive integer scalar。这会设置 Sampling Clock Source 模块内部 Variable Pulse Delay 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成精确输出样本所需的输入样本数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

要启用此参数，请在 **高级** 选项卡中选择 **Enable increased buffer size**。

#### 程序化用法

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** character vector |
| **取值：** positive integer scalar |
| **默认值：** `50` |

## 所属库

Mixed-Signal Blockset / ADC / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

生成带孔径抖动的时钟信号

Sampling Clock Source 模块生成具有孔径抖动损伤的正弦波或方波时钟。
