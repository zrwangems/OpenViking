---
type: simulink-block
title: 'FIR Decimator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'firdecimator'
documentation_source_path: 'ref/firdecimator.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Decimator

## 端口
```yaml
ports:
- name: data
  summary: 输入数据 标量 | 向量
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: coeff
  summary: 滤波器系数 实数或复数行向量
  direction: input
  data_types: fixed point | int8 | int16 | int32 | uint8 | uint16 | uint32 | single | double
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 滤波后的输出数据 标量
  direction: output
  data_types: fixed point | single | double
- name: valid
  summary: 指示有效输出数据 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据 标量 | 向量

输入数据必须是实值或复值的标量或向量。当您使用向量输入且向量大小小于抽取因子时，抽取因子必须是向量大小的整数倍。当您使用向量输入且向量大小大于抽取因子时，向量大小必须是抽取因子的整数倍。向量大小必须小于或等于 64。

当输入数据类型为整数类型或定点类型时，模块使用定点算术进行内部计算。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **coeff** — 滤波器系数 实数或复数行向量

*自 R2025a 起*

滤波器系数，指定为实数或复数值的行向量。您可以随时更改输入系数。系数向量的大小必须与 **Coefficients prototype** 参数中指定的样本系数大小匹配。原型指定了一个样本系数向量，该向量代表预期输入系数的零值位置。模块使用原型通过移除零值系数的乘法器来优化滤波器。

如果输入 **data** 为定点类型，则 **coeff** 值也必须为定点类型。如果输入 **data** 为浮点数据类型，则 **coeff** 值必须为相同的数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

**数据类型：** `fixed point` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `single` | `double`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅硬件控制信号页面中的复位信号部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable reset input port**。

**数据类型：** `Boolean`
### 输出

### **data** — 滤波后的输出数据 标量

滤波后的输出数据，以实值或复值标量形式返回。当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**Data Types** 选项卡上的 **Output** 参数指定输出数据类型。

输出 **valid** 信号指示抽取后哪些样本有效。当输入向量大小大于抽取因子时，输出为 *VectorSize*/*DecimationFactor* 个样本的向量。

**数据类型：** `fixed point` | `single` | `double`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Coefficient source
  summary: 滤波器系数来源 Property（默认）| Input port (Parallel interface)
  group: 主要
- name: Coefficients
  summary: FIR 滤波器系数 fir1(35,0.4)（默认）| 实数或复数值向量
  group: 主要
- name: Coefficients prototype
  summary: 原型滤波器系数 []（默认）| 实数或复数向量
  group: 主要
- name: Filter structure
  summary: HDL 滤波器架构 Direct form systolic（默认）| Direct form transposed
  group: 主要
- name: Decimation factor
  summary: 抽取因子 2（默认）| 大于二的整数
  group: 主要
- name: Minimum number of cycles between valid input samples
  summary: 输入时序的串行化要求 1（默认）| 正整数
  group: 主要
- name: Optimize symmetric coefficients
  summary: 共享对称系数的乘法器 on（默认）| off
  group: 主要
- name: Rounding mode
  summary: 输出类型转换的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 输出类型转换的溢出处理 off（默认）| on
  group: 数据类型
- name: Coefficients
  summary: '滤波器系数的数据类型 Inherit: Same word length as input（默认）| <data type expression>'
  group: 数据类型
- name: Output
  summary: '滤波器输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same word length as input | <data type expression>'
  group: 数据类型
- name: Enable reset input port
  summary: 启用复位输入端口的选项 off（默认）| on
  group: 控制端口
- name: Use HDL global reset
  summary: 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 off（默认）| on
  group: 控制端口
```

### 主要

### **Coefficient source** — 滤波器系数来源 `Property`（默认）| `Input port (Parallel interface)`

*自 R2025a 起*

您可以将常量滤波器系数作为参数输入，也可以通过输入端口提供时变滤波器系数。

当您选择 `Input port (Parallel interface)` 时，**coeff** 端口会出现在模块上。

选择 `Input port (Parallel interface)` 会启用 **Coefficients prototype** 参数。指定一个原型以使模块能够根据系数的值优化滤波器实现。

当您将可编程系数与基于帧的输入一起使用时，系数值更改后的输出可能与标量情况下的输出不完全匹配。出现此差异是因为与标量实现相比，子滤波器计算相对于输入系数值在不同时间执行。

### **Coefficients** — FIR 滤波器系数 `fir1(35,0.4)`（默认）| 实数或复数值向量

