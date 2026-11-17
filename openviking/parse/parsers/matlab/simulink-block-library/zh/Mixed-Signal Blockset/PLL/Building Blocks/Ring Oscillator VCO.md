---
type: simulink-block
title: 'Ring Oscillator VCO'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'ringoscillatorvco'
documentation_source_path: 'ref/ringoscillatorvco.html'
language: zh-CN
chinese_source: worker-translation
---

# Ring Oscillator VCO

## 端口
```yaml
ports:
- name: vctrl
  summary: 用于控制 VCO 输出频率的电压 标量 | 向量
  direction: input
  data_types: double
- name: vco out
  summary: 由 vctrl 端口决定的输出信号 标量
  direction: output
  data_types: double
```

### 输入

### **vctrl** — 用于控制 VCO 输出频率的电压 标量 | 向量

用于控制环形振荡器 VCO 输出频率的 VCO 控制电压。在锁相环（PLL）系统中，**vctrl** 是环路滤波器的输出，包含相位误差信息。

**数据类型：** `double`
### 输出

### **vco out** — 由 `vctrl` 端口决定的输出信号 标量

环形振荡器 VCO 的输出信号。在 PLL 系统中，**vco out** 是 PLL 生成的输出时钟。它 also 通过时钟分频器反馈到 PFD 模块，以完成控制环路。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Specify using
  summary: 定义 VCO 输出频率的指定方式 Voltage sensitivity（默认）| Output frequency vs. control voltage
  group: 参数
  block_parameter: SpecifyUsing
  type: 字符向量
  values: Voltage sensitivity | Output frequency vs. control voltage
  default: Voltage sensitivity
- name: Voltage sensitivity (Hz/V)
  summary: VCO 输出频率的变化量度 100e6（默认）| 正实数标量
  group: 参数
  block_parameter: Kvco
  type: 字符向量
  values: 正实数标量
  default: 100e6
- name: Free running frequency (Hz)
  summary: 无控制电压时的 VCO 输出频率 2.5e9（默认）| 正实数标量
  group: 参数
  block_parameter: Fo
  type: 字符向量
  values: 正实数标量
  default: 2.5e9
- name: Control voltage (V)
  summary: 控制电压值 [-5 0 5]（默认）| 实值向量
  group: 参数
  block_parameter: ControlVoltage
  type: 字符向量
  values: 实值向量
  default: '[-5 0 5]'
- name: Output frequency (Hz)
  summary: VCO 输出频率值 [2e9 2.5e9 3e9]（默认）| 正实值向量
  group: 参数
  block_parameter: OutputFrequency
  type: 字符向量
  values: 正实值向量
  default: '[2e9 2.5e9 3e9]'
- name: Output amplitude (V)
  summary: VCO 输出电压的最大幅度 1（默认）| 正实数标量
  group: 参数
  block_parameter: Amplitude
  type: 字符向量
  values: 正实数标量
- name: Enable increased buffer size
  summary: 启用增大的缓冲区大小 off（默认）| on
  group: 参数
- name: Buffer size
  summary: 仿真期间可用的输入缓冲采样数 10（默认）| 正整数标量
  group: 参数
  block_parameter: NBuffer
  type: 字符向量
  values: 正整数标量
- name: Add phase noise
  summary: 添加随频率变化的相位噪声 on（默认）| off
  group: 损伤
- name: Model double sided phase noise instead of single sided
  summary: 对双边相位噪声而非单边相位噪声建模 off（默认）| on
  group: 损伤
- name: Phase noise frequency offset (Hz)
  summary: 指定相位噪声相对于载波的频率偏移 [30e3 100e3 1e6 3e6 10e6]（默认）| 正实数值向量
  group: 损伤
  block_parameter: Foffset
  type: 字符向量
  values: 正实数值向量
