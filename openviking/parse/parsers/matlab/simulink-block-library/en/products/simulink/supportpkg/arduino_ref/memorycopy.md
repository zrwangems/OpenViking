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
language: en
---

# Memory Copy

## Ports

### Input

### **src** — Input signal scalar | vector

When reading the data from this input port, set the **Copy
from** parameter to `Input port`. When you
choose this option, an input port becomes available. The port label
on the block changes to `src`, indicating that the
block expects data to come from the input port.

To inherit data type from the incoming signal, set the source **Data
Type** parameter to `Inherit from input port`.
Specify the source **Offset** parameter as `0` and
the source **Stride** parameter as `1`.
If you specify any other value for these parameters, you receive an
error message that the specified values are invalid.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **&src** — Start address of source memory location scalar

When reading the source address from this input port, set the **Copy
from** parameter to `Specified address` and
set the source **Specify address source** parameter
to `Input port`. When you choose these options, an
input port becomes available. The port label on the block changes
to `&src`, indicating that the block expects
the address to come from the input port. The ability to change the
address dynamically means that you can the block to copy different
variables by providing the variable address from an upstream block
in your model.

When reading the address from the input port, change the source **Data type** from the default `Inherit
from input port` to one of the data types in the **Data
type** list. If you do not change the parameter value, you
receive an error message. The error message indicates that the data
type cannot be inherited because the input port does not exist.

**Data Types:** `uint32`

### **src ofs** — Number of memory locations added to the start address before reading data scalar

When reading the offset value of data from this input port,
set the source **Specify offset source** parameter
to `Input port`. The source **Specify offset
source** parameter appears only when you select the **Use
offset when reading** parameter.

When you choose this option, an input port becomes available.
The port label on the block changes to `src ofs`,
indicating that the block expects the offset value to come from the
input port. This port enables your program to change the offset dynamically
during execution by providing the offset value as an input to the
block.

When reading the offset value from the input port, do not set
the **Copy from** parameter to `Input port`. If
you choose this option, you receive an error message that you cannot
specify the source offset parameter as an input port when copying
data from the input port.

**Data Types:** `uint32`

### **&dst** — Start address of destination memory location scalar

When reading the start address of the destination memory location
from this input port, set the **Copy to** parameter
to `Specified address` and set the destination **Specify
address source** parameter to `Input port`.
When you choose this option, an input port becomes available. The
port label on the block changes to `&dst`, indicating
that the block expects the address to come from the input port. The
ability to change the address dynamically means that you can the block
to copy different variables by providing the variable address from
an upstream block in your model.

**Data Types:** `uint32`

### **dst ofs** — Number of memory locations added to the start address before writing data scalar

When reading the offset value of the destination memory location
from this input port, set the destination **Specify offset
source** parameter to `Input port`. The
destination **Specify offset source** parameter appears
only when you select the **Use offset when reading** parameter.

When you choose this option, an input port becomes available.
The port label on the block changes to `dst ofs`,
indicating that the block expects the offset value to come from the
input port. This port enables your program to change the offset dynamically
during execution by providing the offset value as an input to the
block.

When reading the offset from the input port, do not set the **Copy
to** parameter to `Output port`. If you
choose this option, you receive an error message that cannot specify
the destination offset parameter as an input port when copying data
to output port.

**Data Types:** `uint32`
### Output

### **dst** — Output signal scalar | vector

When writing data to this output port, set the **Copy
to** parameter to `Output port`. When you
choose this option, an output port becomes available. The port label
on the block changes to `dst`, indicating that the
block writes data to the output port.

To inherit data type from the incoming signal, set the **Data
Type** parameter to `Inherit from source`.
Specify the destination **Offset** parameter as `0` and
the destination **Stride** parameter as `1`.
If you specify any other value for these parameters, you receive an
error message that the specified values are invalid.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

The Memory Copy dialog box contains multiple
tabs:

- **Source** — Identifies
  the sequential memory location to copy from. Specify the data type,
  size, and other attributes of the source variable.
- **Destination** —
  Specify the memory location to copy the source to and specify the
  attributes of the destination.
- **Options** —
  Select various parameters to control the copy process.

### Source

