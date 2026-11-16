---
type: simulink-block
title: 'MIL-188 QAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'mil188qammodulatorbaseband'
documentation_source_path: 'ref/mil188qammodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# MIL-188 QAM Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。输入信号必须是二进制值或范围 [0, (*M* – 1)] 内的整数，其中 *M* 是 **调制阶数**。此端口在模块上未命名。

**注意**

要将输入信号作为二进制元素处理，请将 **输入类型** 参数值设置为 `Bit`。对于二进制输入，行数必须是 log2(*M*) 的整数倍。一列中每组 log2(*M*) 个比特映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Out** — 特定于 MIL-STD-188 标准的 QAM 调制信号 标量 | 向量 | 矩阵

特定于 MIL-STD-188 标准的 QAM 调制信号，返回为复标量、向量或矩阵。输出信号维度取决于指定的 **输入类型** 参数值。此端口在模块上未命名。

| **输入类型** | 输出信号维度 |
| --- | --- |
| `Integer` | 输出信号与输入信号具有相同的维度。 |
| `Bit` | 输出信号的行数等于输入信号的行数除以 log2(*M*)，其中 *M* 是 **调制阶数**。 |

使用 **输出数据类型** 指定输出数据类型。

**数据类型：** `double` | `single`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡中，从 **准备** 库中选择 **属性检查器**。

### **调制阶数** — 调制阶数 `16`（默认） | `32` | `64` | `256`

调制阶数 *M*，指定为 `16`、`32`、`64` 或 `256`。调制阶数指定输出信号星座图中的总点数。

### **星座图缩放** — 星座图缩放 `As specified in standard`（默认） | `Unit average power`

星座图缩放，指定为：

- `As specified in standard` – 模块根据相关标准 [1] 中的规范缩放星座图。
- `Unit average power` – 模块将星座图缩放到以 1 ohm 为参考的平均功率 1 watt。

### **输入类型** — 输入类型 `Integer`（默认） | `Bit`

输入类型，指定为 `Integer` 或 `Bit`。要使用 `Integer`，输入信号必须由范围 [0, (*M* – 1)] 内的整数组成。要使用 `Bit`，输入信号必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 **调制阶数**。

### **输出数据类型** — 输出数据类型 `double`（默认） | `single`

输出数据类型，指定为 `double` 或 `single`。

### **查看星座图** — 绘制参考星座图 `button`

要绘制参考星座图，请点击 **查看星座图** 按钮。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为：

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，并且仿真速度与 `Code generation` 相当。在 `Interpreted execution` 模式下，您可以调试模块的源代码。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox / Modulation / Digital Baseband Modulation / Standard-Compliant

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

MIL-STD-188-110 B/C 标准特定的正交幅度调制（QAM）

MIL-188 QAM Modulator Baseband 模块使用特定于 MIL-STD-188-110 标准的正交幅度调制（QAM）对输入信号进行调制。
