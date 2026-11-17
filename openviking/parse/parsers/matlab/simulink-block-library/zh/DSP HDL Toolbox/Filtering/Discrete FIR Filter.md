---
type: simulink-block
title: 'Discrete FIR Filter'
family: 'hdlcoder'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'discretefirfilter'
documentation_source_path: 'ref/discretefirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete FIR Filter

## 端口
```yaml
ports:
- name: data
  summary: 输入数据 标量 | 列向量 | 行向量
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: valid
  summary: 指示输入数据有效 标量
  direction: input
  data_types: Boolean
- name: coeff
  summary: 滤波器系数（并行接口） 实数或复数行向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: coeff
  summary: 滤波器系数（存储器接口） 实数或复数标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: caddr
  summary: 滤波器系数地址（存储器接口） 标量
  direction: input
  data_types: fixdt(0,N,0)
- name: cwren
  summary: 滤波器系数写使能（存储器接口） 标量
  direction: input
  data_types: Boolean
- name: cdone
  summary: 滤波器系数写入完成（存储器接口） 标量
  direction: input
  data_types: Boolean
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 滤波后的输出数据 标量 | 列向量 | 行向量
  direction: output
  data_types: fixed point | single | double
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

### **data** — 输入数据 标量 | 列向量 | 行向量

输入数据，指定为实数或复数值的标量、列向量或行向量。使用列向量可通过并行处理采样来提高吞吐量。

您可以使用行向量 `[c1 c2 c3]` 来表示单个周期上多个通道的输入采样，也可以提供通道交错的标量多通道数据：第 1 个周期为 `c1` 数据采样，第 2 个周期为 `c2` 数据采样，第 3 个周期为 `c3` 数据采样。各通道可以具有独立的滤波器系数。
 *(自 R2023a 起)*

行向量和标量多通道数据信号的波形。

*在 R2023a 和 R2023b 中：仅当输入之间存在至少与通道数一样多的无效周期时，才能使用多通道行向量输入。当输入为多通道向量时，****Filter structure*** *必须设置为* `Partly serial systolic`*，且****Number of cycles*** *必须大于或等于通道数。此时间允许模块实现一种在通道之间共享资源的部分串行架构。*

基于帧（列向量）的输入不支持多通道系数。要实现高吞吐量多通道滤波器，可以使用 For Each 模块为每个通道实现高吞吐量滤波器。此实现无法在通道之间共享资源。

行向量或列向量的大小必须小于或等于 64 个元素。要实现具有超过 64 个通道的多通道滤波器，必须使用交错的标量输入。

当输入数据类型为整数类型或定点类型时，模块使用定点算术进行内部计算，并在 **Data Types** 选项卡上提供参数以自定义数据类型。当输入数据类型为浮点类型时，模块使用该输入浮点类型进行内部计算和输出数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **valid** — 指示输入数据有效 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **coeff** — 滤波器系数（并行接口） 实数或复数行向量

滤波器系数，指定为实数或复数值的行向量。您可以随时更改输入系数。当使用标量输入数据时，系数向量的大小取决于 **Coefficients prototype** 参数中指定的样本系数的大小和对称性。原型指定了一个样本系数向量，该向量代表了预期输入系数的对称性和零值位置。模块使用原型通过共享对称或反对称系数的乘法器以及移除零值系数的乘法器来优化滤波器。因此，只需在端口提供非重复系数。例如，如果将 **Coefficients prototype** 参数设置为对称的 14 抽头滤波器，则模块期望 **coeff** 输入端口上有一个包含 7 个值的向量。对于非重复的零值系数，您仍必须在输入 **coeff** 向量中提供零。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 来移除零值系数的乘法器。在 **coeff** 输入端口，指定一个与原型大小相同的向量。

如果输入 **data** 为定点类型，则 **coeff** 值也必须为定点类型。如果输入 **data** 为浮点数据类型，则 **coeff** 值必须为相同的数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **coeff** — 滤波器系数（存储器接口） 实数或复数标量

*自 R2023a 起*

滤波器系数，指定为要写入内部存储器的实数或复数值标量。要将单个系数值加载到内部存储器，请在 **caddr** 端口上指定具有对应地址的 **coeff** 值，并在 **cwren** 端口上指定使能信号。您可以随时更改输入系数。

波形图显示了使用存储器接口将一组系数写入滤波器

当您将新系数写入存储器时，模块忽略任何输入数据，但仍返回带有 `validOut` 的 `dataOut`，直到它清空滤波器流水线。模块在 **cdone** 设置为 `1`（`true`）后的下一个周期恢复接受输入。

波形图显示了滤波器在存储器接口上接收新系数时停止处理输入数据

系数存储器具有与 **Coefficients prototype** 参数大小相同数量的地址。原型指定了一个样本系数向量，该向量代表了预期输入系数的对称性和零值位置。当使用标量输入数据时，模块使用原型通过共享对称或反对称系数的乘法器以及移除零值系数的乘法器来优化滤波器。您必须将完整的系数集写入存储器，包括对称或零值系数。例如，如果将 **Coefficients prototype** 参数设置为对称的 14 抽头滤波器，则必须向存储器接口写入 14 个值。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 参数来移除零值系数的乘法器。系数存储器具有与原型大小相同数量的位置。

如果输入 **data** 为定点类型，则 **coeff** 值也必须为定点类型。如果输入 **data** 为浮点数据类型，则 **coeff** 值必须为相同的数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **caddr** — 滤波器系数地址（存储器接口） 标量

*自 R2023a 起*

将滤波器系数地址指定为标量整数值，表示为小数位数为零的无符号定点类型。模块从 **Coefficients prototype** 参数值中唯一系数的数量推导出此整数值的大小以及内部存储器的大小。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `fixdt(0,N,0)`

### **cwren** — 滤波器系数写使能（存储器接口） 标量

*自 R2023a 起*

将此输入设置为 `1`（`true`），以将 **coeff** 端口上的值写入内部存储器中的 **caddr** 位置。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `Boolean`

### **cdone** — 滤波器系数写入完成（存储器接口） 标量

*自 R2023a 起*

将此输入设置为 `1`（`true`），以指示当前端口值将最终系数值写入存储器。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选择 **Enable reset input port**。

**数据类型：** `Boolean`
### 输出

### **data** — 滤波后的输出数据 标量 | 列向量 | 行向量

滤波后的输出数据，以实数或复数值的标量、列向量或行向量形式返回。输出的维度与输入的维度匹配。当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**Data Types** 选项卡上的 **Output** 参数控制输出数据类型。

**数据类型：** `fixed point` | `single` | `double`
**复数支持：** 是

### **valid** — 指示输出数据有效 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，指示模块已准备好在下一个周期接收新的输入数据采样。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块在下一个时间步忽略任何输入数据。

使用部分串行架构时，模块一次处理一个采样。如果您的设计等待此模块返回 **ready** 设置为 `0`（`false`）后再将输入 **valid** 设置为 `0`（`false`），则会有一个额外的输入数据周期到达端口。模块在处理当前数据时存储此额外数据，并且在您的模型处理完额外输入数据之前不会将 **ready** 设置为 `1`（`true`）。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Partly serial systolic`。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Coefficient source
  summary: 滤波器系数的来源 Property（默认） | Input port (Parallel interface) | Input port (Memory interface)
  group: 主要
