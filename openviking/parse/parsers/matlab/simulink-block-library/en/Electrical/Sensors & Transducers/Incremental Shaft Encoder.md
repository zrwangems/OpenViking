---
type: simulink-block
title: 'Incremental Shaft Encoder'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'incrementalshaftencoder'
documentation_source_path: 'ref/incrementalshaftencoder.html'
language: en
---

# Incremental Shaft Encoder

## Ports

### Conserving

### **R** — Rotational velocity mechanical rotational

Mechanical rotational conserving port associated with the sensor
positive probe.

### **C** — Rotational velocity mechanical rotational

Mechanical rotational conserving port associated with the sensor
negative (reference) probe.

### **A** — Voltage electrical

Encoded electrical output.

### **B** — Voltage electrical

Encoded electrical output.

### **Z** — Index or synchronization electrical

Index, or synchronization, electrical output.

### **Ref** — Voltage electrical

Floating zero-volt reference.

## Parameters

### **Pulses per revolution** — Pulse count `2` (default)

Number of pulses produced on each of the *A* and
*B* phases per revolution of the shaft.

### **Output voltage amplitude** — Voltage `5` `V` (default)

Amplitude of the shaft encoder output voltage when the output is
high.

### **Index pulse offset relative to shaft initial angle** — Position `0` `deg` (default)

Offset of the index pulse *Z* relative to the angle of
the shaft at the start of the simulation. This parameter lets you set the
initial location of the index pulse.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Behavioral model that converts angular position to electrical pulses

The Incremental Shaft Encoder block represents a device
that converts information about the angular position of a shaft into electrical pulses.
The block produces *N* pulses on ports **A** and
**B** per shaft revolution, where *N* is the value
you specify for the **Pulses per revolution** parameter. Pulses
*A* and *B* are 90 degrees out of phase. If the
shaft rotates in a positive direction, then *A* leads
*B*. The block produces a single index pulse on port
**Z** once per revolution. The *Z*-pulse positive
transition always coincides with an *A*- pulse positive transition, and
*Z*- pulse length is equal to the length for the
*A* and *B* pulses. The voltages at ports
**A**, **B**, and **Z** are
defined relative to the **Ref** reference port voltage.

Use this block if you need to model the shaft encoder signals, either to support
development of a decoding algorithm or to include the quantization effects. Otherwise,
use the Ideal Rotational Motion Sensor
block from the Simscape™ Foundation library.

### Assumptions and Limitations

- The Incremental Shaft Encoder block is
  not linearizable. For control design studies that require model
  linearization, use the Ideal Rotational Motion
  Sensor block from the Simscape Foundation library.