- name: Phase noise level (dBc/Hz)
  summary: 在相对于载波的相位噪声频率偏移处指定的相位噪声功率 [-56 -106 -132 -143 -152]（默认）| 负实数值向量
  group: 损伤
  block_parameter: PhaseNoise
  type: 字符向量
  values: 负实数值向量
- name: Estimate phase noise parameters
  summary: 设置旨在匹配指定噪声频谱的噪声参数 按钮
  group: 损伤
- name: Period jitter (S)
  summary: 周期抖动的标准差 1.7e-15（默认）| 正实数标量
  group: 损伤
  block_parameter: PeriodJitter
  type: 字符向量
  values: 正实数标量
- name: Flicker corner frequency (Hz)
  summary: 闪烁噪声的拐角频率 5e5（默认）| 标量
  group: 损伤
  block_parameter: CornerFrequency
  type: 字符向量
  values: 标量
- name: Customize flicker exponent (Advanced feature)
  summary: 自定义闪烁噪声功率谱分布 关（默认）| 开
  group: 损伤
- name: Flicker exponent
  summary: 闪烁噪声功率指数 1.0（默认）| 0.8 | 0.9 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5
  group: 损伤
  block_parameter: FlickerExponent
  type: 字符向量
  values: 1.0 | 0.8 | 0.9 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5
- name: Plot fit
  summary: 绘制指定和期望的输出相位噪声密度 按钮
  group: 损伤
```

### 参数

### **Specify using** — 定义 VCO 输出频率的指定方式 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage`

定义 VCO 输出频率的指定方式：

- 选择 `Voltage sensitivity` 以通过 **Voltage sensitivity (Hz/V)** 和 **Free running frequency (Hz)** 参数指定输出频率。
- 选择 `Output frequency vs. control voltage` 以通过 **Control voltage (V)** 向量与 **Output frequency (Hz)** 向量进行插值来得到输出频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** 字符向量 |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认值：** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — VCO 输出频率的变化量度 `100e6`（默认）| 正实数标量

输入电压变化引起的输出频率变化量度，指定为以 Hz/V 为单位的正实数标量。此参数也在 **Loop Filter** 选项卡中报告为 **VCO voltage sensitivity**，用于自动计算环路滤波器的滤波器元件值。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡中将 **Specify using** 设置为 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `100e6` |

**数据类型：** `double`

### **Free running frequency (Hz)** — 无控制电压时的 VCO 输出频率 `2.5e9`（默认）| 正实数标量

无任何控制电压输入（`0` V）时的 VCO 频率，即静态频率，指定为以赫兹为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡中将 **Specify using** 设置为 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `2.5e9` |

**数据类型：** `double`

### **Control voltage (V)** — 控制电压值 `[-5 0 5]`（默认）| 实值向量

VCO 的控制电压值，指定为以伏特为单位的实值向量。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡中将 **Specify using** 设置为 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认值：** `[-5 0 5]` |

**数据类型：** `double`

### **Output frequency (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]`（默认）| 正实值向量

对应于 **Control voltage (V)** 向量的 VCO 输出频率，以赫兹为单位指定。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡中将 **Specify using** 设置为 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** 字符向量 |
| **值：** 正实值向量 |
| **默认值：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **Output amplitude (V)** — VCO 输出电压的最大幅度 `1`（默认）| 正实数标量