- name: Coefficients
  summary: 离散 FIR 滤波器系数 [0.5, 0.5]（默认） | 行向量 | 多通道矩阵
  group: 主要
- name: Coefficients prototype
  summary: 原型滤波器系数 []（默认） | 实数或复数向量
  group: 主要
- name: Filter structure
  summary: HDL 滤波器架构 Direct form systolic（默认）| Direct form transposed | Partly serial systolic
  group: 主要
- name: Specify serialization factor as
  summary: 定义串行实现的规则 Minimum number of cycles between valid input samples（默认）| Maximum number of multipliers
  group: 主要
- name: Number of cycles
  summary: 输入时序的序列化要求 2（默认）| 正整数
  group: 主要
- name: Number of multipliers
  summary: 资源使用的序列化要求 2（默认）| 正整数
  group: 主要
- name: Optimize symmetric coefficients
  summary: 在基于帧的输入下为对称系数共享乘法器 on（默认）| off
  group: 主要
- name: Rounding mode
  summary: 用于对输出进行类型转换的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型
- name: Saturate on integer overflow
  summary: 用于对输出进行类型转换的溢出处理 off（默认）| on
  group: 数据类型
- name: Coefficients
  summary: '离散 FIR 滤波器系数的数据类型 Inherit: Same word length as input（默认）| <data type expression>'
  group: 数据类型
- name: Output
  summary: '滤波器输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same word length as input | <data type expression>'
  group: 数据类型
- name: Enable reset input port
  summary: 启用 reset 输入端口的选项 off（默认）| on
  group: 控制端口
- name: Use HDL global reset
  summary: 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 off（默认）| on
  group: 控制端口
- name: Coefficient multiplication
  summary: 硬件中的系数乘法器实现 Multiplier（默认）| CSD/Factored-CSD
  group: 实现
