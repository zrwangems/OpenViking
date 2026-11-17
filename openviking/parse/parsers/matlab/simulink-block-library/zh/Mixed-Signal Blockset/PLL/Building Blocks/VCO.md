---
type: simulink-block
title: 'VCO'
family: 'pll'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'vco'
documentation_source_path: 'ref/vco.html'
language: zh-CN
chinese_source: worker-translation
---

# VCO

## 端口

### 输入

### **vctrl** — 用于控制 VCO 输出频率的电压 标量 | 向量

用于控制 VCO 输出频率的 VCO 控制电压。在锁相环 (PLL) 系统中，**vctrl** 是包含相位误差信息的 Loop Filter 的输出。

**数据类型：** `double`

### 输出

### **vco out** — 由 `vctrl` 端口确定的输出方波信号 标量

VCO 的输出方波信号。在 PLL 系统中，**vco out** 是由 PLL 生成的输出时钟。它还通过分频器反馈到 PFD 模块，以完成控制环路。

**数据类型：** `double`

## 参数

### 参数

### **指定方式** — 定义如何指定 VCO 输出频率 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage`

定义如何指定 VCO 输出频率：

- 选择 `Voltage sensitivity`，以通过 **电压灵敏度 (Hz/V)** 和 **自由运行频率 (Hz)** 指定输出频率。
- 选择 `Output frequency vs. control voltage`，以根据 **控制电压 (V)** 向量与 **输出频率 (Hz)** 向量插值输出频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** character vector |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认值：** `Voltage sensitivity` |

### **电压灵敏度 (Hz/V)** — VCO 输出频率变化的度量 `100e6`（默认）| 正实数标量

输入电压变化时输出频率变化的度量，指定为以 Hz/V 为单位的正实数标量。此参数还在 **Loop Filter** 选项卡中报告为 **VCO 电压灵敏度**，并用于自动计算环路滤波器的滤波器元件值。

#### 依赖关系

要启用此参数，请在 **参数** 选项卡的 **指定方式** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `100e6` |

**数据类型：** `double`

### **自由运行频率 (Hz)** — 无控制电压时的 VCO 输出频率 `2.5e9`（默认）| 正实数标量

没有任何控制电压输入（`0` V）时的 VCO 频率，即静态频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **参数** 选项卡的 **指定方式** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `2.5e9` |

**数据类型：** `double`

### **控制电压 (V)** — 控制电压值 `[-5 0 5]`（默认）| 实数值向量

VCO 的控制电压值，指定为以 V 为单位的实数值向量。

#### 依赖关系

要启用此参数，请在 **参数** 选项卡的 **指定方式** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** character vector |
| **值：** 实数值向量 |
| **默认值：** `[-5 0 5]` |

**数据类型：** `double`

### **输出频率 (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]`（默认）| 正实数值向量

VCO 的输出频率值，对应于 **控制电压 (V)** 向量，以 Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **参数** 选项卡的 **指定方式** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** character vector |
| **值：** 正实数值向量 |
| **默认值：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **输出幅度 (V)** — VCO 输出电压的最大幅度 `1`（默认）| 正实数标量

VCO 输出电压的最大幅度，指定为正实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1` |

**数据类型：** `double`

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 VCO 模块内 Variable Pulse Delay 模块的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `10`（默认）| 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。此参数设置 VCO 模块内 Variable Pulse Delay 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。请将 **缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

要启用此参数，请选择 **启用增大的缓冲区大小**。

#### 编程用法

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** character vector |
| **值：** 正整数标量 |
| **默认值：** `10` |

**数据类型：** `double`

### 损伤

### **添加相位噪声** — 添加随频率变化的相位噪声 on（默认）| off

选择此项可向 VCO 引入随频率变化的相位噪声。默认情况下，此选项处于选中状态。

### **相位噪声频率偏移 (Hz)** — 相位噪声相对于载波频率的频率偏移 `[10e3 100e3 1e6 3e6 10e6]`（默认）| 正实数值向量

相位噪声相对于载波频率的频率偏移，指定为以 Hz 为单位的正实数值向量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **添加相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** character vector |
| **值：** 正实数值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **相位噪声电平 (dBc/Hz)** — 在相对于载波的指定频率偏移处的相位噪声功率 `[-77 -108 -134 -145 -154]`（默认）| 负实数值向量

在相对于载波的指定频率偏移处，以 1 Hz 带宽测量的相位噪声功率，指定为以 dBc/Hz 为单位的负实数值向量。**相位噪声电平** 的元素对应于 **相位噪声频率偏移** 中的相应元素。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **添加相位噪声**。

#### 编程用法

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** character vector |
| **值：** 负实数值向量 |
| **默认值：** `[-77 -108 -134 -145 -154]` |

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

在 R2025b 中未记载。

## 扩展功能

在 R2025b 中未记载。

## 版本历史

**在 R2019a 中引入**

## 描述

对电压控制振荡器进行建模

VCO 或电压控制振荡器是一种电压到频率转换器。它产生输出方波信号，其频率由输入 **vctrl** 端口上的电压控制。输出信号的频率 *F* 由以下任一方式确定：

F=(KVCO·Vctrl)+Fo

其中：

- *K*vco = 电压灵敏度（以 Hz/V 为单位）
- *V*ctrl = 控制电压（以 V 为单位）
- *F*o= 自由运行频率（以 Hz 为单位）

或通过以下映射进行线性插值：

F=interp(Fout(Vcntl))

其中：

- *V*ctnl = 控制电压向量（以 V 为单位）
- *F*out= 对应的输出频率向量（以 Hz 为单位）
