---
type: simulink-block
title: 'CLA Subsystem'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'clasubsystem'
documentation_source_path: 'ref/clasubsystem.html'
language: en
---

# CLA Subsystem

## Ports

### Input

### **In** — Signal input to a subsystem scalar | vector | matrix

Placing an Inport block in a subsystem adds an external
input port to the Subsystem block. The port label matches
the name of the Inport block.

Use Inport blocks to get signals from the local
environment.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Signal output from a subsystem scalar | vector | matrix

Placing an Outport block in a subsystem adds an output
port from the Subsystem block. The port label on the
Subsystem block is the name of the
Outport block.

Use Outport  blocks to send signals to the local
environment.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

Parameters on the Code Generation tab require a Simulink®
Coder™ or Embedded Coder® license.

### Main

### **Show port labels** — Display options for port labels `FromPortIcon` (default) | `FromPortBlockName` | `SignalName`

Select how to display port labels on the Subsystem
block icon.

`none`
:   Do not display port labels.

`FromPortIcon`
:   If the corresponding port icon displays a signal name,
    display the signal name on the Subsystem
    block. Otherwise, display the port block name or the port
    number if the block name is a default name.

`FromPortBlockName`
:   Display the name of the corresponding port block on the
    Subsystem block.

`SignalName`
:   If the signal connected to the port is named, display the
    name of the signal on the Subsystem block.
    Otherwise, display the name of the corresponding port
    block.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `ShowPortLabels` |
| **Type**: character vector |
| **Value**: `'FromPortIcon'` | `'FromPortBlockName'` | `'SignalName'` |
| **Default**: `'FromPortIcon'` |

### **Read/Write permissions** — Levels of access to contents of subsystem `ReadWrite` (default) | `ReadOnly` | `NoReadOrWrite`

Control user access to the contents of the subsystem.

`ReadWrite`
:   Enable opening and modification of subsystem
    contents.

`ReadOnly`
:   Enable opening but not modification of the subsystem. If
    the subsystem resides in a block library, you can create and
    open links to the subsystem and can make and modify local
    copies of the subsystem but cannot change the permissions or
    modify the contents of the original library instance.

`NoReadOrWrite`
:   Disable opening or modification of subsystem. If the
    subsystem resides in a library, you can create links to the
    subsystem in a model but cannot open, modify, change
    permissions, or create local copies of the subsystem.

**Note**

You do not receive a response if you attempt to view the contents
of a subsystem whose **Read/Write permissions**
parameter is set to `NoReadOrWrite`. For
example, when double-clicking such a subsystem, Simulink does not open the subsystem and does not display any
messages.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `Permissions` |
| **Type**: character vector |
| **Value**: `'ReadWrite'` | `'ReadOnly'` | `'NoReadOrWrite'` |
| **Default**: `'ReadWrite'` |

### **Name of error callback function** — Name of function to be called if error occurs `''` (default) | function name

Enter name of a function to be called if an error occurs while
Simulink is executing the subsystem.

Simulink passes two arguments to the function: the handle of the
subsystem and a character vector that specifies the error type. If no
function is specified, Simulink displays a generic error message if executing the
subsystem causes an error.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `ErrorFcn` |
| **Type**: character vector |
| **Value**: `''` | `'<function name>'` |
| **Default**: `''` |

### **Permit hierarchical resolution** — Resolution for workspace variable names `All` (default) | `ExplicitOnly` | `None`

Select whether to resolve names of workspace variables referenced by
this subsystem.

For more information, see Symbol Resolution and
Symbol Resolution Process.

`All`
:   Resolve all names of workspace variables used by this
    subsystem, including those used to specify block parameter
    values and Simulink data objects (for example, `Simulink.Signal` objects).

`ExplicitOnly`
:   Resolve only names of workspace variables used to specify
    block parameter values, data store memory (where no block
    exists), signals, and states marked as “must
    resolve”.

`None`
:   Do not resolve any workspace variable names.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `PermitHierarchicalResolution` |
| **Type**: character vector |
| **Value**: `'All'` | `'ExplicitOnly'` | `'None'` |
| **Default**: `'All'` |

### Code Generation

### **Function packaging** — Code format `Nonreusable function` (default) | `Inline`

Select the code format to be generated for CLA subsystem.

**Note**

CLA Subsystem block doesn’t support `Auto`
and `Reusable function` code format.

`Inline`
:   Simulink
    Coder and Embedded Coder inline the subsystem unconditionally and
    entire algorithm is inlined to the CLA task (.cla) file. For
    more, see Method 2 - Inline Code Generation for CLA Subsystem

`Nonreusable function`
:   In this subsystem, the code for the algorithm in CLA is
    generated as a separate `.C`  file along
    with data. For more, see Method 1 - Nonreusable Function Code Generation for CLA Subsystem (Recommended).

    Subsystems with this setting generate functions that might
    have arguments depending on the **Function
    interface** parameter setting. You can name the
    generated function and file using parameters
    **Function name** and **File
    name (no extension)**. These functions are not
    reentrant.

