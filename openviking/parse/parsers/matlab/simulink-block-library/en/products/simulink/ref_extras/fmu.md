---
type: simulink-block
title: 'FMU'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulation Integration / Create Large-Scale Model Components / Integrate Components from External Tools / FMU Importing'
documentation_page: 'fmu'
documentation_source_path: 'ref_extras/fmu.html'
language: en
---

# FMU

## Ports

### Output

### **Port\_1** — Placeholder port none | | string size limited to 255

Placeholder port that produces no output as is. Input and output ports
are configured when an actual FMU is imported into the block. Both input
and output ports support numerical and string data types.

## Parameters

### **FMU name** — FMU name character vector

Specify the name of an FMU, with or without the file extension. This entry
is case sensitive. The FMU must exist on the MATLAB® path.

To specify an FMU name, enter the name in the **FMU
name** text box.

When you click **OK**, the block creates an
`/slprj/_fmu/unique_ID` folder
with the unpacked files and the file hierarchy intact.

#### Dependencies

When you specify an FMU name, the block dialog box updates to contain
four tabs:

- **Parameters**
- **Simulation**
- **Input**
- **Output**

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUName` |
| **Type:** character vector |
| **Values:** name of an FMU, with or without file extension |
| **Default:** `' '` |

### Parameters

This tab lists parameters defined in the FMU.

- To display only the parameters you are interested in, type a search string
  in the filter field. This string can match the parameter name or text in the
  description.
- In the parameter table, you can change the value of the parameter in the
  **Value** field.
- The imported parameters names have a 55 character limit.

You can change the hierarchy of structured model parameters by setting the
`FMUParamMapping` block parameter using the `set_param` function. This block
parameter can be set to `Inherit`, `Flat` or
`Structured`. It is set to `Inherit` by
default. Setting it to `Flat` separates the structured model
parameters into individual parameters with corresponding parameter name and value.
Setting it to `Structured` combines the model parameters into a
structure of parameter values.

### Input

This tab lists input variables specified in the FMU
`modelDescription.xml`.

Specify the variable for a structured input port.

To filter the variable by name, type the variable name in the text box.

The variables table lists the variables and their values for nodes at the top of
the hierarchy and their children, many of which you can edit on this tab.

- Name — Variable name. This is not editable.
- Visibility — Select this check box to enable an input port on the block
  for the variable. Clear this check box to remove a port.

  Selecting this check box at a top-level node makes the child nodes visible
  as one port for the block.

  **Note**

  When you click **Apply**, the number of block ports
  change. Remember to add or remove connections accordingly.
- Start — Add a start value defined in
  `modelDescription.xml`. You cannot:

  - Change the start value when the corresponding input port is
    visible.
  - Add start values to nonleaf nodes. (You can edit start values only
    for leaf nodes.)
- Bus object name — Set the bus object variable that corresponds to the
  port. By default, the variable uses the structured variable name defined in
  `modelDescription.xml`. To create a new variable in the
  workspace, use `fmudialog.createBusType`.

Changing any variable values enables the **Restore output to default
settings** button, which you can click to restore original settings.

You can change the layout of the input ports of the FMU block by setting the
`FMUInputMapping` parameter using the `set_param` function. The parameter
can be set to `Inherit`, `Flat` or
`Structured`. It is set to `Inherit` by
default. Setting the parameter to `Flat` separates the bus input
port into individual bus element signal input ports. Setting the parameter to
`Structured` combines the individual bus element input ports
into a bus input port.

### Output

This tab lists output variables and internal variables specified in the FMU
`modelDescription.xml`.

Specify the variable for a structured output port.

To filter the variable by name, type the variable name in the text box.

The variables table lists the variables and their values for nodes at the top of
the hierarchy and their children, many of which you can edit on this tab.

- Name — Variable name. This is not editable.
- Visibility — Select this check box to enable an output port on the block
  for the variable. Clear this check box to remove a port. If internal
  variables exist in this FMU, you can enable or disable visibility for
  individual internal variables. If an internal variable is selected, it
  creates an additional output port.

  Selecting this check box at a top-level node makes the child nodes visible
  as one port for the block.

  **Note**

  When you click **Apply**, the number of block ports
  change. Remember to add or remove connections accordingly.
- Start — Add a start value defined in
  `modelDescription.xml`. You cannot change or add a
  start value for an output variable.
- Bus object name — Set the bus object variable that corresponds to the
  port. By default, the variable uses the structured variable name defined in
  `modelDescription.xml`. To create a new variable in the
  workspace, use `fmudialog.createBusType`.

Changing any variable values enables the **Restore output to default
settings** button, which you can click to restore original settings.

You can change the layout of the output ports of the FMU block by setting the
`FMUOutputMapping` parameter using the `set_param` function. The parameter
can be set to `Inherit`, `Flat` or
`Structured`. It is set to `Inherit` by
default. Setting the parameter to `Flat` separates the bus output
port into individual bus element signal output ports. Setting the parameter to
`Structured` combines the individual bus element output ports
into a bus output port.

### Simulation

### **Enable FMU tolerance** — Enable FMU tolerance off (default) | on

Select this check box to enable the specification of a tolerance value
to the FMU.​ Otherwise, clear this check box.

#### Dependencies

This parameter is applicable only if your FMU version or mode
supports tolerance values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUIsToleranceUsed` |
| **Type:** character vector |
| **Values:** on | off |
| **Default:** `'off'` |

