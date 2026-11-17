---
type: simulink-block
title: 'Biquad Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'biquadfilter'
documentation_source_path: 'ref/biquadfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Biquad Filter

## 端口
```yaml
ports:
- name: In
  summary: 数据输入向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Num
  summary: 分子系数矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Den
  summary: 分母系数矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: g
  summary: 缩放值行向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Out
  summary: 滤波后的输出向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
```

### 输入

### **In** — 数据输入向量 | 矩阵

输入到模块的数据，指定为向量或矩阵。此模块支持可变大小输入信号，使您能够在仿真期间更改输入帧大小（行数）。但是，通道数（列数）必须保持不变。

如果输入为定点，则它必须为带二进制小数点定标的有符号定点。

除非您将 **Coefficient source** 设置为 `Input port(s)`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是

### **Num** — 分子系数矩阵

双二阶滤波器的分子系数，指定为 3×*N* 矩阵，其中 *N* 是双二阶滤波器节的数量。

如果 **Num** 为定点，则它必须为带二进制小数点定标的有符号定点。

#### 依赖关系

此端口仅在您将 **Coefficient source** 设置为 `Input port(s)` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **Den** — 分母系数矩阵

双二阶滤波器的分母系数，指定为 2×*N* 矩阵，其中 *N* 是双二阶滤波器节的数量。

如果 **Den** 为定点，则它必须为带二进制小数点定标的有符号定点。

#### 依赖关系

此端口仅在您将 **Coefficient source** 设置为 `Input port(s)` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **g** — 缩放值行向量

双二阶滤波器的缩放值，指定为 1×(*N*+1) 向量，其中 *N* 是双二阶滤波器节的数量。

如果 **g** 为定点，则它必须为带二进制小数点定标的有符号定点。

#### 依赖关系

此端口仅在您将 **Coefficient source** 设置为 `Input port(s)` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Out** — 滤波后的输出向量 | 矩阵

滤波后的输出，以向量或矩阵形式返回。

输出维度始终等于输入信号的维度。

如果 **Out** 为定点，则它必须为带二进制小数点定标的有符号定点。

除非您将 **Coefficient source** 设置为 `Input port(s)`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Coefficient source
  summary: 操作模式 Dialog parameters（默认）| Input port(s) | Filter object
  group: 主选项卡
- name: Filter
  summary: 滤波器对象名称 BQF（默认）| dsp.BiquadFilter System object 名称
  group: 主选项卡
- name: Filter structure
  summary: 滤波器结构 Direct form II transposed（默认）| Direct form I | Direct form I transposed | Direct form II
  group: 主选项卡
- name: SOS Matrix (Mx6)
  summary: SOS 矩阵 [1 0.3 0.4 1 0.1 0.2]（默认）| *M*×6 矩阵
  group: 主选项卡
- name: Scale values
  summary: 缩放值 1（默认）| 标量 | 向量
  group: 主选项卡
- name: Initial conditions
  summary: 初始条件 0（默认）| 标量 | 向量
  group: 主选项卡
- name: Initial conditions on zeros side
  summary: 零点侧初始条件 0（默认）| 标量 | 向量
  group: 主选项卡
- name: Initial conditions on poles side
  summary: 极点侧初始条件 0（默认）| 标量 | 向量
  group: 主选项卡
- name: Scale values mode
  summary: 指定缩放值的模式 Specify via input port (g)（默认）| Assume all are unity and optimize
  group: 主选项卡
- name: Action when the a0 values of the SOS matrix are not one
  summary: 当 SOS 矩阵的 a0 值不为 1 时的操作 Warning（默认）| None | Error
  group: 主选项卡
- name: Optimize unity scale values
  summary: 优化单位缩放值 on（默认）| off
  group: 主选项卡
- name: Input processing
  summary: 输入处理 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: 主选项卡
- name: View Filter Response
  summary: 查看滤波器响应按钮
  group: 主选项卡
