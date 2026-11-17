---
type: simulink-block
title: 'BPSK Demodulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'bpskdemodulatorbaseband'
documentation_source_path: '../comm/ref/bpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# BPSK Demodulator Baseband

## 端口
```yaml
ports:
- name: In
  summary: BPSK 调制基带信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double | single | fixed point
- name: Var
  summary: 噪声方差 正标量 | 正值向量
  direction: input
  data_types: double
- name: Out
  summary: 解调信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### 输入

### **In** — BPSK 调制基带信号 标量 | 向量 | 矩阵

BPSK 调制基带信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列被视为一个独立通道。在启用 `Var` 端口之前，此端口未命名。当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅 BPSK 软解调以了解解调判决类型的注意事项。

**数据类型：** `double` | `single` | `fixed point`
**复数支持：** 是

### **Var** — 噪声方差 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅 BPSK 软解调以了解解调判决类型的注意事项。

#### 依赖关系

要启用此参数，请将 **噪声方差来源** 参数设置为 `Port`。

**数据类型：** `double`
### 输出

### **Out** — 解调信号 标量 | 向量

解调信号，以标量或向量形式返回。如果输出为标量，则该值为整数。如果输出为向量，则其为整数值或二值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## 参数
```yaml
parameters:
- name: 判决类型
  summary: 判决类型 硬判决（默认）| 对数似然比 | 近似对数似然比
  group: 主要
- name: 噪声方差来源
  summary: 噪声方差来源 对话框（默认）| 端口
  group: 主要
- name: 噪声方差
  summary: 噪声方差 1（默认）| 正标量 | 正值向量
  group: 主要
- name: 相位偏移 (rad)
  summary: 零点相位 0（默认）| 实值标量
  group: 主要
- name: 输出数据类型
  summary: 输出数据类型 通过内部规则继承（默认）| 最小无符号整数 | double | single | ...
  group: 数据类型
- name: 去旋转因子
  summary: 去旋转因子 与输入相同的字长（默认）| 指定字长
  group: 数据类型
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡中，在 **准备** 库中选择 **属性检查器**。

### 主要

### **判决类型** — 判决类型 `硬判决`（默认）| `对数似然比` | `近似对数似然比`

解调期间使用的判决类型，指定为 `硬判决`、`对数似然比` 或 `近似对数似然比`。有关详细信息，请参阅 BPSK 硬判决解调和 BPSK 软解调。

当 **判决类型** 设置为 `对数似然比` 或 `近似对数似然比` 时，输出与输入值的数据类型匹配。

### **噪声方差来源** — 噪声方差来源 `对话框`（默认）| `端口`

噪声方差来源，指定为 `对话框` 或 `端口`。

- `对话框` — 使用 `噪声方差` 参数设置噪声方差。
- `端口` — 使用 `Var` 输入端口设置噪声方差。

### **噪声方差** — 噪声方差 `1`（默认）| 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

- 当指定为标量时，该值应用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号的列数。每个噪声方差向量元素应用于输入信号中对应的列。

当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅 BPSK 软解调以了解解调判决类型的注意事项。

此参数在普通模式、加速模式和快速加速模式下可调。如果您使用 Simulink Coder™ 快速仿真 (RSIM) 目标来构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。这对于蒙特卡洛仿真非常有用，在此类仿真中，您需要以不同的噪声量多次运行仿真（可能在多台计算机上）。

**可调：** 是

#### 依赖关系

要启用此参数，请将 `判决类型` 参数设置为 `对数似然比` 或 `近似对数似然比`，并将 **噪声方差来源** 参数设置为 `对话框`。

### **相位偏移 (rad)** — 零点相位 `0`（默认）| 实值标量

零点相位，指定为实值标量。单位为弧度。

**示例：** `pi/4`

### 数据类型

### **输出数据类型** — 输出数据类型 `通过内部规则继承`（默认）| `最小无符号整数` | `double` | `single` | ...

输出数据类型，指定为以下选项之一

- 当您将 **判决类型** 参数设置为 **硬判决** 时：

  - `通过内部规则继承` — 模块从输入端口继承输出数据类型。如果输入为浮点类型（`single` 或 `double`），则输出数据类型与输入数据类型相同。如果输入数据类型为定点，则输出数据类型的工作方式如同您将此参数设置为 `最小无符号整数`。
  - `最小无符号整数` — 模块根据模型配置参数对话框中 **硬件实现** 窗格所使用的设置来选择输出数据类型。如果您在 **硬件实现** 窗格中选择 `ASIC/FPGA`，则输出数据类型为理想的最小一位大小，即 `ufix(1)`。对于所有其他选择，输出数据类型为具有足够容纳一位的最小可用字长的无符号整数，通常对应于字符的大小（例如 `uint8`）。
  - `double`
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `boolean`
- 当您将 **判决类型** 参数设置为 **对数似然比** 或 **近似对数似然比** 时 — 模块继承的输出数据类型与输入的数据类型匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **去旋转因子** — 去旋转因子 `与输入相同的字长`（默认）| `指定字长`

去旋转因子，指定为 `与输入相同的字长` 或 `指定字长`。

#### 依赖关系

此参数仅在输入为定点且 **相位偏移 (rad)** 参数不是 π/2 的倍数时适用。
## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 定点输入必须为有符号。  b 仅当在硬件实现窗格中选择 ASIC/FPGA 时，输出才为 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 BPSK 调制数据

BPSK Demodulator Baseband 模块解调使用二进制相移键控 (BPSK) 方法调制的信号。输入是调制信号的基带表示。此模块接受标量或列向量输入信号。输入信号必须是离散时间复信号。该模块将点 exp(jϕ) 或 -exp(jϕ) 分别映射为 0 和 1。`相位偏移 (rad)` 参数指定 ϕ 的值。
