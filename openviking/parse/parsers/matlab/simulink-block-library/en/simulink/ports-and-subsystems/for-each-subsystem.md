---
type: simulink-block
title: 'For Each Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Ports and Subsystems'
documentation_page: 'foreachsubsystem'
documentation_source_path: 'slref/foreachsubsystem.html'
language: en
---

# For Each Subsystem

## Ports

### Input

### **In** — Signal input to Subsystem block scalar | vector | matrix

Signal input to a Subsystem block, specified as a
scalar, vector, or matrix. Placing an Inport block in a
Subsystem block adds an external input port to the
block. The port label matches the name of the Inport
block.

Use Inport blocks to receive signals from the local
environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Signal output from Subsystem block scalar | vector | matrix

Signal output from a Subsystem block, returned as a
scalar, vector, or matrix. Placing an Outport block in a
Subsystem block adds an external output port to the
block. The port label matches the name of the Outport
block.

Use Outport blocks to send signals to the local
environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Show port labels** — Display options for port labels `FromPortIcon` (default) | `FromPortBlockName` | `SignalName` | `none`

Select how to display port labels on the Subsystem block icon.

- `none` — Do not display port labels.
- `FromPortIcon` — If the corresponding port icon displays a signal name, display the signal name on the Subsystem block. Otherwise, display the port block name or the port number if the block name is a default name.
- `FromPortBlockName` — Display the name of the corresponding port block on the Subsystem block.
- `SignalName` — If the signal connected to the port is named, display the name of the signal on the Subsystem block. Otherwise, display the name of the corresponding port block.

For port label editing on Subsystem blocks, see Edit Port Labels on Subsystem Blocks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **Values:** | `'FromPortIcon'` (default) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — Levels of access to contents of subsystem `ReadWrite` (default) | `ReadOnly` | `NoReadOrWrite`

Control user access to the contents of the subsystem.

- `ReadWrite` — Enable opening and modification of subsystem contents.
- `ReadOnly` — Enable opening but not modification of the subsystem. If the subsystem resides in a block library, you can create and open links to the subsystem and can make and modify local copies of the subsystem but cannot change the permissions or modify the contents of the original library instance.
- `NoReadOrWrite` — Disable opening or modification of subsystem. If the subsystem resides in a library, you can create links to the subsystem in a model but cannot open, modify, change permissions, or create local copies of the subsystem.

You do not receive a response if you attempt to view the contents of a subsystem whose **Read/Write permissions** parameter is set to `NoReadOrWrite`. For example, when double-clicking such a subsystem, the software does not open the subsystem and does not display any messages.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **Values:** | `'ReadWrite'` (default) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — Name of function to be called if error occurs no default

Enter the name of a function to be called if an error occurs while the software executes the
subsystem.

The software passes two arguments to the function: the handle of the subsystem and a
character vector that specifies the error type. If no function is specified, the software
displays a generic error message if executing the subsystem causes an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — Resolution for workspace variable names `All` (default) | `ExplicitOnly` | `None`

Select whether to resolve names of workspace variables referenced by this subsystem.

For more information, see Symbol Resolution and Symbol Resolution Process.

- `All` — Resolve all names of workspace variables used by this subsystem, including those used to specify block parameter values and Simulink data objects (for example, `Simulink.Signal` objects).
- `ExplicitOnly` — Resolve only names of workspace variables used to specify block parameter values, data store memory (where no block exists), signals, and states marked as “must resolve”.
- `None` — Do not resolve any workspace variable names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **Values:** | `'All'` (default) | `'ExplicitOnly'` | `'None'` |

### **Minimize algebraic loop occurrences** — Option to eliminate artificial algebraic loops `off` (default) | `on`

Try to eliminate any artificial algebraic loops that include the atomic subsystem

- `off` — Do not try to eliminate any artificial algebraic loops that include the atomic subsystem.
- `on` — Try to eliminate any artificial algebraic loops that include the atomic subsystem.

#### Dependencies

