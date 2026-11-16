---
type: simulink-block
title: 'Dataflow Subsystem'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Dataflow'
documentation_page: 'dataflowsubsystem'
documentation_source_path: 'ref/dataflowsubsystem.html'
language: en
---

# Dataflow Subsystem

## Ports

### Input

### **In** — Signal input to dataflow subsystem scalar | vector | matrix

Placing an Inport block in a subsystem adds an external input port
to the block. The port label on the subsystem block is the name of the
Inport block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Signal output from dataflow subsystem scalar | vector | matrix

Placing an Outport block in a subsystem adds an output port from
the block. The port label on the subsystem block is the name of the
Outport block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

The Dataflow Subsystem block uses the same parameters as the
Subsystem block. For parameter descriptions and programmatic use information,
see Subsystem, Atomic Subsystem, Nonvirtual Subsystem,
CodeReuse Subsystem (Simulink).

**Note**

The topmost dataflow subsystem is treated as an atomic subsystem. All child dataflow
subsystems are treated as virtual subsystems.

### **Latency** — Latency of dataflow subsystem 0 (default) | scalar integer

To increase the throughput of a system, it can be advantageous to increase the
latency of the system. Specify the **Latency** value in the
**Execution** tab of the Property Inspector. For more information,
see Latency.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Latency` |
| **Type**: character vector |
| **Values**: scalar integer |
|  |
| **Default**: `'0'` |

### **Automatic frame size calculation** — Automatically calculate frame sizes and insert buffers 0 (default) | 1

When the **Automatic frame size calculation** parameter is enabled,
dataflow domains automatically calculate frame sizes and insert buffers into your model,
avoiding signal size propagation errors in multirate signal processing systems. For more
information, see Automatic Frame Size Calculation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AutoFrameSizeCalculation` |
| **Type**: character vector |
| **Values**: `'off'`|`'on'` |
|  |
| **Default**: `'off'` |

## Libraries

DSP System Toolbox / Dataflow

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

Dataflow subsystems can generate single-core or multi-core code. For more information on
setting up your dataflow subsystem for code generation, see Multicore Simulation and Code Generation of Dataflow Domains.

## Version History

**Introduced in R2018b**

## Description

Subsystem whose execution domain is set to Dataflow

The Dataflow Subsystem block is a Subsystem block
preconfigured with the execution domain set to dataflow. A Dataflow Subsystem uses synchronous
dataflow as a model of computation, which is data-driven and statically scheduled.

Dataflow Subsystems help to

- Improve simulation throughput with multithreaded execution

  Dataflow domains leverage the multicore CPU architecture of the host computer and
  can improve simulation speed significantly. It automatically partitions your model and
  simulates the system using multiple threads. By adding latency to your system, you can
  further increase concurrency and improve simulation throughput of your model.
- Automatically infer signal sizes for frame-based multirate models

See Dataflow Domain for more information.