#### Dependencies

- This parameter requires Simulink
  Coder for code generation.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWSystemCode` |
| **Type**: character vector |
| **Value**: | `'Inline'` | `'Nonreusable function'` | |
| **Default**: `'Nonreusable function'` |

### **Function name options** — How to name generated function `Auto` (default) | `Use subsystem name` | `User specified`

Select how Simulink
Coder names the function it generates for the subsystem.

If you have an Embedded Coder license, you can control function names with options on
the Configuration Parameter **Code Generation** > **Identifiers** pane.

`Auto`
:   Assign a unique function name using the default naming
    convention,
    `model_subsystem()`,
    where *`model`* is the name of the
    model and *`subsystem`* is the name
    of the subsystem (or that of an identical one when code is
    being reused).

`Use subsystem name`
:   Use the subsystem name as the function name. By default,
    the function name uses the naming convention
    `model_subsystem`.

`User specified`
:   Enable the **Function name** field. Enter
    any legal C or C++ function name, which must be
    unique.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function` or `Reusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWFcnNameOpts` |
| **Type**: character vector |
| **Value**: `'Auto'` | `'Use subsystem name'` | `'User specified'` |
| **Default**: `'Auto'` |

### **Function name** — Name of function for subsystem code `''` (default) | function name

Specify a unique, valid C or C++ function name for subsystem
code.

Use this parameter if you want to give the function a specific name
instead of allowing the Simulink
Coder code generator to assign its own autogenerated name or use
the subsystem name.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set the **Function
  name options** parameter to
  `User specified`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWFcnName` |
| **Type**: character vector |
| **Value**: `''` | `'<function name>'` |
| **Default**: `''` |

### **File name options** — How to name generated file `User specified` (default)

Select how Simulink
Coder names the separate file for the function it generates for
the CLA subsystem. Ensure that you set the **File name
options** parameter to `User
specified` for CLA Subsystem.

`User specified`
:   This option enables the **File name (no
    extension)** text entry field. The code
    generator uses the name you enter as the file name. Enter
    any file name, but do not include the `.c`
    or `.cpp` (or any other) extension. This
    file name need not be unique.

    **Note**

    While a subsystem source file name need not be
    unique, you must avoid giving nonunique names that
    result in cyclic dependencies (for example,
    `sys_a.h` includes
    `sys_b.h`,
    `sys_b.h` includes
    `sys_c.h`, and
    `sys_c.h` includes
    `sys_a.h`).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWFileNameOpts` |
| **Type**: character vector |
| **Value**: `'User specified'` |
| **Default**: `'User specified'` |

### **File name (no extension)** — Name of generated file `sample_cla` (default) | file name

The algorithm inside CLA is generated in the source file. (For example
`sample_cla.c` which includes
`sample_cla.h`). The file name that you specify
does not have to be unique. However, avoid giving non-unique names that
result in cyclic dependencies (for example, `sys_a.h`
includes `sys_b.h`, `sys_b.h` includes
`sys_c.h`, and `sys_c.h` includes
`sys_a.h`).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **File name
  options** to `User
  specified`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWFileName` |
| **Type**: character vector |
| **Value**: `''` | `'<file name>'` |
| **Default**: `''` |

### **Function interface** — Select to use arguments with generate function `void_void` (default)

Select to use arguments with generated function. Ensure that you set
the **Function interface** parameter to
`void_void` for CLA Subsystem.

`void_void`
:   Generate a function without arguments and pass data as
    global variables. For example:

    ```
    void subsystem_function(void)
    ```

For more information, see:

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `FunctionInterfaceSpec` |
| **Type**: character vector |
| **Value**: `'void_void'` |
| **Default**: `'void_void'` |

### **Function with separate data** — Control code generation for subsystem on (default) | off

Generate subsystem function code in which the internal data for an
atomic subsystem is separated from its parent model and is owned by the
subsystem.

off
:   Do not generate subsystem function code in which the
    internal data for an atomic subsystem is separated from its
    parent model and is owned by the subsystem.

on
:   Generate subsystem function code in which the internal
    data for an atomic subsystem is separated from its parent
    model and is owned by the subsystem. The subsystem data
    structure is declared independently from the parent model
    data structures. A subsystem with separate data has its own
    block I/O and `DWork` data structure. As a
    result, the generated code for the subsystem is easier to
    trace and test. The data separation also tends to reduce the
    maximum size of global data structures throughout the model,
    because they are split into multiple data structures.

    **Note**

    It is recommended that the **Function with
    separate data** parameter is set to
    `on`.

For details on how to generate modular function code for an atomic
subsystem, see Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder).

For details on how to apply memory sections to atomic subsystems, see
Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `FunctionWithSeparateData` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **Memory section for initialize/terminate functions** — Select how to apply memory sections `C28xFunction` (default)

Select how Embedded Coder applies memory sections to the subsystem initialization
and termination functions. For CLA Subsystem, select
`C28xFunction`. With this selection the
initialize and terminate functions are protected with CLA complier tag
such that it is compiled only by C28x compiler.

**Note**

Ensure that the model is loaded with
**tic2000demospkg** package where
C28xFunction is defined.

For example, if name of the initialize function is
`subsystem_initialize`
then

```
#ifndef __TMS320C28XX_CLA__
void subsystem_initialize()
{
//body of the function
}
#endif
```

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWMemSecFuncInitTerm` |
| **Type**: character vector |
| **Value**: `C28xFunction` |
| **Default**: `C28xFunction` |

