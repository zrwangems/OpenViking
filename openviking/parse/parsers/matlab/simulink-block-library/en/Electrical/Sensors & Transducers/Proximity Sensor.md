---
type: simulink-block
title: 'Proximity Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'proximitysensor'
documentation_source_path: 'ref/proximitysensor.html'
language: en
---

# Proximity Sensor

## Ports

### Input

### **R** — Radial distance physical signal

Physical signal port associated with the radial distance to the sensor.

### **Z** — Perpendicular distance physical signal

Physical signal port associated with the perpendicular distance to the sensor.
### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the proximity sensor positive voltage.

### **-** — Negative voltage electrical

Electrical conserving port associated with the proximity sensor negative voltage.

## Parameters

### **Vector of radial offset distances R** — Vector of radial offset distances `[-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]` `mm` (default)

Vector of distances from the sensor to the object resolved into a plane tangential to the
sensor head.

### **Corresponding sensing distances Z** — Corresponding sensing distances `[0, 0, 5, 8, 9.5, 10, 9.5, 8, 5, 0, 0]` `mm` (default)

Vector of distances from the sensor to the object resolved with respect to a normal
vector at the sensor head.

### **Output when not detected** — Output when not detected `Normally Open (N.O.)` (default) | `Normally Closed (N.C.)`

Indicates whether the output is `Normally Open (N.O.)`, meaning the
output becomes closed only when the object is detected, or `Normally Closed
(N.C.)`, meaning the output becomes open only when the object is detected.

### **Closed resistance R\_closed** — Closed resistance `0.01` `Ohm` (default)

Resistance between the + and - ports when the output contacts are closed.

### **Open conductance G\_open** — Open conductance `1e-8` `1/Ohm` (default)

Conductance between the + and - ports when the output contacts are open.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Ideal behavioral model of simple distance sensor

The Proximity Sensor block represents a simple proximity
sensor. The sensing distance *Z* is defined as the distance normal to the
sensor surface at which the sensor detects an object for a given radial offset
*R*, as shown in the following figure.

This figure shows a typical sensing distance curve:

The sensor switches to detect the object if the **R** and
**Z** inputs are below the sensing curve, in the detection zone.

The output is modeled by an electrical switch which can either be Normally Open (N.O.) or
Normally Closed (N.C.) when no object is detected.