- name: Use multiplier for +/- 1 and power of 2 coefficients
  summary: 硬件中特殊值系数乘法器的实现 on（默认）| off
  group: 实现
```

### 主要

### **Coefficient source** — 滤波器系数的来源 `Property`（默认） | `Input port (Parallel interface)` | `Input port (Memory interface)`

您可以将常量滤波器系数作为参数输入，通过输入端口提供时变滤波器系数，或通过存储器式接口提供时变系数。

不能将可编程系数与多通道数据一起使用。

当您选择 `Input port (Parallel interface)` 时，**coeff** 端口会出现在模块上。

当您选择 `Input port (Memory interface)` 时，模块上会出现存储器式接口。此接口包括 **coeff**、**caddr**、**cwren** 和 **cdone** 端口。

选择 `Input port (Parallel interface)` 或 `Input port (Memory interface)` 会启用 **Coefficients prototype** 参数。指定一个原型以使模块能够根据系数的值优化滤波器实现。

当您将可编程系数与基于帧的输入一起使用时，模块不会针对系数对称性优化滤波器。此外，系数值更改后的输出可能与标量情况下的输出不完全匹配。出现此差异是因为与标量实现相比，子滤波器计算相对于输入系数值在不同时间执行。

#### 依赖关系

*在 R2023b 之前：要使用 `Input port (Parallel interface)`，请将 **Filter structure** 参数设置为 `Direct form systolic` 或 `Direct form transposed`。*

### **Coefficients** — 离散 FIR 滤波器系数 `[0.5, 0.5]`（默认） | 行向量 | 多通道矩阵

离散 FIR 滤波器系数，指定为实数或复数值的行向量。您可以使用 *K*×*L* 的实数或复数值矩阵指定多通道系数，其中 *K* 是通道数，*L* 是滤波器长度。要启用对称性优化，所有通道的对称特性必须一致。例如，如果一个通道是偶对称的，则所有通道都必须是偶对称的。

您还可以将系数指定为工作区变量或滤波器设计函数的调用。当输入数据类型为浮点类型时，模块将系数转换为与输入相同的数据类型。当输入数据类型为整数类型或定点类型时，您可以在 **Data Types** 选项卡上设置系数的数据类型。

**示例：** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0 0])`

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

### **Coefficients prototype** — 原型滤波器系数 `[]`（默认） | 实数或复数向量

原型滤波器系数，指定为实数或复数值的向量。原型指定了一个样本系数向量，该向量代表了预期输入系数的对称性和零值位置。如果所有输入系数向量具有相同的对称性和零值系数位置，请将 **Coefficients prototype** 设置为其中一个向量。模块使用原型通过共享对称或反对称系数的乘法器以及移除零值系数的乘法器来优化滤波器。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 参数来移除零值系数的乘法器。

