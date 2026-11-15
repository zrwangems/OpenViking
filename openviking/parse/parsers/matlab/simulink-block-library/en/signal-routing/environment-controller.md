---
type: simulink-block
title: 'Environment Controller'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'environmentcontroller'
language: en
---

# Environment Controller

(Removed) Create branches of block diagram that apply only to simulation or only to code generation

## Libraries

Simulink / Signal Routing

## Description

The Environment Controller block outputs the signal at its
**Sim** port only if the model that contains it is being simulated.
It outputs the signal at its **Coder** port only if code is being
generated from the model. This option enables you to create branches of a block diagram
that apply only to simulation or code generation. This table describes various scenarios
where either the **Sim** or **Coder** port
applies.

| Scenario | Output |
| --- | --- |
| Normal mode simulation | **Sim** |
| Accelerator mode simulation | **Sim** |
| Rapid accelerator mode simulation | **Sim** |
| Simulation of a referenced model in normal or accelerator modes | **Sim** |
| Simulation of a referenced model in processor-in-the-loop (PIL) mode | **Coder**  (uses the same code generated for a referenced model) |
| External mode simulation | **Coder** |
| Standard code generation | **Coder** |
| Code generation of a referenced model | **Coder** |

Simulink®
Coder™ software does not generate code for blocks connected to the
**Sim** port if these conditions hold:

- On the **Code Generation > Optimization** pane of the
  Configuration Parameters dialog box, you set **Default parameter
  behavior** to `Inlined`.
- The blocks connected to the **Sim** port do not have external
  signals.
- The **Sim** port input path does not contain an S-function or
  an Interpreted MATLAB Function block.

If you enable block reduction optimization, Simulink eliminates blocks in the branch connected to the
**Coder** port when compiling the model for simulation. For more
information, see Block reduction.

**Note**

Simulink
Coder code generation eliminates the blocks connected to the simulation
branch only if the simulation branch has the same signal dimensions as the code
generation branch. Regardless of whether it eliminates the simulation branch,
Simulink
Coder uses the sample times on the simulation branch as well as the code
generation branch to determine the fundamental sample time of the generated code and
might, in some cases, generate sample-time handling code that applies only to sample
times specified on the simulation branch.

## Ports

### Input

### **Sim** — Simulation input scalar | vector | matrix

Simulation input values, specified as a scalar, vector, or matrix.
Input signal must have the same width as the input to the
**Coder** port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Coder** — Code generation input scalar | vector | matrix

Code generation input values, specified as a scalar, vector, or
matrix. Input signal must have the same width as the input to the
**Sim** port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Values from simulation or code generation input port scalar | vector | matrix

Values from the **Sim** or **Coder**
input port, depending on the current environment. For more information
on what the block outputs in various simulation and code generation
modes, see Description.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions on speed
and memory often found in embedded systems. Generated code can contain dynamic
allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Environment Controller block has been removed

The Environment Controller block has been removed from the Signal
Routing library. Existing models that use this block continue to work with a
warning. Use the Variant Source block with the
**Variant control mode** parameter set to `sim codegen
switching` instead. You can use Model Advisor or Upgrade Advisor to
automatically identify and replace all instances of the Environment
Controller block with the Variant Source block. For
information on the Model advisor check, see Identify Environment Controller Blocks and Replace Them with Variant Source Blocks.

Variant blocks offer these advantages over the Environment
Controller block:

- Variant Source block with the **Variant control
  mode** parameter set to `sim codegen
  switching` allows you to automatically switch between
  simulation and code generation workflows. In this mode, Variant
  Source block supports these activation times:

  | Variant activation time | Behavior |
  | --- | --- |
  | `update diagram` | Simulink sets the active choice during update diagram before the propagation of signal attributes. Inactive choices are removed prior to propagation of signal attributes, so the generated code contains only the active choice. |
  | `update diagram analyze all choices` | Simulink sets the active choice during update diagram after the propagation of signal attributes. Signal attributes are propagated to both active and inactive choices to check for consistency. Inactive choices are removed at the end of update diagram before model start occurs. The generated code contains only active choices. |
- Variant Sink block enables branching on the output side
  (destination of a signal).
- Variant blocks highlight the path of the active variant choice during
  simulation and code generation.
- Variant Source block offers optimal code generation
  compared to the Environment Controller block. The
  Environment Controller block can retain blocks
  connected to the **Sim** port in the generated
  code.
- Variant blocks can be centrally managed using the Variant Manager
  tool, which offers these key capabilities:

  - Visualize the variant model hierarchy.
  - Define and validate multiple variant configurations of the
    model.
  - Generate a simplified model for a variant configuration
    using the Variant Reducer tool. For variant blocks with the
    **Variant control mode** parameter set
    to `sim codegen switching`, you can choose
    to retain the simulation branch or the code generation
    branch in the reduced model.
  - Compare variant configurations using the Variant
    Configuration Analysis tool.

  For more information, see Variant Manager for Simulink.
