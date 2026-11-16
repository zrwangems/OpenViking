---
type: simulink-block
title: 'Longitudinal Controller Stanley'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Vehicle Control'
documentation_page: 'longitudinalcontrollerstanley'
documentation_source_path: 'ref/longitudinalcontrollerstanley.html'
language: en
---

# Longitudinal Controller Stanley

## Ports

### Input

### **RefVelocity** — Reference velocity real scalar

Reference velocity, in meters per second, specified as a real scalar.

### **CurrVelocity** — Current velocity real scalar

Current velocity of the vehicle, in meters per second, specified as a real
scalar.

### **Direction** — Driving direction `1` (forward motion) | `-1` (reverse motion)

Driving direction of vehicle, specified as `1` for forward
motion and `-1` for reverse motion.

### **Reset** — Trigger to reset integral of velocity error `0` (hold steady) | nonzero scalar (reset)

Trigger to reset the integral of velocity error,
*e*(*k*), to zero. A value of `0`
holds *e*(*k*) steady. A nonzero value resets
*e*(*k*).
### Output

### **AccelCmd** — Acceleration command real scalar in the range [0, *M*A]

Acceleration command, returned as a real scalar in the range [0,
*M*A], where
*M*A is the value of the **Maximum
longitudinal acceleration (m/s^2)** parameter.

### **DecelCmd** — Deceleration command real scalar in the range [0, *M*D]

Deceleration command, returned as a real scalar in the range [0,
*M*D], where
*M*D is the value of the **Maximum
longitudinal deceleration (m/s^2)** parameter.

## Parameters

### **Proportional gain, Kp** — Proportional gain `2.5` (default) | positive real scalar

Proportional gain of controller, *K*p,
specified as a positive real scalar.

### **Integral gain, Ki** — Integral gain `1` (default) | positive real scalar

Integral gain of controller, *K*i,
specified as a positive real scalar.

### **Sample time (s)** — Sample time `0.05` (default) | positive real scalar

Sample time of controller, in seconds, specified as a positive real scalar.

### **Maximum longitudinal acceleration (m/s^2)** — Maximum longitudinal acceleration `3` (default) | positive real scalar

Maximum longitudinal acceleration, in meters per second squared, specified as a
positive real scalar.

The block saturates the output from the **AccelCmd** to the range
[0, *M*A], where
*M*A is the value of this parameter. Values
above *M*A are set to
*M*A.

### **Maximum longitudinal deceleration (m/s^2)** — Maximum longitudinal deceleration `6` (default) | positive real scalar

Maximum longitudinal deceleration, in meters per second squared, specified as a
positive real scalar.

The block saturates the output from the **DecelCmd** port to the
range [0, *M*D], where
*M*D is the value of this parameter. Values
above *M*D are set to
*M*D.

## Libraries

Automated Driving Toolbox / Vehicle Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Control longitudinal velocity of vehicle by using Stanley method

The Longitudinal Controller Stanley block computes the acceleration and
deceleration commands, in meters per second, that control the velocity of the vehicle. Specify
the reference velocity, current velocity, and current driving direction. The controller
computes these commands using the Stanley method [1], which the block
implements as a discrete proportional-integral (PI) controller with integral anti-windup. For
more details, see Algorithms.

You can also compute the steering angle command of a vehicle using the Stanley method. See
the Lateral Controller
Stanley block.
