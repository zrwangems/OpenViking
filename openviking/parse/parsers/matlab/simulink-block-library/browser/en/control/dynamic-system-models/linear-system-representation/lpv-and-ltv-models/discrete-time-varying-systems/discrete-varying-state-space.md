---
type: simulink-block
title: 'Discrete Varying State Space'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Discrete Time'
documentation_page: 'discretevaryingstatespace'
documentation_source_path: '../control/ref/discretevaryingstatespace.html'
language: en
---

# Discrete Varying State Space

## Ports

### Input

### **uk** — System input scalar | vector

System input signal.

### **A** — State matrix matrix

State matrix of dimensions *Nx*-by-*Nx*, where *Nx* is
the number of system states.

### **B** — Input matrix matrix

Input matrix of dimensions *Nx*-by-*Nu*, where *Nu* is
the number of system inputs.

### **C** — Output matrix matrix

Output matrix *Ny*-by-*Nx*, where *Ny* is
the number of system outputs.

### **D** — Feedforward matrix matrix

Feedforward matrix of dimensions *Ny*-by-*Nu*.

For a zero-feedthrough
state-space model, clear the **Enable feedthrough**
checkbox. Clearing this checkbox disables the **D**
input port. *(since R2023a)*

### **dx0** — State derivative offsets matrix

*Since R2024a*

State derivative offsets of dimensions *Nx*-by-1, where *Nx* is
the number of system states.

#### Dependencies

To enable this port, select
**Enable state derivative offsets dx0**. *(since R2024a)*

### **x0** — State offsets matrix

*Since R2024a*

State offsets of dimensions *Nx*-by-1, where *Nx* is
the number of system states.

#### Dependencies

To enable this port, select
**Enable state offsets x0**. *(since R2024a)*

### **u0** — Input offsets matrix

*Since R2024a*

Input offsets of dimensions *Nu*-by-1, where *Nu* is
the number of system inputs.

#### Dependencies

To enable this port, select
**Enable input offsets u0**. *(since R2024a)*

### **y0** — Output offsets matrix

*Since R2024a*

Output offsets of dimensions *Ny*-by-1, where *Ny* is
the number of system outputs.

#### Dependencies

To enable this port, select
**Enable output offsets y0**. *(since R2024a)*

### **IC** — Initial condition vector

*Since R2024b*

Initial conditions to use with the local model to start the
simulation, specified as a vector of length equal to the number of model
states.

#### Dependencies

To enable this port, set **Initial condition
source** to `external`.
### Output

### **yk** — System output scalar | vector

System output signal.

### **xk** — Current state vector vector

Current state values.

#### Dependencies

To enable this port, select the **Output states**
parameter.

### **xk+1** — Next state vector vector

State values at next time step.

#### Dependencies

To enable this port, select the **Output state
updates** parameter.

## Parameters

### Main Tab

### **Initial condition source** — Option to set initial condition using external signal `internal` (default) | `external`

*Since R2024b*

Specify the initial condition source.

- `internal` — Specify the initial
  conditions of the states using the **Initial
  condition** parameter.
- `external` — Specify the initial
  conditions of the states at the **IC** input
  port of the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialConditionSource` |
| **Values:** | `internal` (default) | `external` |

### **Initial conditions** — System initial conditions 0 (default) | scalar | vector

Initial state values, specified as a vector of length equal to the
number of model states.

#### Dependencies

To enable this parameter, set **Initial condition
source** to `internal`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialCondition` |
| **Values:** | `"0"` (default) | initial state values in quotes |

**Example:** `set_param(gcb,"InitialCondition","[0
0.1]")`

### **Sample time (-1 for inherited)** — Block sample time –1 (default) | positive scalar

Block sample time, specified as either –1 (inherited sample time) or a
positive scalar value.

### **Output states** — Provide state output on (default) | off

Select to enable the state values output port,
**x**.