### **Copy from** — Source from where the block reads data `Input port` (default) | `Specified address` | `Specified source code symbol`

- `Input port` — An input port
  becomes available. The port label on the block changes to `src`,
  indicating that the block expects data to come from the input port.
- `Specified address` — The
  block reads the source address from the option that you select from
  the **Specify address source** parameter.

  If you set the **Specify address source** parameter
  to `Specify via dialog`, the block reads the source
  address that you specify in the **Address** parameter.

  If you set the **Specify address source** parameter
  to `Input Port`, an input port becomes available.
  The port label on the block changes to `&src`,
  indicating that the block expects the address to come from the input
  port
- `Specified source code symbol` —
  The block reads data from the symbol (variable) that you specify in
  the **Source code symbol** parameter.

If you select `Specified address` or `Specified
source code symbol` for the **Copy from** parameter,
change **Data type** from the default `Inherit
from input port` to one of the data types on the **Data
type** list.

### **Specify address source** — Source of memory location to read data `Specify via dialog` (default) | `Input port`

- `Specify via dialog` — The
  block reads data from the memory location that you specify in the **Address** parameter.
- `Input port` — An input port
  becomes available. The port label on the block changes to `&src`,
  indicating that the block expects the source address to come from
  the input port. The ability to change the address dynamically means
  that you can the block to copy different variables by providing the
  variable address from an upstream block in your model.

#### Dependencies

This parameter appears only when you set the **Copy
from** parameter to `Specified address`.

### **Source code symbol** — Symbol (variable) that contains the source address `myVariableSrc` (default) | `Any defined symbol`

The block does not verify whether the symbol is valid. A symbol
is valid only if it has an entry in the symbol table. If it is not
valid you get an error when you try to compile, link, and run your
generated code.

If the symbol contains a scalar value, specify `&` before
the symbol in this parameter. If the symbol contains a vector value,
specify only the symbol in this parameter.

#### Dependencies

This parameter appears only when you set the **Copy
from** parameter to `Specified source code symbol`.

### **Address** — Memory location of input data `hex2dec('00001000')` (default)

Specify the address in a decimal format or as a hexadecimal string
with single quotation marks. When you specify the address as a
hexadecimal string, pass that string as a parameter to the `hex2dec` function. This
function converts the string from the hexadecimal format to the decimal
format. The following example converts `0x1000` to its
decimal form.

```
4096 = hex2dec('1000');
```

For this example, you can specify either `4096` or `hex2dec('1000')` as
the address.

#### Dependencies

This parameter appears only when you set the **Copy
from** parameter to `Specified address` and
set the **Specify address source** to `Specify
via dialog`.

### **Data type** — Type of input data `Inherit from input port` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Use this parameter to specify the data type of your input data.
When you set this parameter to `Inherit from input port`,
the block inherits the data type from the value at the block input
port.

**Note**

If you select the **Copy from** parameter to `Specified
address` or `Specified source code symbol`,
change the **Data type** parameter from
the default `Inherit from input port` to one of the
data types on the **Data type** list.

### **Data length** — Number of elements to copy `1` (default) | `Any integer value greater than 1`

Specify the number of elements to copy from the source location. Each
element has the data type specified by the **Data
type** parameter.

### **Use offset when reading** — Specify an offset when reading data off (default) | on

When you select this parameter, the block reads the source offset
from the option that you select from the **Specify
offset source** parameter. When you clear this parameter,
the block reads data from the start address that you specify in the **Copy
from** parameter.

### **Specify offset source** — Source of offset for input data `Specify via dialog` (default) | `Input port`

- `Specify via dialog` — The
  block reads the offset value that you specify in the **Offset** parameter.
- `Input port` — An input port
  becomes available. The port label on the block changes to `src
  ofs`, indicating that the block expects the offset value
  to come from the input port. This port enables your program to change
  the offset dynamically during execution by providing the offset value
  as an input to the block.

#### Dependencies

This parameter appears only when you select the **Use offset when reading** parameter.

### **Offset** — Number of memory locations added to the start address before starting to read data `0` (default) | `Any integer value greater than 0`

An **Offset** instructs the block
whether to copy the first element of data at the input address, or
skip values before starting to copy the input to the destination.
The **Offset** defines how many input
elements to skip before copying the first value to the destination.

