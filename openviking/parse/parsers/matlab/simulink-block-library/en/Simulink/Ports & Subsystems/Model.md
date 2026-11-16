---
type: simulink-block
title: 'Model'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'model'
documentation_source_path: '../simulink/slref/model.html'
language: en
---

# Model

## Ports

### Input

### **Port\_1** — Input that corresponds to root-level blocks of referenced model scalar | vector | matrix | array | bus

The Model block has an input port for each input port
of the model it references. The input ports of referenced models are
defined by Inport and In Bus Element
blocks. The name of the Model block port matches the name
of the corresponding port in the referenced model. The input signal,
message, or function call for each Model block port must
be valid for the corresponding port in the referenced model. For more
information, see Define Model Reference Interfaces.

#### Tips

- Signal attributes in a referenced model are independent
  from the context of the Model block. For
  example, signal dimensions and data types do not propagate
  across the Model block boundary. To define
  signal attributes in a referenced model, define block
  parameters for root-level Inport and
  In Bus Element blocks.
- Function calls connected to an input port pass into the
  referenced model. To conditionally execute the referenced
  model based on a function call, see **Function Call**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output that corresponds to root-level blocks of referenced model scalar | vector | matrix | array | bus

The Model block has an output port for each output port
of the model it references. The output ports of referenced models are
defined by Outport and Out Bus Element
blocks. The name of the port on the Model block matches
the name of the corresponding port in the referenced model. The output
signals and messages of a Model block are the signals and
messages connected to the Outport and Out Bus
Element blocks in the referenced model. See Define Model Reference Interfaces.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes
### Control

#### Conditional Execution

### **Enable** — Control signal that enables referenced model scalar | vector | matrix

The enable port appears at the top of the Model block.
The port label is an icon that represents an enable signal.

Enable port on Model block

The control signal that connects to the port determines when to
execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add an Enable block to the
top level of the referenced model.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — Control signal that triggers referenced model scalar | vector | matrix

The trigger port appears at the top of the Model block.
The port label is an icon that represents a trigger signal.

Trigger port on Model block

The control signal that connects to the port determines when to
execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add a Trigger block to the
top level of the referenced model and set its **Trigger
type** to `rising`,
`falling`, or
`either`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Function Call** — Control signal for function-call event scalar

The function-call port appears at the top of the Model
block. The port label displays the name of the referenced model as a
function.

Function-call port on Model block

The function-call control signal that connects to the port determines
when to execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add a Trigger block to the
top level of the referenced model and set its **Trigger
type** to
`function-call`.

#### Model Events Simulation

### **initialize** — Control signal for model initialize event scalar

The initialize event port provides a function-call control signal that
triggers a model initialize event, which initializes the states of the
referenced model.

The referenced model can contain an Initialize Function
block that corresponds to the model initialize event. For more
information, see Using Initialize, Reinitialize, Reset, and Terminate Functions.

#### Dependencies

To enable this port, select **Show model initialize
port**.

### **reset** — Control signal for model reset event scalar

A reset event port provides a function-call control signal that
triggers a model reset event, which resets the states of the referenced
model.

The referenced model must contain a Reset Function block
that corresponds to each model reset event. For more information, see
Using Initialize, Reinitialize, Reset, and Terminate Functions.

To specify the port name, use the **Event name**
parameter of the Event Listener block in the Reset
Function block.

#### Dependencies

To enable this type of port, select **Show model reset ports**.

### **reinit** — Control signal for model reinitialize event scalar

A reinitialize event port provides a function-call control signal that
triggers a model reinitialize event, which reinitializes the states of
the referenced model.

The referenced model must contain a Reinitialize Function block that corresponds to each model
reinitialize event. For more information, see Using Initialize, Reinitialize, Reset, and Terminate Functions.

To specify the port name, use the **Event name**
parameter of the Event Listener block in the
Reinitialize Function block.

#### Dependencies

To enable this type of port, select **Show model reinitialize ports**.

### **terminate** — Control signal for model terminate event scalar

The terminate event port provides a function-call control signal that
triggers a model terminate event, which reads and saves the states of
the referenced model.

