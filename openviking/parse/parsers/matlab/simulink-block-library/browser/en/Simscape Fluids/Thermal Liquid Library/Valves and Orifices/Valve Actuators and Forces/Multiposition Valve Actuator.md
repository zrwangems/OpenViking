---
type: simulink-block
title: 'Multiposition Valve Actuator'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Valve Actuators and Forces'
documentation_page: 'multipositionvalveactuator'
documentation_source_path: 'ref/multipositionvalveactuator.html'
language: en
---

# Multiposition Valve Actuator

## Ports

### Input

### **A** — Input signal physical signal

Input port, specified as a physical signal.

When **Actuator positions** is set to `2`,
this port can either control negative or positive actuator movement,
according to the **Actuator travel direction**
setting.

When **Actuator positions** is set to
`3`, this port receives a physical signal
that corresponds to a positive actuator displacement direction.

### **B** — Input signal physical signal

Input port for negative actuator displacement, received as a physical
signal.

#### Dependencies

To enable this port, set **Actuator positions**
to `3`.
### Output

### **S** — Actuator position, m physical signal

Actuator position, in m, specified as a physical signal.

If you use the Multiposition Valve Actuator block with a valve from the Gas Library, the
gas block converts the actuator signal units of m to units of 1.

## Parameters

### **Actuator positions** — Number of valve position signals `2` (default) | `3`

Number of valve position signals. When set to
`2`, the actuator receives one signal and sets one
position signal. When set to `3`, the actuator
receives a positive and a negative signal and sets one position
signal.

### **Push-pin stroke** — Maximum push-pin extension `0.01` m (default) | positive scalar

Maximum push-pin extension.

### **Switching-on time** — Signal transition time period `0.1` s (default) | positive scalar

Time period to reach the value of the **Push-pin stroke** parameter. The
period begins after the input signal rises above 50% of the value of the
**Nominal signal value** parameter.

### **Switching-off time** — Signal transition time period `0.1` s (default) | positive scalar

Time period to return to the **Initial position** parameter from the
**Push-pin stroke** parameter. The period begins after
the input signal falls below 50% of the **Nominal signal
value**.

### **Nominal signal value** — Nominal signal for fully extended actuator `24` (default) | positive scalar

Nominal signal for fully extended actuator. The actuator motion is
triggered when the input signal reaches 50% of the **Nominal signal
value**.

### **Initial position** — Actuator starting position `Retracted` (default) | `Extended` | `Neutral`

Starting position of the actuator. `Retracted`
and `Extended` correspond to the actuator push-pin
stroke limits.

When **Actuator positions** is set to
`2`, the **Initial position**
default is `Retracted`. When **Actuator
positions** is set to `3`, the
**Initial position** default is
`Neutral`. `Neutral`
corresponds to the middle of the **Push-pin
stroke**.

### **Actuator travel direction** — Direction of actuator motion `Positive` (default) | `Negative`

Direction of the actuator motion in response to the physical signal input.
The `Positive` setting corresponds to push-pin
extension.

#### Dependencies

To enable this parameter, set **Actuator positions**
to `2`.

## Libraries

Simscape / Fluids / Valve Actuators Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces / Valve Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Multiposition actuator in any fluid domain

The Multiposition Valve Actuator block models a multiposition actuator in any fluid domain.
You can use it in combination with any valve block that takes a physical signal as
input. The input signal and the switching time affect the actuator position.

### Two-Position Actuator Movement

Actuation begins when the value of the signal at port **A** exceeds 50% of
the value of the **Nominal signal value** parameter. After a time
period that equals one third of the value of the **Switching-on
time** parameter, the actuator begins to move toward the limit
specified by the **Push-pin stroke** parameter.

When the value of the signal at port **A** falls below 50% of the
value of the **Nominal signal value** parameter, the actuator
reverses its direction after a time period that equals one third of the value of the
**Switching-off time** parameter. The motion can be interrupted
mid-stroke.

In the image above, *ton* is the value of the
**Switching-on time** parameter. The actuator motion during
*ton* contains an initial rest, a
quadratic motion, and a linear motion, represented by
*tde*,
*tae*, and
*tve*, respectively.
*tde*,
*tae*, and
*tve* are all equal length.

The actuator switches direction when the control signal is off.
*toff* is the value of the
**Switching-off time** parameter, during which the actuator
repeats the same stages as the switching-on motion.
*tdr* is a stage of rest,
*tar* is a stage of quadratic
motion, and *tvr* is a stage of linear
motion. At the end of *toff*, the actuator
position is at the value of the **Initial position** parameter.
*tdr*,
*tar*, and
*tvr* are all equal length.

When **Actuator positions** is `2`, the
**Actuator travel direction** parameter sets the direction of
the push-pin motion.

The actuator motion can be interrupted at any time. If the push-pin motion is
disrupted mid-stroke, the switch-on and switch-off times are adjusted proportionally
to the push-pin position, relative to the push-pin stroke.

### Three-Position Actuator Movement

When **Actuator positions** is set to
`3`, the signal at port **A** moves
the actuator in a positive direction and the signal received at port
**B** moves the actuator in a negative direction. Only one
signal, from one port, is processed at a time. To switch control between ports
**A** and **B**, or between positive and
negative displacement control, the actuator must first move to a neutral position.
If the push-pin motion is disrupted mid-stroke, the switch-on and switch-off times
are adjusted proportionally to the push-pin position, relative to the push-pin
stroke. The actuator motion can be interrupted at any time.

When controlled by the signal at port **A**, the three-position
actuator has the same displacement profile as the two-position actuator when
**Actuator travel direction** is set to
`Positive`. When controlled by the signal at port
**B**, it has the same profile as the two-position actuator
when **Actuator travel direction** is set to
`Negative`.
