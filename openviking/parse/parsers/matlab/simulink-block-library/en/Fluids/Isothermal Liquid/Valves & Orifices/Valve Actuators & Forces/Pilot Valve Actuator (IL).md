---
type: simulink-block
title: 'Pilot Valve Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'pilotvalveactuatoril'
documentation_source_path: 'ref/pilotvalveactuatoril.html'
language: en
---

# Pilot Valve Actuator (IL)

## Ports
```yaml
ports:
- name: X
  summary: Pressure port *P*X isothermal liquid
  direction: conserving
- name: Y
  summary: Pressure port *P*Y isothermal liquid
  direction: conserving
- name: S
  summary: Piston displacement, m physical signal
  direction: output
```

### Conserving

### **X** — Pressure port *P*X isothermal liquid

Pressure at port **X**. There is no mass flow through
the port.

### **Y** — Pressure port *P*Y isothermal liquid

Pressure at port **Y**. There is no mass flow through
the port.

#### Dependencies

To enable this port, set **Actuator type** to
`Double-acting`.
### Output

### **S** — Piston displacement, m physical signal

Piston displacement, specified as a physical signal. The displacement
sign corresponds to the direction specified in the **Mechanical
orientation** parameter.
## Parameters
```yaml
parameters:
- name: Actuator configuration
  summary: Type of actuator modeled Single-acting (default) | Double-acting
  group: ''
- name: Piston area at port X
  summary: Cross-sectional area of piston rod at port X 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Piston area at port Y
  summary: Cross-sectional area of piston rod at port Y 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Spring preload force
  summary: Force in the neutral position 20 N (default) | scalar
  group: ''
- name: Spring preload force at port X
  summary: Force at port X in the neutral position 20 N (default) | scalar
  group: ''
- name: Spring preload force at port Y
  summary: Force at port Y in the neutral position 20 N (default) | scalar
  group: ''
- name: Spring stiffness
  summary: Stiffness coefficient 15e3 N/m (default) | positive scalar
  group: ''
- name: Spring stiffness at port X
  summary: Stiffness coefficient at port X 15e3 N/m (default) | positive scalar
  group: ''
- name: Spring stiffness at port Y
  summary: Stiffness coefficient at port Y 15e3 N/m (default) | positive scalar
  group: ''
- name: Piston stroke
  summary: Maximum piston travel distance 5e-3 m (default) | positive scalar
  group: ''
- name: Piston stroke from port X
  summary: Maximum piston travel distance at port X 5e-3 m (default) | positive scalar
  group: ''
- name: Piston stroke from port Y
  summary: Maximum piston travel distance at port Y 5e-3 m (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Actuator dynamics
  summary: Whether to account for transients during actuation Off (default) | On
  group: ''
- name: Actuator time constant
  summary: Piston displacement time constant 0.1 s (default) | positive scalar
  group: ''
- name: Mechanical orientation
  summary: Piston displacement direction Pilot pressure at port X causes positive piston displacement (default) | Pilot pressure
    at port X causes negative piston displacement
  group: ''
```

### **Actuator configuration** — Type of actuator modeled `Single-acting` (default) | `Double-acting`

Type of actuator modeled.

### **Piston area at port X** — Cross-sectional area of piston rod at port X `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the piston rod at port
**X**.

### **Piston area at port Y** — Cross-sectional area of piston rod at port Y `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the piston rod at port
**Y**.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Spring preload force** — Force in the neutral position `20 N` (default) | scalar