- name: Rounding mode
  summary: 舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作方法 off（默认）| on
  group: 数据类型选项卡
- name: Section input
  summary: 节输入数据类型 Same as input（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Section output
  summary: 节输出数据类型 Same as section input（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Multiplicand
  summary: 被乘数数据类型 Same as output（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Coefficients
  summary: 系数数据类型 Same word length as input（默认）| Specify word length | Binary point scaling
  group: 数据类型选项卡
- name: Product output
  summary: 乘积输出数据类型 Same as input（默认）| Inherit via internal rule | Binary point scaling
  group: 数据类型选项卡
- name: Accumulator
  summary: 累加器数据类型 Same as product output（默认）| Same as input | Binary point scaling
  group: 数据类型选项卡
- name: States
  summary: 状态数据类型 Same as accumulator（默认）| Same as input | Binary point scaling
  group: 数据类型选项卡
- name: Output
  summary: 输出数据类型 Same as accumulator（默认）| Same as input | Binary point scaling
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 锁定数据类型设置 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Coefficient source** — 操作模式 `Dialog parameters`（默认）| `Input port(s)` | `Filter object`

Biquad Filter 模块可以以三种不同的模式运行：

- `Dialog parameters` — 在模块掩码中输入有关滤波器的信息，例如结构和系数。
- `Input port(s)` — 使用 **Filter structure** 参数在模块掩码中输入有关滤波器结构的信息。滤波器系数通过出现在模块图标上的附加输入端口进入模块：

  - `Num` — 指定分子系数。
  - `Den` — 指定分母系数。
  - `g` — 指定缩放值。

  模块假定每个节的第一个分母系数为 1。此配置适用于 **Coefficient source** 设置为 `Input port(s)` 且 **Scale values mode** 设置为 `Specify via input port (g)` 的情况。
- `Filter object` — 使用 `dsp.BiquadFilter` System object™ 指定滤波器。

### **Filter** — 滤波器对象名称 `BQF`（默认）| `dsp.BiquadFilter System object` 名称

指定您希望模块实现的离散时间滤波器的名称。您必须将滤波器指定为 `dsp.BiquadFilter` System object。

