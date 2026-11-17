---
type: simulink-block
title: 'Segmented DAC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Architectures'
documentation_page: 'segmenteddac'
documentation_source_path: 'ref/segmenteddac.html'
language: zh-CN
chinese_source: worker-translation
---

# Segmented DAC

## 端口

### 输入

### **digital** — 数字输入信号 整数

DAC 的数字输入信号，指定为整数。

如果 **Input polarity** 参数设置为 `Bipolar`，信号的允许范围为 [−2*NBits*-1, 2*NBits*-1]。

如果 **Input polarity** 参数设置为 `Unipolar`，信号的允许范围为 [0, 2*NBits*-1]。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **start** — 用于启动转换的外部时钟 标量

用于启动转换的外部时钟，指定为标量。数字到模拟转换过程在 **start** 端口信号的上升沿开始。

#### 依赖关系

要启用此端口，请选择 **Use external start clock**。

**数据类型：** `double`

### 输出

### **analog** — 转换后的模拟输出信号 标量

转换后的模拟输出信号，以标量形式返回。

**数据类型：** `double`

## 参数

### **Input polarity** — 定义 DAC 输入数据极性 `Unipolar`（默认）| `Bipolar`

定义 DAC 输入数据的极性。将 **Input polarity** 设置为：

- `Unipolar`，当数字输入只能为正时。
- `Bipolar`，当数字输入既可以为正也可以为负时。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型：** 字符向量 |
| **值：** `Unipolar` | `Bipolar` |
| **默认：** `Unipolar` |

### **Use external start clock** — 连接到外部启动转换时钟 on（默认）| off

选择此项以连接到外部启动转换时钟。默认情况下选中此选项。如果取消选择此选项，则使用 Segmented DAC 模块内部的 Sampling Clock Source 模块来生成启动转换时钟。

### **Conversion start frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 实数标量

内部启动转换时钟的频率，以 Hz 为单位的实数标量指定。**Conversion start frequency** 参数决定转换开始时的转换速率。

#### 依赖关系

要启用此参数，请取消选择 **Use external start clock**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `1e6` |

### **Reference (V)** — DAC 输出参考幅度 `0.5`（默认）| 实数标量

DAC 输出的参考幅度，以伏特为单位的实数标量指定。**Reference (V)** 比最大可达到的输出大一个最低有效位（LSB）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0.5` |

### **Bias (V)** — 代码零的模拟输出与模拟零之间的差值 `0`（默认）| 实数标量

在无损伤 DAC 中，代码零的模拟输出与模拟零之间的差值，以伏特为单位的实数标量指定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

### **Settling time (s)** — 输出稳定所需的时间 `2e-7`（默认）| 非负实数标量

DAC 输出稳定到其最终值的某一分数范围内所需的时间，以秒为非负实数标量指定。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `2e-7` |

### **Settling time tolerance (LSB)** — 计算稳定时间的容差 `0.5`（默认）| 正实数标量

计算稳定时间所允许的容差，以 LSB 为正实数标量指定。DAC 的输出必须在 **Settling time (s)** 之前稳定在 **Settling time tolerance (LSB)** 范围内。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `0.5` |

#### 段设置

### **位宽** — DAC 段的物理输入位数，大于或等于 2 的整数标量

DAC 段的物理输入位数，指定为大于或等于 2 的整数标量。对于前两个 DAC 段，**位宽**的默认值为 `4`。对于后续段，默认值为 `2`。

### **位** — 每个段的位范围，向量

每个段的位范围，以向量形式返回。如果通过上移或下移来更改任何段的索引，该段的位范围会相应更改。此参数为只读。

### **拓扑** — 基础 DAC 段的拓扑，`Binary Weighted`（默认）

该段的基础 DAC 的拓扑。该模块使用 `Binary Weighted` DAC。此参数为只读。

### **偏移误差** — 平移量化步长，`0`（默认）| 实数标量

按您在**偏移误差**参数中提供的值平移量化步长，指定为实数标量。

### **偏移误差单位** — 偏移误差的单位，`LSB`（默认）| `FS` | `%FS`

偏移误差的单位，指定为 `LSB`、满量程（`FS`）或满量程百分比（`%FS`）。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码的宽度为 0.5 LSB，而最后一个码的宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器的满量程范围2N位。

### **增益误差** — DAC 传输曲线斜率的误差，`0`（默认）| 实数标量

DAC 传输曲线斜率的误差，指定为实数标量。

### **增益误差单位** — 增益误差的单位，`LSB`（默认）| `FS` | `%FS`

增益误差的单位，指定为 `LSB`、满量程（`FS`）或满量程百分比（`%FS`）。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码的宽度为 0.5 LSB，而最后一个码的宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器的满量程范围2N位。

### **上移所选段** — 将所选段上移一行，按钮

点击将所选段上移一行。

### **下移所选段** — 将所选段下移一行，按钮

点击将所选段下移一行。

### **新建段** — 添加新 DAC 段，按钮

点击以默认值添加新的 DAC 段。目前，您最多可以向 Segmented DAC 模块添加五个 DAC 段。

### **复制所选** — 复制所选段，按钮

点击通过复制所选段来添加新的 DAC 段。目前，您最多可以向 Segmented DAC 模块添加五个段。

### **删除所选** — 删除所选段，按钮

点击从 Segmented DAC 模块中删除所选 DAC 段。

## 所属库

Mixed-Signal Blockset / DAC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

使用较小 DAC 的排列将大数字输入转换为模拟信号

Segmented DAC 模块通过将大数字信号拆分到多个较小的 DAC 上来将其转换为模拟输出。Segmented DAC 模块最多支持五个二进制加权分段 DAC。
