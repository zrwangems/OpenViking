---
type: simulink-block
title: 'ADC DC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'adcdcmeasurement'
documentation_source_path: 'ref/adcdcmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC DC Measurement

## 端口

### 输入

### **analog** — 输入到 ADC 的模拟输入信号 标量

输入到 ADC 模块的模拟输入信号，指定为标量。

**数据类型：** `double`

### **start** — 外部转换启动时钟 标量

外部转换启动时钟，指定为标量。模数转换过程在 **start** 端口信号的上升沿开始。

**数据类型：** `double`

### **digital** — 来自 ADC 的转换后数字信号 标量

来自 ADC 的转换后数字信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — 指示模数转换是否完成 标量

指示模数转换是否完成，指定为标量。

**数据类型：** `double`

## 参数

### **Input range (V)** — ADC 的动态范围 `[-1 1]`（默认）| 2 元素向量

ADC 的动态范围，指定为以 V 为单位的 2 元素向量。两个向量元素从左到右分别表示动态范围的最小值和最大值。

#### 编程使用

- 使用 `get_param(gcb,'InputRange')` 查看 **Input range** 的当前值。
- 使用 `set_param(gcb,'InputRange',value)` 将 **Input range** 设置为特定值。

### **Hold off time (s)** — 延迟测量分析以避免瞬态干扰 `0`（默认）| 非负实数标量

延迟测量分析以避免瞬态干扰，指定为以秒为单位的非负实数标量。

#### 编程使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **Hold off time** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **Hold off time** 设置为特定值。

### **Number of bits** — ADC 中的物理位数 `5`（默认）| 正实数整数

ADC 中的物理位数，指定为无单位的正实数整数。**Number of bits** 必须与 ADC 模块中指定的分辨率匹配。

#### 编程使用

- 使用 `get_param(gcb,'NBits')` 查看当前的 **Number of bits**。
- 使用 `set_param(gcb,'NBits',value)` 将 **Number of bits** 设置为特定值。

### **Start conversion frequency (Hz)** — ADC 启动转换时钟的频率 `10e6`（默认）| 正实数标量

ADC 启动转换时钟的频率，指定为以赫兹为单位的正实数标量。**Start conversion frequency** 必须与 ADC 模块的启动转换时钟频率匹配。此参数用于计算 **Recommended min. simulation stop time**。

#### 编程使用

- 使用 `get_param(gcb,'Frequency')` 查看 **Start conversion frequency** 的当前值。
- 使用 `set_param(gcb,'Frequency',value)` 将 **Start conversion frequency** 设置为特定值。

### **Recommended min. simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `3.2e-5`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

对于 DC 测量，仿真必须运行到 ADC 能够以默认误差容限 `0.1` 对每个数字码采样 10 次，假设在仿真周期内斜坡输入遍历 ADC 的满量程范围。基于此假设，由 ADC Testbench 模块为锯齿波形生成的模拟输入频率（*f*analog）设置为：

fanalog=StartFreq·ErrorTolerance2(Nbits+1)

其中 *StartFreq* 是转换启动时钟的频率，*Nbits* 是 ADC 的分辨率。

因此，**Recommended min. simulation stop time (s)**（*T*）使用以下公式计算：T=1fanalog+HoldOffTime。

**数据类型：** `double`

### **Set as model stop time** — 自动将推荐的最小仿真停止时间设置为模型停止时间按钮

点击以自动将 **Recommended min. simulation stop time (s)** 设置为 Simulink® 模型的停止时间。

### **Endpoint** — 使用端点法测量 DNL、INL on（默认）| off

使用端点法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

### **Best fit** — 使用最佳拟合方法测量 DNL、INL on（默认）| off

使用最佳拟合方法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用标准曲线拟合技术来寻找最佳拟合以测量 DNL 和 INL 误差。

### **Output result to base workspace** — 将详细测试结果存储到基础工作区 off（默认）| on

将详细测试结果存储到基础工作区中的 `struct` 中以供进一步处理。默认情况下，此选项未选中。

### **Workspace variable name** — 存储详细测试结果的变量名称 `adc_dc_out`（默认）| 字符字符串

存储详细测试结果的变量名称，指定为字符字符串。

#### 依赖关系

此参数仅在选中 **Output result to base workspace** 时可用

#### 编程使用

- 使用 `get_param(gcb,'VariableName')` 查看 **Workspace variable name** 的当前值。
- 使用 `set_param(gcb,'VariableName',value)` 将 **Workspace variable name** 设置为特定值。

### **Plot** — 绘制测量结果按钮

点击以绘制测量结果以供进一步分析。

## 所属库

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量 ADC 输出的直流性能指标

ADC DC Measurement 模块测量 ADC 直流性能指标，例如失调误差、增益误差、积分非线性（INL）和微分非线性（DNL）。您可以使用 ADC DC Measurement 模块来验证 Mixed-Signal Blockset™ 中提供的 ADC 架构模型，也可以使用您自己实现的 ADC。