您可以在模块掩码中或 MATLAB® 工作区变量中定义 System object。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Filter object` 时可见。

### **Filter structure** — 滤波器结构 `Direct form II transposed`（默认）| `Direct form I` | `Direct form I transposed` | `Direct form II`

指定滤波器结构。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 时可见。

### **SOS Matrix (Mx6)** — SOS 矩阵 `[1 0.3 0.4 1 0.1 0.2]`（默认）| *M*×6 矩阵

指定一个 *M*×6 矩阵，其中 *M* 是二阶节滤波器中节的数量。SOS 矩阵的每一行包含滤波器中相应节的分子和分母系数（*bik* 和 *aik*）。

[b01b11b21a01a11a21b02b12b22a02a12a22⋮⋮⋮⋮⋮⋮b0Mb1Mb2Ma0Ma1Ma2M]

无论其实际值如何，前导分母系数 [a01 a02 ... a0N] 均被视为 1。当 **a0** 不为 1 时，不对 SOS 矩阵应用缩放。

`ss2sos` 和 `tf2sos` 函数将滤波器的状态空间或传递函数描述转换为此模块使用的二阶节描述。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 时可见。

### **Scale values** — 缩放值 `1`（默认）| 标量 | 向量

指定要在 SOS 节之间使用的缩放值。您可以指定实值标量或长度为 *M*+1 的向量：

- 当您输入标量时，该值指定二阶滤波器第一节之前的增益值。其余增益值默认为 1。
- 当您输入 *M*+1 个值的向量时，每个值指定滤波器的单独节。例如，第一个元素是第一个增益值，第二个元素是第二个增益值，依此类推。

选中 **Optimize unity scale values** 复选框以在一个或多个缩放值等于 1 时优化仿真。选择此选项会移除单位增益，使这些值被视为 Simulink 线或连线。在某些存在单位缩放值的定点情况下，选择此参数还会省略某些类型转换。有关详细信息，请参阅定点数据类型部分。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 时可见。

### **Initial conditions** — 初始条件 `0`（默认）| 标量 | 向量

当 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时，指定滤波器状态的初始条件。

**Direct form II**

**Direct form II transposed**

Biquad Filter 模块默认将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中有关有效初始条件的内容。

**有效初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵（用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件。*M* 是节的数量，*N* 是输入通道的数量：  - 向量长度必须等于滤波器中延迟元素的数量，即 2*M*。 - 矩阵的行数必须等于滤波器中延迟元素的数量 2*M**N*。矩阵还必须为输入信号的每个通道具有一列。 |

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 且 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时可见。

### **Initial conditions on zeros side** — 零点侧初始条件 `0`（默认）| 标量 | 向量

指定滤波器结构中零点侧（*b0*、*b1*、*b2*、…）滤波器状态的初始条件。此参数仅在 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时适用。

**Direct form I**

**Direct form I transposed**

Biquad Filter 模块默认将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions on zeros side** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中有关有效初始条件的内容。

**有效初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵（用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件。其中 *M* 是节的数量，*N* 是输入通道的数量：  - 向量长度必须等于滤波器中延迟元素的数量，即 2*M*。 - 矩阵的行数必须等于滤波器中延迟元素的数量 2*M**N*。矩阵还必须为输入信号的每个通道具有一列。 |

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 且 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时可见。

### **Initial conditions on poles side** — 极点侧初始条件 `0`（默认）| 标量 | 向量

指定滤波器结构中极点侧（*a1*、*a2*、...）滤波器状态的初始条件。此参数仅在 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时适用。

**Direct form I**

**Direct form I transposed**

Biquad Filter 模块默认将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions on poles side** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中有关有效初始条件的内容。

**有效初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵（用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件。其中 *M* 是节的数量，*N* 是输入通道的数量：  - 向量长度必须等于滤波器中延迟元素的数量，即 2*M*。 - 矩阵的行数必须等于滤波器中延迟元素的数量 2*M**N*。矩阵还必须为输入信号的每个通道具有一列。 |

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 且 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时可见。

### **Scale values mode** — 指定缩放值的模式 `Specify via input port (g)`（默认）| `Assume all are unity and optimize`

选择如何指定要在滤波器节之间使用的缩放值。当您选择 `Specify via input port (g)` 时，您在端口 **g** 处输入缩放值作为二维向量。当您选择 `Assume all are unity and optimize` 时，所有缩放值都被移除并被视为 Simulink 线或连线。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Input port(s)` 时可见。

### **Action when the a0 values of the SOS matrix are not one** — 当 SOS 矩阵的 a0 值不为 1 时的操作 `Warning`（默认）| `None` | `Error`

指定当 SOS 矩阵 *a0j* 值不等于 1 时模块应执行的操作。操作可以是 `Warning`、`Error` 或 `None`。

当您选择 `None` 时，无论其实际值如何，前导系数 *a0j* 均被视为 1。当 **a0** 不为 1 时，不对 SOS 矩阵应用缩放。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 时可见。

### **Optimize unity scale values** — 优化单位缩放值 `on`（默认）| `off`

选中此复选框以在一个或多个缩放值等于 1 时优化仿真。选择此选项会移除单位增益，使这些值被视为 Simulink 线或连线。在某些存在单位缩放值的定点情况下，选择此参数还会省略某些类型转换。有关详细信息，请参阅定点数据类型部分。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 时可见。

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定模块应如何处理输入。如果输入是 *M*×*N* 矩阵，您可以将此参数设置为：

- `Columns as channels (frame based)`（默认）— 模块将每一列视为单独的通道。在此模式下，模块创建同一滤波器的 *M* 个实例，每个实例都有自己的独立状态缓冲区。*M* 个滤波器中的每一个在每个 Simulink 时间步处理 *N* 个输入样本。
- `Elements as channels (sample based)` — 模块将每个元素视为单独的通道。在此模式下，模块创建同一滤波器的 *M**N* 个实例，每个实例都有自己的独立状态缓冲区。每个滤波器在每个 Simulink 时间步处理一个输入样本。

