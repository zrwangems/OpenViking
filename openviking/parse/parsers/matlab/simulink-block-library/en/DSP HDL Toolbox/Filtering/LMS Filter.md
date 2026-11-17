---
type: simulink-block
title: 'LMS Filter'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'lmsfilter'
documentation_source_path: 'ref/lmsfilter.html'
language: en
---

# LMS Filter

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar or column vector of real or complex values
  direction: input
  data_types: single | double | fixed point
- name: desired
  summary: Desired input data scalar or column vector of real or complex values
  direction: input
  data_types: single | double | fixed point
- name: valid
  summary: Indicates valid input data scalar
  direction: input
  data_types: Boolean
- name: stepSize
  summary: Convergence and stability of filter real scalar
  direction: input
  data_types: double | single | fixed point
- name: adapt
  summary: Update filter weights scalar
  direction: input
  data_types: Boolean
- name: reset
  summary: Clears internal states scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Filtered output data scalar or column vector of real or complex values
  direction: output
  data_types: single | double | fixed point
- name: valid
  summary: Indicates valid output data scalar
  direction: output
  data_types: Boolean
- name: error
  summary: Error between output and desired signals real or complex scalar or column vector
  direction: output
  data_types: Boolean
- name: weights
  summary: Updated filter weights row vector
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data scalar or column vector of real or complex values

Input data, specified as a scalar or column vector of real or complex values. The
input vector size must be in the range [2, 64] and it must be less than the filter
length. The block can only support input word lengths of up to 32 bits.

Use `double` and `single` data types for
simulation, but not for HDL code generation. For HDL code generation, the input date
type must be `signed fixed point`.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **desired** — Desired input data scalar or column vector of real or complex values

Desired input data, specified as a scalar or column vector of real or complex
values. The input vector size must be in the range [2, 64] and it must be less than
filter length. The **desired** port must have the same data type,
complexity, and dimensions as the input **data** port.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input ports **data** and
**desired**. When **valid** is
`0` (`false`), the block ignores the values from
the input ports **data** and **desired**.

**Data Types:** `Boolean`

### **stepSize** — Convergence and stability of filter real scalar

Specify the step size to control convergence and stability of the filter. The
recommended step size must be less than 1/(2 x *Input power* x
*Filter length*).

You can use `double` and `single` data types for
simulation, but not for HDL code generation. For HDL code generation, the input date
type must be `unsigned fixed point`.

#### Dependencies

To enable this port, on the **Main** tab, set the
**Step-size source** parameter to `Input
port`.

**Data Types:** `double` | `single` | `fixed point`

### **adapt** — Update filter weights scalar

When **adapt** is `1` (`true`)
and input **valid** is `1`
(`true`), the block adapts to the new filter weights for every input
**valid**. When the **adapt** is
`0` (`false`) and the input
**valid** is `1` (`true`) or
`0` (`false`), the block remains at its previous
filter weights.

#### Dependencies

To enable this port, on the **Main** tab, select the
**Enable adapt input port** parameter.

**Data Types:** `Boolean`

### **reset** — Clears internal states scalar

Control signal that clears internal states. When **reset** is
`1` (`true`), the block stops the current
calculation, clears internal states, and sets to the initial values of filter weights
specified on the block mask. When the **reset** is
`0` (`false`) and the input
**valid** is `1` (`true`), the
block captures data for processing.

For more reset considerations, see the Reset Signal section on the
Hardware Control Signals page.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable reset input port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Filtered output data scalar or column vector of real or complex values

Filtered output data, returned as a scalar or column vector of real or complex
values. The dimensions of the output match the dimensions of the input.

When the input data is a floating-point type, the output data inherits the data
type of the input data. When the input data is a fixed-point type, the output data is
a fixed point with word length and fractional length incremented by 1.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the output **data** port. When **valid** is
`0` (`false`), the values from the output
**data** port are not valid.

**Data Types:** `Boolean`

### **error** — Error between output and desired signals real or complex scalar or column vector

Outputs the result of subtracting the filtered output signal from the desired
signal when the output **valid** is `1`
(`true`).

If the input data and desired is a scalar or a column vector, the error signal has
the same dimension and complexity as the input data. When the input data is a
floating-point type, the output data inherits the data type of the input data. When
the input data is a fixed-point type, the output data is fixed point with word length
incremented by 2 and fractional length incremented by 1.

#### Dependencies

To enable this port, on the **Main** tab, select the
**Enable filter error output port** parameter.

**Data Types:** `Boolean`

### **weights** — Updated filter weights row vector

For each iteration, the block outputs the current updated filter weights from this
port when the output **valid** is `1`
(`true`).

For floating-point inputs, the weights data type must match the input type. For
fixed-point signals, the input must match the data type set to the
**Weights** parameter.

#### Dependencies

To enable this port, on the **Main** tab, select the
**Enable filter weights output port** parameter.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Filter length
  summary: Filter length 32 (default) | positive integer less than or equal to 2048
  group: Main
- name: Step-size source
  summary: Step size source Property (default) | Input port
  group: Main
- name: Step size (mu)
  summary: Step size 0.01 (default) | positive scalar numeric value
  group: Main