| 系数来源 | 输入大小 | 如果没有原型 |
| --- | --- | --- |
| `Input port (Parallel interface)` | 当使用标量输入数据时，系数优化会影响 **coeff** 端口上预期向量的大小。只需在端口提供非重复系数。例如，如果将 **Coefficients prototype** 参数设置为对称的 14 抽头滤波器，模块在每对重复系数之间共享一个乘法器，因此模块期望 **coeff** 端口上有一个包含 7 个值的向量。对于非重复的零值系数，您仍必须在输入 **coeff** 向量中提供零。 当使用基于帧的输入数据时，请指定与原型大小相同的 **coeff** 向量。 | 如果您的系数未知或预计不共享对称性或零值位置，可以将 **Coefficients prototype** 设置为 `[]`。 |
| `Input port (Memory interface)` | 写入与原型大小相同数量的系数值。 | **Coefficients prototype** 不能为空。模块使用原型来确定系数存储器的大小。如果您的系数未知或预计不共享对称性或零值位置，请将 **Coefficients prototype** 设置为与预期系数长度相同的向量，该向量不包含对称性或零值，例如 `[1:1:NumCoeffs]`。 |

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Input port (Parallel interface)` 或 `Input port (Memory interface)`。

### **Filter structure** — HDL 滤波器架构 `Direct form systolic`（默认）| `Direct form transposed` | `Partly serial systolic`

将 HDL 滤波器架构指定为以下结构之一：

- `Direct form
  systolic` — 此架构提供完全并行的滤波器实现，
  可高效利用 Intel 和 AMD DSP 模块。有关架构
  详细信息，请参阅 Fully Parallel Systolic Architecture。当您使用此架构指定多通道系数时
  （使用交错输入
  采样），该模块将通道
  系数交错到单个并行滤波器上。
- `Direct form
  transposed` — 此架构是一种
  完全并行实现，适用于
  FPGA 和 ASIC 应用。有关架构
  详细信息，请参阅 Fully Parallel Transposed Architecture。当您使用此架构指定多通道系数时
  （使用交错输入
  采样），该模块将通道
  系数交错到单个并行滤波器上。
- `Partly serial
  systolic` — 此架构
  提供串行滤波器实现，并
  提供在吞吐量与
  资源利用率之间进行权衡的选项。该架构可高效利用 Intel 和 AMD DSP 模块。该模块实现一个
  串行 *L* 系数滤波器，
  具有 *M* 个乘法器，并要求
  输入采样之间至少相隔
  *N* 个周期，使得
  *L* =
  *N*×*M*。您可以
  指定 *M* 或
  *N*。对于此实现，
  该模块提供输出
  **ready** 端口，用于指示
  该模块何时准备好接收新的输入数据。有关
  架构详细信息，请参阅 Partly Serial Systolic Architecture (1 < N < L) 和 Fully Serial Systolic Architecture (N ≥ L)。您不能将基于帧的输入与
  部分串行架构一起使用。

  当您使用串行架构指定多通道系数时，
  必须将序列化因子指定为
  有效输入采样之间的周期数。

  对于标量且
  在通道间交错的多通道输入，该模块
  实现以下串行架构：

  - 当 *N* <
    *L* 时：具有
    *L*/*N*
    个乘法器的部分串行滤波器。
  - 当 *N* >=
    *L* 时：完全串行滤波器。

  对于 1×*K* 向量的多通道输入，其中
  *K* 是通道数，
  该模块实现以下串行架构：

  - 当 *N* = 1 时：完全并行滤波器的
    滤波器组。
  - 当 1
    < *N* <
    *K* 时：部分串行
    滤波器的滤波器组。*（自 R2024a 起）*
  - 当 *N* =
    *K* 时：通道系数交错的完全并行滤波器。
  - 当 *K* <
    *N* <
    *L*×*K* 时：具有
    *L*×*K*/*N*
    个乘法器的部分
    串行滤波器。
  - 当 *N* >=
    *L*×*K* 时：完全
    串行滤波器。

如果任何滤波器是对称的，该架构会为匹配的系数共享
乘法器，因此实际上
*L* 变为
`L/2`。要为多通道滤波器
启用对称优化，
所有通道的对称特性必须一致。

所有单通道实现都会移除零值系数的乘法器。多通道滤波器
不会针对零值系数进行优化。该滤波器为对称和反对称系数
共享乘法器。多通道滤波器在通道之间共享资源，
即使各通道的滤波器系数不同也是如此。

### **Specify serialization factor as** — 定义串行实现的规则 `Minimum number of cycles between valid input samples`（默认）| `Maximum number of multipliers`

您可以将该模块用于序列化
滤波器的规则指定为以下之一：

- `Minimum number of cycles
  between valid input samples` —
  使用 **Number of cycles**
  参数指定输入数据时序要求。
- `Maximum number of
  multipliers` — 使用 **Number of
  multipliers** 参数指定资源使用
  要求。当您具有多通道
  系数时，不支持此选项。

对于具有 *L* 个系数的滤波器，
该模块实现一个串行滤波器，其乘法器不超过
*M* 个，并要求输入
采样之间至少相隔 *N* 个周期，
使得 *L* =
*N*×*M*。该模块
在应用系数
优化时可能会移除乘法器，因此滤波器
实现的实际 *M* 或
*N* 值可能低于指定
值。

如果滤波器是对称的，该架构会为匹配的系数共享
乘法器，因此实际上
`L =
L/2`。

当您将复数
输入数据和/或复数系数与
单通道部分串行架构一起使用时，该模块
实现复数交错，以在非活动输入周期内共享乘法器。
对于复数输入和复数
系数，该模块至少需要
*L*×3 个周期才能使用单个乘法器实现
滤波器。对于具有
实数系数的复数输入或具有实数输入的复数系数，
该模块至少需要 *L*×2 个周期才能
使用单个乘法器实现滤波器。*（自 R2023b 起）*

#### 依赖关系

要启用此参数，请将 **Filter
structure** 参数设置为
`Partly serial systolic`。

### **Number of cycles** — 输入时序的序列化要求 `2`（默认）| 正整数

输入时序的序列化要求，指定为
正整数。此参数表示
*N*，即有效输入采样之间的最小周期数。在这种情况下，该模块
计算 *M* =
*L*/*N*。要
实现完全串行架构，请将
**Number of cycles** 设置为
大于滤波器长度 *L* 的值，
或设置为 `Inf`。要为具有
1×*K* 向量输入的多通道滤波器实现完全串行
架构，请将
**Number of cycles** 设置为
大于 *L*×*K* 的值，
其中 *K* 是通道数。

要为具有复数输入和复数
系数的单通道滤波器实现完全串行架构，请将 **Number of cycles**
设置为大于 *L*×3。如果您具有复数
输入和实数系数，或复数系数和
实数输入，请将 **Number of cycles**
设置为大于 *L*×2。

如果滤波器是对称的，该架构会为匹配的系数共享
乘法器，因此实际上
`L =
L/2`。要为多通道滤波器启用
对称优化，
所有通道的对称特性必须一致。

该模块在应用
系数优化时可能会移除乘法器，因此滤波器的实际
*M* 和 *N* 值
可能低于您指定的
值。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Partly serial
systolic`，并将 **Specify
serialization factor as** 设置为
`Minimum number of cycles between
valid input samples`。

