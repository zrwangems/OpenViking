---
type: simulink-block
title: 'Discrete FIR Filter'
family: 'filtering'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'discretefirfilter'
documentation_source_path: '../dsphdl/ref/discretefirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete FIR Filter

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量 | 行向量

输入数据，指定为实数或复数值的标量、列向量或行向量。使用列向量可通过并行处理样本提高吞吐量。

您可以使用行向量 `[c1 c2 c3]` 表示单个周期上多个通道的输入样本，也可以提供通道交织的标量多通道数据：`c1` 数据样本在第 1 个周期，`c2` 数据样本在第 2 个周期，`c3` 数据样本在第 3 个周期。这些通道可以具有独立的滤波器系数。
 *（自 R2023a 起）*

行向量和标量多通道数据信号的波形。

*在 R2023a 和 R2023b 中：仅当输入之间具有至少与通道数一样多的无效周期时，才能使用多通道行向量输入。当输入是多通道向量时，**Filter structure** 必须设置为 `Partly serial systolic`，并且 **Number of cycles** 必须等于或大于通道数。此时间允许模块实现一种部分串行架构，在通道之间共享资源。*

不支持将基于帧（列向量）输入与多通道系数一起使用。要实现高吞吐量多通道滤波器，可以使用 For Each 模块为每个通道实现高吞吐量滤波器。此实现无法在通道之间共享资源。

行向量或列向量的大小必须小于或等于 64 个元素。要实现具有 64 个以上通道的多通道滤波器，必须使用交织标量输入。

当输入数据类型为整数类型或定点类型时，模块使用定点算术进行内部计算，并在 **Data Types** 选项卡上提供参数以自定义数据类型。当输入数据类型为浮点类型时，模块使用该输入浮点类型进行内部计算和输出数据类型。

该软件支持用于仿真的 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** Yes

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### **coeff** — 滤波器系数（Parallel interface）实数或复数行向量

滤波器系数，指定为实数或复数值的行向量。您可以随时更改输入系数。当使用标量输入数据时，系数向量的大小取决于 **Coefficients prototype** 参数中指定的样本系数的大小和对称性。原型指定一个样本系数向量，该向量代表预期输入系数的对称性和零值位置。模块使用原型通过为对称或反对称系数共享乘法器，以及通过移除零值系数的乘法器来优化滤波器。因此，在端口上仅提供非重复系数。例如，如果将 **Coefficients prototype** 参数设置为对称 14 抽头滤波器，则模块期望 **coeff** 输入端口上有一个包含 7 个值的向量。对于非重复的零值系数，您仍必须在输入 **coeff** 向量中提供零。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 移除零值系数的乘法器。在 **coeff** 输入端口，指定与原型大小相同的向量。

如果输入 **data** 是定点类型，则 **coeff** 值也必须是定点类型。如果输入 **data** 是浮点数据类型，则 **coeff** 值必须具有相同的数据类型。

该软件支持用于仿真的 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **coeff** — 滤波器系数（Memory interface）实数或复数标量

*自 R2023a 起*

滤波器系数，指定为要写入内部存储器的实数或复数值标量。若要将单个系数值加载到内部存储器，请在 **caddr** 端口上指定具有对应地址的 **coeff** 值，并在 **cwren** 端口上指定使能信号。您可以随时更改输入系数。

波形显示使用存储器接口将一组系数写入滤波器

当您将新系数写入存储器时，模块会忽略任何输入数据，但仍会返回 `dataOut` 和 `validOut`，直到它清空滤波器流水线。在 **cdone** 设置为 `1`（`true`）后的下一个周期，模块恢复接受输入。

波形显示滤波器在通过存储器接口接收新系数时停止处理输入数据

系数存储器具有与 **Coefficients prototype** 参数大小相同的地址数。原型指定一个样本系数向量，该向量代表预期输入系数的对称性和零值位置。当使用标量输入数据时，模块使用原型通过为对称或反对称系数共享乘法器，以及通过移除零值系数的乘法器来优化滤波器。您必须将整组系数写入存储器，包括对称或零值系数。例如，如果将 **Coefficients prototype** 参数设置为对称 14 抽头滤波器，则必须向存储器接口写入 14 个值。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 参数来移除零值系数的乘法器。系数存储器具有与原型大小相同的位置数。

