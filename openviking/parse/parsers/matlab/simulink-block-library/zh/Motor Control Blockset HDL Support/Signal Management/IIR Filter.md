---
type: simulink-block
title: 'IIR Filter'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'iirfilter'
documentation_source_path: '../mcb/ref/iirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# IIR Filter

## 端口
```yaml
ports:
- name: u
  summary: 采样输入信号 标量
  direction: input
  data_types: single | double | fixed point
- name: a
  summary: 滤波器系数 标量
  direction: input
  data_types: single | double | fixed point
- name: x0
  summary: 初始状态信号 标量
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: 外部复位信号 标量
  direction: input
  data_types: single | double | fixed point
- name: y
  summary: 滤波后的输出信号 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **u** — 采样输入信号 标量

时域中原始输入信号的采样值。

**数据类型：** `single` | `double` | `fixed point`

### **a** — 滤波器系数 标量

IIR 滤波器的滤波器系数。此信号的数据类型必须与输入信号 **x** 的数据类型相同。当与定点数据类型一起使用时，这可能会限制信号精度。

#### 依赖关系

要启用此端口，请将 **Filter coefficient** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### **x0** — 初始状态信号 标量

IIR 滤波器状态信号的初始值。

#### 依赖关系

要启用此参数，请将 **Initial state** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### **Reset** — 外部复位信号 标量

外部信号，当处于高电平有效状态时，将模块复位以输出 **Initial state**。

#### 依赖关系

要启用此参数，请将 **External reset** 参数设置为 `active high resets to initial condition`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **y** — 滤波后的输出信号 标量

IIR Filter 模块在时域中返回的滤波后的输出信号。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Filter type
  summary: IIR 滤波器类型 Low-pass（默认）| High-pass
  group: ''
- name: Filter coefficient
  summary: 滤波器系数输入方法 Specify via dialog（默认）| Input port
  group: ''
- name: Filter coefficient value
  summary: IIR 滤波器的滤波器系数 0.01（默认）| 范围 (0,1] 内的标量
  group: ''
- name: Initial state
  summary: 指定如何提供初始状态值 Specify via dialog（默认）| Input port
  group: ''
- name: Initial state value
  summary: 状态的初始值 0（默认）| 标量
  group: ''
- name: External reset
  summary: 指定是否提供外部复位信号 none（默认）| active high resets to initial condition
  group: ''
- name: Display cutoff frequency
  summary: 显示截止频率参数 off（默认）| on
  group: ''
- name: Discrete step size (s)
  summary: 模块再次执行前的采样时间 50e-6（默认）| 标量
  group: ''
- name: Theoretical cutoff frequency (Hz)
  summary: IIR 滤波器的理论截止频率 32.1525 | 标量
  group: ''
```

### **Filter type** — IIR 滤波器类型 `Low-pass`（默认）| `High-pass`

IIR 滤波器的类型。

### **Filter coefficient** — 滤波器系数输入方法 `Specify via dialog`（默认）| `Input port`

选择以下方法之一来指定滤波器系数：

- `Specify via dialog` — 如果要使用模块参数对话框指定滤波器系数值，请选择此选项。
- `Input port` — 如果要使用输入端口指定滤波器系数值，请选择此选项。

### **Filter coefficient value** — IIR 滤波器的滤波器系数 `0.01`（默认）| 范围 (0,1] 内的标量

IIR 滤波器的滤波器系数。此信号的数据类型必须与输入信号 **x** 的数据类型相同。当与定点数据类型一起使用时，这可能会限制信号精度。

#### 依赖关系

要启用此参数，请将 **Filter coefficient** 参数设置为 `Specify via dialog`。

### **Initial state** — 指定如何提供初始状态值 `Specify via dialog`（默认）| `Input port`

指定是将初始状态值作为模块参数提供，还是作为输入端口提供。

将此参数设置为以下选项之一：

- `Specify via dialog` — 如果要使用模块参数对话框指定初始状态值，请选择此选项。
- `Input port` — 如果要使用输入端口指定初始状态值，请选择此选项。

