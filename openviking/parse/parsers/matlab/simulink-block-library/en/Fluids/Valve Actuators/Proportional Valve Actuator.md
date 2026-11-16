---
type: simulink-block
title: 'Proportional Valve Actuator'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Valve Actuators'
documentation_page: 'proportionalvalveactuator'
documentation_source_path: 'ref/proportionalvalveactuator.html'
language: en
---

# Proportional Valve Actuator

## Ports

### Input

### **A** — Valve opening signal physical signal

Physical signal that indicates valve opening or closing, specified as
a physical signal. The signal is multiplied by the **Actuator
gain** value.
### Output

### **S** — Valve opening distance, m physical signal

Opening distance for the connected valve, in m, specified as a
physical signal.

If you use the Proportional Valve Actuator block with a valve from the
Gas Library, the gas block converts the actuator signal units of m to
units of 1.

## Parameters

### **Actuator gain** — Input signal multiplier `5e-4 m` (default) | positive scalar

Input signal multiplier for the valve opening distance.

### **Time constant** — Opening signal time constant `0.01 s` (default) | positive scalar

Constant that captures the time required to reach steady-state conditions
during actuation. This parameter impacts the response lag to the valve
opening or closing signal.

### **Valve stroke** — Maximum valve opening distance `0.005 m` (default) | positive scalar

Maximum opening distance of the connected valve.

## Libraries

Simscape / Fluids / Valve Actuators Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces / Valve Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Power-controlled valve actuator in any fluid domain

The Proportional Valve Actuator block models a power-controlled actuator used in conjunction
with a valve block in any fluid domain. You can use it in combination with any valve
block that takes a physical signal as input. The signal to open or close the valve is
received at port **A**. The opening distance for a connected valve is
returned as a physical signal at port **S**.

You can adjust the opening or closing magnitude with the **Actuator gain**
parameter. A first-order lag in time is applied to the actuation distance:

(IG−d)τ,

where:

- *IG* is the signal received at port
  **A** multiplied by the **Actuator
  gain**. Outside of the valve stroke limits,
  *IG* is the **Valve stroke** if fully
  extended and the negative **Valve stroke** if fully
  retracted.
- *d* is the current actuator position.
- *τ* is the **Time constant**.
