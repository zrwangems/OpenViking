---
type: simulink-block
title: 'SLRT Overload Options'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Execution Parameters'
documentation_page: 'slrtoverloadoptions'
documentation_source_path: 'io_ref/slrtoverloadoptions.html'
language: en
---

# SLRT Overload Options

## Ports

### Input

### **TID** — Task ID int

Connect any signal from the model to the TID (Task ID) port and the block applies
the overload options to the model task in which the signal executes.

**Example:**
`1`
### Output

### **Count** — Overload count int

The CPU overload count for the selected model rate.

## Parameters

### **Startup Duration** — Select startup steps for ignoring CPU overloads `1` (default) | int

The number of startup execution steps for which overloads are ignored.

#### Programmatic Use

```
startupDur
```

### **Source** — Selects CPU overload input during startup `Tunable Parameter` (default) | `Input Port`

The source of CPU overloads for the model rate during startup can be a tunable
parameter or a block input port.

#### Programmatic Use

```
startupDurSrc
```

### **Max Overloads** — Select maximum CPU overloads `0` (default) | int

The number of accepted overloads before execution is halted. There is a separate
overload counter for each sub-rate. Each counter is compared to **Max
Overloads** separately, not compared to the sum of the counters.

#### Programmatic Use

```
maxOverload
```

### **Source** — Selects CPU overload input after startup `Tunable Parameter` (default) | `Input Port`

The source of CPU overloads for the model rate after startup can come from a tunable
parameter or from the block input port.

#### Programmatic Use

```
maxOverloadSrc
```

### **Enable TET Output** — Enable output TET data `off` (default) | `on`

When enabled, the CPU overload data is output for display in the TET monitor and the
Simulation Data Inspector.

#### Programmatic Use

```
TETFlag
```

## Libraries

Simulink Real-Time / Target Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Select CPU overload options

The SLRT Overload Options block configures CPU overload options for the
model rate identified through the TID port. This block outputs the current CPU overload count
for the identified rate. If the **Enable TET Output** parameter is
`on`, the block outputs TET data that you can mark for data logging in the
Simulation Data Inspector.

The SLRT Overload Options block may include an optional TET output you can mark for logging in the Simulation Data Inspector.
