---
type: simulink-block
title: 'Execution Time'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Target Profiling'
documentation_page: 'executiontime'
documentation_source_path: 'ref/executiontime.html'
language: en
---

# Execution Time

## Ports

### Output

### **Total Exec Time** — Total execution time for the previous base rate tick double

Presents the total execution time as of the previous sample
time.

### **Task Exec Time** — Task execution times for individual sample rates (optional) vector of double

Presents the task execution times for individual sample rates
in a multitasking model as of the previous sample time.

#### Dependency

When you select **Measure task execution times**,
this port is visible.

## Parameters

### **Measure task execution times** — Show task execution times for individual tasks `‘off’` (default) | `‘on’`

Makes visible the port `Task Exec Time`, which
presents the task execution times for individual sample rates in a
multitasking model as of the previous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowTaskTimes` |

## Libraries

Simulink Desktop Real-Time / Target Profiling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink®
Desktop Real-Time™ block ports appear with labels.

## Description

Output total execution time in Run in Kernel mode

The Execution Time block outputs the execution time in **Run in
Kernel** mode.

In **Connected IO** mode, this block does not perform
any action. It outputs zeros.
