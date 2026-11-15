---
type: simulink-block
title: 'Memory Copy'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'memorycopy'
documentation_source_path: 'supportpkg/arduino_ref/memorycopy.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory Copy

## 端口

### 输入

### **src** — 输入信号 标量 | 向量

从该输入端口读取数据时，将 **复制来源** 参数设置为 `Input port`。选择此选项后，输入端口将变为可用。模块上的端口标签将变为 `src`，表示该模块期望数据来自输入端口。

要从传入信号继承数据类型，请将源 **数据类型** 参数设置为 `Inherit from input port`。将源 **偏移量** 参数指定为 `0`，将源 **步长** 参数指定为 `1`。如果为这些参数指定任何其他值，将收到错误消息，指出指定的值无效。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **&src** — 源内存位置的起始地址 标量

当从该输入端口读取源地址时，将 **复制来源** 参数设置为 `Specified address`，并将源 **指定地址来源** 参数设置为 `Input port`。选择这些选项后，输入端口将变为可用。模块上的端口标签将变为 `&src`，表示该模块期望地址来自输入端口。能够动态更改地址意味着，您可以通过在模型中从上游模块提供变量地址，使该模块复制不同的变量。

当从输入端口读取地址时，将源 **数据类型** 从默认值 `Inherit from input port` 更改为 **数据类型** 列表中的某种数据类型。如果不更改参数值，将收到错误消息。错误消息指出无法继承数据类型，因为输入端口不存在。

**数据类型：** `uint32`

### **src ofs** — 读取数据前添加到起始地址的内存位置数 标量

当从该输入端口读取数据的偏移量值时，将源 **指定偏移量来源** 参数设置为 `Input port`。仅当选择 **读取时使用偏移量** 参数时，源 **指定偏移量来源** 参数才会显示。

选择此选项后，输入端口将变为可用。模块上的端口标签将变为 `src ofs`，表示该模块期望偏移量值来自输入端口。该端口使您的程序能够在执行期间通过将偏移量值作为模块输入来动态更改偏移量。

当从输入端口读取偏移量值时，不要将 **复制来源** 参数设置为 `Input port`。如果选择此选项，将收到错误消息，指出当从输入端口复制数据时，不能将源偏移量参数指定为输入端口。

**数据类型：** `uint32`

### **&dst** — 目标内存位置的起始地址 标量

当从该输入端口读取目标内存位置的起始地址时，将 **复制到** 参数设置为 `Specified address`，并将目标 **指定地址来源** 参数设置为 `Input port`。选择此选项后，输入端口将变为可用。模块上的端口标签将变为 `&dst`，表示该模块期望地址来自输入端口。能够动态更改地址意味着，您可以通过在模型中从上游模块提供变量地址，使该模块复制不同的变量。

**数据类型：** `uint32`

### **dst ofs** — 写入数据前添加到起始地址的内存位置数 标量

当从该输入端口读取目标内存位置的偏移量值时，将目标 **指定偏移量来源** 参数设置为 `Input port`。仅当选择 **读取时使用偏移量** 参数时，目标 **指定偏移量来源** 参数才会显示。

选择此选项后，输入端口将变为可用。模块上的端口标签将变为 `dst ofs`，表示该模块期望偏移量值来自输入端口。该端口使您的程序能够在执行期间通过将偏移量值作为模块输入来动态更改偏移量。

当从输入端口读取偏移量时，不要将 **复制到** 参数设置为 `Output port`。如果选择此选项，将收到错误消息，指出当将数据复制到输出端口时，不能将目标偏移量参数指定为输入端口。

**数据类型：** `uint32`

### 输出

### **dst** — 输出信号 标量 | 向量

当向该输出端口写入数据时，将 **复制到** 参数设置为 `Output port`。选择此选项后，输出端口将变为可用。模块上的端口标签将变为 `dst`，表示该模块将数据写入输出端口。

要从传入信号继承数据类型，请将 **数据类型** 参数设置为 `Inherit from source`。将目标 **偏移量** 参数指定为 `0`，将目标 **步长** 参数指定为 `1`。如果为这些参数指定任何其他值，将收到错误消息，指出指定的值无效。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

Memory Copy 对话框包含多个选项卡：

- **源** — 标识要从中复制的连续内存位置。指定源变量的数据类型、大小和其他属性。
- **目标** — 指定要将源复制到的内存位置，并指定目标的属性。
- **选项** — 选择各种参数以控制复制过程。