### **View Filter Response** — 查看滤波器响应按钮

此按钮打开滤波器可视化工具（FVTool）并显示对话框中指定的滤波器的滤波器响应。

**注意**

当您在模块对话框中更改滤波器参数时，必须先单击 **Apply** 按钮，然后才能使用 **View Filter Response** 按钮。

### 数据类型选项卡

**注意**

此选项卡仅在您将 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 时出现。当 **Coefficient source** 设置为 `Filter object` 时，模块使用滤波器对象属性中指定的数据类型。

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。

有关更多详细信息，请参阅舍入模式。滤波器系数不遵循此参数；相反，它们始终舍入为 `Nearest`。

### **Saturate on integer overflow** — 溢出操作方法 `off`（默认）| `on`

当您选中此参数时，模块对其定点运算的结果进行饱和处理。当您清除此参数时，模块对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

滤波器系数始终饱和，不遵循此参数。

### **Section input** — 节输入数据类型 `Same as input`（默认）| `Binary point scaling`

选择如何指定进入双二阶滤波器每个节的定点数据类型的字长和小数长度。有关说明此模块中节输入数据类型使用的图示，请参阅定点数据类型部分。当您选择：

- `Same as input` — **Section input** 数据类型的字长和小数长度特性与模块输入的特性匹配。
- `Binary point scaling` — 输入节输入的字长和小数长度，以位为单位。

### **Section output** — 节输出数据类型 `Same as section input`（默认）| `Binary point scaling`

选择如何指定双二阶滤波器每个节输出的定点数据类型的字长和小数长度。有关此模块中节输出数据类型的使用图示，请参阅定点数据类型部分。当您选择：

- `Same as section input` — **Section output** 数据类型的字长和小数长度特性与模块输入的特性匹配。
- `Binary point scaling` — 以位为单位输入节输出的字长和小数长度。

### **Multiplicand** — 被乘数数据类型 `Same as output`（默认）| `Binary point scaling`

选择如何指定 `Direct form I transposed` 滤波器结构的被乘数数据类型的字长和小数长度。有关此模块中被乘数数据类型的使用图示，请参阅定点数据类型部分。

当您选择：

- `Same as output` — **Multiplicand** 数据类型的字长和小数长度特性与模块输出的特性匹配。
- `Binary point scaling` — 以位为单位输入被乘数的字长和小数长度。

#### 依赖关系

此参数仅在 **Filter structure** 参数设置为 `Direct form I transposed` 时可见。

### **Coefficients** — 系数数据类型 `Same word length as input`（默认）| `Specify word length` | `Binary point scaling`

当 **Coefficient source** 设置为 `Dialog parameters` 时，选择如何指定滤波器系数（分子、分母和缩放值）的字长和小数长度。有关此模块中系数数据类型的使用图示，请参阅定点数据类型部分。当您选择：

- `Same word length as input` — 滤波器系数的字长与模块输入的字长匹配。在此模式下，模块自动将系数的小数长度设置为仅二进制小数点缩放，在给定系数值和字长的情况下提供最佳精度。
- `Specify word length` — 以位为单位输入系数的字长。在此模式下，模块自动将系数的小数长度设置为仅二进制小数点缩放，在给定系数值和字长的情况下提供最佳精度。
- `Binary point scaling` — 以位为单位输入系数的字长和小数长度。如适用，分别为分子和分母系数输入单独的小数长度。

滤波器系数不遵循 **Rounding mode** 和 **Overflow mode** 参数；相反，它们始终饱和并舍入到 `Nearest`。

#### 依赖关系

此参数仅在 **Coefficient source** 设置为 `Dialog parameters` 时可见。

