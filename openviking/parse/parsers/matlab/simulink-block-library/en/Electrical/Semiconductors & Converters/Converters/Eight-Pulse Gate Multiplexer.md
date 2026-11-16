---
type: simulink-block
title: 'Eight-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'eightpulsegatemultiplexer'
documentation_source_path: 'ref/eightpulsegatemultiplexer.html'
language: en
---

# Eight-Pulse Gate Multiplexer

## Ports

### Input

### **G1** — Gate-control voltage signal 1, V physical signal

Physical signal port associated with the gate terminal of the first
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G2** — Gate-control voltage signal 2, V physical signal

Physical signal port associated with the gate terminal of the second
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G3** — Gate-control voltage signal 3, V physical signal

Physical signal port associated with the gate terminal of the third
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G4** — Gate-control voltage signal 4, V physical signal

Physical signal port associated with the gate terminal of the fourth
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G5** — Gate-control voltage signal 5, V physical signal

Physical signal port associated with the gate terminal of the fifth
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G6** — Gate-control voltage signal 6, V physical signal

Physical signal port associated with the gate terminal of the sixth
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G7** — Gate-control voltage signal 7, V physical signal

Physical signal port associated with the gate terminal of the seventh
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`

### **G8** — Gate-control voltage signal 8, V physical signal

Physical signal port associated with the gate terminal of the eighth
switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.

**Data Types:** `double`
### Conserving

### **G1** — Gate-control voltage signal 1 electrical

Electrical conserving port associated with the gate terminal of the
first switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **a** — *A*-phase reference point electrical

Electrical conserving port associated with the
*A*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G3** — Gate-control voltage signal 3 electrical

Electrical conserving port associated with the gate terminal of the
third switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **b** — *B*-phase reference point electrical

Electrical conserving port associated with the
*B*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G5** — Gate-control voltage signal 5 electrical

Electrical conserving port associated with the gate terminal of the
fifth switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **c** — *C*-phase reference point electrical

Electrical conserving port associated with the
*C*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G7** — Gate-control voltage signal 7 electrical

Electrical conserving port associated with the gate terminal of the
seventh switching device in a Bidirectional DC-DC Converter
block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **d** — *D*-phase reference point electrical

Electrical conserving port associated with the
*D*-phase for the high-side switching device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G2** — Gate-control voltage signal 2 electrical

Electrical conserving port associated with the gate terminal of the
second switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G4** — Gate-control voltage signal 4 electrical

Electrical conserving port associated with the gate terminal of the
fourth switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G6** — Gate-control voltage signal 6 electrical

Electrical conserving port associated with the gate terminal of the
sixth switching device in a Bidirectional DC-DC Converter block.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G8** — Gate-control voltage signal 8 electrical

Electrical conserving port associated with the gate terminal of the
eighth switching device in a Bidirectional DC-DC Converter block.

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

Whether to expose physical signal or electrical control ports.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Multiplex gate voltage signals to Bidirectional DC-DC Converter block

The Eight-Pulse Gate Multiplexer block routes gate
voltage signals to the eight switching devices in a Bidirectional DC-DC
Converter block. The block multiplexes the eight separate gate
signals into a single vector.

When you set the **Gate-control port** parameter to
`Electrical`, the block exposes conserving ports that
represent electrical reference points. These ports are associated with the individual
phase voltages that connect to the high-side switching devices and the negative DC
voltage common to each low-side switching device in the Bidirectional DC-DC
Converter block.