### **Relative tolerance** — FMU relative tolerance 1E-3 (default) | scalar

FMU relative tolerance value (%), specified as a scalar.​

#### Dependencies

This parameter is applicable only if your FMU version or mode
supports tolerance values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUToleranceValue` |
| **Type:** character vector |
| **Values:** `1E-3` | scalar |
| **Default:** `'1E-3'` |

### **Simulate FMU using** — Select binary for simulation x86\_64-windows (default) | x86-windows | x86\_64-linux

Select the binary for simulation of the FMU. Set this option as
`linux64` for an FMU on Windows® when FMU contains Linux® binary .

#### Dependencies

This simulation of FMU using Linux binary on Windows requires the installation of the following products:

- Simulink
  Compiler™
- FMU Builder for Simulink support package
- Windows Subsystem for Linux (WSL) Version 2.0.9.0 or
  newer

For more information, see Simulate FMU with Linux Binary on Windows (Simulink Compiler).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUSelectedBinary` |
| **Type:** character vector |
| **Values:** `x86_64-windows` | `x86-windows` | `linux64` |
| **Default:** `'win64'` |

### **Enable event mode** — FMU in event mode on (default) | off

Simulate the FMU in event mode.​

#### Dependencies

This parameter is enabled only if the FMU supports event mode and
applicable only if your FMU is used in co-simulation mode and is
compatible with FMI 3.0 standards.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CSEventModeEnabled` |
| **Type:** character vector |
| **Values:** on | off |
| **Default:** `'on'` |

### **Communication Step Size** — Step size between co-simulation time instants -1 (default) | scalar positive

Communication step size during simulation, specified as a scalar.​
Specify the time interval between simulation time instants for the
block. For more information, see Timing Considerations.

In most cases, to prevent unexpected behavior, set this value to a
positive value. To inherit the sample time from the driving block or the
model solver, set this parameter to `-1`. For more
information, see Specify Sample Time.

The block supports different types of sample time,​ including
continuous,​ discrete,​ and Inherited. However,​ common co-simulation
FMUs support only periodic discrete sample times without offset (such as
positive scalar).

#### Dependencies

This parameter is applicable only in Co-Simulation mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUSampleTime` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'-1'` |

### **Enable FMU debug logging** — Enable FMU logging display for debug purposes off (default) | on

To enable the display of FMU debug logging, select this check box.
Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUDebugLogging` |
| **Type:** 1xN cell array of character vectors |
| **Values:** on | off |
| **Default:** `'off'` |

### **Filter logs by return status** — Filter debug logs **OK** | **Warning** | **Discard** | **Error** | **Fatal** | **Pending**

Filter debug logs by type, specified by selecting these check
boxes:

- **OK**
- **Warning**
- **Discard**
- **Error**
- **Fatal**
- **Pending**

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUDebugLoggingFilter` |
| **Type:** character vector |
| **Values:** `OK` | `Warning` | `Discard` | `Error` | `Fatal` | `Pending` |
| **Default:** `'OK'` | `'Warning'` | `'Discard'` | `'Error'` | `'Fatal'` | `'Pending'` |

### **Redirect debug logs to** — Direct streaming debug logs `File` (default) | `Display`

Direct debug logs, specified as:

- `File` — Stream to
  `slprj/_fmu/_logs_modelname/modelname_FMUblockname.txt​`.
- `Display` — Stream to the MATLAB Command Window.

#### Dependencies

Setting this parameter to `File` enables
the **Open FMU Log File...** link.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUDebugLoggingRedirect` |
| **Type:** character vector |
| **Values:** `File`| `Display` |
| **Default:** `'File'` |

### Code Generation

### **Call FMU functions using** — Specify source of FMI API for the generated code auto | source code | shared library

Specify source of FMI APIs for the generated code of FMU blocks. State
whether generated code uses FMU functions inlined from source code or
references FMI APIs from compiled binary using function pointers. Source
code based code generation is the default option for nested FMUs, ERT
target, GRT target, and rapid accelerator simulation mode. For an
example, see Integrate FMI APIs in Generated Code Using FMU Source Code or Binary.

#### Tips

Set this option as `source code` to enable the
generated code to be compiled across multiple platforms.

#### Dependencies

This option is only active when the FMU package contains the
source code generated from Simulink . When your FMU only contains
the binary or source code from external tools, the option is
inactive and code generation uses the compiled binary.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FMUCGType` |
| **Type:** character vector |
| **Values:** `source code` | `shared library` | `auto` |

## Libraries

Simulink Extras / FMU Import

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `logicala` | `busa` | `doublea` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `yesa` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `yesa` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

### R2025a: Import and simulate FMUs with windows 32-bit DLLs

Import and simulate FMUs containing windows 32-bit DLLs in Simulink. To do so, in
the **Simulation** tab of the FMU block dialog, set the
**Simulate FMU using:** parameter as
`x86-windows`.

### R2025a: Generate code for FMU from its source code

Generate code for FMU generated from Simulink using its packaged source code.
Source-code based code generation is the default setting for nested FMUs, ERT
target, GRT target, and rapid accelerator simulation mode. Before this, the
generated code for an FMU had a dependency on its platform-specific compiled binary
file.

### R2025a: Enhancements for deploying and simulating FMU with constant periodic clocks

Standalone co-simulation FMU blocks with constant periodic clocks are enhanced for
simulation and performance. You can now:

- Generate code for models containing the FMU.
- Simulate models with the FMU in rapid accelerator mode.
- Include the FMU in model reference and simulate in accelerator
  mode.
- Generate nested FMU.

### R2024b: Time-Based Clock Support

The FMU Import block supports import of standalone co-simulation FMU with
time-based clocks. Simulink registers the time-based FMU clock variables as sample
times of the FMU block, enabling the block to handle the clock event updates and
synchronize with the FMU.

Simulation of FMU with clock is only supported in normal mode simulation. Code
generation is not supported for the block.

### R2023b: FMI 3.0 Support

The FMU Import block supports the following FMI 3.0 features:

- Introduction of new integer and float data types.
- Native support for vectors and matrices.
- Event mode support for co-simulation mode.
- Binary data type support.

### R2023b: Discrete input value changes in model exchange FMU triggers event mode

The FMU Import block detects discrete input value changes for Model Exchange FMU
and triggers event iteration.

### R2023b: Enumeration data type support

The FMU Import block supports Enumerated data type for block input and
output.

## Description

Include Functional Mockup Unit (FMU) in model

The FMU block imports existing functional mockup units (FMUs) into Simulink®. The block automatically selects an FMU mode based on the existing FMU you
want to import:

- `Co-Simulation` — Integrate FMUs that implement a
  Functional Mock-up Interface (FMI) Co-Simulation interface. These FMUs may
  contain local solvers that are used for tool coupling.
- `Model Exchange` — Integrate FMUs that implement an
  FMI Model Exchange interface. These FMUs do not contain local solvers. Instead,
  they inherit solvers from Simulink.

This block supports FMI versions 1.0, 2.0, and 3.0. For FMI version 2.0 and 3.0, if
your FMU contains both Co-Simulation and Model Exchange elements, the block detects them
and prompts you to select the mode you want the block to operate in.

To use this block, you must first have an existing FMU, exported from another tool, or
authored in C language.