### **Product output** — 乘积输出数据类型 `Same as input`（默认）| `Inherit via internal rule` | `Binary point scaling`

指定如何设定乘积输出的字长和小数长度。有关此模块中乘积输出数据类型的使用图示，请参阅乘法数据类型和定点数据类型部分。当您选择：

- `Same as input` — 乘积输出的字长和小数长度特性与模块输入的特性匹配。
- `Inherit via internal rule` — 乘积输出的字长和小数长度基于全精度规则计算。这些规则防止模块内发生量化。根据需要添加位，以确保不发生舍入或溢出。有关更多详细信息，请参阅通过内部规则继承。
- `Binary point scaling` — 以位为单位输入乘积输出的字长和小数长度。如适用，分别为分子和分母乘积输出数据类型输入单独的小数长度。

### **Accumulator** — 累加器数据类型 `Same as product output`（默认）| `Same as input` | `Binary point scaling`

指定如何设定累加器的字长和小数长度。有关此模块中累加器数据类型的使用图示，请参阅乘法数据类型和定点数据类型部分。当您选择：

- `Same as input` — 累加器的字长和小数长度特性与模块输入的特性匹配。
- `Same as product output` — 累加器的字长和小数长度特性与乘积输出的特性匹配。
- `Binary point scaling` — 以位为单位输入累加器的字长和小数长度。如适用，分别为分子和分母累加器数据类型输入单独的小数长度。

### **States** — 状态数据类型 `Same as accumulator`（默认）| `Same as input` | `Binary point scaling`

当 **Coefficient source** 设置为 `Dialog parameters` 时，指定如何设定状态的字长和小数长度。有关此模块中状态数据类型的使用图示，请参阅定点数据类型部分。

当您选择：

- `Same as input` — 状态的字长和小数长度特性与模块输入的特性匹配。
- `Same as accumulator` — 状态的字长和小数长度特性与累加器的特性匹配。
- `Binary point scaling` — 以位为单位输入状态的字长和小数长度。如适用，分别为分子和分母状态数据类型输入单独的小数长度。

#### 依赖关系

此参数仅在 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时可见。

### **Output** — 输出数据类型 `Same as accumulator`（默认）| `Same as input` | `Binary point scaling`

选择如何指定输出的字长和小数长度。有关此模块中输出数据类型的使用图示，请参阅定点数据类型部分。当您选择：

- `Same as input` — 输出的字长和小数长度特性与模块输入的特性匹配。
- `Same as accumulator` — 输出的字长和小数长度特性与累加器的特性匹配。
- `Binary point scaling` — 以位为单位输入输出的字长和小数长度。

### **Lock data type settings against changes by the fixed-point tools** — 锁定数据类型设置 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块掩码上指定的数据类型。
## 所属库

DSP System Toolbox / Filtering / Filter Implementations DSP System Toolbox HDL Support / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**注意**