The referenced model can contain a Terminate Function block
that corresponds to the model terminate event. For more information, see
Using Initialize, Reinitialize, Reset, and Terminate Functions.

#### Dependencies

To enable this port, select **Show model terminate
port**.

### **D** — Control signal for scheduling periodic events scalar

Periodic event ports provide function-call control signals that
specify when to execute the model. For an example, see Test Rate-Based Model Simulation Using Function-Call Generators.

Each port label displays information about the periodic event, such as
the sample time of the corresponding Inport block. For
example, the Model block in this image displays periodic
event ports and references a model with two discrete rates: 0.01 and
0.1.

A Model block has ports labeled D1[0.01] and D2[0.1].

#### Dependencies

To enable this type of port, set **Schedule rates with** to
`Ports`.

## Parameters

To interactively modify Model block parameters, select the
Model block. Then, in the Simulink Toolstrip, on the **Model Block** tab, click
**Block Parameters**.

### Main

Specify fundamental information for the Model block.

### **Model name** — File name of referenced model no default

Specify the filename of the referenced model. The filename must be a
valid MATLAB® identifier for a model, as defined in Choose Valid Model File Names. The file extension is
optional.

To select the model that you want to reference, click
**Browse**. To view the specified model, click
**Open Model**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ModelNameDialog` |
| **Values:** | `''` (default) | filename in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,ModelNameDialog="mymodel.slx")`

To get the block parameter value
programmatically, use the `get_param` function.

You can query the name of the referenced model in different formats:

- `ModelFile` — Model name with file
  extension. When you do not specify a file extension, the
  first match that the software finds on the MATLAB path determines the file extension.
- `ModelNameDialog` — Model name with
  or without file extension, depending on whether you
  specify a file extension.
- `ModelName` — Model name without file
  extension. If you specify a model name with a file
  extension for `ModelName`, the software
  retains the file extension by setting
  `ModelNameDialog` and
  `ModelFile`.

### **Simulation mode** — Simulation mode for model reference `Normal` (default) | `Accelerator` | `Software-in-the-loop (SIL)` | `Processor-in-the-loop (PIL)`

Specify the simulation mode for the Model block. The
simulation mode for the Model block can be different than
the simulation mode of its referenced model and of other models in the
model hierarchy.

- `Normal` — Execute the referenced
  model interpretively, as if the referenced model is an atomic
  subsystem implemented directly within the parent model.
- `Accelerator` — Create a MEX file for
  the referenced model. Then, execute the referenced model by
  running the S-function.
- `Software-in-the-loop (SIL)` — This
  option requires an Embedded Coder® license. Generate production code based on the
  **Code interface** parameter setting. The code is
  compiled for and executed on the host platform.
- `Processor-in-the-loop (PIL)` — This
  option requires an Embedded Coder license. Generate production code based on the
  **Code Interface** parameter setting. This
  code is compiled for and executed on the target platform. A
  target connectivity API implementation supports the exchange of
  data between the host and target at each time step during the
  PIL simulation.

The corners of the Model block indicate the simulation
mode of the Model block. For normal mode, the corners
have empty triangles. For accelerator mode, the corner triangles are
filled in. For SIL and PIL modes, the corners are filled in and the word
`(SIL)` or `(PIL)` appears on the
block icon.

Although you can specify any simulation mode for a model, when you
reference that model, the Model block specifies the
simulation mode of the referenced model instance. The simulation mode of
a parent model can override the simulation mode of a
Model block.

For more information, see Choose Simulation Modes for Model Hierarchies.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SimulationMode` |
| **Values:** | `"Normal"` (default) | `"Accelerator"` | `"Software-in-the-loop (SIL)"` | `"Processor-in-the-loop (PIL)"` |

**Example:** `set_param(gcb,SimulationMode="Accelerator")`

### **Code interface** — Option to generate code from top model or referenced model `Model reference` (default) | `Top model`

Specify whether to generate the code from the top model or the
referenced model for SIL and PIL simulation modes. To deploy the
generated code as part of a larger application that uses the referenced
model, specify `Model reference`. To deploy the
generated code as a standalone application, specify `Top
model`.

- `Model reference` — The code is
  generated from the referenced model as part of a model
  hierarchy. Code generation uses a command similar to this
  command, which generates code for a model named
  `ModelName`.

  ```
  slbuild("ModelName","ModelReferenceCoderTarget")
  ```
- `Top model` — The code is generated
  from the top model with the standalone code interface. Code
  generation uses a command similar to this command, which
  generates code for a model named
  `ModelName`.

  ```
  slbuild("ModelName")
  ```

#### Dependencies

To enable this parameter, set **Simulation mode** to either
`Software-in-the-loop (SIL)` or
`Processor-in-the-loop (PIL)`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CodeInterface` |
| **Values:** | `"Model reference"` (default) | `"Top model"` |

