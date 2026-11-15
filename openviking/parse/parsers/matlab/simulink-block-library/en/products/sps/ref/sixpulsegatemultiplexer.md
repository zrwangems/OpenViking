---
type: simulink-block
title: 'Six-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Multiplexors'
documentation_page: 'sixpulsegatemultiplexer'
documentation_source_path: 'ref/sixpulsegatemultiplexer.html'
language: en
---

# Six-Pulse Gate Multiplexer

## Ports

### Input

### **Ga(H),Gb(H),Gc(H)** — Ga(H),Gb(H),Gc(H) physical signal

Physical signal ports associated with the gate
terminal of the Converter
(Three-Phase) block high-side
switching devices.

#### Dependencies

To enable this port, set
**Gate-control port** to
`PS`.

### **Ga(L),Gb(L),Gc(L)** — Ga(L),Gb(L),Gc(L) physical signal

Physical signal ports associated with the gate
terminal of the Converter
(Three-Phase) block low-side
switching devices.

#### Dependencies

To enable this port, set
**Gate-control port** to
`PS`.
### Conserving

### **Ga(H),Gb(H),Gc(H)** — Ga(H),Gb(H),Gc(H) electrical

Electrical conserving ports associated with
the gate terminals of the Converter
(Three-Phase) block high-side
switching devices.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

### **Ga(L),Gb(L),Gc(L)** — Ga(L),Gb(L),Gc(L) electrical

Electrical conserving ports associated with
the gate terminals of the Converter
(Three-Phase) block low-side
switching devices.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

### **G** — G electrical

Vector output port associated with the
multiplexed gate signals. Connect this port to the
`G` port of the
Converter
(Three-Phase) block.

### **a** — *A*-phase AC reference point electrical

Electrical conserving port associated with the
*A*-phase for the high-side
switching device of the Converter
(Three-Phase) block.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

### **b** — *B*-phase AC reference point electrical

Electrical conserving port associated with the
*B*-phase for the high-side
switching device of the Converter
(Three-Phase) block.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

### **c** — *C*-phase AC reference point electrical

Electrical conserving port associated with the
*C*-phase for the high-side
switching device of the Converter
(Three-Phase) block.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

### **L** — L electrical

Electrical conserving port associated with the
negative DC voltage common to each low-side
switching device in the Converter
(Three-Phase) block.

#### Dependencies

To enable this port, set
**Gate-control port** to
`Electrical`.

## Parameters

### **Gate-control port** — Gate control port `PS` (default) | `Electrical`

Whether to expose PS or electrical control
ports.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2021b: Physical and electrical connection ports update

From R2021b forward, to switch between physical and electrical ports,
set the **Gate-control port** parameter to either
`PS` or
`Electrical`.

As a result of these changes, inside a model saved in an earlier
release, review the **Gate-control port** parameter
of this block.

## Description

Multiplex gate input signals to Converter block

The Six-Pulse Gate Multiplexer block routes
gate voltage signals to the six switching devices in a
Converter (Three-Phase) block. The
block multiplexes the six separate gate signals into a single vector.

When you switch the block inputs to electrical ports, the block shows
additional electrical reference input ports. The additional electrical
reference ports are associated with the individual phase voltages that
connect to the high-side switching devices in the Converter
(Three-Phase) block and the negative DC voltage
common to each low-side switching device in the Converter
(Three-Phase) block.