### **Number of multipliers** — 资源使用的序列化要求 `2`（默认）| 正整数

资源使用的序列化要求，指定为
正整数。此参数表示
*M*，即滤波器实现中的最大乘法器
数。在这种情况下，
该模块计算 *N* =
*L*/*M*。如果
输入数据是复数，该模块会分配
`floor(M/2)`
个乘法器用于滤波器的实部，并分配
`floor(M/2)`
个乘法器用于滤波器的虚部。要
实现完全串行架构，请将
**Number of multipliers** 设置为
`1`。

如果滤波器是对称的，该架构会为匹配的系数共享
乘法器，因此实际上
`L =
L/2`。

当您将复数输入数据和/或复数
系数与单通道部分串行
架构一起使用时，该模块实现复数交错，以
在非活动输入周期内共享乘法器。对于
复数输入和复数系数，该模块至少需要
*L*×3 个周期才能使用单个乘法器实现
滤波器。对于具有
实数系数的复数输入或具有实数输入的复数系数，
该模块至少需要 *L*×2 个周期才能
使用单个乘法器实现滤波器。

该模块在应用
系数优化时可能会移除乘法器，因此滤波器的实际
*M* 和 *N* 值
可能低于指定
值。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Partly serial
systolic`，并将 **Specify
serialization factor as** 设置为
`Maximum number of
multipliers`。

当您指定
多通道系数时，不能使用此参数。请改用 **Number
of cycles** 参数。

### **Optimize symmetric coefficients** — 在基于帧的输入下为对称系数共享乘法器 on（默认）| off

*自 R2025a 起*

在基于帧的输入数据所使用的多相滤波器架构中，
启用跨对称系数共享乘法器。此优化可减少
延迟并将乘法器数量减半。

对称滤波器系数的多相分解
不会在每个多相分支中产生对称性。例如，
如果滤波器系数为 `[1 2 3 4
4 3 2 1]`，则分解后
多相分支为 `[1 3 4 2]` 和
`[2 4 3 1]`。对称对
优化会重构系数，以恢复
多相分支上的对称性。该实现
包含一个预加法器，用于合并重构后的多相分支的输出采样。
滤波器输出与未优化实现的输出
相同。

### 数据类型

### **Rounding mode** — 用于对输出进行类型转换的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于将输出类型转换为 **Output** 参数所指定
数据类型的舍入模式。
当输入数据类型为浮点型时，该模块
忽略此参数。有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 用于对输出进行类型转换的溢出处理 `off`（默认）| `on`

用于将输出类型转换为 **Output**
参数所指定数据类型的溢出处理。当输入数据类型为浮点型时，
该模块忽略此参数。有关更多详细信息，请参阅 Overflow Handling。

### **Coefficients** — 离散 FIR 滤波器系数的数据类型 `Inherit: Same word length as input`（默认）| `<data type expression>`

当输入为定点或整数类型时，该模块
使用此参数中的规则或数据类型对滤波器系数
进行类型转换。量化会舍入到最接近的
可表示值，并在溢出时饱和。当
输入数据类型为浮点类型时，该模块
忽略此参数，并且所有内部算术都使用
与输入相同的数据类型。

此参数的推荐设置为
`Inherit: Same word length as
input`。

如果出现以下情况，该模块会返回警告或错误：

- 系数数据类型没有
  足够的小数长度来准确表示
  系数。
- 系数数据类型为无符号，
  且系数包含负值。

#### 依赖关系

要启用此参数，请将 **Coefficients
source** 设置为
`Property`。

### **Output** — 滤波器输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same word length as input` | `<data type expression>`

当输入为定点或整数类型时，该模块
使用此参数中的规则或数据类型对滤波器输出
进行类型转换。量化使用
**Rounding mode** 和
**Overflow mode** 参数的设置。当
输入数据类型为浮点型时，该模块忽略
此参数，并以与输入相同的数据类型返回输出。

该模块在每个滤波器抽头内部增加字长以实现全精度，
并将最终输出转换为
指定类型。最大最终内部数据类型
（*WF*）取决于输入数据类型
（*WI*）、系数数据类型
（*WC*）以及系数数量
（*L*），其公式为

`WF = WI +
WC +
ceil(log2(L))`。

当您指定固定的一组系数时，实际
全精度内部字长通常小于
*WF*，因为系数值
限制了潜在的增长。

当您使用可编程系数时，该模块无法
计算动态范围，并且内部数据类型始终为
*WF*。

### 控制端口

### **Enable reset input port** — 启用 reset 输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **reset** 输入端口。
reset 信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅
Hardware Control Signals
页面上的 Reset Signal 部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认）| `on`

选中此复选框以将生成的 HDL 全局复位信号连接到
数据路径寄存器。此参数不会改变模块的外观，
也不会修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位
仅清除控制路径寄存器。生成的 HDL 全局复位可以是
同步或异步，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅
Hardware Control Signals
页面上的 Reset Signal 部分。

### 实现

### **Coefficient multiplication** — 硬件中的系数乘法器实现 `Multiplier`（默认）| `CSD/Factored-CSD`

*自 R2023b 起*

默认情况下，该模块使用硬件乘法器实现系数乘法器。
选择
`CSD/Factored-CSD` 可将系数乘法器替换为 CSD 或 factored-CSD
实现。CSD 或 factored-CSD 实现使用
移位和加法运算，而不是乘法器。当您
选择 CSD 时，+/- 1 和 2 的幂的系数也会
使用移位逻辑实现。

该模块的延迟不会随乘法器
实现而改变。在任一实现中，每个乘法器周围都有相同数量的
流水线级。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 参数设置为
`Direct form transposed`。
不支持将 CSD 乘法器与 systolic 架构一起使用，
因为这可能会妨碍高效
利用 FPGA DSP 模块。

多通道或可编程滤波器不支持
CSD 实现。

### **Use multiplier for +/- 1 and power of 2 coefficients** — 硬件中特殊值系数乘法器的实现 `on`（默认）| `off`

*自 R2023b 起*

默认情况下，该模块使用硬件乘法器实现特殊值系数
乘法器。清除此复选框
可将特殊值系数乘法器替换为
移位实现。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Direct form
transposed`，并将
**Coefficient multiplication** 设置为
`Multiplier`，或将
**Filter structure** 设置为
`Direct form
systolic`。

多通道或可编程滤波器不支持
CSD 实现。
## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink accelerator 和 rapid accelerator 模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

您可以设置模块参数，以在吞吐量和资源利用率之间进行权衡。

- 为获得最高吞吐量，请选择全并行脉动或转置架构。生成的代码在每个周期接收输入数据并提供滤波后的输出数据。
- 为减少面积，请选择部分串行脉动架构。然后指定模块用于基于输入时序或资源使用情况对滤波器进行串行化的规则。要使用输入时序规则指定串行滤波器，请将 **Specify serialization factor as** 设置为 `Minimum number of cycles between valid input samples`，并将 **Number of cycles** 设置为大于或等于 `2` 的值。在这种情况下，滤波器仅接受至少相隔 **Number of cycles** 个周期的输入样本。要使用资源规则指定串行滤波器，请将 **Specify serialization factor as** 设置为 `Maximum number of multipliers`，并将 **Number of multipliers** 设置为小于滤波器系数数量的值。在这种情况下，滤波器接受至少相隔 `NumCoeffs/NumMults` 的输入样本。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

Discrete FIR Filter 模块不支持通过 HDL Coder 设置进行资源共享优化。相反，请将 **Filter structure** 参数设置为 `Partly serial systolic`，并基于输入时序或资源使用情况配置串行化因子。

## 版本历史

**在 R2017a 中引入**

### R2025a：为基于帧的输入优化对称系数

该模块优化了基于帧输入的多相滤波器架构中的对称系数乘法器。此优化减少了延迟并将乘法器数量减半。要启用此优化，请选择 **Optimize symmetric coefficients**。

### R2024a：将多通道向量输入与全并行滤波器配合使用

该模块支持 `Direct form systolic` 和 `Direct form transposed` 滤波器结构的多通道向量输入。该模块现在还支持 **Number of cycles** 小于通道数的 `Partly serial systolic` 滤波器的多通道向量输入。

### R2023b：对称滤波器的多通道优化

当您使用多通道输入数据时，该模块在奇数或偶数对称滤波器系数之间共享乘法器。要启用对称优化，所有通道的对称特性必须一致。例如，如果一个通道是偶对称的，则所有通道都必须是偶对称的。

### R2023b：针对复数乘法器的部分串行 FIR 滤波器优化

当您使用复数输入数据和/或复数系数以及单通道部分串行架构时，该模块实现复数交织以在非活动输入周期内共享乘法器。此优化使用更少的乘法器并增加滤波器的延迟。

对于复数输入和复数系数，该模块至少需要 `NumCycles = 3*FilterLength` 才能使用单个乘法器实现滤波器。对于具有实数系数的复数输入或具有实数输入的复数系数，该模块至少需要 `NumCycles = 2*FilterLength` 才能使用单个乘法器实现滤波器。如果滤波器是对称的，则有效滤波器长度为 `FilterLength/2`。

### R2023b：具有串行架构的可编程系数

该模块支持将并行系数输入端口与 `Partly serial systolic` 架构配合使用。

### R2023b：规范符号数字实现

当您使用 `Direct form transposed` 架构时，该模块提供了一个选项，用 CSD 或因式分解 CSD 实现来替换系数乘法器。CSD 或因式分解 CSD 实现使用移位和加法运算而不是乘法器。当您使用 `Direct form systolic` 或 `Direct form transposed` 时，您可以选择为值等于 1、-1 或 2 的幂的系数用移位实现替换乘法器。

多通道或可编程滤波器不支持 CSD 实现。

### R2023a：使用内存风格接口加载系数

该模块提供了可选的内存风格接口来加载系数。要使用此接口，请将 **Coefficient source** 参数设置为 `Input port (Memory interface)`。您可以将此接口与任何滤波器架构配合使用。

### R2023a：多通道支持

将系数指定为 K×L 矩阵，其中 K 是通道数，L 是滤波器长度。您可以提供 K×1 行向量形式的输入数据，或者提供通道在时间上交织的标量输入。滤波器在通道之间共享资源，即使各通道的滤波器系数不同也是如此。如果输入数据通道在有效输入样本之间有足够的周期，该模块可以将多通道滤波器实现为单个全串行 FIR 滤波器。当输入是多通道向量时，**Filter structure** 必须设置为 `Partly serial systolic`，并且 **Number of cycles** 必须等于或大于通道数。

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Discrete FIR Filter HDL Optimized，包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a：高吞吐量接口

该模块支持高吞吐量数据。您可以将输入数据作为 *N*×1 向量应用，其中 *N* 最多可达 64 个值。您不能将基于帧的输入与部分串行架构配合使用。

### R2022a：输入系数必须是行向量

当您将此模块与可编程系数配合使用时，必须以行向量（1×*N* 矩阵）形式提供系数。在 R2022a 之前，该模块接受一维数组（例如 `ones(5)`）、列向量（*M*×1 矩阵）或系数行向量。

### R2022a：基于 RAM 的部分串行架构

该模块使用基于 RAM 的部分串行架构，比以前的基于寄存器的架构使用更少的资源。未初始化的 RAM 位置可能导致 HDL 仿真开始时出现 `X` 值。您可以通过让测试初始化 RAM 或在模型配置参数中启用 **Initialize all RAM blocks** 选项来避免 `X` 值。此参数将 RAM 位置设置为 `0` 以供仿真使用，综合工具会忽略此参数。避免未初始化 RAM 位置瞬态效应的另一个选项是将复位保持 *L*/*M* 个周期，其中 *L* 是系数数量，*M* 是滤波器实现中的乘法器数量。此操作将 RAM 位置设置为零。

