---
type: simulink-block
title: 'M-FSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Frequency Modulation'
documentation_page: 'mfskmodulatorbaseband'
documentation_source_path: 'ref/mfskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-FSK Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 行向量

输入信号，指定为标量或列向量。有关详细信息，请参阅 **Input type**。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — M-FSK 调制信号 标量 | 列向量

M-FSK 调制信号，以复符号的标量或列向量形式返回。有关详细信息，请参阅单速率处理和多速率处理。

输出是调制信号的基带表示。**Output data type** 参数指定所需的输出数据类型。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **M-ary number** — 调制信号中的频率数量 `8`（默认值）| 正整数 ≥ 2

调制信号中的频率数量，指定为 ≥ 2 的正整数。

### **Input type** — 整数或位组输入指示符 `Integer`（默认值）| `Bit`

指示输入由整数还是位组组成，指定为 `Integer` 或 `Bit`。

如果将此参数设置为 `Bit`，则 **M-ary number** 参数必须为 2*K*，其中 *K* 为某个正整数。

### **Symbol set ordering** — 符号映射 `Binary`（默认值）| `Gray`

输入符号的符号映射，指定为 `Binary` 或 `Gray`。

- 将此参数设置为 `Binary`，以使用二进制编码顺序映射符号。
- 将此参数设置为 `Gray`，以使用格雷编码顺序映射符号。对于格雷编码顺序，**M-ary number** 值必须是 2 的幂。

有关详细信息，请参阅整数值信号和二值信号。

### **Frequency separation (Hz)** — 以 Hz 为单位的频率间隔 `6`（默认值）| 正标量

以 Hz 为单位的频率间隔，指定为正标量，表示调制信号中相邻频率之间的距离。

### **Phase continuity** — 相位连续性 `Continuous`（默认值）| `Discontinuous`

相位连续性，指定为 `Continuous` 或 `Discontinuous`，用于确定调制信号是以连续还是不连续方式改变相位。

- 如果将此参数设置为 `Continuous`，则调制信号即使改变频率也保持其相位。
- 如果将此参数设置为 `Discontinuous`，则调制信号由不同频率的 *M* 个正弦波部分组成。输入值的变化有时会导致调制信号相位的变化。*M* 是 **M-ary number** 参数值。

### **Samples per symbol** — 符号采样率 `17`（默认值）| 正整数

符号采样率，指定为正整数，表示模块为输入中的每个整数或二进制字生成的输出样本数。

有关详细信息，请参阅信号上采样和速率变化。

### **Rate options** — 模块处理速率 `Enforce single-rate processing`（默认值）| `Allow multirate processing`

模块处理速率，指定为以下选项之一：

- `Enforce single-rate processing` — 输入和输出信号具有相同的采样时间。模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。
- `Allow multirate processing` — 输入和输出信号具有不同的采样时间。输出采样时间等于符号周期除以 **Samples per symbol** 参数值。

### **Output data type** — 输出数据类型 `double`（默认值）| `single`

输出数据类型，指定为 `double` 或 `single`。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / FM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 M 进制频移键控方法进行调制

M-FSK Modulator Baseband 模块使用 M 进制频移键控 (M-FSK) 方法对信号进行调制。

为防止输出信号中出现混叠，请将采样频率设置为大于 **M-ary number** 与 **Frequency separation (Hz)** 参数值的乘积的值。采样频率是 **Samples per symbol** 参数值除以模型中定义的输入符号周期（以秒为单位）。
