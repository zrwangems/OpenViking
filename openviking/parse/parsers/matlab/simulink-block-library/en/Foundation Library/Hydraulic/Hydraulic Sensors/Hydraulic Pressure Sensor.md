---
type: simulink-block
title: 'Hydraulic Pressure Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sensors'
documentation_page: 'hydraulicpressuresensor'
documentation_source_path: 'ref/hydraulicpressuresensor.html'
language: en
---

# Hydraulic Pressure Sensor

## Ports

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the sensor positive probe.

`B`
:   Hydraulic conserving port associated with the sensor negative (reference) probe.

`P`
:   Physical signal port that outputs the pressure value.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Ideal pressure sensing device

The Hydraulic Pressure Sensor block represents an ideal hydraulic pressure
sensor, that is, a device that converts hydraulic pressure differential measured between two
points into a control signal proportional to this pressure. The sensor is ideal because it does
not account for inertia, friction, delays, pressure loss, and so on.

Connections A and B are conserving hydraulic ports connecting the sensor to the hydraulic
line. Connection P is a physical signal port that outputs the pressure value. The sensor positive
direction is from A to B. This means that the pressure differential is determined as p=pA−pB.