对于具有硬件友好控制信号的 HDL 优化双二阶滤波器架构，请使用 Biquad Filter (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块在 Simulink 中模拟 HDL 算法的延迟。DSP HDL Toolbox 模块生成适合 FPGA 上 DSP 块的直接形式 II 或直接形式 II 转置流水线加乘运算。它提供可选的流水线反馈架构，使用更多乘法器但减少关键路径并实现更高的时钟速率。DSP HDL Toolbox 模块不支持可编程系数。要执行多通道滤波，请将 DSP HDL Toolbox Biquad Filter 模块放入 For Each 子系统。

**HDL 架构**

该模块默认架构为 `HDLDataPath`。此架构提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中移除 Filter 子系统的层次结构。默认值为 `auto`。请参阅 FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数。默认值为 0。另请参阅资源分享 (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径（或向量）数。默认值为 0，表示实现完全并行的数据路径。另请参阅流式处理 (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 选择乘法器架构为 `linear` 或 `shiftadd`。默认值为 `linear`。有关更多信息，请参阅 Product, Matrix Multiply (Simulink) 中的 HDL 代码生成部分。 |
| **MultiplierInputPipeline** | 指定在滤波器乘法器输入端添加的流水线级数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定在滤波器乘法器输出端添加的流水线级数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **SectionOutputPipeline** | 指定为节输出添加的流水线级数。默认值为 `0`。 |
| **AdderOutputPipeline** | 在生成代码中为加法运算插入的输出流水线级数。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量  矩阵 | 是 | Half  Single  Double | 是 | 是 | 是 | 是 | 是 |

**模块参数配置**

以下模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制 |
| --- | --- |
| **Input processing** | 不支持参数值 `Columns as channels (frame based)`。 |

**优化**

该模块参与以下 HDL 优化以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| 资源分享 (HDL Coder) | *资源分享*是一种面积优化，HDL Coder 识别多个功能等效资源并将其替换为单个资源。 |
| 流式处理 (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 将向量数据路径转换为标量数据路径（或转换为多个较小尺寸的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| 分布式流水线 (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，通过移动设计中现有的延迟来减少关键路径，同时保持功能行为。 |
| 时钟速率流水线 (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| 自适应流水线 (HDL Coder) | *自适应流水线*优化创建带寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| 关键路径估计 (HDL Coder) | 要快速识别设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中被表征的模块，请参阅已表征模块 (HDL Coder)。 |

**限制和注意事项**

该模块具有以下限制：

- HDL 代码生成不支持帧输入。对于基于帧的输入，请使用 Biquad Filter (DSP HDL Toolbox) 模块。
- 您必须将 **Initial conditions** 设置为 `0`。HDL 代码生成不支持非零初始状态。
- 您必须选择 **Optimize unity scale values**。

要将 Biquad Filter 模块配置为可编程滤波器或多通道滤波器，请使用以下模块设置：

| 滤波器情况 | 注意事项 |
| --- | --- |
| **可编程滤波器** | HDL Coder 支持 Biquad Filter 模块的可编程滤波器。  1. 在滤波器模块掩码上，将 **Coefficient source** 设置为 **Input port(s)**。 2. 将向量信号连接到 **Num** 和 **Den** 系数端口。您必须为滤波器中的每个二阶节使用一个 Biquad Filter 模块。对于具有 *M* 个二阶节的滤波器，使用一系列 *M* 个 Biquad Filter 模块，每个模块的输入 **Num** 为 3×1 向量，输入 **Den** 为 2×1 向量。 |
| **多通道滤波器** | HDL Coder 支持将向量输入用于 Biquad Filter 模块。  1. 将向量信号连接到 Biquad Filter 模块输入端口。 2. 将 **Input processing** 指定为 `Elements as channels (sample based)`。 3. 要通过在通道之间共享滤波器内核来减少面积，请将模块的 **StreamingFactor** 参数设置为通道数。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2008b 中引入**

## 描述

对双二阶 IIR (SOS) 滤波器进行建模

Biquad Filter 模块使用指定的双二阶无限脉冲响应 (IIR) 滤波器独立地对输入信号的每个通道进行滤波。当您在对话框中指定滤波器系数时，该模块实现具有固定系数的静态滤波器。当您通过输入端口提供滤波器系数时，您可以在仿真期间调整系数。

Biquad Filter 模块支持 Simulink® 状态记录功能。有关更多信息，请参阅 State (Simulink)。

**注意**

Biquad Filter 和 Second-Order Section Filter 模块都在 Simulink 中实现二阶节滤波器的级联。但是，它们在滤波器可调性和定点信号支持等方面存在一些差异。

如果输入信号为 `single` 或 `double` 数据类型，请使用 Second-Order Section Filter 模块，因为它比 Biquad Filter 模块具有多个优势。如果输入信号为内置整数或定点算术，请使用 Biquad Filter 模块。您可以为定点算术运算自定义 Biquad Filter 模块。

有关两个模块之间关键差异的更多信息，请参阅 Biquad Filter 和 Second-Order Section Filter 模块之间的差异。