### 源

### **复制来源** — 模块读取数据的来源 `Input port`（默认） | `Specified address` | `Specified source code symbol`

- `Input port` — 输入端口将变为可用。模块上的端口标签将变为 `src`，表示该模块期望数据来自输入端口。
- `Specified address` — 该模块从 **指定地址来源** 参数中选择的选项读取源地址。

  如果将 **指定地址来源** 参数设置为 `Specify via dialog`，则该模块读取您在 **地址** 参数中指定的源地址。

  如果将 **指定地址来源** 参数设置为 `Input Port`，则输入端口将变为可用。模块上的端口标签将变为 `&src`，表示该模块期望地址来自输入端口。
- `Specified source code symbol` — 该模块从 **源代码符号** 参数中指定的符号（变量）读取数据。

如果为 **复制来源** 参数选择 `Specified address` 或 `Specified source code symbol`，请将 **数据类型** 从默认值 `Inherit from input port` 更改为 **数据类型** 列表中的某种数据类型。

### **指定地址来源** — 用于读取数据的内存位置来源 `Specify via dialog`（默认） | `Input port`

- `Specify via dialog` — 该模块从 **地址** 参数中指定的内存位置读取数据。
- `Input port` — 输入端口将变为可用。模块上的端口标签将变为 `&src`，表示该模块期望源地址来自输入端口。能够动态更改地址意味着，您可以通过在模型中从上游模块提供变量地址，使该模块复制不同的变量。

#### 依赖关系

仅当将 **复制来源** 参数设置为 `Specified address` 时，此参数才会显示。

### **源代码符号** — 包含源地址的符号（变量） `myVariableSrc`（默认） | `Any defined symbol`

该模块不验证符号是否有效。符号只有在符号表中有条目时才有效。如果无效，则在尝试编译、链接和运行生成的代码时会收到错误。

如果符号包含标量值，请在此参数中于符号前指定 `&`。如果符号包含向量值，请在此参数中仅指定符号。

#### 依赖关系

仅当将 **复制来源** 参数设置为 `Specified source code symbol` 时，此参数才会显示。

### **地址** — 输入数据的内存位置 `hex2dec('00001000')`（默认）

以十进制格式或带单引号的十六进制字符串指定地址。当以十六进制字符串指定地址时，将该字符串作为参数传递给 `hex2dec` 函数。此函数将字符串从十六进制格式转换为十进制格式。以下示例将 `0x1000` 转换为其十进制形式。

```
4096 = hex2dec('1000');
```

对于此示例，您可以将 `4096` 或 `hex2dec('1000')` 指定为地址。

#### 依赖关系

仅当将 **复制来源** 参数设置为 `Specified address`，并将 **指定地址来源** 设置为 `Specify via dialog` 时，此参数才会显示。

### **数据类型** — 输入数据的类型 `Inherit from input port`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

使用此参数指定输入数据的数据类型。当将此参数设置为 `Inherit from input port` 时，该模块从模块输入端口处的值继承数据类型。

**注意**

如果为 **复制来源** 参数选择 `Specified address` 或 `Specified source code symbol`，请将 **数据类型** 参数从默认值 `Inherit from input port` 更改为 **数据类型** 列表中的某种数据类型。

### **数据长度** — 要复制的元素数 `1`（默认） | `Any integer value greater than 1`

指定要从源位置复制的元素数。每个元素具有由 **数据类型** 参数指定的数据类型。

### **读取时使用偏移量** — 指定读取数据时的偏移量 off（默认） | on

选择此参数时，该模块从 **指定偏移量来源** 参数中选择的选项读取源偏移量。清除此参数时，该模块从 **复制来源** 参数中指定的起始地址读取数据。

### **指定偏移量来源** — 输入数据的偏移量来源 `Specify via dialog`（默认） | `Input port`

- `Specify via dialog` — 该模块读取您在 **偏移量** 参数中指定的偏移量值。
- `Input port` — 输入端口将变为可用。模块上的端口标签将变为 `src ofs`，表示该模块期望偏移量值来自输入端口。该端口使您的程序能够在执行期间通过将偏移量值作为模块输入来动态更改偏移量。

#### 依赖关系

仅当选择 **读取时使用偏移量** 参数时，此参数才会显示。

### **偏移量** — 在开始读取数据前添加到起始地址的内存位置数 `0`（默认） | `Any integer value greater than 0`