如果输入 **data** 是定点类型，则 **coeff** 值也必须是定点类型。如果输入 **data** 是浮点数据类型，则 **coeff** 值必须具有相同的数据类型。

该软件支持用于仿真的 `double` 和 `single` 数据类型，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **caddr** — 滤波器系数地址（Memory interface）标量

*自 R2023a 起*

将滤波器系数地址指定为标量整数值，表示为小数位为零的无符号定点类型。模块根据 **Coefficients prototype** 参数值中唯一系数的数量推导此整数值的大小以及内部存储器的大小。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `fixdt(0,N,0)`

### **cwren** — 滤波器系数写使能（Memory interface）标量

*自 R2023a 起*

将此输入设置为 `1`（`true`），以将 **coeff** 端口上的值写入内部存储器中的 **caddr** 位置。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `Boolean`

### **cdone** — 滤波器系数写入完成（Memory interface）标量

*自 R2023a 起*

将此输入设置为 `1`（`true`），以指示当前端口值将最终系数值写入存储器。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Memory interface)`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获要处理的数据。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选择 **Enable reset input port**。

**数据类型：** `Boolean`
### 输出

### **data** — 滤波后的输出数据 标量 | 列向量 | 行向量

滤波后的输出数据，以实数或复数值的标量、列向量或行向量返回。输出的维度与输入的维度匹配。当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**Data Types** 选项卡上的 **Output** 参数控制输出数据类型。

**数据类型：** `fixed point` | `single` | `double`
**复数支持：** Yes

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据 标量

控制信号，指示模块已准备好在下一个周期接收新的输入数据样本。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块将在下一个时间步忽略任何输入数据。

使用部分串行架构时，模块一次处理一个样本。如果您的设计等待此模块将 **ready** 返回为 `0`（`false`）后再将输入 **valid** 设置为 `0`（`false`），则一个额外的输入数据周期会到达端口。模块在处理当前数据时存储此额外数据，并且在您的模型处理此额外输入数据之前不会将 **ready** 设置为 `1`（`true`）。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Partly serial systolic`。

**数据类型：** `Boolean`

## 参数

### Main

### **Coefficient source** — 滤波器系数的来源 `Property`（默认） | `Input port (Parallel interface)` | `Input port (Memory interface)`

您可以将恒定滤波器系数作为参数输入，通过输入端口提供时变滤波器系数，或通过存储器式接口提供时变系数。

不能将可编程系数与多通道数据一起使用。

当您选择 `Input port (Parallel interface)` 时，**coeff** 端口会出现在模块上。

当您选择 `Input port (Memory interface)` 时，模块上会出现存储器式接口。此接口包括 **coeff**、**caddr**、**cwren** 和 **cdone** 端口。

选择 `Input port (Parallel interface)` 或 `Input port (Memory interface)` 会启用 **Coefficients prototype** 参数。指定原型以使模块能够根据系数值优化滤波器实现。

当您将可编程系数与基于帧的输入一起使用时，模块不会针对系数对称性优化滤波器。此外，更改系数值后的输出可能与标量情况下的输出不完全匹配。出现此差异是因为与标量实现相比，子滤波器计算相对于输入系数值是在不同时间执行的。

#### 依赖关系

*在 R2023b 之前：要使用 `Input port (Parallel interface)`，请将 **Filter structure** 参数设置为 `Direct form systolic` 或 `Direct form transposed`。*

### **Coefficients** — 离散 FIR 滤波器系数 `[0.5, 0.5]`（默认） | 行向量 | 多通道矩阵

离散 FIR 滤波器系数，指定为实数或复数值的行向量。您可以使用 *K*×*L* 的实数或复数值矩阵指定多通道系数，其中 *K* 是通道数，*L* 是滤波器长度。要启用对称性优化，所有通道的对称特性必须一致。例如，如果一个通道是偶对称的，则所有通道都必须是偶对称的。

