---
type: simulink-block
title: 'Digital Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Design and Analysis / Filter Design / Filter Design and Visualization Tools'
documentation_page: 'digitalfilterdesign'
documentation_source_path: 'ref/digitalfilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Filter Design

## 端口

### 输入

### **Port\_1** — 输入信号向量 | 矩阵

要滤波的信号，指定为实数值向量或矩阵。当给定矩阵输入时，该模块将每一列视为独立通道。

你在滤波器设计器应用中指定的采样率 `Fs` 必须与 Digital Filter Design 模块输入的采样率相同。当采样频率不匹配时，Digital Filter Design 模块会返回警告消息，并继承输入模块的采样率。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号向量 | 矩阵

滤波后的信号，以实数值向量或矩阵形式返回。

**数据类型：** `single` | `double`

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Filtering / Filter Designs

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

**使用 Intel AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

在以下条件下，Digital Filter Design 模块支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **Input processing** 设置为 `Columns as channels (frame based)`。
- **Filter Structure**（在 **Import Filter from Workspace** 窗格中）设置为 `Direct-Form FIR`。即使滤波器是 `Direct-Form FIR Transposed` 滤波器，也可以生成 SIMD 代码。要创建 `Direct-Form FIR Transposed` 滤波器，请选择 **Edit** > **Convert Structure**，并点击 **Direct-Form FIR Transposed**。
- 输入信号的数据类型为 `single` 或 `double`。

**通过利用目标硬件指令集扩展生成 SIMD 代码**

**注意**

需要 Simulink® Coder™ 或 Embedded Coder 许可证

在以下条件下，你可以通过使用模型配置参数 **Leverage target hardware instruction set extensions**，为所有 Intel® 平台、ARM® Cortex®-A 处理器和 Apple silicon 处理器上的 Digital Filter Design 模块生成 SIMD 代码：

- **Input processing** 设置为 `Columns as channels (frame based)`。
- **Filter Structure**（在 **Import Filter from Workspace** 窗格中）设置为 `Direct-Form FIR`。
- 输入信号的数据类型为 `single`（ARM Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或 `double`（Intel 平台）

SIMD 技术显著提高生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅：

- 使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码
- 使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（Intel 平台）
- 使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（Apple silicon）
- 使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（ARM Cortex-A 处理器）

## 版本历史

**R2006a 之前推出**

### R2024b：为 Apple silicon 处理器生成 SIMD 代码

在 R2024b 中，如果你有 Embedded Coder，则可以通过使用模型配置参数 **Leverage target hardware instruction set extensions**，为 Apple silicon 处理器生成 Digital Filter Design 模块的 SIMD 代码。有关详细信息，请参阅使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（Apple silicon）。

## 描述

设计并实现数字 FIR 和 IIR 滤波器

使用此模块设计、分析并高效实现浮点滤波器。

Digital Filter Design 模块实现你使用 Filter Designer (`filterDesigner`) 应用设计的数字有限脉冲响应 (FIR) 或无限脉冲响应 (IIR) 滤波器。此模块提供与 Discrete FIR Filter 或 Biquad Filter 模块相同的滤波器实现。

你必须通过设置 **Input processing** 参数来指定模块对输入执行基于帧还是基于采样的处理。该模块将指定滤波器应用于离散时间输入信号的每个通道并输出结果。该模块的输出在数值上与 Discrete FIR Filter 或 Biquad Filter 模块以及 MATLAB® `filter` 函数的输出匹配。有关详细信息，请参阅 Getting Started with Filter Designer。

Discrete FIR Filter (Simulink) 和 Biquad Filter 模块也实现数字滤波器，但用途略有不同。使用这些模块高效实现你已设计好的浮点或定点滤波器。这些模块提供与 Digital Filter Design 模块完全相同的滤波器实现。
