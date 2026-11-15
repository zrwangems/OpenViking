---
type: simulink-block
title: 'Thermistor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'thermistor'
documentation_source_path: 'ref/thermistor.html'
language: en
---

# Thermistor

## Ports

### Conserving

### **A** — Thermal port thermal

Thermal port.

### **+** — Positive port electrical

Electrical conserving port associated with the thermistor positive
port.

### **-** — Negative port electrical

Electrical conserving port associated with the thermistor negative
port.

## Parameters

### Electrical

### **Nominal resistance R0 at reference temperature T0** — Nominal resistance at reference temperature `1000` `Ohm` (default)

Nominal resistance of the thermistor at the reference temperature.
Many datasheets quote the nominal resistance at 25°C and list it as
R25.

### **Characteristic temperature constant B** — Characteristic temperature constant `3500` `K` (default)

Coefficient *B* in the equation that describes
resistance as a function of temperature.

### **Reference temperature T0** — Reference temperature `298.15` `K` (default)

Temperature at which the nominal resistance was measured.

### Thermal

### **Thermal time constant** — Thermal time constant `5.0` `s` (default)

Time it takes the sensor temperature to reach 63% of the final
temperature change when a step change in ambient temperature
occurs.

### **Dissipation factor** — Dissipation factor `0.75e-3` `W/K` (default)

Thermal power required to raise the thermistor temperature by one
K.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Negative temperature coefficient thermistor using B-parameter equation

The Thermistor block represents an NTC thermistor using
the B-parameter equation. The resistance at temperature *T* is

R=R0eB(1/T−1/T0)

where:

- *R0* is the nominal resistance at the
  reference temperature *T0*.
- *B* is the characteristic temperature constant.

The following equation describes the thermal behavior of the block:

Q=KdtcdTdt

where:

- *Q* is the net heat flow into port A.
- *K*d is the **Dissipation
  factor** parameter value.
- *t*c is the **Thermal time
  constant** parameter value.
- *dT/dt* is the rate of change of the temperature.

To model the thermistor in free space:

1. Connect the thermistor to the B port of a Simscape™
   Convective Heat Transfer block.
2. Connect the A port of the Convective Heat Transfer block to a
   Simscape
   Ideal Temperature Source block whose temperature is set to the
   ambient temperature.
3. Set the **Area** parameter of the Convective Heat
   Transfer block to an approximate area
   *A*nom.
4. Set the **Heat transfer coefficient** parameter of the
   Convective Heat Transfer block to
   *K*d/*A*nom.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