**Example:** `set_param(gcb,CodeInterface="Top
model")`

### Model Events Simulation

Control when the referenced model executes and changes states.

### **Show model initialize port** — Option to display initialize event port `off` (default) | `on`

Select this parameter to display the initialize event port. Clear this
parameter to remove the port.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelInitializePort` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelInitializePort="on")`

### **Show model reinitialize ports** — Option to display reinitialize event ports `off` (default) | `on`

Select this parameter to display the reinitialize event ports. Clear
this parameter to remove the ports.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution and contains a Reinitialize Function block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelReinitializePorts` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelReinitializePorts="on")`

### **Show model reset ports** — Option to display reset event ports `off` (default) | `on`

Select this parameter to display the reset event ports. Clear this
parameter to remove the ports.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution and contains a Reset Function
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelResetPorts` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelResetPorts="on")`

### **Show model terminate port** — Option to display terminate event port `off` (default) | `on`

Select this parameter to display the terminate event port. Clear this
parameter to remove the port.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution. Then, select **Show model initialize port**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelTerminatePort` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelTerminatePort="on")`

### **Schedule rates** — Option to schedule periodic events `off` (default) | `on`

Control the execution of the referenced model with periodic
events.

Depending on the value of the **Schedule rates with** parameter, selecting this parameter
will either display the periodic event ports on the Model
block or create partitions to use with the Schedule Editor. When the **Schedule rates
with** parameter is not visible, its default value
(`Ports`) applies.

Clearing this parameter hides the periodic event ports and does not
create partitions.

#### Dependencies

To enable this parameter, reference a model with discrete sample
times that is not configured for conditional execution and is not an
export-function model. When the parent model is rate based and the
referenced model is an export-function model, **Schedule
rates** is automatically selected.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ScheduleRates` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ScheduleRates="on")`

### **Schedule rates with** — Option to create partitions or periodic event ports `Ports` (default) | `Schedule Editor`

Create ports or partitions.

- `Ports` — Display periodic event
  ports for discrete rates in the referenced model.

  To manually specify port rates, use the `set_param`
  function to set the `AutoFillPortDiscreteRates`
  parameter of the Model block to
  `"off"`. Then, specify the port rates with
  the `PortDiscreteRates` parameter.
- `Schedule Editor` — Create partitions
  for the referenced model to use with the Schedule Editor.

#### Dependencies

To enable this parameter:

- The parent model must not be an export-function
  model.
- The parent model must not use a fixed-step solver and
  single-tasking mode.
- Select **Schedule rates**. When the parent model
  is rate based and the referenced model is an
  export-function model, **Schedule
  rates** is automatically selected.
