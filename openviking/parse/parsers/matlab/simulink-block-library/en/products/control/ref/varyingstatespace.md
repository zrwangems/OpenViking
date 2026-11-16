---
type: simulink-block
title: 'Varying State Space'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / LPV and LTV Models / Continuous-Time Varying Systems'
documentation_page: 'varyingstatespace'
documentation_source_path: 'ref/varyingstatespace.html'
language: en
---

# Varying State Space

## Ports

### Input

### **u** — System input scalar | vector

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

To enable this port, select **Enable state derivative
offsets dx0**.

### **x0** — State offsets matrix

*Since R2024a*

State offsets of dimensions *Nx*-by-1, where *Nx* is
the number of system states.

#### Dependencies

To enable this port, select **Enable state offsets
x0**.

### **u0** — Input offsets matrix

*Since R2024a*

Input offsets of dimensions *Nu*-by-1, where *Nu* is
the number of system inputs.

#### Dependencies

To enable this port, select **Enable input offsets
u0**.

### **y0** — Output offsets matrix

*Since R2024a*

Output offsets of dimensions *Ny*-by-1, where *Ny* is
the number of system outputs.

#### Dependencies

To enable this port, select **Enable output offsets
y0**.

### **IC** — Initial condition vector

*Since R2024b*

Initial conditions to use with the local model to start the
simulation, specified as a vector of length equal to the number of model
states.

#### Dependencies

To enable this port, set **Initial condition
source** to `external`.
### Output

### **y** — System output scalar | vector

System output signal.

### **x** — Current state vector vector

Current state values.

#### Dependencies

To enable this port, select the **Output states**
parameter.

### **dx** — State derivatives vector

Current derivatives of the corresponding states in
**x**.

#### Dependencies

To enable this port, select the **Output state
derivatives** parameter.

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

### **State names** — System state names `''` (default) | character vector | cell array

To identify system states, specify state names as a:

- character vector, for a one-state plant.
- Cell array of character vectors, for a multistate
  plant.

### **Output states** — Provide state output on (default) | off

Select to enable the state values output port,
**x**.

### **Output state derivatives** — Provide state derivatives on (default) | off

Select to enable the state derivatives output port,
**dx**.

### **Enable feedthrough** — Add input port for feedthrough matrix on (default) | off

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

State-space model with varying matrix values

Use this block to implement a continuous-time state-space model with varying matrices.
Feed the instantaneous values of the state matrix *A*, input matrix
*B*, output matrix *C*, and feedforward matrix
*D* to the corresponding input ports. The system response is given
by:

dx=Ax+Buy=Cx+Du,

where *u* is the system input, *y* is the system
output, and *x* and *dx* are the state vector and
state derivatives, respectively.

The block also lets you specify varying offsets *(since R2024a)*.
Then, the system response is given by:

dx=dx0+A(x−x0)+B(u−u0)y=y0+C(x−x0)+D(u−u0),

where *u*0 is the input offset,
*y*0 is the output offset, and
*x*0 and
*dx*0 are the state offset and state
derivative offset, respectively.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the **C** and **D** matrices depend
on the system output **y**. If you have such dependence, the
resulting state-space equation *y* =
*C*(*y*)*x* +
*D*(*y*)*u* creates an algebraic loop, because computing the output value
*y* requires knowing the output value. This algebraic loop is
prone to instability and divergence. Instead, try expressing **C**
and **D** in terms of the time *t*, the block
input **u**, and the state outputs **x**.

For similar reasons, avoid making **A** and
**B** depend on the **dx** output. Note that
it is safe for **A** and **B** to depend on
**y** when **y** is a fixed combination of
states and inputs (in other words, when *y* = *C**x* +
*D**u*, where *C* and *D* are constant
matrices).