您还可以将系数指定为工作区变量或对滤波器设计函数的调用。当输入数据类型为浮点类型时，模块将系数转换为与输入相同的数据类型。当输入数据类型为整数类型或定点类型时，您可以在 **Data Types** 选项卡上设置系数的数据类型。

**示例：** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0 0])`

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

### **Coefficients prototype** — 原型滤波器系数 `[]`（默认） | 实数或复数向量

原型滤波器系数，指定为实数或复数值的向量。原型指定一个样本系数向量，该向量代表预期输入系数的对称性和零值位置。如果所有输入系数向量具有相同的对称性和零值系数位置，请将 **Coefficients prototype** 设置为其中一个向量。模块使用原型通过为对称或反对称系数共享乘法器，以及通过移除零值系数的乘法器来优化滤波器。

当使用基于帧的输入数据时，模块不会针对系数对称性优化滤波器。模块仍使用 **Coefficients prototype** 参数来移除零值系数的乘法器。

| Coefficient Source | Input Size | If No Prototype |
| --- | --- | --- |
| `Input port (Parallel interface)` | 当您使用标量输入数据时，系数优化会影响 **coeff** 端口上向量的预期大小。在端口上仅提供非重复系数。例如，如果将 **Coefficients prototype** 参数设置为对称 14 抽头滤波器，则模块在每对重复系数之间共享一个乘法器，因此模块期望 **coeff** 端口上有一个包含 7 个值的向量。对于非重复的零值系数，您仍必须在输入 **coeff** 向量中提供零。当您使用基于帧的输入数据时，请指定与原型大小相同的 **coeff** 向量。 | 如果您的系数未知或预计不共享对称性或零值位置，可以将 **Coefficients prototype** 设置为 `[]`。 |
| `Input port (Memory interface)` | 写入与原型大小相同数量的系数值。 | **Coefficients prototype** 不能为空。模块使用原型确定系数存储器的大小。如果您的系数未知或预计不共享对称性或零值位置，请将 **Coefficients prototype** 设置为与预期系数长度相同的向量，该向量不包含对称性或零值，例如 `[1:1:NumCoeffs]`。 |

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Input port (Parallel interface)` 或 `Input port (Memory interface)`。

### **Filter structure** — HDL 滤波器架构 `Direct form systolic`（默认） | `Direct form transposed` | `Partly serial systolic`

将 HDL 滤波器架构指定为以下结构之一：

- `Direct form systolic` — 此架构提供完全并行的滤波器实现，可高效利用 Intel 和 AMD DSP 模块。有关架构详细信息，请参阅 Fully Parallel Systolic Architecture。当您使用此架构指定多通道系数时（使用交织输入样本），模块将通道系数交织到单个并行滤波器上。
- `Direct form transposed` — 此架构是适用于 FPGA 和 ASIC 应用的完全并行实现。有关架构详细信息，请参阅 Fully Parallel Transposed Architecture。当您使用此架构指定多通道系数时（使用交织输入样本），模块将通道系数交织到单个并行滤波器上。
- `Partly serial systolic` — 此架构提供串行滤波器实现，并提供吞吐量与资源利用率之间折衷的选项。该架构可高效利用 Intel 和 AMD DSP 模块。模块实现具有 *M* 个乘法器的串行 *L* 系数滤波器，并要求输入样本至少相隔 *N* 个周期，使得 *L* = *N*×*M*。您可以指定 *M* 或 *N*。对于此实现，模块提供输出 **ready** 端口，指示模块何时准备好接收新输入数据。有关架构详细信息，请参阅 Partly Serial Systolic Architecture (1 < N < L) 和 Fully Serial Systolic Architecture (N ≥ L)。不能将基于帧的输入与部分串行架构一起使用。

  当您使用串行架构指定多通道系数时，必须将串行化因子指定为有效输入样本之间的周期数。

  对于在通道上交织的标量多通道输入，模块实现以下串行架构：

  - 当 *N* < *L* 时：具有 *L*/*N* 个乘法器的部分串行滤波器。
  - 当 *N* >= *L* 时：完全串行滤波器。

  对于 1×*K* 向量的多通道输入，其中 *K* 是通道数，模块实现以下串行架构：

  - 当 *N* = 1 时：完全并行滤波器的滤波器组。
  - 当 1 < *N* < *K* 时：部分串行滤波器的滤波器组。*(自 R2024a 起)*
  - 当 *N* = *K* 时：通道系数交织的完全并行滤波器。
  - 当 *K* < *N* < *L*×*K* 时：具有 *L*×*K*/*N* 个乘法器的部分串行滤波器。
  - 当 *N* >= *L*×*K* 时：完全串行滤波器。

