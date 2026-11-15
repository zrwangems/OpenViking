---
type: simulink-block
title: 'C Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'cfunction'
---

# C Function

Integrate and call external C/C++ code from a Simulink model

## Libraries

Simulink / User-Defined Functions

## Description

The C Function block integrates and calls external C/C++ code from a
Simulink® model. Use this block to define external code and customize the integration of
your code by preprocessing or postprocessing the data. In addition, you can specify customized
code for simulation and C code generation. You can conditionally call functions defined in
your code, and you can also call multiple functions in one block. Using this block, you can
initialize persistent data and pass it to an external function.

The C Function block supports initializing persistent data and calling
external functions from the block dialog box. Persistent data can include an object of a C++
class defined in your custom code. See Interface with C++ Classes Using C Function Block. The block supports only
initializing and terminating persistent data. The block does not support updating the data
during simulation. To model a dynamic system with continuous states, use an
S-Function block. To learn more about S-functions, see What Is an S-Function?

**Note**

C99 is the standard version of C language supported for custom C code integration into
Simulink.

### Specify Custom Code

*Since R2024a*

Starting in R2024a, the block provides you with a range of options to specify custom C
/C++ code for the block.

- You can specify the custom code locally in the block, so you can integrate a code
  component that is fully contained in a single block. For example, if you want a
  C Function block to behave like a custom filter which is defined
  using external C/C++ code, specify the custom code locally in the block.
- You can share the custom code with other blocks in a model or across multiple
  models. To share the custom code across multiple models you must define the custom
  code in the Configuration Parameters dialog box of a Simulink library model. Then, use
  the code in a block within the library and fetch that block from that library in other
  models.

For more information, see **Configure custom code
settings**.

### Call C Library Functions

You can call these C Math Library functions directly from the C Function
block.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `abs` | `acos` | `asin` | `atan` | `atan2` | `ceil` |
| `cos` | `cosh` | `exp` | `fabs` | `floor` | `fmod` |
| `labs` | `ldexp` | `log` | `log10` | `pow` | `sin` |
| `sinh` | `sqrt` | `tan` | `tanh` |  |  |

When you call these functions, double precision applies unless all the input arguments
are explicitly single precision. When a type mismatch occurs, a cast of the input arguments
to the expected type replaces the original arguments. For example, if you call the
`sin` function with an integer argument, a cast of the input argument to
a floating-point number of type `double` replaces the original
argument.

Starting in R2025a, you can call these string library functions inside the C
function block.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `strlen` | `strncpy` | `strncat` | `strcmp` | `strncmp` | `strstr` |

For more information, see Use Simulink Strings inside C Function Block to Model Scrolling Display.

To call other C library functions, create and call an external wrapper function that
calls the C library function.

**Call the `abs`, `fabs`, and `labs`
Functions**

Interpretation of the `abs`, `fabs`, and
`labs` functions in C Function block goes beyond the
standard C version to include integer and floating-point arguments:

- If `x` is an integer, the standard C function
  `abs` applies to `x`, or
  `abs(x)`.
- If `x` is a double, the standard C function
  `labs` applies to `x`, or
  `labs(x)`.
- If `x` is a single, the standard C function
  `fabs` applies to `x`, or
  `fabs(x)`.

**Code Replacement Library (CRL) Based on Type**

The call to the function should call the correct CRL based on the type of data passed
into the function. If no CRL is specified, the call to the function should call to
type-specific library. The CRL for C99 generates a type-specific function. For
example:

| Type passed in | Code generation call |
| --- | --- |
| `sin(doubleIn)` | `sin(doubleIn)` |
| `sin(floatIn)` | `sinf(floatIn)` |

You can call `printf`,
`memcpy` and `memset` functions in the C
Function block. *(since R2023a)*

### Report Run-time Errors and Warnings in Simulink

*Since R2024a*

In custom C code that you specify in the C Function block , use the
`slError` and `slWarning` functions to report
run-time errors and warnings, respectively. An error terminates the simulation and must be
resolved before simulation continues. A warning indicates a potential issue with the code
but does not terminate the simulation.

Both `slError` and `slWarning` functions support
different data type format specifiers (for example, `%d`  for integer,
`%f`  for float) that are similar to C.

Examples :

- `slError("Error message");`
- `slError("Input %f should be non-negative", x);`
- `slWarning("Warning message");`
- `slWarning("Input %d should be non-zero", y);`