**偏移量** 指示模块是在输入地址处复制数据的第一个元素，还是在开始将输入复制到目标之前跳过一些值。**偏移量** 定义在将第一个值复制到目标之前要跳过多少个输入元素。

#### 依赖关系

仅当选择 **读取时使用偏移量** 参数时，此参数才会显示。

### **步长** — 读取输入数据时元素之间的间距 `1`（默认） | `Any integer value greater than 1`

指定读取输入数据时元素之间的间距。步长值等于 `1` 表示生成的代码按顺序读取输入数据。当添加大于 1 的步长值时，该模块会跳过该数量的元素，并从生成的地址读取元素。

接下来的两幅图说明了步长概念。在第一幅图中，您看到的是没有步长的情况下复制的数据。

第二幅图显示了步长值等于 2。当模块将输入复制到输出位置时，应用步长值 2。您可以使用 **步长** 参数从 **目标** 选项卡为输出指定步长值。

### 目标

### **复制到** — 模块将数据写入到的目标 `Input port`（默认） | `Specified address` | `Specified source code symbol`

- `Output port` — 输出端口将变为可用。模块上的端口标签将变为 `dst`，表示该模块将数据写入输出端口。
- `Specified address` — 该模块将数据复制到您在 **指定地址来源** 参数中指定的内存位置。

  如果将 **指定地址来源** 参数设置为 `Specify via dialog`，则该模块读取您在 **地址** 参数中指定的目标地址。

  如果将 **指定地址来源** 参数设置为 `Input Port`，则输入端口将变为可用。模块上的端口标签将变为 `&dst`，表示该模块期望目标地址来自输入端口。
- `Specified source code symbol` — 该模块将数据复制到 **源代码符号** 参数中指定的符号（变量）。

### **指定地址来源** — 用于写入数据的内存位置来源 `Specify via dialog`（默认） | `Input port`

- `Specify via dialog` — 该模块将数据写入 **地址** 参数中指定的位置。
- `Input port` — 输入端口将变为可用。模块上的端口标签将变为 `&dst`，表示该模块期望目标地址来自输入端口。能够动态更改地址意味着，您可以通过在模型中从上游模块提供变量地址，使该模块复制不同的变量。

#### 依赖关系

仅当将 **复制到** 参数设置为 `Specified address` 时，此参数才会显示。

### **源代码符号** — 包含目标地址的符号（变量） `myVariableDst`（默认） | `Any defined symbol`

该模块不验证符号是否有效。符号只有在符号表中有条目时才有效。如果无效，则在尝试编译、链接和运行生成的代码时会收到错误。

如果符号包含标量值，请在此参数中于符号前指定 `&`。如果符号包含向量值，请在此参数中仅指定符号。

#### 依赖关系

仅当将 **复制到** 参数设置为 `Specified source code symbol` 时，此参数才会显示。

### **地址** — 模块写入数据的内存位置 `hex2dec('00001000')`（默认）

以十进制格式或带单引号的十六进制字符串指定地址。当以十六进制字符串指定地址时，将该向量作为参数传递给 `hex2dec` 函数。此函数将字符串从十六进制格式转换为十进制格式。以下示例将 `Ox2000` 转换为十进制形式。

```
8192 = hex2dec('2000');
```

对于此示例，您可以将 `8192` 或 `hex2dec('2000')` 指定为地址。

#### 依赖关系

仅当将 **复制到** 参数设置为 `Specified address`，并将 **指定地址来源** 设置为 `Specify via dialog` 时，此参数才会显示。

### **数据类型** — 输出数据的类型 `uint32`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean` | `Inherit from source`

使用此参数指定输出的数据类型。当将此参数设置为 `Inherit from source` 时，该模块从模块输入端口处的输入信号继承数据类型。

### **写入时使用偏移量** — 指定写入数据时的偏移量 off（默认） | on

选择此参数时，该模块从 **指定偏移量来源** 参数中选择的选项读取偏移量。清除此参数时，该模块从 **复制到** 参数中指定的选项读取起始地址的数据。

### **Specify offset source** — 写入数据的偏移源 `Specify via dialog`（默认）| `Input port`

- `Specify via dialog` — 该模块读取您在 **Offset** 参数中指定的偏移值。
- `Input port` — 一个输入端口变为可用。模块上的端口标签变为 `dst ofs`，表示该模块期望偏移值来自输入端口。此端口使您的程序能够通过在运行时将偏移值作为模块输入来动态更改偏移。

