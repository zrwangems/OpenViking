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

### **digital** — 来自 DAC 的数字输入信号 标量

来自 DAC 的数字信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **analog** — 来自 DAC 的转换后模拟信号 标量

来自 DAC 的转换后模拟信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟 标量

用于启动转换的外部时钟，指定为标量。此端口决定数模转换过程何时开始。

**数据类型：** `double`

## 参数

### **Input polarity** — DAC 输入信号的极性 `Bipolar`（默认）| `Unipolar`

DAC 输入信号的极性。

#### 编程使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型：** 字符向量 |
| **值：** `Bipolar`|`Unipolar` |
| **默认：** `Bipolar` |

### **Reference (V)** — 参考电压 `2`（默认）| 实数标量

DAC 的参考电压，以伏特为单位指定为实数标量。**Reference (V)** 有助于根据输入数字码、**Number of bits** 和 **Bias (V)** 使用以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `2` |

**数据类型：** `double`

### **Bias (V)** — 添加到输出的偏置电压 `0`（默认）| 实数标量

添加到 DAC 输出的偏置电压，以伏特为单位指定为实数标量。**Bias (V)** 有助于根据输入数字码、**Number of bits** 和 **Reference (V)** 使用以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置。

#### 编程使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **Settling time (s)** — 输出稳定所需时间 `3e-7`（默认）| 非负实数标量

DAC 输出稳定到其最终值某一比例范围内所需的时间，以秒为单位指定为非负实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `3e-7` |

**数据类型：** `double`

### **Hold off time (s)** — 测量分析前的延迟 `1e-3`（默认）| 非负实数标量

测量分析前的延迟，以避免瞬态造成的干扰，以秒为单位指定为非负实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `1e-3` |

**数据类型：** `double`

### **Number of bits** — 输入字中的位数 `10`（默认）| 正实数整数

输入字中的位数，指定为无单位的正实数整数。**Number of bits** 决定 DAC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型：** 字符向量 |
| **值：** 正实数整数 |
| **默认：** `10` |

**数据类型：** `double`

### **Start conversion frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，以 Hz 为单位指定为实数标量。**Start conversion frequency** 参数决定启动转换时的转换速率。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1e6` |

**数据类型：** `double`

### **Recommended simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `0.02148`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

要测量直流性能，仿真必须运行到 DAC 能够对每个数字码采样 20 次。基于此假设，**Recommended simulation stop time (s)** *T* 由下式给出：

T=Samples per bit(StartFreq/2Nbits+1)+Hold off time，

其中 *StartFreq* 是转换启动时钟的频率，*Nbits* 是 DAC 的分辨率。

每比特采样数使用以下公式计算：

Samples per bit = max(1Error tolerance,10)。

此参数仅由模块报告，不可编辑。

**Data Types:** `double`

### **Endpoint** — 使用端点法测量 DNL、INL on（默认）| off

使用端点法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

### **Best fit** — 使用最佳拟合方法测量 DNL、INL on（默认）| off

使用最佳拟合方法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用标准曲线拟合技术来找到最佳拟合，以测量 DNL 和 INL 误差。

### **Output result to base workspace** — 将详细测试结果存储到基础工作区 off（默认）| on

选择此项可在仿真结束时将详细测试结果存储到基础工作区中的 `struct`，以便进一步处理。默认情况下，此参数未选中。

### **Workspace variable name** — 存储详细测试结果的变量名称 `dac_dc_out`（默认）| 字符字符串

存储详细测试结果的变量名称，指定为字符字符串。

#### 依赖关系

要启用此参数，请选择 **Output result to base workspace** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型**：character vector |
| **值**：character string |
| **默认值**：`dac_dc_out` |

### **Plot** — 绘制测量结果 button

点击以绘制测量结果以供进一步分析。

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

DAC DC Measurement 模块测量 DAC 直流性能指标，例如失调误差、增益误差、积分非线性（INL）和微分非线性（DNL）误差。您可以使用 DAC DC Measurement 模块验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以使用您自己实现的 DAC。