Force acting against the piston in the neutral position.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Single-acting`.

### **Spring preload force at port X** — Force at port X in the neutral position `20 N` (default) | scalar

Force at port **X** in the neutral position.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Spring preload force at port Y** — Force at port Y in the neutral position `20 N` (default) | scalar

Force at port **Y** in the neutral position.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Spring stiffness** — Stiffness coefficient `15e3 N/m` (default) | positive scalar

Spring stiffness factor. The maximum spring force is determined from the
stiffness, *K*, and the **Spring preload
force**: Fmax=Kxstroke+Fpre,

#### Dependencies

To enable this parameter, set **Actuator type** to
`Single-acting`.

### **Spring stiffness at port X** — Stiffness coefficient at port X `15e3 N/m` (default) | positive scalar

Port **X** spring stiffness. The maximum spring force is
determined from the stiffness, *K*, and the
**Spring preload force at port X**: Fmax=Kxstroke+Fpre,

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Spring stiffness at port Y** — Stiffness coefficient at port Y `15e3 N/m` (default) | positive scalar

Port **Y** spring stiffness. The maximum spring force is
determined from the stiffness, *K*, and the
**Spring preload force at port Y**: Fmax=Kxstroke+Fpre,

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Piston stroke** — Maximum piston travel distance `5e-3 m` (default) | positive scalar

Maximum piston travel distance.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Single-acting`.

### **Piston stroke from port X** — Maximum piston travel distance at port X `5e-3 m` (default) | positive scalar

Maximum piston travel distance at port **X**.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Piston stroke from port Y** — Maximum piston travel distance at port Y `5e-3 m` (default) | positive scalar

Maximum piston travel distance at port **Y**.

#### Dependencies

To enable this parameter, set **Actuator type** to
`Double-acting`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to
the flow response when the valve is in near-open or near-closed positions.
Set this value to a nonzero value less than one to increase the stability of
your simulation in these regimes.

### **Actuator dynamics** — Whether to account for transients during actuation `Off` (default) | `On`

Whether to account for transient effects in the spool position due to
actuation. Setting **Actuator dynamics** to
`On` approximates actuator motion by introducing a
first-order lag in the spool position. The **Actuator time
constant** also impacts the modeled dynamics.

### **Actuator time constant** — Piston displacement time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the piston to reach
steady-state when moving from one position to another. This parameter
impacts the modeled actuator dynamics.

#### Dependencies

To enable this parameter, set **Actuator dynamics**
to `On`.

### **Mechanical orientation** — Piston displacement direction `Pilot pressure at port X causes positive piston displacement` (default) | `Pilot pressure at port X causes negative piston displacement`

Sets the piston displacement direction based on the configuration at port
**X**. If **Actuator configuration**
is set to `Double-acting`, the displacement force
at port **Y** acts in the opposite direction of the force
at port **X**. `Pilot pressure at port X causes
positive piston displacement` corresponds to positive
displacement when the pressure at **X** pushes the piston
towards port **Y**. `Pilot pressure at port X
causes negative piston displacement` corresponds to
negative displacement when the pressure at **X** pushes the
piston towards port **Y**.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Single-acting or double-acting actuator controlled by a pilot pressure in an isothermal liquid network

The Pilot Valve Actuator (IL) block models a single-acting or double-acting actuator
controlled by a pilot pressure for control of a connected valve or orifice in an
isothermal liquid network.

For the single-acting actuator, when the control pressure,
*P*X –
*P*atm, exceeds the **Spring preload
force at port X**, the piston begins to actuate in the direction assigned
by the **Mechanical orientation** parameter.

For the double-acting actuator, the control pressure
*P*control is the difference between
*P*X –
*P*atm and
*P*Y –
*P*atm. The piston actuates in the direction
of the larger applied pressure differential, opposing the spring force at the opposite
port. When the piston motion reverses, this spring does not extend and does not exert a
counterbalancing force on the piston position.

The pistons at port **X** and port **Y** are
attached to a single spool. Both springs restore the spool to its neutral position when
*F*spool falls below the opposing spring
preload force. For single-acting actuators, the neutral position is at port
**X**. For double-acting actuators, the neutral position is at the
center of the actuator.

### Single-Acting Actuator

The force on the piston is created by the pressure differential between port
**X** and atmospheric pressure:

Fspool=(pX−patm)AX,

