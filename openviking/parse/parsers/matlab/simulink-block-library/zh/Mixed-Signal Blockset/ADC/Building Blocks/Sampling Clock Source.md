---
type: simulink-block
title: 'Sampling Clock Source'
family: 'msblks'
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

### **clk** — 带孔径抖动的输出时钟 标量

带孔径抖动的输出时钟信号，以标量形式返回。该时钟是周期性脉冲序列，根据 **Clock type** 参数可以是正弦波或方波。

**数据类型：** `double`

## 参数

### **Clock type** — 输出时钟信号形状 `Square wave`（默认）| `Sine wave`

输出时钟信号的形状。

- `Square wave` — 返回幅度为 1 伏特、频率指定的方波。
- `Sine wave` — 返回幅度为 1 伏特、频率指定的正弦波。

#### 编程使用

|  |
| --- |
| **模块参数：** `SignalType` |
| **类型：** 字符向量 |
| **值：** `Square wave` | `Sine wave` |
| **默认：** `Square wave` |

### **Clock frequency (Hz)** — 输出时钟信号的期望频率 `1e6`（默认）| 标量

输出时钟信号的期望频率，以赫兹为单位的标量指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `Freq` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `1e6` |

### **Min (V)** — 最小时钟输出电压 `0`（默认）| 实标量

输出时钟信号的最小电压，以伏特为单位的实标量指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `Min` |
| **类型：** 字符向量 |
| **值：** 实标量 |
| **默认：** `0` |

### **Max (V)** — 最大时钟输出电压 `1`（默认）| 实标量

输出时钟信号的最大电压，以伏特为单位的实标量指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `Max` |
| **类型：** 字符向量 |
| **值：** 实标量 |
| **默认：** `1` |

### **RMS aperture jitter (s)** — 时钟边沿位置的标准差 `1e-12`（默认）| 实非负标量

时钟边沿位置的标准差，由相对于理想时钟的受损时钟生成。**RMS aperture jitter** 以秒为单位的实非负标量指定。

孔径延迟是采样时钟信号与实际采样时刻之间的延迟。孔径抖动是孔径延迟之间的逐样本变化。孔径抖动会在 ADC 中产生误差电压，该误差电压与抖动幅度和 ADC 输入信号的压摆率成正比。

#### 编程使用

|  |
| --- |
| **模块参数：** `RMSJitt` |
| **类型：** 字符向量 |
| **值：** 非负实标量 |
| **默认：** `1e-12` |

#### 高级

### **Specify custom seed** — 指定种子 off（默认）| on

选择此项以指定用于生成时钟信号的自定义种子。默认情况下，此选项未选中。

### **Seed** — 用于生成时钟信号的种子 `0`（默认）| 非负实标量

用于生成时钟信号的种子，以非负实标量指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `Seed` |
| **类型：** 字符向量 |
| **值：** 非负实标量 |
| **默认：** `0` |

#### 依赖关系

要启用此参数，请在 **Advanced** 选项卡中选择 **Specify custom seed**。

### **Specify custom initial output** — 指定初始输出 off（默认）| on

选择此项以指定采样时钟源的自定义初始输出。默认情况下，此选项未选中。

### **Initial output** — 采样时钟的初始输出 `1`（默认）| 实标量

采样时钟源的初始输出，以实标量指定。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量 |
| **值：** 实标量 |
| **默认：** `0` |

#### 依赖关系

要启用此参数，请在 **Advanced** 选项卡中选择 **Specify custom initial output**。

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Sampling Clock Source 模块内部 Variable Pulse Delay 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `50`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。此参数设置 Sampling Clock Source 模块内部 Variable Pulse Delay 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。请将 **Buffer size** 设置为足够大的值，以确保输入缓冲区包含所有所需的输入采样。

#### 依赖关系

要启用此参数，请在 **Advanced** 选项卡中选择 **Enable increased buffer size**。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型**：character vector |
| **值**：positive integer scalar |
| **默认值**：`50` |

## 所属库

Mixed-Signal Blockset / ADC / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

生成带有孔径抖动的时钟信号

Sampling Clock Source 模块生成带有孔径抖动损伤的正弦波或方波时钟。