VCO 输出电压的最大幅度，指定为正实数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1` |

**数据类型：** `double`

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Ring Oscillator VCO 模块内部 Variable Pulse Delay 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `10`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 Ring Oscillator VCO 模块内部 Variable Pulse Delay 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入采样。

#### 依赖关系

要启用此参数，请选中 **Enable increased buffer size**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认：** `10` |

**数据类型：** `double`

### 损伤

### **Add phase noise** — 添加随频率变化的相位噪声 on（默认）| off

选择此项可向 VCO 引入随频率变化的相位噪声。默认情况下，此选项已选中。

### **Model double sided phase noise instead of single sided** — 对双边相位噪声而非单边相位噪声建模 off（默认）| on

选择此项可对双边相位噪声而非单边相位噪声建模。默认情况下，该模块假定指定的相位噪声为单边相位噪声。

### **Phase noise frequency offset (Hz)** — 指定相位噪声相对于载波的频率偏移 `[30e3 100e3 1e6 3e6 10e6]`（默认）| 正实数值向量

指定相位噪声相对于载波的频率偏移，指定为以赫兹为单位的正实数值向量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** 字符向量 |
| **值：** 正实数值向量 |
| **默认：** `[30e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — 在相对于载波的相位噪声频率偏移处指定的相位噪声功率 `[-56 -106 -132 -143 -152]`（默认）| 负实数值向量

在相对于载波的相位噪声频率偏移处、以 1 Hz 带宽为中心的指定相位噪声功率，指定为以 dBc/Hz 为单位的负实数值向量。**Phase noise level** 的元素对应于 **Phase noise frequency offset (Hz)** 参数中的相对元素。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** 字符向量 |
| **值：** 负实数值向量 |
| **默认：** `[-56 -106 -132 -143 -152]` |

**数据类型：** `double`

### **Estimate phase noise parameters** — 设置旨在匹配指定噪声频谱的噪声参数 按钮

单击以将噪声参数设置为旨在匹配指定噪声频谱的初始估计值。

### **Period jitter (S)** — 周期抖动的标准差 `1.7e-15`（默认）| 正实数标量

周期抖动的标准差，指定为正实数标量，单位为秒。周期抖动是时钟信号的周期时间相对于理想周期的偏差。

#### 编程使用

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1.7e-15` |

### **Flicker corner frequency (Hz)** — 闪烁噪声的拐角频率 `5e5`（默认）| 标量

闪烁噪声的拐角频率，指定为标量，单位为赫兹。**Flicker corner frequency (Hz)** 定义为由于闪烁噪声导致相位噪声从 1/*f*2 过渡到 1/*f*3 的频率。在该频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 编程使用

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `5e5` |

### **Customize flicker exponent (Advanced feature)** — 自定义闪烁噪声功率谱分布 关（默认）| 开

选择此参数以自定义闪烁噪声的功率谱分布。传统上，闪烁噪声定义为 1/*f* 噪声，但它可以变化为 1/*fV*，其中 0.8<*V*<1.5。

### **Flicker exponent** — 闪烁噪声功率指数 `1.0`（默认）| `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5`

闪烁噪声功率指数，指定在 `0.8` 到 `1.5` 之间。

#### 编程使用

|  |
| --- |
| **模块参数：** `FlickerExponent` |
| **类型：** 字符向量 |
| **值：** `1.0` | `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5` |
| **默认：** `1.0` |

### **Plot fit** — 绘制指定和期望的输出相位噪声密度 按钮

点击以绘制指定的相位噪声密度和可实现的期望输出相位噪声密度。
## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

### R2023b：对双边相位噪声建模

您可以指定 VCO 相位噪声是单边还是双边。

## 描述

对环形振荡器 VCO 建模

Ring Oscillator VCO 模块对 VCO（压控振荡器）的输出信号、频率控制、周期抖动和闪烁噪声进行建模，例如偏置控制的环形振荡器电路。此模块使用环形振荡器相位噪声的数学描述来生成相位噪声。这使得在启动期间和后续仿真期间能够更快地计算仿真结果。您还可以通过选择高斯噪声水平、拐角频率和闪烁指数来控制相位噪声分布。相位噪声频谱限于环形振荡器物理模型所能产生的频谱。

您可以选择相位噪声数学描述的系数。您可以从数据手册中提供特定的相位噪声频谱密度，并将其与数学系数产生的相位噪声频谱密度进行比较。然后，您可以调整系数，以在物理上最合理的方式拟合指定的相位噪声。

**注意**

如果闪烁噪声拐角频率设置为零，Ring Oscillator VCO 模块也可用于对谐振回路调谐 VCO 进行建模。