#### 依赖关系

此参数仅在您选择 **Use offset when writing** 参数时出现。

### **Offset** — 在开始写入数据之前添加到起始地址的内存位置数 `0`（默认）| `Any integer value greater than 0`

**Offset** 指示模块是将数据的第一个元素写入目标的起始地址，还是在写入输出之前跳过目标处的一个或多个位置。**Offset** 定义在将第一个值写入目标之前要跳过目标中的多少个值。

#### 依赖关系

此参数仅在您选择 **Use offset when writing** 参数时出现。

### **Stride** — 写入数据时元素之间的间距 `1`（默认）| `Any integer value greater than 1`

指定写入输出数据时元素之间的间距。stride 值等于 1 表示生成的代码将输入数据按连续位置顺序写入目标。当添加大于 1 的 stride 值时，输出数据不会顺序存储，而是跳过等于 stride 的元素。

此图展示了将 stride 值 3 应用于将输入写入输出位置。您可以使用 **Stride** 参数从 **Source** 选项卡为输入指定 stride 值。如图所示，您可以同时对输入和输出应用 stride，以更充分地操作内存。

### **Sample time** — 内存复制操作发生的速率，以秒为单位 `Inf`（默认）| `-1` | `Any value greater than 0`

默认值 `Inf` 指示模块使用常量采样时间。当您将 **Sample time** 指定为 `-1` 时，Memory Copy 模块从输入继承采样时间。当没有模块输入时，该模块从 Simulink® 模型继承采样时间。

### 选项

### **Set memory value at initialization** — 指定用于初始化目标内存位置的值及其来源 off（默认）| on

当您选择此选项时，您指示模块在运行时初始化程序时将内存位置初始化为特定值。选择此选项后，使用 **Specify initialization value source** 参数设置所需的值。或者，您可以指示模块从模块输入获取初始值。

如果选择此参数，请将目标 **Copy to** 参数设置为 `Specified address` 或 `Specified source code symbol`。如果不更改参数值，则会收到错误消息，指出当目标是输出端口时无法在初始化时设置内存。

### **Specify initialization value source** — 指定初始值的来源 `Specify constant value`（默认）| `Specify source code symbol`

- `Specify constant value` — 设置程序初始化内存时要使用的单个值。

  该模块从您在 **Initialization value (constant)** 参数中指定的值读取初始化值。
- `Specify source code symbol` — 指定用于初始值的变量（符号）。

  该模块从您在 **Initialization value (source code symbol)** 参数中指定的符号读取初始化值。该模块不验证符号是否有效。符号只有在符号表中具有条目时才有效。如果无效，您在尝试编译、链接和运行生成的代码时会收到错误。

#### 依赖关系

此参数仅在您选择 **Set memory value at initialization** 参数时出现。

### **Initialization value (constant)** — 在运行时初始化程序时用于初始化内存位置的常量值 `1`（默认）| `Any value`

#### 依赖关系

此参数仅在您选择 **Set memory value at initialization** 参数并将 **Specify initialization value source** 设置为 `Specify constant value` 时出现。

### **Initialization value (source code symbol)** — 包含初始化值的已定义符号（变量） `myInitValueVariable`（默认）| `Any defined symbol`

当您指定符号时，该模块不验证符号是否有效。符号只有在符号表中具有条目时才有效。如果无效，您在尝试编译、链接和运行生成的代码时会收到错误。

#### 依赖关系

此参数仅在您选择 **Set memory value at initialization** 参数并将 **Specify initialization value source** 设置为 `Specify source code symbol` 时出现。

### **Apply initialization value as mask** — 将初始化值指定为掩码 off（默认）| on

初始化值被视为用于掩码的位串。

该模块对初始化值执行按位运算，以在位级别操作寄存器内容。您在 **Bitwise operator** 参数中指定的运算符决定按位运算。

**注意**

要将初始化值用作掩码，请将目标 **Copy to** 参数设置为 `Specified address` 或 `Specified source code symbol`。

#### 依赖关系

此参数仅在您选择 **Set memory value at initialization** 参数时出现。

### **Bitwise operator** — 指定用于操作寄存器中内存值的按位运算符 `bitwise AND`（默认）| `bitwise OR` | `bitwise exclusive OR` | `left shift` | `right shift`

要将初始化值用作掩码，请从 **Bitwise operator** 列表中选择此表中列出的条目之一。

