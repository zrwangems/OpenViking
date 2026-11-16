---
type: simulink-block
title: 'Twelve-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'twelvepulsegatemultiplexer'
documentation_source_path: 'ref/twelvepulsegatemultiplexer.html'
language: en
---

# Twelve-Pulse Gate Multiplexer

## Ports

### Input

### **Ga(1),Ga(2),Ga(3),Ga(4)** — Ga(1),Ga(2),Ga(3),Ga(4) physical signal

Physical signal ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*a*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

### **Gb(1),Gb(2),Gb(3),Gb(4)** — Gb(1),Gb(2),Gb(3),Gb(4) physical signal

Physical signal ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*b*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

### **Gc(1),Gc(2),Gc(3),Gc(4)** — Gc(1),Gc(2),Gc(3),Gc(4) physical signal

Physical signal ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*c*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.
### Conserving

### **Ga(1),Ga(2),Ga(3),Ga(4)** — Ga(1),Ga(2),Ga(3),Ga(4) electrical

Electrical conserving ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*a*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **Gb(1),Gb(2),Gb(3),Gb(4)** — Gb(1),Gb(2),Gb(3),Gb(4) electrical

Electrical conserving ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*b*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **Gc(1),Gc(2),Gc(3),Gc(4)** — Gc(1),Gc(2),Gc(3),Gc(4) electrical

Electrical conserving ports associated with the gate terminals of the
Three-Level Converter
(Three-Phase)*c*-phase switching
devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G** — G electrical

Vector output port associated with the multiplexed gate signals.
Connect this port to the G port of the Three-Level
Converter (Three-Phase) block.

### **Ka(1),Ka(2),Ka(3),Ka(4)** — Ka(1),Ka(2),Ka(3),Ka(4) electrical

Electrical conserving ports associated with the individual cathode
terminals corresponding to the Three-Level Converter
(Three-Phase) block *a*-phase
switching devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **Kb(1),Kb(2),Kb(3),Kb(4)** — Kb(1),Kb(2),Kb(3),Kb(4) electrical

Electrical conserving ports associated with the individual cathode
terminals corresponding to the Three-Level Converter
(Three-Phase) block *b*-phase
switching devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **Kc(1),Kc(2),Kc(3),Kc(4)** — Kc(1),Kc(2),Kc(3),Kc(4) electrical

Electrical conserving ports associated with the individual cathode
terminals corresponding to the Three-Level Converter
(Three-Phase) block *c*-phase
switching devices.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

## Parameters

### **Gate-control port** — Gate control port `PS` (default) | `Electrical`

Whether to expose PS or electrical control ports.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2021b: Physical and electrical connection ports update

From R2021b forward, to switch between physical and electrical ports, set the
**Gate-control port** parameter to either
`PS` or `Electrical`.

As a result of these changes, inside a model saved in an earlier release, review
the **Gate-control port** parameter of this block.

## Description

Multiplex gate input signals to Three-Level Converter (Three-Phase) block

The Twelve-Pulse Gate Multiplexer block routes gate
voltage signals to the 12 switching devices in a Three-Level Converter (Three-Phase) block. The block multiplexes
the 12 gate signals into a single vector. Gate signals are ordered as
*a*-phase, *b*-phase, and then
*c*-phase, with four gate signals per phase.

When you switch the block inputs to electrical ports, the block shows 12 pairs of
electrical connections, each pair corresponding to the gate and cathode of a switching
device.
