---
type: simulink-block
title: 'Channelizer'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'channelizer'
documentation_source_path: 'ref/channelizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Channelizer

## 端口
```yaml
ports:
- name: data
  summary: 输入数据，实数或复数值的标量或列向量
  direction: input
  data_types: fixed point | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | single | double
- name: valid
  summary: 指示有效输入数据，标量
  direction: input
  data_types: Boolean
- name: reset
  summary: 清除内部状态，标量
  direction: input
  data_types: Boolean
- name: data
  summary: 频率信道输出数据，向量
  direction: output
- name: valid
  summary: 指示有效输出数据，标量
  direction: output
  data_types: Boolean
- name: start
  summary: 指示输出帧的第一个有效周期，标量
  direction: output
  data_types: Boolean
- name: end
  summary: 指示输出帧的最后一个有效周期，标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据，实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。

向量大小必须是 2 的幂，且在 [2, 64] 范围内，并且不大于信道数（FFT 长度）。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

该模块不接受 `uint64` 数据。

**数据类型：** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `single` | `double`
**复数支持：** 是

### **valid** — 指示有效输入数据，标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态，标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面中的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 频率信道输出数据，向量

- 如果将 **Output vector size** 设置为 `Same as number of frequency bands`（默认值），则输出数据为 1×*M* 向量，其中 *M* 为 FFT 长度。
- 如果将 **Output vector size** 设置为 `Same as input size`，则输出数据为 *M*×1 向量，其中 *M* 为输入向量大小。

对于任一输出大小，输出顺序均为位自然序。输出数据类型是 **Filter output** 以及 FFT 中为避免溢出所需的位增长的结果。

### **valid** — 指示有效输出数据，标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **start** — 指示输出帧的第一个有效周期，标量

控制信号，指示输出帧的第一个有效周期。

当 **start** 为 `1`（`true`）时，模块从输出 **data** 端口返回帧的第一个有效采样。

#### 依赖关系

要启用此端口，请在 **Control Ports** 中选择 **Enable start output port** 参数。

**数据类型：** `Boolean`

### **end** — 指示输出帧的最后一个有效周期，标量

控制信号，指示输出帧的最后一个有效周期。

当 **end** 为 `1`（`true`）时，模块从输出 **data** 端口返回帧的最后一个有效采样。

#### 依赖关系

要启用此端口，请在 **Control Ports** 中选择 **Enable end output port** 参数。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Filter coefficients
  summary: 多相滤波器系数 [ -0.032, 0.121, 0.318, 0.482, 0.546, 0.482, 0.318, 0.121, -0.032 ]（默认值）| 实数或复数数值向量
  group: 主
- name: Filter structure
  summary: HDL 滤波器架构 Direct form transposed（默认值）| Direct form systolic
  group: 主
- name: Number of frequency bands (FFT length)
  summary: FFT 长度 8（默认值）| 2 的整数次幂
  group: 主
- name: Complex multiplication
  summary: 复数乘法器的 HDL 实现 Use 4 multipliers and 2 adders（默认值）| Use 3 multipliers and 5 adders
  group: 主
- name: Output vector size
  summary: 输出数据大小 Same as number of frequency bands（默认值）| Same as input size
  group: 主
- name: Divide butterfly outputs by two
  summary: FFT 缩放，开启（默认值）| 关闭
  group: 主
- name: Rounding mode
  summary: 用于内部定点计算的舍入方法 Floor（默认值）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 内部定点计算的溢出处理，关闭（默认值）| 开启
  group: 数据类型
- name: Coefficients
  summary: '滤波器系数的数据类型 Inherit: Same word length as input（默认值）| 数据类型表达式'
  group: 数据类型
- name: Filter output
  summary: '多相滤波器输出的数据类型 Inherit: Same word length as input（默认值）| Inherit: via internal rule | 数据类型表达式'
  group: 数据类型
- name: Enable reset input port
  summary: 可选复位信号，关闭（默认值）| 开启
  group: 控制端口
- name: Enable start output port
  summary: 指示数据开始的可选控制信号，关闭（默认值）| 开启
  group: 控制端口
- name: Enable end output port
  summary: 指示数据结束的可选控制信号，关闭（默认值）| 开启
  group: 控制端口
```

### 主

### **Filter coefficients** — 多相滤波器系数 `[ -0.032, 0.121, 0.318, 0.482, 0.546, 0.482, 0.318, 0.121, -0.032 ]`（默认值）| 实数或复数数值向量

如果系数个数不是 **Number of frequency bands (FFT length)** 的倍数，模块会用零填充此向量。默认滤波器规格为升余弦 FIR 滤波器，`rcosdesign(0.25,2,4,'sqrt')`。您可以指定系数向量或调用返回系数值的滤波器设计函数。默认情况下，模块将系数转换为与输入相同的数据类型。

### **Filter structure** — HDL 滤波器架构 `Direct form transposed`（默认值）| `Direct form systolic`

将 HDL 滤波器架构指定为以下结构之一：

- `Direct form transposed` — 此架构是完全并行实现，适用于 FPGA 和 ASIC 应用。有关架构和性能详细信息，请参阅 Fully Parallel Transposed Architecture。
- `Direct form systolic` — 此架构提供完全并行滤波器实现，可高效利用 Intel® 和 Xilinx® DSP 模块。有关架构和性能详细信息，请参阅 Fully Parallel Systolic Architecture。

