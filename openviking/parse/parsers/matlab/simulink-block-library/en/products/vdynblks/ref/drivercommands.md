---
type: simulink-block
title: 'Driver Commands'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'drivercommands'
documentation_source_path: 'ref/drivercommands.html'
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

### **Steer** — Steer angle scalar

Steer angle, specified as a scalar.

#### Dependencies

To enable this port, set **Vehicle command mode** to
`Open Loop`.

### **Accel** — Vehicle acceleration scalar

Vehicle acceleration, specified as a scalar.

#### Dependencies

To enable this port, set **Vehicle command mode** to
`Open Loop`.

### **Brake** — Vehicle deceleration scalar

Vehicle deceleration, specified as a scalar.

#### Dependencies

To enable this port, set **Vehicle command mode** to
`Open Loop`.

### **Gear** — Vehicle gear scalar

Vehicle gear, specified as a scalar.

#### Dependencies

To enable this port, set **Vehicle command mode** to
`Open Loop`.
### Output

### **Driver** — Command signals `Bus`

Bus containing these steering, acceleration, braking, and gear commands.

| Signal | Description |
| --- | --- |
| `SteerCmd` | Commanded steer angle. |
| `AccelCmd` | Commanded vehicle acceleration. |
| `DecelCmd` | Commanded vehicle deceleration. |
| `GearCmd` | Commanded vehicle gear. |

## Parameters

### **Vehicle command mode** — Enable 3D visualization `Predictive Driver` (default) | `Longitudinal Driver` | `Open Loop`

Specify driver model.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Configure driver

The Driver Commands block implements the driver
model that the reference application uses to generate acceleration, braking, gear, and steering
commands. By default, if you select the Reference Generator block parameter
**Use maneuver-specific driver, initial position, and scene**, the
reference application selects the driver for the maneuver that you specified.

| Vehicle Command Mode Setting | Implementation |
| --- | --- |
| `Longitudinal Driver` | Longitudinal Driver block — Longitudinal speed-tracking controller. Based on reference and feedback velocities, the block generates normalized acceleration and braking commands that can vary from 0 through 1. Use the block to model the dynamic response of a driver or to generate the commands necessary to track a longitudinal drive cycle. |
| `Predictive Driver` (default) | Predictive Driver block — Controller that generates normalized steering, acceleration, and braking commands to track longitudinal velocity and a lateral reference displacement. The normalized commands can vary between -1 to 1. The controller uses a single-track (bicycle) model for optimal single-point preview control. |
| `Open Loop` | Implements an open-loop system so that you can configure the reference application for constant or signal-based steering, acceleration, braking, and gear command input. |