### **Memory section for execution functions** — Select how to apply memory sections `ClaFunction` (default)

Select how Embedded Coder applies memory sections to the subsystem execution
functions. For CLA Subsystem, select
`ClaFunction`. With this selection the
execution functions are protected with CLA complier tag such that it is
compiled only by CLA compiler.

**Note**

Ensure that the model is loaded with
**tic2000demospkg** package where ClaFunction
is defined.

For example, if name of the execution function is
`subsystem`
then

```
#ifdef __TMS320C28XX_CLA__
void subsystem()
{
//body of the function
}
#endif
```

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function`.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWMemSecFuncExecute` |
| **Type**: character vector |
| **Value**: `ClaFunction` |
| **Default**: `ClaFunction` |

### **Memory section for constants** — Select how to apply memory sections `ClaDataRAM` (default)

Select how Embedded Coder applies memory sections to the subsystem constants. For
CLA Subsystem, select `ClaDataRAM`. Memory
section for constants parameter allows the constants to be stored in CLA
data RAM.

Ensure that the model is loaded with
**tic2000demospkg** package where ClaDataRAM is
defined.

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function` and select the
  **Function with separate data**
  parameter.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWMemSecDataConstants` |
| **Type**: character vector |
| **Value**: `ClaDataRAM` |
| **Default**: `ClaDataRAM` |

### **Memory section for internal data** — Select how to apply memory sections `ClaDataRAM` (default)

Select how Embedded Coder applies memory sections to the subsystem internal data.
For CLA Subsystem, select `ClaDataRAM`. Memory
section for internal data parameter allows the internal data to be
stored in CLA data RAM.

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function` and select the
  **Function with separate data**
  parameter.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWMemSecDataInternal` |
| **Type**: character vector |
| **Value**: `ClaDataRAM` |
| **Default**: `ClaDataRAM` |

### **Memory section for parameters** — Select how to apply memory sections `ClaDataRAM` (default)

Select how Embedded Coder applies memory sections to the subsystem parameters. For
CLA Subsystem, select `ClaDataRAM`. Memory
section for parameters allows the parameters to be stored in CLA data
RAM

#### Dependencies

- To enable this parameter, set **Function
  packaging** to `Nonreusable
  function` and select the
  **Function with separate data**
  parameter.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `RTWMemSecDataParameters` |
| **Type**: character vector |
| **Value**: `ClaDataRAM` |
| **Default**: `ClaDataRAM` |

### Subsystem Reference

### **Subsystem file name** — File name for referenced subsystem string | character vector

#### Dependencies

To access this parameter, click the **Convert**
button.

For more information on how to convert a subsystem to a referenced
subsystem, see Convert Subsystem to a Referenced Subsystem.

## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Group blocks to execute algorithm inside CLA

A CLA Subsystem block contains a subset of blocks within a model or
system. CLA Subsystem is a triggered subsystem which is caused by a CLA
Task block.

CLA Subsystem block can only be used along with CLA Task block.

CLA Subsystem requires you to load `tic2000demospkg` package in the
model with a valid TI C2000™ based hardware board. To load the `tic2000demospkg`
package in the model, follow the below steps.

- From Simulink toolstrip, navigate to **Apps** and click
  **Embedded Coder**.

  CLA-APPS
- Go to **C Code**  > **Code Interface** and click **Embedded Coder Dictionary
  (Model)**.

  Code-Interface
- From the Embedded Coder Dictionary window, go to **Storage
  Class** and click **Manage Packages**. If you
  do not find the `tic2000demospkg`, click
  **Refresh** and load the package. For more information,
  see Data Exchange Between CLA and C28x CPU.

  Manage packages

**Note**

- To know more about how to use the subsystem for CLA, refer Overview of CLA Configuration for C2000 Processors Using Subsystem.
- CLA Subsystem block is derived from Subsystem block with additional
  parameter configurations specific to CLA. It is recommended to use
  the options provided in this block for successful usage of CLA
  Subsystem.
- Not all TI C2000 hardware board variants support CLA. For
  instance, within the TI Piccolo F2805x processor family, only the
  F28055 and F28053 processors support CLA, while the F28054, F28052,
  F28051, and F28050 processors do not.