The following code executes at the start of the simulation. It uses the
`slError` function to issue an error message if the data store fails to
initialize at the start of simulation.

C Function block uses slError to report an error message at the start of simulation.

### Specify Row-Major and Column-Major Array Layouts in Custom Code

*Since R2024a*

Use the `slSetRowMajor` and `slSetColumnMajor`
functions to specify row-major and column-major array layouts, respectively. Specify these
functions in the **Simulation Target** pane of the Configuration Parameters
dialog box using **Use Configuration Parameters Custom Code** parameter
from block dialog box.

For a row-major layout, the row elements of a matrix are stored contiguously in memory.
Similarly, for a column-major layout, the column elements of a matrix are stored
contiguously in memory. For more information, see Row-Major and Column-Major Array Layouts (MATLAB Coder).

Function prototypes:

- `void slSetRowMajor(const char* functionName)`
- `void slSetColumnMajor(const char* functionName)`

`functionName` must be a string literal and fully qualified.

For example, consider the following code:

```
namespace NS1 {
	class ACLASS{
		public:
			void foo_row();
	};
	namespace NS2{
		void foo_col(double*, double*);
	}
}
```

For a fully qualified function name.

- If the function is inside a namespace, all the nested namespaces should be included
  in the function name string. Based on the above code, for the column-major function,
  `foo_col`, use
  `slSetColumnMajor("NS1::NS2::foo_col")` in the configuration
  parameters custom code.
- For all class members, the class name along with any nested namespaces should be
  included in the function name string. Based on the above code, for the row-major
  function `foo_row`, use
  `slSetRowMajor("NS1::ACLASS::foo_row")` in the configuration
  parameters custom code.

For a C Function block that uses classes, if the constructor takes
majority, the majority must be specified in the **Start** code.

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

The number of input ports is determined by the number of symbols with
`Input` or `InputOutput` scope
defined in the **Symbols** table in the block parameters dialog box.
Each input port label is the same as the name of the `Input`
or `InputOutput` symbol unless you change it by editing the
**Label** field in the **Symbols** table of the
block dialog box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`
### Output

### **Port\_1** — Output port scalar | vector | matrix

The number of output ports is determined by the number of symbols with
`Output` or `InputOutput` scope
defined in the **Symbols** table in the block parameters dialog box.
Each output port label is the same as the name of the
`Output` or `InputOutput` symbol
unless you change it by editing the **Label** field in the
**Symbols** table of the block dialog box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `enumerated` | `bus` | `fixedpoint`

## Parameters

Parameters common to both **Simulation** and **Code
Generation** tabs.

### **Configure custom code settings** — Option to specify custom code location button

Use the Configure Custom Code settings button C Function block gear icon. to choose whether to specify the custom code in the
block locally or in the Configuration Parameters dialog box. Click the arrow next to the C Function block gear icon. icon to select an option:

- **Use Block Custom Code**

  Use this option to specify the custom code locally in the C
  Function block. This setting is default. This option enables the
  **Simulation Custom Code** and the **Code Generation
  Custom Code** parameters in the **Simulation** section
  and the **Code generation** section, respectively.

  Starting in R2025a, code coverage is supported for locally specified custom
  code. To use code coverage, you must have Simulink
  Coverage license.
- **Use Configuration Parameters Custom Code**

  Use this option to specify the custom code in the **Simulation
  Target** pane of the model Configuration Parameters dialog box. For more
  information, see Model Configuration Parameters: Simulation Target.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomCodeSettingLocation` |
| **Type:** character vector |
| **Value:**`'BlockSettings'` | `'ModelConfigurationParameters'` |
| **Default:** `'BlockSettings'` |

### **Port and Parameter Symbols** — Symbols and symbol properties table

Symbols and symbol properties used in the C code, specified as a table. You must
enter the following attributes of each symbol in the table:

- **Name** — Symbol name in the code.

  If the symbol represents a C++ class object, the **Name**
  field serves as a call to the class
  constructor:

  ```
  ObjectName(Argument1,Argument2,...)
  ```
