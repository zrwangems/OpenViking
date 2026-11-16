---
type: simulink-block
title: 'Four-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'fourpulsegatemultiplexer'
documentation_source_path: 'ref/fourpulsegatemultiplexer.html'
language: en
---

# Four-Pulse Gate Multiplexer

## Ports

### Input

### **G1** — Gate-control voltage signal 1 physical signal

Physical signal port associated with the gate terminal of the first
switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G2** — Gate-control voltage signal 2 physical signal

Physical signal port associated with the gate terminal of the second
switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G3** — Gate-control voltage signal 3 physical signal

Physical signal port associated with the gate terminal of the third
switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G4** — Gate-control voltage signal 4 physical signal

Physical signal port associated with the gate terminal of the fourth
switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`
### Conserving

### **G1** — Gate-control voltage signal 1 electrical

Electrical conserving port associated with the gate terminal of the
first switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **a** — *A*-phase AC reference point electrical

Electrical conserving port associated with the
*A*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G2** — Gate-control voltage signal 2 electrical

Electrical conserving port associated with the gate terminal of the
second switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **b** — *B*-phase AC reference point electrical

Electrical conserving port associated with the
*B*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G3** — Gate-control voltage signal 3 electrical

Electrical conserving port associated with the gate terminal of the
third switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G4** — Gate-control voltage signal 4 electrical

Electrical conserving port associated with the gate terminal of the
fourth switching device in a connected converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **L** — DC reference point electrical

Electrical conserving port associated with the DC negative connection
for the low-side switching device.

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

**Introduced in R2018a**

### R2021b: Physical and electrical connection ports update

From R2021b forward, to switch between physical and electrical ports, set the
**Gate-control port** parameter to either
`PS` or `Electrical`.

As a result of these changes, inside a model saved in an earlier release, review
the **Gate-control port** parameter of this block.

## Description

Multiplex gate input signals to four quadrant

The Four-Pulse Gate Multiplexer block multiplexes four separate voltage
signals into a single vector. The vectorized signal can control the gates of four
switching devices in a converter, such as a Four-Quadrant
Chopper block.

### Model

This block can model a four-pulse gate multiplexer through either physical signal
ports or electrical ports:

- PS ports — Four-pulse gate multiplexer with physical signal ports. Set
  the **Gate-control port** parameter to
  `PS` to control switching device gates in a
  converter block using Simulink® gate-control voltage signals. To multiplex and
  connect Simulink signals to the gate-control inport of a
  converter block:

  1. Convert each voltage signal using a Simulink-PS
     Converter block.
  2. Multiplex the converted gate signals into a single vector
     using the multiplexer block.
  3. Connect the vector signal to the **G**
     port of the converter.
- Electrical ports — Four-pulse gate multiplexer with electrical
  conserving ports. To control switching device gates in a converter block
  using Simscape™
  Electrical™ Electronics and Mechatronics blocks, set the
  **Gate-control port** parameter to
  `Electrical`. The electrical ports include
  pairs of electrical connections. Each pair corresponds to the gate and
  cathode of a switching device in the connected converter block.
