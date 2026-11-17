---
type: simulink-block
title: 'Peltier Device'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'peltierdevice'
documentation_source_path: 'ref/peltierdevice.html'
language: en
---

# Peltier Device

## Ports
```yaml
ports:
- name: +
  summary: Positive electrical port electrical
  direction: conserving
- name: '-'
  summary: Negative electrical port electrical
  direction: conserving
- name: A
  summary: Thermal port thermal
  direction: conserving
- name: B
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **+** — Positive electrical port electrical

Electrical conserving port associated with the positive terminal.

### **-** — Negative electrical port electrical

Electrical conserving port associated with the negative terminal.

### **A** — Thermal port thermal

Thermal conserving port. When the block acts as a cooling device, a positive
current causes heat to flow from port **A** to port
**B**, cooling port **A** relative to port
**B**.

### **B** — Thermal port thermal

Thermal conserving port.
## Parameters
```yaml
parameters:
- name: Seebeck coefficient
  summary: Thermoelectric sensitivity coefficient 220e-6 V/K (default)
  group: Electrical
- name: Total electrical resistance
  summary: Resistance between the electrical ports 0.02 Ω (default)
  group: Electrical
- name: Thermal conductance
  summary: Conductance between the thermal ports 1.5e-3 W/K (default)
  group: Thermal
```

### Electrical

### **Seebeck coefficient** — Thermoelectric sensitivity coefficient `220e-6` `V/K` (default)

Measure of the magnitude of an induced thermoelectric voltage in response to a
temperature difference across that material.

### **Total electrical resistance** — Resistance between the electrical ports `0.02` `Ω` (default)

Total electrical resistance between the **+** and
**-** ports.

### Thermal

### **Thermal conductance** — Conductance between the thermal ports `1.5e-3` `W/K` (default)

Thermal conductance between the **A** and **B**
ports.
## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Electrothermal cooler or thermoelectric generator

The Peltier Device block represents an electrothermal
cooler or thermoelectric generator that uses the Peltier and Seebeck effects. The block
converters between electrical and thermal energy:

- With no current flowing, if the temperature presented at thermal port
  **B** is greater than the temperature presented at thermal port
  **A**, then there is a positive potential difference measured from the
  positive to the negative electrical port.
- When the block acts as a cooling device, a positive current causes heat to flow from
  port **A** to port **B**, cooling port
  **A** relative to port **B**.

The defining equations are:

QA=αTAI−12I2R+K(TA−TB)QB=−αTBI−12I2R+K(TB−TA)W=VIW+QA+QB=0

where:

- *Q*A is heat flow into port
  **A**.
- *Q*B is heat flow into port
  **B**.
- *T*A is port **A**
  temperature.
- *T*B is port **B**
  temperature.
- *W* is electrical power (positive when flowing into the
  block).
- *V* is potential difference across the **+** and
  **-** ports.
- *I* is electrical current, positive from **+** to
  **-** port.
- *R* is total electrical resistance.
- *α* is Seebeck coefficient.
- *K* is thermal conductance.

Substituting for powers and dividing all terms by current gives the electrical
equation:

V=α(TB−TA)+IR

The block has a logging variable `power_dissipated` (**Dissipated
power**). This variable reports the DC electrical power, that is, the average
electrical power over one AC cycle if you drive the device with an AC source. In terms of
equations it is equal to the instantaneous value of
*I*2*R* and is useful in a
cooling application to indicate the nonproductive portion of the heat flow. In a heating
application, the interpretation of dissipated power is less useful.