如果任何滤波器是对称的，则该架构会为匹配的系数共享乘法器，因此 *L* 实际上变为 `L/2`。要为多通道滤波器启用对称性优化，所有通道的对称特性必须一致。

所有单通道实现都会移除零值系数的乘法器。多通道滤波器不会针对零值系数进行优化。滤波器为对称和反对称系数共享乘法器。多通道滤波器会在通道之间共享资源，即使各通道的滤波器系数不同。

### **Specify serialization factor as** — 定义串行实现的规则 `Minimum number of cycles between valid input samples`（默认） | `Maximum number of multipliers`

您可以指定模块用于串行化滤波器的规则，可以是：

- `Minimum number of cycles between valid input samples` — 使用 **Number of cycles** 参数指定对输入数据时序的要求。
- `Maximum number of multipliers` — 使用 **Number of multipliers** 参数指定对资源使用的要求。当您具有多通道系数时，不支持此选项。

对于具有 *L* 个系数的滤波器，模块实现具有不超过 *M* 个乘法器的串行滤波器，并要求输入样本至少相隔 *N* 个周期，使得 *L* = *N*×*M*。当模块应用系数优化时，可能会移除乘法器，因此滤波器实现的实际 *M* 或 *N* 值可能低于指定值。

如果滤波器是对称的，则该架构会为匹配的系数共享乘法器，因此实际上 `L = L/2`。

当您将复数输入数据和/或复数系数与单通道部分串行架构一起使用时，模块实现复数交织，以在非活动输入周期内共享乘法器。对于复数输入和复数系数，模块至少需要 *L*×3 个周期才能使用单个乘法器实现滤波器。对于具有实数系数的复数输入，或具有实数输入的复数系数，模块至少需要 *L*×2 个周期才能使用单个乘法器实现滤波器。 *(自 R2023b 起)*

#### 依赖关系

要启用此参数，请将 **Filter structure** 参数设置为 `Partly serial systolic`。

### **Number of cycles** — 输入时序的串行化要求 `2`（默认） | 正整数

输入时序的串行化要求，指定为正整数。此参数表示 *N*，即有效输入样本之间的最小周期数。在这种情况下，模块计算 *M* = *L*/*N*。要实现完全串行架构，请将 **Number of cycles** 设置为大于滤波器长度 *L* 的值，或设置为 `Inf`。要为具有 1×*K* 向量输入的多通道滤波器实现完全串行架构，请将 **Number of cycles** 设置为大于 *L*×*K* 的值，其中 *K* 是通道数。

要为具有复数输入和复数系数的单通道滤波器实现完全串行架构，请将 **Number of cycles** 设置为大于 *L*×3。如果您具有实数系数的复数输入或实数输入的复数系数，请将 **Number of cycles** 设置为大于 *L*×2。

如果滤波器是对称的，则该架构会为匹配的系数共享乘法器，因此实际上 `L = L/2`。要为多通道滤波器启用对称性优化，所有通道的对称特性必须一致。

当模块应用系数优化时，可能会移除乘法器，因此滤波器的实际 *M* 和 *N* 值可能低于您指定的值。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Partly serial systolic`，并将 **Specify serialization factor as** 设置为 `Minimum number of cycles between valid input samples`。

### **Number of multipliers** — 资源使用的串行化要求 `2`（默认） | 正整数

资源使用的串行化要求，指定为正整数。此参数表示 *M*，即滤波器实现中的最大乘法器数。在这种情况下，模块计算 *N* = *L*/*M*。如果输入数据是复数，模块为滤波器的实部分配 `floor(M/2)` 个乘法器，为滤波器的虚部分配 `floor(M/2)` 个乘法器。要实现完全串行架构，请将 **Number of multipliers** 设置为 `1`。

