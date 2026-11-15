---
type: simulink-block
title: 'While Iterator Subsystem'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'whileiteratorsubsystem'
language: en
---

# While Iterator Subsystem

## Ports

### Input

### **In1** — Signal input to a subsystem block scalar | vector | matrix

Placing an Inport block in a subsystem block adds an
external input port to the block. The port label matches the name of the
Inport block.

Use Inport blocks to get signals from the local
environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **IC (initial logical condition)** — Control initial execution of a subsystem block scalar

Placing a While Iterator block connected to an
Input block in a Subsystem block adds
this external input port to the block.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Out** — Signal output from a subsystem scalar | vector | matrix

Placing an Outport block in a subsystem block adds an
output port from the block. The port label on the subsystem block is the
name of the Outport block.

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

### **Show subsystem reinitialize ports** — Option to display reinitialize event ports `off` (default) | `on`

Select this parameter to display the reinitialize event ports. Clear this parameter to remove the ports.

#### Dependencies

To enable this parameter, select **Treat as atomic unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowSubsystemReinitializePorts` |
| **Values:** | `'off'` (default) | `'on'` |

### Code Generation

Parameters on the Code Generation tab require a Simulink
Coder™ or Embedded Coder® license.

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

Simulink / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced before R2006a**

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

Repeat subsystem execution during simulation time step while logical expression is true

The While Iterator Subsystem block is a Subsystem block preconfigured as a starting point for creating a subsystem
that repeats execution during a simulation time step while a logical condition is
`true`. Execution is controlled by a While Iterator block inside the
subsystem. For an example, see `ex_while_iterator_block`.

**Note**

To break a loop and terminate the simulation manually before the simulation stop
time of a model, press **Ctrl + C**.

Use While Iterator Subsystem blocks to model:

- Block diagram equivalent of a program `while` or
  `do-while` loop.
- An iterative algorithm that converges on a more accurate solution after
  multiple iterations.

When using simplified initialization mode, if you place a block that needs elapsed
time (such as a Discrete-Time Integrator block) in a While
Iterator Subsystem block, Simulink® displays an error.

If the output signal from a While Iterator Subsystem block is a
function-call signal, Simulink displays an error when you simulate the model or update the
diagram.