FIR 滤波器系数，指定为实数或复数值向量。您可以将向量指定为工作区变量或滤波器设计函数的调用。当输入数据类型为浮点类型时，模块将系数转换为与输入相同的数据类型。当输入数据类型为整数类型或定点类型时，请在 **Data Types** 选项卡上设置系数的数据类型。

**示例：** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0 0])` 使用线性相位滤波器设计函数定义系数。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

**复数支持：** 是

### **Coefficients prototype** — 原型滤波器系数 `[]`（默认）| 实数或复数向量

*自 R2025a 起*

原型滤波器系数，指定为实数或复数值的向量。原型指定了一个样本系数向量，该向量代表预期输入系数的零值位置。如果所有输入系数向量具有相同的零值系数位置，请将 **Coefficients prototype** 设置为其中一个向量。模块使用原型通过移除零值系数的乘法器来优化滤波器。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

### **Filter structure** — HDL 滤波器架构 `Direct form systolic`（默认）| `Direct form transposed`

模块通过使用 Discrete FIR Filter 模块实现多相分解滤波器。两种结构通过在输入向量中每个样本的一个滤波器实现上交错子滤波器系数来共享资源。将 HDL 滤波器架构指定为以下结构之一：

- `Direct form systolic` — 此架构提供并行或部分串行滤波器实现，可高效利用 Intel 和 Xilinx DSP 模块。对于部分串行实现，请为 **Minimum number of cycles between valid input samples** 参数指定大于 1 的值。您不能将基于帧的输入与部分串行架构一起使用。

  当 **Minimum number of cycles between valid input samples** 大于 1 时，模块选择导致最少乘法器的滤波器架构。如果 *N* 允许每个子滤波器中使用单个乘法器，则模块实现单个串行滤波器并对输出样本进行抽取。
- `Direct form transposed` — 此架构是完全并行实现，适用于 FPGA 和 ASIC 应用。

所有实现通过在输入向量中每个样本的一个滤波器实现上交错子滤波器系数来共享资源。

模块通过使用 Discrete FIR Filter 模块实现多相分解滤波器。有关架构详细信息，请参阅 FIR Filter Architectures for FPGAs and ASICs。

### **Decimation factor** — 抽取因子 2（默认）| 大于二的整数

指定大于二的整数抽取因子。当您使用向量输入且向量大小小于抽取因子时，抽取因子必须是向量大小的整数倍。当您使用向量输入且向量大小大于抽取因子时，向量大小必须是抽取因子的整数倍。

### **Minimum number of cycles between valid input samples** — 输入时序的串行化要求 `1`（默认）| 正整数

输入时序的串行化要求，指定为正整数。此参数表示 *N*，即有效输入样本之间的最小周期数。要实现完全串行架构，请将 **Minimum number of cycles between valid input samples** 设置为大于滤波器长度 *L*，或设置为 `Inf`。

模块在串行化之前应用系数优化，因此最终滤波器的共享因子可能低于您指定的周期数。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form systolic`。

您不能将基于帧的输入与大于 1 的 **Minimum number of cycles between valid input samples** 一起使用。

### **Optimize symmetric coefficients** — 共享对称系数的乘法器 on（默认）| off

*自 R2024b 起*

在多相滤波器架构中启用跨对称系数共享乘法器。此优化减少延迟并将乘法器数量减半。

对称滤波器系数的多相分解不会导致每个多相分支中的对称性。例如，如果滤波器系数为 `[1 2 3 4 4 3 2 1]`，分解后两个多相分支为 `[1 3 4 2]` 和 `[2 4 3 1]`。对称对优化重构系数以恢复多相分支上的对称性。该实现包含一个预加法器，用于组合重构多相分支的输入样本。滤波器输出与非优化实现的输出相同。

### 数据类型

### **Rounding mode** — 输出类型转换的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

将输出类型转换为 **Output** 参数指定的数据类型时的舍入模式。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 输出类型转换的溢出处理 `off`（默认）| `on`

将输出类型转换为 **Output** 参数指定的数据类型时的溢出处理。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅溢出处理。

### **Coefficients** — 滤波器系数的数据类型 `Inherit: Same word length as input`（默认）| `<data type expression>`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型转换滤波器系数。量化舍入到最近的可表示值并在溢出时饱和。当输入数据类型为浮点类型时，模块忽略此参数，所有内部算术使用与输入相同的数据类型。

此参数的推荐数据类型为 `Inherit: Same word length as input`。

如果出现以下情况，模块将返回警告或错误：

- 系数数据类型没有足够的小数长度来准确表示系数。
- 系数数据类型为无符号，且系数包含负值。

