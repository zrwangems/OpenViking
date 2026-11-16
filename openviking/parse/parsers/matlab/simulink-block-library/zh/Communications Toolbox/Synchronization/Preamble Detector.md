---
type: simulink-block
title: 'Preamble Detector'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Synchronization'
documentation_page: 'preambledetector'
documentation_source_path: 'ref/preambledetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Preamble Detector

## 端口

### 输入

### **In** — 输入数据 [ ] | 标量 | 列向量

符号或比特的输入数据，指定为标量、列向量，或者可以为空。输入数据可以包含多个数据包。此端口在模块上未命名。

**数据类型:** `single` | `double` | `Boolean` | `int8` | `uint8`
**复数支持:** Yes
### 输出

### **Idx** — 最后一个前导码符号的索引 [ ] | 标量 | 列向量

最后一个前导码符号的索引，返回为标量或列向量，或者为与输入数据具有相同数据类型的空值。

- 当 **Detections** 参数设置为 `All` 时，`Idx` 输出对应于每个检测到的前导码最后一个元素的索引。
- 当 **Detections** 参数设置为 `First` 时，`Idx` 输出对应于第一个检测到的前导码最后一个元素的索引。

在启用 `DtMt` 端口之前，此端口未命名。

### **DtMt** — 检测度量 标量 | 列向量

检测度量，返回为与输入数据包 `In` 具有相同维度和数据类型的标量或列向量。

- 如果前导码或输入数据中任一者为复数，则检测度量为前导码与输入数据的互相关的绝对值。
- 如果前导码和输入数据均为实数，则检测度量为前导码与输入数据的互相关。

#### 依赖关系

要启用此端口，请将 **Input** 参数设置为 `Symbol`，并选择 **Output detection metric** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **Input** — 输入类型 `Symbol`（默认）| `Bit`

输入类型，指定为 `Symbol` 或 `Bit`。

- 对于二进制输入，请将此参数设置为 `Bit`。
- 对于所有其他输入，请将此参数设置为 `Symbol`。

有关执行速度的信息，请参阅提示。

### **Preamble** — 前导码序列 `[1 + 1i; 1 - 1i]`（默认）| 列向量

前导码序列，指定为列向量。

- 如果 **Input** 参数设置为 `Bit`，则前导码必须为二进制。
- 如果 **Input** 参数设置为 `Symbol`，则前导码可以是任意实数或复数序列。

### **Detection threshold** — 检测阈值 `3`（默认）| 非负标量

检测阈值，指定为非负标量。当检测度量大于或等于阈值时，模块会检测到前导码并更新 `Idx`。

**可调:** Yes

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `Symbol`。

### **Output detection metric** — 输出检测度量的选项 `off`（默认）| `on`

选择此参数可输出检测度量并启用 `DtMt` 输出端口。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `Symbol`。

### **Detections** — 返回的检测 `All`（默认）| `First`

返回的检测，指定为 `All` 或 `First`。指定 `All` 返回所有检测到的前导码。指定 `First` 仅返回第一个检测到的前导码。

**可调:** Yes

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生更改，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。
- `Interpreted execution` — 通过使用 MATLAB® 解释器来仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Synchronization

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

检测数据包中的前导码

Preamble Detector 模块检测数据包中前导码的末尾。前导码是一组符号或比特，用于基于数据包的通信系统中指示数据包的开始。数据包由前导码数据和用户数据组成。在仿真运行期间，数据包中用户数据部分的长度可以变化。

此图标展示了启用所有端口时的模块：
