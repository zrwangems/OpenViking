---
type: simulink-block
title: 'DAC DC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Measurements & Testbenches'
documentation_page: 'dacdcmeasurement'
documentation_source_path: 'ref/dacdcmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# DAC DC Measurement

## 端口

### 输入

### **digital** — 来自 DAC 的数字输入信号（标量）

来自 DAC 的数字信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — 来自 DAC 的转换后模拟信号（标量）

来自 DAC 的转换后模拟信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟（标量）

用于启动转换的外部时钟，指定为标量。此端口确定数模转换过程何时启动。

**数据类型：** `double`

## 参数

### **输入极性** — DAC 输入信号的极性 `Bipolar`（默认）| `Unipolar`

DAC 输入信号的极性。

#### 编程使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型：** character vector |
| **值：** `Bipolar`|`Unipolar` |
| **默认值：** `Bipolar` |

### **参考电压 (V)** — 参考电压 `2`（默认）| real scalar

DAC 的参考电压，指定为 real scalar，单位为 V。**参考电压 (V)** 使用以下方程帮助根据输入数字代码、**位数**和**偏置 (V)** 确定输出：

DAC output = ((Digital input code / 2^(Number of bits)) × Reference) + Bias。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型：** character vector |
| **值：** real scalar |
| **默认值：** `2` |

**数据类型：** `double`

### **偏置 (V)** — 添加到输出的偏置电压 `0`（默认）| real scalar

添加到 DAC 输出的偏置电压，指定为 real scalar，单位为 V。**偏置 (V)** 使用以下方程帮助根据输入数字代码、**位数**和**参考电压 (V)** 确定输出：

DAC output = ((Digital input code / 2^(Number of bits)) × Reference) + Bias。

#### 编程使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** character vector |
| **值：** real scalar |
| **默认值：** `0` |

**数据类型：** `double`

### **建立时间 (s)** — 输出稳定所需时间 `3e-7`（默认）| nonnegative real scalar

DAC 输出稳定到其最终值某一比例范围内所需的时间，指定为 nonnegative real scalar，单位为 s。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** character vector |
| **值：** real scalar |
| **默认值：** `3e-7` |

**数据类型：** `double`

### **保持关闭时间 (s)** — 测量分析前的延迟 `1e-3`（默认）| nonnegative real scalar

为避免瞬态造成破坏而在测量分析之前引入的延迟，指定为 nonnegative real scalar，单位为 s。

#### 编程使用

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** character vector |
| **值：** nonnegative real scalar |
| **默认值：** `1e-3` |

**数据类型：** `double`

### **位数** — 输入字中的位数 `10`（默认）| positive real integer

输入字中的位数，指定为无单位的 positive real integer。**位数**确定 DAC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型：** character vector |
| **值：** positive real integer |
| **默认值：** `10` |

**数据类型：** `double`

### **启动转换频率 (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| positive real scalar

内部启动转换时钟的频率，指定为 real scalar，单位为 Hz。**启动转换频率**参数确定启动转换时的转换速率。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `1e6` |

**数据类型：** `double`

### **推荐的仿真停止时间 (s)** — 仿真必须运行以获得有意义结果的最短时间 `0.02148`（默认）| positive real scalar

仿真必须运行以获得有意义结果的最短时间，指定为 positive real scalar，单位为 s。

要测量直流性能，仿真必须运行到 DAC 可以对每个数字代码采样 20 次。基于此假设，**推荐的仿真停止时间 (s)** *T* 由以下公式给出：

T = Samples per bit / (StartFreq / 2^(Nbits+1)) + Hold off time,

其中 *StartFreq* 是转换启动时钟的频率，*Nbits* 是 DAC 的分辨率。

每位的采样数使用以下方程计算：

Samples per bit = max(1 / Error tolerance, 10)。

此参数仅由模块报告，不可编辑。

**数据类型：** `double`

### **端点** — 使用端点法测量 DNL、INL on（默认）| off

使用端点法测量微分非线性 (DNL) 误差和积分非线性 (INL) 误差。此方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

### **最佳拟合** — 使用最佳拟合方法测量 DNL、INL on（默认）| off

使用最佳拟合方法测量微分非线性 (DNL) 误差和积分非线性 (INL) 误差。此方法使用标准曲线拟合技术来找到最佳拟合，以测量 DNL 和 INL 误差。

### **将结果输出到基础工作区** — 将详细测试结果存储到基础工作区 off（默认）| on

选择此项可在仿真结束时将详细测试结果存储到基础工作区中的 `struct` 中，以供进一步处理。默认情况下，此参数未选中。

### **工作区变量名称** — 存储详细测试结果的变量名称 `dac_dc_out`（默认）| character string

存储详细测试结果的变量名称，指定为 character string。

#### 依赖关系

要启用此参数，请选择**将结果输出到基础工作区**参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型：** character vector |
| **值：** character string |
| **默认值：** `dac_dc_out` |

### **绘图** — 绘制测量结果的按钮

单击以绘制测量结果，供进一步分析。

## 所属库

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量 DAC 输出的直流性能指标

DAC DC Measurement 模块测量 DAC 直流性能指标，例如失调误差、增益误差、积分非线性 (INL) 和微分非线性 (DNL) 误差。您可以使用 DAC DC Measurement 模块验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以使用自己实现的 DAC。