#### Dependencies

This parameter appears only when you select the **Use offset when reading** parameter.

### **Stride** — Spacing between the elements when reading input data `1` (default) | `Any integer value greater than 1`

Specify spacing between the elements when reading the input
data. A stride value equal to `1` means that the
generated code reads the input data sequentially. When you add a stride
value that is more than 1, the block skips that number of elements
and reads the elements from the resulting address.

The next two figures illustrate the stride concept. In the first
figure, you see data copied without a stride.

The second figure shows a stride value equal to 2. A stride
value 2 is applied when the block is copying the input to an output
location. You can specify a stride value for the output from the **Destination** tab by using the **Stride** parameter.

### Destination

### **Copy to** — Source to where the block writes data `Input port` (default) | `Specified address` | `Specified source code symbol`

- `Output port` — An output
  port becomes available. The port label on the block changes to `dst`,
  indicating that the block writes data to the output port.
- `Specified address` — The
  block copies data to the memory location that you that you specify
  in the **Specify address source** parameter.

  If you set the **Specify address source** parameter
  to `Specify via dialog`, the block reads the destination
  address that you specify in the **Address** parameter.

  If you set the **Specify address source** parameter to `Input
  Port`, an input port becomes available. The port
  label on the block changes to `&dst`,
  indicating that the block expects the destination address to
  come from the input port.
- `Specified source code symbol` —
  The block copies data to the symbol (variable) that you specify in
  the **Source code symbol** parameter.

### **Specify address source** — Source of memory location to write data `Specify via dialog` (default) | `Input port`

- `Specify via dialog` — The
  block writes data to the location that you specify in the **Address** parameter.
- `Input port` — An input port
  becomes available. The port label on the block changes to `&dst`,
  indicating that the block expects the destination address to come
  from the input port. The ability to change the address dynamically
  means that you can the block to copy different variables by providing
  the variable address from an upstream block in your model.

#### Dependencies

This parameter appears only when you set the **Copy
to** parameter to `Specified address`.

### **Source code symbol** — Symbol (variable) that contains the destination address `myVariableDst` (default) | `Any defined symbol`

The block does not verify whether the symbol is valid. A symbol
is valid only if it has an entry in the symbol table. If it is not
valid you get an error when you try to compile, link, and run your
generated code.

If the symbol contains a scalar value, specify `&` before
the symbol in this parameter. If the symbol contains a vector value,
specify only the symbol in this parameter.

#### Dependencies

This parameter appears only when you set the **Copy
to** parameter to `Specified source code symbol`.

### **Address** — Memory location where the block writes data `hex2dec('00001000')` (default)

Specify the address in a decimal format or as a hexadecimal string with single quotation
marks. When you specify the address as a hexadecimal string, pass that
vector as a parameter to the `hex2dec` function. This
function converts the string from hexadecimal format to decimal format.
The following example converts `Ox2000` to decimal
form.

```
8192 = hex2dec('2000');
```

For this example, you can specify either `8192` or `hex2dec('2000')` as
the address.

#### Dependencies

This parameter appears only when you set the **Copy
to** parameter to `Specified address` and
set the **Specify address source** to `Specify
via dialog`.

### **Data type** — Type of output data `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean` | `Inherit from source`

Use this parameter to specify the data type of your output.
When you set this parameter to `Inherit from source`,
the block inherits the data type from the input signal at the block
input port.

### **Use offset when writing** — Specify an offset when writing data off (default) | on

When you select this parameter, the block reads the offset from
the option that you select from the **Specify
offset source** parameter. When you clear this parameter,
the block reads data from the start address from the option that you
specify in the **Copy to** parameter.

### **Specify offset source** — Source of offset for writing data `Specify via dialog` (default) | `Input port`

- `Specify via dialog` — The
  block reads the offset value that you specify in the **Offset** parameter.
- `Input port` — An input port
  becomes available. The port label on the block changes to `dst
  ofs`, indicating that the block expects the offset value
  to come from the input port. This port enables your program to change
  the offset dynamically during execution by providing the offset value
  as an input to the block.

#### Dependencies

