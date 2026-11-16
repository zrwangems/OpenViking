---
type: simulink-block
title: 'Memory Copy'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'memorycopy'
documentation_source_path: 'ref/memorycopy.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory Copy

## 端口

### 输入

### **src** — 用于复制操作的输入数据 标量 | 向量

用于内存复制操作的源数据，指定为标量或向量。

#### 端口依赖

若要将此端口用作内存复制操作的源，请将参数 **Copy from** 设置为 `Input port`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **&src** — 用于复制操作的输入数据的地址 标量 | 向量

用于复制操作的源数据的内存地址，指定为标量或向量。

#### 端口依赖

若要将此端口用作内存复制操作的源，请将参数 **Copy from** 设置为 `Specified address`，并将 **Specify address source** 设置为 `Input port`。Copy Memory 模块将输入端口 `src` 转换为 `&src`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **src ofs** — 复制操作期间读取数据的偏移量 标量 | 向量

复制操作期间读取数据要使用的偏移量，指定为标量或向量。

#### 端口依赖

要创建此端口，请选择参数 **Use offset when reading**，并将 **Specify offset source** 设置为 `Input port`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **&dst** — 用于复制操作的输出数据的地址 标量 | 向量

用作复制操作的数据目标的内存地址，指定为标量或向量。

#### 端口依赖

若要将此端口用作内存复制操作的目标，请将参数 **Copy to** 设置为 `Specified address`，并将 **Specify address source** 设置为 `Input port`。Copy Memory 模块将输出端口 `dst` 转换为输入端口 `&dst`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **dst ofs** — 复制操作期间写入数据的偏移量 标量 | 向量

复制操作期间写入数据要使用的偏移量，指定为标量或向量。

#### 端口依赖

要创建此端口，请选择参数 **Use offset when writing**，并将 **Specify offset source** 设置为 `Input port`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出

### **dst** — 用于复制操作的输出数据 标量 | 向量

复制的数据，指定为标量或向量。

#### 端口依赖

若要将此端口用作内存复制操作的目标，请将参数 **Copy to** 设置为 `Output port`。

