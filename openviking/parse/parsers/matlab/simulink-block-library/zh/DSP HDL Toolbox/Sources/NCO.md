---
type: simulink-block
title: 'NCO'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'nco'
documentation_source_path: 'ref/nco.html'
language: zh-CN
chinese_source: worker-translation
---

# NCO

## 端口
```yaml
ports:
- name: inc
  summary: 相位增量标量整数
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixdt([],N,0)
- name: offset
  summary: 相位偏移标量整数
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixdt([],N,0)
- name: dither
  summary: 抖动整数 | 整数列向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixdt([],N,0)
- name: valid
  summary: 启用 NCO 操作的控制信号标量
  direction: input
  data_types: Boolean
- name: reset accum
  summary: 复位累加器标量
  direction: input
  data_types: Boolean
- name: sin, cos, exp
  summary: 生成波形标量 | 列向量
  direction: output
- name: phase
  summary: NCO 的当前相位标量 | 列向量
  direction: output
  data_types: single | double | fixdt(1,N,0)
- name: valid
  summary: 指示输出数据的有效性标量
  direction: output
  data_types: Boolean
```

### 输入

### **inc** — 相位增量标量整数

相位增量，指定为标量整数。该模块将此值强制转换以匹配累加器字长。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

#### 依赖

要启用此端口，请将 **Phase increment source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **offset** — 相位偏移标量整数

相位偏移，指定为标量整数。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

#### 依赖

要启用此端口，请将 **Phase offset source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **dither** — 抖动整数 | 整数列向量

抖动，指定为整数或整数列向量。向量的长度必须等于 **Samples per frame** 参数值。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。

#### 依赖

要启用此端口，请将 **Dither source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **valid** — 启用 NCO 操作的控制信号标量

启用 NCO 操作的控制信号，指定为布尔标量。当此信号为 `1` 时，模块递增相位并捕获任何输入值。当此信号为 `0` 时，模块保持相位累加器并忽略任何输入值。

当 **Samples per frame** 参数大于 `1` 时，此值启用对 **Samples per frame** 个样本的处理。

**数据类型：** `Boolean`

### **reset accum** — 复位累加器标量

复位累加器的控制信号，指定为布尔标量。当此信号为 `1` 时，模块将累加器复位为其初始值。此信号不会复位流水线中的输出样本。

#### 依赖

要启用此端口，请选择 **Enable accumulator reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **sin, cos, exp** — 生成波形标量 | 列向量

生成的波形，以标量或长度等于 **Samples per frame** 参数值的列向量形式返回。输出可以是返回 **sin** 或 **cos** 值的单个端口，返回表示 `cosine + j*sine` 的 **exp** 值的单个端口，或分别返回 **sin** 和 **cos** 值的两个端口。

当所有输入值为定点类型或所有输入端口被禁用时，模块使用 **Output data type** 参数确定输出类型。当任何输入值为浮点类型时，模块忽略 **Output data type** 参数。在这种情况下，模块以浮点值返回波形。浮点数据类型支持仿真，但不支持 HDL 代码生成。

#### 依赖

默认情况下，此输出端口为正弦波 **sin**。端口标签和格式根据 **Type of output signal** 参数而变化。

### **phase** — NCO 的当前相位标量 | 列向量

NCO 的当前相位，以标量或长度等于 **Samples per frame** 参数值的列向量形式返回。相位是应用了偏移和增量后的量化累加器的输出。如果量化被禁用，此端口返回应用了偏移和增量后的累加器的输出。值的类型为 `fixdt(1,N,0)`，其中 `N` 是 **Number of quantizer accumulator bits** 参数值。如果量化被禁用，则 `N` 是 **Accumulator Word length** 参数值。

如果任何输入值为浮点类型，模块以浮点值返回 **phase**。浮点数据类型支持仿真，但不支持 HDL 代码生成。

#### 依赖

要启用此端口，请选择 **Enable phase port** 参数。

**数据类型：** `single` | `double` | `fixdt(1,N,0)`

### **valid** — 指示输出数据的有效性标量

指示输出数据有效性的控制信号，以布尔标量形式返回。当输出 **valid** 为 `1` 时，**sin**、**cos**、**exp** 和 **phase** 端口上的值有效。当输出 **valid** 为 `0` 时，输出端口上的值无效。

当 **Samples per frame** 参数大于 `1` 时，此信号指示输出向量中所有元素的有效性。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Phase increment source
  summary: 相位增量的来源 Input port（默认）| Property
  group: 主要
- name: Phase increment
  summary: 生成波形的相位增量 100（默认）| 整数
  group: 主要
- name: Phase offset source
  summary: 相位偏移的来源 Input port（默认）| Property
  group: 主要
