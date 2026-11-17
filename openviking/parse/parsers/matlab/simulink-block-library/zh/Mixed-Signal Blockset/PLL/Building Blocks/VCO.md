---
type: simulink-block
title: 'VCO'
family: 'msblks'
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
```yaml
ports:
- name: vctrl
  summary: 用于控制 VCO 输出频率的电压 标量 | 向量
  direction: input
  data_types: double
- name: vco out
  summary: 由 vctrl 端口决定的输出方波信号 标量
  direction: output
  data_types: double
```

### 输入

### **vctrl** — 用于控制 VCO 输出频率的电压 标量 | 向量

用于控制 VCO 输出频率的 VCO 控制电压。在锁相环（PLL）系统中，**vctrl** 是包含相位误差信息的环路滤波器输出。

**数据类型：** `double`
### 输出

### **vco out** — 由 `vctrl` 端口决定的输出方波信号 标量

VCO 的输出方波信号。在 PLL 系统中，**vco out** 是 PLL 生成的输出时钟。它 also 通过时钟分频器反馈到 PFD 模块，以完成控制环路。

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
- name: Voltage sensitivity (Hz/V)
  summary: VCO 输出频率的变化量度 100e6（默认）| 正实数标量
  group: 参数
  block_parameter: Kvco
  type: 字符向量
  values: 正实数标量
- name: Free running frequency (Hz)
  summary: 无控制电压时的 VCO 输出频率 2.5e9（默认）| 正实数标量
  group: 参数
  block_parameter: Fo
  type: 字符向量
  values: 正实数标量
- name: Control voltage (V)
  summary: 控制电压值 [-5 0 5]（默认）| 实数值向量
  group: 参数
  block_parameter: ControlVoltage
  type: 字符向量
  values: 实数值向量
- name: Output frequency (Hz)
  summary: VCO 输出频率值 [2e9 2.5e9 3e9]（默认）| 正实数值向量
  group: 参数
  block_parameter: OutputFrequency
  type: 字符向量
  values: 正实数值向量
- name: Output amplitude (V)
  summary: VCO 输出电压的最大幅度 1（默认）| 正实数标量
  group: 参数
  block_parameter: Amplitude
  type: 字符向量
  values: 正实数标量
  default: '1'
- name: Enable increased buffer size
  summary: 启用增大的缓冲区大小 off（默认）| on
  group: 参数
- name: Buffer size
  summary: 仿真期间可用的输入缓冲采样数 10（默认）| 正整数标量
  group: 参数
  block_parameter: NBuffer
  type: 字符向量
  values: 正整数标量
  default: '10'
- name: Add phase noise
  summary: 添加随频率变化的相位噪声 on（默认）| off
  group: 损伤
- name: Phase noise frequency offset (Hz)
  summary: 相位噪声相对于载波频率的频率偏移 [10e3 100e3 1e6 3e6 10e6]（默认）| 正实数值向量
  group: 损伤
  block_parameter: Foffset
  type: 字符向量
  values: 正实数值向量
  default: '[10e3 100e3 1e6 3e6 10e6]'
- name: Phase noise level (dBc/Hz)
  summary: 在指定频率偏移处相对于载波的相位噪声功率 [-77 -108 -134 -145 -154]（默认）| 负实数值向量
  group: 损伤
  block_parameter: PhaseNoise
  type: 字符向量
  values: 负实数值向量
  default: '[-77 -108 -134 -145 -154]'
```

### 参数

### **Specify using** — 定义 VCO 输出频率的指定方式 `Voltage sensitivity`（默认）| `Output frequency vs. control voltage`

定义 VCO 输出频率的指定方式：

- 选择 `Voltage sensitivity`，通过 **Voltage sensitivity (Hz/V)** 和 **Free running frequency (Hz)** 指定输出频率。
- 选择 `Output frequency vs. control voltage`，通过 **Control voltage (V)** 向量与 **Output frequency (Hz)** 向量插值得到输出频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpecifyUsing` |
| **类型：** 字符向量 |
| **值：** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **默认：** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — VCO 输出频率的变化量度 `100e6`（默认）| 正实数标量

