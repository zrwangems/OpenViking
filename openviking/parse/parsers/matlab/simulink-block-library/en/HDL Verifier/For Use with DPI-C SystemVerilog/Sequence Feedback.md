---
type: simulink-block
title: 'Sequence Feedback'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with DPI-C SystemVerilog'
documentation_page: 'sequencefeedback'
documentation_source_path: 'ref/sequencefeedback.html'
language: en
---

# Sequence Feedback

## Ports

### Input

### **Port\_1** — Feedback signal from scoreboard subsystem scalar

The Sequence Feedback block accepts an input signal directly from
the scoreboard subsystem.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Feedback signal to sequence subsystem scalar

The Sequence Feedback block outputs a signal directly to the
sequence subsystem.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

Not documented in R2025b.

## Libraries

HDL Verifier / For Use with DPI-C SystemVerilog

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Connect between scoreboard and sequence in UVM testbench model

The Sequence Feedback block promotes a feedback signal from the scoreboard
to the sequence in a UVM testbench model. The block implements a Unit
Delay (Simulink) block with the **Initial condition** parameter set to
`0`.
