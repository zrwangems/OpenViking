---
type: simulink-block
title: 'Log Event'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Logging and Profiling'
documentation_page: 'logevent'
documentation_source_path: 'io_ref/logevent.html'
language: en
---

# Log Event

## Ports

### Input

### **T** — Trigger for log event `1..0`

When the T (trigger input) changes from 0 to 1 (Rising) or from 1 to 0 (Falling),
the block inserts a user-defined simple event defined by the parameters
**Channel**, **Code**, and
**Value** into the execution profiling event stream.

**Example:**  1

## Parameters

### **Channel** — Event channel ID `0` (default) | int

Select the event change ID, for example `500`.

#### Programmatic Use

```
channel
```

### **Code** — Event code number `0` (default) | uint32

Select the event code number, for example `200`.

#### Programmatic Use

```
code
```

### **Value** — Event value number `0` (default) | uint32

Select the event value number, for example `200`.

#### Programmatic Use

```
value
```

### **Trigger type** — Selects trigger signal edge `Rising` (default) | `Falling` | `Either`

Select the type of signal change that triggers the block. When the T (trigger input)
changes from 0 to 1 (Rising) or from 1 to 9 (Falling), the block inserts a user-defined
simple event defined by the parameters **Channel**,
**Code**, and **Value** into the execution profiling
event stream.

#### Programmatic Use

```
trigger
```

## Libraries

Simulink Real-Time / Profiling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Log an execution profiling event

The Log Event block inserts a user-defined event into the execution
profiling event stream when triggered. The user-defined event includes a channel ID, a code
number, and a value number. The channel ID value ranges from 0 to 1023.
