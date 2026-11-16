---
type: simulink-block
title: 'Flux Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sensors'
documentation_page: 'fluxsensor'
documentation_source_path: 'ref/fluxsensor.html'
language: en
---

# Flux Sensor

## Ports

The block has the following ports:

`N`
:   Magnetic conserving port associated with the sensor North terminal.

`S`
:   Magnetic conserving port associated with the sensor South terminal.

The block also has a physical signal output port, which outputs
the value of the flux.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Ideal flux sensor

The Flux Sensor block represents an ideal flux
sensor, that is, a device that converts flux measured in any magnetic
branch into a physical signal proportional to the flux.

Connections N and S are conserving magnetic ports through which
the sensor is inserted into the circuit. The physical signal port
outputs the value of the flux, which is positive when the flux flows
from the N to the S port.
