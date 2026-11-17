---
type: simulink-block
title: 'DAC AC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Measurements & Testbenches'
documentation_page: 'dacacmeasurement'
documentation_source_path: 'ref/dacacmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# DAC AC Measurement

## 端口

### 输入

### **digital** — 来自 DAC 的数字输入信号 标量

来自 DAC 的数字输入信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — 来自 DAC 的转换后模拟信号 标量

来自 DAC 的转换后模拟信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟 标量

用于启动转换的外部时钟，指定为标量。此端口决定数模转换过程何时开始。

**数据类型：** `double`

## 参数

### **Digital signal frequency (Hz)** — DAC 数字输入信号的频率 `1e3`（默认）| 正实数标量

DAC 模块数字输入信号的频率，指定为以赫兹为单位的正实数标量。**Digital signal frequency (Hz)** 必须与被测 DAC 设备的输入频率匹配。

**Digital input frequency (Hz)** 需要满足两个要求：

- DAC 的所有输出码必须被激活。
- **Digital signal frequency (Hz)** 与 **Conversion start frequency (Hz)** 之间除 1 外不得有任何公倍数。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1e3` |

**数据类型：** `double`

### **Start conversion frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的实数标量。**Start conversion frequency** 参数决定转换开始时的转换速率。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1e6` |

**数据类型：** `double`

### **Settling time tolerance (LSB)** — 用于计算建立时间的容差 `0.5`（默认）| 正实数标量

用于计算建立时间的允许容差，指定为以 LSB 为单位的正实数标量。DAC 的输出必须在 **Settling time (s)** 内稳定在 **Settling time tolerance (LSB)** 范围内。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `0.5` |

**数据类型：** `double`

### **Hold off time (s)** — 测量分析前的延迟，以避免瞬态干扰 `0`（默认）| 非负实数标量

测量分析前的延迟，以避免瞬态干扰，指定为以秒为单位的非负实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `0` |

### **Recommended simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `0.09`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

要测量交流性能，仿真必须运行到 DAC 能够生成 DAC 输出的六次频谱更新。因此，**Recommended simulation stop time (s)** *T* 由下式给出 [1]：

T=6(1.5RBW+Hold off time)，

其中 *RBW* 是 DAC Testbench 模块内频谱估计器的分辨率带宽，由以下公式给出：RBW=[min(Input frequency)0.1]。

此参数仅由模块报告，不可编辑。

**数据类型：** `double`

### **Output result to base workspace** — 将详细测试结果存储到基础工作区 off（默认）| on

在仿真结束时将详细测试结果存储到基础工作区中的结构体，以便进一步处理。默认情况下，此参数未选中。

### **Workspace variable name** — 存储详细测试结果的变量名称 `dac_ac_out`（默认）| 字符字符串

存储详细测试结果的变量名称，指定为字符字符串。

#### 依赖关系

要启用此参数，请选择 **Output result to base workspace** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型**：character vector |
| **值**：character string |
| **默认值**：`dac_ac_out` |

### **Show spectrum analyzer during simulation** — 在仿真期间显示频谱分析仪 on（默认）| off

选择此参数以在仿真期间显示频谱分析仪窗口。默认情况下，此参数处于选中状态。

## 所属库

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量 DAC 输出的交流性能指标

DAC AC Measurement 模块测量 DAC 交流性能指标，例如信噪比（SNR）、信纳比（SINAD）、无杂散动态范围（SFDR）、有效位数（ENOB）和噪声底。您可以使用 DAC AC Measurement 模块来验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以使用您自己实现的 DAC