### R2019b：复数系数

该模块支持复值系数。如果系数和输入数据都是复数，该模块使用三个乘法器实现每个滤波器抽头。如果数据或系数中只有一个是复数，该模块为每个滤波器抽头使用两个乘法器。您可以将复数系数与所有架构以及可编程系数配合使用。

### R2019a：可编程系数

当您选择 `Direct form systolic` 架构时，该模块提供了使用输入端口指定系数的选项。您不能将可编程系数与转置或部分串行脉动架构配合使用。

### R2019a：优化对称系数

该模块提供对称和反对称系数的优化。此优化减少了乘法器数量并有效利用 FPGA DSP 资源。

在 R2018b 中，该模块仅对全并行架构执行这些优化。

### R2019a：可选复位端口

该模块为任何架构提供可选复位端口，包括具有资源共享的串行脉动架构。**reset** 端口提供数据路径寄存器的局部同步复位。

在 R2018b 中，该模块仅对全并行架构支持 **reset** 端口。

### R2019a：串行滤波器参数的更改

在 R2019a 之前，您通过设置输入时序要求来指定串行实现。从 R2019a 开始，您可以基于输入时序或资源使用情况指定串行化要求。

对于具有 *L* 个系数的滤波器，该模块实现不超过 *M* 个乘法器的串行滤波器，并要求输入样本至少相隔 *N* 个周期，使得 *L* = *N*×*M*。

