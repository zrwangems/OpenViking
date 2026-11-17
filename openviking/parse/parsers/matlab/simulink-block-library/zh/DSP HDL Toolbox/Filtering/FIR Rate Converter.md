---
type: simulink-block
title: 'FIR Rate Converter'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'firrateconverter'
documentation_source_path: 'ref/firrateconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Rate Converter

## 端口
```yaml
ports:
- name: data
  summary: 输入数据采样 标量 | 行向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: valid
  summary: 指示输入数据有效 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 输出数据采样 标量 | 行向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: valid
  summary: 指示输出数据有效 标量
  direction: output
  data_types: Boolean
- name: ready
  summary: 指示模块已准备好接收新的输入数据 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据采样 标量 | 行向量

输入数据采样，指定为标量或行向量，其中每个元素表示一个独立通道。该模块接受实数或复数数据。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **valid** — 指示输入数据有效 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入 **data** 端口的值。

您可以每隔 `ceiling(L/M)` 个时间步应用一个有效数据采样。

**数据类型：** `Boolean`
### 输出

### **data** — 输出数据采样 标量 | 行向量

输出数据采样，以标量或行向量形式返回，其中每个元素表示一个独立通道。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **valid** — 指示输出数据有效 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，指示模块已准备好在下一个周期接收新的输入数据采样。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块在下一个时间步忽略任何输入数据。

#### 依赖关系

要启用此端口，请选中 **Enable ready output port** 复选框。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Interpolation factor
  summary: 插值因子 3（默认）| 正整数
  group: 主
- name: Decimation factor
  summary: 抽取因子 2（默认）| 正整数
  group: 主
- name: FIR filter coefficients
  summary: FIR 滤波器系数 firpm(70, [0 0.28 0.32 1],[1 1 0 0])（默认）| 行向量
  group: 主
- name: Rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 溢出操作方式 off（默认）| on
  group: 数据类型
- name: Coefficients
  summary: FIR 滤波器系数数据类型 fixdt(1,16,16)（默认）
  group: 数据类型
- name: Output
  summary: '输出数据采样的数据类型 Inherit: Same word length as input（默认）| Inherit via internal rule | fixdt(s,wl,fl)'
  group: 数据类型
- name: Enable ready output port
  summary: 启用 ready 控制信号的选项 off（默认）| on
  group: 控制端口
```

### 主

### **Interpolation factor** — 插值因子 `3`（默认）| 正整数

指定模块对输入数据采样进行插值的因子。

### **Decimation factor** — 抽取因子 `2`（默认）| 正整数

指定模块对输入数据采样进行抽取的因子。

### **FIR filter coefficients** — FIR 滤波器系数 `firpm(70, [0 0.28 0.32 1],[1 1 0 0])`（默认）| 行向量

指定按 *z-1* 降幂排列的系数行向量。

您还可以将系数指定为工作区变量或对 Signal Processing Toolbox™ 滤波器设计函数（如 `fir1`）的调用。设计一个归一化截止频率不大于 `min(1/L,1/M)` 的低通滤波器。模块将内部滤波器状态初始化为零。

当输入数据类型为浮点类型时，模块将系数转换为与输入相同的数据类型。当输入数据类型为整数类型或定点类型时，请在 **Data Types** 选项卡上设置系数的数据类型。

### 数据类型

### **Rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

选择定点运算的舍入模式。有关详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作方式 `off`（默认）| `on`

指定溢出时饱和还是回绕。

- `off` — 溢出回绕到数据类型可表示的相应值。例如，由于 130 无法容纳在有符号 8 位整数中，它会回绕到 -126。
- `on` — 溢出饱和到数据类型可表示的最小值或最大值。例如，与有符号 8 位整数相关的溢出可以饱和到 -128 或 127。

### **Coefficients** — FIR 滤波器系数数据类型 `fixdt(1,16,16)`（默认）

FIR 滤波器系数数据类型，指定为具有 `signedness`、`word length` 和 `fractional length` 属性的 `fixdt(s,wl,fl)` 对象。当输入为定点或整数类型时，模块使用此参数中的规则或数据类型对滤波器系数进行转换。量化舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点类型时，模块忽略此参数，所有内部运算使用与输入相同的数据类型。

### **Output** — 输出数据采样的数据类型 `Inherit: Same word length as input`（默认）| `Inherit via internal rule` | `fixdt(s,wl,fl)`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型对滤波器输出进行转换。量化使用 **Rounding mode** 和 **Overflow mode** 参数的设置。当输入数据类型为浮点时，模块忽略此参数，并以与输入相同的数据类型返回输出。

### 控制端口

### **Enable ready output port** — 启用 ready 控制信号的选项 `off`（默认）| `on`

选中此参数以启用 **ready** 端口。
## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015b 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，该模块名为 FIR Rate Conversion HDL Optimized，包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a：移除 request 端口

在以前的版本中，该模块提供了一个可选的 **request** 端口。此端口不再可用。有关在模型中控制数据速率的替代方法，请参阅 Control Data Rate Using Ready Signal。

### R2022a：同步 ready 信号

**ready** 信号现在在模块输出端进行流水线处理。在以前的版本中，**ready** 输出信号是直接馈通，没有输出流水线寄存器。

## 描述

对输入信号进行上采样、滤波和下采样

FIR Rate Converter 模块对输入信号进行上采样、滤波和下采样。它针对 HDL 代码生成进行了优化，每次对每个通道的一个采样进行操作。该模块实现多相架构，以避免不必要的算术运算和高中间采样率。

高级速率转换器架构

该模块将输入信号上采样整数因子 *L*，将其应用于 FIR 滤波器，并将输入信号下采样整数因子 *M*。

您可以使用输入和输出控制端口来控制采样的流动。在默认配置中，模块使用输入和输出 **valid** 控制信号。对于额外的流控制，您可以启用 **ready** 输出信号。

**ready** 输出端口指示模块可以在下一个时间步接受新的输入数据采样。当 *L* ≥ *M* 时，您可以使用 **ready** 信号实现连续输出数据采样。如果在模块每次返回 **ready** 信号为 `1` 后应用新的输入采样，则模块在每个时间步返回一个输出 **valid** 信号设置为 `1` 的数据输出采样。

当您禁用 **ready** 端口时，您只能每隔 `ceil(L/M)` 个时间步应用一个有效数据采样。例如，如果：

- *L*/*M* = 4/5，则您可以在每个时间步应用新的输入采样。
- *L*/*M* = 3/2，则您可以在每隔一个时间步应用新的输入采样。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
