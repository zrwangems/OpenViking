---
type: simulink-block
title: 'Pressure Transducer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'pressuretransducer'
documentation_source_path: 'ref/pressuretransducer.html'
language: en
---

# Pressure Transducer

## Ports
```yaml
ports:
- name: A
  summary: pressure measurement gas | hydraulic | thermal liquid | moist air | two-phase fluid | isothermal liquid
  direction: conserving
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **A** — pressure measurement gas | hydraulic | thermal liquid | moist air | two-phase fluid | isothermal liquid

Conserving fluid port associated with the pressure measurement. Define
the port type using the **Fluid port type**
parameter.

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal.
## Parameters
```yaml
parameters:
- name: Fluid port type
  summary: Type of fluid port Gas (default) | Hydraulic | Thermal Liquid | Moist Air | Two-Phase Fluid | Isothermal Liquid
  group: ''
- name: Pressure range
  summary: Maximum pressure 1e6 Pa (default) | positive scalar
  group: ''
- name: Operation mode
  summary: Reference point for pressure measurement Absolute (default) | Gauge | Sealed-Gauge
  group: ''
- name: Reference pressure
  summary: Reference pressure 101325 Pa (default) | positive scalar
  group: ''
- name: Full-scale deflection
  summary: Output voltage at full-scale deflection 5 V (default) | positive scalar
  group: ''
- name: Output resistance
  summary: Transducer output resistance 200 Ohm (default) | nonnegative scalar
  group: ''
- name: Dynamics
  summary: Sensor dynamics option No dynamics — Suitable for HIL (default) | Model transducer bandwidth
  group: ''
- name: Bandwidth
  summary: Bandwidth 5 kHz (default) | positive scalar
  group: ''
```

### **Fluid port type** — Type of fluid port `Gas` (default) | `Hydraulic` | `Thermal Liquid` | `Moist Air` | `Two-Phase Fluid` | `Isothermal Liquid`

Type of fluid port. The value defines the domain of the
**A** conserving port.

**Note**

The Hydraulics library will be removed in a future release. Use
the Isothermal Liquid library instead by setting this parameter to
`Isothermal Liquid`.

### **Pressure range** — Maximum pressure `1e6` `Pa` (default) | positive scalar

Maximum pressure in Pa that the sensor can measure.

### **Operation mode** — Reference point for pressure measurement `Absolute` (default) | `Gauge` | `Sealed-Gauge`

Operation mode. Select one of these options to define the reference point
for the pressure measurement:

- `Absolute` — The block
  measures the pressure relative to zero absolute pressure, the
  pressure in an ideal vacuum.
- `Gauge` — The block measures
  pressure relative to atmospheric pressure. If you set the
  **Fluid port type** parameter to
  `Hydraulic`, the block assumes that
  the atmospheric pressure is 1 bar. You cannot change the
  atmospheric pressure in a hydraulic network because, in the
  hydraulic domain, the pressure across-variable is gauge
  pressure. When the node has a value of 0 bar, the node is at
  atmospheric pressure so you can not set the atmospheric pressure
  in the network. If you want to change the reference pressure for
  the pressure measurement, set the **Operation
  mode** parameter to
  `Sealed-Gauge`.

  For the other fluid domains, you can set the atmospheric
  pressure in your fluid network because the pressure
  across-variable is absolute pressure. The default value of the
  atmospheric pressure is 0.101325 MPa. Set the atmospheric
  pressure using a block from the Simscape™ Foundation library that corresponds to the option
  you specify for the **Fluid port type**
  parameter:

  - For `Gas`, use a
    Gas Properties
    (G) block.
  - For `Thermal Liquid`, use
    a Thermal Liquid
    Settings (TL) block.
  - For `Moist Air`, use a
    Moist Air Properties (MA)
    block.
  - For `Two-Phase Fluid`,
    use a Two-Phase
    Fluid Properties (2P)
    block.
  - For `Isothermal Liquid`,
    use a Isothermal Liquid Properties (IL)
    block.
- `Sealed-Gauge` — The block
  measures pressure relative to an internal sealed chamber. If you
  select this option, specify the reference point for the pressure
  measurement by setting the **Reference
  pressure** parameter.

### **Reference pressure** — Reference pressure `101325` `Pa` (default) | positive scalar

Reference pressure in the internal sealed chamber.

#### Dependencies

To enable this parameter, set **Operation mode** to
`Sealed-Gauge`.

### **Full-scale deflection** — Output voltage at full-scale deflection `5` `V` (default) | positive scalar

Output voltage when the measured pressure is equal to or greater than the
**Pressure range** parameter value.

### **Output resistance** — Transducer output resistance `200` `Ohm` (default) | nonnegative scalar

Output resistance of the transducer.

### **Dynamics** — Sensor dynamics option `No dynamics — Suitable for HIL` (default) | `Model transducer bandwidth`

Option for modeling sensor dynamics:

- `No dynamics — Suitable for
  HIL` — Do not model sensor dynamics. If
  your sensor bandwidth is high, you need a small simulation time
  step unless you model the sensor with no dynamics. Use this
  option to use a fixed-step solver or generate code for
  hardware-in-the-loop testing.
- `Model transducer bandwidth` —
  Model sensor dynamics with a first-order lag approximation based
  on the **Bandwidth** parameter value. Specify
  the **Measured pressure** initial target to
  control the initial condition for the lag.

### **Bandwidth** — Bandwidth `5` `kHz` (default) | positive scalar

Bandwidth. This parameter determines the value of the sensor lag.

#### Dependencies

To enable this parameter, set **Dynamics** to
`Model transducer bandwidth`.
## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2023b: Measure Pressure of Isothermal Liquids

You can now use the Pressure Transducer block to
measure the pressure in an isothermal liquid network. To measure the pressure at a
node, set the **Fluid port type** parameter to
`Isothermal Liquid` and connect the
**A** port in parallel with the network at that node.

### R2019a: Select Domain Type for Pressure Measurement

Before R2019a, the Pressure Transducer block has a
pneumatic measurement port. Pneumatic blocks are no longer part of the Foundation
library, but they are included in the Simscape product installation as an example custom library. The legacy
Pressure Transducer block, with a pneumatic port,
is now part of this custom library.

You can now use the Gas library for modeling pneumatic systems. Use the latest
version of the Pressure Transducer block with a gas
port.

## Description

Pressure transducer that converts pressure measurement into voltage

The Pressure Transducer block models a generic pressure
transducer that converts a pressure measurement into a voltage. Use the block to measure
pressure in a variety of domains. Specify the domain type using the **Fluid port
type** parameter.

The output voltage is linearly proportional to the pressure. The block outputs zero
volts if the pressure is less than zero. If the input pressure equals the value of the
**Pressure range** parameter, the output voltage is equal to the
**Full-scale deflection** parameter value. For higher pressures,
the output voltage remains at this **Full-scale deflection**
value.

You can choose between vacuum pressure, atmospheric pressure, or sealed-gauge
reference pressure as the reference point for the pressure measurement.

If you set the **Dynamics** parameter to `Model
transducer bandwidth`, the block approximates the sensor dynamics by a
first-order lag. The **Bandwidth** parameter determines the lag. If you
select the `Model transducer bandwidth` option, you must also
specify an initial condition for the lag using the **Measured
pressure** initial target.

To use a fixed-step solver or generate code for hardware-in-the-loop testing, set the
**Dynamics** parameter to `No dynamics —
Suitable for HIL`. If your sensor bandwidth is high, you need a small
simulation time step unless you model the sensor with no dynamics.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

The **Measured pressure** initial target specifies the initial
output for the sensor.
