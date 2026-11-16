---
type: simulink-block
title: 'Thermal Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'thermalresistor'
documentation_source_path: 'ref/thermalresistor.html'
language: en
---

# Thermal Resistor

## Ports

### Conserving

### **H** — Thermal port thermal

Thermal conserving port that provides the resistor temperature.

### **+** — Positive terminal electrical

Electrical conserving port associated with the resistor positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the resistor negative terminal.

## Parameters

### **Nominal resistance** — Resistance at reference temperature `1 Ohm` (default) | positive scalar

The nominal resistance of the thermistor at the reference temperature. Many
datasheets quote the nominal resistance at 25°C (298.15 K) and list it as R25.

### **Reference temperature** — Temperature corresponding to nominal resistance `298.15 K` (default) | positive scalar

The temperature at which the nominal resistance was measured.

### **Temperature coefficient** — Resistance temperature dependency coefficient `5e-05 1/K` (default) | positive scalar

The coefficient *α* in the equation that describes resistance as a
function of temperature.

### **Thermal time constant** — Time constant for thermal equation `10 s` (default) | positive scalar

The time it takes the resistor temperature to reach 63% of the final temperature
change when a step change in ambient temperature occurs.

### **Dissipation factor** — Dissipation coefficient for thermal equation `0.001 W/K` (default) | positive scalar

The thermal power required to raise the thermal resistor temperature by one K.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Resistor with thermal port

The Thermal Resistor block represents a
temperature-dependent resistor. When the temperature at the thermal port is
*T*, the resistance is

R=R0(1+α(T−T0))

where:

- *R*0 is the nominal resistance at the
  reference temperature *T*0.
- *α* is the temperature coefficient.

The following equation describes the thermal behavior of the block:

Q=KdtcdTdt−i2R

where:

- *Q* is the net heat flow into port **H**.
- *K*d is the **Dissipation
  factor** parameter value.
- *t*c is the **Thermal time
  constant** parameter value.
- *dT/dt* is the rate of change of the temperature.
- *i* is the current through the resistor.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

In particular, the **Temperature** variable lets you set a
high-priority target for the temperature of the thermal resistor at the start of the
simulation. The default value is `300` K.