where *A*X is the
**Piston area at port X**. When
*F*spool is greater than the
**Spring preload force at port X**, the piston begins to
move.

**Schematic of a Single-Acting Actuator**

**Piston Displacement**

The instantaneous piston displacement is calculated as:

x˙dyn=xsteady−xdynτ,

where the steady piston position,
*x*steady, is the piston position at
the current pressure differential, proportional to the spring force at maximum
piston stroke:

xsteady=Fxstrokeε=Fspool−FpreFmax−Fprexstrokeε,

where:

- *F*pre is the
  **Spring preload force at port X**.
- *F*max is the maximum
  spring force acting against piston displacement, Fmax=Kxstroke+Fpre, and where *K* is the
  **Spring stiffness at port X**.
- *x*stroke is the
  **Piston stroke from port X**.
- *ε* is the **Mechanical
  orientation**, which indicates piston movement in a
  positive direction (extension) or negative direction (retraction).

If the force on the piston is less than the **Spring
preload force at X**, the piston remains at the neutral position or
moves to the neutral position. If the force on the piston meets or exceeds the
maximum spring force, the piston remains at the stroke until the applied
pressure changes.

### Double-Acting Actuator

The difference between the forces at ports **X** and
**Y** dictates the piston motion:

Fspool=(pX−patm)AX−(pY−patm)AY.

The pressure applied at port **X** shifts the
spool away from the chamber at **X** and opposes the spring at port
**Y**. Similarly, the pressure applied at port
**Y** shifts the spool away from the chamber at
**Y** and opposes the spring at port **X**.
When the spool reverses direction, the formerly extended spring compresses, exerting
a force on the spool. The formerly compressed spring, the spring at the port in the
direction of motion, does not extend and does not influence the spool
position.

**Schematic of a Double-Acting Actuator**

**Piston Displacement**

The piston displacement is calculated as:

x˙dyn=xsteady−xdynτ,

where the steady piston position,
*x*steady, is the piston position at
the current pressure differential, proportional to the spring force at maximum
piston stroke:

xsteady=(FYxstroke,Y−FXxstroke,X)ε=(Fspool−Fpre,YFmax,Y−Fpre,Yxstroke,Y−(−Fspool−Fpre,X)Fmax,X−Fpre,Xxstroke,X)ε,

where:

- *F*pre,X and
  *F*pre,Y are the
  **Spring preload force at port X** and
  **Spring preload force at port Y**,
  respectively.
- *F*max,X and
  *F*max,Y are the maximum
  spring forces acting against piston displacement at ports
  **X** and **Y**, respectively,
  where:

  Fmax=Kxstroke+Fpre,

  *K* is the spring stiffness per port.
- *x*stroke is the piston
  stroke per port.
- *ε* is the **Mechanical
  orientation**, which assigns the signal for piston
  movement as positive (extension) or negative (retraction).

If the force on the piston is less than the respective port
spring preload force, the piston remains or returns to the neutral position. If
the force on the piston meets or exceeds the maximum spring force for the
respective port, the piston remains at the piston stroke until the applied
pressure changes.

### Numerically-Smoothed Force

When the actuator is close to full extension or full retraction, you can maintain numerical
robustness in your simulation by adjusting the block **Smoothing
factor**. With a nonzero smoothing factor, a smoothing function is
applied to all calculated forces, but primarily influences the simulation at the
extremes of the piston motion.

When **Actuator configuration** is set to
`Single-acting`, the normalized force on the piston is
calculated as:

F^X=Fspool−FPreFmax−FPre.

When **Actuator configuration** is set to
`Double-acting`, the normalized force on the piston at
**X** is calculated as:

F^X=−Fspool−FPre,XFmax,X−FPre,X.

and the normalized force at **Y** is calculated as:

F^Y=Fspool−FPre,YFmax,Y−FPre,Y.

When the **Smoothing factor** is nonzero, the block smoothes each
normalized force between `0` and `1`.

For more information, see Numerical Smoothing.
