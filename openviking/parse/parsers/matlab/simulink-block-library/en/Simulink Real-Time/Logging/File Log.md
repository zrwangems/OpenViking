---
type: simulink-block
title: 'File Log'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Logging'
documentation_page: 'filelog'
documentation_source_path: 'io_ref/filelog.html'
language: en
---

# File Log

## Ports
```yaml
ports:
- name: S
  summary: Signal data for file log scalar | vector | matrix | array | bus | nonvirtual bus
  direction: input
```

### Input

### **S** — Signal data for file log scalar | vector | matrix | array | bus | nonvirtual bus

Provides the signal data input for the file log.
## Parameters
```yaml
parameters:
- name: Decimation
  summary: Applies decimation to file log data 1 (default) | integer
  group: ''
- name: Input Processing
  summary: Selects processing mode for file log data Elements as channels (sample based) (default) | Columns as channels (frame
    based)
  group: ''
```

### **Decimation** — Applies decimation to file log data `1` (default) | integer

The decimation parameter value selects decimation for the samples captured in the
file log.

By using the File Log decimation functions, subsequent loads of the
real-time application MLDATX file run on the target with the modified decimation value
of the File Log block. These functions are:

- `getAllFileLogBlocks`
- `getFileLogDecimation`
- `setFileLogDecimation`

For more information, see Tune Decimation for File Log Data Without Model Rebuild.

#### Programmatic Use

```
decimation
```

### **Input Processing** — Selects processing mode for file log data `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

The input processing parameter value selects whether the logged signal data is
processed and sent to the Simulation Data Inspector in sample or frame processing mode.
For more information about sample-based data and frame-based data in the Simulation Data
Inspector, see View Simulation Data in Simulation Data Inspector.

#### Programmatic Use

```
inputProcessing
```
## Libraries

Simulink Real-Time / Logging

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2022a: Decimation, Log Retention, and Frame-Based Input

Functions let you get and set decimation values for File Log blocks in a model. Also,
functions let you control when File Log recording starts and stops.

## Description

Write signal data file log on target computer

The File Log block logs the signal at its input port to the Speedgoat® target computer file system when you enable logging service.

For more information about the file logging workflow, see Real-Time Signal Logging and Streaming Basics.