如果滤波器是对称的，则该架构会为匹配的系数共享乘法器，因此实际上 `L = L/2`。

当您将复数输入数据和/或复数系数与单通道部分串行架构一起使用时，模块实现复数交织，以在非活动输入周期内共享乘法器。对于复数输入和复数系数，模块至少需要 *L*×3 个周期才能使用单个乘法器实现滤波器。对于具有实数系数的复数输入，或具有实数输入的复数系数，模块至少需要 *L*×2 个周期才能使用单个乘法器实现滤波器。

当模块应用系数优化时，可能会移除乘法器，因此滤波器的实际 *M* 和 *N* 值可能低于指定值。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Partly serial systolic`，并将 **Specify serialization factor as** 设置为 `Maximum number of multipliers`。

当您指定多通道系数时，不能使用此参数。请改用 **Number of cycles** 参数。

### **Optimize symmetric coefficients** — 对基于帧输入的对称系数共享乘法器 on（默认） | off

*自 R2025a 起*

在使用基于帧输入数据时所使用的多相滤波器架构中，启用跨对称系数共享乘法器。此优化可减少延迟并将乘法器数量减半。

对称滤波器系数的多相分解不会在每个多相分支中产生对称性。例如，如果滤波器系数为 `[1 2 3 4 4 3 2 1]`，则分解后多相分支为 `[1 3 4 2]` 和 `[2 4 3 1]`。对称对优化会重构系数，以恢复多相分支上的对称性。该实现包括一个预加法器，用于组合重构后的多相分支的输出样本。滤波器输出与非优化实现的输出相同。

### Data Types

### **Rounding mode** — 将输出类型转换时的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

将输出类型转换为 **Output** 参数所指定数据类型时的舍入模式。当输入数据类型为浮点类型时，模块忽略此参数。有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 将输出类型转换时的溢出处理 `off`（默认） | `on`

将输出类型转换为 **Output** 参数所指定数据类型时的溢出处理。当输入数据类型为浮点类型时，模块忽略此参数。有关更多详细信息，请参阅 Overflow Handling。

### **Coefficients** — 离散 FIR 滤波器系数的数据类型 `Inherit: Same word length as input`（默认） | `<data type expression>`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型转换滤波器系数。量化会舍入到最接近的可表示值，并在溢出时饱和。当输入数据类型为浮点类型时，模块忽略此参数，所有内部算术使用与输入相同的数据类型。

此参数的推荐设置为 `Inherit: Same word length as input`。

如果出现以下情况，模块会返回警告或错误：

- 系数数据类型没有足够的小数长度来准确表示系数。
- 系数数据类型为无符号，且系数包含负值。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

### **Output** — 滤波器输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same word length as input` | `<data type expression>`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型转换滤波器输出。量化使用 **Rounding mode** 和 **Overflow mode** 参数的设置。当输入数据类型为浮点类型时，模块忽略此参数，并以与输入相同的数据类型返回输出。

模块在每个滤波器抽头内部增加字长以实现全精度，并将最终输出转换为指定类型。最大最终内部数据类型（*WF*）取决于输入数据类型（*WI*）、系数数据类型（*WC*）和系数数量（*L*），由下式给出：

`WF = WI + WC + ceil(log2(L))`。

当您指定固定的系数集时，实际的全精度内部字长通常小于 *WF*，因为系数值限制了潜在增长。

当您使用可编程系数时，模块无法计算动态范围，并且内部数据类型始终为 *WF*。

### Control Ports

### **Enable reset input port** — 启用 reset 输入端口的选项 `off`（默认） | `on`

选中此复选框以启用 **reset** 输入端口。reset 信号对数据路径寄存器实现本地同步复位。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认） | `on`

选中此复选框以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观，也不会修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步，具体取决于模型 Configuration Parameters 中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

### Implementation

### **Coefficient multiplication** — 硬件中的系数乘法器实现 `Multiplier`（默认） | `CSD/Factored-CSD`

*自 R2023b 起*

默认情况下，模块使用硬件乘法器实现系数乘法器。选择 `CSD/Factored-CSD` 以将系数乘法器替换为 CSD 或 factored-CSD 实现。CSD 或 factored-CSD 实现使用移位和加法运算，而不是乘法器。当您选择 CSD 时，+/- 1 和 2 的幂的系数也使用移位逻辑实现。

