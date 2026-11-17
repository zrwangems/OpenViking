---
type: simulink-block
title: 'LMS Filter'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'lmsfilter'
documentation_source_path: '../dsphdl/ref/lmsfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# LMS Filter

## 端口
```yaml
ports:
- name: data
  summary: 输入数据 实数或复数值的标量或列向量
  direction: input
  data_types: single | double | fixed point
- name: desired
  summary: 期望输入数据 实数或复数值的标量或列向量
  direction: input
  data_types: single | double | fixed point
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: stepSize
  summary: 滤波器的收敛性和稳定性 实数标量
  direction: input
  data_types: double | single | fixed point
- name: adapt
  summary: 更新滤波器权重 标量
  direction: input
  data_types: Boolean
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 滤波后的输出数据 实数或复数值的标量或列向量
  direction: output
  data_types: single | double | fixed point
- name: valid
  summary: 指示有效输出数据 标量
  direction: output
  data_types: Boolean
- name: error
  summary: 输出信号与期望信号之间的误差 实数或复数标量或列向量
  direction: output
  data_types: Boolean
- name: weights
  summary: 更新后的滤波器权重 行向量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据 实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。输入向量大小必须在 [2, 64] 范围内，且必须小于滤波器长度。该模块仅支持最高 32 位的输入字长。

使用 `double` 和 `single` 数据类型进行仿真，但不用于 HDL 代码生成。对于 HDL 代码生成，输入数据类型必须为 `signed fixed point`。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **desired** — 期望输入数据 实数或复数值的标量或列向量

期望输入数据，指定为实数或复数值的标量或列向量。输入向量大小必须在 [2, 64] 范围内，且必须小于滤波器长度。**desired** 端口必须与输入 **data** 端口具有相同的数据类型、复数性和维度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入端口 **data** 和 **desired** 捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入端口 **data** 和 **desired** 的值。

**数据类型：** `Boolean`

### **stepSize** — 滤波器的收敛性和稳定性 实数标量

指定步长以控制滤波器的收敛性和稳定性。推荐的步长必须小于 1/(2 x *输入功率* x *滤波器长度*)。

您可以使用 `double` 和 `single` 数据类型进行仿真，但不用于 HDL 代码生成。对于 HDL 代码生成，输入数据类型必须为 `unsigned fixed point`。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上将 **Step-size source** 参数设置为 `Input port`。

**数据类型：** `double` | `single` | `fixed point`

### **adapt** — 更新滤波器权重 标量

当 **adapt** 为 `1`（`true`）且输入 **valid** 为 `1`（`true`）时，模块针对每个输入 **valid** 适应新的滤波器权重。当 **adapt** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）或 `0`（`false`）时，模块保持其先前的滤波器权重。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选中 **Enable adapt input port** 参数。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算，清除内部状态，并设置为模块掩码上指定的滤波器权重初始值。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选中 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 滤波后的输出数据 实数或复数值的标量或列向量

滤波后的输出数据，以实数或复数值的标量或列向量形式返回。输出的维度与输入的维度匹配。

当输入数据为浮点类型时，输出数据继承输入数据的数据类型。当输入数据为定点类型时，输出数据为定点类型，其字长和小数长度各增加 1。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **error** — 输出信号与期望信号之间的误差 实数或复数标量或列向量

当输出 **valid** 为 `1`（`true`）时，输出从期望信号中减去滤波后输出信号的结果。

如果输入数据和期望数据为标量或列向量，则误差信号具有与输入数据相同的维度和复数性。当输入数据为浮点类型时，输出数据继承输入数据的数据类型。当输入数据为定点类型时，输出数据为定点类型，其字长增加 2，小数长度增加 1。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选中 **Enable filter error output port** 参数。

**数据类型：** `Boolean`

### **weights** — 更新后的滤波器权重 行向量

对于每次迭代，当输出 **valid** 为 `1`（`true`）时，模块从此端口输出当前更新后的滤波器权重。

对于浮点输入，权重数据类型必须与输入类型匹配。对于定点信号，输入必须与 **Weights** 参数设置的数据类型匹配。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选中 **Enable filter weights output port** 参数。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Filter length
  summary: 滤波器长度 32（默认）| 小于或等于 2048 的正整数
  group: 主要参数
- name: Step-size source
  summary: 步长来源 Property（默认）| Input port
  group: 主要参数
- name: Step size (mu)
  summary: 步长 0.01（默认）| 正标量数值
  group: 主要参数
- name: Initial value of filter weights
  summary: 滤波器权重初始值 0（默认）| 标量 | 行向量
  group: 主要参数
- name: Enable adapt input port
  summary: 启用 adapt 输入端口的选项 off（默认）| on
  group: 主要参数
- name: Enable filter weights output port
  summary: 启用 weights 输出端口的选项 on（默认）| off
  group: 主要参数
- name: Enable filter error output port
  summary: 启用 error 输出端口的选项 off（默认）| on
  group: 主要参数
- name: Rounding mode
  summary: 用于对输出进行类型转换的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 用于对输出进行类型转换的溢出处理 off（默认）| on
  group: 数据类型
- name: Step size
  summary: '步长类型 Inherit: Same word length as input（默认）| fixdt(0,16,16) | <data type expression>'
  group: 数据类型
- name: Weights
  summary: '滤波器权重类型 fixdt(1,16,15)（默认）| Inherit: Same as input | <data type expression>'
  group: 数据类型
- name: Step-size error product
  summary: '步长误差乘积类型 Inherit: Same word length as input（默认）| Inherit: Inherit via internal rule | fixdt(1,16,15) | <data type
    expression>'
  group: 数据类型
- name: Enable reset input port
  summary: 启用 reset 输入端口的选项 off（默认）| on
  group: Control Ports
- name: Use HDL global reset
  summary: 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 off（默认）| on
  group: Control Ports
```