### **Number of frequency bands (FFT length)** — FFT 长度 `8`（默认值）| 2 的整数次幂

对于 HDL 代码生成，FFT 长度必须是 2 的幂，从 2² 到 2¹⁶。

### **Complex multiplication** — 复数乘法器的 HDL 实现 `Use 4 multipliers and 2 adders`（默认值）| `Use 3 multipliers and 5 adders`

复数乘法器的 HDL 实现，指定为 `'Use 4 multipliers and 2 adders'` 或 `'Use 3 multipliers and 5 adders'`。根据您的综合工具和目标器件，某个选项可能更快或更小。

### **Output vector size** — 输出数据大小 `Same as number of frequency bands`（默认值）| `Same as input size`

输出数据是 *M* 个元素的向量。对于任一输出大小，输出顺序均为位自然序。

- `Same as number of frequency bands` — 输出数据为 1×*M* 向量，其中 *M* 为 FFT 长度。
- `Same as input size` — 输出数据为 *M*×1 向量，其中 *M* 为输入向量大小。

### **Divide butterfly outputs by two** — FFT 缩放，开启（默认值）| 关闭

当您选择此参数时，FFT 通过将每个流水线级的结果缩放 2 来实现总体 1/*N* 比例因子。此调整使 FFT 的输出保持与其输入相同的幅度范围。如果禁用缩放，FFT 通过在每个级将字长增加 1 位来避免溢出。

### 数据类型

### **Rounding mode** — 用于内部定点计算的舍入方法 `Floor`（默认值）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

请参阅 Rounding Modes。当输入为任何整数或定点数据类型时，模块使用定点算术进行内部计算。当输入为 `single` 或 `double` 时，此选项不适用。每个 FFT 级在旋转因子乘法之后、蝶形运算之前进行舍入。在将系数和多相滤波器的输出转换为您指定的数据类型时，也可能发生舍入。

### **Saturate on integer overflow** — 内部定点计算的溢出处理，关闭（默认值）| 开启

请参阅 Overflow Handling。当输入为任何整数或定点数据类型时，模块使用定点算术进行内部计算。当输入为 `single` 或 `double` 时，此选项不适用。此选项适用于将系数和多相滤波器的输出转换为您指定的数据类型。

FFT 算法通过以下方式之一避免溢出：缩放每个级的输出（启用 `Normalize`），或在每个级将字长增加 1 位（禁用 `Normalize`）。

### **Coefficients** — 滤波器系数的数据类型 `Inherit: Same word length as input`（默认值）| 数据类型表达式

模块使用您指定的舍入和溢出设置，将多相滤波器系数转换为该数据类型。当您选择 `Inherit: Same word length as input`（默认值）时，模块使用 `fi()` 最佳精度规则选择二进制小数点。

### **Filter output** — 多相滤波器输出的数据类型 `Inherit: Same word length as input`（默认值）| `Inherit: via internal rule` | 数据类型表达式

模块使用您指定的舍入和溢出设置，将多相滤波器的输出（FFT 的输入）转换为该数据类型。当您选择 `Inherit: via internal rule` 时，模块通过考虑滤波器系数的值和输入数据类型的范围来选择最佳精度二进制小数点。

默认情况下，FFT 逻辑不修改数据类型。当您禁用 **Divide butterfly outputs by two** 时，FFT 在每个级将字长增加 1 位以避免溢出。

### 控制端口

### **Enable reset input port** — 可选复位信号，关闭（默认值）| 开启

当您选择此参数时，**reset** 端口会显示在模块图标上。当 **reset** 输入为 `true` 时，模块停止计算并清除所有内部状态。

### **Enable start output port** — 指示数据开始的可选控制信号，关闭（默认值）| 开启

当您选择此参数时，**start** 端口会显示在模块图标上。**start** 信号在帧中输出数据的第一个周期为 true。

### **Enable end output port** — 指示数据结束的可选控制信号，关闭（默认值）| 开启

当您选择此参数时，**end** 端口会显示在模块图标上。**end** 信号在帧中输出数据的最后一个周期为 true。
## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017a 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Channelizer HDL Optimized，包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a：FFT 长度为 4

您现在可以将 FFT 长度设置为 4（2²）。在以前的版本中，FFT 长度必须是 2 的幂，从 8（2³）到 2¹⁶。

### R2022a：支持直接型 systolic 滤波器结构

该模块现在支持完全并行 systolic 架构。要使用此架构，请将 **Filter structure** 参数设置为 `Direct form systolic`。

## 描述

多相滤波器组和快速傅里叶变换

Channelizer 模块将宽带输入信号分离为多个窄带输出信号。它为流数据应用提供硬件速度和面积优化。该模块接受实数或复数数据的标量或向量输入，提供硬件友好的控制信号，并具有可选的输出帧控制信号。您可以使用向量输入实现每秒千兆采样（GSPS）吞吐量，也称为超采样率。该模块实现多相滤波器，每个输入向量元素对应一个子滤波器。硬件实现交错子滤波器，从而将每个滤波器乘法器共享（*FFT Length* / *Input Size*）次。FFT 实现使用与 FFT 模块相同的流水线 Radix 2^2 FFT 算法。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
