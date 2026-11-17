---
type: simulink-block
title: 'Enable Profiler'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Profiling'
documentation_page: 'enableprofiler'
documentation_source_path: 'io_ref/enableprofiler.html'
language: en
---

# Enable Profiler

## Ports
```yaml
ports:
- name: Start
  summary: Starts the profiler 0 | 1
  direction: input
  data_types: Boolean
- name: Stop
  summary: Stops the profiler 0 | 1
  direction: input
  data_types: Boolean
```

### Input

### **Start** — Starts the profiler `0` | `1`

When the `Start` input changes from
`0` to `1`, the block starts the
profiler.

After the resources required to collect the data become available in
the background, the profiler starts collecting data. Profiler
preparation can span several time steps.

**Data Types:** `Boolean`

### **Stop** — Stops the profiler `0` | `1`

When the `Stop` input changes from
`0` to `1`, the block stops the
profiler.

If the profiler is still running when the application stops, the
profiler stops by itself. You do not have to trigger the
`Stop` input.

The amount of data
collected is limited to `1`GB. The profiler stops by itself when it reaches
this limit.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Real-Time / Profiling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Start and stop execution profiler on target computer

The Enable Profiler block detects a rising edge on its
`Start` input and starts the execution profiler on the Speedgoat® target computer. A rising edge on the `Stop` input stops
the execution profiler. A rising edge on both ports has no effect.