**Data Types:** `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

### 源

指定用于复制操作的源连续内存位置。指定源变量的数据类型、大小和其他属性。

### **Copy from** — 用于复制操作的输入源 Input port (默认) | Specified address | Specified source code symbol

指定复制操作的数据读取部分的输入源。从此表列出的源中进行选择。

| 数据读取源 | 要指定的参数值 |
| --- | --- |
| `src` 输入端口 | `Input port` |
| 内存地址 | `Specified address` |
| 源代码查找表中的符号（变量） | `Specified source code symbol` |

#### 参数依赖

- 如果选择 `Specified address`，请使用 **Specify address source** 指定内存地址的源，并使用 **Address** 指定地址。
- 如果选择 `Specified source code symbol`，请使用 **Source code symbol** 指定源代码符号表中要复制的符号（变量）。
- 如果选择 `Specified address` 或 `Specified source code symbol`，请将 **Data type** 更改为 `Inherit from source`（默认值）以外的值。如果不进行此更改，将收到错误消息，指示由于输入端口不存在而无法继承数据类型。

### **Specify address source** — 输入数据的内存地址的源 Specify via dialog (默认) | Input port

指定复制操作的输入源的内存地址的源。要为源变量指定内存地址，请选择 `Specify via dialog`。该选择将启用 **Address** 参数，用于指定内存地址。

要指定模块从输入端口获取地址，请选择 `Input port`。当选择 `Input port` 时，模块输入端口标签更改为 `&src`。

#### 参数依赖

- 要启用此参数，请将 **Copy from** 设置为 `Specified address`。
- 如果选择 `Specify via dialog`，此参数将启用 **Address** 参数，用于指定源变量的地址。
- 如果选择 `Specify via dialog`，请将 **Data type** 设置为 `Inherit from source`（默认值）以外的值。如果不进行此更改，将收到错误消息，指示由于输入端口不存在而无法继承数据类型。
- 如果选择 `Inport port`，请为 **Data type** 参数指定数据类型。

### **Address** — 源数据的内存地址 hex2dec('00001000') (默认) | 以十进制或十六进制形式表示并转换为十进制形式的内存地址

以十进制形式或以十六进制形式并转换为十进制形式指定源数据的内存地址，如默认值 `hex2dec('00001000')` 所示。

此示例将 `Ox1000` 转换为十进制形式。

```
4096 = hex2dec('1000');
```

对于此示例，可以将地址指定为 `4096` 或 `hex2dec('1000')`。

#### 参数依赖

要启用此参数，请将 **Copy from** 设置为 `Specified address`，并将 **Specify address source** 设置为 `Specify via dialog`。

### **Source code symbol** — 源代码符号表中的符号 myVariableSrc (默认) | string | character vector

指定源代码符号表中要复制的符号（变量）。指定的符号必须存在于程序的符号表中。模块不会验证符号是否存在于符号表中，也不会验证是否使用有效语法指定了符号。输入的文本应完全按照符号在代码中的显示方式来指定符号。

#### 参数依赖

- 要启用此参数，请将 **Copy from** 设置为 `Specified source code symbol`。
- 将 **Data type** 设置为 `Inherit from source`（默认值）以外的值。如果不进行此更改，将收到错误消息，指示由于输入端口不存在而无法继承数据类型。

### **Data type** — 正在复制的数据的数据类型 uint8 (默认) | double | single | int8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | Inherit from input port

指定正在复制的源数据的数据类型。要从 `src` 输入端口继承数据类型，请选择 `Inherit from input port`。

### **Data length** — 要复制的数据元素数 1 (默认) | 正整数

指定要从源位置复制的元素数。每个元素的数据类型由 **Data type** 参数指定。

### **Use offset when reading** — 读取输入时使用偏移量 off (默认) | on

指定模块在读取输入时是否使用偏移量。偏移值以指定数据类型的元素为单位。使用 **Specify offset source** 参数指定偏移量的源。

#### 参数依赖

- 如果选择此参数，请使用 **Specify offset source** 指定偏移量的源。
- 使用 **Offset** 指定偏移值。

### **Specify offset source** — 输入偏移量的源 Specify via dialog (默认) | Input port

指定复制操作的输入偏移量的源。要指定偏移值，请选择 `Specify via dialog`。该选择将启用 **Offset** 参数，用于指定偏移值。

要指定模块从输入端口获取偏移量，请选择 `Input port`。当选择 `Input port` 时，模块会创建一个标记为 `src ofs` 的输入端口，并从该端口读取偏移值。`src ofs` 端口使您的程序能够在程序执行期间动态更改偏移量。

#### 参数依赖

要启用此参数，请选择 **Use offset when reading**。

### **Offset** — 在将第一个值复制到目标之前要跳过的值的数量 0 (默认) | 正整数

在将第一个值复制到目标之前，指定要跳过的值的数量。

#### 参数依赖

要启用此参数，请选择 **Use offset when reading**，并将 **Specify offset source** 设置为 `Specify via dialog`。

### **Stride** — 读取输入的间隔 1 (默认) | 正整数

指定读取输入的间隔。默认情况下，stride 值为一，意味着生成的代码按顺序读取输入数据。当添加不等于一的 stride 值时，在读取输入数据时，生成的代码会跳过源地址中等距的间隔。

这些图展示了 stride 概念。在第一张图中，数据在没有 stride 的情况下复制。第二张图显示了 stride 值为二的结果。您可以使用 **Destination** 选项卡上的参数 **Stride** 为模块输出指定 stride 值。您还可以比较 stride 与 offset 以查看差异。

### 目标

指定复制操作的目标内存位置。指定目标的属性。

### **Copy to** — 用于复制操作的输出目标的类型 Output port (默认) | Specified address | Specified destination code symbol

指定复制操作的输出目标的类型。从此表列出的值中选择一个。

| 参数值 | 数据写入目标 |
| --- | --- |
| `Output port` | 模块 `dst` 输出端口 |
| `Specified address` | 由参数 **Specify address destination** 和 **Address** 指定的内存位置 |
| `Specified source code symbol` | 由参数 **Source code symbol** 指定的符号（变量） |

#### 参数依赖

- 如果选择 `Specified address`，请使用 **Specify address destination** 指定目标内存位置。
- 如果选择 `Specified source code symbol`，请使用 **Destination code symbol** 指定源代码符号表中要将变量复制到的符号（变量）。

### **Specify address source** — 输出目标的内存地址的源 Specify via dialog (默认) | Input port |

指定复制操作的变量的目标内存地址的源。要为变量指定内存地址，请选择 `Specify via dialog`。该选择将启用 **Address** 参数，用于指定内存地址。要指定模块从输入端口获取地址，请选择 `Input port`。当选择 `Input port` 时，模块会创建一个标记为 `&dst` 的输入端口。动态更改地址意味着您可以通过从模型中的上游模块提供变量地址来使用该模块复制不同的变量。

#### 参数依赖

- 要启用此参数，请将 **Copy to** 设置为 `Specified address`。
- 如果选择 `Specify via dialog`，此参数将启用 **Address** 参数，用于指定目标变量的地址。

### **Address** — 目标变量的内存地址 hex2dec('00002000') (默认) | 以十进制或十六进制形式表示并转换为十进制形式的内存地址

以十进制形式或以十六进制形式并转换为十进制形式指定目标变量的内存地址，如默认值 `hex2dec('00001000')` 所示。

此示例将 `Ox2000` 转换为十进制形式。

```
8192 = hex2dec('2000');
```

对于此示例，可以将地址指定为 `8192` 或 `hex2dec('2000')`。

#### 参数依赖

要启用此参数，请将 **Copy to** 设置为 `Specified address`，并将 **Specify address source** 设置为 `Specify via dialog`。

### **Source code symbol** — 源代码符号表中的符号 myVariableDst (默认) | string | character vector

指定源代码符号表中要将变量复制到的符号（变量）。指定的符号必须存在于程序的符号表中。模块不会验证符号是否存在于符号表中，也不会验证是否使用有效语法指定了符号。输入的文本应完全按照符号在代码中的显示方式来指定符号。

#### 参数依赖

要启用此参数，请将 **Copy to** 设置为 `Specified source code symbol`。

### **Data type** — 变量的数据类型 uint32 (默认) | double | single | int8 | uint8 | int16 | uint16 | uint32 | int64 | uint64 | boolean | Inherit from source

指定源变量的数据类型。要从源变量继承数据类型，请选择 `Inherit from source`。

### **Use offset when writing** — 写入输出时使用偏移量 off (默认) | on

指定模块在写入输出时是否使用偏移量。偏移值以指定数据类型的元素为单位。使用 **Specify offset source** 参数指定偏移量的源。

#### 参数依赖

如果选择此参数，请使用 **Specify offset source** 指定偏移量的源。使用 **Offset** 指定偏移值。

### **Specify offset source** — 输出目标的偏移量的源 Specify constant value (默认) | Specify source code symbol

指定复制操作的输出目标的偏移量的源。要为目标变量指定偏移值，请选择 `Specify via dialog`。该选择将启用 **Offset** 参数，用于指定偏移值。

要指定模块从输入端口获取偏移量，请选择 `Input port`。当选择 `Input port` 时，模块会添加一个标记为 `dst ofs` 的输入端口，并从该端口读取偏移值。`dst ofs` 端口使您的程序能够在执行期间动态更改偏移量。

#### 参数依赖

要启用此参数，请选择 **Specify offset source**。

### **Offset** — 在将第一个值写入目标之前要跳过的值的数量 0 (默认) | 正整数

在将第一个值写入目标之前，指定要跳过的值的数量。

#### 参数依赖

要启用此参数，请选择 **Use offset when writing**，并将 **Specify offset source** 设置为 `Specify via dialog`。

### **Stride** — 写入输出的间隔 1 (默认) | 正整数

指定写入输出的间隔。默认情况下，stride 值为一，意味着生成的代码将输入数据按顺序写入目标的连续位置。当添加不等于一的 stride 值时，在写入输入数据时，生成的代码会跳过目标地址中等距的间隔。

此图显示了将 stride 值三应用于将输入写入输出位置。您可以使用 **Source** 窗格上的参数 **Stride** 为输入指定 stride 值。如图所示，您可以同时使用输入 stride 和输出 stride 来更全面地操作内存。

### **Sample time** — 内存复制的速率 inf (默认) | scalar

指定内存复制操作发生的速率，以 seconds 为单位。要使用恒定采样时间，请指定 `Inf`。要从输入端口继承采样时间，或者当模块没有输入端口时从 Simulink® 模型继承，请指定 `-1`。

### 选项

配置控制复制过程的参数。

### **Set memory value at initialization** — 在初始化期间设置内存地址 off (默认) | on

指定是否在程序初始化期间将内存地址初始化为特定值。

#### 参数依赖关系

If you select this parameter, use a combination of parameters to
configure the initialization value.

| 要配置的内容 | 参数 |
| --- | --- |
| 初始化值的来源 | **Specify initialization value source** |
| 作为常量的初始化值 | **Initialization value (constant)** |
| 作为变量的初始化值 | **Initialization value (source code symbol)** |
| 作为掩码以在位级操作寄存器内容的初始化值 | **Apply initialization value as mask** |
| 应用掩码值 | **Bitwise operator** |

### **Specify initialization value source** — 初始化值来源 Specify constant value (default) | Specify source code symbol

指定初始值的来源。要将内存初始化的来源配置为特定值，请选择 `Specify constant
value`。要将来源配置为变量（符号），请选择 `Specify source code symbol`。

#### 参数依赖关系

- 要启用此参数，请选择 **Set memory value at
  initialization**。
- 使用 **Initialization value (constant)** 或
  **Initialization value (source code symbol)** 指定初始值。

### **Initialization value (constant)** — 常量初始化值 1 (default) | scalar

指定一个常量值。

#### 参数依赖关系

要启用此参数，请选择 **Set memory value at
initialization**，并将 **Set initialization value
source** 设置为 `Specify constant
value`。

### **Initialization value (source code symbol)** — 源代码符号表中的符号 myInitValueVariable (default) | string | character vector

指定源代码符号表中要用于初始化值的符号（变量）。您指定的符号必须存在于程序的符号表中。该模块不会验证符号是否存在于符号表中，也不会验证您是否使用有效语法指定该符号。输入的文本应完全按照该符号在代码中的显示方式指定该符号。

#### 参数依赖关系

要启用此参数，请选择 **Set memory value at
initialization**，并将 **Set initialization value
source** 设置为 `Specify source code
symbol`。

### **Apply initialization value as mask** — 将初始化值作为掩码应用 off (default) | on

指定是否将初始化值用作掩码，以在位级操作寄存器内容。您的初始化值将被视为用于掩码的位字符串。

要定义如何应用掩码值，请为 **Bitwise operator** 参数指定值。

要将初始化值用作掩码，复制的输出必须是特定地址。该输出：

- 可以是符号
- 不能是输出端口

#### 参数依赖关系

如果选择此参数，请使用 **Bitwise operator**
定义如何应用掩码值。

### **Bitwise operator** — 按位运算类型 bitwise AND (default) | bitwise OR | bitwise exclusive OR | left shift | right shift

指定用作掩码以操作内存值的按位运算类型。将掩码应用于复制过程意味着您可以选择结果中的各个位。例如，通过应用掩码，您可以读取第五位的值。

从此表中选择一种按位运算。

| 按位运算 | 描述 |
| --- | --- |
| `bitwise AND` | 将掩码值作为按位 AND 应用于寄存器中的值。 |
| `bitwise OR` | 将掩码值作为按位 OR 应用于寄存器中的值。 |
| `bitwise exclusive OR` | 将掩码值作为按位异或应用于寄存器中的值。 |
| `left shift` | 将寄存器中的位向左移位，移位量由初始化值表示的位数决定。例如，如果初始化值为 3，则该模块将寄存器值左移 3 位。在这种情况下，该值必须是正整数。 |
| `right shift` | 将寄存器中的位向右移位，移位量由初始化值表示的位数决定。例如，如果初始化值为 6，则该模块将寄存器值右移 6 位。在这种情况下，该值必须是正整数。 |

#### 参数依赖关系

要启用此参数，请选择 **Apply initialization value as
mask**。

### **Set memory value at termination** — 在程序终止时复制内存 off (default) | on

指定程序在程序终止期间复制内存。在终止期间复制内存中的值是在程序初始化期间复制之外额外进行的。

#### 参数依赖关系

如果选择此参数，您可以使用 **Set memory value only
at initialization/termination** 将复制操作限制为仅在程序初始化和终止期间发生。

### **Termination value** — 终止值 1 (default) | scalar | vector | matrix

指定在程序终止期间写入内存的值。

#### 参数依赖关系

要启用此参数，请选择 **Set memory value at
termination**。

### **Set memory value only at initialization/termination** — 仅在程序初始化和终止期间复制内存值 off (default) | on

指定是否仅在程序初始化和终止期间执行复制。清除此参数时，模块在初始化、实时操作和终止期间执行复制。如果选择此参数，模块仅在初始化和终止期间执行复制。

### **Insert custom code before memory write** — 在内存写入之前插入自定义代码 off (default) | on

指定代码生成器是否在程序写入指定内存位置之前立即插入自定义 ANSI C 代码。您可以使用此参数和 **Insert custom code
after memory write** 在访问寄存器之前和之后锁定和解锁寄存器。例如，某些处理器具有一些寄存器，您可能需要在程序访问它们之前和之后使用 EALLOW 和 EDIS 宏来解锁和锁定这些寄存器。

#### 参数依赖关系

如果选择此参数，请使用 **Custom code** 指定要在内存写操作之前立即插入生成代码中的自定义 ANSI C 代码。

### **Insert custom code after memory write** — 内存写入后的自定义代码标志 off (default) | on

指定代码生成器是否在程序写入指定内存位置之后立即插入自定义 ANSI C 代码。您可以使用 **Insert custom code before memory
write** 和此参数在访问寄存器之前和之后锁定和解锁寄存器。例如，某些处理器具有一些寄存器，您可能需要在程序访问它们之前和之后使用 EALLOW 和 EDIS 宏来解锁和锁定这些寄存器。

#### 参数依赖关系

如果选择此参数，请使用 **Custom code** 指定要在内存写操作之后立即插入生成代码中的自定义 ANSI C 代码。

### **Custom code** — /\* Custom Code Before Write\*/ 或 /\* Custom Code After Write\*/ (default) | string | character vector

指定要在内存写操作之前或之后立即插入生成代码中的自定义 ANSI C 代码。您指定的代码将完全按照您输入的内容出现在生成代码中。

#### 参数依赖关系

要启用此参数，请选择 **Insert custom code before
memory write** 或 **Insert custom code after memory
write**。

## 所属库

Motor Control Blockset / Signal Management

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

在内存段之间复制数据

Memory Copy 模块的生成代码根据模块参数配置，从处理器内存复制数据以及向处理器内存复制数据。当您使用此模块将单个数据元素从源复制到目标时，该模块使用源数据类型从源复制该元素，然后将该数据元素转换为指定的目标数据类型。

在模型中根据需要包含尽可能多的 Memory Copy 模块实例，以操作目标处理器上的内存。该模块的每个实例处理提供给该模块作为输入的一个变量、地址或地址集。

使用模块参数指定内存复制的源和目标。您可以使用模块参数控制内存复制的其他方面，例如：

- 内存位置的初始化
- 运行时内存步长和偏移
- 在程序初始化期间、程序终止期间以及每个采样时间对内存的写操作
- 在每次内存复制读和写操作之前和之后插入自定义 ANSI® C 源代码（例如，在访问寄存器之前和之后锁定和解锁寄存器）

Memory Copy 模块在程序执行期间的三个时段执行操作：

- 初始化
- 实时操作
- 终止

您可以使用模块参数控制该模块何时以及如何初始化内存、在内存之间复制数据或变量，以及终止复制操作。这些参数使您能够在三个时段中独立打开和关闭内存复制操作。

使用 Memory Copy 模块和 Memory Allocate (Embedded Coder) 模块为自定义设备驱动程序（例如 PCI 总线驱动程序或 codec 风格驱动程序）操作和分配内存。

在仿真期间，Memory Copy 模块不执行操作。模块输出未定义。
