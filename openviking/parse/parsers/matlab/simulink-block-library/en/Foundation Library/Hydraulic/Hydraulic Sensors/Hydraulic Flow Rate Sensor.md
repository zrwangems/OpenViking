---
type: simulink-block
title: 'Hydraulic Flow Rate Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sensors'
documentation_page: 'hydraulicflowratesensor'
documentation_source_path: 'ref/hydraulicflowratesensor.html'
language: en
---

# Hydraulic Flow Rate Sensor

## Ports
```yaml
ports: []
```

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the sensor positive probe.

`B`
:   Hydraulic conserving port associated with the sensor negative (reference) probe.

`Q`
:   Physical signal port that outputs the volumetric flow rate value.

`M`
:   Physical signal port that outputs the mass flow rate value.
## Parameters
```yaml
parameters: []
```

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

(To be removed) Ideal flow meter

The Hydraulic Flow Rate Sensor block represents an ideal flow meter, that is,
a device that converts volumetric flow rate through a hydraulic line into a control signal
proportional to this flow rate. Connection Q is a physical signal port that outputs the
volumetric flow rate value. Connection M is a physical signal port that outputs the mass flow
rate value. The sensor is ideal because it does not account for inertia, friction, delays,
pressure loss, and so on.

Connections A and B are conserving hydraulic ports connecting the sensor to the hydraulic
line. The sensor positive direction is from A to B. This means that the flow rate is positive if
it flows from A to B.