- name: Initial value of filter weights
  summary: Initial value of filter weights 0 (default) | scalar | row vector
  group: Main
- name: Enable adapt input port
  summary: Option to enable adapt input port off (default) | on
  group: Main
- name: Enable filter weights output port
  summary: Option to enable weights output port on (default) | off
  group: Main
- name: Enable filter error output port
  summary: Option to enable error output port off (default) | on
  group: Main
- name: Rounding mode
  summary: Rounding mode for type-casting the output Floor (default) | Ceiling | Convergent | Nearest | Round | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow handling for type-casting the output off (default) | on
  group: Data Types
- name: Step size
  summary: 'Step size type Inherit: Same word length as input (default) | fixdt(0,16,16) | <data type expression>'
  group: Data Types
- name: Weights
  summary: 'Filter weights type fixdt(1,16,15) (default) | Inherit: Same as input | <data type expression>'
  group: Data Types
- name: Step-size error product
  summary: 'Step size error product type Inherit: Same word length as input (default) | Inherit: Inherit via internal rule
    | fixdt(1,16,15) | <data type expression>'
  group: Data Types
- name: Enable reset input port
  summary: Option to enable reset input port off (default) | on
  group: Control Ports
- name: Use HDL global reset
  summary: Option to connect data path registers to generated HDL global reset signal off (default) | on
  group: Control Ports
```

### Main

### **Filter length** — Filter length `32` (default) | positive integer less than or equal to 2048

Specify the length of the LMS filter as a positive integer less than or equal to
2048.

### **Step-size source** — Step size source `Property` (default) | `Input port`

Select whether the block specifies the step size through property or input
port.

- `Property` — Specify step size by using the
  **Step size (mu)** parameter.
- `Input port` — Specify step size by using the
  **stepSize** port.

### **Step size (mu)** — Step size `0.01` (default) | positive scalar numeric value

Specify the step size as a positive scalar numeric value. The recommended step
size must be less than 1/(2 x *Input power* x *Filter
length*).

#### Dependencies

To enable this parameter, set the **Step-size source**
parameter to `Property`.

### **Initial value of filter weights** — Initial value of filter weights `0` (default) | scalar | row vector

Enter the initial filter weights as a scalar or row vector of size equal to filter
length.

When you specify a scalar value, the block considers it as a row vector equivalent
to the specified scalar value.

### **Enable adapt input port** — Option to enable adapt input port `off` (default) | on

Select this parameter to enable the **adapt** input port.

### **Enable filter weights output port** — Option to enable weights output port `on` (default) | off

Select this parameter to enable the **weights** output
port.

For each iteration, the block outputs the current updated filter weights from this
port.

### **Enable filter error output port** — Option to enable error output port `off` (default) | on

Select this parameter to enable the **error** output port.

### Data Types

### **Rounding mode** — Rounding mode for type-casting the output `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Rounding mode for type-casting the output to the data type specified by the
**Output** parameter. When the input data type is floating point,
the block ignores this parameter. For more details, see Rounding Modes.

### **Saturate on integer overflow** — Overflow handling for type-casting the output `off` (default) | `on`

Overflow handling for type-casting the output to the data type specified by the
**Output** parameter. When the input data type is floating point,
the block ignores this parameter. For more details, see Overflow Handling.

### **Step size** — Step size type `Inherit: Same word length as input` (default) | `fixdt(0,16,16)` | `<data type expression>`

Specify the step size data type.

#### Dependencies

To enable this parameter, set the **Step-size source**
parameter to `Property`.

### **Weights** — Filter weights type `fixdt(1,16,15)` (default) | `Inherit: Same as input` | `<data type expression>`

Specify the data type for the filter weights.

### **Step-size error product** — Step size error product type `Inherit: Same word length as input` (default) | `Inherit: Inherit via internal rule` | `fixdt(1,16,15)` | `<data type expression>`

Specify the step size error product.

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this check box to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path
registers.

For more reset considerations, see the Reset Signal section on
the Hardware Control Signals
page.

### **Use HDL global reset** — Option to connect data path registers to generated HDL global reset signal `off` (default) | `on`

Select this check box to connect the generated HDL global reset signal to the
data path registers. This parameter does not change the appearance of the block
or modify simulation behavior in Simulink. When you clear this check box, the generated HDL global reset
clears only the control path registers. The generated HDL global reset can be
synchronous or asynchronous depending on the **HDL Code Generation** > **Global Settings** > **Reset type** parameter in the model Configuration Parameters.

For more reset considerations, see the Reset Signal section on
the Hardware Control Signals
page.
## Libraries

DSP HDL Toolbox / Filtering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2023a**

## Description

Minimize error between observed and desired signals

The LMS Filter  block estimates the filter weights and minimizes the error
between a desired signal and an observed signal using the mean square error (MSE) criteria.
The block adapts its weights until the error between the data and the desired data is minimal.
The block accepts scalar and vector inputs of type real and complex.

You can use this block for various applications, such as noise cancellation, system
identification, and inverse system modeling. The block provides an architecture suitable for
HDL code generation and hardware deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