This parameter appears only when you select the **Use
offset when writing** parameter.

### **Offset** — Number of memory locations added to the start address before starting to write data `0` (default) | `Any integer value greater than 0`

An **Offset** instructs the block
whether to write the first element of data to the start address of
destination, or skip one or more locations at the destination before
writing the output. The **Offset** defines
how many values to skip in the destination before writing the first
value to the destination.

#### Dependencies

This parameter appears only when you select the **Use
offset when writing** parameter.

### **Stride** — Spacing between the elements when writing data `1` (default) | `Any integer value greater than 1`

Specify the spacing between the elements when writing the output
data. A stride value equal to one means that the generated code writes
the input data sequentially to the destination in consecutive locations.
When you add a stride value that is more than 1, the output data is
stored not sequentially, but skips elements equal to the stride.

This figure shows a stride value of 3 applied to writing the
input to an output location. You can specify a stride value for the
input from the **Source** tab by using
the **Stride** parameter. As shown in
the figure, you can apply input and output stride at the same time
to manipulate your memory more fully.

### **Sample time** — The rate, in seconds, at which memory copy operation occurs `Inf` (default) | `-1` | `Any value greater than 0`

The default value `Inf` instructs the block
to use a constant sample time. When you specify the **Sample
time** as `-1`, the Memory Copy block
inherits the sample time from the input. When there are no block inputs,
the block inherits the sample time from the Simulink® model.

### Options

### **Set memory value at initialization** — Specify a value and its source for initializing the destination memory location off (default) | on

When you select this option, you direct the block to initialize
the memory location to a specific value when you initialize your program
at run time. After you select this option, use the **Specify
initialization value source** parameter to set the value
that you want. Alternately, you can direct the block to get the initial
value from the block input.

If you select this parameter, set the destination **Copy
to** parameter to either `Specified address` or `Specified
source code symbol`. If you do not change the parameter
value, you receive an error message that memory cannot be set at initialization
when the destination is output port.

### **Specify initialization value source** — Specify the source of the initial value `Specify constant value` (default) | `Specify source code symbol`

- `Specify constant value` —
  Set a single value to use when your program initializes memory.

  The block reads the initialization value from the value that
  you specify in the **Initialization value (constant)** parameter.
- `Specify source code symbol` —
  Specifies a variable (a symbol) to use for the initial value.

  The block reads the initialization value from the symbol that
  you specify in the **Initialization value (source code symbol)** parameter.
  The block does not verify whether the symbol is valid. A symbol is
  valid only if it has an entry in the symbol table. If it is not valid,
  you get an error when you try to compile, link, and run your generated
  code.

#### Dependencies

This parameter appears only when you select the **Set
memory value at initialization** parameter.

### **Initialization value (constant)** — A constant value to initialize the memory location when you initialize your program at run time `1` (default) | `Any value`

#### Dependencies

This parameter appears only when you select the **Set
memory value at initialization** parameter and set the **Specify
initialization value source** to `Specify constant
value`.

### **Initialization value (source code symbol)** — A defined symbol (variable) that contains initialization value `myInitValueVariable` (default) | `Any defined symbol`

When you specify a symbol, the block does not verify whether
the symbol is valid. A symbol is valid only if it has an entry in
the symbol table. If it is not valid, you get an error when you try
to compile, link, and run your generated code.

#### Dependencies

This parameter appears only when you select the **Set
memory value at initialization** parameter and set the **Specify
initialization value source** to `Specify source
code symbol`.

### **Apply initialization value as mask** — Specify the initialization value as mask off (default) | on

The initialization value is treated as a string of bits for
the mask.

The block performs the bitwise operation on the initialization
value to manipulate register contents at the bit level. The operator
that you specify in the **Bitwise operator** parameter
determines the bitwise operation.

**Note**

To use your initialization value as a mask, set the destination **Copy
to** parameter to either `Specified address` or `Specified
source code symbol`.

#### Dependencies

This parameter appears only when you select the **Set
memory value at initialization** parameter.

### **Bitwise operator** — Specify bitwise operator for manipulating memory value in the register `bitwise AND` (default) | `bitwise OR` | `bitwise exclusive OR` | `left shift` | `right shift`