- **Scope** — Scope of the symbol. These scopes are available:

  - `Input` — Input to the block.
  - `Output` — Output to the block.
  - `InputOutput` — Both input and output to the
    block.

    Use the `InputOutput` scope to map an input
    passed by a pointer in your C code. Ports created using an
    `InputOutput` scope have the same name for input
    and output ports. `InputOutput` scope enables
    buffer reuse for input and output ports. Buffer reuse may optimize memory
    use and improve code simulation and code generation efficiency, depending on
    the signal size and the block layout. Limitations include:

    - An `InputOutput` symbol cannot be used in
      **Start**, **Initialize
      Conditions**, or **Terminate**.
    - `InputOutput` symbols do not support the
      `void*` data type.
    - `InputOutput` symbols do not support
      `size()`  expressions.
  - `Parameter` — Block parameter that appears on the block
    parameter mask. The parameter name is defined by the
    **Label** of the symbol.
  - `Persistent` — Persistent block data, which retains its
    value from one time step to the next during simulation.

    You can define a void pointer using the `Persistent`
    scope. A *void pointer* is a pointer that can store any
    type of data that you create or allocate.

    You can instantiate an object of a C++ class defined in your custom code
    by defining a symbol with `Persistent` scope and using
    `Class:`
    *`ClassName`* as the **Type** for
    the symbol. See Interface with C++ Classes Using C Function Block.
  - `Constant` — Constant value, defined using value-size
    or numeric expressions.
- **Label** — Label of the symbol. For a symbol
  with `Input`, `InputOutput`, or
  `Output` scope, the label appears as the port name on
  the block. For a symbol with `Parameter` scope, the label
  appears on the block parameter mask. If the scope is
  `Constant`, the label is the constant expression. You
  cannot define a label for `Persistent` scope
  symbols.
- **Type** — Data type of the symbol. Select a data
  type from the drop-down list or specify a custom data type.

  **Note**

  Starting in R2025a, the block supports Simulink strings types for `Input`,
  `Output`, `InputOutput` and
  `Persistent` scopes.

  C++ class types defined in your custom code are supported, as are `Simulink.Bus`, Simulink Enum, and `Simulink.AliasType` types. Enter the
  **Type** as shown in this table.

  | Custom type | Specification in **Type** field |
  | --- | --- |
  | C++ class | `Class:`*`C++ClassName`* |
  | `Simulink.Bus` | `Bus:`*`BusTypeName`* |
  | `Simulink.Enum` | `Enum:`*`EnumTypeName`* |
  | `Simulink.AliasType` | *`AliasTypeName`* |
- **Size** — Size of the symbol data. You can use a
  size expression to define the size of an output or use `-1` to
  inherit size.
- **Port** — Port index of the symbol. For an
  `Input`, `InputOutput`, or
  `Output` symbol, **Port**
  specifies the port index on the block of the port or ports corresponding to the
  symbol. For a `Parameter` symbol, **Port** specifies the order that the symbol appears in the block
  parameter mask.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SymbolSpec` |
| **Type:** `SymbolSpec` object |
| **Value:** `SymbolSpec` object |
| **Default:** Empty array of `Symbol` objects |

### **Sample time** — Sample period `-1` (default) | scalar | vector

Sample period, specified in seconds. See Types of Sample Time
and Specify Sample Time. If the block
defines persistent symbols, you cannot specify a continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string scalar or character vector |
| **Default**: `"-1"` |

### **Block specified custom code supports multiple instances** — Option to specify the same custom code locally in multiple C Function blocks `off` (default) | `on`

*Since R2024a*

Select this option if the same custom code can be locally specified in multiple
C Function blocks within a model without the blocks interfering with
each other. For example, if you use a mathematical counter that contains internal
states, multiple instances of the code can interfere with each other.

When you select this option, these modeling scenarios are supported:

- Specify custom code locally in a C Function block and use the
  block within a For Each subsystem.
- Specify custom code locally in a C Function block that uses
  continuous sample time.
- Generate code for multiple instances of the same custom code, where each
  instance of the code is specified locally in a C Function block
  within a model.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomCodeIsMultiInstantiable` |
| **Type**: string scalar or character vector |
| **Default**: `'off'` |

### Simulation

### **Output** — Output code no default

Output code that the block executes at each time step during simulation, specified
as a character vector or string scalar. For example, use this parameter to call a
function from external C code, make modifications to the results, and perform
operations to pass the results to other blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Start** — Initialization code no default

Initialization code that the block executes one time at the start of simulation.
For example, use this parameter to initialize persistent symbols.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StartCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Initialize Conditions** — Reinitialization code no default

Reinitialization code for the block to execute when enabling a subsystem or model
in which the block is placed. The code executes one time at the start of simulation.
If the block is inside a subsystem or a model that contains an Enable block with the **States when enabling** parameter
set to `reset`, the code also executes each time the
subsystem or model switches from disabled to enabled. See Using Enabled Subsystems. You can use this code, for example, to set an initial output value or reset the
value of a persistent variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitializeConditionsCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Terminate** — Termination code no default

