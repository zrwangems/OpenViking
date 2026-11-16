---
type: simulink-block
title: 'Timestamp'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Target Profiling'
documentation_page: 'timestamp'
documentation_source_path: 'ref/timestamp.html'
language: en
---

# Timestamp

## Ports

### Input

### **Signals** — Signals for which to capture timestamps vector

The actual data values are ignored.
### Output

### **Timestamps** — Timestamps of signals vector of double

For each signal connected to `Signals`, the block
returns the signal timestamp measured from the beginning of model
execution.

## Parameters

Not documented in R2025b.

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

Output signal timestamp in Run in Kernel mode

The Timestamp block outputs the timestamp for its input signal. The
timestamp is relative to model start time in **Run in Kernel** mode.
The input signal can be any signal of
any data type.

In **Connected IO** mode, this block does not perform
any action. It outputs zeros.