| 按位运算符列表条目 | 描述 |
| --- | --- |
| `bitwise AND` | 将掩码值作为按位 AND 应用于寄存器中的值。 |
| `bitwise OR` | 将掩码值作为按位 OR 应用于寄存器中的值。 |
| `bitwise exclusive OR` | 将掩码值作为按位异或应用于寄存器中的值。 |
| `left shift` | 将寄存器中的位向左移动初始化值所表示的位数。例如，如果初始化值为 3，则模块将寄存器值向左移动 3 位。在这种情况下，该值必须为正整数。 |
| `right shift` | 将寄存器中的位向右移动初始化值所表示的位数。例如，如果初始化值为 6，则模块将寄存器值向右移动 6 位。在这种情况下，该值必须为正整数。 |

#### 依赖关系

此参数仅在您选择 **Apply initialization value as mask** 参数时出现。

### **Set memory value at termination** — 指定写入操作后目标内存的值 off（默认）| on

此参数在程序开始访问目标内存位置时初始化内存，并指示程序在程序终止时将内存设置为特定值。

### **Termination value** — 写入操作后目标内存的常量值 `1`（默认）| `Any value`

此参数仅在您选择 **Set memory value at termination** 参数时出现。

### **Set memory value only at initialization/termination** — 指定模块执行复制操作的程序执行时段 off（默认）| on

此 Memory Copy 模块在程序执行期间的三个时段执行操作：初始化、实时操作和终止。当您选择此参数时，该模块仅执行内存初始化和终止操作。它不会在实时操作期间复制数据。

### **Insert custom code before memory write** — 指定要在模块写入指定内存位置之前插入到生成代码中的自定义 ANSI C 代码 off（默认）| on

该模块在写入操作之前插入您在 **Custom code** 参数中指定的自定义 ANSI C 代码。

您可以使用自定义代码功能在访问寄存器之前和之后锁定和解锁寄存器。例如，某些处理器的寄存器需要在程序访问它们之前使用 EALLOW 宏解锁。

### **Custom code** — 在模块写入指定内存位置之前插入到生成代码中的自定义 ANSI C 代码 `/* Custom Code Before Write*/`（默认）

您在此参数中指定的代码就是出现在生成代码中的代码。

#### 依赖关系

要启用此参数，请选择 **Insert custom code before memory write** 参数。

### **Insert custom code after memory write** — 指定要在模块写入指定内存位置之后插入到生成代码中的自定义 ANSI C 代码 off（默认）| on

该模块在写入操作之后插入您在 **Custom code** 参数中指定的自定义 ANSI C 代码。

您可以使用自定义代码功能在访问寄存器之前和之后锁定和解锁寄存器。例如，某些处理器的寄存器需要在程序访问它们之后使用 EDIS 宏锁定。

### **Custom code** — 在模块写入指定内存位置之后插入到生成代码中的自定义 ANSI C 代码 `/* Custom Code After Write*/`（默认）

您在此参数中指定的代码就是出现在生成代码中的代码。

#### 依赖关系

此参数仅在您选择 **Insert custom code after memory write** 参数时出现。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities Simulink Support Package for Arduino Hardware / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

复制到内存和从内存复制部分

在生成的代码中，Memory Copy 模块按您使用模块参数配置的方式，把变量或数据复制到处理器内存以及从处理器内存复制出来。您的模型可以包含所需数量的此类模块，以操作处理器上的内存。

每个模块处理提供给该模块的一个变量、地址或地址集。使用此模块的参数，您可以指定内存复制的源和目标，以及初始化内存位置的选项。

在运行时，您可以更改内存 stride 和 offset 等选项。通过选择模块中的各种参数，您可以在程序初始化时、程序终止时以及每个采样时间写入内存。初始化过程只发生一次，而不是在每次读取和写入操作时都发生。

借助自定义源代码选项，该模块允许您在每次内存读取和写入（复制）操作之前和之后添加自定义 ANSI® C 源代码。

### 模块操作

此模块在程序执行期间的三个时段执行操作：初始化、实时操作和终止。通过设置内存初始化和终止的选项，您可以控制该模块何时以及如何初始化内存、复制到内存和从内存复制，以及终止内存操作。这些参数使您能够彼此独立地打开和关闭这三个时段中的内存操作。

### 复制内存

当您使用此模块将单个数据元素从源复制到目标时，该模块会以源数据类型从源复制该元素，然后将该数据元素转换为您在模块参数中指定的目标数据类型。
