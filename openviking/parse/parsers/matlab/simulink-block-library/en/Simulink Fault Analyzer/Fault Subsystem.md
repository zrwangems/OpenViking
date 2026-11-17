---
type: simulink-block
title: 'Fault Subsystem'
family: 'fault-analyzer'
product_id: 'fault-analyzer'
product_name: 'Simulink Fault Analyzer'
documentation_release: R2025b
official_category: ''
documentation_page: 'faultsubsystem'
documentation_source_path: 'ref/faultsubsystem.html'
language: en
---

# Fault Subsystem

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Fault Analyzer

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Model behaviors for fault injection

Use these blocks to model fault behavior. Fault Subsystem blocks contains
a Fault Inport
block that retrieves the signal you want to modify, and a Fault Outport
block that outputs the signal. Connect the behavior between these two blocks.

When you add fault behaviors to faults, Simulink®
Fault Analyzer™ creates a copy of the fault behavior from the library and stores the model in
this block. You can pick from built-in behaviors or create and register custom behaviors. See
Create Predefined and Custom Fault Behaviors.

Each Fault Subsystem block can contain only one Fault Input
and Fault Outport block. To retrieve additional model signal data for use
Fault Subsystem blocks, use Fault Data Inport blocks.