### **Output state derivatives** — Provide state updates on (default) | off

Select to enable the state updates output port,
**xk+1**.

### **Enable feedthrough** — Add input port for feedthrough matrix `on` (default) | `off`

*Since R2023a*

Enable the **D** input port for a state-space model
with direct feedthrough. For a zero-feedthrough model, clear this
checkbox. Disabling the port for zero-feedthrough models is numerically
more reliable than feeding a zero-constant into the port.

### Offsets Tab

### **Enable state offsets x0** — Add input port for state offsets off (default) | on

Enable the **x0** input port for specifying varying
state offsets.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputX0` |
| **Values:** | `"off"` (default) | `"on"` |

### **Enable state derivative offsets dx0** — Add input port for state derivative offsets off (default) | on

Enable the **dx0** input port for specifying varying
state derivative offsets.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputDX0` |
| **Values:** | `"off"` (default) | `"on"` |

### **Enable input offsets u0** — Add input port for input offsets off (default) | on

Enable the **u0** input port for specifying varying
input offsets.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputU0` |
| **Values:** | `"off"` (default) | `"on"` |

### **Enable output offsets y0** — Add input port for output offsets off (default) | on

Enable the **y0** input port for specifying varying
output offsets.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `InputY0` |
| **Values:** | `"off"` (default) | `"on"` |

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2017b**

### R2024b: Specify initial condition externally as block input

The block now allows you to specify initial state values at the block input port
**IC**. To enable this port, set the **Initial
condition source** parameter to
`external`.

### R2024b: Initial condition parameter `x0` renamed to `InitialCondition`

The Initial state parameter `x0` for programmatic use is now
called `InitialCondition`. If your code sets this parameter
programmatically using, for example `set_param(blockPath,"x0","[0
0.1]")`, update your code to
`set_param(blockPath,"InitialCondition","[0 0.1]")`.

### R2024a: Support for specifying offsets

Use the **Offsets** tab of the block parameters to enable the
input ports for specifying instantaneous values of the varying offsets.

### R2023a: Enable feedthrough checkbox added

For a zero-feedthrough state-space model, clear the **Enable
feedthrough** checkbox. Clearing this checkbox disables the
**D** input port. Disabling the port for zero-feedthrough
models is numerically more reliable than feeding a zero-constant into the
port.

## Description

Discrete-time state-space model with varying matrix values

Use this block to implement a discrete-time state-space model with varying matrices.
Feed the instantaneous values of the state matrix *A*, input matrix
*B*, output matrix *C*, and feedforward matrix
*D* to the corresponding input ports. The system response is given
by:

xk+1=Axk+Bukyk=Cxk+Duk,

where *uk* is the system input,
*yk* is the system output,
*xk* is the current system state, and *x**k*+1 is the system state at the next time step.

The block also lets you specify varying offsets *(since R2024a)*.
Then, the system response is given by:

xk+1=dx0k+A(xk−x0k)+B(uk−u0k)yk=y0k+C(xk−x0k)+D(uk−u0k),

where *u*0*k* is the input
offset, *y*0*k* is the output
offset, and *x*0*k* and
*dx*0*k* are the state
offset and state derivative offset, respectively.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the **C** and **D** matrices depend
on the system output **yk**. If you have
such dependence, the resulting state-space equation *yk* =
*C*(*yk*)*xk*
+
*D*(*yk*)*uk* creates an algebraic loop, because computing the output value
*yk* requires knowing the output
value. This algebraic loop is prone to instability and divergence. Instead, try
expressing **C** and **D** in terms of the time
*t*, the block input
**uk**, and the state outputs
**xk**.

For similar reasons, avoid making **A** and
**B** depend on the
**xk+1** output. Note that it is safe
for **A** and **B** to depend on
**yk** when
**yk** is a fixed combination of
states and inputs (in other words, when *yk* =
*C**xk* +
*D**uk*, where *C* and *D* are constant
matrices).