To enable this parameter, select **Treat as atomic unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MinAlgLoopOccurrences` |
| **Values:** | `'off'` (default) | `'on'` |

### Code Generation

Parameters on the Code Generation tab require a Simulink
Coder or Embedded Coder® license.

### **Function packaging** — Code format `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

Select the code format to be generated for an atomic (nonvirtual) subsystem.

- `Auto` — The software chooses the optimal format for you
  based on the type and number of instances of the subsystem that exist in the
  model.
- `Inline` — The software inlines the subsystem
  unconditionally.
- `Nonreusable function` — If **Filename
  options** is set to `Auto`, the software packages
  separate functions in the model file. If **File name options** is
  set to `Use subsystem name`, `Use function
  name`, or `User specified` using different
  filenames, the software packages separate functions in separate files.

  Subsystems with this setting generate functions that might have arguments depending on
  the Function interface parameter setting.
  You can name the generated function and file using parameters Function name and File name (no extension), respectively.
  These functions are not reentrant.
- `Reusable function` — The software generates a function
  with arguments that allows reuse of subsystem code when a model includes multiple
  instances of the subsystem.

  This option also generates a function with arguments that allows subsystem code to
  be reused in the generated code of a model reference hierarchy that includes multiple
  instances of a subsystem across referenced models. In this case, the subsystem must be
  in a library.

For more information, see:

- Generate Code and Executables for Individual Subsystems (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- Generate Subsystem Code as Separate Function and Files (Simulink Coder)
- Generate Reusable Code from Library Subsystems Shared Across Models (Simulink Coder)

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Reusable function`.

#### Tips

- When you want multiple instances of a subsystem to be represented as one
  reusable function, you can designate each one of them as
  `Auto` or as `Reusable
  function`. Using one or the other is best, as using both creates two
  reusable functions, one for each designation. The outcomes of these choices differ
  only when reuse is not possible. Selecting `Auto` does not
  allow control of the function or filename for the subsystem code.
- The `Reusable function` and `Auto`
  options both try to determine if multiple instances of a subsystem exist and if the
  code can be reused. The difference between the behavior of each option is that when
  reuse is not possible:

  - `Auto` yields inlined code, or if circumstances
    prohibit inlining, separate functions for each subsystem instance.
  - `Reusable function` yields a separate function
    with arguments for each subsystem instance in the model.
- If you select `Reusable function` while your generated
  code is under source control, set **File name options** to
  `Use subsystem name`, `Use function
  name`, or `User specified`. Otherwise, the
  names of your code files change whenever you modify your model, which prevents
  source control on your files.
- If you select an option other than `Auto` or
  `Inline` and the model configuration parameter
  **States**, the code generator produces separate output and
  update methods. The code generator does not take into account the
  **Combine output and update methods for code generation and
  simulation** specification.

#### Dependencies

- This parameter requires a Simulink
  Coder license for code generation.
- To enable this parameter, select **Treat as atomic
  unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWSystemCode` |
| **Values:** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — How to name generated function `Auto` | `Use subsystem name` | `User specified`

Select how the software names the function it generates for the subsystem.

If you have an Embedded Coder license, you can control function names with options on the Configuration
Parameter **Code Generation** > **Identifiers** pane.

- `Auto` — Assign a unique function name using the default
  naming convention,
  `model_subsystem()`,
  where *`model`* is the name of the model and
  *`subsystem`* is the name of the subsystem, or that of an
  identical one when code is being reused.

  If you select `Reusable function` for the
  **Function packaging** parameter and a model reference hierarchy
  contains multiple instances of the reusable subsystem, in order to generate reusable
  code for the subsystem, **Function name options** must be set to
  `Auto`.
- `Use subsystem name` — Use the subsystem name as the
  function name. By default, the function name uses the naming convention
  `model_subsystem`.

  When a subsystem is in a library block and the subsystem parameter Function packaging is set to
  `Reusable function`, if you set the
  `Use subsystem name` option, the code
  generator uses the name of the library block for the subsystem function
  name and filename.
- `User specified` — Enable the **Function
  name** field. Enter any legal C or C++ function name, which must be
  unique.

For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Use subsystem name`.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnNameOpts` |
| **Values:** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — Name of function for subsystem code no default

Specify a unique, valid C or C++ function name for subsystem code.

Use this parameter if you want to give the function a specific name instead of
allowing the Simulink
Coder code generator to assign its own autogenerated name or use the subsystem
name. For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function name options** to
  `User specified`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnName` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **File name options** — How to name generated file `Auto` | `Use subsystem name` | `Use function name` | `User specified`

Select how the software names the separate file for the function it generates for the
subsystem.

- `Auto` — Depending on the configuration of the subsystem
  and how many instances are in the model, `Auto` yields
  different results.

  - If the code generator does *not* generate a separate file
    for the subsystem, the subsystem code is generated within the code module
    generated from the subsystem parent system. If the subsystem parent is the model
    itself, the subsystem code is generated within
    `model.c` or
    `model.cpp`.
  - If you select `Reusable function` for the
    **Function packaging** parameter and your generated code is
    under source control, consider specifying a **File name
    options** value other than `Auto`. This
    prevents the generated filename from changing due to unrelated model
    modifications, which is problematic for using source control to manage
    configurations.
  - If you select `Reusable function` for the
    **Function packaging** parameter and a model reference
    hierarchy contains multiple instances of the reusable subsystem, in order to
    generate reusable code for the subsystem, **File name
    options** must be set to `Auto`.
- `Use subsystem name` — The code generator generates a
  separate file, using the subsystem (or library block) name as the filename.

  When **File name options** is set to `Use subsystem
  name`, the subsystem filename is mangled if the model contains
  Model blocks, or if a model reference target is being generated for
  the model. In these situations, the filename for the subsystem consists of the
  subsystem name prefixed by the model name.
- `Use function name` — The code generator uses the
  function name specified by **Function name options** as the
  filename.
- `User specified` — This option enables the
  **File name (no extension)** text entry field. The code generator
  uses the name you enter as the filename. Enter any filename, but do not include the
  `.c` or `.cpp` (or any other) extension. This
  filename need not be unique.

  While a subsystem source filename need not be unique, you must avoid giving nonunique
  names that result in cyclic dependencies. For example, `sys_a.h`
  includes `sys_b.h`, `sys_b.h` includes
  `sys_c.h`, and `sys_c.h` includes
  `sys_a.h`.

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Use function name`.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileNameOpts` |
| **Values:** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — Name of generated file no default

The filename that you specify does not have to be unique. However, avoid giving
non-unique names that result in cyclic dependencies. For example,
`sys_a.h` includes `sys_b.h`,
`sys_b.h` includes `sys_c.h`, and
`sys_c.h` includes `sys_a.h`.

For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **File name options** to
  `User specified`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileName` |
| **Values:** | `''` (default) | filename in quotes |
| **Data Types:** | `char` | `string` |

### **Function interface** — How to use arguments with generated function `void_void` (default) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

Select how to use arguments with the generated function.

- `void_void` — Generate a function without arguments and
  pass data as global variables. For example:

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — Generate a function that
  uses arguments instead of passing data as global variables. This specification reduces
  global RAM. This option might reduce code size and improve execution speed and enable
  the code generator to apply additional optimizations. For
  example:

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  In some cases, when generating optimized code, the code generator might not
  generate a function that has arguments.
- `Allow arguments (Match graphical interface)` — Generate
  a function interface that uses arguments that match the Subsystem
  graphical block interface. The generated function interface is predictable and does
  not change. A predictable interface can be useful for debugging and testing your code
  and integrating with external applications. For example, if a model has two
  Inport blocks and two Outport blocks, then the
  generated function interface
  is:

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

For more information, see:

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionInterfaceSpec` |
| **Values:** | `'void_void'` (default) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — Control code generation for subsystem `off` (default) | `on`

Generate subsystem function code in which the internal data for an atomic subsystem is
separated from its parent model and is owned by the subsystem.

- `off` — Do not generate subsystem function code in which the
  internal data for an atomic subsystem is separated from its parent model and is owned
  by the subsystem.
- `on` — Generate subsystem function code in which the internal
  data for an atomic subsystem is separated from its parent model and is owned by the
  subsystem. The subsystem data structure is declared independently from the parent
  model data structures. A subsystem with separate data has its own block I/O and
  `DWork` data structure. As a result, the generated code for the
  subsystem is easier to trace and test. The data separation also tends to reduce the
  maximum size of global data structures throughout the model, because they are split
  into multiple data structures.

For details on how to generate modular function code for an atomic subsystem, see
Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder).

For details on how to apply memory sections to atomic subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionWithSeparateData` |
| **Values:** | `'off'` (default) | `'on'` |

### **Memory section for initialize/terminate functions** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem initialization and
termination functions.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to the subsystem
  system code, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) and Model Configuration Parameters: Code Generation (Simulink Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncInitTerm` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for execution functions** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how Embedded Coder applies memory sections to the subsystem execution functions.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to the subsystem
  system code, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) and Model Configuration Parameters: Code Generation (Simulink Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncExecute` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for constants** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem constants.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem data.
- `Default` — Do not apply memory sections to the subsystem
  data, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structures in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataConstants` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for internal data** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem internal data.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem data.
- `Default` — Do not apply memory sections to the subsystem
  data, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structures in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataInternal` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for parameters** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem parameters.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to
  the subsystem system code, overriding any model-level
  specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structure in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataParameters` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

When you generate HDL code for the For Each Subsystem, the code
generator attempts to use a `for-generate` loop that iterates
through elements of the input and output signals. The for-generate loop improves
readability and reduces the number of lines of code, which could otherwise be
hundreds of lines of code for large vector signals. The subsystem supports vector
and 3D matrix input signals. See Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder).

You can use a nonzero partition offset for HDL code generation. The code generator
supports a scalar, vector, or matrix as mask parameter values. You can generate HDL
code for element, 1D, and 2D partitions of mask parameters inside a For Each
Subsystem block. Inside the For Each Subsystem block, use
the mask parameter as the **Constant value** parameter in Constant blocks or as the
**Gain** parameter in Gain blocks.

**Limitations**

- You cannot use the For Each Subsystem block as the
  DUT.
- You cannot set the `SpecifiedNumIters` parameter of
  the For Each block for HDL
  code generation. HDL code generation returns an error when the value of
  `SpecifiedNumIters` is not equal to the default
  value of `-1`.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining (HDL Coder). |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

**Target Specification**

This block cannot be the DUT, so the block property settings in the **Target
Specification** tab are ignored.

**Complex Data Support**

The block does not support complex data signals for HDL code generation. To
input complex signals, convert the complex signal to an array of signals, and
then input to the block. To learn more, see Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder).

**Generate HDL Code with Algebraic Loops**

To generate HDL code for models that contain For Each Subsystem
blocks:

- In the Configuration Parameters dialog box, click
  **Diagnostics**, and set the
  **Algebraic loop** parameter to
  `none` or
  `warning`.
- Open the block mask for the For Each Subsystem block
  and select the **Minimize algebraic loop
  occurrences** parameter.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2010a**

### R2024b: Add signal breakpoints and port value labels to iteration number outputs in iterator subsystems

You can now pause a simulation on a particular iteration of an iterator subsystem by adding
signal breakpoints to signals produced by:

- Iteration number output ports of While Iterator blocks inside While Iterator Subsystem blocks
- Iterator value output ports of For Iterator blocks inside For Iterator Subsystem blocks
- Partition index output ports of For Each blocks inside For Each Subsystem blocks

In previous releases, you could add a breakpoint in these locations, but the breakpoints
did not pause the simulation and appeared as invalid in the block diagram.

Port value labels at the same locations now display the iteration number. In previous releases, port value labels at these locations showed `inaccessible`.

For an example, see Debug Simulation of Iterator Subsystem.

## Description

Apply algorithm to individual elements or subarrays of input signals or mask parameters

The For Each Subsystem block is a Subsystem block preconfigured as a starting point for creating a subsystem
that repeats execution during a simulation time step on each element or subarray of an
input signal or mask parameter array.

For Each Subsystem block icon, displayed alongside contents of for-each subsystem, consisting of a For Each block, an Inport block, and an Outport block.

The set of blocks within the subsystem represents the algorithm applied to a single
element or subarray of the original signal or mask parameter array. Inside the
subsystem, each block that has states maintains separate sets of states for each element
or subarray that it processes. Consequently, the operation of this subsystem is similar
in behavior to copying the contents of the subsystem for each element in the original
input signal or mask parameter array and then processing each element using its
respective copy of the subsystem. As the set of blocks in the subsystem processes the
elements or subarrays, the subsystem concatenates the results to form output
signals.

### Configure the Subsystem

The For Each Subsystem block contains a For Each block that acts as a control
block for the subsystem. Specify the parameters of the For Each block
to configure the decomposition of the subsystem inputs or mask parameters into
elements or subarrays and to configure the concatenation of the individual results
into output signals. The block parameters **Partition Dimension**
and **Partition Width** specify the dimension through which to
slice the input signal or mask parameter array and the width of each slice,
respectively. To partition a row vector, specify the **Partition
Dimension** as `2`. To partition a column vector,
specify the **Partition Dimension** as `1`. Use
the parameter **Partition Offset** to specify a gap or an overlap
between partitions. Specify a **Number of iterations** to limit
processing to a subset of the data. To learn more about the block parameters, see
For Each.

**Partition Input Signals to the Subsystem**

To specify which input signals to partition for each iteration in a for-each
subsystem, use the **Input Partition** tab in the dialog box of the
For Each block. When specifying a signal to be partitioned, specify the
**Partition Dimension**, **Partition Width**, and
**Partition Offset** parameters.

**Partition Mask Parameters of the Subsystem**

You can partition the mask parameters of a For Each Subsystem
block. Partitioning is useful for systems that have identical structures in each iteration
but different parameter values. In this case, changing the model to partition extra input
signals for each parameter is cumbersome. Instead, add a mask parameter to a for-each
subsystem. For more information, see Create a Simple Mask. To select the mask parameter for partitioning, use the
**Parameter Partition** tab of the For Each block dialog
box. For more information, see Select Partition Parameters, below.

**Concatenate Output**

Define the dimension along which to concatenate the results by specifying the
**Concatenation Dimension** in the **Output
Concatenation** tab.

The results generated by the block for each subarray are stacked along the
concatenation dimension. By default, dimension 1 (*y*-axis) is
used, meaning that the results are stacked vertically. However, if you specify a
concatenation dimension of 2, the results concatenate along the horizontal
direction (*x*-axis). Thus, if the process generates row
vectors, then the concatenated result is a matrix in the first case and a row
vector in the second case. For an example, see Specifying the Concatenation Dimension in the For Each Block.

**Select Partition Parameters**

When selecting an input signal or subsystem mask parameter for partitioning,
you must specify how to decompose it into elements or subarrays for each
iteration. Set integer values for the **Partition Dimension**,
**Partition Width**, and **Partition
Offset** parameters.

As an illustration, consider an input signal matrix `A` of
the form:

A 3-by-3 matrix A with all nine elements displayed, showing d1 as the vertical dimension and d2 as the horizontal dimension

The labels *d*1 and
*d*2 define dimensions 1 and 2,
respectively. If you retain the default setting of `1` for both
the partition dimension and the partition width and `0` for the
partition offset, then Simulink® slices perpendicular to partition dimension 1 at a width equal to
the partition width, that is one element:

A 3-by-3 matrix A, with all nine elements showing, partitioned into rows

Matrix A decomposes into these three row vectors:

A 3-by-3 matrix A, decomposed into three 3-element row vectors

If you specify `2` as the partition dimension instead,
Simulink slices perpendicular to dimension 2 to form three column
vectors:

A 3-by-3 matrix A, decomposed into three 3-element column vectors

In addition to setting the **Partition Dimension** to
`2`, if you set the **Partition Width** to
`2` and the **Partition Offset** to
`-1`, Simulink uses two overlapping 3-by-2 partitions for processing.

A 3-by-3 matrix A, decomposed into two overlapping 3-by-2 matrices

For an example, see Partitioning an Input Signal with the For Each Block.

By default, all partitions of the input signal or mask parameter are
processed. To process a subset of the partitions, enter the number of partitions
to process as the **Number of iterations**. In the matrix
examples above, if **Partition Offset** is set to
`0` (the default) and **Number of
iterations** is set to `2`, only the first 2 rows
or columns of the input matrix `A` are processed.

**Note**

Only signals are considered one-dimensional in Simulink. Mask parameters
are row or column vectors, according to their orientation. To partition a
row vector, specify the partition dimension as 2, along the columns. To
partition a column vector, specify the partition dimension as 1, along the
rows.

### Code Reuse Support

For certain models, the For Each Subsystem block improves code
reuse in Simulink
Coder™ generated code. Consider a model containing two reusable Atomic
Subsystem blocks with the same scalar algorithm applied to each element
of the signal. If the input signal dimensions of these subsystems are different,
Simulink
Coder generated code includes two distinct functions. You can replace these
two subsystems with two identical For Each Subsystem blocks that are
configured to process each element of their respective inputs using the same
algorithm. In this case, Simulink
Coder generated code consists of a single function parameterized by the
number of input signal elements. This function is invoked twice, once for each
unique instance of the For Each Subsystem block in the model. For
each of these cases, the input signal elements have different values.

### Multicore Execution Support

When you simulate your model in rapid accelerator mode, Simulink uses multicore execution for faster simulation of for-each subsystems.
Simulink automatically profiles each eligible for-each subsystem the first two time
steps it runs in rapid accelerator mode to compare parallel and serial execution times.
Simulink then designates the for-each subsystem for parallel, multicore execution in
subsequent time steps of the simulation run if doing so would speed up execution time. For
nested for-each subsystems, multicore execution applies only to the top-level subsystem.
Multicore execution does not apply to for-each subsystems containing continuous states or
Function Caller blocks.

To suppress multicore execution for a given for-each subsystem, set the
`MultithreadedSim` parameter of the For Each block within
the subsystem to
`'off'`.

```
set_param(ForEachBlockName,'MultithreadedSim','off')
```

Note that this is a parameter of the For Each block within the
subsystem, not the For Each Subsystem block itself. To suppress multicore
execution for all for-each subsystems in a model, set the
`MultithreadedSim` parameter of the model to
`'off'`.

```
set_param(ModelName,'MultithreadedSim','off')
```

To re-enable multicore execution, set the relevant
`MultithreadedSim` parameter to its default value of
`'auto'`.

For an example, see Multithreaded Simulation Using For Each Subsystem.

**Note**

If you simulate your model in rapid accelerator mode or generate code from your model,
and you partition mask parameters in a for-each subsystem, then any expression inside the
for-each subsystem that references a partitioned parameter must be a tunable expression.
See Tunable Expression Limitations (Simulink Coder).

### S-Function Support

The For Each Subsystem block supports both C-MEX S-functions and
Level-2 MATLAB® S-functions, provided that the S-function supports multiple execution
instances using one of these techniques:

- A C-MEX S-function must declare
  `ssSupportsMultipleExecInstances(S, true)` in the
  `mdlSetWorkWidths` method.
- A Level-2 MATLAB S-function must declare
  `block.SupportsMultipleExecInstances = true` in the
  setup method.

If you use these specifications:

- Do not cache run-time data such as DWork and Block I/O using global or
  persistent variables or within the user data of the S-function.
- In a For Each Subsystem block, every S-function execution
  method from `mdlStart` up to
  `mdlTerminate` is called once for each element
  processed by the S-function. Consequently, you must make sure not to free
  the same memory on repeated calls to `mdlTerminate`. For
  example, consider a C-MEX S-function that allocates memory for a run-time
  parameter within `mdlSetWorkWidths`. The memory only needs
  to be freed once in `mdlTerminate`. As a solution, set the
  pointer to be empty after the first call to
  `mdlTerminate`.
