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

### **digital** — 来自 DAC 的数字输入信号（标量）

来自 DAC 的数字输入信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — 来自 DAC 的转换后模拟信号（标量）

来自 DAC 的转换后模拟信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟（标量）

用于启动转换的外部时钟，指定为标量。此端口确定数模转换过程何时开始。

**数据类型：** `double`

## 参数

### **Digital signal frequency (Hz)** — DAC 数字输入信号的频率 `1e3`（默认）| 正实数标量

DAC 模块数字输入信号的频率，指定为以 Hz 为单位的正实数标量。**Digital signal frequency (Hz)** 必须与受测 DAC 设备的输入频率匹配。

**Digital input frequency (Hz)** 需要满足两个要求：

- 必须激活 DAC 的所有输出码。
- **Digital signal frequency (Hz)** 与 **Conversion start frequency (Hz)** 除 1 外不得共享任何公倍数。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1e3` |

**数据类型：** `double`

### **Start conversion frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的实数标量。**Start conversion frequency** 参数确定启动转换时的转换速率。

#### 编程用法

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1e6` |

**数据类型：** `double`

### **Settling time tolerance (LSB)** — 用于计算建立时间的容差 `0.5`（默认）| 正实数标量

允许用于计算建立时间的容差，指定为以 LSB 为单位的正实数标量。DAC 的输出必须在 **Settling time (s)** 之前稳定在 **Settling time tolerance (LSB)** 范围内。

#### 编程用法

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `0.5` |

**数据类型：** `double`

### **Hold off time (s)** — 测量分析前的延迟，用于避免瞬态造成破坏 `0`（默认）| 非负实数标量

测量分析前的延迟，用于避免瞬态造成破坏，指定为以 s 为单位的非负实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** character vector |
| **值：** 非负实数标量 |
| **默认值：** `0` |

### **Recommended simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `0.09`（默认）| 正实数标量

仿真必须运行的最短时间，以获得有意义的结果，指定为以 s 为单位的正实数标量。

要测量 AC 性能，仿真必须运行到 DAC 能够生成 DAC 输出的六次频谱更新。因此，**Recommended simulation stop time (s)** *T* 由 [1] 给出：

T=6(1.5RBW+Hold off time),

其中 *RBW* 是 DAC Testbench 模块内部频谱估计器的分辨率带宽，由以下方程给出：RBW=[min(Input frequency)0.1]。

此参数仅由模块报告，不可编辑。

**数据类型：** `double`

### **Output result to base workspace** — 将详细测试结果存储到基础工作区 off（默认）| on

将详细测试结果存储到基础工作区中的结构体中，以便在仿真结束时进一步处理。默认情况下，此参数未选中。

### **Workspace variable name** — 存储详细测试结果的变量名称 `dac_ac_out`（默认）| character string

存储详细测试结果的变量名称，指定为 character string。

#### 依赖关系

要启用此参数，请选择 **Output result to base workspace** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型：** character vector |
| **值：** character string |
| **默认值：** `dac_ac_out` |

### **Show spectrum analyzer during simulation** — 在仿真期间显示 Spectrum Analyzer on（默认）| off

选择此参数以在仿真期间显示 Spectrum Analyzer 窗口。默认情况下，此参数处于选中状态。

## 所属库

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量 DAC 输出的 AC 性能指标

DAC AC Measurement 模块测量 DAC AC 性能指标，例如信噪比 (SNR)、信号与噪声及失真比 (SINAD)、无杂散动态范围 (SFDR)、有效位数 (ENOB) 和噪声底。您可以使用 DAC AC Measurement 模块验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以使用您自己实现的 DAC
