---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Math Functions'
documentation_page: 'complextomagnitudeangle'
documentation_source_path: 'ref/complextomagnitudeangle.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex to Magnitude-Angle

## 端口
```yaml
ports:
- name: data
  summary: 复数输入信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: valid
  summary: 指示输入数据是否有效 标量
  direction: input
  data_types: Boolean
- name: Magnitude
  summary: 输入信号的幅值 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixdt([],N,0)
- name: Angle
  summary: 输入信号的相角 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixdt([],N,0)
- name: valid
  summary: 指示输出数据是否有效 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 复数输入信号 标量 | 向量

复数输入信号，指定为标量、表示时间采样的列向量或表示通道的行向量。使用向量输入可提高数据吞吐量，但会占用更多硬件资源。该模块对向量中的每个元素并行实现转换逻辑。输入向量最多可包含 64 个元素。

软件支持在仿真中使用 `double` 和 `single` 数据类型，但不支持将其用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **valid** — 指示输入数据是否有效 标量

指示输入数据是否有效的控制信号。当 **valid** 为 `1` (`true`) 时，该模块捕获来自输入 **data** 端口的值。当 **valid** 为 `0` (`false`) 时，该模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`
### 输出

### **Magnitude** — 输入信号的幅值 标量 | 向量

输入信号的幅值，以标量、表示时间采样的列向量或表示通道的行向量形式返回。此端口的维度与输入 **data** 端口的维度相匹配。

#### 依存关系

要启用此端口，请将 **Output format** 参数设置为 `Magnitude and Angle` 或 `Magnitude`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **Angle** — 输入信号的相角 标量 | 向量

输入信号的相角，以标量、表示时间采样的列向量或表示通道的行向量形式返回。此端口的维度与输入 **data** 端口的维度相匹配。

#### 依赖关系

要启用此端口，请将 **Output format** 参数设置为
`Magnitude and Angle` 或 `Angle`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **valid** — 指示输出数据是否有效 标量

控制信号，指示输出 **data** 端口的数据是否有效。当 **valid** 为
`1`（`true`）时，模块从 **Magnitude** 和/或 **Angle** 端口返回有效数据。当
**valid** 为 `0`（`false`）时，来自 **Magnitude** 和/或 **Angle** 端口的值无效。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Number of iterations source
  summary: 迭代次数的来源 Auto（默认） | Property
  group: ''
- name: Number of iterations
  summary: CORDIC 迭代次数 正整数
  group: ''
- name: Output format
  summary: 输出信号格式 Magnitude and Angle（默认） | Magnitude | Angle
  group: ''
- name: Angle format
  summary: 输出角度格式 Normalized (默认) | Radians
  group: ''
- name: Scale output
  summary: 缩放输出 on (默认) | off
  group: ''
- name: Scaling method
  summary: CORDIC 增益缩放的实现方式 Shift-Add (默认) | Multipliers
  group: ''
```

### **Number of iterations source** — 迭代次数的来源 `Auto`（默认） | `Property`

- 要将迭代次数设置为输入字长 *WL* − 1，请选择
  `Auto`。如果输入的数据类型为 `double` 或
  `single`，则默认情况下，迭代次数设置为 16。
- 要使用 **Number of iterations** 参数指定迭代次数，请选择 `Property`。

### **Number of iterations** — CORDIC 迭代次数 正整数

迭代次数必须小于或等于输入字长 *WL* −
1。模块的延迟取决于所执行的迭代次数。有关延迟的信息，请参阅“延迟”。

#### 依赖关系

要启用此参数，请将 **Number of iterations source** 设置为
`Property`。

### **Output format** — 输出信号格式 `Magnitude and Angle`（默认） | `Magnitude` | `Angle`

使用此参数指定启用哪些输出端口。

- 要启用 **Magnitude** 和 **Angle**
  输出端口，请选择 `Magnitude and Angle`（默认）。
- 要启用 **Magnitude** 输出端口并禁用
  **Angle** 输出端口，请选择
  `Magnitude`。
- 要启用 **Angle** 输出端口并禁用
  **Magnitude** 输出端口，请选择 `Angle`。

### **Angle format** — 输出角度格式 `Normalized` (默认) | `Radians`

- 若要以定点值形式返回 **Angle** 输出，并将角度归一化到 [–1,1] 范围内，请选择 `Normalized`。有关详细信息，请参阅归一化角度格式。
- 若要以 [-π, π] 范围内的定点值形式返回 **Angle** 输出，请选择 `Radians`。使用此模块实现 `atan2` 函数时，请将此参数设置为 `Radians`。

### **Scale output** — 缩放输出 `on` (默认) | `off`

选中此参数可将 **Angle** 输出乘以 CORDIC 增益因子的倒数。该模块根据 **Scaling method** 参数，使用 CSD 逻辑或乘法器来实现此增益因子。

**注意**

如果清除此参数并在设计的其他位置应用 CORDIC 增益，则必须排除 π/4 项。由于象限映射算法通过将输入映射到角度范围 [0, π/4] 来取代第一次 CORDIC 迭代，因此初始旋转不会产生增益项。增益因子是 `cos(atan(2-n))` 的连乘积，其中 *n* 的取值范围为 1 到 **Number of iterations** – 1。

#### 依赖关系

要启用此参数，请将 **Output format** 参数设置为 `Magnitude and Angle` 或 `Magnitude`。

### **Scaling method** — CORDIC 增益缩放的实现方式 `Shift-Add` (默认) | `Multipliers`

当将此参数设置为 `Shift-Add` 时，模块使用移位相加架构实现乘法运算，从而完成 CORDIC 增益缩放。此实现不使用乘法器资源，但可能会增加设计中关键路径的长度。当选择 `Multipliers` 时，模块使用乘法器实现 CORDIC 增益缩放，并将模块的延迟增加四个周期。

#### 依赖关系

要启用此参数，请选中 **Scale output** 参数。
## 所属库

DSP HDL Toolbox / Math Functions

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速模式和快速加速模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认的 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持对复数信号进行代码生成。

## 版本历史

**在 R2014b 中推出**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Complex to Magnitude-Angle HDL Optimized，并包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a：可选择为缩放因子使用乘法器

在以前的版本中，该模块使用移位相加逻辑在硬件中实现 CORDIC 增益。要使用乘法器，请将 **Scaling method** 参数设置为 `Multipliers`。要使用移位相加逻辑，请将此参数设置为 `Shift-Add`。

### R2021b: 高吞吐量接口

该模块接受并返回一个列向量，向量中的元素表示时间上的采样值。输入向量最多可包含 64 个采样值。

## 描述

使用 CORDIC 算法计算复信号的幅值和相角

Complex to Magnitude-Angle 模块计算复信号的幅值和相角，并提供硬件友好的控制信号。为了获得高效的 HDL 实现，该模块使用流水线式坐标旋转数字计算机 (CORDIC) 算法。

您可以使用此模块在硬件中实现 `atan2` 等运算。

**注意**

您还可以使用 DSP HDL IP Designer 应用，在不创建 Simulink® 模型的情况下，为此硬件优化算法生成 HDL 代码。该应用提供与 Simulink 模块相同的接口和配置选项。
