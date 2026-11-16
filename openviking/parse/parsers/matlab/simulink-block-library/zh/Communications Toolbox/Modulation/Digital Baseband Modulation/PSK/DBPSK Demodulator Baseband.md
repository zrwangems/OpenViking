---
type: simulink-block
title: 'DBPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'dbpskdemodulatorbaseband'
documentation_source_path: 'ref/dbpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DBPSK Demodulator Baseband

## 端口

### 输入

### **In** — DBPSK 调制基带信号，标量 | 列向量

DBPSK 调制基带信号，指定为复值标量或向量。有关详细信息，请参阅 Supported Data Types。

此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **Var** — 噪声方差，正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

#### 依赖关系

要启用此输入，请将 `Noise variance source` 设置为 `Input port`。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出信号，标量 | 列向量

输出信号，返回为标量或列向量，其元素值为 `0` 或 `1`。

此端口在模块上未命名。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Phase rotation (rad)** — 附加相移 `0`（默认）| 标量

前一个和当前调制符号之间的附加相移，以弧度为单位，指定为标量。当输入为零时，此值对应于前一个和当前调制符号之间的相位差。

**示例：** `pi/4`

### **Decision type** — 解调判决方法 `Hard decision`（默认）| `Approximate log-likelihood ratio`

*自 R2024b 起*

解调判决方法，指定为 `Hard decision` 或 `Approximate log-likelihood ratio`。当设置为 `Hard decision` 时，解调器输出位值的列向量。当设置为 `Approximate log-likelihood ratio` 时，解调器为 0 生成正值，为 1 生成负值。

### **Noise variance source** — 噪声方差的来源 `Property`（默认）| `Input port`

*自 R2024b 起*

噪声方差的来源，指定为 `Property` 或 `Input port`。

#### 依赖关系

要启用此参数，请将 `Decision type` 参数设置为 `Approximate log-likelihood ratio`。

### **Noise variance** — 噪声的方差 `1`（默认）| 非负标量

*自 R2024b 起*

噪声的方差，指定为非负标量。

#### 依赖关系

要启用此参数，请将 `Noise variance source` 参数设置为 `Property`。

### **Output data type** — 输出数据类型 `Inherit via internal`（默认）| `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输出数据类型，指定为 `Inherit via internal`、`Smallest unsigned integer`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

将此参数设置为 `Inherit via internal rule` 会根据输入端口设置输出数据类型。如果输入类型为 `single` 或 `double`，则输出数据类型与输入数据类型相同。

当将 `Decision type` 参数设置为 `Approximate log-likelihood ratio` 时，输出数据类型与输入数据类型匹配。输入数据类型必须为 double 或 single。

有关详细信息，请参阅 Supported Data Types。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

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

### R2024b：包含对软判决解调的支持

DBPSK Demodulator Baseband 模块现在支持以下功能。

- 使用 `Decision type` 参数将解调的判决类型指定为 `Approximate log-likelihood ratio`。
- 分别使用 `Noise variance source` 和 `Noise variance` 参数指定噪声方差的来源及其值。

## 描述

解调 DBPSK 调制数据

DBPSK Demodulator Baseband 模块解调使用差分二进制相移键控 (DBPSK) 方法调制的信号。输入是调制信号的基带表示。有关详细信息，请参阅 Algorithms。
