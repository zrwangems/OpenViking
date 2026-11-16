---
type: simulink-block
title: 'Straight Maneuver Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'straightmaneuverreferencegenerator'
documentation_source_path: 'ref/straightmaneuverreferencegenerator.html'
language: en
---

# Straight Maneuver Reference Generator

## Ports

### Input

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.
### Output

### **Ref** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

## Parameters

#### Maneuver Parameters

### **Maneuver start time, t\_start** — Start time `2` (default) | `scalar`

Maneuver start time, in s.

### **Longitudinal acceleration at t\_start, ax** — Longitudinal acceleration `0.5` (default) | `scalar`

Longitudinal acceleration at maneuver start, in g.

### **Longitudinal velocity reference, xdot\_r** — Longitudinal velocity reference, xdot\_r `20` (default) | `scalar`

Longitudinal velocity reference, xdot\_r, in units specified by **Units of
velocity, xdotUnit**.

### **Units of velocity, xdotUnit** — Units `m/s` (default) | `km/h` | `char`

Units of velocity.

### **Brake pedal actuation** — Deceleration trigger `Longitudinal displacement` (default) | `Time`

Method to start deceleration.

Select `Longitudinal displacement` to specify a
displacement to start decelerating the vehicle.

Select `Time` to specify a time to start decelerating the
vehicle.

### **Longitudinal displacement of vehicle CG, x\_brake** — Displacement `200` (default) | `scalar`

Longitudinal displacement of vehicle CG to start deceleration, in m.

#### Dependency

To enable this parameter, set **Brake pedal actuation** to
`Longitudinal displacement`.

### **Brake actuation time, t\_brake** — Time `15` (default) | `scalar`

Time to start deceleration, in s.

#### Dependency

To enable this parameter, set **Brake pedal actuation** to
`Time`.

### **Longitudinal deceleration at t\_brake, ax\_dec** — Deceleration `1` (default) | `scalar`

Longitudinal deceleration at braking time, in g.

### **Transport delay buffer size, BufferSize** — Buffer `4096` (default) | `scalar`

Transport delay buffer size.

### **Select handwheel angle to 0 deg after braking** — Selection `on` (default) | `off`

Set the handwheel angle to 0 after braking.

#### Tracking Parameters

### **Enable fault tracking before braking** — Enable fault tracking `on` (default) | `off`

Select this parameter to enable fault tracking before braking. Use the parameters to
specify fault conditions before braking during a split-mu test. If the vehicle speed,
steering angle, or yaw rate is not within the allowable range before braking, the block
sets a fault condition. The default values represent compliance with ISO
145121.

### **Longitudinal velocity and mean longitudinal velocity, xdot\_rmax** — Maximum velocity tolerance `1` (default) | `scalar`

The longitudinal velocity and mean longitudinal velocity tolerance. If the
longitudinal velocity or mean longitudinal velocity exceeds the allowable range, the
block sets a fault condition.

#### Dependencies

To enable this parameter, on the **Tracking Parameters** tab,
select **Enable fault tracking before braking**.

### **Mean longitudinal velocity and longitudinal velocity reference, xdot\_rmean** — Mean velocity tolerance `2` (default) | `scalar`

The mean longitudinal velocity and longitudinal velocity reference tolerance. If the
mean longitudinal velocity or longitudinal velocity exceeds the allowable range, the
block sets a fault condition.

#### Dependencies

To enable this parameter, on the **Tracking Parameters** tab,
select **Enable fault tracking before braking**.

### **Yaw velocity and mean yaw velocity, r\_max** — Yaw velocity tolerance `1` (default) | `scalar`

The yaw velocity and mean yaw velocity tolerance, in deg/s. If the yaw velocity or
mean yaw velocity exceeds the allowable range, the block sets a fault condition.

#### Dependencies

To enable this parameter, on the **Tracking Parameters** tab,
select **Enable fault tracking before braking**.

### **Handwheel angle and mean handwheel angle, hw\_max** — Handwheel angle tolerance `3` (default) | `scalar`

Handwheel angle and mean handwheel angle, in deg. If the handwheel angle or mean
handwheel angle exceeds the allowable range, the block sets a fault condition.

#### Dependencies

To enable this parameter, on the **Tracking Parameters** tab,
select **Enable fault tracking before braking**.

### **Stop simulation when fault occurs** — Select to stop simulation `off` (default) | `on`

Select this parameter to stop the simulation if a fault occurs.

#### Dependencies

To enable this parameter, on the **Tracking Parameters** tab,
select **Enable fault tracking before braking**.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Generate straight maneuver reference signals

The Straight Maneuver Reference Generator block generates accelerator and
brake commands to conduct a straight line maneuver for the Braking Test. The acceleration begins
at the specified rate until the vehicle achieves the longitudinal velocity setpoint. The
vehicle controller maintains the longitudinal velocity setpoint for the specified time or
distance. The controller then decelerates the vehicle.

Use the **Maneuver Parameters** to specify the maneuver start time,
velocity setpoint, acceleration, and deceleration.

Optionally, on the **Tracking Parameters** tab, select **Enable
fault tracking before braking**. Use the parameters to specify fault conditions
before braking during a split-mu test. If the vehicle speed, steering angle, or yaw rate is
not within the allowable range before braking, the block sets a fault condition. The default
values represent compliance with ISO 145121.
