---
type: simulink-block
title: 'Slowing Increasing Steer Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'slowlyincreasingsteerreferencegenerator'
documentation_source_path: 'ref/slowlyincreasingsteerreferencegenerator.html'
language: en
---

# Slowing Increasing Steer Reference Generator

## Ports

### Input

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.
### Output

### **Ref** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral displacement, and steering.

## Parameters

#### Maneuver

### **Steady-state solver mode** — Start maneuver from steady-state `Initialize from model` (default) | `Solve using block parameters` | `Resume from a workspace variable`

Use the **Steady-state solver mode** parameter to specify the
steady-state initial conditions for the maneuver. By default, the simulation will not
find or start the simulation at the steady-state operating points.

| Setting | Description |
| --- | --- |
| `Initialize from model` | Simulation starts maneuver at the simulation start time specified by **Maneuver start time, t\_start** at longitudinal velocity of 0. |
| `Solve using block parameters` | Simulation *finds* the steady-state operating points using the parameters on the **Steady-State Solver**  tab. |
| `Resume from a workspace variable` | Simulation *starts* at the steady-state operating points workspace variable specified by **Steady-state solution to start from, ssVar**. |

### **Steady-state solution to start from, ssVar** — Workspace variable with steady-state operating points `char`

Workspace variable containing the steady-state operating points.

#### Dependencies

To enable this parameter, set **Steady-state solver mode** to
`Resume from a workspace variable`.

### **Maneuver start time, t\_start** — Start time `scalar`

Maneuver start time, in s.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Initialize from model`.

### **Longitudinal speed setpoint, xdot\_r** — Target velocity `50` (default) | `scalar`

Target velocity.

### **Longitudinal speed setpoint units, xdotUnit** — Units `mph` (default)

Units for target velocity.

### **Handwheel rate, omega\_hw** — Handwheel rate `scalar`

Handwheel rate, in deg/s.

### **Maximum absolute handwheel angle, theta\_max** — Maximum handwheel `scalar`

Maximum handwheel angle, in deg.

### **Steering hold time after max angle reached, t\_stop** — Steering hold `scalar`

Steering hold, in s.

### **Lateral acceleration absolute threshold, ay\_max** — Lateral acceleration `scalar`

Lateral acceleration threshold, in g.

#### Steady-State Solver

### **Initial longitudinal position, X\_o** — Initial longitudinal position `175` (default) | `scalar`

Initial vehicle CG position along the earth-fixed *X*-axis, in m.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

### **Initial lateral position, Y\_o** — Initial lateral position `scalar`

Initial vehicle CG position along the earth-fixed *Y*-axis, in m.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

### **Initial heading (yaw) angle, psi\_o** — Initial yaw angle `scalar`

Initial vehicle yaw angle about the earth-fixed *Z*-axis, in rad.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

### **Steady-state solver tolerance, ssTol** — Solver velocity tolerance `scalar`

Steady-state solver velocity tolerance.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

### **Maximum simulated time to reach steady-state, ssMaxTime** — Max time `scalar`

Maximum simulated time to reach steady-state, in s.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

### **Workspace variable name to generate, ssWSName** — Steady-state operating points `scalar`

Name of workspace variable containing steady-state operating points.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions** to
`Solve using block parameters`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Generate slowly increasing steer maneuver reference signals

The Slowly Increasing Steer Reference Generator block sets the parameters
that configure the slowly increasing steer maneuver.

The block generates steering, accelerator, and brake commands to conduct a linearly
increasing steering maneuver. The steering command begins at the specified rate once the
vehicle reaches the longitudinal velocity setpoint. After the vehicle achieves the maximum
steering angle, the vehicle maintains the steering angle for a desired duration. The block
then reduces the steering angle to zero at the same rate. A longitudinal controller regulates
the vehicle at the prescribed speed throughout the maneuver.

Use the **Steady-state solver mode** parameter
to specify the initial conditions for the maneuver. By default, the parameter is set to
`Initialize from model`, and the simulation starts with the vehicle
at rest at the specified initial position. If you want to start the simulation at the non-zero
steady-state velocity:

1. Set **Steady-state solver mode** to `Solve using
   block parameters`.
2. On the **Steady-State Solver** tab, specify the initial
   conditions, workspace variable, and solver settings. Click **Generate steady
   state solution**.
3. After the simulation completes, set **Steady-state solver mode**
   to `Resume from a workspace variable`.
4. Set **Steady-state solution to start from, ssVar** to the
   workspace variable you specified in step 2.
5. Run the simulation.