To use the initialization value as a mask, from the **Bitwise
operator** list, select one of the entries listed in this
table.

| Bitwise Operator List Entry | Description |
| --- | --- |
| `bitwise AND` | Apply the mask value as a bitwise AND to the value in the register. |
| `bitwise OR` | Apply the mask value as a bitwise OR to the value in the register. |
| `bitwise exclusive OR` | Apply the mask value as a bitwise exclusive OR to the value in the register. |
| `left shift` | Shift the bits in the register to the left by the number of bits represented by the initialization value. For example, if your initialization value is 3, the block shifts the register value to the left by 3 bits. In this case, the value must be a positive integer. |
| `right shift` | Shift the bits in the register to the right by the number of bits represented by the initialization value. For example, if your initialization value is 6, the block shifts the register value to the right by 6 bits. In this case, the value must be a positive integer. |

#### Dependencies

This parameter appears only when you select the **Apply
initialization value as mask** parameter.

### **Set memory value at termination** — Specify a value of the target memory after the write operation off (default) | on

This parameter initializes memory when the program starts to
access the target memory location and directs the program to set memory
to a specific value when the program terminates.

### **Termination value** — A constant value of the target memory after the write operation `1` (default) | `Any value`

This parameter appears only when you select the **Set
memory value at termination** parameter.

### **Set memory value only at initialization/termination** — Specify the periods of program execution at which the block performs copy operation off (default) | on

This Memory Copy block performs operations at
three periods during program execution: initialization, real-time
operations, and termination. When you select this parameter, the block
performs only the memory initialization and termination operations.
It does not copy data during real-time operations.

### **Insert custom code before memory write** — Specify a custom ANSI C code that you want to insert into the generated code before the block writes to a specified memory location off (default) | on

The block inserts a custom ANSI C code that you specify
in the **Custom code** parameter before the write
operation.

You can use the custom code capability to lock and unlock registers
before and after accessing them. For example, some processors have
registers that you want to unlock with the EALLOW macro before your
program accesses them.

### **Custom code** — A custom ANSI C code that you insert into the generated code before the block writes to a specified memory location `/* Custom Code Before Write*/` (default)

The code that you specify in this parameter is the code that
appears in the generated code.

#### Dependencies

To enable this parameter, select the **Insert
custom code before memory write** parameter.

### **Insert custom code after memory write** — Specify a custom ANSI C code that you insert into the generated code after the block writes to the specified memory location off (default) | on

The block inserts a custom ANSI C code that you specify
in the **Custom code** parameter after the write
operation.

You can use the custom code capability to lock and unlock registers
before and after accessing them. For example, some processors have
registers that you want to lock with the EDIS macro after your program
accesses them.

### **Custom code** — A custom ANSI C code that you insert into the generated code after the block writes to the specified memory location `/* Custom Code After Write*/` (default)

The code that you specify in this parameter is the code that
appears in the generated code.

#### Dependencies

This parameter appears only when you select the **Insert
custom code after memory write** parameter.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities Simulink Support Package for Arduino Hardware / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Copy to and from memory section

In generated code, the Memory Copy block copies
variables or data to and from processor memory as you have configured
with block parameters. Your model can contain as many of these blocks
as you require to manipulate memory on your processor.

Each block works with one variable, address, or set of addresses provided to the block. Using
the parameters of this block you specify the source and the destination for the memory
copy and options for initializing the memory locations.

At run time, you can change options like the memory stride and
offset. You can write to memory at program initialization, at program
termination, and at every sample time by selecting various parameters
in the block. The initialization process occurs once, rather than
occurring for every read and write operation.

With the custom source code options, the block enables you to add custom ANSI® C source code before and after each memory read and write (copy) operation.

### Block Operations

This block performs operations at three periods during program
execution: initialization, real-time operations, and termination. With
the options for setting the memory initialization and termination,
you control when and how the block initializes memory, copies to and
from memory, and terminates memory operations. The parameters enable
you to turn on and off memory operations in the three periods, independently
of each other.

### Copy Memory

When you use this block to copy an individual data element from
the source to the destination, the block copies the element from the
source in the source data type, and then casts the data element to
the destination data type that you specify in the block parameters.