| 串行滤波器要求 | R2019a 之前的配置 | R2019a 中的配置 |
| --- | --- | --- |
| 基于输入时序指定串行化规则，即 *N* 个周期。 | - 将 **Filter structure** 设置为 `Direct form systolic`。 - 选择 **Share DSP resources**。 - 将 **Sharing factor** 设置为 *N*。 | - 将 **Filter structure** 设置为 `Partly serial systolic`。 - 将 **Specify serialization factor as** 设置为 `Minimum number of cycles between valid input samples`。 - 将 **Number of cycles** 设置为 *N*。 |
| 基于资源使用情况指定串行化规则，即 *M* 个乘法器。 | R2019a 之前不支持按资源使用情况串行化。但是，您可以根据乘法器需求计算 *N*。 - 将 **Filter structure** 设置为 `Direct form systolic`。 - 选择 **Share DSP resources**。 - 将 **Sharing factor** 设置为 `ceil(NumCoeffs/M)`。 | - 将 **Filter structure** 设置为 `Partly serial systolic`。 - 将 **Specify serialization factor as** 设置为 `Maximum number of multipliers`。 - 将 **Number of multipliers** 设置为 *M*。 |

### R2018b：转置架构

该模块提供了选择直接型转置架构的选项。

### R2018b：并行滤波器架构的更改

