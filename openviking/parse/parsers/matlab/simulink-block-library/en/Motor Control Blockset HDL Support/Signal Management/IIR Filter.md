---
type: simulink-block
title: 'IIR Filter'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'iirfilter'
documentation_source_path: '../mcb/ref/iirfilter.html'
language: en
---

# IIR Filter

## Ports
```yaml
ports:
- name: u
  summary: Sampled input signal scalar
  direction: input
  data_types: single | double | fixed point
- name: a
  summary: Filter coefficient scalar
  direction: input
  data_types: single | double | fixed point
- name: x0
  summary: Initial state signal scalar
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: External reset signal scalar
  direction: input
  data_types: single | double | fixed point
- name: y
  summary: Filtered output signal scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **u** — Sampled input signal scalar

Sampled values of the raw input signal in the time domain.

**Data Types:** `single` | `double` | `fixed point`

### **a** — Filter coefficient scalar

Filter coefficient of the IIR filter. The data type of this signal must be same as
that of the input signal **x**. This may restrict the signal
precision when used with fixed point data type.

#### Dependencies

To enable this port, set the **Filter coefficient** parameter
to `Input port`.

**Data Types:** `single` | `double` | `fixed point`

### **x0** — Initial state signal scalar

Initial value of the IIR filter state signal.

#### Dependencies

To enable this parameter, set the **Initial state** parameter
to `Input port`.

**Data Types:** `single` | `double` | `fixed point`

### **Reset** — External reset signal scalar

External signal that resets the block to deliver the **Initial
state** when in an active-high state.

#### Dependencies

To enable this parameter, set the **External reset** parameter
to `active high resets to initial condition`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **y** — Filtered output signal scalar

Filtered output signal returned by the IIR Filter block in the time domain.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Filter type
  summary: IIR filter type Low-pass (default) | High-pass
  group: ''
- name: Filter coefficient
  summary: Filter coefficient input method Specify via dialog (default) | Input port
  group: ''
- name: Filter coefficient value
  summary: Filter coefficient of IIR filter 0.01 (default) | scalar in the range (0,1]
  group: ''
- name: Initial state
  summary: Specify how to provide initial state value Specify via dialog (default) | Input port
  group: ''
- name: Initial state value
  summary: Initial value of state 0 (default) | scalar
  group: ''
- name: External reset
  summary: Specify whether to provide external reset signal none (default) | active high resets to initial condition
  group: ''
- name: Display cutoff frequency
  summary: Display the cutoff frequency parameters off (default) | on
  group: ''
- name: Discrete step size (s)
  summary: Sample time after which block executes again 50e-6 (default) | scalar
  group: ''
- name: Theoretical cutoff frequency (Hz)
  summary: Theoretical cutoff frequency of IIR filter 32.1525 | scalar
  group: ''
```

### **Filter type** — IIR filter type `Low-pass` (default) | `High-pass`

Type of IIR filter.

### **Filter coefficient** — Filter coefficient input method `Specify via dialog` (default) | `Input port`

Select one of these methods to specify the filter coefficient:

- `Specify via dialog` — Select this option if you want
  to specify the filter coefficient value using the block parameters dialog
  box.
- `Input port` — Select this option if you want to
  specify the filter coefficient value using an input port.

### **Filter coefficient value** — Filter coefficient of IIR filter `0.01` (default) | scalar in the range (0,1]

Filter coefficient of the IIR filter. The data type of this signal must be same as
that of the input signal **x**. This may restrict the signal precision
when used with fixed point data type.

#### Dependencies

To enable this parameter, set the **Filter coefficient**
parameter to `Specify via dialog`.

### **Initial state** — Specify how to provide initial state value `Specify via dialog` (default) | `Input port`

Specify whether to provide the initial state value as a block parameter or as an
input port.

Set this parameter to one of these options:

- `Specify via dialog` — Select this option if you want
  to specify the initial state value using the block parameters dialog box.
- `Input port` — Select this option if you want to
  specify the initial state value using an input port.

### **Initial state value** — Initial value of state `0` (default) | scalar

Initial value of the IIR filter state.

#### Dependencies

To enable this parameter, set the **Initial state** parameter to
`Specify via dialog`.

### **External reset** — Specify whether to provide external reset signal `none` (default) | `active high resets to initial condition`

Specify whether to provide an external reset signal as an input port.

Set this parameter to one of these options:

- `none` — Select this option if you do not want to
  provide an external reset signal.
- `active high resets to initial condition` — Select this
  option if you want to provide an external reset signal using an input port.

### **Display cutoff frequency** — Display the cutoff frequency parameters `off` (default) | `on`

Select this parameter for the block to display the **Theoretical cutoff
frequency (Hz)** parameter.

#### Dependencies

To enable this parameter, set the **Filter coefficient**
parameter to `Specify via dialog`.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

**Note**

The block uses this value to compute and display the **Theoretical cutoff
frequency (Hz)** in the block dialog box. This parameter does not set the
sample time of the block. The block inherits the sample time from the model.

#### Dependencies

To display this parameter:

- Set the **Filter coefficient** parameter to
  `Specify via dialog`.
- Select the **Display cutoff frequency** parameter.

### **Theoretical cutoff frequency (Hz)** — Theoretical cutoff frequency of IIR filter `32.1525` | scalar

Computed theoretical cutoff frequency (in Hertz) of the IIR filter. This parameter
is not configurable.

#### Dependencies

To display this parameter:

- Set the **Filter coefficient** parameter to
  `Specify via dialog`.
- Select the **Display cutoff frequency** parameter.
## Libraries

Motor Control Blockset / Signal Management Motor Control Blockset HDL Support / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

### R2025a: New input port and block parameters added

The Block Parameters dialog box now includes parameters for you to specify the initial
output value and an external reset signal from input ports.

## Description

Implement infinite impulse response (IIR) filter

The IIR Filter block implements a discrete first-order infinite impulse
response (IIR) filter on the specified input signal. The block supports fixed-point and
floating-point data types. The block is also optimized for code generation when you use it
with the model settings and configuration adopted by the examples shipped with Motor Control Blockset™.

It is recommended that you use a fixed-step discrete solver for this block to enable code
generation and ensure accurate simulation.

### Equations

You can configure the IIR filter by using the filter coefficient (a) block parameter to set the required cutoff frequency (*f*c) for the filter. Optionally, you can also provide the filter coefficient
value through an input port.

If you know the cutoff frequency of the filter, you can compute the required filter
coefficient using this equation:

a= ( 2πTsfc2πTsfc+1 )

The block also includes the option of displaying the cutoff frequency for a given filter
coefficient and sample time on the block mask.

Use the **Filter type** parameter to configure the block either as a
lowpass or highpass filter.

The following two equations describe how the block computes its output.

`Lowpass Filter:`

y(k)=a⋅u(k)+(1−a)⋅y(k−1)

`Highpass Filter:`

y(k)=(1−a)[u(k)−u(k−1)+y(k−1)]

where:

- *f*c is the cutoff frequency of the IIR filter.
- a is the filter coefficient (0 < a ≤ 1).
- y(k) is the output value at time k.
- y(k−1) is the output value at time k−1.
- x(k) is the input value at time k.
- x(k−1) is the input value at time k−1.
- *T*s is the sample time of the IIR Filter block.

Both lowpass and highpass IIR filters can be modeled as RC filters, where the state
value corresponds to the voltage drop across the capacitor.

The following equations describe how the block computes the initial output
`y0` from the initial input
`u0` and initial state
`x0`.

`Lowpass Filter:`

y0=x0

`Highpass Filter:`

y0=u0−x0
