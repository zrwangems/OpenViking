---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Complex Numbers'
documentation_page: 'complextomagnitudeangle'
documentation_source_path: '../dsphdl/ref/complextomagnitudeangle.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex to Magnitude-Angle

## 端口

### 输入

### **data** — 复数输入信号 标量 | 向量

复数输入信号，指定为标量、表示时间样本的列向量或表示通道的行向量。使用向量输入可提高数据吞吐量，但会占用更多硬件资源。该模块对向量的每个元素并行实现转换逻辑。输入向量最多可包含 64 个元素。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **valid** — 指示输入数据有效 标量

控制信号，用于指示输入数据是否有效。当
**valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当
**valid** 为 `0`（`false`）时，模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### 输出

### **Magnitude** — 输入信号的幅值 标量 | 向量

输入信号的幅值，以标量、表示时间样本的列向量或表示通道的行向量形式返回。此端口的维度与输入 **data** 端口的维度匹配。

#### 依赖关系

要启用此端口，请将 **输出格式** 参数设置为
`Magnitude and Angle` 或 `Magnitude`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **Angle** — 输入信号的相位角 标量 | 向量

输入信号的相位角，以标量、表示时间样本的列向量或表示通道的行向量形式返回。此端口的维度与输入 **data** 端口的维度匹配。

#### 依赖关系

要启用此端口，请将 **输出格式** 参数设置为
`Magnitude and Angle` 或 `Angle`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **valid** — 指示输出数据有效 标量

控制信号，用于指示来自输出
**data** 端口的数据是否有效。当 **valid** 为
`1`（`true`）时，模块从 **Magnitude** 和/或 **Angle** 端口返回有效数据。当
**valid** 为 `0`（`false`）时，来自 **Magnitude** 和/或 **Angle** 端口的值无效。

**数据类型：** `Boolean`

## 参数

### **迭代次数来源** — 迭代次数的来源 `Auto`（默认）| `Property`

- 要将迭代次数设置为输入 *WL* − 1，请选择
  `Auto`。如果输入的数据类型为 `double` 或
  `single`，则默认情况下迭代次数设置为 16。
- 要通过 **迭代次数** 参数指定迭代次数，请选择 `Property`。

### **迭代次数** — CORDIC 迭代次数 正整数

迭代次数必须小于或等于输入 *WL* −
1。模块的时延取决于所执行的迭代次数。有关时延的信息，请参阅 Latency。

#### 依赖关系

要启用此参数，请将 **迭代次数来源** 设置为
`Property`。

### **输出格式** — 输出信号格式 `Magnitude and Angle`（默认）| `Magnitude` | `Angle`

使用此参数指定启用哪些输出端口。

- 要启用 **Magnitude** 和 **Angle**
  输出端口，请选择 `Magnitude and Angle`（默认）。
- 要启用 **Magnitude** 输出端口并禁用
  **Angle** 输出端口，请选择
  `Magnitude`。
- 要启用 **Angle** 输出端口并禁用
  **Magnitude** 输出端口，请选择 `Angle`。

### **角度格式** — 输出角度格式 `Normalized`（默认）| `Radians`

- 要将 **Angle** 输出返回为将角度归一化到范围 [–1,1] 内的定点值，请选择 `Normalized`。有关更多信息，请参阅 Normalized Angle Format。
- 要将 **Angle** 输出返回为范围 [-π, π] 内的定点值，请选择 `Radians`。使用此模块实现
  `atan2` 函数时，请将此参数设置为
  `Radians`。

### **缩放输出** — 缩放输出 `on`（默认）| `off`

选择此参数可将 **Angle** 输出乘以 CORDIC 增益因子的倒数。模块根据 **缩放方法** 参数，使用 CSD
逻辑或乘法器实现此增益因子。

**注意**

如果清除此参数并在设计中的其他地方应用 CORDIC 增益，
则必须排除 π/4 项。因为象限映射算法通过将输入映射到角度范围 [0, π/4] 来替代第一次 CORDIC 迭代，所以初始旋转不贡献增益项。增益因子是
`cos(atan(2-n))` 的乘积，其中
*n* 从 1 到 **迭代次数** – 1。

#### 依赖关系

要启用此参数，请将 **输出格式** 参数设置为
`Magnitude and Angle` 或 `Magnitude`。

### **缩放方法** — CORDIC 增益缩放的实现 `Shift-Add`（默认）| `Multipliers`

将此参数设置为 `Shift-Add` 时，模块使用移位相加架构进行乘法运算来实现 CORDIC 增益缩放。此实现不使用乘法器资源，并且可能会增加设计中关键路径的长度。选择
`Multipliers` 时，模块使用乘法器实现 CORDIC 增益缩放，并将模块的时延增加 4
cycles。

#### 依赖关系

要启用此参数，请选择 **缩放输出**
参数。

## 所属库

DSP HDL Toolbox / Math Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2014b 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Complex to Magnitude-Angle HDL
Optimized，并包含在 DSP System Toolbox™
**DSP System Toolbox HDL Support** 库中。

### R2022a：使用乘法器实现比例因子的选项

在以前的版本中，该模块使用移位相加逻辑为硬件实现 CORDIC 增益。要使用乘法器，请将 **缩放方法**
参数设置为 `Multipliers`。要使用移位相加逻辑，请将此参数设置为 `Shift-Add`。

### R2021b：高吞吐量接口

该模块接受并返回表示时间样本的元素的列向量。输入向量最多可包含 64 个样本。

## 描述

使用 CORDIC 算法计算复数信号的幅值和相位角

Complex to Magnitude-Angle 模块计算复数信号的幅值和相位角，并提供对硬件友好的控制信号。为实现高效的
HDL 实现，该模块使用流水线坐标旋转数字计算机 (CORDIC)
算法。

您可以使用此模块在硬件中实现诸如 `atan2` 之类的运算。

**注意**

您还可以使用 DSP HDL IP Designer 应用为这种硬件优化算法生成 HDL 代码，而无需创建
Simulink® 模型。该应用提供与 Simulink 模块相同的界面和配置选项。