- **validIn** 端口是必需的。**Enable valid input port** 参数不再可用。
- 当您选择 **Share DSP resources** 时，**ready** 端口启用；当您清除 **Share DSP resources** 时，**ready** 端口禁用。**Enable ready output port** 参数不再可用。
- 当您选择 `Direct form systolic` 而未启用 **Share DSP resources** 时，该模块实现了比先前版本改进的全并行架构。此架构可能具有与先前版本不同的延迟。使用 **validOut** 信号与并行延迟路径对齐。使用此架构时，默认全局 HDL 复位现在仅清除控制路径寄存器。先前版本将全局 HDL 复位连接到数据路径寄存器和控制路径寄存器。此更改提高了硬件性能并降低了使用的资源。要实现与先前版本相同的全并行架构，请选择 **Share DSP resources** 并将 **Sharing factor** 设置为 `1`。
- 当您选择 `Direct form systolic`、选择 **Share DSP resources** 并使用任何 **Sharing factor** 时，实现的滤波器具有与先前版本相同的延迟并使用相同的硬件资源。此架构的复位行为也与先前版本相同。

## 描述

有限脉冲响应滤波器

Discrete FIR Filter 模块为 HDL 代码生成建模优化的有限脉冲响应滤波器架构。该模块接受标量或基于帧的输入，支持多通道输入，并通过使用并行接口或内存接口提供可编程系数选项。该模块提供具有输入和输出控制信号的硬件友好接口。为了提供生成 HDL 代码的周期精确仿真，该模块对架构延迟（包括流水线寄存器和资源共享）进行建模。

该模块提供三种滤波器结构。

- 直接型脉动架构提供全并行实现，可有效利用 Intel® 和 AMD® DSP 模块。
- 直接型转置架构是全并行实现，适用于 FPGA 和 ASIC 应用。
- 部分串行脉动架构提供可配置的串行实现，可有效利用 FPGA DSP 模块。

对于将乘法器、流水线寄存器和预加法器与 FPGA 供应商的 DSP 配置相匹配的滤波器实现，请在生成 HDL 代码时指定目标器件。

所有单通道滤波器结构都会移除零值系数的乘法器，例如半带滤波器和希尔伯特变换中的乘法器。该模块还提供了一个选项，可以在没有乘法器的情况下实现 +/- 1 和 2 的幂系数，以及一个选项，用 CSD 或因式分解 CSD 逻辑实现所有系数。滤波器为对称和反对称系数共享乘法器。多通道滤波器不会移除零值系数的乘法器。多通道滤波器在通道之间共享资源，即使各通道的滤波器系数不同也是如此。

有效输入数据与相应有效输出数据之间的延迟取决于滤波器结构、串行化选项、系数数量以及系数值是否提供优化机会。有关结构和延迟的详细信息，请参阅 FIR Filter Architectures for FPGAs and ASICs。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