- name: Phase offset
  summary: 生成波形的相位偏移 0（默认）| 整数
  group: 主要
- name: Dither source
  summary: 抖动位数的来源 Property（默认）| Input port | None
  group: 主要
- name: Number of dither bits
  summary: 用于表示抖动的位数 4（默认）| 正整数
  group: 主要
- name: Samples per frame
  summary: 基于帧的输入和输出的向量大小 1（默认）| 正整数
  group: 主要
- name: Enable look up table compression method
  summary: 压缩查找表 off（默认）| on
  group: 主要
- name: Enable accumulator reset input port
  summary: 启用复位控制信号 off（默认）| on
  group: 主要
- name: Type of output signal
  summary: 输出波形的格式 Sine（默认）| Cosine | Complex exponential | Sine and cosine
  group: 主要
- name: Enable phase port
  summary: 输出当前相位 off（默认）| on
  group: 主要
- name: Rounding Mode
  summary: 定点运算的舍入模式 Floor（默认）
  group: 数据类型
- name: Overflow mode
  summary: 定点运算的溢出模式 Wrap（默认）
  group: 数据类型
- name: Accumulator Data Type
  summary: 累加器数据类型 Binary point scaling（默认）
  group: 数据类型
- name: Accumulator Signed
  summary: 有符号或无符号累加器数据格式 Signed（默认）
  group: 数据类型
- name: Accumulator Word length
  summary: 累加器字长 16（默认）| 整数
  group: 数据类型
- name: Accumulator Fraction length
  summary: 累加器小数长度 0（默认）| 整数
  group: 数据类型
- name: Quantize phase
  summary: 量化累加相位 off（默认）| on
  group: 数据类型
- name: Number of quantizer accumulator bits
  summary: 量化器累加器位数 12（默认）| 整数
  group: 数据类型
- name: Output Data Type
  summary: 输出数据类型 Binary point scaling（默认）| double | single
  group: 数据类型
- name: Output Signed
  summary: 有符号或无符号输出数据格式 Signed（默认）
  group: 数据类型
- name: Output Word length
  summary: 输出字长 16（默认）| 整数
  group: 数据类型
- name: Output Fraction length
  summary: 输出小数长度 14（默认）| 整数
  group: 数据类型
