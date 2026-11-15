---
type: simulink-block
title: 'Enable File Log'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Logging and Profiling'
documentation_page: 'enablefilelog'
documentation_source_path: 'io_ref/enablefilelog.html'
language: en
---

# Enable File Log

## Ports

### Input

### **E** — Enable or disable file logging boolean

Provides enable or disable control over File
Log block operation. When the enable input is triggered by a boolean signal
in the model, there are logs created on the target computer. Retention of these logs
depends on the `FileLogMaxRuns` setting.

## Parameters

Not documented in R2025b.

## Libraries

Simulink Real-Time / Logging

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Enable or disable file logging of signals on target computer

The Enable File Log block enables the file logging service on the
Speedgoat® target computer so that File Log blocks in the model start recording data when
the input port value is true. When the input port value is false, the block disables file
logging on the target computer, and the File Log blocks do not record
data.

If a model includes a Enable File
Log block, the `startRecording` function and `stopRecording`
function only control signal streaming, not File Log logging. In this case, the
`start(tg)`
`AutoImportFileLog` option does not import data into the Simulation Data Inspector
when you use the `stopRecording`
function or click the **Stop Recording** button.

For more information about the file logging workflow, see Real-Time Signal Logging and Streaming Basics.
