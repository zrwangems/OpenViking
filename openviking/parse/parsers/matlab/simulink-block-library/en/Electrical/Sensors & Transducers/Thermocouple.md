---
type: simulink-block
title: 'Thermocouple'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'thermocouple'
documentation_source_path: 'ref/thermocouple.html'
language: en
---

# Thermocouple

## Ports
```yaml
ports:
- name: A
  summary: Thermal port thermal
  direction: conserving
- name: +
  summary: Positive port electrical
  direction: conserving
- name: '-'
  summary: Negative port electrical
  direction: conserving
```

### Conserving

### **A** — Thermal port thermal

Thermocouple thermal port.

### **+** — Positive port electrical

Electrical conserving port associated with the thermocouple positive
port.

### **-** — Negative port electrical

Electrical conserving port associated with the thermocouple negative
port.
## Parameters
```yaml
parameters:
- name: Thermocouple type
  summary: Thermocouple type Type B, E, J, K (t<=0 degC), N, R, S or T (default) | Type K (t>=0 degC)
  group: Electrical
- name: Coefficients [c0 c1 ... cn]
  summary: Coefficients [c0 c1 ... cn] [0, 0, 0, 0, 0, 0, 0, 0, 0] (default)
  group: Electrical
- name: Coefficients [a0 a1 a2]
  summary: Coefficients [a0 a1 a2] [0, 0, 0] (default)
  group: Electrical
- name: Reference temperature
  summary: Reference temperature 0 degC (default)
  group: Thermal
- name: Thermal time constant
  summary: Thermal time constant 1 s (default)
  group: Thermal
- name: Dissipation factor
  summary: Dissipation factor 1e-3 W/K (default)
  group: Thermal
- name: Initial temperature
  summary: Initial temperature 25 degC (default)
  group: Thermal
```

### Electrical

### **Thermocouple type** — Thermocouple type `Type B, E, J, K (t<=0 degC), N, R, S or T` (default) | `Type K (t>=0 degC)`

Select one of the modeling options:

- `Type B, E, J, K (t<=0 degC), N, R, S or
  T` — This option is equivalent to
  the block functionality in previous releases.
- `Type K (t>=0 degC)` —
  This option adds an exponential term to the block equations
  when the temperature difference is greater than 0 degrees
  Celsius.

### **Coefficients [c0 c1 ... cn]** — Coefficients [c0 c1 ... cn] `[0, 0, 0, 0, 0, 0, 0, 0, 0]` (default)

Vector of coefficients *c* in the equation that
describes voltage as a function of temperature. The maximum length of
the vector is 15 elements.

**Note**

You can download parameters for standard thermocouple types
from the NIST database [1]. For information on how to do this, see the Simulink®Approximating Nonlinear Relationships: Type S Thermocouple
example.

### **Coefficients [a0 a1 a2]** — Coefficients [a0 a1 a2] `[0, 0, 0]` (default)

Vector of additional coefficients
*a*0,
*a*1, and
*a*2, required only by the
Type K thermocouple.

#### Dependencies

This parameter is visible only when you select `Type
K (t>=0 degC)` for the **Thermocouple
model** parameter.

### Thermal

### **Reference temperature** — Reference temperature `0` `degC` (default)

Temperature the block subtracts from the temperature at the thermal
port in calculating the voltage across the device.

### **Thermal time constant** — Thermal time constant `1` `s` (default)

Time it takes the thermocouple temperature to reach 63% of the final
temperature change when a step change in ambient temperature
occurs.

### **Dissipation factor** — Dissipation factor `1e-3` `W/K` (default)

Thermal power required to raise the thermocouple temperature by one
K.

### **Initial temperature** — Initial temperature `25` `degC` (default)

Temperature of the thermocouple at the start of the simulation.
## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Sensor that converts thermal potential difference into electrical potential difference

The Thermocouple block represents a thermocouple using
the standard polynomial parameterization defined in the NIST ITS-90 Thermocouple
Database [1].

For thermocouples Type B, E, J, K (t<=0 degC), N, R, S or T, the voltage
*E* across the device in mV is

E(mV)=c0+c1t+...+cntn

where:

- *ci* is the *ith*
  element of the **Coefficients [c0 c1 ... cn]** parameter
  value.
- *t* is the temperature difference in degrees Celsius between
  the temperature at the thermal port A and the **Reference
  temperature** parameter value.

**Note**

The equation for voltage across the device as a function of temperature difference
is defined in mV. The units of the voltage across the actual device is V.

For thermocouples Type K (t>=0 degC), the equation contains an additional exponential
term:

E(mV)=c0+c1t+...+cntn+a0ea1(t−a2)2

where *a*0,
*a*1, and
*a*2 are additional coefficients, required
only by the Type K thermocouple, defined by the **Coefficients [a0 a1
a2]** parameter value.

The following equation describes the thermal behavior of the block:

Q=KdtcdTdt

where:

- *T* is the temperature at port A.
- *Q* is the net heat flow into port A.
- *K*d is the **Dissipation
  factor** parameter value.
- *t*c is the **Thermal time
  constant** parameter value.
- *dT/dt* is the rate of change of the temperature.

To model the thermocouple in free space:

1. Connect the thermocouple to the B port of a Simscape™
   Convective Heat Transfer block.
2. Connect the A port of the Convective Heat
   Transfer block to a Simscape
   Ideal Temperature Source block whose temperature
   is set to the ambient temperature.
3. Set the **Area** parameter of the Convective Heat
   Transfer block to an approximate area
   *A*nom.
4. Set the **Heat transfer coefficient** parameter of the
   Convective Heat Transfer block to
   *K*d/*A*nom.