输入电压变化引起的输出频率变化量度，指定为以 Hz/V 为单位的正实数标量。此参数也在 **Loop Filter** 选项卡中报告为 **VCO voltage sensitivity**，用于自动计算环路滤波器的滤波器元件值。

#### 依赖

要启用此参数，请在 **Parameters** 选项卡的 **Specify using** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `100e6` |

**数据类型：** `double`

### **Free running frequency (Hz)** — 无控制电压时的 VCO 输出频率 `2.5e9`（默认）| 正实数标量

无任何控制电压输入（`0` V）时的 VCO 频率，即静态频率，指定为以 Hz 为单位的正实数标量。

#### 依赖

要启用此参数，请在 **Parameters** 选项卡的 **Specify using** 中选择 `Voltage sensitivity`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Fo` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `2.5e9` |

**数据类型：** `double`

### **Control voltage (V)** — 控制电压值 `[-5 0 5]`（默认）| 实数值向量

VCO 的控制电压值，指定为以伏特为单位的实数值向量。

#### 依赖

要启用此参数，请在 **Parameters** 选项卡的 **Specify using** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControlVoltage` |
| **类型：** 字符向量 |
| **值：** 实数值向量 |
| **默认：** `[-5 0 5]` |

**数据类型：** `double`

### **Output frequency (Hz)** — VCO 输出频率值 `[2e9 2.5e9 3e9]`（默认）| 正实数值向量

与 **Control voltage (V)** 向量对应的 VCO 输出频率值，以 Hz 为单位指定。

#### 依赖

要启用此参数，请在 **Parameters** 选项卡的 **Specify using** 中选择 `Output frequency vs. control voltage`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数值向量 |
| **默认：** `[2e9 2.5e9 3e9]` |

**数据类型：** `double`

### **Output amplitude (V)** — VCO 输出电压的最大幅度 `1`（默认）| 正实数标量

VCO 输出电压的最大幅度，指定为正实数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Amplitude` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `1` |

**数据类型：** `double`

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 VCO 模块内部 Variable Pulse Delay 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `10`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。此参数设置 VCO 模块内部 Variable Pulse Delay 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，以使输入缓冲区包含所有所需的输入采样。

#### 依赖关系

要启用此参数，请选中 **Enable increased buffer size**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `10` |

**数据类型：** `double`

### 损伤

### **Add phase noise** — 添加随频率变化的相位噪声 on（默认）| off

选择此项可向 VCO 引入随频率变化的相位噪声。默认情况下，此选项已选中。

### **Phase noise frequency offset (Hz)** — 相位噪声相对于载波频率的频率偏移 `[10e3 100e3 1e6 3e6 10e6]`（默认）| 正实数值向量

相位噪声相对于载波频率的频率偏移，指定为以 Hz 为单位的正实数值向量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** 字符向量 |
| **值：** 正实数值向量 |
| **默认值：** `[10e3 100e3 1e6 3e6 10e6]` |

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — 在指定频率偏移处相对于载波的相位噪声功率 `[-77 -108 -134 -145 -154]`（默认）| 负实数值向量

在以指定频率偏移为中心、相对于载波的 1 Hz 带宽内的相位噪声功率，指定为以 dBc/Hz 为单位的负实数值向量。**Phase noise level** 的元素与 **Phase noise frequency offset** 中的对应元素相对应。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Add phase noise**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** 字符向量 |
| **值：** 负实数值向量 |
| **默认值：** `[-77 -108 -134 -145 -154]` |

**数据类型：** `double`
## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对压控振荡器进行建模

VCO 或压控振荡器是一种电压到频率转换器。它产生一个输出方波信号，其频率由输入 **vctrl** 端口处的电压控制。输出信号的频率 *F* 由以下任一方式确定：

F=(KVCO·Vctrl)+Fo

其中：

- *K*vco = 电压灵敏度（单位为 Hz/V）
- *V*ctrl = 控制电压（单位为 V）
- *F*o= 自由运行频率（单位为 Hz）

或者通过使用以下映射进行线性插值：

F=interp(Fout(Vcntl))

其中：

- *V*ctnl = 控制电压向量（单位为 V）
- *F*out= 对应输出频率向量（单位为 Hz）