- Clear **Show model initialize port**, **Show model reset ports**, and **Show model reinitialize ports**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ScheduleRatesWith` |
| **Values:** | `"Ports"` (default) | `"Schedule Editor"` |

**Example:** `set_param(gcb,ScheduleRatesWith="Schedule
Editor")`

### Instance Parameters

Specify instance-specific values for model arguments.

### **Instance parameters** — Display instance parameters and specify values for referenced model number | workspace variable | mathematical expression | structure or structure field

Display instance parameters and specify instance-specific values.
*Instance parameters* are block parameters that
have been configured in the referenced model to use a different value
for each instance of the model.

To specify instance-specific values, use the
**Value** column in the table. To specify that a
parameter value can be overridden by the parent model, select the
**Argument** check
box. For more
information about configuring instance parameters in a referenced model
and specifying instance-specific values at the Model
block, see Configure Instance-Specific Values for Block Parameters in a Referenced Model.

When changing instance-specific values, you can use a partial
structure that has fields that correspond to only the instance
parameters whose values you want to change. Instance parameters not
included in the partial structure retain their values. In the structure,
include the instance parameter names and values, specified as character
vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterArgumentNames` |
| **Values:** | comma-separated parameter names in quotes |

|  |  |
| --- | --- |
| **Parameter:** | `InstanceParameters` |
| **Values:** | structure with fields `Name`, `Value`, `Path`, and `Argument` |
| **Data Types:** | `struct` |

For an example of how to set these programmatic parameters, see
Parameterize a Referenced Model Programmatically.

To get the instance parameter names and values for a
Model block, query
`InstanceParameters` or
`ParameterArgumentValues` with the `get_param` function.
Do not use `ParameterArgumentValues` to set the
instance-specific
values.

#### Dependencies

To enable this parameter, the referenced model must have
MATLAB variables or `Simulink.Parameter`
objects in the model workspace that are configured as model
arguments. To configure a variable or object as a model argument,
select the **Argument** property.

### Solver

Configure a referenced model to use a local solver by using a combination of the
configuration parameters for the referenced model and the block parameters for each
Model block that references the model.

#### Referenced Model Configuration Parameters

### **Use local solver** — Option to use local solver to solve referenced model link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, select or clear the **Use local solver when referencing model** parameter of
the referenced model.

When you select **Use local solver when referencing
model**, the software uses a local solver to solve the
system implemented in the referenced model as a separate system of
differential equations. During simulation, the local solver computes the
values of continuous states in the referenced model and the output
values for the blocks inside the referenced model.

Using a local solver can facilitate system composition and
integration. When you use local solvers, you can solve referenced models
in system-level simulations using the same solver and step size used to
design and test each model in isolation. Using local solvers can also
reduce the number of configuration adjustments you need to make to
configuration parameters in referenced models while integrating the
model into a larger system.

For some systems, using a local solver can improve simulation
performance by allowing you to:

- Choose a solver that is more appropriate to solve the
  system in the referenced model
- Use different step sizes for different components to
  reduce the number of redundant calculations in systems that
  have a wide range of dynamics among components.

For more information, see Use Local Solvers in Referenced Models.

### **Solver** — Option to select local solver link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, select a value for the **Solver** parameter
of the referenced model. When you use a local solver, the
**Solver** parameter of the referenced model
specifies the solver to use as the local solver.

In some systems, using a different local solver can improve simulation
performance. For example, when the system is not stiff but the component
implemented by the referenced model is stiff, using a stiff local solver
can improve performance when simulating the system.

The top solver can be a variable-step or fixed-step solver. The local
solver can be a variable-step *(since R2025a)* or
fixed-step solver.

For more information, see Use Local Solvers in Referenced Models.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
configuration parameters for the model referenced by this
block.

### **Fixed step** — Option to specify step size for fixed-step local solver link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, specify the value for the
**Fixed-step size (fundamental
sample time)** parameter of the referenced model to
specify the step size for the local solver. The step size you specify
for the local solver is not registered as a discrete rate in either the
referenced model or the parent model.

The local step size can be greater than, less than, or equal to the
parent solver step size. However, the *communication step
size*, which determines when the local and parent solvers
exchange data, constrains possible values for the local step size.

- The local step size must be less than or equal to the
  communication step size.
- When the local step size is smaller than the communication
  step size, the local step size must be an integer divisor of
  the communication step size.

  For example, when the communication step size is 0.1
  seconds, the local solver can be an integer divisor such as
  0.1 seconds, 0.05 seconds, 0.025 seconds, and so on.

*Before R2024a: When the parent solver is a
fixed-step solver, the local solver step size must be an integer
multiple of the parent solver step size.*

For more information, see Use Local Solvers in Referenced Models.

#### Dependencies

To enable this parameter, in the configuration parameters for the
model referenced by this block:

- Select **Use local solver when referencing
  model**.
- Set **Type** to
  `Fixed-step`.

#### Model Block Parameters

### **Communication step size** — Discrete interval of communication between local solver and parent solver positive scalar double

The *communication step size* specifies the rate
at which the local and parent solvers exchange data. The communication
step size is registered as a discrete sample time of the
Model block in the parent model.

By default, the communication step size is inherited
(`-1`) and determined by the software.

- Fixed-step local solver — The inherited communication step
  size is the local step size.
- Variable-step local
  solver *(since R2025a)* — The inherited communication step size
  depends on various criteria.

  - When the referenced model has discrete rates, the
    inherited communication step size is the greatest common
    divisor of these rates.
  - When the referenced model has no discrete rates and
    the local maximum step size is finite, the inherited
    communication step size is the local maximum step size.
  - When the referenced model has no discrete rates and
    both the local maximum step size and the simulation stop
    time are infinite, the inherited communication step size
    is `0.2`.
  - When the referenced model has no discrete rates, the
    local maximum step size is infinite, and the simulation
    stop time is finite, the inherited communication step
    size is 2% of the simulation time.

When you explicitly specify the communication step size, the value you
specify must satisfy all of these constraints:

- The communication step size must be:

  - Greater than or equal to both the local and
    parent minimum step sizes
  - An integer multiple of both the local and
    parent fixed step sizes, when applicable
  - Greater than or equal to the fastest discrete
    rate in the referenced model
- Every discrete rate in the referenced model must be evenly
  divisible by the communication step size.

When the local step size is larger than the parent step size, specify
the communication step size as inherited (`-1`) or
equal to the local step size. For example, if the parent step size is 1
second and the local step size is 2 seconds, specify the communication
step size as `-1` (inherited) or `2`.
Specifying the communication step size as a larger value, such as
`4`, could reduce accuracy without providing any
performance improvement.

For a variable-step local solver *(since R2025a)*:

- When the communication step size is smaller than the local
  maximum step size, the local solver does not step farther
  than the communication step size.
- Within the interval between hit times for the
  communication step size, the local solver determines the
  size of each local step based on the dynamics of the
  continuous states in the referenced model and the tolerance
  values you specify for the local solver.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CommunicationStepSize` |
| **Values:** | `-1` (default) | positive scalar double |
| **Data Types:** | `double` |

**Example:** `set_param(gcb,CommunicationStepSize="0.5")`

### **Input signal handling** — Extrapolation method for local solver inputs `Auto` (default) | `Zero-order hold`

The local solver computes continuous state values and block output
values by extrapolating continuous derivative or input signal values
that come from the parent solver. This parameter specifies the method
the local solver uses to extrapolate continuous derivative or input
signal values to the local simulation time.

- `Auto` — The software determines the
  extrapolation method based on the selected solver, the model
  structure, and how the local step size compares to the parent
  solver step size.

  The local solver extrapolates input signal values to the local
  simulation time using a zero-order hold when:

  - You select an implicit solver, such as
    `ode1be` or
    `ode14x`.
  - The referenced model has no input ports.
  - The local step size is smaller than the parent
    step size.

  Otherwise, the local solver extrapolates continuous
  derivatives to the local simulation time using an extrapolation
  algorithm that is appropriate for the selected solver. The
  extrapolation algorithms generally improve the accuracy of
  simulation results but are more computationally intensive than
  the zero-order hold extrapolation.

  *Before R2024a: The software determines
  how to extrapolate continuous derivative or input signal values
  based only on the selected solver, and the local step size is
  always greater than or equal to the parent solver step
  size.*
- `Zero-Order Hold` — The local solver
  extrapolates input signal values to the local simulation time
  using a zero-order hold. Each input signal value at the local
  simulation time is equal to the value the parent solver
  calculated for the signal at the most recent communication
  step.

  Consider using `Zero-order hold`
  input handling in any of these situations:

  - When simulation results are acceptable with
    `Zero-order hold` input
    handling and performance is a concern
  - When input port values do not affect continuous
    state computations
  - When a significant part of the derivative is based
    on the state itself, for example, from feedback
    loops in the model
  - To improve local solver stability for a given step
    size

The local solver propagates time independently during the local solver
advance phase that occurs when the parent solver executes the update
method for the Model block. Because the update method
executes before the advance method in the parent solver simulation loop:

- The local solver advance occurs before the parent solver
  advance.
- The local solver gets ahead of the parent solver in
  simulation time.

To compute the continuous state values and block output values inside
the referenced model, the local solver extrapolates the values for
continuous derivatives or input signals to the local simulation time.
For more information, see Use Local Solvers in Referenced Models.

When you use a variable-step local
solver *(since R2025a)*, only `Zero-order hold`
input and output signal handling are supported.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
model configuration parameters for the model referenced by this
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InputSignalHandling` |
| **Values:** | `"Auto"` (default) | `"Zero-order hold"` |

**Example:** `set_param(gcb,InputSignalHandling="Zero-order
hold")`

### **Output signal handling** — Interpolation method for outputs from local solver `Auto` (default) | `Use solver interpolant` | `Zero-order hold`

The local solver might need to provide values for output signals on
the model reference interface at the parent solver simulation time. To
provide the output signal values, the local solver interpolates
continuous state values that affect the output signal values or
interpolates the output signal values themselves. This parameter
specifies how the local solver interpolates the continuous state or
output signal values.

- `Auto` — The software determines
  the interpolation method based on how the local step size
  compares to the communication step size. *(since R2024a)*

  - When the local step size is smaller than the
    communication step size, the local solver interpolates
    the output signal values to the parent solver simulation
    time using a zero-order hold.
  - When the local step size is greater than or equal to
    the communication step size, the local solver
    interpolates continuous state values to the parent
    solver simulation time using the local solver
    interpolant. The local solver then computes the output
    signal values for the parent solver simulation time
    using the interpolated continuous state values.
- `Use solver interpolant` — The local
  solver interpolates continuous state values to the parent solver
  simulation time using the local solver interpolant. This option
  is supported only when the local step size is greater than or
  equal to the parent solver step size.
- `Zero-order hold` — The local solver
  interpolates output signal values to the parent solver
  simulation time using a zero-order hold.

Using the solver interpolant for interpolation generally increases
accuracy but also increases computational complexity. Zero-order hold
output handling reduces computational complexity but also reduces
accuracy.

The local solver propagates time independently during the local solver
advance phase that occurs when the parent solver executes the update
method for the Model block. Because the update method
executes before the advance method in the simulation loop for the parent solver:

- The local solver advance occurs before the parent solver
  advance.
- The local solver gets ahead of the parent solver in
  simulation time.

To compute output signal values to provide to the parent solver, the
local solver interpolates either the values of continuous states that
are used in the Model block output method or the output
signal values to the parent solver simulation time. For more
information, see Use Local Solvers in Referenced Models.

When you use a variable-step local
solver *(since R2025a)*, only `Zero-order hold`
input and output signal handling are supported.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
model configuration parameters for the model referenced by this
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputSignalHandling` |
| **Values:** | `"Auto"` (default) | `"Use solver interpolant"` | `"Zero-order Hold"` |

**Example:** `set_param(gcb,OutputSignalHandling="Zero-order
Hold")`

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

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

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. For more information about using the
Model block for HDL code generation and best practices and
limitations, see Model Referencing for HDL Code Generation (HDL Coder).

See also Generate Black Box Interface for Referenced Model (HDL Coder) and Generate Parameterized Code for Referenced Models (HDL Coder).

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `ModelReference` (default) | When you want to generate code from a referenced model and any nested models, use the `ModelReference` implementation. For more information, see Model Referencing for HDL Code Generation (HDL Coder). |
| `BlackBox` | Use the `BlackBox` implementation to instantiate an HDL wrapper, or black box interface, for legacy or external HDL code. If you specify a black box interface, HDL Coder does not attempt to generate HDL code for the referenced model.  For more information, see Generate Black Box Interface for Referenced Model (HDL Coder). |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

|  |  |
| --- | --- |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ReferenceModelPrefix** | Prefix of the referenced model to insert in the generated code. The code generator applies this prefix to submodel file names and HDL identifiers. The default prefix is `modelname_` where `modelname` is the name of the referenced model.  **Note**  - If you specify an empty prefix, the code generator   does not add a prefix to submodel file names. This can cause HDL compilation   errors due to naming collisions between the models. - If you use the referenced model as the DUT, the code   generator ignores the prefix that you specify. |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced before R2006a**

### R2025a: Variable-step local solver

You can now configure a referenced model to use a variable-step local solver.
Previously, only fixed-step local solvers were supported.

When you use a variable-step local solver, the **Communication step
size** parameter of the Model block specifies when the
parent and local solvers exchange data. Within the interval between hit times for
the communication step size, the variable-step local solver determines the size of
each local step based on the dynamics of the continuous states in the referenced
model and the tolerance values you specify for the local solver.

When you use a variable-step local solver, only `Zero-order
hold` input and output signal handling are supported.

For more information, see Use Local Solvers in Referenced Models.

### R2024b: Improved sample time propagation for output ports of model references that use local solvers

Model blocks that reference models configured to use local solvers
now propagate a discrete sample time to the block output ports if the local solver
uses zero-order hold output signal handling. The **Communication step
size** parameter of the Model block defines the discrete
sample time propagated to the block output ports. In previous releases, the
Model block propagated the sample time of the port in the
referenced model to the block output ports.

This change to sample time propagation:

- Simplifies the interactions between the parent solver and local
  solver
- More clearly reflects the effect of the zero-order hold output signal
  handling in the context of the parent model
- Reduces the number of parent solver resets

In some cases, the change to sample time propagation causes warnings about sample
time discrepancies or collisions. For example, when a Model block
output port that now has a discrete sample time drives the input port of another
model reference, the software issues a warning if the sample time of the input port
in the referenced model does not match the sample time of the input signal in the
top model. For more information, see Improve Simulation Performance Using Performance Advisor.

In most cases, this change does not affect numerical results and only results in
fewer or different points in logged data for the Model block output
signals. The table summarizes the impact of this change for different local solver
configurations.

| Local Solver Step Size | **Output signal handling** Parameter Value | Effect of Sample Time Propagation Change |
| --- | --- | --- |
| Local solver step size less than communication step size | `Zero-order hold` | Model block output ports have a discrete sample time defined by the **Communication step size** parameter of the block.  The change in sample time does not affect the numerical results of the simulation but can result in different or fewer data points in logged data for Model block output signals in the top model. |
| `Auto`  *Only zero-order hold output signal handling is supported.* |
| Local solver step size equal to communication step size | `Auto` | No change to sample time propagation. |
| `Use solver interpolant` |
| `Zero-order hold` | Model block output ports have a discrete sample time defined by the **Communication step size** parameter of the block.  The change in sample time can result in different or fewer data points in logged data for Model block output signals in the top model.  In rare cases, the change in sample time can affect numerical results as a result of:  - Applying the zero-order hold to output signals   that do not depend on continuous states in the   referenced model - Performing fewer parent solver resets |

### R2024a: Use local solver for components with faster dynamics

You can use local solvers for system components with faster dynamics by specifying
a local step size that is smaller than the parent solver step size. The new
**Communication step size** parameter specifies the discrete
rate for communication between the parent and local solver. The communication step
size is registered as a discrete rate in the parent model instead of the local
solver step size.

### R2024a: New default **Output signal handling** parameter value and improved behavior when **Input signal handling** parameter value is `Auto`

The default value of the **Output signal handling** parameter is
the new value `Auto`. When the **Output signal
handling** parameter value is `Auto`, the
software determines the method to use to interpolate continuous state or input
signal values to the parent solver simulation time based on how the local step size
compares to the communication step size. In previous releases, the local step size
had to be greater than or equal to the parent solver step size, and the
`Auto` option did not exist.

When the **Input signal handling** parameter value is
`Auto`, the software now determines how to extrapolate
continuous derivative or input signal values to the local simulation time based on
the model structure and how the local step size compares to the communication step
size. In previous releases, the software did not consider the model structure when
selecting the interpolation method. Considering how the local step size compares to
the communication step size was also not relevant because the
**Communication step size** parameter did not exist.

### R2024a: Use local solver for model that contains blocks with wrapped states

You can configure a model that contains one or more blocks with wrapped states to
use a local solver when referenced in a model hierarchy. Wrapping states can improve
numerical stability for systems with cyclical state values and allows the state
value to wrap to the start of the cycle without resetting the solver, which can slow
simulation performance.

For example, you can model the angular position of a wheel as having a value that
is always between 0 and 2*π*. When the wheel rotates beyond an
angular position of 2*π*, the angular position wraps back to 0
rather than continually increasing.

### R2023b: Create Model block ports without entering referenced model

Starting in R2023b, you can create ports on Model blocks without
entering the referenced model the same way you can on a Subsystem
block.

To create a port, pause on any of the four edges of the Model
block. When your pointer turns into a cross, click. A new port appears on the edge
you clicked, highlighted in blue. Pause your pointer on the new port. In the action
menu that expands, select the type of port you want to create.

To delete an existing port, select the port and press **Delete**. To
delete multiple ports, press **Shift** and select the ports. Then,
press **Delete**.

For more information about creating Model block ports, see Add Ports to Model Reference Interface.

### R2023a: Use local solver for model reference at any location in model hierarchy

Model blocks at any location in a model hierarchy can use a local
solver, including Model blocks inside referenced models that use
local solvers.

### R2022b: Local solver support for accelerator and rapid accelerator simulation

Accelerator and rapid accelerator mode support simulating model reference
hierarchies that use local solvers.

### R2022a: Use local solvers in referenced models

You can configure a referenced model to use a local solver when referenced by
another model. The local solver solves the referenced model as a separate system of
differential equations.

Using a local solver can facilitate system composition and integration. When you
use local solvers, you can solve referenced models in system-level simulations using
the same solver and step size used to design and test each model in isolation. Using
local solvers can also reduce the amount of configuration adjustments you need to
make to configuration parameters in referenced models while integrating the model
into a larger system.

For some systems, using a local solver can improve simulation performance by
allowing you to choose a solver that is more appropriate to solve the system in the
referenced model or by reducing the number of redundant calculations in systems that
have a wide range of dynamics among components.

These limitations apply for model hierarchies that reference one or more models
configured to use a local solver:

- Only models referenced from the top model can use local
  solvers.
- Local solvers are supported for only normal mode simulations.
- The parent solver can be a variable-step or fixed-step solver. The
  local solver must be a fixed-step solver.
- When the parent solver is a fixed-step solver, the local solver step
  size must be larger than the top solver step size.

For more information, see Use Local Solvers in Referenced Models.

### R2019a: Specifying variant models in Model blocks is no longer supported

Starting in R2019a, specifying variant models in Model blocks is no
longer supported. The Model Variants block, which was a
Model block preconfigured to specify variant models, is also no
longer supported. Loading a model that contains these blocks converts them to
Variant Subsystem blocks that contain Model blocks
that represent the variant choices.

Variant Subsystem blocks provide these advantages:

- You can mix Model blocks and Subsystem
  blocks as variant choices.
- You can specify variants that have different numbers of input and output
  ports.

The Variant Subsystem block parameter **Analyze all choices
during update diagram and generate preprocessor conditionals** behaves
differently from the Model block parameter **Generate
preprocessor conditionals**. Instead of causing simulation and update
diagram to compile the active variant only, the Variant Subsystem
block parameter compiles all variants.

If you have scripts that use Model block parameters for variants,
you must update them to use Variant Subsystem block
parameters.

## Description

Reference another model to create model hierarchy

The Model block references the specified model. It displays input and
output ports that correspond to the top-level input and output ports of the referenced
model. These ports allow you to connect the referenced model to other blocks in the
parent model.

To determine whether the Model block is better suited for your goal
than another block with similar functionality, see Explore Types of Model Components and Compare Capabilities of Model Components.

For instructions on how to reference a model with a Model block, see
Reference Existing Models.

By default, the Model block displays a representation of the contents
of the referenced model. For more information, see Preview Content of Model Components.
To see the contents of a referenced model, double-click the Model
block.

If you have a Simulink®
Coder™ license, you can conceal the implementation details of a referenced model
by protecting the model. To protect a model, see Protect Models to Conceal Contents (Simulink Coder). To
reference a protected model, see Reference Protected Models from Third Parties.