Termination code that the block executes one time at the end of simulation. For
example, use this code to free the memory cached on persistent symbols specified as
void pointers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TerminateCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Headers** — Locally specify header files for custom code no default

Locally specify header files for custom code. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomHeaderFile` |
| **Type:** character vector or string scalar |
| **Value:** header file names or #include statements |
| **Default:** `""` |

### **Sources** — Locally specify source files for the custom code no default

Locally specify source files for the custom code. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomSourceFile` |
| **Type:** character vector or string scalar |
| **Value:** any file name |
| **Default:** `""` |

### **Libraries** — Locally specify a list of static or shared libraries no default

Locally specify a list of static or shared libraries. This parameter is in the
**Simulation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomLibraries` |
| **Type:** character vector or string scalar |
| **Value:** any library file name |
| **Default:** `""` |

### **Search Directories** — Locally specify directories containing header and source files for custom code no default

Locally specify directories containing header and source files for custom code.
This parameter is available in the **Simulation Custom Code**
section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SimCustomSearchDirectory` |
| **Type:** character vector or string scalar |
| **Value:** any folder path |
| **Default:** `""` |

### **Defines** — Locally specify preprocessor macro definition to be added to the compiler command line no default

Locally specify preprocessor macro definition to be added to the compiler command
line. This parameter is available in the **Simulation Custom Code**
section, in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomDefines` |
| **Type:** character vector |
| **Value:** preprocessor macro definition |
| **Default:** `''` |

### **Compiler Flags** — Locally specify additional flags to be added to the compiler command line no default

Locally specify additional flags to be added to the compiler command line. This
parameter is available in the **Simulation Custom Code** section,
in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomCompilerFlags` |
| **Type:** character vector |
| **Value:** compiler flags |
| **Default:** `''` |

### **Linker Flags** — Locally specify additional flags to be added to the linker command line no default

Locally specify additional flags to be added to the linker command line. This
parameter is available in the **Simulation Custom Code** section,
in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimCustomLinkerFlags` |
| **Type:** character vector |
| **Value:** linker flags |
| **Default:** `''` |

### Code generation

Parameters on the **Code generation** tab require a Simulink
Coder™ or Embedded Coder® license.

### **Use same code as simulation** — Option to use same or different codes for simulation and code generation `on` (default) | `off`

Specify whether to use same or different codes for simulation and code generation.
By default, this option is selected and the block uses the same code for simulation
and code generation. Clear this option to use different code for simulation and code
generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CodegenUsesSimCustomCode` |
| **Type**: string scalar or character vector |
| **Default**: `'on'` |

### **Generate code as - is (optimizations off)** — Option to allow parsing for code generation code `on` (default) | `off`

Specify whether to allow parsing for code generation code. By default, this option
is selected and the block embeds your code in the generated code without parsing.
Clearing this option enables the block to analyze the code and report any
errors.

When you use different code for simulation and code generation, this parameter
uses its default settings.

#### Dependencies

This option is only available for selection when the **Use same code as
simulation** parameter is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GenerateCodeAsIs` |
| **Type**: string scalar or character vector |
| **Default**: `'on'` |

### **Output** — Output code no value

Output code that the block executes at each time step during code generation. For
example, use this parameter to call a function from external C/C++ code, make
modifications to the results, and perform operations to pass the results to other
blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenOutputCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Start** — Initialization code no default

Initialization code that the block executes one time at the start of code
generation. For example, use this parameter to initialize persistent symbols.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenStartCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Initialize Conditions** — Reinitialization code no default

Reinitialization code for the block to execute when enabling a subsystem or model
in which the block is placed. The code executes one time at the start of code
generation. If the block is inside a subsystem or in a model that contains an Enable block with the **States when enabling** parameter
set to `reset`, the code also executes each time the
subsystem or model switches from disabled to enabled. See Using Enabled Subsystems. You can use this code, for example, to set an initial output value or reset the
value of a persistent variable.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenInitializeConditionsCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Terminate** — Termination code no default

Termination code that the block executes one time at the end of code generation,
specified as a character vector or string scalar. For example, use this code to free
the memory cached on persistent symbols specified as void pointers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CodegenTerminateCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `C/C++ code` |
| **Default:** `""` |

### **Headers** — Locally specify header files for custom code no default

Locally specify header files for custom code. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomHeaderFile` |
| **Type:** character vector or string scalar |
| **Value:** header file names or #include statements |
| **Default:** `""` |