### 主要参数

### **Filter length** — 滤波器长度 `32`（默认）| 小于或等于 2048 的正整数

将 LMS 滤波器的长度指定为小于或等于 2048 的正整数。

### **Step-size source** — 步长来源 `Property`（默认）| `Input port`

选择模块是通过属性还是输入端口指定步长。

- `Property` — 使用 **Step size (mu)** 参数指定步长。
- `Input port` — 使用 **stepSize** 端口指定步长。

### **Step size (mu)** — 步长 `0.01`（默认）| 正标量数值

将步长指定为正标量数值。推荐的步长必须小于 1/(2 x *输入功率* x *滤波器长度*)。

#### 依赖关系

要启用此参数，请将 **Step-size source** 参数设置为 `Property`。

### **Initial value of filter weights** — 滤波器权重初始值 `0`（默认）| 标量 | 行向量

输入滤波器权重初始值，为标量或大小等于滤波器长度的行向量。

当您指定标量值时，模块将其视为等同于指定标量值的行向量。

### **Enable adapt input port** — 启用 adapt 输入端口的选项 `off`（默认）| on

选中此参数以启用 **adapt** 输入端口。

### **Enable filter weights output port** — 启用 weights 输出端口的选项 `on`（默认）| off

选中此参数以启用 **weights** 输出端口。

对于每次迭代，模块从此端口输出当前更新后的滤波器权重。

### **Enable filter error output port** — 启用 error 输出端口的选项 `off`（默认）| on

选中此参数以启用 **error** 输出端口。

### 数据类型

### **Rounding mode** — 用于对输出进行类型转换的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于将输出类型转换为 **Output** 参数指定的数据类型的舍入模式。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 用于对输出进行类型转换的溢出处理 `off`（默认）| `on`

用于将输出类型转换为 **Output** 参数指定的数据类型的溢出处理。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅 Overflow Handling。

### **Step size** — 步长类型 `Inherit: Same word length as input`（默认）| `fixdt(0,16,16)` | `<data type expression>`

指定步长数据类型。

#### 依赖关系

要启用此参数，请将 **Step-size source** 参数设置为 `Property`。

### **Weights** — 滤波器权重类型 `fixdt(1,16,15)`（默认）| `Inherit: Same as input` | `<data type expression>`

指定滤波器权重的数据类型。

### **Step-size error product** — 步长误差乘积类型 `Inherit: Same word length as input`（默认）| `Inherit: Inherit via internal rule` | `fixdt(1,16,15)` | `<data type expression>`

指定步长误差乘积。

### Control Ports

### **Enable reset input port** — 启用 reset 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **reset** 输入端口。复位信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认）| `on`

选中此复选框以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观或修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步的，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。
## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

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

**在 R2023a 中引入**

## 描述

最小化观测信号与期望信号之间的误差

LMS Filter 模块使用均方误差 (MSE) 准则估计滤波器权重并最小化期望信号与观测信号之间的误差。该模块调整其权重，直到数据与期望数据之间的误差最小。该模块接受实数和复数类型的标量和向量输入。

您可以将此模块用于各种应用，例如噪声消除、系统辨识和逆系统建模。该模块提供了适用于 HDL 代码生成和硬件部署的架构。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