```

### 主要

**注意**

此模块支持 `double` 和 `single` 输入用于仿真，但不支持 HDL 代码生成。当所有输入值为定点类型或所有输入端口被禁用时，模块使用 **Output data type** 参数确定输出类型。当任何输入值为浮点类型时，模块忽略 **Output data type** 参数。在这种情况下，模块以浮点值返回波形和可选的 **phase**。

要使用 Fixed-Point Designer™ 数据类型覆盖功能，您可以通过将 `double` 输入数据应用于其中一个可选端口来获得 `double` 输出值。

### **Phase increment source** — 相位增量的来源 `Input port`（默认）| `Property`

您可以通过输入端口或为参数输入值来设置相位增量。如果选择 `Property`，将出现 **Phase increment** 参数供您输入值。如果选择 `Input port`，模块上将出现 **inc** 端口。

### **Phase increment** — 生成波形的相位增量 `100`（默认）| 整数

生成波形的相位增量，指定为整数。模块将此值强制转换以匹配累加器字长。

#### 依赖

要启用此参数，请将 **Phase increment source** 参数设置为 `Property`。

### **Phase offset source** — 相位偏移的来源 `Input port`（默认）| `Property`

您可以通过输入端口或为参数输入值来设置相位偏移。如果选择 `Property`，将出现 **Phase offset** 参数供您输入值。如果选择 `Input port`，模块上将出现 **offset** 端口。

### **Phase offset** — 生成波形的相位偏移 `0`（默认）| 整数

生成波形的相位偏移，指定为整数。

#### 依赖

要启用此参数，请将 **Phase offset source** 参数设置为 `Property`。

### **Dither source** — 抖动位数的来源 `Property`（默认）| `Input port` | `None`

您可以通过输入端口或参数来设置抖动。如果选择 `Property`，将出现 **Number of dither bits** 参数。如果选择 `Input port`，模块上将出现一个端口。如果选择 `None`，模块不添加抖动。

### **Number of dither bits** — 用于表示抖动的位数 `4`（默认）| 正整数

抖动位数，指定为正整数。

#### 依赖

要启用此参数，请将 **Dither source** 参数设置为 `Property`。

### **Samples per frame** — 基于帧的输入和输出的向量大小 `1`（默认）| 正整数

当将此值设置为 `1` 时，模块具有标量输入和输出。当此值大于 `1` 时，**dither** 端口期望长度为 **Samples per frame** 的列向量，并且 **sin**、**cos**、**exp** 和 **phase** 端口返回长度为 **Samples per frame** 的列向量。

### **Enable look up table compression method** — 压缩查找表 `off`（默认）| `on`

默认情况下，模块实现非压缩查找表，此模块的输出与 NCO 模块的输出匹配。当您启用此选项时，模块实现压缩查找表。Sunderland 压缩方法减小了查找表的大小，精度损失小于 1 个 LSB。无杂散动态范围（SFDR）在经验上比非压缩情况低 1–3 dB。压缩查找表的硬件节省为通过增加累加器字长和量化位数来提高性能提供了空间。有关压缩方法的详细信息，请参阅算法。

### **Enable accumulator reset input port** — 启用复位控制信号 `off`（默认）| `on`

选择此参数以启用 **reset accum** 端口。当 **reset accum** 为 `1` 时，模块将累加器复位为其初始值。

### **Type of output signal** — 输出波形的格式 `Sine`（默认）| `Cosine` | `Complex exponential` | `Sine and cosine`

如果选择 `Sine` 或 `Cosine`，模块显示适用的端口 **sin** 或 **cos**。如果选择 `Complex exponential`，输出形式为 `cosine + j*sine`，端口标记为 **exp**。如果选择 `Sine and cosine`，模块显示两个端口 **sin** 和 **cos**。

当将 **Type of output signal** 参数设置为 `Complex exponential` 或 `Sine and cosine` 时，模块为波形的正弦和余弦部分各实现一个 1/8 正弦波查找表，并使用控制逻辑选择和反转值以生成正弦和余弦波形。这种优化意味着双输出模式与单输出模式相比使用相似的硬件资源。

### **Enable phase port** — 输出当前相位 `off`（默认）| `on`

选择此参数以在 **phase** 端口上返回当前 NCO 相位。相位是应用了偏移和增量后的量化累加器的输出。如果量化被禁用，此端口返回应用了偏移和增量后的累加器的输出。

### 数据类型

### **Rounding Mode** — 定点运算的舍入模式 `Floor`（默认）

定点运算的舍入模式。**Rounding Mode** 是只读参数，值为 `Floor`。

### **Overflow mode** — 定点运算的溢出模式 `Wrap`（默认）

定点运算的溢出模式。**Overflow mode** 是只读参数。定点数在溢出时回绕。

### **Accumulator Data Type** — 累加器数据类型 `Binary point scaling`（默认）

累加器数据类型描述。此参数为只读，值为 `Binary point scaling`。模块使用 **Accumulator Signed**、**Accumulator Word length** 和 **Accumulator Fraction length** 参数定义定点数据类型。

### **Accumulator Signed** — 有符号或无符号累加器数据格式 `Signed`（默认）

此参数为只读。所有输出均为有符号格式。

### **Accumulator Word length** — 累加器字长 `16`（默认）| 整数

单位为位。此值必须包含符号位。

如果清除 **Quantize phase** 参数，则 **Accumulator word length** 决定 LUT 大小。对于 HDL 代码生成，LUT 大小必须在 2 到 217 个条目之间。当选择 **Enable look up table compression method** 时，此参数必须是范围 [5,21] 内的整数。当清除 **Enable look up table compression method** 时，此参数必须是范围 [3,19] 内的整数。有关此参数如何影响 LUT 大小的更多信息，请参阅算法部分。

当选择 **Quantize phase** 参数时，**Accumulator word length** 参数值没有限制。

### **Accumulator Fraction length** — 累加器小数长度 `0`（默认）| 整数

此参数为只读。累加器小数长度为零位。

累加器对整数进行运算。如果相位增量为带小数部分的 `fixdt` 类型，模块将返回错误。

### **Quantize phase** — 量化累加相位 `off`（默认）| `on`

当选择 **Quantize phase** 时，模块将相位累加器的结果量化为固定位宽。模块使用此量化值从查找表中选择波形值。量化相位累加器的输出使您能够在不降低频率分辨率的情况下减小查找表大小。使用 **Number of quantizer accumulator bits** 参数选择查找表的大小。

当清除 **Quantize phase** 时，模块使用完整累加器值作为查找表的地址。

### **Number of quantizer accumulator bits** — 量化器累加器位数 `12`（默认）| 整数

量化器累加器位数，指定为小于累加器字长的整数标量。对于 HDL 代码生成，此参数值必须产生 2 到 217 个条目之间的 LUT 大小。当选择 **Enable look up table compression method** 时，此参数必须是范围 [5,21] 内的整数。当清除 **Enable look up table compression method** 时，此参数必须是范围 [3,19] 内的整数。有关此参数如何影响 LUT 大小的更多信息，请参阅算法部分。

#### 依赖

要启用此参数，请选择 **Quantize phase** 参数。

### **Output Data Type** — 输出数据类型 `Binary point scaling`（默认）| `double` | `single`

指定 **sin**、**cos** 和 **exp** 端口的数据类型。如果任何输入为浮点类型，则忽略此参数。在这种情况下，输出数据类型为浮点。

如果选择 `Binary point scaling`，模块使用 **Output Signed**、**Output Word length** 和 **Output Fraction length** 参数定义定点数据类型。

### **Output Signed** — 有符号或无符号输出数据格式 `Signed`（默认）

此参数为只读。所有输出均为有符号格式。

### **Output Word length** — 输出字长 `16`（默认）| 整数

单位为位。此值必须包含符号位。

### **Output Fraction length** — 输出小数长度 `14`（默认）| 整数

单位为位。
## 所属库

DSP HDL Toolbox / Signal Operations DSP HDL Toolbox / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 当您将 **Dither source** 设置为 `Property` 时，该模块每个周期都会添加随机抖动。如果您使用这些设置生成验证模型，则会显示警告。内部抖动的随机生成可能导致模型之间出现不匹配。您可以增加验证比较的误差容限以考虑该差异。您也可以禁用抖动或将 **Dither source** 设置为 `Input port` 以避免此问题。
- 您不能在可复位同步子系统 (HDL Coder) 内使用 NCO 模块。

## 版本历史

**在 R2013a 中引入**

### R2022a: 从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 NCO HDL Optimized，并包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a: 双输出模式的资源优化

当您将 **Type of output signal** 参数设置为 `Complex exponential` 或 `Sine and cosine` 时，此模块会为波形的正弦和余弦部分分别实现一个 1/8 正弦波查找表，并使用控制逻辑选择并反转这些值以生成正弦和余弦波形。此优化意味着双输出模式使用的硬件资源与单输出模式相似。在以前的版本中，该模块为每个输出波形实现一个查找表。

### R2020a: 需要有效输入端口

在以前的版本中，输入 **validIn** 端口是可选的。现在它是必需的，并重命名为 **valid**。如果您不使用其他输入端口，则该模块使用 **valid** 信号作为使能信号。

### R2020a: 浮点输入的相位量化

从浮点输入值返回的输出波形已更改。现在，输出波形与从以定点类型指定的相同输入值返回的波形匹配。

在 R2020a 之前，使用浮点输入类型时，该模块不会在内部量化相位。该模块期望以弧度指定浮点相位增量和相位偏移输入。现在，该模块会在内部量化相位，并且对于浮点输入类型和定点输入类型，您都必须根据量化大小指定输入相位增量和偏移。

例如，在 R2020a 之前，对于浮点 HDL NCO，要以所需输出频率 *F*0 和采样频率 *F*s 生成输出样本，您必须将相位增量指定为 2π(*F*0/*F*s)，并将相位偏移指定为 π/2。

从 R2020a 开始，您必须根据量化大小 *N* 指定相位增量和相位偏移。这些输入值与您使用定点类型时使用的输入值相同。将相位增量指定为 (*F*0×2*N*)/*F*s，并将相位偏移指定为 (π/2)×2*N*/2π，或 2*N*/4。

### R2020a: 移除了 LUTRegisterResetType 选项

在以前的版本中，您可以在 **HDL Block Properties** 对话框的 **LUTRegisterResetType** 参数中选择两个选项。这两个选项是 `default` 和 `none`。从 R2020a 开始，该模块忽略该参数设置，并对该参数值使用 `none`。此选项不会将复位信号连接到 LUT 寄存器。此配置使综合工具能够确定是使用 LUT 还是 BRAM 实现查找表。

### R2020a: 高吞吐量接口

您可以从该模块生成基于帧的波形。该模块返回一个向量，其中每个元素表示一个时间样本。将 **Samples per frame** 参数设置为所需的输出向量大小。

## 描述

生成实数或复数正弦信号

NCO 模块生成实数或复数正弦信号，同时提供硬件友好的控制信号。

数控振荡器 (NCO) 累加相位增量，并使用累加器的量化输出作为包含正弦波值的查找表的索引。定点累加器和量化器数据类型的回绕提供了正弦波的周期性，而量化减少了给定频率分辨率所需的表大小。

NCO 的高层架构

有关如何使用 NCO 模块生成正弦波的示例，请参阅 Generate Sine Wave。有关配置和实现的更多信息，请参阅 Algorithms 部分。

该模块还提供以下功能：

- 可选的基于帧的输出。
- 查找表压缩选项，用于减小查找表大小。此压缩导致精度损失小于一个 LSB。有关更多信息，请参阅 Lookup Table Compression。
- 用于外部抖动的可选输入端口。
- 可选复位端口，用于将相位累加器复位为其初始值。
- 用于当前 NCO 相位的可选输出端口。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
