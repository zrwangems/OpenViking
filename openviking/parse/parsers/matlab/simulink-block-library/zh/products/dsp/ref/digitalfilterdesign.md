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

### **Port\_1** — 输入信号 向量 | 矩阵

要滤波的信号，指定为实值向量或矩阵。当输入为矩阵时，模块将每一列视为一个独立通道。

您在 filter designer App 中指定的采样率 `Fs` 必须与 Digital Filter Design 模块输入的采样率相同。当采样频率不匹配时，Digital Filter Design 模块会返回警告消息，并继承输入模块的采样率。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 向量 | 矩阵

滤波后的信号，以实值向量或矩阵形式返回。

**数据类型：** `single` | `double`

## 参数

### 对话框

有关此对话框中参数的详细信息，请参阅 Using Filter Designer。

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

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

**使用 Intel AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

在以下条件下，Digital Filter Design 模块支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **Input processing** 设置为 `Columns as channels (frame based)`。
- **Filter Structure**（位于 **Import Filter from Workspace** 窗格中）设置为 `Direct-Form FIR`。即使滤波器是 `Direct-Form FIR Transposed` 滤波器，您也可以生成 SIMD 代码。要创建 `Direct-Form FIR Transposed` 滤波器，请选择 **Edit** > **Convert Structure**，然后点击 **Direct-Form FIR Transposed**。
- 输入信号的数据类型为 `single` 或 `double`。

**利用目标硬件指令集扩展生成 SIMD 代码**

**注意**

需要 Simulink® Coder™ 或 Embedded Coder 许可证

在以下条件下，您可以使用模型配置参数 **Leverage target hardware instruction set extensions**，在所有 Intel® 平台、ARM® Cortex®-A 处理器和 Apple silicon 处理器上为 Digital Filter Design 模块生成 SIMD 代码：

- **Input processing** 设置为 `Columns as channels (frame based)`。
- **Filter Structure**（位于 **Import Filter from Workspace** 窗格中）设置为 `Direct-Form FIR`。
- 输入信号的数据类型为 `single`（ARM Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或 `double`（Intel 平台）

SIMD 技术可显著提高生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从此模块生成 SIMD 代码，请参阅：

- Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Intel Platforms
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon
- Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for ARM Cortex-A Processors

## 版本历史

**在 R2006a 之前推出**

### R2024b：为 Apple silicon 处理器生成 SIMD 代码

在 R2024b 中，如果您拥有 Embedded Coder，则可以使用模型配置参数 **Leverage target hardware instruction set extensions**，为 Apple silicon 处理器上的 Digital Filter Design 模块生成 SIMD 代码。有关详细信息，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon。

## 描述

设计并实现数字 FIR 和 IIR 滤波器

使用此模块设计、分析并高效实现浮点滤波器。

Digital Filter Design 模块实现数字有限冲激响应 (FIR) 或无限冲激响应 (IIR) 滤波器，您可以使用 Filter Designer (`filterDesigner`) App 设计该滤波器。此模块提供与 Discrete FIR Filter 或 Biquad Filter 模块相同的滤波器实现。

您必须通过设置 **Input processing** 参数，指定模块对输入执行基于帧还是基于采样的处理。模块将指定的滤波器应用于离散时间输入信号的每个通道，并输出结果。该模块的输出在数值上与 Discrete FIR Filter 或 Biquad Filter 模块以及 MATLAB® `filter` 函数的输出一致。有关详细信息，请参阅 Getting Started with Filter Designer。

Discrete FIR Filter (Simulink) 和 Biquad Filter 模块也可实现数字滤波器，但用途略有不同。使用这些模块可高效实现您已经设计好的浮点或定点滤波器。这些模块提供与 Digital Filter Design 模块完全相同的滤波器实现。
