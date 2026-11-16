---
type: simulink-block
title: 'Stop Simulation'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sinks'
documentation_page: 'stopsimulation'
documentation_source_path: 'slref/stopsimulation.html'
language: en
---

# Stop Simulation

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Stop simulation when input signal is nonzero. This port accepts real
signals of `double` or `Boolean` data
types.

**Data Types:** `double` | `Boolean`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely varying execution times. While the code is functionally valid and acceptable
in resource-rich environments, smaller embedded targets often cannot support such
code. Usually, blocks evolve toward being suitable for production code. Thus, blocks
suitable for production code remain suitable.

Generated code stops executing when the stop condition is true.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

Stop simulation when input is nonzero

The Stop Simulation block stops the simulation when the input is
nonzero. The simulation completes the current time step before terminating. If the block
input is a vector, any nonzero vector element causes the simulation to stop.

When you use the Stop Simulation block in a For Iterator subsystem, the stop action
occurs after execution of *all* iterations in the subsystem during a
time step. The stop action does not interrupt execution until the start of the next time
step.

You cannot use the Stop Simulation block to pause the simulation. To
create a block that pauses the simulation, see Pause Simulation Using Assertion Blocks.