### **Output** — 滤波器输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same word length as input` | `<data type expression>`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型转换滤波器的输出。量化使用 **Rounding mode** 和 **Overflow mode** 参数的设置。当输入数据类型为浮点时，模块忽略此参数并以与输入相同的数据类型返回输出。

模块在每个滤波器抽头内增加字长以实现全精度，并将最终输出转换为指定类型。最大最终内部数据类型（*WF*）取决于输入数据类型（*WI*）、系数数据类型（*WC*）和系数数量（*L*），由下式给出

`WF = WI + WC + ceil(log2(L))`。

由于系数值限制了潜在增长，通常实际全精度内部字长小于 *WF*。

### 控制端口

### **Enable reset input port** — 启用复位输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **reset** 输入端口。复位信号实现数据路径寄存器的局部同步复位。

有关更多复位注意事项，请参阅硬件控制信号页面中的复位信号部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认）| `on`

选中此复选框以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观或修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步的，取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅硬件控制信号页面中的复位信号部分。
## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

FIR Decimator 模块不支持通过 HDL Coder 设置进行资源共享优化。相反，请将 **Filter structure** 参数设置为 `Partly serial systolic`，并根据输入时序或资源使用情况配置串行化因子。

## 版本历史

**在 R2020b 中引入**

### R2025a：可编程系数

模块提供可选的 **coeff** 端口，允许随时更改系数。将 **Coefficient source** 参数设置为 `Input port (Parallel interface)`，并将滤波器系数指定为实数或复数值的行向量。

您可以设置 **Coefficients prototype** 属性来指示一致为零值的系数的位置，例如，如果所有输入系数都是半带滤波器。给定原型后，模块会移除零值系数的乘法器。

### R2024b: 优化对称系数

使用 **Optimize symmetric coefficients** 参数可在多相滤波器架构中启用对称系数乘法器优化。此优化可减少延迟并将乘法器数量减半。

### R2022a: 从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 FIR Decimation HDL Optimized，包含在 DSP System Toolbox 的 **DSP System Toolbox HDL Support** 库中。

### R2022a: 串行 systolic 架构

此模块支持部分和完全串行 systolic 架构。如果在有效输入采样之间存在规则模式的无效周期，此架构使您能够共享硬件资源。要使用串行 systolic 架构，请将 **Filter structure** 设置为 `Direct form systolic`，并将 **Minimum number of cycles between valid input samples** 设置为大于 1 的值。串行架构不支持基于帧的输入。

### R2022a: 输入向量大小可以大于抽取因子

在以前的版本中，此模块不支持大于抽取因子的输入向量大小。

## 描述

有限脉冲响应 (FIR) 抽取滤波器

FIR Decimator 模块实现了一个针对 HDL 代码生成优化的单速率多相 FIR 抽取滤波器。此模块提供具有输入和输出控制信号的硬件友好接口。为了提供所生成 HDL 代码的周期精确仿真，此模块对架构延迟（包括流水线寄存器和资源共享）进行建模。

此模块接受标量或向量输入。当您使用向量输入且向量大小小于抽取因子时，抽取因子必须是向量大小的整数倍。在这种情况下，输出为标量，输出有效信号指示抽取后哪些采样有效。输出数据每 *DecimationFactor*/*VectorSize* 个采样有效一次。波形显示了四个采样的输入向量和抽取因子为八的情况。输出数据为标量，每第二个周期有效一次。

逻辑分析仪波形，显示 FIR Decimator 模块在上述配置下的输入和输出信号

当您使用向量输入且向量大小大于抽取因子时，向量大小必须是抽取因子的整数倍。在这种情况下，输出为 *VectorSize*/*DecimationFactor* 个采样的向量。波形显示了八个采样的输入向量和抽取因子为四的情况。输出数据为每个周期两个采样的向量。

逻辑分析仪波形，显示 FIR Decimator 模块在上述配置下的输入和输出信号

此模块提供两种滤波器结构。直接型 systolic 架构提供了一种高效利用 Intel® 和 Xilinx® DSP 模块的实现。此架构可以是完全并行或串行的。要使用串行架构，输入采样之间必须以规则数量的无效周期隔开。直接型转置架构是一种完全并行的实现，适用于 FPGA 和 ASIC 应用。对于将乘法器、流水线寄存器和预加法器与 FPGA 供应商的 DSP 配置相匹配的滤波器实现，请在生成 HDL 代码时指定目标器件。

所有滤波器结构通过共享对称或反对称滤波器的乘法器，以及移除零值系数（如半带滤波器和希尔伯特变换中）的乘法器来优化硬件资源。

此模块为输入向量中的每个采样实现一个滤波器。然后，此模块通过时间交织子滤波器系数，在多相子滤波器之间共享此滤波器。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