### **Initial state value** — 状态的初始值 `0`（默认）| 标量

IIR 滤波器状态的初始值。

#### 依赖关系

要启用此参数，请将 **Initial state** 参数设置为 `Specify via dialog`。

### **External reset** — 指定是否提供外部复位信号 `none`（默认）| `active high resets to initial condition`

指定是否将外部复位信号作为输入端口提供。

将此参数设置为以下选项之一：

- `none` — 如果不希望提供外部复位信号，请选择此选项。
- `active high resets to initial condition` — 如果要使用输入端口提供外部复位信号，请选择此选项。

### **Display cutoff frequency** — 显示截止频率参数 `off`（默认）| `on`

选择此参数，使模块显示 **Theoretical cutoff frequency (Hz)** 参数。

#### 依赖关系

要启用此参数，请将 **Filter coefficient** 参数设置为 `Specify via dialog`。

### **Discrete step size (s)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

每两次连续模块执行之间的固定时间间隔（以秒为单位）。

**注意**

模块使用此值来计算并显示模块对话框中的**Theoretical cutoff frequency (Hz)**。此参数不设置模块的采样时间。模块从模型继承采样时间。

#### 依赖关系

要显示此参数：

- 将 **Filter coefficient** 参数设置为 `Specify via dialog`。
- 选择 **Display cutoff frequency** 参数。

### **Theoretical cutoff frequency (Hz)** — IIR 滤波器的理论截止频率 `32.1525` | 标量

计算得到的 IIR 滤波器理论截止频率（以赫兹为单位）。此参数不可配置。

#### 依赖关系

要显示此参数：

- 将 **Filter coefficient** 参数设置为 `Specify via dialog`。
- 选择 **Display cutoff frequency** 参数。
## 所属库

Motor Control Blockset / Signal Management Motor Control Blockset HDL Support / Signal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

### R2025a：新增输入端口和模块参数

模块参数对话框现在包含用于指定初始输出值和来自输入端口的 external reset 信号的参数。

## 描述

实现无限脉冲响应 (IIR) 滤波器

IIR Filter 模块对指定输入信号实现离散一阶无限脉冲响应 (IIR) 滤波器。该模块支持定点数和浮点数数据类型。当您将其与 Motor Control Blockset™ 附带的示例所采用的模型设置和配置一起使用时，该模块还针对代码生成进行了优化。

建议您为此模块使用固定步长离散求解器，以启用代码生成并确保准确的仿真。

### 方程

您可以使用滤波器系数 (a) 模块参数来配置 IIR 滤波器，从而为滤波器设置所需的截止频率 (*f*c)。您也可以选择通过输入端口提供滤波器系数值。

如果您知道滤波器的截止频率，可以使用以下方程计算所需的滤波器系数：

a= ( 2πTsfc2πTsfc+1 )

该模块还包含在模块掩码上显示给定滤波器系数和采样时间对应的截止频率的选项。

使用 **Filter type** 参数将模块配置为低通或高通滤波器。

以下两个方程描述了该模块如何计算其输出。

`低通滤波器：`

y(k)=a⋅u(k)+(1−a)⋅y(k−1)

`高通滤波器：`

y(k)=(1−a)[u(k)−u(k−1)+y(k−1)]

其中：

- *f*c 是 IIR 滤波器的截止频率。
- a 是滤波器系数 (0 < a ≤ 1)。
- y(k) 是时间 k 处的输出值。
- y(k−1) 是时间 k−1 处的输出值。
- x(k) 是时间 k 处的输入值。
- x(k−1) 是时间 k−1 处的输入值。
- *T*s 是 IIR Filter 模块的采样时间。

低通和高通 IIR 滤波器都可以建模为 RC 滤波器，其中状态值对应于电容器两端的电压降。

以下方程描述了该模块如何根据初始输入 `u0` 和初始状态 `x0` 计算初始输出 `y0`。

`低通滤波器：`

y0=x0

`高通滤波器：`

y0=u0−x0
