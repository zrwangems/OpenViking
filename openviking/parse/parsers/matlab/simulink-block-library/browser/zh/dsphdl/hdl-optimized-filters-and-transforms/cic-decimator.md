---
type: simulink-block
title: 'CIC Decimator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'cicdecimator'
documentation_source_path: 'ref/cicdecimator.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Decimator

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为标量或长度为 1 到 64 的列向量。输入数据必须是有符号整数或有符号定点，其字长小于或等于 32。**Decimation factor (R)** 参数必须是输入帧大小的整数倍。

处理输入数据时，模块实现舍入方法 `Floor` 和溢出操作 `Wrap`。有关详细信息，请参阅舍入模式和溢出处理。

**数据类型：** `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输入数据的标量

控制信号，用于指示输入数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0` (`false`) 时，模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **R** — 可变抽取率 标量

使用此端口在运行时动态指定可变抽取率。

此值的数据类型必须为 `fixdt(0,12,0)`，并且必须是范围从 1 到 **Decimation factor (Rmax)** 参数值的整数。

#### 依赖项

要启用此端口，请在 **主** 选项卡上将 **Decimation factor source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,12,0)`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1` (`true`) 时，模块停止当前计算并清除内部状态。当 **reset** 为 `0` (`false`) 且输入 **valid** 为 `1` (`true`) 时，模块捕获数据以进行处理。

有关复位的更多注意事项，请参阅硬件控制信号页面中的复位信号部分。

#### 依赖项

要启用此端口，请在 **控制端口** 选项卡上选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — CIC 抽取后的输出数据 标量 | 列向量

模块返回滤波后的输出数据，形式为标量或长度为 1 到 64 的列向量。您可以通过在 **数据类型** 选项卡上设置 **Output data type** 参数来定义此输出的数据类型。

**数据类型：** `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输出数据的标量

控制信号，用于指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0` (`false`) 时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

## 参数

### 主

### **Decimation factor source** — 抽取因子来源 `Property`（默认）| `Input port`

选择模块以固定还是可变抽取率运行。

- `Property` — 使用从 **Decimation factor (R)** 参数指定的固定抽取率。
- `Input port` — 使用从 **R** 输入端口指定的可变抽取率。

**注意**

对于向量输入，模块不支持可变抽取。

### **Decimation factor (R)** — 抽取因子 `2`（默认）| 从 1 到 2048 的整数

指定模块对输入进行抽取的抽取因子率。

#### 依赖项

要启用此参数，请将 **Decimation factor source** 参数设置为 `Property`。

### **Decimation factor (Rmax)** — 可变抽取因子的上界 `2`（默认）| 从 1 到 2048 的整数

指定 **R** 输入端口有效值范围的上界。

**注意**

对于向量输入，模块不支持可变抽取。

#### 依赖项

要启用此参数，请将 **Decimation factor source** 参数设置为 `Input port`。

### **Differential delay (M)** — 差分延迟 `1`（默认）| `2`

指定模块梳状部分的差分延迟。

### **Number of sections (N)** — 积分器和梳状部分的数量 `2`（默认）| `1` | `3` | `4` | `5` | `6`

指定模块梳状部分或积分器部分中的部分数量。

### **Gain correction** — 输出增益补偿 `off`（默认）| `on`

选择此参数以补偿模块的输出增益。

模块的延迟会因输入类型、您指定的抽取、部分数量以及此参数的值而变化。有关模块延迟的更多信息，请参阅延迟。

### 数据类型

### **Output data type** — 输出的数据类型 `Full precision`（默认）| `Same word length as input` | `Minimum section word lengths`

选择输出数据的数据类型。

- `Full precision` — 输出数据类型的字长等于输入字长加增益位。
- `Same word length as input` — 输出数据类型的字长等于输入字长。
- `Minimum section word lengths` — 输出数据类型使用您在 **Output word length** 参数中指定的字长。选择此选项时，模块会应用修剪算法。有关修剪算法的更多信息，请参阅 [1]。

### **Output word length** — 输出的字长 `16`（默认）| 从 2 到 104 的整数

指定输出的字长。

**注意**

当此值为 `2`、`3`、`4`、`5` 或 `6` 时，模块可能会使输出数据溢出。

#### 依赖项

要启用此参数，请将 **Output data type** 参数设置为 `Minimum section word lengths`。

### 控制端口

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。reset 信号实现对数据路径寄存器的本地同步复位。

有关复位的更多注意事项，请参阅提示。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认）| `on`

选择此参数以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观，也不会修改 Simulink 中的仿真行为。清除此参数时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步的，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关复位的更多注意事项，请参阅提示。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2019b 中引入**

### R2022a: 从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 CIC Decimation HDL Optimized，并包含在 DSP System Toolbox™ **DSP System Toolbox HDL Support** 库中。

### R2022a: 对抽取因子参数的更改

现在可以将抽取因子设置为 `1`。在以前的版本中，抽取因子 `1` 无效。

| 配置 | R2022a 之前 | 2022a 之后 |
| --- | --- | --- |
| 可变抽取因子 | 选择 **Variable decimation** 参数，并将 **Decimation factor (R)** 参数设置为最大预期抽取因子。 | 将 **Decimation factor source** 参数设置为 `Input port`，并将 **Decimation factor (Rmax)** 参数设置为最大预期抽取因子。**decimFactor** 端口已重命名为 **R**。 |
| 固定抽取因子 | 清除 **Variable decimation** 参数，并将 **Decimation factor (R)** 参数设置为所需抽取因子。 | 将 **Decimation factor source** 参数设置为 `Property`，并将 **Decimation factor (R)** 设置为所需抽取因子。 |

### R2021b: 高吞吐量接口

此模块接受并返回表示时间样本的元素的列向量。输入向量最多可包含 64 个样本。使用基于帧的输入时，必须使用固定抽取因子。

### R2020a: 增益校正和可编程抽取因子

您可以选择启用自动增益校正。您还可以将抽取因子指定为输入端口。

## 描述

使用 CIC 滤波器对信号进行抽取

CIC Decimator 模块通过使用级联积分器-梳状 (CIC) 抽取滤波器对输入信号进行抽取。CIC 抽取滤波器是一类线性相位有限脉冲响应 (FIR) 滤波器，由梳状部分和积分器部分组成。CIC 抽取滤波器结构由 *N* 个级联积分器部分、速率变化因子 *R* 以及 *N* 个级联梳状滤波器部分组成。有关 CIC 抽取滤波器的更多信息，请参阅算法。

此模块支持以下输入和输出数据组合。

- 标量输入和标量输出 — 支持固定和可变抽取率
- 向量输入和标量输出 — 仅支持固定抽取率
- 向量输入和向量输出 — 仅支持固定抽取率

此模块提供适合 HDL 代码生成和硬件部署的架构。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
