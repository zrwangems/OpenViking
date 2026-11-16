---
type: simulink-block
title: 'SRM Hysteresis Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control\u200b'
documentation_page: 'srmhysteresiscurrentcontroller'
documentation_source_path: 'ref/srmhysteresiscurrentcontroller.html'
language: en
---

# SRM Hysteresis Current Controller

## Ports

### Input

### **IsRef** — Reference current scalar

Reference current for control.

**Data Types:** `single` | `double`

### **iabc** — Measured current vector

Measured three-phase current.

**Data Types:** `single` | `double`

### **Reset** — Integrator reset scalar

External reset signal (rising edge) for the integrator.

**Data Types:** `Boolean`

### **theta** — Theta-rotor angle scalar

Rotor angle in the interval [0, *β* ].

**Data Types:** `single` | `double`

### **thetaON** — Switch-on angle scalar

Angle for switching on the phase supply.

**Data Types:** `single` | `double`

### **thetaOFF** — Switch-off angle scalar

Angle for switching on the phase supply.

**Data Types:** `single` | `double`
### Output

### **Sabc** — Voltage switch signal vector | `0 or 1`

Signal for switching on and off the three-phase voltage.

**Data Types:** `single` | `double`

## Parameters

### **Torque capability angle (rad)** — Torque capability angle pi/2 (default) | [0, 2\*pi/number of rotor poles]

The torque production capability of one rotor pole, in radians.

### **Hysteresis band (A)** — Hysteresis bandwidth `5` (default)

Hysteresis band, *h*, for the current controller. The
switch-on point is *h*/2 and the switch-off point is
-*h*/2.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / SRM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Hysteresis current control for switched reluctance machines

The SRM Hysteresis Current Controller block implements hysteresis current
control for the Switched Reluctance
Machine (SRM) block.
