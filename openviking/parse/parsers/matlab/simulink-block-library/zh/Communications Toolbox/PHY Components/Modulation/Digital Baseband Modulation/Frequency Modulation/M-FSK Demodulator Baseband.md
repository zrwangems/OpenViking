---
type: simulink-block
title: 'M-FSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Frequency Modulation'
documentation_page: 'mfskdemodulatorbaseband'
documentation_source_path: 'ref/mfskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-FSK Demodulator Baseband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。输入是调制信号的基带表示。

此端口在模块上未命名。

**数据类型:** `double`
### 输出

### **Out** — 解调输出信号标量 | 列向量

解调输出信号，以标量或列向量形式返回。有关详细信息，请参阅单速率处理和多速率处理。**Output type** 参数指定模块输出整数还是比特组。

此端口在模块上未命名。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **M-ary number** — 调制信号中的频率数 `8` (default) | 正整数 ≥ 2

调制信号中的频率数，指定为 ≥ 2 的正整数。

### **Output type** — 输出整数或比特组的指示符 `Integer` (default) | `Bit`

指示模块输出整数还是比特组，指定为 `Integer` 或 `Bit`。

如果将此参数设置为 `Bit`，则 **M-ary number** 参数必须为 2*K*，其中 *K* 为某正整数。

### **Symbol set ordering** — 符号映射 `Binary` (default) | `Gray`

输出符号的符号映射，指定为 `Binary` 或 `Gray`。

- 将此参数设置为 `Binary`，以使用二进制编码顺序映射符号。
- 将此参数设置为 `Gray`，以使用格雷编码顺序映射符号。对于格雷编码顺序，**M-ary number** 值必须为 2 的幂。

有关详细信息，请参阅整数值信号和二进制值信号。

### **Frequency separation (Hz)** — 以 Hz 为单位的频率间隔 `6` (default) | 正标量

以 Hz 为单位的频率间隔，指定为正标量，表示调制信号中相邻频率之间的距离。

### **Samples per symbol** — 符号采样率 `17` (default) | 正整数

符号采样率，指定为正整数，表示每个调制符号所对应的输入样本数。

有关详细信息，请参阅信号上采样和速率变化。

### **Rate options** — 模块处理速率 `Enforce single-rate processing` (default) | `Allow multirate processing`

模块处理速率，指定为以下选项之一：

- `Enforce single-rate processing` — 输入和输出信号具有相同的端口采样时间。该模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度为符号数（当 **Output type** 参数设置为 `Integer` 时，该值由输入长度除以 **Samples per symbol** 参数值得到）。
- `Allow multirate processing` — 输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，并等于输入周期与 **Samples per symbol** 参数值的乘积。

### **Output data type** — 输出数据类型 `double` (default) | `boolean` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

输出数据类型，指定为 `double`、`boolean`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`。

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

解调 FSK 调制数据

M-FSK Demodulator Baseband 模块解调使用 M 进制频移键控 (M-FSK) 方法调制的信号。输入和输出为离散时间信号。
