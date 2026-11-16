---
type: simulink-block
title: 'Driver Commands'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'drivercommandsvirtualvehiclemodels'
documentation_source_path: 'ref/drivercommandsvirtualvehiclemodels.html'
language: en
---

# Driver Commands

## Ports

### Input

### **VehRef** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

### **VehFdbk** — Vehicle feedback signals `Bus`

Bus containing vehicle displacement feedback signals.

### **Env** — Environment signals `Bus`

Bus containing environment signals.
### Output

### **Driver** — Command signals `Bus`

Bus containing the commands, including steering, acceleration, braking, and gear
commands.

## Parameters

### **Vehicle command mode** — Enable 3D visualization `Longitudinal Driver` (default) | `Predictive Driver` | `Predictive Stanley Driver` | `Open Loop` | `Dashboard Widgets` | `Game Wheel Hardware` | `No Driver`

Specify driver model.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Configure driver in configured virtual vehicle models and Powertrain Blockset reference applications

The Driver Commands subsystem implements
the driver model that generates acceleration, braking, gear, and steering commands. The
subsystem contains variants that interact with typical driver vehicle inputs, such as
steering, accelerator, decelerator, and transmission commands. These variants include driver
models suitable for both longitudinal and lateral reference tracking, gaming hardware,
interactive canvas widgets, and pass-through or external signal inputs.

| Vehicle Command Mode Setting | Implementation |
| --- | --- |
| `Longitudinal Driver` | Longitudinal Driver block — Longitudinal speed-tracking controller. Based on reference and feedback velocities, the block generates normalized acceleration and braking commands that can vary from 0 through 1. Use the block to model the dynamic response of a driver or to generate the commands necessary to track a longitudinal drive cycle.  **Note**  The `Longitudinal Driver` setting is the only configuration implemented in the Powertrain Blockset™ reference applications. |
| `Predictive Driver` | Predictive Driver (Vehicle Dynamics Blockset) block — Controller that generates normalized steering, acceleration, and braking commands to track longitudinal velocity and a lateral reference displacement. The normalized commands can vary between -1 to 1. The controller uses a single-track (bicycle) model for optimal single-point preview control. |
| `Predictive Stanley Driver` | Predictive Driver (Vehicle Dynamics Blockset) block — Controller that generates normalized steering, acceleration, and braking commands to track longitudinal velocity and a lateral reference displacement. For lateral control, implements the Stanley method. |
| `Open Loop` | Implements an open-loop system so that you can configure the reference application for constant or signal-based steering, acceleration, braking, and gear command input. |
| `Dashboard Widgets` | Implements dashboard widgets for accelerator and brake control. |
| `Game Wheel Hardware` | Implements a game wheel for 3D simulation. Requires Simulink® 3D Animation™. |
| `No Driver` | No driver implemented. |