模块的延迟不会随乘法器实现而变化。在任一实现中，每个乘法器周围具有相同数量的流水线级。

#### 依赖关系

要启用此参数，请将 **Filter structure** 参数设置为 `Direct form transposed`。不支持将 CSD 乘法器与 systolic 架构一起使用，因为这可能会妨碍高效利用 FPGA DSP 模块。

多通道或可编程滤波器不支持 CSD 实现。

### **Use multiplier for +/- 1 and power of 2 coefficients** — 硬件中特殊值系数乘法器实现 `on`（默认） | `off`

*自 R2023b 起*

默认情况下，模块使用硬件乘法器实现特殊值系数乘法器。清除此复选框以将特殊值系数乘法器替换为移位实现。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form transposed`，并将 **Coefficient multiplication** 设置为 `Multiplier`，或者将 **Filter structure** 设置为 `Direct form systolic`。

多通道或可编程滤波器不支持 CSD 实现。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

您可以设置模块参数，以在吞吐量和资源利用率之间进行折衷。

- 为获得最高吞吐量，请选择完全并行的 systolic 或 transposed 架构。生成的代码在每个周期接受输入数据并提供滤波后的输出数据。
- 为减小面积，请选择 partly serial systolic 架构。然后指定模块用于基于输入时序或资源使用来串行化滤波器的规则。要使用输入时序规则指定串行滤波器，请将 **Specify serialization factor as** 设置为 `Minimum number of cycles between valid input samples`，并将 **Number of cycles** 设置为大于或等于 `2` 的值。在这种情况下，滤波器仅接受至少相隔 **Number of cycles** 个周期的输入样本。要使用资源规则指定串行滤波器，请将 **Specify serialization factor as** 设置为 `Maximum number of multipliers`，并将 **Number of multipliers** 设置为小于滤波器系数数量的值。在这种情况下，滤波器接受至少相隔 `NumCoeffs/NumMults` 的输入样本。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

Discrete FIR Filter 模块不支持通过 HDL Coder 设置进行资源共享优化。请改为将 **Filter structure** 参数设置为 `Partly serial systolic`，并基于输入时序或资源使用配置串行化因子。

## 版本历史

**在 R2017a 中引入**

### R2025a：为基于帧输入优化对称系数

模块优化基于帧输入所使用的多相滤波器架构中的对称系数乘法器。此优化可减少延迟并将乘法器数量减半。要启用此优化，请选择 **Optimize symmetric coefficients**。

### R2024a：将多通道向量输入与完全并行滤波器一起使用

模块支持用于 `Direct form systolic` 和 `Direct form transposed` 滤波器结构的多通道向量输入。模块现在还支持 **Number of cycles** 小于通道数的 `Partly serial systolic` 滤波器的多通道向量输入。

### R2023b：对称滤波器的多通道优化

当您使用多通道输入数据时，模块在奇对称或偶对称滤波器系数之间共享乘法器。要启用对称性优化，所有通道的对称特性必须一致。例如，如果一个通道是偶对称的，则所有通道都必须是偶对称的。

### R2023b：用于复数乘法器的部分串行 FIR 滤波器优化

当您将复数输入数据和/或复数系数与单通道部分串行架构一起使用时，模块实现复数交织，以在非活动输入周期内共享乘法器。此优化使用更少的乘法器并增加滤波器的延迟。

对于复数输入和复数系数，模块至少需要 `NumCycles = 3*FilterLength` 才能使用单个乘法器实现滤波器。对于具有实数系数的复数输入，或具有实数输入的复数系数，模块至少需要 `NumCycles = 2*FilterLength` 才能使用单个乘法器实现滤波器。如果滤波器是对称的，则有效滤波器长度为 `FilterLength/2`。

### R2023b：具有串行架构的可编程系数

模块支持将并行系数输入端口与 `Partly serial systolic` 架构一起使用。

### R2023b：规范符号数字实现

当您使用 `Direct form transposed` 架构时，模块提供将系数乘法器替换为 CSD 或 factored-CSD 实现的选项。CSD 或 factored-CSD 实现使用移位和加法运算，而不是乘法器。当您使用 `Direct form systolic` 或 `Direct form transposed` 时，可以选择对值为 1、-1 或 2 的幂的系数用移位实现替换乘法器。

多通道或可编程滤波器不支持 CSD 实现。

### R2023a：使用存储器式接口加载系数

此模块提供可选的存储器式接口来加载系数。要使用此接口，请将 **Coefficient source** 参数设置为 `Input port (Memory interface)`。您可以将此接口与任何滤波器架构一起使用。

### R2023a：多通道支持

将系数指定为 K×L 矩阵，其中 K 是通道数，L 是滤波器长度。您可以提供 K×1 行向量形式的输入数据，或以通道在时间上交织的标量输入形式提供。滤波器在通道之间共享资源，即使各通道的滤波器系数不同。如果输入数据通道在有效输入样本之间有足够的周期，模块可以将多通道滤波器实现为单个完全串行 FIR 滤波器。当输入是多通道向量时，**Filter structure** 必须设置为 `Partly serial systolic`，并且 **Number of cycles** 必须等于或大于通道数。

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Discrete FIR Filter HDL Optimized，并包含在 DSP System Toolbox™ **DSP System Toolbox HDL Support** 库中。

### R2022a：高吞吐量接口

此模块支持高吞吐量数据。您可以将输入数据作为 *N*×1 向量应用，其中 *N* 最多可为 64 个值。不能将基于帧的输入与部分串行架构一起使用。

### R2022a：输入系数必须为行向量

当您将可编程系数与此模块一起使用时，必须以行向量（1×*N* 矩阵）形式提供系数。在 R2022a 之前，模块接受一维数组（例如 `ones(5)`）、列向量（*M*×1 矩阵）或系数行向量。

### R2022a：基于 RAM 的部分串行架构

此模块使用基于 RAM 的部分串行架构，与以前的基于寄存器的架构相比，该架构使用更少的资源。未初始化的 RAM 位置可能导致 HDL 仿真开始时出现 `X` 值。您可以通过让测试初始化 RAM，或在模型配置参数中启用 **Initialize all RAM blocks** 选项来避免 `X` 值。此参数在仿真中将 RAM 位置设置为 `0`，并由综合工具忽略。避免未初始化 RAM 位置瞬态影响的另一种方法是保持复位 *L*/*M* 个周期，其中 *L* 是系数数量，*M* 是滤波器实现中的乘法器数量。此操作将 RAM 位置设置为零。

### R2019b：复数系数

模块支持复数值系数。如果系数和输入数据均为复数，则模块使用三个乘法器实现每个滤波器抽头。如果数据或系数中仅一个为复数而不是两者均为复数，则模块为每个滤波器抽头使用两个乘法器。您可以将复数系数与所有架构以及可编程系数一起使用。

### R2019a：可编程系数

当您选择 `Direct form systolic` 架构时，模块提供使用输入端口指定系数的选项。不能将可编程系数与 transposed 或 partly serial systolic 架构一起使用。

### R2019a：优化对称系数

模块提供对称和反对称系数的优化。此优化减少乘法器数量，并高效利用 FPGA DSP 资源。

在 R2018b 中，模块仅对完全并行架构执行这些优化。

### R2019a：可选 reset 端口

模块为任何架构提供可选 reset 端口，包括具有资源共享的串行 systolic 架构。**reset** 端口提供数据路径寄存器的本地同步复位。

在 R2018b 中，模块仅对完全并行架构支持 **reset** 端口。

### R2019a：串行滤波器参数的更改

在 R2019a 之前，您通过设置输入时序要求来指定串行实现。从 R2019a 开始，您可以基于输入时序或资源使用指定串行化要求。

对于具有 *L* 个系数的滤波器，模块实现具有不超过 *M* 个乘法器的串行滤波器，并要求输入样本至少相隔 *N* 个周期，使得 *L* = *N*×*M*。

| Serial Filter Requirement | Configuration Before R2019a | Configuration in R2019a |
| --- | --- | --- |
| 指定基于输入时序的串行化规则，即 *N* 个周期。 | - 将 **Filter structure** 设置为 `Direct form systolic`。 - 选择 **Share DSP resources**。 - 将 **Sharing factor** 设置为 *N*。 | - 将 **Filter structure** 设置为 `Partly serial systolic`。 - 将 **Specify serialization factor as** 设置为 `Minimum number of cycles between valid input samples`。 - 将 **Number of cycles** 设置为 *N*。 |
| 指定基于资源使用的串行化规则，即 *M* 个乘法器。 | R2019a 之前不支持按资源使用进行串行化。但是，您可以根据乘法器要求计算 *N*。 - 将 **Filter structure** 设置为 `Direct form systolic`。 - 选择 **Share DSP resources**。 - 将 **Sharing factor** 设置为 `ceil(NumCoeffs/M)`。 | - 将 **Filter structure** 设置为 `Partly serial systolic`。 - 将 **Specify serialization factor as** 设置为 `Maximum number of multipliers`。 - 将 **Number of multipliers** 设置为 *M*。 |

### R2018b：Transposed 架构

模块提供选择 direct form transposed 架构的选项。

### R2018b：并行滤波器架构的更改

- **validIn** 端口是必需的。**Enable valid input port** 参数不再可用。
- 当您选择 **Share DSP resources** 时，**ready** 端口启用；当您清除 **Share DSP resources** 时，**ready** 端口禁用。**Enable ready output port** 参数不再可用。
- 当您选择 `Direct form systolic` 而未启用 **Share DSP resources** 时，与以前的版本相比，模块实现改进的完全并行架构。此架构的延迟可能与以前的版本不同。使用 **validOut** 信号与并行延迟路径对齐。使用此架构时，默认的全局 HDL 复位现在仅清除控制路径寄存器。以前的版本将全局 HDL 复位连接到数据路径寄存器和控制路径寄存器。此更改提高了硬件性能并降低了资源使用。要实现与以前版本相同的完全并行架构，请选择 **Share DSP resources** 并将 **Sharing factor** 设置为 `1`。
- 当您选择 `Direct form systolic`、选择 **Share DSP resources** 并使用任何 **Sharing factor** 时，所实现的滤波器具有与以前版本相同的延迟并使用相同的硬件资源。此架构的复位行为也与以前版本相同。

## 描述

有限脉冲响应滤波器

Discrete FIR Filter 模块对针对 HDL 代码生成优化的有限脉冲响应滤波器架构进行建模。该模块接受标量或基于帧的输入，支持多通道输入，并通过使用并行接口或存储器接口提供可编程系数选项。该模块提供具有输入和输出控制信号的硬件友好接口。为了提供生成 HDL 代码的周期精确仿真，该模块对架构延迟（包括流水线寄存器和资源共享）进行建模。

该模块提供三种滤波器结构。

- direct form systolic 架构提供完全并行实现，可高效利用 Intel® 和 AMD® DSP 模块。
- direct form transposed 架构是适用于 FPGA 和 ASIC 应用的完全并行实现。
- partly serial systolic 架构提供可配置的串行实现，可高效利用 FPGA DSP 模块。

为使滤波器实现中的乘法器、流水线寄存器和预加法器与 FPGA 供应商的 DSP 配置匹配，请在生成 HDL 代码时指定目标器件。

所有单通道滤波器结构都会移除零值系数的乘法器，例如在半带滤波器和 Hilbert 变换中。该模块还提供选项以在不使用乘法器的情况下实现 +/- 1 和 2 的幂系数，并提供使用 CSD 或 factored-CSD 逻辑实现所有系数的选项。滤波器为对称和反对称系数共享乘法器。多通道滤波器不会移除零值系数的乘法器。多通道滤波器会在通道之间共享资源，即使各通道的滤波器系数不同。

有效输入数据与对应有效输出数据之间的延迟取决于滤波器结构、串行化选项、系数数量以及系数值是否提供优化机会。有关结构和延迟的详细信息，请参阅 FIR Filter Architectures for FPGAs and ASICs。

**注意**

您还可以通过使用 DSP HDL IP Designer App 为此硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该 App 提供与 Simulink 模块相同的接口和配置选项。
