---
type: simulink-block
title: 'MMF Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sensors'
documentation_page: 'mmfsensor'
documentation_source_path: 'ref/mmfsensor.html'
language: en
---

# MMF Sensor

## Ports
```yaml
ports: []
```

The block has the following ports:

`N`
:   Magnetic conserving port associated with the sensor North terminal.

`S`
:   Magnetic conserving port associated with the sensor South terminal.

The block also has a physical signal output port, which outputs
the value of the mmf.
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

**Introduced in R2010a**

## Description

Ideal magnetomotive force sensor

The MMF Sensor block represents an ideal magnetomotive
force (mmf) sensor, that is, a device that converts the mmf measured
between any magnetic connections into a physical signal proportional
to the mmf.

Connections N and S are conserving magnetic ports through which
the sensor is connected to the circuit. The physical signal port outputs
the value of the mmf.