### **Sources** — Locally specify source files for the custom code no default

Locally specify source files for the custom code. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomSourceFile` |
| **Type:** character vector or string scalar |
| **Value:** any file name |
| **Default:** `""` |

### **Libraries** — Locally specify a list of static or shared libraries no default

Locally specify a list of static or shared libraries. This parameter is in the
**Code Generation Custom Code** section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CustomLibraries` |
| **Type:** character vector or string scalar |
| **Value:** any library file name |
| **Default:** `""` |

### **Search Directories** — Locally specify Directories that contain header and source files for custom code no default

Locally specify Directories that contain header and source files for custom code.
This parameter is in the **Code Generation Custom Code**
section.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CustomSearchDirectory` |
| **Type:** character vector or string scalar |
| **Value:** any folder path |
| **Default:** `""` |

### **Defines** — Locally specify preprocessor macro definition to be added the compiler command line no default

Locally specify preprocessor macro definition to be added the compiler command
line. This parameter is in the **Code Generation Custom Code**
section, in the **Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomDefines` |
| **Type:** character vector |
| **Value:** preprocessor macro definition |
| **Default:** `''` |

### **Compiler Flags** — Add Additional flags to compiler command line no default

Add additional flags to compiler command line. This parameter is in the
**Code Generation Custom Code** section, in the
**Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomCompilerFlags` |
| **Type:** character vector |
| **Value:** compiler flags |
| **Default:** `''` |

### **Linker Flags** — Add additional flags to linker command line no default

Add additional flags to linker command line. This parameter is in the
**Code Generation Custom Code** section, in the
**Advanced** tab.

#### Dependencies

To enable this parameter, set the **Configure Custom
Code settings** parameter to `Use Block Custom
Code`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomLinkerFlags` |
| **Type:** character vector |
| **Value:** linker flags |
| **Default:** `''` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2020a**

### R2025a: Enhancements related to function interface and custom code coverage

- The C Function block now supports Simulink strings types for `Input`, `Output`,
  `InputOutput` and `Persistent` scopes.
- You can now call a subset of string library functions. For more information about
  supported string library functions, see Call C Library Functions.
- Code coverage is now supported for locally specified custom code. To locally
  specify custom code in the block dialog box, use the **Use Block Custom
  Code** parameter. For more information, see **Configure custom
  code settings**.

### R2024a: Changes to C Function block dialog box and parameter names

These changes are made to block dialog box and parameters:

- The block dialog box has two new tabs, **Simulation** and
  **Code generation**.
- The **Output code**, **Start code**,
  **Initialize conditions code**, and **Terminate
  code** parameters are now called **Output**,
  **Start**, **Initialize code**, and
  **Terminate**, respectively.
- The Configure custom code settings C Function block gear icon. button lists two drop-down options, **Use Block
  Custom Code** and **Use Configuration Parameters Custom
  Code**. Use these options to specify whether to specify the custom code
  locally in the block parameters dialog box or use the configuration parameters dialog
  box to integrate your custom code into Simulink.
- The **Symbols** table is now the **Ports and
  Parameters** table.
- The **Size** column in the **Symbols** table is
  now the **Dimensions** column in the **Ports and
  Parameters** table.

### R2024a: Enhancements related to custom code specification

- You can now specify target-specific code for code generation that is different from
  the code you use for simulation. To do so, use the parameters in the
  **Simulation** and **Code generation**
  sections.
- You can use the parameters in the **Simulation Custom Code** and
  **Code Generation Custom Code** sections to specify your custom code
  for simulation and code generation, respectively. Use these parameters to specify custom
  code locally and only specify the code that is required for a particular C
  Function block.
- You can embed your custom code in the generated code without parsing (see **Generate code as -
  is (optimizations off)**). This enhancement extends the capability of the
  C Function block by allowing you to use custom C code that is not
  compatible with desktop MEX compilers.
- Use `slError` and `slWarning` messages in your
  custom code to report error and warning messages, respectively.
- Use `slSetRowMajor` and `slSetColumnMajor`
  functions in your custom code to specify row-major and column-major array layouts,
  respectively.

### R2023a: Support for `printf`, `memcpy` and `memset` C library functions

You can use `printf`, `memcpy` and
`memset` functions in the **Start**,
**Initialize Conditions**, and **Terminate** codes of
the C Function block.
