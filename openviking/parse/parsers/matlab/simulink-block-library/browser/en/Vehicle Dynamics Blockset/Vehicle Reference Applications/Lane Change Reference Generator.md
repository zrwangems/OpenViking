---
type: simulink-block
title: 'Lane Change Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'lanechangereferencegenerator'
documentation_source_path: 'ref/lanechangereferencegenerator.html'
language: en
---

# Lane Change Reference Generator

## Ports

### Input

### **VehFdbk** — Vehicle feedback `Bus`

Bus containing vehicle feedback signals, including velocity, acceleration, and
steering wheel torque.
### Output

### **Lane** — Lane boundaries `Bus`

Bus containing left, right, and lateral reference lane boundaries.

### **Ref** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral displacement, and steering.

## Parameters

#### Maneuver

### **Steady-state initial conditions** — Start maneuver from steady-state `Initialize from model` (default) | `Solve using block parameters` | `Resume from a workspace variable`

Use the **Steady-state initial conditions** parameter to specify
the steady-state initial conditions for the maneuver. By default, the simulation will
not find or start the simulation at the steady-state operating points.

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

### **Inertial longitudinal position of gate entrance, XGate** — Position `175` (default) | `scalar`

Inertial longitudinal position of gate entrance, in m.

### **Longitudinal entrance velocity setpoint, xdot\_r** — Target velocity `35` (default) | `scalar`

Target velocity.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Initialize from model` or `Solve using block parameters`.

### **Longitudinal entrance velocity setpoint units, xdotUnit** — Units `mph` (default)

Units for target velocity.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Initialize from model` or `Solve using block parameters`.

### **Vehicle width, vehW** — Vehicle width `2` (default) | `scalar`

Vehicle width, in m.

The left and right lane boundaries are a function of the **Vehicle
width** parameter.

### **Lateral offset, latoff** — Lateral offset `scalar`

Lateral offset, in m.

### **Lateral reference position breakpoints, latRefbp** — Breakpoints `scalar`

Lateral reference position breakpoints, in m.

Use the **Lateral reference position breakpoints** and
**Lateral reference data** parameters to specify the lateral
reference trajectory as a function of the longitudinal distance.

### **Lateral reference data, latRef** — Lateral data `scalar`

Use the **Lateral reference position breakpoints** and
**Lateral reference data** parameters to specify the lateral
reference trajectory as a function of the longitudinal distance.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Initialize from model` or `Solve using block parameters`.

#### Steady-State Solver

### **Initial longitudinal position, X\_o** — Initial longitudinal position `175` (default) | `scalar`

Initial vehicle CG position along the earth-fixed *X*-axis, in
m.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

### **Initial lateral position, Y\_o** — Initial lateral position `scalar`

Initial vehicle CG position along the earth-fixed *Y*-axis, in
m.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

### **Initial heading (yaw) angle, psi\_o** — Initial yaw angle `scalar`

Initial vehicle yaw angle about the earth-fixed *Z*-axis, in
rad.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

### **Steady-state solver tolerance, ssTol** — Solver velocity tolerance `scalar`

Steady-state solver velocity tolerance.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

### **Maximum simulated time to reach steady-state, ssMaxTime** — Max time `scalar`

Maximum simulated time to reach steady-state, in s.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

### **Workspace variable name to generate, ssWSName** — Steady-state operating points `scalar`

Name of workspace variable containing steady-state operating points.

#### Dependencies

To enable this parameter, set **Steady-state initial conditions**
to `Solve using block parameters`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Generate double-lane change maneuver reference signals

The Lane Change Reference Generator block sets the parameters that
configure the double-lane change maneuver.

After the vehicle reaches the reference velocity, the block commands a zero acceleration
signal and generates a lateral reference trajectory as a function of the longitudinal
displacement. The block also generates signals indicating the left and right lane boundaries
as a function of the axle width.

Use the **Steady-state initial
conditions** parameter to specify the initial conditions for the maneuver. By
default, the parameter is set to `Initialize from model`, and the
simulation starts with the vehicle at rest at the specified initial position. If you want to
start the simulation at the non-zero steady-state velocity:

1. Set **Steady-state initial conditions** to `Solve using
   block parameters`.
2. On the **Steady-State Solver** tab, specify the initial conditions,
   workspace variable, and solver settings. Click **Generate steady state
   solution**.
3. After the simulation completes, set **Steady-state initial
   conditions** to `Resume from a workspace
   variable`.
4. Set **Steady-state solution to start from, ssVar** to the workspace
   variable you specified in step 2.
5. Run the simulation.

For an example, see Start Double-Lane Change Maneuver at Target Velocity.
