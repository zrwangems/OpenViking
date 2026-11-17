---
type: simulink-block
title: 'Terminator'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'terminator'
documentation_source_path: '../simulink/slref/terminator.html'
language: en
---

# Terminator

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix | n-D array | bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix | n-D array | bus

Use this port to direct signals from output ports that are otherwise
unconnected during a simulation. The port accepts real or complex
signals of all data types.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Terminate unconnected output port

Use the Terminator block to cap blocks whose output ports do not connect to other
blocks. If you run a simulation with blocks having unconnected output ports, Simulink® issues warning messages. Using Terminator blocks to cap those blocks helps
prevent warning messages.
